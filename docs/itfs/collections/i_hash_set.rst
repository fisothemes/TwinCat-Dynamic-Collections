.. _i_hash_set:

I_Hash_Set (Interface)
======================

Interface for a set implemented using a hash table.

**Extends:** :ref:`I_Set <i_set>`

Properties
----------

.. _i_hash_set._bucket_count:

_Bucket_Count
~~~~~~~~~~~~~

Type: :ref:`T_Capacity <t_capacity>`

Number of buckets in the hash set.

Methods
-------

.. _i_hash_set.resize:

Resize
~~~~~~

**Returns:** :ref:`I_Hash_Set <i_hash_set>`

Sets the number of buckets in the hash set.
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

