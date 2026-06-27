"""
build_docs.py  –  Parse TwinCAT PLC source files and emit Sphinx RST.

Usage:
    python build_docs.py <path/to/Project.plcproj> [--out <docs_dir>]

Reads the .plcproj to determine which files belong to which folder,
then parses each .TcPOU / .TcIO / .TcTLEO / .TcDUT / .TcGVL and writes one .rst per
source file plus index / toctree pages for each folder.
"""

import argparse
import os
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from textwrap import indent, dedent
from collections import defaultdict

# Folders we don't want in the public docs
SKIP_FOLDERS = {"Internal", "Version", "Project Information"}


# ── Helpers ─────────────────────────────────────────────────────────────────

def heading(text, char):
    return f"{text}\n{char * len(text)}\n"


def clean_doc(raw: str) -> str:
    """Strip (* *) delimiters and leading/trailing blank lines."""
    raw = raw.strip()
    raw = re.sub(r'^\(\*\s*', '', raw)
    raw = re.sub(r'\s*\*\)$', '', raw)
    # strip attribute lines
    lines = [l for l in raw.splitlines() if not l.strip().startswith('{attribute')]
    text = "\n".join(lines).strip()
    # :itf:`Name` is a LibDoc custom role — convert to inline code
    text = re.sub(r':itf:`([^`]+)`', r'``\1``', text)
    return text


def rst_safe(name: str) -> str:
    """Make a filesystem-safe name for RST files."""
    return re.sub(r'[^A-Za-z0-9_\-]', '_', name).lower()


def parse_declaration(decl: str):
    """
    Extract the docstring and signature from a CDATA declaration block.

    Accepts both (* ... *) block comments and // line comments that appear
    before the FUNCTION_BLOCK / FUNCTION / TYPE keyword.  Returns
    (docstring, signature_line).
    """
    decl = decl.strip()
    docstring = ""

    # Prefer (* ... *) block comment at the very start
    m = re.match(r'^\(\*(.*?)\*\)\s*', decl, re.DOTALL)
    if m:
        raw_doc = m.group(1).strip()
        raw_doc = re.sub(r':itf:`([^`]+)`', r'``\1``', raw_doc)
        docstring = raw_doc
        decl = decl[m.end():]
    else:
        # Collect consecutive // comment lines before the first keyword line
        lines = decl.splitlines()
        doc_lines = []
        rest_start = 0
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith('//'):
                doc_lines.append(stripped.lstrip('/').strip())
                rest_start = i + 1
            else:
                break
        if doc_lines:
            docstring = "\n".join(doc_lines)
            decl = "\n".join(lines[rest_start:])

    # Convert TwinCAT bold markers (** ... **) to RST strong, then
    # escape any remaining bare * or ** that would break RST inline markup.
    if docstring:
        # (** text **) -> **text** (TwinCAT bold → RST strong)
        docstring = re.sub(r'\(\*\*\s*(.*?)\s*\*\*\)', r'**\1**', docstring, flags=re.DOTALL)
        # Escape standalone * not already part of ** pairs
        # Split on existing ** pairs, escape * in the non-bold parts
        parts = re.split(r'(\*\*[^*]+\*\*)', docstring)
        parts = [re.sub(r'(?<!\*)\*(?!\*)', r'\\*', p) if not p.startswith('**') else p for p in parts]
        docstring = ''.join(parts)

    # Strip attribute lines
    decl_lines = [l for l in decl.splitlines() if not l.strip().startswith('{')]
    signature = "\n".join(decl_lines).strip()
    return docstring, signature


def escape_rst(text: str) -> str:
    """Escape characters that have special meaning in RST inline markup."""
    text = re.sub(r'\*', r'\\*', text)
    text = re.sub(r'`', r'\\`', text)
    return text


# Populated in main() before the write loop; used by link_type().
KNOWN_REFS: set = set()


_TYPE_MODIFIERS = re.compile(
    r'^((?:(?:POINTER\s+TO|REFERENCE\s+TO)\s+)*)'
    r'(ARRAY\s*\[.*?\]\s*OF\s+)*'
    r'(\S+(?:\(\d+\))?)',
    re.IGNORECASE
)


