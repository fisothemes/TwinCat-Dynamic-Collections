.. _i_stack:

I_Stack (Interface)
===================

**Extends:** :ref:`I_Collection <i_collection>`

Properties
----------

.. _i_stack._values:

_Values
~~~~~~~

Type: :ref:`I_Immutable_List <i_immutable_list>`

Gets an immutable list of the items in the stack.

Methods
-------

.. _i_stack.clear:

Clear
~~~~~

**Returns:** :ref:`I_Stack <i_stack>`

Empties/Clears/Deletes every item in the stack.

.. _i_stack.get:

Get
~~~

**Returns:** :ref:`I_Stack <i_stack>`

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


.. _i_stack.get_generic:

Get_Generic
~~~~~~~~~~~

**Returns:** :ref:`I_Stack <i_stack>`

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


.. _i_stack.pop:

Pop
~~~

**Returns:** :ref:`I_Stack <i_stack>`

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


.. _i_stack.push:

Push
~~~~

**Returns:** :ref:`I_Stack <i_stack>`

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


.. _i_stack.push_generic:

Push_Generic
~~~~~~~~~~~~

**Returns:** :ref:`I_Stack <i_stack>`

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


.. _i_stack.reverse:

Reverse
~~~~~~~

**Returns:** :ref:`I_Stack <i_stack>`

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

