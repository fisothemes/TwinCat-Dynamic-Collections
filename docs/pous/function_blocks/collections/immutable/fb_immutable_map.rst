.. _fb_immutable_map:

FB_Immutable_Map (Function Block)
=================================

Collection that exposes only immutable methods and properties of a collection that implements I_Map.

**Implements:** :ref:`I_Immutable_Map <i_immutable_map>`

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``ipMap``
     - :ref:`I_Map <i_map>`
     -


Properties
----------

.. _fb_immutable_map._count:

_Count
~~~~~~

Type: :ref:`T_Capacity <t_capacity>`

Number of items in the collection.

.. _fb_immutable_map._empty:

_Empty
~~~~~~

Type: ``BOOL``

Checks if collection is empty.

.. _fb_immutable_map._error_status:

_Error_Status
~~~~~~~~~~~~~

Type: :ref:`T_Error <t_error>`

Error status of the collection.

Methods
-------

.. _fb_immutable_map.contains:

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


.. _fb_immutable_map.get:

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


.. _fb_immutable_map.get_as_string:

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


.. _fb_immutable_map.get_keys:

Get_Keys
~~~~~~~~

Gets an immutable list of the keys.

.. _fb_immutable_map.get_values:

Get_Values
~~~~~~~~~~

Gets an immutable list of the values in the map.
