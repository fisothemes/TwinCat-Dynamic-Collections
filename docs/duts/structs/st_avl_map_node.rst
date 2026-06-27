.. _st_avl_map_node:

ST_AVL_MAP_NODE (Struct)
========================

Node for an AVL Tree Map.

**Extends:** :ref:`ST_MAP_ENTRY <st_map_entry>`

**Fields**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Height``
     - :ref:`T_Position <t_position>`
     - Height of the node.
   * - ``pParent``
     - ``POINTER TO`` :ref:`ST_AVL_MAP_NODE <st_avl_map_node>`
     - Pointer to parent node.
   * - ``pLeft``
     - ``POINTER TO`` :ref:`ST_AVL_MAP_NODE <st_avl_map_node>`
     - Pointer to left node.
   * - ``pRight``
     - ``POINTER TO`` :ref:`ST_AVL_MAP_NODE <st_avl_map_node>`
     - Pointer to right node.

