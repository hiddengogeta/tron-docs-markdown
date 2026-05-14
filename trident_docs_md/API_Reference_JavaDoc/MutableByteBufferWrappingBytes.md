

org.tron.trident.crypto.tuwenitypes

## Class MutableByteBufferWrappingBytes

* java.lang.Object
* + [org.tron.trident.crypto.tuwenitypes.AbstractBytes](../../../../../org/tron/trident/crypto/tuwenitypes/AbstractBytes.html "class in org.tron.trident.crypto.tuwenitypes")
  + - org.tron.trident.crypto.tuwenitypes.MutableByteBufferWrappingBytes

* All Implemented Interfaces:
  :   java.lang.Comparable<[Bytes](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes")>, [Bytes](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes"), [MutableBytes](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes")

  ---

    

  ```
  public class MutableByteBufferWrappingBytes
  extends AbstractBytes
  implements MutableBytes
  ```

* + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `protected java.nio.ByteBuffer` | `byteBuffer` |
    | `protected int` | `length` |
    | `protected int` | `offset` |

    - ### Fields inherited from interface org.tron.trident.crypto.tuwenitypes.[MutableBytes](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes")

      `EMPTY`
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `void` | `appendTo(java.nio.ByteBuffer byteBuffer)` Append the bytes of this value to the `ByteBuffer`. |
    | `Bytes` | `copy()` Return a value equivalent to this one but guaranteed to 1) be deeply immutable (i.e. |
    | `byte` | `get(int i)` Retrieve a byte in this value. |
    | `int` | `getInt(int i)` Retrieve the 4 bytes starting at the provided index in this value as an integer. |
    | `long` | `getLong(int i)` Retrieves the 8 bytes starting at the provided index in this value as a long. |
    | `MutableBytes` | `mutableCopy()` Return a new mutable value initialized with the content of this value. |
    | `MutableBytes` | `mutableSlice(int i, int length)` Create a mutable slice of the bytes of this value. |
    | `void` | `set(int i, byte b)` Set a byte in this value. |
    | `void` | `setInt(int i, int value)` Set the 4 bytes starting at the specified index to the specified integer value. |
    | `void` | `setLong(int i, long value)` Set the 8 bytes starting at the specified index to the specified long value. |
    | `int` | `size()` Provides the number of bytes this value represents. |
    | `Bytes` | `slice(int i, int length)` Create a new value representing (a view of) a slice of the bytes of this value. |
    | `byte[]` | `toArray()` Extract the bytes of this value into a byte array. |
    | `byte[]` | `toArrayUnsafe()` Get the bytes represented by this value as byte array. |

    - ### Methods inherited from class org.tron.trident.crypto.tuwenitypes.[AbstractBytes](../../../../../org/tron/trident/crypto/tuwenitypes/AbstractBytes.html "class in org.tron.trident.crypto.tuwenitypes")

      `equals, hashCode, toString`
    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, wait, wait, wait`
    - ### Methods inherited from interface org.tron.trident.crypto.tuwenitypes.[MutableBytes](../../../../../org/tron/trident/crypto/tuwenitypes/MutableBytes.html "interface in org.tron.trident.crypto.tuwenitypes")

      `clear, create, decrement, fill, increment, of, of, set, wrap, wrap, wrapBuffer, wrapBuffer, wrapByteBuf, wrapByteBuf, wrapByteBuffer, wrapByteBuffer`
    - ### Methods inherited from interface org.tron.trident.crypto.tuwenitypes.[Bytes](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes")

      `and, and, appendHexTo, appendTo, appendTo, bitLength, commonPrefix, commonPrefixLength, compareTo, concatenate, concatenate, copyTo, copyTo, fromBase64String, fromHexString, fromHexString, fromHexStringLenient, fromHexStringLenient, get, getInt, getInt, getLong, getLong, hasLeadingZero, hasLeadingZeroByte, isEmpty, isZero, minimalBytes, mutableCopy, not, not, numberOfLeadingZeroBytes, numberOfLeadingZeros, numberOfTrailingZeroBytes, ofUnsignedInt, ofUnsignedInt, ofUnsignedLong, ofUnsignedLong, ofUnsignedShort, ofUnsignedShort, or, or, random, random, reverse, shiftLeft, shiftLeft, shiftRight, shiftRight, size, slice, slice, toArray, toArray, toArrayUnsafe, toBase64String, toBigInteger, toBigInteger, toEllipsisHexString, toHexString, toInt, toInt, toLong, toLong, toQuantityHexString, toShortHexString, toString, toUnprefixedHexString, toUnsignedBigInteger, toUnsignedBigInteger, trimLeadingZeros, update, wrap, xor, xor`

* + ### Field Detail

    - #### byteBuffer

      ```
      protected final java.nio.ByteBuffer byteBuffer
      ```
    - #### offset

      ```
      protected final int offset
      ```
    - #### length

      ```
      protected final int length
      ```
  + ### Method Detail

    - #### setInt

      ```
      public void setInt(int i,
                         int value)
      ```

      Description copied from interface: `MutableBytes`

      Set the 4 bytes starting at the specified index to the specified integer value.

      Specified by:
      :   `setInt` in interface `MutableBytes`

      Parameters:
      :   `i` - The index, which must less than or equal to `size() - 4`.
      :   `value` - The integer value.
    - #### setLong

      ```
      public void setLong(int i,
                          long value)
      ```

      Description copied from interface: `MutableBytes`

      Set the 8 bytes starting at the specified index to the specified long value.

      Specified by:
      :   `setLong` in interface `MutableBytes`

      Parameters:
      :   `i` - The index, which must less than or equal to `size() - 8`.
      :   `value` - The long value.
    - #### set

      ```
      public void set(int i,
                      byte b)
      ```

      Description copied from interface: `MutableBytes`

      Set a byte in this value.

      Specified by:
      :   `set` in interface `MutableBytes`

      Parameters:
      :   `i` - The index of the byte to set.
      :   `b` - The value to set that byte to.
    - #### mutableSlice

      ```
      public MutableBytes mutableSlice(int i,
                                       int length)
      ```

      Description copied from interface: `MutableBytes`

      Create a mutable slice of the bytes of this value.

      Note: the resulting slice is only a view over the original value. Holding a reference to the returned slice may
      hold more memory than the slide represents. Use [`Bytes.copy()`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html#copy--) on the returned slice to avoid this.

      Specified by:
      :   `mutableSlice` in interface `MutableBytes`

      Parameters:
      :   `i` - The start index for the slice.
      :   `length` - The length of the resulting value.

      Returns:
      :   A new mutable view over the bytes of this value from index `i` (included) to index `i + length`
          (excluded).
    - #### copy

      ```
      public Bytes copy()
      ```

      Description copied from interface: `Bytes`

      Return a value equivalent to this one but guaranteed to 1) be deeply immutable (i.e. the underlying value will be
      immutable) and 2) to not retain more bytes than exposed by the value.

      Specified by:
      :   `copy` in interface `Bytes`

      Returns:
      :   A value, equals to this one, but deeply immutable and that doesn't retain any "unreachable" bytes. For
          performance reasons, this is allowed to return this value however if it already fit those constraints.
    - #### size

      ```
      public int size()
      ```

      Description copied from interface: `Bytes`

      Provides the number of bytes this value represents.

      Returns:
      :   The number of bytes this value represents.
    - #### getInt

      ```
      public int getInt(int i)
      ```

      Description copied from interface: `Bytes`

      Retrieve the 4 bytes starting at the provided index in this value as an integer.

      Parameters:
      :   `i` - The index from which to get the int, which must less than or equal to `size() - 4`.

      Returns:
      :   An integer whose value is the 4 bytes from this value starting at index `i`.
    - #### getLong

      ```
      public long getLong(int i)
      ```

      Description copied from interface: `Bytes`

      Retrieves the 8 bytes starting at the provided index in this value as a long.

      Parameters:
      :   `i` - The index from which to get the long, which must less than or equal to `size() - 8`.

      Returns:
      :   A long whose value is the 8 bytes from this value starting at index `i`.
    - #### get

      ```
      public byte get(int i)
      ```

      Description copied from interface: `Bytes`

      Retrieve a byte in this value.

      Parameters:
      :   `i` - The index of the byte to fetch within the value (0-indexed).

      Returns:
      :   The byte at index `i` in this value.
    - #### slice

      ```
      public Bytes slice(int i,
                         int length)
      ```

      Description copied from interface: `Bytes`

      Create a new value representing (a view of) a slice of the bytes of this value.

      Please note that the resulting slice is only a view and as such maintains a link to the underlying full value. So
      holding a reference to the returned slice may hold more memory than the slide represents. Use [`Bytes.copy()`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html#copy--) on the
      returned slice if that is not what you want.

      Parameters:
      :   `i` - The start index for the slice.
      :   `length` - The length of the resulting value.

      Returns:
      :   A new value providing a view over the bytes from index `i` (included) to `i + length`
          (excluded).
    - #### mutableCopy

      ```
      public MutableBytes mutableCopy()
      ```

      Description copied from interface: `Bytes`

      Return a new mutable value initialized with the content of this value.

      Returns:
      :   A mutable copy of this value. This will copy bytes, modifying the returned value will **not** modify
          this value.
    - #### appendTo

      ```
      public void appendTo(java.nio.ByteBuffer byteBuffer)
      ```

      Description copied from interface: `Bytes`

      Append the bytes of this value to the `ByteBuffer`.

      Parameters:
      :   `byteBuffer` - The `ByteBuffer` to which to append this value.
    - #### toArray

      ```
      public byte[] toArray()
      ```

      Description copied from interface: `Bytes`

      Extract the bytes of this value into a byte array.

      Returns:
      :   A byte array with the same content than this value.
    - #### toArrayUnsafe

      ```
      public byte[] toArrayUnsafe()
      ```

      Description copied from interface: `Bytes`

      Get the bytes represented by this value as byte array.

      Contrarily to [`Bytes.toArray()`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html#toArray--), this may avoid allocating a new array and directly return the backing array of
      this value if said value is array backed and doing so is possible. As such, modifications to the returned array may
      or may not impact this value. As such, this method should be used with care and hence the "unsafe" moniker.

      Returns:
      :   A byte array with the same content than this value, which may or may not be the direct backing of this
          value.