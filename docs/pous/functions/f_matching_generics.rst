.. _f_matching_generics:

F_Matching_Generics (Function)
==============================

Checks if 2 generics can be compared to see if they match (same size, same class). Match = TRUE, Not Matching = FALSE.
The exception is strings. If 2 generics are strings they're considered to be matching regardless of size;

**Returns:** ``BOOL``

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``A, B``
     - :ref:`T_Generic <t_generic>`
     -

