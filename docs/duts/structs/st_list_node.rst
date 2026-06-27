.. _st_list_node:

ST_LIST_NODE (Struct)
=====================

Node for linked list.

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
   * - ``pPrevious``
     - ``POINTER TO`` :ref:`ST_LIST_NODE <st_list_node>`
     - Pointer to previous node.
   * - ``pNext``
     - ``POINTER TO`` :ref:`ST_LIST_NODE <st_list_node>`
     - Pointer to next node.

