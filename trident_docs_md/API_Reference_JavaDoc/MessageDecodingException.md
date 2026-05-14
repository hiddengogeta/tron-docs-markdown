

org.tron.trident.exceptions

## Class MessageDecodingException

* java.lang.Object
* + java.lang.Throwable
  + - java.lang.Exception
    - * java.lang.RuntimeException
      * + org.tron.trident.exceptions.MessageDecodingException

* All Implemented Interfaces:
  :   java.io.Serializable

  ---

    

  ```
  public class MessageDecodingException
  extends java.lang.RuntimeException
  ```

  Encoding exception.

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.exceptions.MessageDecodingException)

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `MessageDecodingException(java.lang.String message)` |
    | `MessageDecodingException(java.lang.String message, java.lang.Throwable cause)` |
  + ### Method Summary

    - ### Methods inherited from class java.lang.Throwable

      `addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`
    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

    - #### MessageDecodingException

      ```
      public MessageDecodingException(java.lang.String message)
      ```
    - #### MessageDecodingException

      ```
      public MessageDecodingException(java.lang.String message,
                                      java.lang.Throwable cause)
      ```