def link_type(typ: str) -> str:
    """
    Render a TwinCAT type expression as RST, hyperlinking the base type
    if it appears in KNOWN_REFS.

    Handles:
      POINTER TO X, REFERENCE TO X
      ARRAY[*] OF X, ARRAY[*] OF ARRAY[*] OF X
      POINTER TO POINTER TO X
      combinations of the above
    """
    if not typ:
        return ''
    m = _TYPE_MODIFIERS.match(typ.strip())
    if not m:
        return f'``{typ}``'
    prefix  = m.group(1) or ''        # POINTER TO / REFERENCE TO chain
    arr     = m.group(2) or ''        # ARRAY[...] OF chain
    base    = m.group(3)              # terminal identifier
    # Normalise whitespace in prefix/array parts for display
    display_pre = re.sub(r'\s+', ' ', (prefix + arr)).strip()
    base_lower  = base.rstrip(';').lower()
    # Strip parameterisation for lookup: STRING(255) -> STRING
    lookup_key  = re.sub(r'\(.*\)', '', base_lower)
    if lookup_key in KNOWN_REFS:
        base_rst = f':ref:`{base} <{base_lower}>`'
    else:
        base_rst = f'``{base}``'
    if display_pre:
        return f'``{display_pre}`` {base_rst}'
    return base_rst


def parse_var_line(line: str):
    """Parse   name : TYPE; // comment   → (name, type, comment)"""
    line = line.strip().rstrip(';')
    comment = ""
    if '//' in line:
        line, comment = line.split('//', 1)
        comment = escape_rst(comment.strip())
    # handle inline assignment e.g.  bInit : BOOL := TRUE
    line = re.sub(r'\s*:=.*$', '', line).strip()
    if ':' in line:
        name, typ = line.split(':', 1)
        return name.strip(), typ.strip().rstrip(';').strip(), comment
    return line.strip(), '', comment


def extract_var_block(decl: str, block_name: str):
    """Extract variables from a named VAR_xxx block."""
    pattern = rf'VAR_{block_name}\s*(.*?)END_VAR'
    m = re.search(pattern, decl, re.DOTALL | re.IGNORECASE)
    if not m:
        return []
    lines = m.group(1).splitlines()
    vars_ = []
    for l in lines:
        l = l.strip()
        if l and not l.startswith('{') and not l.startswith('//'):
            n, t, c = parse_var_line(l)
            if n:
                vars_.append((n, t, c))
    return vars_


def var_table(vars_, caption=""):
    if not vars_:
        return ""
    lines = []
    if caption:
        lines.append(f"**{caption}**\n")
    lines.append(".. list-table::")
    lines.append("   :header-rows: 1")
    lines.append("   :widths: 25 20 55")
    lines.append("")
    lines.append("   * - Name")
    lines.append("     - Type")
    lines.append("     - Description")
    for name, typ, desc in vars_:
        lines.append(f"   * - ``{name}``")
        lines.append(f"     - {link_type(typ)}" if typ else "     -")
        lines.append(f"     - {desc}" if desc else "     -")
    return "\n".join(lines) + "\n"


# ── RST generators ───────────────────────────────────────────────────────────

def _render_var_tables(sig: str, rst: list):
    """
    Append VAR_INPUT, VAR_IN_OUT, and VAR_OUTPUT tables to rst if present in sig.
    Used for functions, FB bodies, and methods.
    """
    inputs   = extract_var_block(sig, 'INPUT')
    in_outs  = extract_var_block(sig, 'IN_OUT')
    outputs  = extract_var_block(sig, 'OUTPUT')
    if inputs:
        rst.append(var_table(inputs, "Inputs") + "\n")
    if in_outs:
        rst.append(var_table(in_outs, "In/Out") + "\n")
    if outputs:
        rst.append(var_table(outputs, "Outputs") + "\n")


