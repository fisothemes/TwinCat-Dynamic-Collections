.. _i_immutable_map:

I_Immutable_Map (Interface)
===========================

**Extends:** :ref:`I_Immutable_Collection <i_immutable_collection>`

Methods
-------

.. _i_immutable_map.contains:

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


.. _i_immutable_map.get:

Get
~~~

**Returns:** :ref:`I_Immutable_Map <i_immutable_map>`

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


.. _i_immutable_map.get_as_string:

Get_As_String
~~~~~~~~~~~~~

**Returns:** :ref:`I_Immutable_Map <i_immutable_map>`

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


.. _i_immutable_map.get_keys:

Get_Keys
~~~~~~~~

**Returns:** :ref:`I_Immutable_List <i_immutable_list>`

Gets an immutable list of the keys.

.. _i_immutable_map.get_values:

Get_Values
~~~~~~~~~~

**Returns:** :ref:`I_Immutable_List <i_immutable_list>`

Gets an immutable list of the values.
