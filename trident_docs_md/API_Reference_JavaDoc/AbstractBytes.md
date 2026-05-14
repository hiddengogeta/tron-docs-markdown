

org.tron.trident.crypto.tuwenitypes

## Class AbstractBytes

* java.lang.Object
* + org.tron.trident.crypto.tuwenitypes.AbstractBytes

* All Implemented Interfaces:
  :   java.lang.Comparable<[Bytes](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes")>, [Bytes](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes")

  Direct Known Subclasses:
  :   [DelegatingBytes32](../../../../../org/tron/trident/crypto/tuwenitypes/DelegatingBytes32.html "class in org.tron.trident.crypto.tuwenitypes"), [MutableByteBufferWrappingBytes](../../../../../org/tron/trident/crypto/tuwenitypes/MutableByteBufferWrappingBytes.html "class in org.tron.trident.crypto.tuwenitypes")

  ---

    

  ```
  public abstract class AbstractBytes
  extends java.lang.Object
  implements Bytes
  ```

  An abstract [`Bytes`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes") value that provides implementations of [`equals(Object)`](../../../../../org/tron/trident/crypto/tuwenitypes/AbstractBytes.html#equals-java.lang.Object-), [`hashCode()`](../../../../../org/tron/trident/crypto/tuwenitypes/AbstractBytes.html#hashCode--) and
  [`toString()`](../../../../../org/tron/trident/crypto/tuwenitypes/AbstractBytes.html#toString--).

* + ### Field Summary

    - ### Fields inherited from interface org.tron.trident.crypto.tuwenitypes.[Bytes](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes")

      `EMPTY`
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `AbstractBytes()` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `boolean` | `equals(java.lang.Object obj)` Compare this value and the provided one for equality. |
    | `int` | `hashCode()` |
    | `java.lang.String` | `toString()` Return the hexadecimal string representation of this value. |

    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, wait, wait, wait`
    - ### Methods inherited from interface org.tron.trident.crypto.tuwenitypes.[Bytes](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes")

      `and, and, appendHexTo, appendTo, appendTo, bitLength, commonPrefix, commonPrefixLength, compareTo, concatenate, concatenate, copy, copyTo, copyTo, fromBase64String, fromHexString, fromHexString, fromHexStringLenient, fromHexStringLenient, get, getInt, getInt, getLong, getLong, hasLeadingZero, hasLeadingZeroByte, isEmpty, isZero, minimalBytes, mutableCopy, not, not, numberOfLeadingZeroBytes, numberOfLeadingZeros, numberOfTrailingZeroBytes, of, of, ofUnsignedInt, ofUnsignedInt, ofUnsignedLong, ofUnsignedLong, ofUnsignedShort, ofUnsignedShort, or, or, random, random, reverse, shiftLeft, shiftLeft, shiftRight, shiftRight, size, slice, slice, toArray, toArray, toArrayUnsafe, toBase64String, toBigInteger, toBigInteger, toEllipsisHexString, toHexString, toInt, toInt, toLong, toLong, toQuantityHexString, toShortHexString, toUnprefixedHexString, toUnsignedBigInteger, toUnsignedBigInteger, trimLeadingZeros, update, wrap, wrap, wrap, wrapBuffer, wrapBuffer, wrapByteBuf, wrapByteBuf, wrapByteBuffer, wrapByteBuffer, xor, xor`

* + ### Constructor Detail

    - #### AbstractBytes

      ```
      public AbstractBytes()
      ```
  + ### Method Detail

    - #### equals

      ```
      public boolean equals(java.lang.Object obj)
      ```

      Compare this value and the provided one for equality.

      Two [`Bytes`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes") values are equal is they have contain the exact same bytes.

      Overrides:
      :   `equals` in class `java.lang.Object`

      Parameters:
      :   `obj` - The object to test for equality with.

      Returns:
      :   `true` if this value and `obj` are equal.
    - #### hashCode

      ```
      public int hashCode()
      ```

      Overrides:
      :   `hashCode` in class `java.lang.Object`
    - #### toString

      ```
      public java.lang.String toString()
      ```

      Description copied from interface: `Bytes`

      Return the hexadecimal string representation of this value.

      Specified by:
      :   `toString` in interface `Bytes`

      Overrides:
      :   `toString` in class `java.lang.Object`

      Returns:
      :   The hexadecimal representation of this value, starting with "0x".