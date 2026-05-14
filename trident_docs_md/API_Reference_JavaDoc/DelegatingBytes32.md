

org.tron.trident.crypto.tuwenitypes

## Class DelegatingBytes32

* java.lang.Object
* + [org.tron.trident.crypto.tuwenitypes.AbstractBytes](../../../../../org/tron/trident/crypto/tuwenitypes/AbstractBytes.html "class in org.tron.trident.crypto.tuwenitypes")
  + - org.tron.trident.crypto.tuwenitypes.DelegatingBytes32

* All Implemented Interfaces:
  :   java.lang.Comparable<[Bytes](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes")>, [Bytes](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes"), [Bytes32](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes")

  ---

    

  ```
  public class DelegatingBytes32
  extends AbstractBytes
  implements Bytes32
  ```

  A class that holds and delegates all operations to its inner bytes field.

  This class may be used to create more types that represent 32 bytes, but need a different name for business logic.

* + ### Field Summary

    - ### Fields inherited from interface org.tron.trident.crypto.tuwenitypes.[Bytes32](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes")

      `SIZE, ZERO`
    - ### Fields inherited from interface org.tron.trident.crypto.tuwenitypes.[Bytes](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes")

      `EMPTY`
  + ### Constructor Summary

    Constructors

    | Modifier | Constructor and Description |
    | `protected` | `DelegatingBytes32(Bytes delegate)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Bytes32` | `copy()` Return a value equivalent to this one but guaranteed to 1) be deeply immutable (i.e. |
    | `byte` | `get(int i)` Retrieve a byte in this value. |
    | `MutableBytes32` | `mutableCopy()` Return a new mutable value initialized with the content of this value. |
    | `int` | `size()` Provides the number of bytes this value represents. |
    | `Bytes` | `slice(int index, int length)` Create a new value representing (a view of) a slice of the bytes of this value. |

    - ### Methods inherited from class org.tron.trident.crypto.tuwenitypes.[AbstractBytes](../../../../../org/tron/trident/crypto/tuwenitypes/AbstractBytes.html "class in org.tron.trident.crypto.tuwenitypes")

      `equals, hashCode, toString`
    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, wait, wait, wait`
    - ### Methods inherited from interface org.tron.trident.crypto.tuwenitypes.[Bytes32](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes32.html "interface in org.tron.trident.crypto.tuwenitypes")

      `and, fromHexString, fromHexStringLenient, fromHexStringStrict, leftPad, not, or, random, random, rightPad, shiftLeft, shiftRight, wrap, wrap, wrap, wrap, xor`
    - ### Methods inherited from interface org.tron.trident.crypto.tuwenitypes.[Bytes](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html "interface in org.tron.trident.crypto.tuwenitypes")

      `and, and, appendHexTo, appendTo, appendTo, bitLength, commonPrefix, commonPrefixLength, compareTo, concatenate, concatenate, copyTo, copyTo, fromBase64String, fromHexString, fromHexStringLenient, getInt, getInt, getLong, getLong, hasLeadingZero, hasLeadingZeroByte, isEmpty, isZero, minimalBytes, not, numberOfLeadingZeroBytes, numberOfLeadingZeros, numberOfTrailingZeroBytes, of, of, ofUnsignedInt, ofUnsignedInt, ofUnsignedLong, ofUnsignedLong, ofUnsignedShort, ofUnsignedShort, or, or, random, random, reverse, shiftLeft, shiftRight, slice, toArray, toArray, toArrayUnsafe, toBase64String, toBigInteger, toBigInteger, toEllipsisHexString, toHexString, toInt, toInt, toLong, toLong, toQuantityHexString, toShortHexString, toString, toUnprefixedHexString, toUnsignedBigInteger, toUnsignedBigInteger, trimLeadingZeros, update, wrap, wrap, wrapBuffer, wrapBuffer, wrapByteBuf, wrapByteBuf, wrapByteBuffer, wrapByteBuffer, xor, xor`

* + ### Constructor Detail

    - #### DelegatingBytes32

      ```
      protected DelegatingBytes32(Bytes delegate)
      ```
  + ### Method Detail

    - #### size

      ```
      public int size()
      ```

      Description copied from interface: `Bytes`

      Provides the number of bytes this value represents.

      Specified by:
      :   `size` in interface `Bytes`

      Specified by:
      :   `size` in interface `Bytes32`

      Returns:
      :   The number of bytes this value represents.
    - #### get

      ```
      public byte get(int i)
      ```

      Description copied from interface: `Bytes`

      Retrieve a byte in this value.

      Specified by:
      :   `get` in interface `Bytes`

      Parameters:
      :   `i` - The index of the byte to fetch within the value (0-indexed).

      Returns:
      :   The byte at index `i` in this value.
    - #### slice

      ```
      public Bytes slice(int index,
                         int length)
      ```

      Description copied from interface: `Bytes`

      Create a new value representing (a view of) a slice of the bytes of this value.

      Please note that the resulting slice is only a view and as such maintains a link to the underlying full value. So
      holding a reference to the returned slice may hold more memory than the slide represents. Use [`Bytes.copy()`](../../../../../org/tron/trident/crypto/tuwenitypes/Bytes.html#copy--) on the
      returned slice if that is not what you want.

      Specified by:
      :   `slice` in interface `Bytes`

      Parameters:
      :   `index` - The start index for the slice.
      :   `length` - The length of the resulting value.

      Returns:
      :   A new value providing a view over the bytes from index `i` (included) to `i + length`
          (excluded).
    - #### copy

      ```
      public Bytes32 copy()
      ```

      Description copied from interface: `Bytes`

      Return a value equivalent to this one but guaranteed to 1) be deeply immutable (i.e. the underlying value will be
      immutable) and 2) to not retain more bytes than exposed by the value.

      Specified by:
      :   `copy` in interface `Bytes`

      Specified by:
      :   `copy` in interface `Bytes32`

      Returns:
      :   A value, equals to this one, but deeply immutable and that doesn't retain any "unreachable" bytes. For
          performance reasons, this is allowed to return this value however if it already fit those constraints.
    - #### mutableCopy

      ```
      public MutableBytes32 mutableCopy()
      ```

      Description copied from interface: `Bytes`

      Return a new mutable value initialized with the content of this value.

      Specified by:
      :   `mutableCopy` in interface `Bytes`

      Specified by:
      :   `mutableCopy` in interface `Bytes32`

      Returns:
      :   A mutable copy of this value. This will copy bytes, modifying the returned value will **not** modify
          this value.