.. _fb_immutable_list:

FB_Immutable_List (Function Block)
==================================

Collection that exposes only immutable methods and properties of a collection that implements I_List.

**Implements:** :ref:`I_Immutable_List <i_immutable_list>`, :ref:`I_Iterable <i_iterable>`

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``ipList``
     - :ref:`I_List <i_list>`
     -


Properties
----------

.. _fb_immutable_list._begin:

_Begin
~~~~~~

Type: :ref:`T_Position <t_position>`

Index of the first element.

.. _fb_immutable_list._count:

_Count
~~~~~~

Type: :ref:`T_Capacity <t_capacity>`

Number of items in the collection.

.. _fb_immutable_list._empty:

_Empty
~~~~~~

Type: ``BOOL``

Checks if collection is empty.

.. _fb_immutable_list._end:

_End
~~~~

Type: :ref:`T_Position <t_position>`

Index of the last element.

.. _fb_immutable_list._error_status:

_Error_Status
~~~~~~~~~~~~~

Type: :ref:`T_Error <t_error>`

Error status of the collection.

Methods
-------

.. _fb_immutable_list.contains:

Contains
~~~~~~~~

Checks if item is contained in list.

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


.. _fb_immutable_list.get:

Get
~~~

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


.. _fb_immutable_list.get_as_string:

Get_As_String
~~~~~~~~~~~~~

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


.. _fb_immutable_list.get_type_at:

Get_Type_At
~~~~~~~~~~~

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


.. _fb_immutable_list.search:

Search
~~~~~~

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

