.. _fb_tree_set:

FB_Tree_Set (Function Block)
============================

A collection that contains no duplicate items implemented using an iterative AVL Tree.
This data structure was implemented with the help of Max Goren's iterative AVL tree in C++. See Function Block's body for more details.

**Extends:** :ref:`FB_Collection <fb_collection>`

**Implements:** :ref:`I_Tree_Set <i_tree_set>`

Properties
----------

.. _fb_tree_set._traversal:

_Traversal
~~~~~~~~~~

Type: :ref:`T_BST_Traversal <t_bst_traversal>`

Traversal method for retrieving values in the tree set.

Methods
-------

.. _fb_tree_set.balance:

Balance
~~~~~~~

Performs rotation and updates heights until tree is balanced.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``pNode``
     - ``POINTER TO`` :ref:`T_AVL_Node <t_avl_node>`
     -


.. _fb_tree_set.clear:

Clear
~~~~~

Empties/Clears/Deletes every item in the set.

.. _fb_tree_set.clear_node:

Clear_Node
~~~~~~~~~~

Deletes the node and its tree/sub-trees.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``pRoot``
     - ``POINTER TO`` :ref:`T_AVL_Node <t_avl_node>`
     -


.. _fb_tree_set.contains:

Contains
~~~~~~~~

Checks if item is contained in set.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Item``
     - ``ANY``
     - Item to find.


.. _fb_tree_set.create_node:

Create_Node
~~~~~~~~~~~

Creates a new node in dynamic memory with a clone of the generic item as it data.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Item``
     - :ref:`T_Generic <t_generic>`
     -


**Outputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``bSuccess``
     - ``BOOL``
     -
   * - ``Error``
     - :ref:`T_Error <t_error>`
     -


.. _fb_tree_set.delete_node:

Delete_Node
~~~~~~~~~~~

Safety deletes node.
If the node and/or it's value/data is in dynamic memory it/they will be deleted.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``pNode``
     - ``REFERENCE TO POINTER TO`` :ref:`T_AVL_Node <t_avl_node>`
     -


.. _fb_tree_set.fb_exit:

FB_exit
~~~~~~~

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``bInCopyCode``
     - ``BOOL``
     - if TRUE, the exit method is called for exiting an instance that is copied afterwards (online change).


.. _fb_tree_set.find_minimum_node:

Find_Minimum_Node
~~~~~~~~~~~~~~~~~

Finds the node with the smallest item in a tree or sub-tree.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``pNode``
     - ``POINTER TO`` :ref:`T_AVL_Node <t_avl_node>`
     -


.. _fb_tree_set.get_balance:

Get_Balance
~~~~~~~~~~~

Gets the difference between the left and right sub-trees.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``pNode``
     - ``POINTER TO`` :ref:`T_AVL_Node <t_avl_node>`
     -


.. _fb_tree_set.get_height:

Get_Height
~~~~~~~~~~

Safely gets the height of a sub-tree.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``pNode``
     - ``POINTER TO`` :ref:`T_AVL_Node <t_avl_node>`
     -


.. _fb_tree_set.get_values:

Get_Values
~~~~~~~~~~

Gets an immutable list of the values in the set.

.. _fb_tree_set.insert:

Insert
~~~~~~

Insert item into set.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Item``
     - ``ANY``
     - Data to insert


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


.. _fb_tree_set.insert_generic:

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


.. _fb_tree_set.move_node:

Move_Node
~~~~~~~~~

Moves from node at source into the position of the destination.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``pDestination, pSource``
     - ``POINTER TO`` :ref:`T_AVL_Node <t_avl_node>`
     -


.. _fb_tree_set.remove:

Remove
~~~~~~

Removes item from the set.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Item``
     - ``ANY``
     - Data to remove


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


.. _fb_tree_set.remove_generic:

Remove_Generic
~~~~~~~~~~~~~~

Removes generic item from the set.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Item``
     - :ref:`T_Generic <t_generic>`
     - Data to remove


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


.. _fb_tree_set.remove_node:

Remove_Node
~~~~~~~~~~~

Finds and removes a node from a tree/sub-tree and returns the new root of the tree/subtree.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``pNode``
     - ``REFERENCE TO POINTER TO`` :ref:`T_AVL_Node <t_avl_node>`
     -


.. _fb_tree_set.rotate_left:

Rotate_Left
~~~~~~~~~~~

Rotates a tree/sub-tree left.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``pX``
     - ``POINTER TO`` :ref:`T_AVL_Node <t_avl_node>`
     -


.. _fb_tree_set.rotate_right:

Rotate_Right
~~~~~~~~~~~~

Rotates a tree/sub-tree right.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``pX``
     - ``POINTER TO`` :ref:`T_AVL_Node <t_avl_node>`
     -


.. _fb_tree_set.search_node:

Search_Node
~~~~~~~~~~~

Checks if an item is in a tree/ sub-tree.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``pNode``
     - ``POINTER TO`` :ref:`T_AVL_Node <t_avl_node>`
     -
   * - ``Item``
     - :ref:`T_Generic <t_generic>`
     -


.. _fb_tree_set.update_height:

Update_Height
~~~~~~~~~~~~~

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``pNode``
     - ``POINTER TO`` :ref:`T_AVL_Node <t_avl_node>`
     -

