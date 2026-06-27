.. _fb_tree_multiset:

FB_Tree_Multiset (Function Block)
=================================

A collection similiar to a set except it allows for duplicate items. It is implemented using an iterative AVL Tree.
This data structure was implemented with the help of Max Goren's iterative AVL tree in C++. See Function Block's body for more details.

**Extends:** :ref:`FB_Tree_Set <fb_tree_set>`

Methods
-------

.. _fb_tree_multiset.insert_generic:

Insert_Generic
~~~~~~~~~~~~~~

Adds new generic item at into set.
The set will store a copy of the generic item so as to not modify the original value outside it's scope.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Item``
     - :ref:`T_Generic <t_generic>`
     - Item to store


**Outputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``bSuccess``
     - ``BOOL``
     - Indicates whether operation was successful. Success = TRUE, Failure = FALSE

