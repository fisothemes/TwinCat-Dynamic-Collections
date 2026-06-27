.. _fb_immutable_set:

FB_Immutable_Set (Function Block)
=================================

Collection that exposes only immutable methods and properties of a collection that implements I_Set.

**Implements:** :ref:`I_Immutable_Set <i_immutable_set>`

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``ipSet``
     - :ref:`I_Set <i_set>`
     -


Properties
----------

.. _fb_immutable_set._count:

_Count
~~~~~~

Type: :ref:`T_Capacity <t_capacity>`

Number of items in the collection.

.. _fb_immutable_set._empty:

_Empty
~~~~~~

Type: ``BOOL``

Checks if collection is empty.

.. _fb_immutable_set._error_status:

_Error_Status
~~~~~~~~~~~~~

Type: :ref:`T_Error <t_error>`

Error status of the collection.

Methods
-------

.. _fb_immutable_set.contains:

Contains
~~~~~~~~

Checks if item is contained in set.

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


.. _fb_immutable_set.get_values:

Get_Values
~~~~~~~~~~

Gets an immutable list of the values in the set.