def rst_for_pou(name: str, xml_path: Path):
    """
    Generate RST for a .TcPOU file (FB, Function, Program, or GVL).

    Returns None if the POU is marked INTERNAL (so the caller can skip it).
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Could be POU or GVL
    pou = root.find('POU')
    if pou is None:
        gvl = root.find('GVL')
        if gvl is not None:
            return rst_for_gvl(name, gvl)
        return f"{heading(name, '=')}\n*(No content)*\n"

    decl_el = pou.find('Declaration')
    decl_raw = decl_el.text if decl_el is not None else ""
    docstring, signature = parse_declaration(decl_raw)

    # Detect type and INTERNAL modifier from the first keyword line.
    # fn_kind matches any FUNCTION (with or without a return type).
    # fn_ret separately captures the return type when present.
    fb_match   = re.search(r'FUNCTION_BLOCK\s+((?:(?:ABSTRACT|FINAL|INTERNAL)\s+)*)(\S+)', signature)
    fn_kind    = re.search(r'\bFUNCTION\s+((?:(?:INTERNAL)\s+)*)(\S+)', signature)
    fn_ret     = re.search(r'\bFUNCTION\s+(?:(?:INTERNAL)\s+)?\S+\s*:\s*(\S+)', signature)
    prg_match  = re.search(r'\bPROGRAM\s+((?:(?:INTERNAL)\s+)*)(\S+)', signature)

    if fb_match:
        kind = "Function Block"
        modifiers = fb_match.group(1).upper()
    elif fn_kind:
        kind = "Function"
        modifiers = fn_kind.group(1).upper()
    elif prg_match:
        kind = "Program"
        modifiers = prg_match.group(1).upper()
    else:
        kind = "POU"
        modifiers = ""

    # Skip anything marked INTERNAL
    if 'INTERNAL' in modifiers:
        return None

    rst = []
    rst.append(f".. _{name.lower()}:\n")
    rst.append(heading(f"{name} ({kind})", "="))

    if docstring:
        rst.append(docstring + "\n")

    if fn_kind:
        # Return type only when the signature has one; void functions omit the line
        if fn_ret:
            rst.append(f"**Returns:** {link_type(fn_ret.group(1))}\n")
        _render_var_tables(signature, rst)

    if fb_match:
        # Parse EXTENDS and IMPLEMENTS from the first line
        first_line = signature.splitlines()[0] if signature else ""
        ext = re.search(r'\bEXTENDS\s+([\w,\s]+?)(?:\s+IMPLEMENTS|\s*$)', first_line, re.IGNORECASE)
        imp = re.search(r'\bIMPLEMENTS\s+(.+)', first_line, re.IGNORECASE)
        extends_list = [e.strip() for e in ext.group(1).split(',') if e.strip()] if ext else []
        raw_imp = re.sub(r'//.*', '', imp.group(1)) if imp else ''
        implements_list = [i.strip() for i in raw_imp.split(',') if i.strip()]

        if extends_list:
            rst.append(f"**Extends:** {', '.join(link_type(e) for e in extends_list)}\n")
        if implements_list:
            rst.append(f"**Implements:** {', '.join(link_type(i) for i in implements_list)}\n")

        # FB-level VAR_INPUT / VAR_IN_OUT / VAR_OUTPUT (direct inputs to the FB)
        _render_var_tables(signature, rst)

    def _is_internal(decl_text: str) -> bool:
        return bool(re.search(r'\bINTERNAL\b', decl_text.splitlines()[0] if decl_text else '', re.IGNORECASE))

    public_props = [p for p in pou.findall('Property')
                    if not _is_internal(p.findtext('Declaration') or '')]
    public_meths = [m for m in pou.findall('Method')
                    if not _is_internal(m.findtext('Declaration') or '')]

    if public_props:
        rst.append(heading("Properties", "-"))
        for prop in public_props:
            pname = prop.get('Name', '')
            pdecl = prop.find('Declaration')
            pdoc, psig = parse_declaration(pdecl.text if pdecl is not None else "")
            rst.append(f".. _{name.lower()}.{pname.lower()}:\n")
            rst.append(heading(pname, "~"))
            m = re.search(r'PROPERTY\s+\S+\s*:\s*(\S+)', psig)
            if m:
                rst.append(f"Type: {link_type(m.group(1).rstrip(chr(59)).strip())}\n")
            if pdoc:
                rst.append(pdoc + "\n")

    if public_meths:
        rst.append(heading("Methods", "-"))
        for meth in public_meths:
            mname = meth.get('Name', '')
            mdecl = meth.find('Declaration')
            mdoc, msig = parse_declaration(mdecl.text if mdecl is not None else "")
            rst.append(f".. _{name.lower()}.{mname.lower()}:\n")
            rst.append(heading(mname, "~"))
            if mdoc:
                rst.append(mdoc + "\n")
            _render_var_tables(msig, rst)

    return "\n".join(rst)

def _parse_gvl_vars(sig: str) -> list:
    """
    Parse variables from a VAR_GLOBAL block.

    Returns a list of (name, type, default, comment) tuples.
    Standalone // comment lines that precede a group of variables are
    collected as a single blank-name sentinel row so callers can render
    them as section separators in the table.
    """
    body = re.search(r'VAR_GLOBAL[^(]*?(.*?)END_VAR', sig, re.DOTALL | re.IGNORECASE)
    if not body:
        return []

    rows = []
    pending_group = None

    for line in body.group(1).splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith('{'):
            continue
        if stripped.startswith('//'):
            # Group header comment — hold it until we see a real variable
            pending_group = escape_rst(stripped.lstrip("/").strip())
            continue

        # Real variable line
        line_work = stripped.rstrip(';')
        comment = ""
        if '//' in line_work:
            line_work, comment = line_work.split('//', 1)
            comment = escape_rst(comment.strip())

        # Split off default value
        default = ""
        m_default = re.search(r':=\s*(.+)$', line_work)
        if m_default:
            default = m_default.group(1).strip().rstrip(';').strip()
            line_work = line_work[:m_default.start()]

        if ':' not in line_work:
            continue
        vname, vtype = line_work.split(':', 1)
        vname = vname.strip()
        vtype = vtype.strip().rstrip(';').strip()
        if not vname:
            continue

        if pending_group is not None:
            rows.append(('', '', '', pending_group))   # sentinel
            pending_group = None

        rows.append((vname, vtype, default, comment))

    return rows


def _gvl_var_table(rows: list) -> str:
    """Render parsed GVL rows as an RST list-table, with group headers as spanning rows."""
    if not rows:
        return ""
    lines = []
    lines.append(".. list-table::")
    lines.append("   :header-rows: 1")
    lines.append("   :widths: 25 20 20 35")
    lines.append("")
    lines.append("   * - Name")
    lines.append("     - Type")
    lines.append("     - Default")
    lines.append("     - Description")
    for vname, vtype, default, comment in rows:
        if vname == '':
            # Group separator sentinel — emit as a bold label spanning all columns
            lines.append(f"   * - **{comment}**")
            lines.append("     -")
            lines.append("     -")
            lines.append("     -")
        else:
            lines.append(f"   * - ``{vname}``")
            lines.append(f"     - {link_type(vtype)}" if vtype else "     -")
            lines.append(f"     - ``{default}``" if default else "     -")
            lines.append(f"     - {comment}" if comment else "     -")
    return "\n".join(lines) + "\n"


def rst_for_gvl(name: str, gvl_el) -> str:
    """Generate RST for a GVL element (called inline from rst_for_pou or rst_for_gvl_file)."""
    decl_el = gvl_el.find('Declaration')
    decl_raw = decl_el.text if decl_el is not None else ""
    docstring, sig = parse_declaration(decl_raw)

    is_param = gvl_el.get('ParameterList', 'False').lower() == 'true'
    label = "Parameter List" if is_param else "GVL"

    rst = []
    rst.append(f".. _{name.lower()}:\n")
    rst.append(heading(f"{name} ({label})", "="))
    if docstring:
        rst.append(docstring + "\n")
    rows = _parse_gvl_vars(sig)
    if rows:
        rst.append(_gvl_var_table(rows) + "\n")
    return "\n".join(rst)


def rst_for_gvl_file(name: str, xml_path: Path) -> str:
    """Generate RST for a standalone .TcGVL file."""
    tree = ET.parse(xml_path)
    root = tree.getroot()
    gvl_el = root.find('GVL')
    if gvl_el is None:
        return heading(name, "=") + "\n*(No content)*\n"
    return rst_for_gvl(name, gvl_el)


def rst_for_itf(name: str, xml_path: Path):
    """Generate RST for a .TcIO interface file.

    Returns None if the interface is marked INTERNAL.
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()
    itf = root.find('Itf')
    if itf is None:
        return heading(name, "=") + "\n*(No content)*\n"

    decl_el = itf.find('Declaration')
    decl_raw = decl_el.text if decl_el is not None else ""
    docstring, signature = parse_declaration(decl_raw)

    # Check for INTERNAL
    first_line = signature.splitlines()[0] if signature else ""
    if re.search(r'\bINTERNAL\b', first_line, re.IGNORECASE):
        return None

    # Parse EXTENDS from: INTERFACE Name EXTENDS Base1, Base2
    extends_list = []
    ext = re.search(r'\bEXTENDS\s+(.+)', first_line, re.IGNORECASE)
    if ext:
        raw = re.sub(r'//.*', '', ext.group(1))
        extends_list = [e.strip() for e in raw.split(',') if e.strip()]

    def _is_internal(decl_text: str) -> bool:
        return bool(re.search(r'\bINTERNAL\b', decl_text.splitlines()[0] if decl_text else '', re.IGNORECASE))

    rst = []
    rst.append(f".. _{name.lower()}:\n")
    rst.append(heading(f"{name} (Interface)", "="))
    if docstring:
        rst.append(docstring + "\n")
    if extends_list:
        rst.append(f"**Extends:** {', '.join(link_type(e) for e in extends_list)}\n")

    public_props = [p for p in itf.findall('Property')
                    if not _is_internal(p.findtext('Declaration') or '')]
    public_meths = [m for m in itf.findall('Method')
                    if not _is_internal(m.findtext('Declaration') or '')]

    if public_props:
        rst.append(heading("Properties", "-"))
        for prop in public_props:
            pname = prop.get('Name', '')
            pdecl = prop.find('Declaration')
            pdoc, psig = parse_declaration(pdecl.text if pdecl is not None else "")
            rst.append(f".. _{name.lower()}.{pname.lower()}:\n")
            rst.append(heading(pname, "~"))
            m = re.search(r'PROPERTY\s+\S+\s*:\s*(\S+)', psig)
            if m:
                rst.append(f"Type: {link_type(m.group(1).rstrip(chr(59)).strip())}\n")
            if pdoc:
                rst.append(pdoc + "\n")

    if public_meths:
        rst.append(heading("Methods", "-"))
        for meth in public_meths:
            mname = meth.get('Name', '')
            mdecl = meth.find('Declaration')
            mdoc, msig = parse_declaration(mdecl.text if mdecl is not None else "")
            # Return type: METHOD Name : ReturnType
            ret_m = re.search(r'\bMETHOD\s+\S+\s*:\s*(\S+)', msig)
            rst.append(f".. _{name.lower()}.{mname.lower()}:\n")
            rst.append(heading(mname, "~"))
            if ret_m:
                rst.append(f"**Returns:** {link_type(ret_m.group(1))}\n")
            if mdoc:
                rst.append(mdoc + "\n")
            _render_var_tables(msig, rst)

    return "\n".join(rst)


