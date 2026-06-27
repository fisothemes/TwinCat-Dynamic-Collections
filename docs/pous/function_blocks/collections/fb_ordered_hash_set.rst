.. _fb_ordered_hash_set:

FB_Ordered_Hash_Set (Function Block)
====================================

A collection that stores unique items while preserving their insertion order.
Implemented using hash table with closed addressing.

**Extends:** :ref:`FB_Collection <fb_collection>`

**Implements:** :ref:`I_Hash_Set <i_hash_set>`

Properties
----------

.. _fb_ordered_hash_set._bucket_count:

_Bucket_Count
~~~~~~~~~~~~~

Type: :ref:`T_Capacity <t_capacity>`

Number of buckets in the hash set.

Methods
-------

.. _fb_ordered_hash_set.clear:

Clear
~~~~~

Empties/Clears/Deletes every item in the set.

.. _fb_ordered_hash_set.contains:

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


.. _fb_ordered_hash_set.create_buckets:

Create_Buckets
~~~~~~~~~~~~~~

Creates buckets and initialises them since user defined types can't be created as arrays dynamically using __NEW(...).

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Count``
     - :ref:`T_Capacity <t_capacity>`
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


.. _fb_ordered_hash_set.create_node:

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


.. _fb_ordered_hash_set.delete_node:

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
     - ``REFERENCE TO POINTER TO`` :ref:`ST_ORDERED_HASHSET_BUCKET_NODE <st_ordered_hashset_bucket_node>`
     -


.. _fb_ordered_hash_set.fb_exit:

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


.. _fb_ordered_hash_set.fb_init:

FB_init
~~~~~~~

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``bInitRetains``
     - ``BOOL``
     - if TRUE, the retain variables are initialized (warm start / cold start)
   * - ``bInCopyCode``
     - ``BOOL``
     - if TRUE, the instance afterwards gets moved into the copy code (online change)
   * - ``Initial_Bucket_Count``
     - :ref:`T_Capacity <t_capacity>`
     - Number of buckets you want to initialise the hash set with. Use 0 if you don't know.


.. _fb_ordered_hash_set.get_values:

Get_Values
~~~~~~~~~~

Gets an immutable list of the values in the set.

.. _fb_ordered_hash_set.hash:

Hash
~~~~

Wrapper for murmur3 hash function that generates a value that fits in the upperage of DINT to avoid negative values due to integer overflow.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Data``
     - :ref:`T_Generic <t_generic>`
     -


.. _fb_ordered_hash_set.insert:

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


.. _fb_ordered_hash_set.insert_generic:

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


.. _fb_ordered_hash_set.remove:

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


.. _fb_ordered_hash_set.remove_generic:

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


.. _fb_ordered_hash_set.resize:

Resize
~~~~~~

Sets the number of buckets in the hash set.
Existing items are rehashed and redistributed into the new buckets.
Note that of the count is 0 the hashtable is cleared.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Count``
     - :ref:`T_Capacity <t_capacity>`
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

