

org.tron.trident.core.utils

## Class Base58

* java.lang.Object
* + org.tron.trident.core.utils.Base58

* ---

    

  ```
  public class Base58
  extends java.lang.Object
  ```

* + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static char[]` | `ALPHABET` |
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `Base58()` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static byte[]` | `decode(java.lang.String input)` |
    | `static java.math.BigInteger` | `decodeToBigInteger(java.lang.String input)` |
    | `static java.lang.String` | `encode(byte[] input)` Encodes the given bytes in base58. |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Field Detail

    - #### ALPHABET

      ```
      public static final char[] ALPHABET
      ```
  + ### Constructor Detail

    - #### Base58

      ```
      public Base58()
      ```
  + ### Method Detail

    - #### encode

      ```
      public static java.lang.String encode(byte[] input)
      ```

      Encodes the given bytes in base58. No checksum is appended.
    - #### decode

      ```
      public static byte[] decode(java.lang.String input)
                           throws java.lang.IllegalArgumentException
      ```

      Throws:
      :   `java.lang.IllegalArgumentException`
    - #### decodeToBigInteger

      ```
      public static java.math.BigInteger decodeToBigInteger(java.lang.String input)
                                                     throws java.lang.IllegalArgumentException
      ```

      Throws:
      :   `java.lang.IllegalArgumentException`