def _parse_enum_members(sig: str) -> list:
    """
    Parse (name, value, comment) tuples from a TYPE ... : ( ... )BASE; block.

    Handles both explicit assignments (In_Order := 0) and implicit ones
    (Pre_Order), incrementing the counter from the last explicit value.
    """
    members = []
    type_block = re.search(r'TYPE\s+\S+\s*:\s*\(\s*(.*?)\s*\)\w*;', sig, re.DOTALL)
    if not type_block:
        return members
    counter = 0
    for line in type_block.group(1).splitlines():
        line = line.strip().rstrip(',')
        if not line or line.startswith('//'):
            continue
        comment = ""
        if '//' in line:
            line, comment = line.split('//', 1)
            comment = escape_rst(comment.strip())
        line = line.strip()
        m_explicit = re.match(r'(\w+)\s*:=\s*(-?\d+)', line)
        m_implicit = re.match(r'(\w+)$', line)
        if m_explicit:
            counter = int(m_explicit.group(2))
            members.append((m_explicit.group(1), str(counter), comment))
            counter += 1
        elif m_implicit:
            members.append((m_implicit.group(1), str(counter), comment))
            counter += 1
    return members


def _enum_rst_table(members: list) -> list:
    """Return RST list-table lines for an enum members list."""
    lines = []
    lines.append(heading("Members", "-"))
    lines.append(".. list-table::")
    lines.append("   :header-rows: 1")
    lines.append("   :widths: 30 10 60")
    lines.append("")
    lines.append("   * - Name")
    lines.append("     - Value")
    lines.append("     - Description")
    for mname, mval, mdesc in members:
        lines.append(f"   * - ``{mname}``")
        lines.append(f"     - {mval}")
        lines.append(f"     - {mdesc}" if mdesc else "     -")
    lines.append("")
    return lines


