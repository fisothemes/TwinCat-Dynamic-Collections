.. _e_error_code:

E_ERROR_CODE (Enum)
===================

Error code are @ CmpErrors.Errors.<variable> from the CmpErrors2 Interfaces library.
https://help.codesys.com/webapp/Errors;product=CmpErrors2_Itfs;version=3.5.15.0

Members
-------

.. list-table::
   :header-rows: 1
   :widths: 30 10 60

   * - Name
     - Value
     - Description
   * - ``ERR_OK``
     - 16
     - Ok
   * - ``ERR_FAILED``
     - 16
     - General error - To be used only for internal errors
   * - ``ERR_PARAMETER``
     - 16
     - Invalid parameter for this operation
   * - ``ERR_NOT_INITIALIZED``
     - 16
     - Function cannot be executed, since component has not been initialized yet. It may work later, though
   * - ``ERR_VERSION``
     - 16
     - Version conflict
   * - ``ERR_TIMEOUT``
     - 16
     - Operation timed out
   * - ``ERR_NO_BUFFER``
     - 16
     - Insufficient memory to carry out the request
   * - ``ERR_PENDING``
     - 16
     - For async-calls: call not complete, yet
   * - ``ERR_NUM_PENDING``
     - 16
     - Too many pending calls. Try later
   * - ``ERR_NOT_IMPLEMENTED``
     - 16
     - The function is not implemented
   * - ``ERR_INVALID_ID``
     - 16
     - No object with the provided id found
   * - ``ERR_OVERFLOW``
     - 16
     - Integer overflow
   * - ``ERR_BUFFER_SIZE``
     - 16
     - The size of a buffer is too small OR invalid
   * - ``ERR_NO_OBJECT``
     - 16
     - No object with this specified name available
   * - ``ERR_NO_MEMORY``
     - 16
     - No heap memory available
   * - ``ERR_DUPLICATE``
     - 16
     - An object with the same name is still available
   * - ``ERR_MEMORY_OVERWRITE``
     - 16
     - Heap memory was written out of bounds! Memory overwrite error
   * - ``ERR_INVALID_HANDLE``
     - 16
     - Invalid handle to an object
   * - ``ERR_END_OF_0BJECT``
     - 16
     - End OF object reached
   * - ``ERR_NO_CHANGE``
     - 16
     - No changes done
   * - ``ERR_INVALID_INTERFACE``
     - 16
     - Invalid or unknown interface
   * - ``ERR_NOT_SUPPORTED``
     - 16
     - Functionality not supported
   * - ``ERR_NO_ACCESS_RIGHTS``
     - 16
     - No access rights for this operation
   * - ``ERR_OUT_OF_LIMITS``
     - 16
     - Specified limits of a resource exceeded
   * - ``ERR_ENTRIES_REMAINING``
     - 16
     - Remaining entries that could not be transmitted because of buffer limitation
   * - ``ERR_INVALID_SESSION_ID``
     - 16
     - Invalid online sessionid
   * - ``ERR_EXCEPTION``
     - 16
     - Exception occurred
   * - ``ERR_SIGNATURE_MISMATCH``
     - 16
     - Signature mismatch of an api function
   * - ``ERR_VERSION_MISMATCH``
     - 16
     - Version mismatch
   * - ``ERR_TYPE_MISMATCH``
     - 16
     - Type mismatch
   * - ``ERR_ID_MISMATCH``
     - 16
     - ID mismatch
   * - ``ERR_NO_CONSISTENCY``
     - 16
     - Consistency error
   * - ``ERR_NO_COMM_CYCLE``
     - 16
     - No COMM_CYCLE needed
   * - ``ERR_DONT_SUSPEND_TASK``
     - 16
     - Do not suspend task after an exception
   * - ``ERR_MEMORY_LOCK_FAILED``
     - 16
     - Memory cannot be locked in this operation
   * - ``ERR_LICENSE_MISSING``
     - 16
     - License missing for the runtime
   * - ``ERR_OPERATION_DENIED``
     - 16
     - Operation denied
   * - ``ERR_DEVICE``
     - 16
     - Device error
   * - ``ERR_DISK_FULL``
     - 16
     - Disk full
   * - ``ERR_CRC_FAILED``
     - 16
     - Internal use in runtime
   * - ``ERR_MEDIA_ERASE``
     - 16
     - Internal use in runtime
   * - ``ERR_FILE_ERROR``
     - 16
     - File error. e.g. cannot open a file for writing because it could be write protected
   * - ``ERR_NO_RETAIN_MEMORY``
     - 16
     - No retain memory available
   * - ``ERR_OUT_OF_LIMITS_MIN``
     - 16
     - Specified minimum-limit of a resource exceeded
   * - ``ERR_OUT_OF_LIMITS_MAX``
     - 16
     - Specified maximum-limit of a resource exceeded
   * - ``ERR_SIZE_MISMATCH``
     - 16
     - Size mismatch
   * - ``ERR_CALL_AGAIN``
     - 16
     - Operation is not yet finished, call function again to proceed
   * - ``ERR_NOTHING_TO_DO``
     - 16
     - Operation has nothing to do. No execution.
   * - ``ERR_SECURITY_CHECKS_FAILED``
     - 16
     - Some security checks have failed. /\* This is a generic error code to report this error over public channels. In this case the error code doesn’t provide a detailed cause for the error. \*/
   * - ``ERR_INVALID_SEQUENCE``
     - 16
     -
   * - ``ERR_INVALID_REFERENCE``
     - 16
     - Dereferencing an IEC reference in IecVarAccess failed due to invalid destination address, e. G. NULL.
   * - ``ERR_CONVERSION_INCOMPLETE``
     - 16
     - Conversion of string encodings was not lossless.
   * - ``ERR_SOCK_NOT_INITIALIZED``
     - 16
     - Socket errors (range: 0x0200 - 0X02FF)
   * - ``ERR_SOCK_NOT_SOCKET``
     - 16
     - The provided socket handle is invalid
   * - ``ERR_SOCK_AF_UNSUPPORTED``
     - 16
     - The address family is not supported
   * - ``ERR_SOCK_PROTO_UNSUPPORTED``
     - 16
     - Protocol is not supported \*/
   * - ``ERR_SOCK_NO_BUFFER``
     - 16
     - Not enough buffer to handle the request \*/
   * - ``ERR_SOCK_WOULD_BLOCK``
     - 167206
     - Socket is in nonblocking mode but this call would block =/
   * - ``ERR_SOCK_ADDR_INUSE``
     - 16
     - The provided address is already in use \*/
   * - ``ERR_SOCK_ADDR_NOT_AVAILABLE``
     - 16
     - The provided address is not available on THIS computer \*/
   * - ``ERR_SOCK_CONN_REFUSED``
     - 16
     - Connection has been refused by the remote host \*/
   * - ``ERR_SOCK_TIMEDOUT``
     - 16
     - Operation timed out \*/
   * - ``ERR_SOCK_HOST_NOT_FOUND``
     - 16
     - The host has NOT been found \*/
   * - ``ERR_SOCK_HOST_UNREACHABLE``
     - 16
     - Host is unreachable \*/
   * - ``ERR_SOCK_1S_CONNECTED``
     - 16
     - Socket is already connected =/
   * - ``ERR_SOCK_NOT_CONNECTED``
     - 16
     - The socket is not connected \*/
   * - ``ERR_SOCK_SHUTDOWN``
     - 16
     - Shutdown has been called on the socket =/
   * - ``ERR_SOCK_MSGSIZE``
     - 16
     - For sockets of type DGRAM. The package to send exceeds the maximum package size =/
   * - ``ERR_SOCK_CLOSED``
     - 16
     - Socket has been gracefully closed. No more send/receives allowed =/
   * - ``ERR_L7_TAG_MISSING``
     - 16
     - Tag missing in online communication buffer
   * - ``ERR_L7_UNKNOWN_CMD_GROUP``
     - 16
     - Unknown command group
   * - ``ERR_L7_UNKNOWN_CMD``
     - 16
     - Unknown command (within a valid command group)
   * - ``ERR_L7_INCOMPLETE``
     - 16
     - Level 7 service incomplete
