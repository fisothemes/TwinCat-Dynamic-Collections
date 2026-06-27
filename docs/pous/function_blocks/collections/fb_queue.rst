.. _fb_queue:

FB_Queue (Function Block)
=========================

A collection whose access/mutation of items is first-in, first-out.

**Implements:** :ref:`I_Queue <i_queue>`

Properties
----------

.. _fb_queue._count:

_Count
~~~~~~

Type: :ref:`T_Capacity <t_capacity>`

Number of items in the collection.

.. _fb_queue._empty:

_Empty
~~~~~~

Type: ``BOOL``

Checks if collection is empty.

.. _fb_queue._error_status:

_Error_Status
~~~~~~~~~~~~~

Type: :ref:`T_Error <t_error>`

Error status of the collection.

.. _fb_queue._values:

_Values
~~~~~~~

Type: :ref:`I_Immutable_List <i_immutable_list>`

Gets an immutable list of the items in the queue.

Methods
-------

.. _fb_queue.clear:

Clear
~~~~~

Empties/Clears/Deletes every item in the queue.

.. _fb_queue.dequeue:

Dequeue
~~~~~~~

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


.. _fb_queue.enqueue:

Enqueue
~~~~~~~

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
     - Variable containg data to store on the queue.


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


.. _fb_queue.enqueue_at_front:

Enqueue_At_Front
~~~~~~~~~~~~~~~~

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
     - Variable containg data to store on the queue.


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


.. _fb_queue.enqueue_generic:

Enqueue_Generic
~~~~~~~~~~~~~~~

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


.. _fb_queue.get:

Get
~~~

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


.. _fb_queue.get_generic:

Get_Generic
~~~~~~~~~~~

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


.. _fb_queue.reverse:

Reverse
~~~~~~~

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

