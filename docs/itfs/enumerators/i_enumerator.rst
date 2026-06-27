.. _i_enumerator:

I_Enumerator (Interface)
========================

**Extends:** ``__SYSTEM.IQueryInterface``

Methods
-------

.. _i_enumerator.current:

Current
~~~~~~~

**Returns:** :ref:`I_Enumerator <i_enumerator>`

Gets an item in the collection at current positon of the enumerator.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Item``
     - ``ANY``
     -


.. _i_enumerator.current_as_string:

Current_As_String
~~~~~~~~~~~~~~~~~

**Returns:** :ref:`I_Enumerable <i_enumerable>`

Gets an item in the collection at current positon of the enumerator as a string.

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``sItem``
     - ``REFERENCE TO`` ``STRING``
     -


.. _i_enumerator.dispose:

Dispose
~~~~~~~

**Returns:** ``BOOL``

Releases resources allocated to the enumerator. Returns TRUE if successful.

.. _i_enumerator.next:

Next
~~~~

**Returns:** ``BOOL``

Advances the enumerator to the next item of the collection.

.. _i_enumerator.reset:

Reset
~~~~~

**Returns:** :ref:`I_Enumerator <i_enumerator>`

Sets the enumerator to its initial position, which is before the first element in the collection.
