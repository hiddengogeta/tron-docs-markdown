

org.tron.trident.core.utils

## Class ByteArray

* java.lang.Object
* + org.tron.trident.core.utils.ByteArray

* ---

    

  ```
  public class ByteArray
  extends java.lang.Object
  ```

* + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static byte[]` | `EMPTY_BYTE_ARRAY` |
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `ByteArray()` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static java.lang.String` | `fromHex(java.lang.String x)` |
    | `static byte[]` | `fromHexString(java.lang.String data)` get bytes data from hex string data. |
    | `static byte[]` | `fromInt(int val)` |
    | `static byte[]` | `fromLong(long val)` |
    | `static java.math.BigInteger` | `hexToBigInteger(java.lang.String input)` |
    | `static boolean` | `isEmpty(byte[] input)` |
    | `static boolean` | `isHexString(java.lang.String str)` |
    | `static int` | `jsonHexToInt(java.lang.String x)` |
    | `static boolean` | `matrixContains(java.util.List<byte[]> source, byte[] obj)` |
    | `static byte[]` | `subArray(byte[] input, int start, int end)` Generate a subarray of a given byte array. |
    | `static java.lang.String` | `toHexString(byte[] data)` |
    | `static java.lang.String` | `toJsonHex(byte[] x)` Stringify byte[] x null for null null for empty [] |
    | `static java.lang.String` | `toJsonHex(java.lang.Long x)` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Field Detail

    - #### EMPTY\_BYTE\_ARRAY

      ```
      public static final byte[] EMPTY_BYTE_ARRAY
      ```
  + ### Constructor Detail

    - #### ByteArray

      ```
      public ByteArray()
      ```
  + ### Method Detail

    - #### toHexString

      ```
      public static java.lang.String toHexString(byte[] data)
      ```
    - #### fromHexString

      ```
      public static byte[] fromHexString(java.lang.String data)
      ```

      get bytes data from hex string data.
    - #### fromLong

      ```
      public static byte[] fromLong(long val)
      ```
    - #### fromInt

      ```
      public static byte[] fromInt(int val)
      ```
    - #### toJsonHex

      ```
      public static java.lang.String toJsonHex(byte[] x)
      ```

      Stringify byte[] x
      null for null
      null for empty []
    - #### toJsonHex

      ```
      public static java.lang.String toJsonHex(java.lang.Long x)
      ```
    - #### hexToBigInteger

      ```
      public static java.math.BigInteger hexToBigInteger(java.lang.String input)
      ```
    - #### jsonHexToInt

      ```
      public static int jsonHexToInt(java.lang.String x)
                              throws java.lang.Exception
      ```

      Throws:
      :   `java.lang.Exception`
    - #### subArray

      ```
      public static byte[] subArray(byte[] input,
                                    int start,
                                    int end)
      ```

      Generate a subarray of a given byte array.

      Parameters:
      :   `input` - the input byte array
      :   `start` - the start index
      :   `end` - the end index

      Returns:
      :   a subarray of input, ranging from start (inclusively) to end
          (exclusively)
    - #### isEmpty

      ```
      public static boolean isEmpty(byte[] input)
      ```
    - #### matrixContains

      ```
      public static boolean matrixContains(java.util.List<byte[]> source,
                                           byte[] obj)
      ```
    - #### fromHex

      ```
      public static java.lang.String fromHex(java.lang.String x)
      ```
    - #### isHexString

      ```
      public static boolean isHexString(java.lang.String str)
      ```