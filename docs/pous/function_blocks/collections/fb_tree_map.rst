.. _fb_tree_map:

FB_Tree_Map (Function Block)
============================

A collection of key-value pair items implemented using an iterative AVL Tree.
Keys and values can be retrieved as an immutable list (whose base is FB_ArrayList) via 4 traversal methods; Inorder, Preorder, Postorder and Level Order.
This data structure was implemented with the help of Max Goren's iterative AVL tree in C++. See Function Block's body for more details.

**Extends:** :ref:`FB_Collection <fb_collection>`

**Implements:** :ref:`I_Tree_Map <i_tree_map>`

Properties
----------

.. _fb_tree_map._traversal:

_Traversal
~~~~~~~~~~

Type: :ref:`T_BST_Traversal <t_bst_traversal>`

Traversal method for retrieving keys and values in the tree map set.

Methods
-------

.. _fb_tree_map.balance:

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
     - ``POINTER TO`` :ref:`T_AVL_Map_Node <t_avl_map_node>`
     -


.. _fb_tree_map.clear:

Clear
~~~~~

Empties/Clears/Deletes every item in the map.

.. _fb_tree_map.clear_node:

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
     - ``POINTER TO`` :ref:`T_AVL_Map_Node <t_avl_map_node>`
     -


.. _fb_tree_map.contains:

Contains
~~~~~~~~

Checks if key is contained in the map.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Key``
     - ``ANY``
     - Key to find.


.. _fb_tree_map.create_node:

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
   * - ``Key, Value``
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


.. _fb_tree_map.delete_node:

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
     - ``REFERENCE TO POINTER TO`` :ref:`T_AVL_Map_Node <t_avl_map_node>`
     -


.. _fb_tree_map.fb_exit:

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


.. _fb_tree_map.find_minimum_node:

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
     - ``POINTER TO`` :ref:`T_AVL_Map_Node <t_avl_map_node>`
     -


.. _fb_tree_map.get:

Get
~~~

Gets the value associated with the specified key without removing it from the map.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Key``
     - ``ANY``
     - Key used to identify stored value
   * - ``Value``
     - ``ANY``
     - Variable to store requested data


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


.. _fb_tree_map.get_as_string:

Get_As_String
~~~~~~~~~~~~~

Returns value as a string, if type to string conversion is supported.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Key``
     - ``ANY``
     - Key used to identify stored value
   * - ``sValue``
     - ``REFERENCE TO`` ``STRING``
     - Variable to store returned item.


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


.. _fb_tree_map.get_balance:

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
     - ``POINTER TO`` :ref:`T_AVL_Map_Node <t_avl_map_node>`
     -


.. _fb_tree_map.get_generic:

Get_Generic
~~~~~~~~~~~

Gets the value in its generic form associated with the specified key in its generic form without removing it from the map.
**Use carefully as this contains the pointer of the actual value in the collection.**
If you wish to use this it is recommeded you create a copy of the returned value using MEMMOVE or MEMCPY

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Key``
     - :ref:`T_Generic <t_generic>`
     - Key used to identify stored value


**Outputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Value``
     - :ref:`T_Generic <t_generic>`
     - Variable to store requested data
   * - ``bSuccess``
     - ``BOOL``
     -


.. _fb_tree_map.get_height:

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
     - ``POINTER TO`` :ref:`T_AVL_Map_Node <t_avl_map_node>`
     -


.. _fb_tree_map.get_keys:

Get_Keys
~~~~~~~~

Gets an immutable list of the keys.

.. _fb_tree_map.get_values:

Get_Values
~~~~~~~~~~

Gets an immutable list of the values.

.. _fb_tree_map.insert:

Insert
~~~~~~

Insert an element with the provided key and value to the map.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Key``
     - ``ANY``
     - Key used to identify stored value
   * - ``Value``
     - ``ANY``
     - Value to store in map with key


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


.. _fb_tree_map.insert_generic:

Insert_Generic
~~~~~~~~~~~~~~

Insert an element with the provided key and value in their generic forms to the map.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Key``
     - :ref:`T_Generic <t_generic>`
     - Key used to identify stored value
   * - ``Value``
     - :ref:`T_Generic <t_generic>`
     - Value to store in map with key
   * - ``bUpdate``
     - ``BOOL``
     - If this is true the value will be updated if the key already exists.


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


.. _fb_tree_map.move_node:

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
     - ``POINTER TO`` :ref:`T_AVL_Map_Node <t_avl_map_node>`
     -


.. _fb_tree_map.remove:

Remove
~~~~~~

Removes value with the specified key from the map.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Key``
     - ``ANY``
     - Key used to identify stored value


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


.. _fb_tree_map.remove_generic:

Remove_Generic
~~~~~~~~~~~~~~

Removes value with the specified key in its generic form from the map.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Key``
     - :ref:`T_Generic <t_generic>`
     - Key used to identify stored value


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


.. _fb_tree_map.remove_node:

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
     - ``REFERENCE TO POINTER TO`` :ref:`T_AVL_Map_Node <t_avl_map_node>`
     -


.. _fb_tree_map.rotate_left:

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
     - ``POINTER TO`` :ref:`T_AVL_Map_Node <t_avl_map_node>`
     -


.. _fb_tree_map.rotate_right:

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
     - ``POINTER TO`` :ref:`T_AVL_Map_Node <t_avl_map_node>`
     -


.. _fb_tree_map.search_node:

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
     - ``POINTER TO`` :ref:`T_AVL_Map_Node <t_avl_map_node>`
     -
   * - ``Key``
     - :ref:`T_Generic <t_generic>`
     -


.. _fb_tree_map.update:

Update
~~~~~~

Updates the value at the provided key with the new value in the map.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Key``
     - ``ANY``
     - Key used to identify stored value
   * - ``Value``
     - ``ANY``
     - Value to store in map with key


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


.. _fb_tree_map.update_generic:

Update_Generic
~~~~~~~~~~~~~~

Updates the value at the provided key with the new value in their generic forms in the map.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Key``
     - :ref:`T_Generic <t_generic>`
     - Key used to identify stored value
   * - ``Value``
     - :ref:`T_Generic <t_generic>`
     - Value to store in map with key


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


.. _fb_tree_map.update_height:

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
     - ``POINTER TO`` :ref:`T_AVL_Map_Node <t_avl_map_node>`
     -


.. _fb_tree_map.upsert:

Upsert
~~~~~~

Updates a value in the map for a given key. If the key doesnt exist, it will be inserted.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Key``
     - ``ANY``
     - Key used to identify stored value
   * - ``Value``
     - ``ANY``
     - Value to store in map with key


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

