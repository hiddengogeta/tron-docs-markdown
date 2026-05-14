

org.tron.trident.crypto.tuwenitypes

## Interface MutableBytes

* All Superinterfaces:
  :   [Bytes](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes"), java.lang.Comparable<[Bytes](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes")>

  All Known Subinterfaces:
  :   [MutableBytes32](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes32.html "interface in org.tron.trident.crypto.tuwenitypes")

  All Known Implementing Classes:
  :   [MutableByteBufferWrappingBytes](../../../../../org/tron/trident/crypto/tuwenitypes/MutableByteBufferWrappingBytes.html "class in org.tron.trident.crypto.tuwenitypes")

  ---

    

  ```
  public interface MutableBytes
  extends Bytes
  ```

  A mutable [`Bytes`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes") value.

* + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static MutableBytes` | `EMPTY` The empty value (with 0 bytes). |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Default Methods](javascript:show(16);)

    | Modifier and Type | Method and Description |
    | `default void` | `clear()` Set all bytes in this value to 0. |
    | `static MutableBytes` | `create(int size)` Create a new mutable byte value. |
    | `default MutableBytes` | `decrement()` Decrements the value of the bytes by 1, treating the value as big endian. |
    | `default void` | `fill(byte b)` Fill all the bytes of this value with the specified byte. |
    | `default MutableBytes` | `increment()` Increments the value of the bytes by 1, treating the value as big endian. |
    | `MutableBytes` | `mutableSlice(int i, int length)` Create a mutable slice of the bytes of this value. |
    | `static MutableBytes` | `of(byte... bytes)` Create a value that contains the specified bytes in their specified order. |
    | `static MutableBytes` | `of(int... bytes)` Create a value that contains the specified bytes in their specified order. |
    | `void` | `set(int i, byte b)` Set a byte in this value. |
    | `default void` | `set(int offset, Bytes bytes)` Set a byte in this value. |
    | `default void` | `setInt(int i, int value)` Set the 4 bytes starting at the specified index to the specified integer value. |
    | `default void` | `setLong(int i, long value)` Set the 8 bytes starting at the specified index to the specified long value. |
    | `static MutableBytes` | `wrap(byte[] value)` Wrap a byte array in a [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value. |
    | `static MutableBytes` | `wrap(byte[] value, int offset, int length)` Wrap a slice of a byte array as a [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value. |
    | `static MutableBytes` | `wrapBuffer(io.vertx.core.buffer.Buffer buffer)` Wrap a full Vert.x `Buffer` as a [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value. |
    | `static MutableBytes` | `wrapBuffer(io.vertx.core.buffer.Buffer buffer, int offset, int size)` Wrap a slice of a Vert.x `Buffer` as a [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value. |
    | `static MutableBytes` | `wrapByteBuf(io.netty.buffer.ByteBuf byteBuf)` Wrap a full Netty `ByteBuf` as a [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value. |
    | `static MutableBytes` | `wrapByteBuf(io.netty.buffer.ByteBuf byteBuf, int offset, int size)` Wrap a slice of a Netty `ByteBuf` as a [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value. |
    | `static MutableBytes` | `wrapByteBuffer(java.nio.ByteBuffer byteBuffer)` Wrap a full Java NIO `ByteBuffer` as a [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value. |
    | `static MutableBytes` | `wrapByteBuffer(java.nio.ByteBuffer byteBuffer, int offset, int size)` Wrap a slice of a Java NIO `ByteBuffer` as a [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value. |

    - ### Methods inherited from interface org.tron.trident.crypto.tuwenitypes.[Bytes](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes")

      `and, and, appendHexTo, appendTo, appendTo, bitLength, commonPrefix, commonPrefixLength, compareTo, concatenate, concatenate, copy, copyTo, copyTo, fromBase64String, fromHexString, fromHexString, fromHexStringLenient, fromHexStringLenient, get, getInt, getInt, getLong, getLong, hasLeadingZero, hasLeadingZeroByte, isEmpty, isZero, minimalBytes, mutableCopy, not, not, numberOfLeadingZeroBytes, numberOfLeadingZeros, numberOfTrailingZeroBytes, ofUnsignedInt, ofUnsignedInt, ofUnsignedLong, ofUnsignedLong, ofUnsignedShort, ofUnsignedShort, or, or, random, random, reverse, shiftLeft, shiftLeft, shiftRight, shiftRight, size, slice, slice, toArray, toArray, toArrayUnsafe, toBase64String, toBigInteger, toBigInteger, toEllipsisHexString, toHexString, toInt, toInt, toLong, toLong, toQuantityHexString, toShortHexString, toString, toUnprefixedHexString, toUnsignedBigInteger, toUnsignedBigInteger, trimLeadingZeros, update, wrap, xor, xor`

* + ### Field Detail

    - #### EMPTY

      ```
      static final MutableBytes EMPTY
      ```

      The empty value (with 0 bytes).
  + ### Method Detail

    - #### create

      ```
      static MutableBytes create(int size)
      ```

      Create a new mutable byte value.

      Parameters:
      :   `size` - The size of the returned value.

      Returns:
      :   A [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value.
    - #### wrap

      ```
      static MutableBytes wrap(byte[] value)
      ```

      Wrap a byte array in a [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value.

      Specified by:
      :   `wrap` in interface `Bytes`

      Parameters:
      :   `value` - The value to wrap.

      Returns:
      :   A [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value wrapping `value`.
    - #### wrap

      ```
      static MutableBytes wrap(byte[] value,
                               int offset,
                               int length)
      ```

      Wrap a slice of a byte array as a [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value.

      Note that value is not copied and thus any future update to `value` within the slice will be reflected in the
      returned value.

      Specified by:
      :   `wrap` in interface `Bytes`

      Parameters:
      :   `value` - The value to wrap.
      :   `offset` - The index (inclusive) in `value` of the first byte exposed by the returned value. In other
          words, you will have `wrap(value, o, l).get(0) == value[o]`.
      :   `length` - The length of the resulting value.

      Returns:
      :   A [`Bytes`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes") value that expose the bytes of `value` from `offset` (inclusive) to
          `offset + length` (exclusive).

      Throws:
      :   `java.lang.IndexOutOfBoundsException` - if `offset < 0 || (value.length > 0 && offset >=
          value.length)`.
      :   `java.lang.IllegalArgumentException` - if `length < 0 || offset + length > value.length`.
    - #### wrapBuffer

      ```
      static MutableBytes wrapBuffer(io.vertx.core.buffer.Buffer buffer)
      ```

      Wrap a full Vert.x `Buffer` as a [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value.

      Note that any change to the content of the buffer may be reflected in the returned value.

      Specified by:
      :   `wrapBuffer` in interface `Bytes`

      Parameters:
      :   `buffer` - The buffer to wrap.

      Returns:
      :   A [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value.
    - #### wrapBuffer

      ```
      static MutableBytes wrapBuffer(io.vertx.core.buffer.Buffer buffer,
                                     int offset,
                                     int size)
      ```

      Wrap a slice of a Vert.x `Buffer` as a [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value.

      Note that any change to the content of the buffer may be reflected in the returned value, and any change to the
      returned value will be reflected in the buffer.

      Specified by:
      :   `wrapBuffer` in interface `Bytes`

      Parameters:
      :   `buffer` - The buffer to wrap.
      :   `offset` - The offset in `buffer` from which to expose the bytes in the returned value. That is,
          `wrapBuffer(buffer, i, 1).get(0) == buffer.getByte(i)`.
      :   `size` - The size of the returned value.

      Returns:
      :   A [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value.

      Throws:
      :   `java.lang.IndexOutOfBoundsException` - if `offset < 0 || (buffer.length() > 0 && offset >=
          buffer.length())`.
      :   `java.lang.IllegalArgumentException` - if `length < 0 || offset + length > buffer.length()`.
    - #### wrapByteBuf

      ```
      static MutableBytes wrapByteBuf(io.netty.buffer.ByteBuf byteBuf)
      ```

      Wrap a full Netty `ByteBuf` as a [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value.

      Note that any change to the content of the buffer may be reflected in the returned value.

      Specified by:
      :   `wrapByteBuf` in interface `Bytes`

      Parameters:
      :   `byteBuf` - The `ByteBuf` to wrap.

      Returns:
      :   A [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value.
    - #### wrapByteBuf

      ```
      static MutableBytes wrapByteBuf(io.netty.buffer.ByteBuf byteBuf,
                                      int offset,
                                      int size)
      ```

      Wrap a slice of a Netty `ByteBuf` as a [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value.

      Note that any change to the content of the buffer may be reflected in the returned value, and any change to the
      returned value will be reflected in the buffer.

      Specified by:
      :   `wrapByteBuf` in interface `Bytes`

      Parameters:
      :   `byteBuf` - The `ByteBuf` to wrap.
      :   `offset` - The offset in `byteBuf` from which to expose the bytes in the returned value. That is,
          `wrapByteBuf(byteBuf, i, 1).get(0) == byteBuf.getByte(i)`.
      :   `size` - The size of the returned value.

      Returns:
      :   A [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value.

      Throws:
      :   `java.lang.IndexOutOfBoundsException` - if `offset < 0 || (byteBuf.capacity() > 0 && offset >=
          byteBuf.capacity())`.
      :   `java.lang.IllegalArgumentException` - if `length < 0 || offset + length > byteBuf.capacity()`.
    - #### wrapByteBuffer

      ```
      static MutableBytes wrapByteBuffer(java.nio.ByteBuffer byteBuffer)
      ```

      Wrap a full Java NIO `ByteBuffer` as a [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value.

      Note that any change to the content of the buffer may be reflected in the returned value.

      Specified by:
      :   `wrapByteBuffer` in interface `Bytes`

      Parameters:
      :   `byteBuffer` - The `ByteBuffer` to wrap.

      Returns:
      :   A [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value.
    - #### wrapByteBuffer

      ```
      static MutableBytes wrapByteBuffer(java.nio.ByteBuffer byteBuffer,
                                         int offset,
                                         int size)
      ```

      Wrap a slice of a Java NIO `ByteBuffer` as a [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value.

      Note that any change to the content of the buffer may be reflected in the returned value, and any change to the
      returned value will be reflected in the buffer.

      Specified by:
      :   `wrapByteBuffer` in interface `Bytes`

      Parameters:
      :   `byteBuffer` - The `ByteBuffer` to wrap.
      :   `offset` - The offset in `byteBuffer` from which to expose the bytes in the returned value. That is,
          `wrapByteBuffer(byteBuffer, i, 1).get(0) == byteBuffer.getByte(i)`.
      :   `size` - The size of the returned value.

      Returns:
      :   A [`MutableBytes`](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes") value.

      Throws:
      :   `java.lang.IndexOutOfBoundsException` - if `offset < 0 || (byteBuffer.limit() > 0 && offset >=
          byteBuffer.limit())`.
      :   `java.lang.IllegalArgumentException` - if `length < 0 || offset + length > byteBuffer.limit()`.
    - #### of

      ```
      static MutableBytes of(byte... bytes)
      ```

      Create a value that contains the specified bytes in their specified order.

      Specified by:
      :   `of` in interface `Bytes`

      Parameters:
      :   `bytes` - The bytes that must compose the returned value.

      Returns:
      :   A value containing the specified bytes.
    - #### of

      ```
      static MutableBytes of(int... bytes)
      ```

      Create a value that contains the specified bytes in their specified order.

      Specified by:
      :   `of` in interface `Bytes`

      Parameters:
      :   `bytes` - The bytes.

      Returns:
      :   A value containing bytes are the one from `bytes`.

      Throws:
      :   `java.lang.IllegalArgumentException` - if any of the specified would be truncated when storing as a byte.
    - #### set

      ```
      void set(int i,
               byte b)
      ```

      Set a byte in this value.

      Parameters:
      :   `i` - The index of the byte to set.
      :   `b` - The value to set that byte to.

      Throws:
      :   `java.lang.IndexOutOfBoundsException` - if `i < 0` or {i >= size()}.
    - #### set

      ```
      default void set(int offset,
                       Bytes bytes)
      ```

      Set a byte in this value.

      Parameters:
      :   `offset` - The offset of the bytes to set.
      :   `bytes` - The value to set bytes to.

      Throws:
      :   `java.lang.IndexOutOfBoundsException` - if `i < 0` or {i >= size()}.
    - #### setInt

      ```
      default void setInt(int i,
                          int value)
      ```

      Set the 4 bytes starting at the specified index to the specified integer value.

      Parameters:
      :   `i` - The index, which must less than or equal to `size() - 4`.
      :   `value` - The integer value.

      Throws:
      :   `java.lang.IndexOutOfBoundsException` - if `i < 0` or `i > size() - 4`.
    - #### setLong

      ```
      default void setLong(int i,
                           long value)
      ```

      Set the 8 bytes starting at the specified index to the specified long value.

      Parameters:
      :   `i` - The index, which must less than or equal to `size() - 8`.
      :   `value` - The long value.

      Throws:
      :   `java.lang.IndexOutOfBoundsException` - if `i < 0` or `i > size() - 8`.
    - #### increment

      ```
      default MutableBytes increment()
      ```

      Increments the value of the bytes by 1, treating the value as big endian.
      If incrementing overflows the value then all bits flip, i.e. incrementing 0xFFFF will return 0x0000.

      Returns:
      :   this value
    - #### decrement

      ```
      default MutableBytes decrement()
      ```

      Decrements the value of the bytes by 1, treating the value as big endian.
      If decrementing underflows the value then all bits flip, i.e. decrementing 0x0000 will return 0xFFFF.

      Returns:
      :   this value
    - #### mutableSlice

      ```
      MutableBytes mutableSlice(int i,
                                int length)
      ```

      Create a mutable slice of the bytes of this value.

      Note: the resulting slice is only a view over the original value. Holding a reference to the returned slice may
      hold more memory than the slide represents. Use [`Bytes.copy()`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html#copy--) on the returned slice to avoid this.

      Parameters:
      :   `i` - The start index for the slice.
      :   `length` - The length of the resulting value.

      Returns:
      :   A new mutable view over the bytes of this value from index `i` (included) to index `i + length`
          (excluded).

      Throws:
      :   `java.lang.IllegalArgumentException` - if `length < 0`.
      :   `java.lang.IndexOutOfBoundsException` - if `i < 0` or {i >= size()} or {i + length > size()} .
    - #### fill

      ```
      default void fill(byte b)
      ```

      Fill all the bytes of this value with the specified byte.

      Parameters:
      :   `b` - The byte to use to fill the value.
    - #### clear

      ```
      default void clear()
      ```

      Set all bytes in this value to 0.