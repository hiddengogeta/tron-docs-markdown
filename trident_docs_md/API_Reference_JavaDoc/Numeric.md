

org.tron.trident.utils

## Class Numeric

* java.lang.Object
* + org.tron.trident.utils.Numeric

* ---

    

  ```
  public final class Numeric
  extends java.lang.Object
  ```

  Message codec functions.

  Implementation as per https://github.com/ethereum/wiki/wiki/JSON-RPC#hex-value-encoding

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static byte` | `asByte(int m, int n)` |
    | `static java.lang.String` | `cleanHexPrefix(java.lang.String input)` |
    | `static boolean` | `containsHexPrefix(java.lang.String input)` |
    | `static java.math.BigInteger` | `decodeQuantity(java.lang.String value)` |
    | `static java.lang.String` | `encodeQuantity(java.math.BigInteger value)` |
    | `static byte[]` | `hexStringToByteArray(java.lang.String input)` |
    | `static boolean` | `isIntegerValue(java.math.BigDecimal value)` |
    | `static boolean` | `isNumericString(java.lang.String str)` |
    | `static java.lang.String` | `prependHexPrefix(java.lang.String input)` |
    | `static java.math.BigInteger` | `toBigInt(byte[] value)` |
    | `static java.math.BigInteger` | `toBigInt(byte[] value, int offset, int length)` |
    | `static java.math.BigInteger` | `toBigInt(java.lang.String hexValue)` |
    | `static java.math.BigInteger` | `toBigIntNoPrefix(java.lang.String hexValue)` |
    | `static byte[]` | `toBytesPadded(java.math.BigInteger value, int length)` |
    | `static java.lang.String` | `toHexString(byte[] input)` |
    | `static java.lang.String` | `toHexString(byte[] input, int offset, int length, boolean withPrefix)` |
    | `static java.lang.String` | `toHexStringNoPrefix(java.math.BigInteger value)` |
    | `static java.lang.String` | `toHexStringNoPrefix(byte[] input)` |
    | `static java.lang.String` | `toHexStringNoPrefixZeroPadded(java.math.BigInteger value, int size)` |
    | `static java.lang.String` | `toHexStringWithPrefix(java.math.BigInteger value)` |
    | `static java.lang.String` | `toHexStringWithPrefixSafe(java.math.BigInteger value)` |
    | `static java.lang.String` | `toHexStringWithPrefixZeroPadded(java.math.BigInteger value, int size)` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Method Detail

    - #### encodeQuantity

      ```
      public static java.lang.String encodeQuantity(java.math.BigInteger value)
      ```
    - #### decodeQuantity

      ```
      public static java.math.BigInteger decodeQuantity(java.lang.String value)
      ```
    - #### cleanHexPrefix

      ```
      public static java.lang.String cleanHexPrefix(java.lang.String input)
      ```
    - #### prependHexPrefix

      ```
      public static java.lang.String prependHexPrefix(java.lang.String input)
      ```
    - #### containsHexPrefix

      ```
      public static boolean containsHexPrefix(java.lang.String input)
      ```
    - #### toBigInt

      ```
      public static java.math.BigInteger toBigInt(byte[] value,
                                                  int offset,
                                                  int length)
      ```
    - #### toBigInt

      ```
      public static java.math.BigInteger toBigInt(byte[] value)
      ```
    - #### toBigInt

      ```
      public static java.math.BigInteger toBigInt(java.lang.String hexValue)
      ```
    - #### toBigIntNoPrefix

      ```
      public static java.math.BigInteger toBigIntNoPrefix(java.lang.String hexValue)
      ```
    - #### toHexStringWithPrefix

      ```
      public static java.lang.String toHexStringWithPrefix(java.math.BigInteger value)
      ```
    - #### toHexStringNoPrefix

      ```
      public static java.lang.String toHexStringNoPrefix(java.math.BigInteger value)
      ```
    - #### toHexStringNoPrefix

      ```
      public static java.lang.String toHexStringNoPrefix(byte[] input)
      ```
    - #### toHexStringWithPrefixZeroPadded

      ```
      public static java.lang.String toHexStringWithPrefixZeroPadded(java.math.BigInteger value,
                                                                     int size)
      ```
    - #### toHexStringWithPrefixSafe

      ```
      public static java.lang.String toHexStringWithPrefixSafe(java.math.BigInteger value)
      ```
    - #### toHexStringNoPrefixZeroPadded

      ```
      public static java.lang.String toHexStringNoPrefixZeroPadded(java.math.BigInteger value,
                                                                   int size)
      ```
    - #### toBytesPadded

      ```
      public static byte[] toBytesPadded(java.math.BigInteger value,
                                         int length)
      ```
    - #### hexStringToByteArray

      ```
      public static byte[] hexStringToByteArray(java.lang.String input)
      ```
    - #### toHexString

      ```
      public static java.lang.String toHexString(byte[] input,
                                                 int offset,
                                                 int length,
                                                 boolean withPrefix)
      ```
    - #### toHexString

      ```
      public static java.lang.String toHexString(byte[] input)
      ```
    - #### asByte

      ```
      public static byte asByte(int m,
                                int n)
      ```
    - #### isIntegerValue

      ```
      public static boolean isIntegerValue(java.math.BigDecimal value)
      ```
    - #### isNumericString

      ```
      public static boolean isNumericString(java.lang.String str)
      ```