.. _fb_hash_map:

FB_Hash_Map (Function Block)
============================

A collection of key value pairs items.
Implemented using hash table with closed addressing.

**Extends:** :ref:`FB_Collection <fb_collection>`

**Implements:** :ref:`I_Hash_Map <i_hash_map>`

Properties
----------

.. _fb_hash_map._bucket_count:

_Bucket_Count
~~~~~~~~~~~~~

Type: :ref:`T_Capacity <t_capacity>`

Number of buckets in the hash map.

Methods
-------

.. _fb_hash_map.clear:

Clear
~~~~~

Empties/Clears/Deletes every item in the map.

.. _fb_hash_map.contains:

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


.. _fb_hash_map.create_buckets:

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


.. _fb_hash_map.create_node:

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


.. _fb_hash_map.delete_node:

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
     - ``REFERENCE TO POINTER TO`` :ref:`T_Hashmap_Bucket_Node <t_hashmap_bucket_node>`
     -


.. _fb_hash_map.fb_exit:

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


.. _fb_hash_map.fb_init:

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
     - Number of buckets you want to initialise the hash map with. Use 0 if you don't know.


.. _fb_hash_map.get:

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


.. _fb_hash_map.get_as_string:

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


.. _fb_hash_map.get_generic:

Get_Generic
~~~~~~~~~~~

Gets the value in its generic form associated with the specified key in its generic form without removing it from the map.
**Use carefully as this contains the pointer of the actual value in the collection.**
If you wish to use this it is recommeded you create a copy of the returned value using MEMCPY

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


.. _fb_hash_map.get_keys:

Get_Keys
~~~~~~~~

Gets an immutable list of the keys.

.. _fb_hash_map.get_values:

Get_Values
~~~~~~~~~~

Gets an immutable list of the values.

.. _fb_hash_map.hash:

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


.. _fb_hash_map.insert:

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


.. _fb_hash_map.insert_generic:

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


.. _fb_hash_map.remove:

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


.. _fb_hash_map.remove_generic:

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
     -


.. _fb_hash_map.resize:

Resize
~~~~~~

Sets the number of buckets in the hash map.
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


.. _fb_hash_map.update:

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


.. _fb_hash_map.update_generic:

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


.. _fb_hash_map.upsert:

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

