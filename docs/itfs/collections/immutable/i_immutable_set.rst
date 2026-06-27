.. _i_immutable_set:

I_Immutable_Set (Interface)
===========================

Interface for immutable set.

**Extends:** :ref:`I_Immutable_Collection <i_immutable_collection>`

Methods
-------

.. _i_immutable_set.contains:

Contains
~~~~~~~~

**Returns:** ``BOOL``

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


.. _i_immutable_set.get_values:

Get_Values
~~~~~~~~~~

**Returns:** :ref:`I_Immutable_List <i_immutable_list>`

Gets an immutable list of the values in the set.
