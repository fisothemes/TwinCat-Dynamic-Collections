.. _st_avl_node:

ST_AVL_NODE (Struct)
====================

Node for AVL Tree.

**Fields**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Data``
     - :ref:`T_Generic <t_generic>`
     - Stored data.
   * - ``Height``
     - :ref:`T_Position <t_position>`
     - Height of the node.
   * - ``pParent``
     - ``POINTER TO`` :ref:`ST_AVL_NODE <st_avl_node>`
     - Pointer to parent node.
   * - ``pLeft``
     - ``POINTER TO`` :ref:`ST_AVL_NODE <st_avl_node>`
     - Pointer to left node.
   * - ``pRight``
     - ``POINTER TO`` :ref:`ST_AVL_NODE <st_avl_node>`
     - Pointer to right node.

