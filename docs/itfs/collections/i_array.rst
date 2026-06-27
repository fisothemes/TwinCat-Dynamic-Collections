.. _i_array:

I_Array (Interface)
===================

Interface for a static array.

**Extends:** :ref:`I_Collection <i_collection>`

Properties
----------

.. _i_array._begin:

_Begin
~~~~~~

Type: :ref:`T_Position <t_position>`

Index of the first element.

.. _i_array._end:

_End
~~~~

Type: :ref:`T_Position <t_position>`

Index of the last element.

Methods
-------

.. _i_array.contains:

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


.. _i_array.get:

Get
~~~

**Returns:** :ref:`I_Array <i_array>`

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


.. _i_array.get_as_string:

Get_As_String
~~~~~~~~~~~~~

**Returns:** :ref:`I_Array <i_array>`

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


.. _i_array.get_generic:

Get_Generic
~~~~~~~~~~~

**Returns:** :ref:`I_Array <i_array>`

Gets an item from the array in it's generic form.
**Use carefully as this contains the pointer of the actual value in the collection.**
If you wish to use this it is recommeded you create a copy of the returned value using MEMMOVE or MEMCPY

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


**Outputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Item``
     - :ref:`T_Generic <t_generic>`
     -
   * - ``bSuccess``
     - ``BOOL``
     -


.. _i_array.get_type_at:

Get_Type_At
~~~~~~~~~~~

**Returns:** :ref:`I_Array <i_array>`

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


.. _i_array.reverse:

Reverse
~~~~~~~

**Returns:** :ref:`I_Array <i_array>`

Reverses the order of items in the array.

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


.. _i_array.search:

Search
~~~~~~

**Returns:** :ref:`I_Array <i_array>`

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


.. _i_array.set:

Set
~~~

**Returns:** :ref:`I_Array <i_array>`

Changes the item at the specified location in the array.

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
     - Item to store.


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


.. _i_array.set_generic:

Set_Generic
~~~~~~~~~~~

**Returns:** :ref:`I_Array <i_array>`

Changes the item at the specified location in the array in it's generic form.

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
     - :ref:`T_Generic <t_generic>`
     - Item to store.


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


.. _i_array.swap:

Swap
~~~~

**Returns:** :ref:`I_Array <i_array>`

Swaps item at index with item at index B.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Index_A, Index_B``
     - :ref:`T_Position <t_position>`
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

