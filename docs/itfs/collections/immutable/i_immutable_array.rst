.. _i_immutable_array:

I_Immutable_Array (Interface)
=============================

Interface for an immutable array.

**Extends:** :ref:`I_Immutable_Collection <i_immutable_collection>`

Properties
----------

.. _i_immutable_array._begin:

_Begin
~~~~~~

Type: :ref:`T_Position <t_position>`

Index of the first element.

.. _i_immutable_array._end:

_End
~~~~

Type: :ref:`T_Position <t_position>`

Index of the last element.

Methods
-------

.. _i_immutable_array.contains:

Contains
~~~~~~~~

**Returns:** ``BOOL``

Checks if item is contained in array.

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


.. _i_immutable_array.get:

Get
~~~

**Returns:** :ref:`I_Immutable_Array <i_immutable_array>`

Gets item from array at specified location.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Index``
     - :ref:`T_Position <t_position>`
     - Location of item.
   * - ``Item``
     - ``ANY``
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


.. _i_immutable_array.get_as_string:

Get_As_String
~~~~~~~~~~~~~

**Returns:** :ref:`I_Immutable_Array <i_immutable_array>`

Returns item as a string, if type to string conversion is supported.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Index``
     - :ref:`T_Position <t_position>`
     - Location of item.
   * - ``sItem``
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


.. _i_immutable_array.get_type_at:

Get_Type_At
~~~~~~~~~~~

**Returns:** :ref:`I_Immutable_Array <i_immutable_array>`

Gets the type of the item at specified location.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Index``
     - :ref:`T_Position <t_position>`
     -


**Outputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Item_Type``
     - :ref:`T_Type <t_type>`
     -
   * - ``bSuccess``
     - ``BOOL``
     -


.. _i_immutable_array.search:

Search
~~~~~~

**Returns:** :ref:`I_Immutable_Array <i_immutable_array>`

Find the location of an item in the array.

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


**Outputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Index``
     - :ref:`T_Position <t_position>`
     - Location of item.
   * - ``bSuccess``
     - ``BOOL``
     -

