.. _i_map:

I_Map (Interface)
=================

An interface for a collection that holds key/value pairs

**Extends:** :ref:`I_Collection <i_collection>`

Methods
-------

.. _i_map.clear:

Clear
~~~~~

**Returns:** :ref:`I_Map <i_map>`

Empties/Clears/Deletes every item in the map.

.. _i_map.contains:

Contains
~~~~~~~~

**Returns:** ``BOOL``

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


.. _i_map.get:

Get
~~~

**Returns:** :ref:`I_Map <i_map>`

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


.. _i_map.get_as_string:

Get_As_String
~~~~~~~~~~~~~

**Returns:** :ref:`I_Map <i_map>`

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


.. _i_map.get_generic:

Get_Generic
~~~~~~~~~~~

**Returns:** :ref:`I_Map <i_map>`

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


.. _i_map.get_keys:

Get_Keys
~~~~~~~~

**Returns:** :ref:`I_Immutable_List <i_immutable_list>`

Gets an immutable list of the keys.

.. _i_map.get_values:

Get_Values
~~~~~~~~~~

**Returns:** :ref:`I_Immutable_List <i_immutable_list>`

Gets an immutable list of the values.

.. _i_map.insert:

Insert
~~~~~~

**Returns:** :ref:`I_Map <i_map>`

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


.. _i_map.insert_generic:

Insert_Generic
~~~~~~~~~~~~~~

**Returns:** :ref:`I_Map <i_map>`

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


.. _i_map.remove:

Remove
~~~~~~

**Returns:** :ref:`I_Map <i_map>`

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


.. _i_map.remove_generic:

Remove_Generic
~~~~~~~~~~~~~~

**Returns:** :ref:`I_Map <i_map>`

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


.. _i_map.update:

Update
~~~~~~

**Returns:** :ref:`I_Map <i_map>`

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


.. _i_map.update_generic:

Update_Generic
~~~~~~~~~~~~~~

**Returns:** :ref:`I_Map <i_map>`

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


.. _i_map.upsert:

Upsert
~~~~~~

**Returns:** :ref:`I_Map <i_map>`

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