def rst_for_enum(name: str, xml_path: Path) -> str:
    """Generate RST for a .TcTLEO enum file."""
    tree = ET.parse(xml_path)
    root = tree.getroot()
    el = root.find('EnumerationTextList')
    if el is None:
        return heading(name, "=") + "\n*(No content)*\n"

    decl_el = el.find('Declaration')
    decl_raw = decl_el.text if decl_el is not None else ""
    docstring, sig = parse_declaration(decl_raw)
    members = _parse_enum_members(sig)

    rst = []
    rst.append(f".. _{name.lower()}:\n")
    rst.append(heading(f"{name} (Enum)", "="))
    if docstring:
        rst.append(docstring + "\n")
    if members:
        rst.extend(_enum_rst_table(members))
    return "\n".join(rst)

def rst_for_dut(name: str, xml_path: Path) -> str:
    """Generate RST for a .TcDUT file (STRUCT, UNION, enum, or type alias)."""
    tree = ET.parse(xml_path)
    root = tree.getroot()
    dut = root.find('DUT')
    if dut is None:
        return heading(name, "=") + "\n*(No content)*\n"

    decl_el = dut.find('Declaration')
    decl_raw = decl_el.text if decl_el is not None else ""
    docstring, sig = parse_declaration(decl_raw)

    # Determine DUT kind from the signature
    if re.search(r'\bSTRUCT\b', sig, re.IGNORECASE):
        return _rst_for_struct(name, docstring, sig)
    if re.search(r'\bUNION\b', sig, re.IGNORECASE):
        return _rst_for_union(name, docstring, sig)
    if re.search(r'TYPE\s+\S+\s*:\s*\(', sig, re.DOTALL):
        return _rst_for_dut_enum(name, docstring, sig)
    # Type alias: TYPE Foo : Bar; END_TYPE
    return _rst_for_alias(name, docstring, sig)


