.. _i_hash_map:

I_Hash_Map (Interface)
======================

Interface for a set implemented using a hash table.

**Extends:** :ref:`I_Map <i_map>`

Properties
----------

.. _i_hash_map._bucket_count:

_Bucket_Count
~~~~~~~~~~~~~

Type: :ref:`T_Capacity <t_capacity>`

Number of buckets in the hash map.

Methods
-------

.. _i_hash_map.resize:

Resize
~~~~~~

**Returns:** :ref:`I_Hash_Map <i_hash_map>`

Sets the number of buckets in the hash map.
Existing items are rehashed and redistributed into the new buckets.

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

