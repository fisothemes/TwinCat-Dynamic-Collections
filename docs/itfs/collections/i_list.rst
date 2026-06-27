.. _i_list:

I_List (Interface)
==================

Interface for a list.

**Extends:** :ref:`I_Collection <i_collection>`

Properties
----------

.. _i_list._begin:

_Begin
~~~~~~

Type: :ref:`T_Position <t_position>`

Index of the first element.

.. _i_list._end:

_End
~~~~

Type: :ref:`T_Position <t_position>`

Index of the last element.

Methods
-------

.. _i_list.append:

Append
~~~~~~

**Returns:** :ref:`I_List <i_list>`

Adds an item to the end of the list.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Item``
     - ``ANY``
     - Value to store in list


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


.. _i_list.clear:

Clear
~~~~~

**Returns:** :ref:`I_List <i_list>`

Empties/Clears/Deletes every item in the list.

.. _i_list.contains:

Contains
~~~~~~~~

**Returns:** ``BOOL``

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


.. _i_list.get:

Get
~~~

**Returns:** :ref:`I_List <i_list>`

Gets item from list at specified location without removing it

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


.. _i_list.get_as_string:

Get_As_String
~~~~~~~~~~~~~

**Returns:** :ref:`I_List <i_list>`

Returns item as a string, if type to string conversion is supported

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


.. _i_list.get_generic:

Get_Generic
~~~~~~~~~~~

**Returns:** :ref:`I_List <i_list>`

Gets a value from a list in it's generic form.
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
     - Location of item


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


.. _i_list.get_type_at:

Get_Type_At
~~~~~~~~~~~

**Returns:** :ref:`I_List <i_list>`

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


.. _i_list.insert:

Insert
~~~~~~

**Returns:** :ref:`I_List <i_list>`

Adds new item to list at specified location, if index = 0, item will be added at the front, if index = count, item will be added at the back

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
     - Item to store in list


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


.. _i_list.insert_generic:

Insert_Generic
~~~~~~~~~~~~~~

**Returns:** :ref:`I_List <i_list>`

Adds new item to list at specified location using the generic form.
If index = 0, item will be added at the front, if index = count, item will be added at the back

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
     - :ref:`T_Generic <t_generic>`
     - Item to store in list


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


.. _i_list.prepend:

Prepend
~~~~~~~

**Returns:** :ref:`I_List <i_list>`

Adds an item at the front of the list.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Item``
     - ``ANY``
     - Value to store in list


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


.. _i_list.remove:

Remove
~~~~~~

**Returns:** :ref:`I_List <i_list>`

Removes item from the list.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Item``
     - ``ANY``
     - Item to remove from in list


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


.. _i_list.remove_at:

Remove_At
~~~~~~~~~

**Returns:** :ref:`I_List <i_list>`

Remove item at specified location

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


.. _i_list.remove_last:

Remove_Last
~~~~~~~~~~~

**Returns:** :ref:`I_List <i_list>`

Removes item at the back of the list.

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


.. _i_list.resize:

Resize
~~~~~~

**Returns:** :ref:`I_List <i_list>`

Manually resize list. If list becomes smaller, item on higher locations will be deleted.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Size``
     - :ref:`T_Capacity <t_capacity>`
     - New size of list.


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


.. _i_list.reverse:

Reverse
~~~~~~~

**Returns:** :ref:`I_List <i_list>`

Reverses the order of items in the list

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


.. _i_list.search:

Search
~~~~~~

**Returns:** :ref:`I_List <i_list>`

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


.. _i_list.set:

Set
~~~

**Returns:** :ref:`I_List <i_list>`

Changes the item at the specified location in the list.

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
     - Item to store in list


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


.. _i_list.set_generic:

Set_Generic
~~~~~~~~~~~

**Returns:** :ref:`I_List <i_list>`

Changes the item at the specified location in the list in it's generic form.

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
     - :ref:`T_Generic <t_generic>`
     - Item to store in list


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


.. _i_list.swap:

Swap
~~~~

**Returns:** :ref:`I_List <i_list>`

Swaps item at index A with item at index B.

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

