.. _i_queue:

I_Queue (Interface)
===================

Interface for a queue

**Extends:** :ref:`I_Collection <i_collection>`

Properties
----------

.. _i_queue._values:

_Values
~~~~~~~

Type: :ref:`I_Immutable_List <i_immutable_list>`

Gets an immutable list of the items in the queue.

Methods
-------

.. _i_queue.clear:

Clear
~~~~~

**Returns:** :ref:`I_Queue <i_queue>`

Empties/Clears/Deletes every item in the queue.

.. _i_queue.dequeue:

Dequeue
~~~~~~~

**Returns:** :ref:`I_Queue <i_queue>`

Removes item at the front the queue.

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


.. _i_queue.enqueue:

Enqueue
~~~~~~~

**Returns:** :ref:`I_Queue <i_queue>`

Adds item at the back of the queue.

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


.. _i_queue.enqueue_at_front:

Enqueue_At_Front
~~~~~~~~~~~~~~~~

**Returns:** :ref:`I_Queue <i_queue>`

Adds item at the front of the queue.

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


.. _i_queue.enqueue_generic:

Enqueue_Generic
~~~~~~~~~~~~~~~

**Returns:** :ref:`I_Queue <i_queue>`

Adds a generic item at the back of the queue.

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


.. _i_queue.get:

Get
~~~

**Returns:** :ref:`I_Queue <i_queue>`

Gets the item at the front of the queue.

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


.. _i_queue.get_generic:

Get_Generic
~~~~~~~~~~~

**Returns:** :ref:`I_Queue <i_queue>`

Gets the item at the front of the queue as a generic.

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


.. _i_queue.reverse:

Reverse
~~~~~~~

**Returns:** :ref:`I_Queue <i_queue>`

Reverses the order of the items in the queue.

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

