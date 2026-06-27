.. _i_immutable_list:

I_Immutable_List (Interface)
============================

Interface for an immutable list.

**Extends:** :ref:`I_Immutable_Collection <i_immutable_collection>`

Properties
----------

.. _i_immutable_list._begin:

_Begin
~~~~~~

Type: :ref:`T_Position <t_position>`

Index of the first element.

.. _i_immutable_list._end:

_End
~~~~

Type: :ref:`T_Position <t_position>`

Index of the last element.

Methods
-------

.. _i_immutable_list.contains:

Contains
~~~~~~~~

**Returns:** ``BOOL``

Checks if item is contained in list

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Item``
     - ``ANY``
     - Item to find in list


.. _i_immutable_list.get:

Get
~~~

**Returns:** :ref:`I_Immutable_List <i_immutable_list>`

Gets item from list at specified location without removing it.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Index``
     - :ref:`T_Position <t_position>`
     - Location of item
   * - ``Item``
     - ``ANY``
     - Variable to store returned item


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


.. _i_immutable_list.get_as_string:

Get_As_String
~~~~~~~~~~~~~

**Returns:** :ref:`I_Immutable_List <i_immutable_list>`

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
     - Location of item
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


.. _i_immutable_list.get_type_at:

Get_Type_At
~~~~~~~~~~~

**Returns:** :ref:`I_Immutable_List <i_immutable_list>`

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


.. _i_immutable_list.search:

Search
~~~~~~

**Returns:** :ref:`I_Immutable_List <i_immutable_list>`

Find the location of an item in list.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Item``
     - ``ANY``
     - Item to find in list


**Outputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Index``
     - :ref:`T_Position <t_position>`
     - Location of item in list
   * - ``bSuccess``
     - ``BOOL``
     -

