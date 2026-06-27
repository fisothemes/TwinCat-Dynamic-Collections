.. _i_set:

I_Set (Interface)
=================

Interface for a set collection.

**Extends:** :ref:`I_Collection <i_collection>`

Methods
-------

.. _i_set.clear:

Clear
~~~~~

**Returns:** :ref:`I_Set <i_set>`

Empties/Clears/Deletes every item in the set.

.. _i_set.contains:

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


.. _i_set.get_values:

Get_Values
~~~~~~~~~~

**Returns:** :ref:`I_Immutable_List <i_immutable_list>`

Gets an immutable list of the values in the set.

.. _i_set.insert:

Insert
~~~~~~

**Returns:** :ref:`I_Set <i_set>`

Insert item into set.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Item``
     - ``ANY``
     - Data to insert


**Outputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``bSuccess``
     - ``BOOL``
     - Indicates whether operation was successful. Success = TRUE, Failure = FALSE


.. _i_set.insert_generic:

Insert_Generic
~~~~~~~~~~~~~~

**Returns:** :ref:`I_Set <i_set>`

Adds new generic item at into set.
The set will store a copy of the generic item so as to not modify the original value outside it's scope.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Item``
     - :ref:`T_Generic <t_generic>`
     - Item to store


**Outputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``bSuccess``
     - ``BOOL``
     - Indicates whether operation was successful. Success = TRUE, Failure = FALSE


.. _i_set.remove:

Remove
~~~~~~

**Returns:** :ref:`I_Set <i_set>`

Removes item from the set.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Item``
     - ``ANY``
     - Data to remove


**Outputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``bSuccess``
     - ``BOOL``
     - Indicates whether operation was successful. Success = TRUE, Failure = FALSE


.. _i_set.remove_generic:

Remove_Generic
~~~~~~~~~~~~~~

**Returns:** :ref:`I_Set <i_set>`

Removes generic item from the set.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Item``
     - :ref:`T_Generic <t_generic>`
     - Data to remove


**Outputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``bSuccess``
     - ``BOOL``
     - Indicates whether operation was successful. Success = TRUE, Failure = FALSE

