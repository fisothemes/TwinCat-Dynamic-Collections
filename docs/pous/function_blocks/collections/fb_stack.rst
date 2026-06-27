.. _fb_stack:

FB_Stack (Function Block)
=========================

A collection whose access/mutation of items is last-in, first-out.

**Implements:** :ref:`I_Stack <i_stack>`

Properties
----------

.. _fb_stack._count:

_Count
~~~~~~

Type: :ref:`T_Capacity <t_capacity>`

Number of items in the collection.

.. _fb_stack._empty:

_Empty
~~~~~~

Type: ``BOOL``

Checks if collection is empty.

.. _fb_stack._error_status:

_Error_Status
~~~~~~~~~~~~~

Type: :ref:`T_Error <t_error>`

Error status of the collection.

.. _fb_stack._values:

_Values
~~~~~~~

Type: :ref:`I_Immutable_List <i_immutable_list>`

Gets an immutable list of the items in the stack.

Methods
-------

.. _fb_stack.clear:

Clear
~~~~~

Empties/Clears/Deletes every item in the stack.

.. _fb_stack.get:

Get
~~~

Gets item at the top of the stack.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Item``
     - ``ANY``
     - Variable to store returned item value.


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


.. _fb_stack.get_generic:

Get_Generic
~~~~~~~~~~~

Gets item at the top of the stack as a generic.

**Outputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Item``
     - :ref:`T_Generic <t_generic>`
     - Variable to store returned item value
   * - ``bSuccess``
     - ``BOOL``
     -


.. _fb_stack.pop:

Pop
~~~

Removes item at the top of the stack without returning anything.

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


.. _fb_stack.push:

Push
~~~~

Add item to the top of the stack.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
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


.. _fb_stack.push_generic:

Push_Generic
~~~~~~~~~~~~

Add generic item to the top of the stack.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
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


.. _fb_stack.reverse:

Reverse
~~~~~~~

Reverses order of items on stack.

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

