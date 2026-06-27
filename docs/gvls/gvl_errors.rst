.. _gvl_errors:

GVL_Errors (GVL)
================

Library errors

.. list-table::
   :header-rows: 1
   :widths: 25 20 20 35

   * - Name
     - Type
     - Default
     - Description
   * - ``ERR_NO_ERROR``
     - :ref:`T_Error <t_error>`
     - ``(bStatus := FALSE,	nCode := E_ERROR_CODE.ERR_OK, 				sSource := 'No Error.')``
     - No Error.
   * - ``ERR_TYPE_MISMATCH``
     - :ref:`T_Error <t_error>`
     - ``(bStatus := TRUE,	nCode := E_ERROR_CODE.ERR_TYPE_MISMATCH, 	sSource := 'Type mismatch.')``
     - Type mismatch.
   * - ``ERR_SIZE_MISMATCH``
     - :ref:`T_Error <t_error>`
     - ``(bStatus := TRUE,	nCode := E_ERROR_CODE.ERR_SIZE_MISMATCH, 	sSource := 'Size mismatch.')``
     - Size mismatch.
   * - ``ERR_INVALID_REFERENCE``
     - :ref:`T_Error <t_error>`
     - ``(bStatus := TRUE,	nCode := E_ERROR_CODE.ERR_INVALID_REFERENCE,sSource := 'Invalid reference.')``
     - Invalid reference.
   * - ``ERR_INVALID_INTERFACE``
     - :ref:`T_Error <t_error>`
     - ``(bStatus := TRUE,	nCode := E_ERROR_CODE.ERR_INVALID_INTERFACE,sSource := 'Invalid interface.')``
     - Invalid interface.
   * - ``ERR_INVALID_CONVERSION``
     - :ref:`T_Error <t_error>`
     - ``(bStatus := TRUE,	nCode := E_ERROR_CODE.ERR_NOT_SUPPORTED, 	sSource := 'Conversion not supported.')``
     - Conversion not supported.
   * - ``ERR_INVALID_COMPARISON``
     - :ref:`T_Error <t_error>`
     - ``(bStatus := TRUE,	nCode := E_ERROR_CODE.ERR_NOT_SUPPORTED, 	sSource := 'Invalid comparison.')``
     - Invalid comparison.
   * - ``ERR_NO_KEY``
     - :ref:`T_Error <t_error>`
     - ``(bStatus := TRUE,	nCode := E_ERROR_CODE.ERR_NO_OBJECT,		sSource := 'Key not found.')``
     - Key not found.'
   * - ``ERR_NO_ITEM``
     - :ref:`T_Error <t_error>`
     - ``(bStatus := TRUE,	nCode := E_ERROR_CODE.ERR_NO_OBJECT, 		sSource := 'Item not found.')``
     - Item not found.
   * - ``ERR_INDEX_OUT_OF_BOUNDS``
     - :ref:`T_Error <t_error>`
     - ``(bStatus := TRUE,	nCode := E_ERROR_CODE.ERR_OUT_OF_LIMITS, 	sSource := 'Index out of bounds.')``
     - Index out of bounds.
   * - ``ERR_DUPLICATE_KEY``
     - :ref:`T_Error <t_error>`
     - ``(bStatus := TRUE,	nCode := E_ERROR_CODE.ERR_DUPLICATE, 		sSource := 'Duplicate key.')``
     - Duplicate key.
   * - ``ERR_DUPLICATE_ITEM``
     - :ref:`T_Error <t_error>`
     - ``(bStatus := TRUE,	nCode := E_ERROR_CODE.ERR_DUPLICATE, 		sSource := 'Duplicate item.')``
     - Duplicate item.
   * - ``ERR_MALLOC_FAILED``
     - :ref:`T_Error <t_error>`
     - ``(bStatus := TRUE,	nCode := E_ERROR_CODE.ERR_NO_MEMORY, 		sSource := 'Memory allocation failed.')``
     - Memory allocation failed.