def _extract_fields(sig: str, keyword: str) -> list:
    """Extract (name, type, comment) tuples from a STRUCT or UNION body."""
    fields = []
    body = re.search(rf'\b{keyword}\b(.*?)\bEND_{keyword}\b', sig, re.DOTALL | re.IGNORECASE)
    if body:
        for line in body.group(1).splitlines():
            line = line.strip()
            if not line or line.startswith('{') or line.startswith('//'):
                continue
            n, t, c = parse_var_line(line)
            if n:
                fields.append((n, t, c))
    return fields


def _dut_extends(sig: str) -> str:
    """Return the base type name if the DUT declaration has EXTENDS, else ''."""
    m = re.search(r'\bTYPE\s+\S+\s+EXTENDS\s+(\S+)\s*:', sig, re.IGNORECASE)
    return m.group(1) if m else ''


def _rst_for_struct(name: str, docstring: str, sig: str) -> str:
    """RST for a STRUCT DUT."""
    fields = _extract_fields(sig, 'STRUCT')
    base = _dut_extends(sig)
    rst = []
    rst.append(f".. _{name.lower()}:\n")
    rst.append(heading(f"{name} (Struct)", "="))
    if docstring:
        rst.append(docstring + "\n")
    if base:
        rst.append(f"**Extends:** {link_type(base)}\n")
    if fields:
        rst.append(var_table(fields, "Fields") + "\n")
    return "\n".join(rst)


def _rst_for_union(name: str, docstring: str, sig: str) -> str:
    """RST for a UNION DUT."""
    fields = _extract_fields(sig, 'UNION')
    base = _dut_extends(sig)
    rst = []
    rst.append(f".. _{name.lower()}:\n")
    rst.append(heading(f"{name} (Union)", "="))
    if docstring:
        rst.append(docstring + "\n")
    if base:
        rst.append(f"**Extends:** {link_type(base)}\n")
    if fields:
        rst.append(var_table(fields, "Members") + "\n")
    return "\n".join(rst)


def _rst_for_dut_enum(name: str, docstring: str, sig: str) -> str:
    """RST for an enum defined in a .TcDUT file."""
    members = _parse_enum_members(sig)
    rst = []
    rst.append(f".. _{name.lower()}:\n")
    rst.append(heading(f"{name} (Enum)", "="))
    if docstring:
        rst.append(docstring + "\n")
    if members:
        rst.extend(_enum_rst_table(members))
    return "\n".join(rst)

def _rst_for_alias(name: str, docstring: str, sig: str) -> str:
    """RST for a type alias (TYPE Foo : Bar; END_TYPE)."""
    rst = []
    rst.append(f".. _{name.lower()}:\n")
    rst.append(heading(f"{name} (Type)", "="))
    if docstring:
        rst.append(docstring + "\n")
    m = re.search(r'TYPE\s+\S+\s*:\s*(\S+)\s*;', sig)
    if m:
        rst.append(f"Alias for {link_type(m.group(1))}.\n")
    return "\n".join(rst)


# ── Project metadata from generated files ────────────────────────────────────

