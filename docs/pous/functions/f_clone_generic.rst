.. _f_clone_generic:

F_Clone_Generic (Function)
==========================

Clones a generic.
NOTE: memory is allocated in the heap for the clone and is set to pValue. Dont forget to delete it when done.

**Returns:** :ref:`T_Generic <t_generic>`

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``Source``
     - :ref:`T_Generic <t_generic>`
     -


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
   * - ``Error``
     - :ref:`T_Error <t_error>`
     -

