.. _i_deque:

I_Deque (Interface)
===================

Interface for a double ended queue - Deque

**Extends:** :ref:`I_Collection <i_collection>`

Properties
----------

.. _i_deque._values:

_Values
~~~~~~~

Type: :ref:`I_Immutable_List <i_immutable_list>`

Gets an immutable list of the items in Deque.

Methods
-------

.. _i_deque.back:

Back
~~~~

**Returns:** :ref:`I_Deque <i_deque>`

Get item at the back of the deque without removing it.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Item``
     - ``ANY``
     - Variable to store returned item value


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


.. _i_deque.clear:

Clear
~~~~~

**Returns:** :ref:`I_Deque <i_deque>`

Empties/Clears/Deletes every item in the deque.

.. _i_deque.dequeue_at_back:

Dequeue_At_Back
~~~~~~~~~~~~~~~

**Returns:** :ref:`I_Deque <i_deque>`

Removes item at the front of the deque.

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


.. _i_deque.dequeue_at_front:

Dequeue_At_Front
~~~~~~~~~~~~~~~~

**Returns:** :ref:`I_Deque <i_deque>`

Removes item at the front of the deque.

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


.. _i_deque.enqueue_at_back:

Enqueue_At_Back
~~~~~~~~~~~~~~~

**Returns:** :ref:`I_Deque <i_deque>`

Adds item at the back of the deque.

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


.. _i_deque.enqueue_at_front:

Enqueue_At_Front
~~~~~~~~~~~~~~~~

**Returns:** :ref:`I_Deque <i_deque>`

Add item to the front of the deque.

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


.. _i_deque.enqueue_generic:

Enqueue_Generic
~~~~~~~~~~~~~~~

**Returns:** :ref:`I_Deque <i_deque>`

Adds a generic item at the back of the deque.

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
   * - ``bAt_Front``
     - ``BOOL``
     - Enqueues at front if set to TRUE.


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


.. _i_deque.front:

Front
~~~~~

**Returns:** :ref:`I_Deque <i_deque>`

Get item at the front of the deque without removing it.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Item``
     - ``ANY``
     - Variable to store returned item value


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


.. _i_deque.reverse:

Reverse
~~~~~~~

**Returns:** :ref:`I_Deque <i_deque>`

Reverses the order of items in the deque.

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