def read_project_info(proj_dir: Path) -> dict:
    """
    Extract version, title, and company from the auto-generated TwinCAT files.
    Falls back to defaults if any file is missing.
    """
    info = {"version": "0.0.0", "title": "Library", "company": ""}

    # Version from Global_Version.TcGVL
    gvl_candidates = list(proj_dir.rglob("Global_Version.TcGVL"))
    if gvl_candidates:
        try:
            tree = ET.parse(gvl_candidates[0])
            decl = tree.find('.//Declaration')
            if decl is not None and decl.text:
                m = re.search(r"sVersion\s*:=\s*'([^']+)'", decl.text)
                if m:
                    info["version"] = m.group(1)
        except Exception:
            pass

    # Company and title from F_GetCompany / F_GetTitle implementations
    for fname, key in [("F_GetCompany.TcPOU", "company"), ("F_GetTitle.TcPOU", "title")]:
        candidates = list(proj_dir.rglob(fname))
        if candidates:
            try:
                tree = ET.parse(candidates[0])
                st = tree.find('.//ST')
                if st is not None and st.text:
                    m = re.search(r':=\s*"([^"]+)"', st.text)
                    if m:
                        info[key] = m.group(1)
            except Exception:
                pass

    return info


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Parse TwinCAT PLC source files and emit Sphinx RST."
    )
    parser.add_argument(
        "plcproj",
        metavar="PROJECT.plcproj",
        type=Path,
        help="Path to the .plcproj file (or its containing directory).",
    )
    parser.add_argument(
        "--out",
        metavar="DIR",
        type=Path,
        default=None,
        help="Output directory for RST files (default: <plcproj_dir>/docs).",
    )
    args = parser.parse_args()

    # Accept either the .plcproj file itself or its directory
    plcproj_path = args.plcproj.resolve()
    if plcproj_path.is_dir():
        candidates = list(plcproj_path.glob("*.plcproj"))
        if not candidates:
            sys.exit(f"ERROR: No .plcproj file found in {plcproj_path}")
        PLCPROJ = candidates[0]
        PROJ_DIR = plcproj_path
    else:
        if not plcproj_path.exists():
            sys.exit(f"ERROR: File not found: {plcproj_path}")
        PLCPROJ = plcproj_path
        PROJ_DIR = plcproj_path.parent

    OUT_DIR = (args.out.resolve() if args.out else PROJ_DIR / "docs")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Parse plcproj for folder -> file mapping.
    # folder_key is the full directory path using '/' separators,
    # e.g. "POUs/Function Blocks/Collections/Immutable".
    tree = ET.parse(PLCPROJ)
    root = tree.getroot()

    # folder_files[folder_key] = [(name, xml_path)]
    folder_files = defaultdict(list)

    for compile_el in root.iter('{http://schemas.microsoft.com/developer/msbuild/2003}Compile'):
        inc = compile_el.get('Include', '')
        parts = inc.replace('\\', '/').split('/')
        if len(parts) < 2:
            continue
        if parts[0] in SKIP_FOLDERS:
            continue
        name = parts[-1].rsplit('.', 1)[0]
        folder_key = '/'.join(parts[:-1])   # full directory path, arbitrary depth
        xml_path = PROJ_DIR / inc.replace('\\', '/').replace('/', os.sep)
        folder_files[folder_key].append((name, xml_path))

    # Collect every folder that needs an index.rst, including ancestors that
    # contain no direct files (e.g. "POUs/Function Blocks" only has sub-folders).
    all_folders = set()
    for fk in folder_files:
        segs = fk.split('/')
        for depth in range(1, len(segs) + 1):
            ancestor = '/'.join(segs[:depth])
            if ancestor.split('/')[0] not in SKIP_FOLDERS:
                all_folders.add(ancestor)

    # Pre-pass: determine which names will actually be written so link_type()
    # can generate valid :ref: links. We check INTERNAL at parse time.
    global KNOWN_REFS
    for fk_items in folder_files.values():
        for name, xml_path in fk_items:
            ext = xml_path.suffix.lower()
            try:
                if not xml_path.exists():
                    continue
                tree2 = ET.parse(xml_path)
                r2 = tree2.getroot()
                # For POUs and ITFs, check for INTERNAL in declaration
                for tag in ('POU', 'Itf'):
                    el = r2.find(tag)
                    if el is not None:
                        decl = (el.findtext('Declaration') or '').strip()
                        first = decl.splitlines()[0] if decl else ''
                        if not re.search(r'\bINTERNAL\b', first, re.IGNORECASE):
                            KNOWN_REFS.add(name.lower())
                        break
                else:
                    # DUTs, enums, GVLs — always include
                    KNOWN_REFS.add(name.lower())
            except Exception:
                pass
    print(f'  cross-reference index: {len(KNOWN_REFS)} names')

    # Write each file's RST.
    # written_files[folder_key] = [rst_safe_name, ...] — only files that weren't skipped.
    written_files = defaultdict(list)

    for folder_key, items in folder_files.items():
        folder_out = OUT_DIR.joinpath(*[rst_safe(p) for p in folder_key.split('/')])
        folder_out.mkdir(parents=True, exist_ok=True)

        for name, xml_path in items:
            ext = xml_path.suffix.lower()
            try:
                if ext == '.tcpou':
                    rst = rst_for_pou(name, xml_path)
                elif ext == '.tcio':
                    rst = rst_for_itf(name, xml_path)
                elif ext == '.tctleo':
                    rst = rst_for_enum(name, xml_path)
                elif ext == '.tcdut':
                    rst = rst_for_dut(name, xml_path)
                elif ext == '.tcgvl':
                    rst = rst_for_gvl_file(name, xml_path)
                else:
                    continue
            except Exception as e:
                print(f"  SKIP {name}: {e}")
                continue
            if rst is None:
                print(f"  skip  {name} (INTERNAL)")
                continue

            out_file = folder_out / f"{rst_safe(name)}.rst"
            out_file.write_text(rst, encoding='utf-8')
            written_files[folder_key].append(rst_safe(name))
            print(f"  wrote {out_file.relative_to(OUT_DIR)}")

    # Write index.rst for every folder.
    # Each index lists only its immediate children: direct files, then direct sub-folders.
    for folder_key in sorted(all_folders):
        segs = folder_key.split('/')
        folder_label = segs[-1]
        folder_out = OUT_DIR.joinpath(*[rst_safe(p) for p in segs])
        folder_out.mkdir(parents=True, exist_ok=True)

        direct_files = sorted(written_files.get(folder_key, []))

        # Direct child sub-folders only (exactly one level deeper)
        child_folders = sorted(
            fk for fk in all_folders
            if fk.startswith(folder_key + '/') and fk.count('/') == folder_key.count('/') + 1
        )
        child_labels = [rst_safe(fk.split('/')[-1]) for fk in child_folders]

        idx = heading(folder_label, "=")
        idx += "\n.. toctree::\n   :maxdepth: 1\n\n"
        for f in direct_files:
            idx += f"   {f}\n"
        for cl in child_labels:
            idx += f"   {cl}/index\n"
        (folder_out / "index.rst").write_text(idx, encoding='utf-8')

    # Top-level folder names (for the root toctree)
    top_folders = sorted({fk.split('/')[0] for fk in all_folders})

        # Read project metadata from the auto-generated TwinCAT files
    meta = read_project_info(PROJ_DIR)
    lib_title   = meta["title"]
    lib_version = meta["version"]
    lib_company = meta["company"]
    print(f"  project: {lib_title} v{lib_version} ({lib_company})")

    # Write conf.py so version stays in sync with Global_Version.TcGVL
    conf_lines = [
        f'project   = "{lib_title}"',
        f'author    = "{lib_company}"',
        f'copyright = "2026, {lib_company}"',
        f'version   = "{lib_version}"',
        f'release   = "{lib_version}"',
        '',
        'extensions = ["sphinx.ext.autosectionlabel"]',
        'autosectionlabel_prefix_document = True',
        'suppress_warnings = ["autosectionlabel.*"]',
        '',
        'html_theme = "sphinx_rtd_theme"',
        'html_title = f"{project} v{release}"',
        'html_theme_options = {',
        '    "navigation_depth": -1,',
        '}',
        'html_show_sourcelink = False',
        'html_copy_source = False',
        'highlight_language = "none"',
    ]
    (OUT_DIR / "conf.py").write_text("\n".join(conf_lines) + "\n", encoding="utf-8")

    # Write root index.rst
    title_bar = "=" * len(lib_title)
    toc_entries = "".join(f"   {rst_safe(top)}/index\n" for top in top_folders)
    root_idx = (
        f"{lib_title}\n{title_bar}\n\n"
        "A library of composable building blocks for modelling and building control systems in TwinCAT.\n\n"
        f":Company: {lib_company}\n"
        f":Version: {lib_version}\n\n"
        ".. toctree::\n"
        "   :maxdepth: 2\n"
        "   :caption: Contents\n\n"
        + toc_entries
    )
    (OUT_DIR / "index.rst").write_text(root_idx, encoding="utf-8")
    print(f"\nDone. RST written to {OUT_DIR}")


if __name__ == '__main__':
    main()