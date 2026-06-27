.. _f_error:

F_Error (Function)
==================

Error Function: Passes error code and message to type ST_ERROR when bStatus = TRUE.

**Returns:** :ref:`T_Error <t_error>`

**Inputs**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``bStatus``
     - ``BOOL``
     - Trigger to pass code and message | Note: Default is FALSE
   * - ``nCode``
     - ``DINT``
     - Code to pass to error struct | Note: code is 0 if there is no error
   * - ``sSource``
     - ``T_MaxString``
     - Message to pass to error struct | Note: message is 'No Error.'  if there is no error

