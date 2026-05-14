

org.tron.trident.crypto.tuwenitypes

## Interface Bytes32

* All Superinterfaces:
  :   [Bytes](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes"), java.lang.Comparable<[Bytes](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes")>

  All Known Subinterfaces:
  :   [MutableBytes32](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes32.html "interface in org.tron.trident.crypto.tuwenitypes")

  All Known Implementing Classes:
  :   [DelegatingBytes32](../../../../../org/tron/trident/crypto/tuwenitypes/DelegatingBytes32.html "class in org.tron.trident.crypto.tuwenitypes")

  ---

    

  ```
  public interface Bytes32
  extends Bytes
  ```

  A [`Bytes`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes") value that is guaranteed to contain exactly 32 bytes.

* + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `SIZE` The number of bytes in this value - i.e. |
    | `static Bytes32` | `ZERO` A `Bytes32` containing all zero bytes |

    - ### Fields inherited from interface org.tron.trident.crypto.tuwenitypes.[Bytes](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes")

      `EMPTY`
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Default Methods](javascript:show(16);)

    | Modifier and Type | Method and Description |
    | `default Bytes32` | `and(Bytes32 other)` Return a bit-wise AND of these bytes and the supplied bytes. |
    | `Bytes32` | `copy()` Return a value equivalent to this one but guaranteed to 1) be deeply immutable (i.e. |
    | `static Bytes32` | `fromHexString(java.lang.CharSequence str)` Parse a hexadecimal string into a [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes"). |
    | `static Bytes32` | `fromHexStringLenient(java.lang.CharSequence str)` Parse a hexadecimal string into a [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes"). |
    | `static Bytes32` | `fromHexStringStrict(java.lang.CharSequence str)` Parse a hexadecimal string into a [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes"). |
    | `static Bytes32` | `leftPad(Bytes value)` Left pad a [`Bytes`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes") value with zero bytes to create a [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes"). |
    | `MutableBytes32` | `mutableCopy()` Return a new mutable value initialized with the content of this value. |
    | `default Bytes32` | `not()` Return a bit-wise NOT of these bytes. |
    | `default Bytes32` | `or(Bytes32 other)` Return a bit-wise OR of these bytes and the supplied bytes. |
    | `static Bytes32` | `random()` Generate random bytes. |
    | `static Bytes32` | `random(java.util.Random generator)` Generate random bytes. |
    | `static Bytes32` | `rightPad(Bytes value)` Right pad a [`Bytes`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes") value with zero bytes to create a [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes"). |
    | `default Bytes32` | `shiftLeft(int distance)` Shift all bits in this value to the left. |
    | `default Bytes32` | `shiftRight(int distance)` Shift all bits in this value to the right. |
    | `default int` | `size()` Provides the number of bytes this value represents. |
    | `static Bytes32` | `wrap(byte[] bytes)` Wrap the provided byte array, which must be of length 32, as a [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes"). |
    | `static Bytes32` | `wrap(byte[] bytes, int offset)` Wrap a slice/sub-part of the provided array as a [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes"). |
    | `static Bytes32` | `wrap(Bytes value)` Wrap a the provided value, which must be of size 32, as a [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes"). |
    | `static Bytes32` | `wrap(Bytes value, int offset)` Wrap a slice/sub-part of the provided value as a [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes"). |
    | `default Bytes32` | `xor(Bytes32 other)` Return a bit-wise XOR of these bytes and the supplied bytes. |

    - ### Methods inherited from interface org.tron.trident.crypto.tuwenitypes.[Bytes](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes")

      `and, and, appendHexTo, appendTo, appendTo, bitLength, commonPrefix, commonPrefixLength, compareTo, concatenate, concatenate, copyTo, copyTo, fromBase64String, fromHexString, fromHexStringLenient, get, getInt, getInt, getLong, getLong, hasLeadingZero, hasLeadingZeroByte, isEmpty, isZero, minimalBytes, not, numberOfLeadingZeroBytes, numberOfLeadingZeros, numberOfTrailingZeroBytes, of, of, ofUnsignedInt, ofUnsignedInt, ofUnsignedLong, ofUnsignedLong, ofUnsignedShort, ofUnsignedShort, or, or, random, random, reverse, shiftLeft, shiftRight, slice, slice, toArray, toArray, toArrayUnsafe, toBase64String, toBigInteger, toBigInteger, toEllipsisHexString, toHexString, toInt, toInt, toLong, toLong, toQuantityHexString, toShortHexString, toString, toUnprefixedHexString, toUnsignedBigInteger, toUnsignedBigInteger, trimLeadingZeros, update, wrap, wrap, wrapBuffer, wrapBuffer, wrapByteBuf, wrapByteBuf, wrapByteBuffer, wrapByteBuffer, xor, xor`

* + ### Field Detail

    - #### SIZE

      ```
      static final int SIZE
      ```

      The number of bytes in this value - i.e. 32

      See Also:
      :   [Constant Field Values](../../../../../constant-values.html#org.tron.trident.crypto.tuwenitypes.Bytes32.SIZE)
    - #### ZERO

      ```
      static final Bytes32 ZERO
      ```

      A `Bytes32` containing all zero bytes
  + ### Method Detail

    - #### wrap

      ```
      static Bytes32 wrap(byte[] bytes)
      ```

      Wrap the provided byte array, which must be of length 32, as a [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes").

      Note that value is not copied, only wrapped, and thus any future update to `value` will be reflected in the
      returned value.

      Specified by:
      :   `wrap` in interface `Bytes`

      Parameters:
      :   `bytes` - The bytes to wrap.

      Returns:
      :   A [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes") wrapping `value`.

      Throws:
      :   `java.lang.IllegalArgumentException` - if `value.length != 32`.
    - #### wrap

      ```
      static Bytes32 wrap(byte[] bytes,
                          int offset)
      ```

      Wrap a slice/sub-part of the provided array as a [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes").

      Note that value is not copied, only wrapped, and thus any future update to `value` within the wrapped parts
      will be reflected in the returned value.

      Parameters:
      :   `bytes` - The bytes to wrap.
      :   `offset` - The index (inclusive) in `value` of the first byte exposed by the returned value. In other
          words, you will have `wrap(value, i).get(0) == value[i]`.

      Returns:
      :   A [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes") that exposes the bytes of `value` from `offset` (inclusive) to
          `offset + 32` (exclusive).

      Throws:
      :   `java.lang.IndexOutOfBoundsException` - if `offset < 0 || (value.length > 0 && offset >=
          value.length)`.
      :   `java.lang.IllegalArgumentException` - if `length < 0 || offset + 32 > value.length`.
    - #### wrap

      ```
      static Bytes32 wrap(Bytes value)
      ```

      Wrap a the provided value, which must be of size 32, as a [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes").

      Note that value is not copied, only wrapped, and thus any future update to `value` will be reflected in the
      returned value.

      Parameters:
      :   `value` - The bytes to wrap.

      Returns:
      :   A [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes") that exposes the bytes of `value`.

      Throws:
      :   `java.lang.IllegalArgumentException` - if `value.size() != 32`.
    - #### wrap

      ```
      static Bytes32 wrap(Bytes value,
                          int offset)
      ```

      Wrap a slice/sub-part of the provided value as a [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes").

      Note that value is not copied, only wrapped, and thus any future update to `value` within the wrapped parts
      will be reflected in the returned value.

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
    - #### leftPad

      ```
      static Bytes32 leftPad(Bytes value)
      ```

      Left pad a [`Bytes`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes") value with zero bytes to create a [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes").

      Parameters:
      :   `value` - The bytes value pad.

      Returns:
      :   A [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes") that exposes the left-padded bytes of `value`.

      Throws:
      :   `java.lang.IllegalArgumentException` - if `value.size() > 32`.
    - #### rightPad

      ```
      static Bytes32 rightPad(Bytes value)
      ```

      Right pad a [`Bytes`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes") value with zero bytes to create a [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes").

      Parameters:
      :   `value` - The bytes value pad.

      Returns:
      :   A [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes") that exposes the rightw-padded bytes of `value`.

      Throws:
      :   `java.lang.IllegalArgumentException` - if `value.size() > 32`.
    - #### fromHexStringLenient

      ```
      static Bytes32 fromHexStringLenient(java.lang.CharSequence str)
      ```

      Parse a hexadecimal string into a [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes").

      This method is lenient in that `str` may of an odd length, in which case it will behave exactly as if it had
      an additional 0 in front.

      Specified by:
      :   `fromHexStringLenient` in interface `Bytes`

      Parameters:
      :   `str` - The hexadecimal string to parse, which may or may not start with "0x". That representation may contain
          less than 32 bytes, in which case the result is left padded with zeros (see [`fromHexStringStrict(java.lang.CharSequence)`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html#fromHexStringStrict-java.lang.CharSequence-) if
          this is not what you want).

      Returns:
      :   The value corresponding to `str`.

      Throws:
      :   `java.lang.IllegalArgumentException` - if `str` does not correspond to a valid hexadecimal representation or
          contains more than 32 bytes.
    - #### fromHexString

      ```
      static Bytes32 fromHexString(java.lang.CharSequence str)
      ```

      Parse a hexadecimal string into a [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes").

      This method is strict in that `str` must of an even length.

      Specified by:
      :   `fromHexString` in interface `Bytes`

      Parameters:
      :   `str` - The hexadecimal string to parse, which may or may not start with "0x". That representation may contain
          less than 32 bytes, in which case the result is left padded with zeros (see [`fromHexStringStrict(java.lang.CharSequence)`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html#fromHexStringStrict-java.lang.CharSequence-) if
          this is not what you want).

      Returns:
      :   The value corresponding to `str`.

      Throws:
      :   `java.lang.IllegalArgumentException` - if `str` does not correspond to a valid hexadecimal representation, is of an
          odd length, or contains more than 32 bytes.
    - #### random

      ```
      static Bytes32 random()
      ```

      Generate random bytes.

      Returns:
      :   A value containing random bytes.
    - #### random

      ```
      static Bytes32 random(java.util.Random generator)
      ```

      Generate random bytes.

      Parameters:
      :   `generator` - The generator for random bytes.

      Returns:
      :   A value containing random bytes.
    - #### fromHexStringStrict

      ```
      static Bytes32 fromHexStringStrict(java.lang.CharSequence str)
      ```

      Parse a hexadecimal string into a [`Bytes32`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes").

      This method is extra strict in that `str` must of an even length and the provided representation must have
      exactly 32 bytes.

      Parameters:
      :   `str` - The hexadecimal string to parse, which may or may not start with "0x".

      Returns:
      :   The value corresponding to `str`.

      Throws:
      :   `java.lang.IllegalArgumentException` - if `str` does not correspond to a valid hexadecimal representation, is of an
          odd length or does not contain exactly 32 bytes.
    - #### size

      ```
      default int size()
      ```

      Description copied from interface: `Bytes`

      Provides the number of bytes this value represents.

      Specified by:
      :   `size` in interface `Bytes`

      Returns:
      :   The number of bytes this value represents.
    - #### and

      ```
      default Bytes32 and(Bytes32 other)
      ```

      Return a bit-wise AND of these bytes and the supplied bytes.

      Parameters:
      :   `other` - The bytes to perform the operation with.

      Returns:
      :   The result of a bit-wise AND.
    - #### or

      ```
      default Bytes32 or(Bytes32 other)
      ```

      Return a bit-wise OR of these bytes and the supplied bytes.

      Parameters:
      :   `other` - The bytes to perform the operation with.

      Returns:
      :   The result of a bit-wise OR.
    - #### xor

      ```
      default Bytes32 xor(Bytes32 other)
      ```

      Return a bit-wise XOR of these bytes and the supplied bytes.

      Parameters:
      :   `other` - The bytes to perform the operation with.

      Returns:
      :   The result of a bit-wise XOR.
    - #### not

      ```
      default Bytes32 not()
      ```

      Description copied from interface: `Bytes`

      Return a bit-wise NOT of these bytes.

      Specified by:
      :   `not` in interface `Bytes`

      Returns:
      :   The result of a bit-wise NOT.
    - #### shiftRight

      ```
      default Bytes32 shiftRight(int distance)
      ```

      Description copied from interface: `Bytes`

      Shift all bits in this value to the right.

      Specified by:
      :   `shiftRight` in interface `Bytes`

      Parameters:
      :   `distance` - The number of bits to shift by.

      Returns:
      :   A value containing the shifted bits.
    - #### shiftLeft

      ```
      default Bytes32 shiftLeft(int distance)
      ```

      Description copied from interface: `Bytes`

      Shift all bits in this value to the left.

      Specified by:
      :   `shiftLeft` in interface `Bytes`

      Parameters:
      :   `distance` - The number of bits to shift by.

      Returns:
      :   A value containing the shifted bits.
    - #### copy

      ```
      Bytes32 copy()
      ```

      Description copied from interface: `Bytes`

      Return a value equivalent to this one but guaranteed to 1) be deeply immutable (i.e. the underlying value will be
      immutable) and 2) to not retain more bytes than exposed by the value.

      Specified by:
      :   `copy` in interface `Bytes`

      Returns:
      :   A value, equals to this one, but deeply immutable and that doesn't retain any "unreachable" bytes. For
          performance reasons, this is allowed to return this value however if it already fit those constraints.
    - #### mutableCopy

      ```
      MutableBytes32 mutableCopy()
      ```

      Description copied from interface: `Bytes`

      Return a new mutable value initialized with the content of this value.

      Specified by:
      :   `mutableCopy` in interface `Bytes`

      Returns:
      :   A mutable copy of this value. This will copy bytes, modifying the returned value will **not** modify
          this value.