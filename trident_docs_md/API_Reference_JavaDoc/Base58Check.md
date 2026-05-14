

org.tron.trident.utils

## Class Base58Check

* java.lang.Object
* + org.tron.trident.utils.Base58Check

* ---

    

  ```
  public final class Base58Check
  extends java.lang.Object
  ```

  Converts between an array of bytes and a Base58Check string. Not instantiable.

* + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static java.lang.String` | `ALPHABET` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static byte[]` | `base58ToBytes(java.lang.String s)` |
    | `static java.lang.String` | `bytesToBase58(byte[] data)` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Field Detail

    - #### ALPHABET

      ```
      public static final java.lang.String ALPHABET
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.utils.Base58Check.ALPHABET)
  + ### Method Detail

    - #### bytesToBase58

      ```
      public static java.lang.String bytesToBase58(byte[] data)
      ```
    - #### base58ToBytes

      ```
      public static byte[] base58ToBytes(java.lang.String s)
      ```