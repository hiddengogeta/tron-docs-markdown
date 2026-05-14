

org.tron.trident.exceptions

## Class MessageEncodingException

* java.lang.Object
* + java.lang.Throwable
  + - java.lang.Exception
    - * java.lang.RuntimeException
      * + org.tron.trident.exceptions.MessageEncodingException

* All Implemented Interfaces:
  :   java.io.Serializable

  ---

    

  ```
  public class MessageEncodingException
  extends java.lang.RuntimeException
  ```

  Encoding exception.

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.exceptions.MessageEncodingException)

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `MessageEncodingException(java.lang.String message)` |
    | `MessageEncodingException(java.lang.String message, java.lang.Throwable cause)` |
  + ### Method Summary

    - ### Methods inherited from class java.lang.Throwable

      `addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`
    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

    - #### MessageEncodingException

      ```
      public MessageEncodingException(java.lang.String message)
      ```
    - #### MessageEncodingException

      ```
      public MessageEncodingException(java.lang.String message,
                                      java.lang.Throwable cause)
      ```