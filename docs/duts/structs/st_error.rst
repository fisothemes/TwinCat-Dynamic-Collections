.. _st_error:

ST_ERROR (Struct)
=================

STRUCT used to contain error status information.

**Fields**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Type
     - Description
   * - ``nCODE``
     - ``DINT``
     - Error code specific to the particular error.
   * - ``bSTATUS``
     - ``BOOL``
     - Indicates if an error has occurred | TRUE = error, FALSE = no error
   * - ``sSOURCE``
     - ``STRING``
     - Textual information describing the error.

