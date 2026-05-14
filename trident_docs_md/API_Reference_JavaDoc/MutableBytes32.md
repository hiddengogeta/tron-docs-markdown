

org.tron.trident.crypto.tuwenitypes

## Interface MutableBytes32

* All Superinterfaces:
  :   [Bytes](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes"), [Bytes32](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes"), java.lang.Comparable<[Bytes](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes")>, [MutableBytes](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes")

  ---

    

  ```
  public interface MutableBytes32
  extends MutableBytes, Bytes32
  ```

  A mutable [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes"), that is a mutable [`Bytes`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes") value of exactly 32 bytes.

* + ### Field Summary

    - ### Fields inherited from interface org.tron.trident.crypto.tuwenitypes.[MutableBytes](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes")

      `EMPTY`
    - ### Fields inherited from interface org.tron.trident.crypto.tuwenitypes.[Bytes32](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes")

      `SIZE, ZERO`
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Default Methods](javascript:show(16);)

    | Modifier and Type | Method and Description |
    | `static MutableBytes32` | `create()` Create a new mutable 32 bytes value. |
    | `static MutableBytes32` | `wrap(byte[] value)` Wrap a 32 bytes array as a mutable 32 bytes value. |
    | `static MutableBytes32` | `wrap(byte[] value, int offset)` Wrap a the provided array as a [`MutableBytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes32.html "interface in org.tron.trident.crypto.tuwenitypes"). |
    | `static MutableBytes32` | `wrap(MutableBytes value)` Wrap a the provided value, which must be of size 32, as a [`MutableBytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes32.html "interface in org.tron.trident.crypto.tuwenitypes"). |
    | `static MutableBytes32` | `wrap(MutableBytes value, int offset)` Wrap a slice/sub-part of the provided value as a [`MutableBytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes32.html "interface in org.tron.trident.crypto.tuwenitypes"). |

    - ### Methods inherited from interface org.tron.trident.crypto.tuwenitypes.[MutableBytes](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes")

      `clear, create, decrement, fill, increment, mutableSlice, of, of, set, set, setInt, setLong, wrap, wrapBuffer, wrapBuffer, wrapByteBuf, wrapByteBuf, wrapByteBuffer, wrapByteBuffer`
    - ### Methods inherited from interface org.tron.trident.crypto.tuwenitypes.[Bytes32](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes")

      `and, copy, fromHexString, fromHexStringLenient, fromHexStringStrict, leftPad, mutableCopy, not, or, random, random, rightPad, shiftLeft, shiftRight, size, wrap, wrap, xor`
    - ### Methods inherited from interface org.tron.trident.crypto.tuwenitypes.[Bytes](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes")

      `and, and, appendHexTo, appendTo, appendTo, bitLength, commonPrefix, commonPrefixLength, compareTo, concatenate, concatenate, copyTo, copyTo, fromBase64String, fromHexString, fromHexStringLenient, get, getInt, getInt, getLong, getLong, hasLeadingZero, hasLeadingZeroByte, isEmpty, isZero, minimalBytes, not, numberOfLeadingZeroBytes, numberOfLeadingZeros, numberOfTrailingZeroBytes, ofUnsignedInt, ofUnsignedInt, ofUnsignedLong, ofUnsignedLong, ofUnsignedShort, ofUnsignedShort, or, or, random, random, reverse, shiftLeft, shiftRight, slice, slice, toArray, toArray, toArrayUnsafe, toBase64String, toBigInteger, toBigInteger, toEllipsisHexString, toHexString, toInt, toInt, toLong, toLong, toQuantityHexString, toShortHexString, toString, toUnprefixedHexString, toUnsignedBigInteger, toUnsignedBigInteger, trimLeadingZeros, update, wrap, xor, xor`

* + ### Method Detail

    - #### create

      ```
      static MutableBytes32 create()
      ```

      Create a new mutable 32 bytes value.

      Returns:
      :   A newly allocated [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value.
    - #### wrap

      ```
      static MutableBytes32 wrap(byte[] value)
      ```

      Wrap a 32 bytes array as a mutable 32 bytes value.

      Specified by:
      :   `wrap` in interface `Bytes`

      Specified by:
      :   `wrap` in interface `Bytes32`

      Specified by:
      :   `wrap` in interface `MutableBytes`

      Parameters:
      :   `value` - The value to wrap.

      Returns:
      :   A [`MutableBytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes32.html "interface in org.tron.trident.crypto.tuwenitypes") wrapping `value`.

      Throws:
      :   `java.lang.IllegalArgumentException` - if `value.length != 32`.
    - #### wrap

      ```
      static MutableBytes32 wrap(byte[] value,
                                 int offset)
      ```

      Wrap a the provided array as a [`MutableBytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes32.html "interface in org.tron.trident.crypto.tuwenitypes").

      Note that value is not copied, only wrapped, and thus any future update to `value` within the wrapped parts
      will be reflected in the returned value.

      Specified by:
      :   `wrap` in interface `Bytes32`

      Parameters:
      :   `value` - The bytes to wrap.
      :   `offset` - The index (inclusive) in `value` of the first byte exposed by the returned value. In other
          words, you will have `wrap(value, i).get(0) == value[i]`.

      Returns:
      :   A [`MutableBytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes32.html "interface in org.tron.trident.crypto.tuwenitypes") that exposes the bytes of `value` from `offset` (inclusive) to
          `offset + 32` (exclusive).

      Throws:
      :   `java.lang.IndexOutOfBoundsException` - if `offset < 0 || (value.length > 0 && offset >=
          value.length)`.
      :   `java.lang.IllegalArgumentException` - if `length < 0 || offset + 32 > value.length`.
    - #### wrap

      ```
      static MutableBytes32 wrap(MutableBytes value)
      ```

      Wrap a the provided value, which must be of size 32, as a [`MutableBytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes32.html "interface in org.tron.trident.crypto.tuwenitypes").

      Note that value is not copied, only wrapped, and thus any future update to `value` will be reflected in the
      returned value.

      Parameters:
      :   `value` - The bytes to wrap.

      Returns:
      :   A [`MutableBytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes32.html "interface in org.tron.trident.crypto.tuwenitypes") that exposes the bytes of `value`.

      Throws:
      :   `java.lang.IllegalArgumentException` - if `value.size() != 32`.
    - #### wrap

      ```
      static MutableBytes32 wrap(MutableBytes value,
                                 int offset)
      ```

      Wrap a slice/sub-part of the provided value as a [`MutableBytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes32.html "interface in org.tron.trident.crypto.tuwenitypes").

      Note that the value is not copied, and thus any future update to `value` within the wrapped parts will be
      reflected in the returned value.

      Parameters:
      :   `value` - The bytes to wrap.
      :   `offset` - The index (inclusive) in `value` of the first byte exposed by the returned value. In other
          words, you will have `wrap(value, i).get(0) == value.get(i)`.

      Returns:
      :   A [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes") that exposes the bytes of `value` from `offset` (inclusive) to
          `offset + 32` (exclusive).

      Throws:
      :   `java.lang.IndexOutOfBoundsException` - if `offset < 0 || (value.size() > 0 && offset >=
          value.size())`.
      :   `java.lang.IllegalArgumentException` - if `length < 0 || offset + 32 > value.size()`.