.. _fb_deque:

FB_Deque (Function Block)
=========================

(Pronounced Deck) Double ended queue. A collection that supports the insertion and removal of items at the front and back.

**Implements:** :ref:`I_Deque <i_deque>`

Properties
----------

.. _fb_deque._count:

_Count
~~~~~~

Type: :ref:`T_Capacity <t_capacity>`

Number of items in the collection.

.. _fb_deque._empty:

_Empty
~~~~~~

Type: ``BOOL``

Checks if collection is empty.

.. _fb_deque._error_status:

_Error_Status
~~~~~~~~~~~~~

Type: :ref:`T_Error <t_error>`

Error status of the collection.

.. _fb_deque._values:

_Values
~~~~~~~

Type: :ref:`I_Immutable_List <i_immutable_list>`

Gets an immutable list of the items in Deque.

Methods
-------

.. _fb_deque.back:

Back
~~~~

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


.. _fb_deque.clear:

Clear
~~~~~

Empties/Clears/Deletes every item in the deque.

.. _fb_deque.dequeue_at_back:

Dequeue_At_Back
~~~~~~~~~~~~~~~

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


.. _fb_deque.dequeue_at_front:

Dequeue_At_Front
~~~~~~~~~~~~~~~~

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


.. _fb_deque.enqueue_at_back:

Enqueue_At_Back
~~~~~~~~~~~~~~~

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


.. _fb_deque.enqueue_at_front:

Enqueue_At_Front
~~~~~~~~~~~~~~~~

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


.. _fb_deque.enqueue_generic:

Enqueue_Generic
~~~~~~~~~~~~~~~

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


.. _fb_deque.front:

Front
~~~~~

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


.. _fb_deque.reverse:

Reverse
~~~~~~~

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

