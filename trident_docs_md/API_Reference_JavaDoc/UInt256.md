

org.tron.trident.crypto.tuwenitypes

## Class UInt256

* java.lang.Object
* + org.tron.trident.crypto.tuwenitypes.UInt256

* All Implemented Interfaces:
  :   java.lang.Comparable<[UInt256](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256.html "class in org.tron.trident.crypto.tuwenitypes")>, [UInt256Value](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256Value.html "interface in org.tron.trident.crypto.tuwenitypes")<[UInt256](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256.html "class in org.tron.trident.crypto.tuwenitypes")>

  ---

    

  ```
  public final class UInt256
  extends java.lang.Object
  implements UInt256Value<UInt256>
  ```

  An unsigned 256-bit precision number.
  This is a raw [`UInt256Value`](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256Value.html "interface in org.tron.trident.crypto.tuwenitypes") - a 256-bit precision unsigned number of no particular unit.

* + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static UInt256` | `MAX_VALUE` The maximum value of a UInt256 |
    | `static UInt256` | `MIN_VALUE` The minimum value of a UInt256 |
    | `static UInt256` | `ONE` The value 1 |
    | `static UInt256` | `ZERO` The value 0 |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `UInt256` | `add(long value)` Returns a value that is `(this + value)`. |
    | `UInt256` | `add(UInt256 value)` Returns a value that is `(this + value)`. |
    | `UInt256` | `addMod(long value, long modulus)` Returns a value equivalent to `((this + value) mod modulus)`. |
    | `UInt256` | `addMod(long value, UInt256 modulus)` Returns a value equivalent to `((this + value) mod modulus)`. |
    | `UInt256` | `addMod(UInt256 value, UInt256 modulus)` Returns a value equivalent to `((this + value) mod modulus)`. |
    | `UInt256` | `and(Bytes32 bytes)` Return a bit-wise AND of this value and the supplied bytes. |
    | `UInt256` | `and(UInt256 value)` Return a bit-wise AND of this value and the supplied value. |
    | `int` | `bitLength()` Provides the number of bits following and including the highest-order ("leftmost") one-bit in the binary representation of this value, or zero if all bits are zero. |
    | `int` | `compareTo(UInt256 other)` |
    | `UInt256` | `divide(long value)` Returns a value that is `(this / value)`. |
    | `UInt256` | `divide(UInt256 value)` Returns a value that is `(this / value)`. |
    | `UInt256` | `divideCeil(long value)` Returns a value that is `ceiling(this / value)`. |
    | `UInt256` | `divideCeil(UInt256 value)` Returns a value that is `ceiling(this / value)`. |
    | `boolean` | `equals(java.lang.Object object)` |
    | `boolean` | `fitsInt()` Returns true if the value can fit in an int. |
    | `boolean` | `fitsLong()` Returns true if the value can fit in a long. |
    | `static UInt256` | `fromBytes(Bytes bytes)` Return a [`UInt256`](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256.html "class in org.tron.trident.crypto.tuwenitypes") containing the value described by the specified bytes. |
    | `static UInt256` | `fromHexString(java.lang.String str)` Parse a hexadecimal string into a [`UInt256`](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256.html "class in org.tron.trident.crypto.tuwenitypes"). |
    | `int` | `hashCode()` |
    | `int` | `intValue()` Provides this value as an int. |
    | `boolean` | `isZero()` Returns true is the value is 0. |
    | `UInt256` | `mod(long modulus)` Returns a value that is `(this mod modulus)`. |
    | `UInt256` | `mod(UInt256 modulus)` Returns a value that is `(this mod modulus)`. |
    | `UInt256` | `mod0(long modulus)` Returns a value that is `(this mod modulus)`, or 0 if modulus is 0. |
    | `UInt256` | `mod0(UInt256 modulus)` Returns a value that is `(this mod modulus)`, or 0 if modulus is 0. |
    | `UInt256` | `multiply(long value)` Returns a value that is `(this * value)`. |
    | `UInt256` | `multiply(UInt256 value)` Returns a value that is `(this * value)`. |
    | `UInt256` | `multiplyMod(long value, long modulus)` Returns a value that is `((this * value) mod modulus)`. |
    | `UInt256` | `multiplyMod(long value, UInt256 modulus)` Returns a value that is `((this * value) mod modulus)`. |
    | `UInt256` | `multiplyMod(UInt256 value, UInt256 modulus)` Returns a value that is `((this * value) mod modulus)`. |
    | `UInt256` | `not()` Return a bit-wise NOT of this value. |
    | `int` | `numberOfLeadingZeros()` Provides the number of zero bits preceding the highest-order one-bit. |
    | `UInt256` | `or(Bytes32 bytes)` Return a bit-wise OR of this value and the supplied bytes. |
    | `UInt256` | `or(UInt256 value)` Return a bit-wise OR of this value and the supplied value. |
    | `UInt256` | `pow(long exponent)` Returns a value that is `(this<sup>exponent</sup> mod 2<sup>256</sup>)` |
    | `UInt256` | `pow(UInt256 exponent)` Returns a value that is `(this<sup>exponent</sup> mod 2<sup>256</sup>)` |
    | `UInt256` | `shiftLeft(int distance)` Shift all bits in this value to the left. |
    | `UInt256` | `shiftRight(int distance)` Shift all bits in this value to the right. |
    | `UInt256` | `subtract(long value)` Returns a value that is `(this - value)`. |
    | `UInt256` | `subtract(UInt256 value)` Returns a value that is `(this - value)`. |
    | `java.math.BigInteger` | `toBigInteger()` Provides the value as a BigInteger. |
    | `Bytes32` | `toBytes()` Provides the value as bytes. |
    | `long` | `toLong()` Provides the value as a long. |
    | `Bytes` | `toMinimalBytes()` Provides the value as bytes without any leading zero bytes. |
    | `java.lang.String` | `toString()` |
    | `UInt256` | `toUInt256()` Convert this value to a [`UInt256`](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256.html "class in org.tron.trident.crypto.tuwenitypes"). |
    | `static UInt256` | `valueOf(java.math.BigInteger value)` Return a [`UInt256`](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256.html "class in org.tron.trident.crypto.tuwenitypes") containing the specified value. |
    | `static UInt256` | `valueOf(long value)` Return a `UInt256` containing the specified value. |
    | `UInt256` | `xor(Bytes32 bytes)` Return a bit-wise XOR of this value and the supplied bytes. |
    | `UInt256` | `xor(UInt256 value)` Return a bit-wise XOR of this value and the supplied value. |

    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, wait, wait, wait`
    - ### Methods inherited from interface org.tron.trident.crypto.tuwenitypes.[UInt256Value](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256Value.html "interface in org.tron.trident.crypto.tuwenitypes")

      `addExact, addExact, plus, plus, subtractExact, subtractExact, toHexString, toShortHexString`

* + ### Field Detail

    - #### MIN\_VALUE

      ```
      public static final UInt256 MIN_VALUE
      ```

      The minimum value of a UInt256
    - #### MAX\_VALUE

      ```
      public static final UInt256 MAX_VALUE
      ```

      The maximum value of a UInt256
    - #### ZERO

      ```
      public static final UInt256 ZERO
      ```

      The value 0
    - #### ONE

      ```
      public static final UInt256 ONE
      ```

      The value 1
  + ### Method Detail

    - #### valueOf

      ```
      public static UInt256 valueOf(long value)
      ```

      Return a `UInt256` containing the specified value.

      Parameters:
      :   `value` - The value to create a `UInt256` for.

      Returns:
      :   A `UInt256` containing the specified value.

      Throws:
      :   `java.lang.IllegalArgumentException` - If the value is negative.
    - #### valueOf

      ```
      public static UInt256 valueOf(java.math.BigInteger value)
      ```

      Return a [`UInt256`](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256.html "class in org.tron.trident.crypto.tuwenitypes") containing the specified value.

      Parameters:
      :   `value` - the value to create a [`UInt256`](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256.html "class in org.tron.trident.crypto.tuwenitypes") for

      Returns:
      :   a [`UInt256`](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256.html "class in org.tron.trident.crypto.tuwenitypes") containing the specified value

      Throws:
      :   `java.lang.IllegalArgumentException` - if the value is negative or too large to be represented as a UInt256
    - #### fromBytes

      ```
      public static UInt256 fromBytes(Bytes bytes)
      ```

      Return a [`UInt256`](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256.html "class in org.tron.trident.crypto.tuwenitypes") containing the value described by the specified bytes.

      Parameters:
      :   `bytes` - The bytes containing a [`UInt256`](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256.html "class in org.tron.trident.crypto.tuwenitypes").

      Returns:
      :   A [`UInt256`](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256.html "class in org.tron.trident.crypto.tuwenitypes") containing the specified value.

      Throws:
      :   `java.lang.IllegalArgumentException` - if `bytes.size() > 32`.
    - #### fromHexString

      ```
      public static UInt256 fromHexString(java.lang.String str)
      ```

      Parse a hexadecimal string into a [`UInt256`](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256.html "class in org.tron.trident.crypto.tuwenitypes").

      Parameters:
      :   `str` - The hexadecimal string to parse, which may or may not start with "0x". That representation may contain
          less than 32 bytes, in which case the result is left padded with zeros.

      Returns:
      :   The value corresponding to `str`.

      Throws:
      :   `java.lang.IllegalArgumentException` - if `str` does not correspond to a valid hexadecimal representation or
          contains more than 32 bytes.
    - #### isZero

      ```
      public boolean isZero()
      ```

      Description copied from interface: `UInt256Value`

      Returns true is the value is 0.

      Specified by:
      :   `isZero` in interface `UInt256Value<UInt256>`

      Returns:
      :   True if this is the value 0.
    - #### add

      ```
      public UInt256 add(UInt256 value)
      ```

      Description copied from interface: `UInt256Value`

      Returns a value that is `(this + value)`.

      Specified by:
      :   `add` in interface `UInt256Value<UInt256>`

      Parameters:
      :   `value` - The amount to be added to this value.

      Returns:
      :   `this + value`
    - #### add

      ```
      public UInt256 add(long value)
      ```

      Description copied from interface: `UInt256Value`

      Returns a value that is `(this + value)`.

      Specified by:
      :   `add` in interface `UInt256Value<UInt256>`

      Parameters:
      :   `value` - The amount to be added to this value.

      Returns:
      :   `this + value`
    - #### addMod

      ```
      public UInt256 addMod(UInt256 value,
                            UInt256 modulus)
      ```

      Description copied from interface: `UInt256Value`

      Returns a value equivalent to `((this + value) mod modulus)`.

      Specified by:
      :   `addMod` in interface `UInt256Value<UInt256>`

      Parameters:
      :   `value` - The amount to be added to this value.
      :   `modulus` - The modulus.

      Returns:
      :   `(this + value) mod modulus`
    - #### addMod

      ```
      public UInt256 addMod(long value,
                            UInt256 modulus)
      ```

      Description copied from interface: `UInt256Value`

      Returns a value equivalent to `((this + value) mod modulus)`.

      Specified by:
      :   `addMod` in interface `UInt256Value<UInt256>`

      Parameters:
      :   `value` - The amount to be added to this value.
      :   `modulus` - The modulus.

      Returns:
      :   `(this + value) mod modulus`
    - #### addMod

      ```
      public UInt256 addMod(long value,
                            long modulus)
      ```

      Description copied from interface: `UInt256Value`

      Returns a value equivalent to `((this + value) mod modulus)`.

      Specified by:
      :   `addMod` in interface `UInt256Value<UInt256>`

      Parameters:
      :   `value` - The amount to be added to this value.
      :   `modulus` - The modulus.

      Returns:
      :   `(this + value) mod modulus`
    - #### subtract

      ```
      public UInt256 subtract(UInt256 value)
      ```

      Description copied from interface: `UInt256Value`

      Returns a value that is `(this - value)`.

      Specified by:
      :   `subtract` in interface `UInt256Value<UInt256>`

      Parameters:
      :   `value` - The amount to be subtracted from this value.

      Returns:
      :   `this - value`
    - #### subtract

      ```
      public UInt256 subtract(long value)
      ```

      Description copied from interface: `UInt256Value`

      Returns a value that is `(this - value)`.

      Specified by:
      :   `subtract` in interface `UInt256Value<UInt256>`

      Parameters:
      :   `value` - The amount to be subtracted from this value.

      Returns:
      :   `this - value`
    - #### multiply

      ```
      public UInt256 multiply(UInt256 value)
      ```

      Description copied from interface: `UInt256Value`

      Returns a value that is `(this * value)`.

      Specified by:
      :   `multiply` in interface `UInt256Value<UInt256>`

      Parameters:
      :   `value` - The amount to multiply this value by.

      Returns:
      :   `this * value`
    - #### multiply

      ```
      public UInt256 multiply(long value)
      ```

      Description copied from interface: `UInt256Value`

      Returns a value that is `(this * value)`.

      Specified by:
      :   `multiply` in interface `UInt256Value<UInt256>`

      Parameters:
      :   `value` - The amount to multiply this value by.

      Returns:
      :   `this * value`
    - #### multiplyMod

      ```
      public UInt256 multiplyMod(UInt256 value,
                                 UInt256 modulus)
      ```

      Description copied from interface: `UInt256Value`

      Returns a value that is `((this * value) mod modulus)`.

      Specified by:
      :   `multiplyMod` in interface `UInt256Value<UInt256>`

      Parameters:
      :   `value` - The amount to multiply this value by.
      :   `modulus` - The modulus.

      Returns:
      :   `(this * value) mod modulus`
    - #### multiplyMod

      ```
      public UInt256 multiplyMod(long value,
                                 UInt256 modulus)
      ```

      Description copied from interface: `UInt256Value`

      Returns a value that is `((this * value) mod modulus)`.

      Specified by:
      :   `multiplyMod` in interface `UInt256Value<UInt256>`

      Parameters:
      :   `value` - The amount to multiply this value by.
      :   `modulus` - The modulus.

      Returns:
      :   `(this * value) mod modulus`
    - #### multiplyMod

      ```
      public UInt256 multiplyMod(long value,
                                 long modulus)
      ```

      Description copied from interface: `UInt256Value`

      Returns a value that is `((this * value) mod modulus)`.

      Specified by:
      :   `multiplyMod` in interface `UInt256Value<UInt256>`

      Parameters:
      :   `value` - The amount to multiply this value by.
      :   `modulus` - The modulus.

      Returns:
      :   `(this * value) mod modulus`
    - #### divide

      ```
      public UInt256 divide(UInt256 value)
      ```

      Description copied from interface: `UInt256Value`

      Returns a value that is `(this / value)`.

      Specified by:
      :   `divide` in interface `UInt256Value<UInt256>`

      Parameters:
      :   `value` - The amount to divide this value by.

      Returns:
      :   `this / value`
    - #### divide

      ```
      public UInt256 divide(long value)
      ```

      Description copied from interface: `UInt256Value`

      Returns a value that is `(this / value)`.

      Specified by:
      :   `divide` in interface `UInt256Value<UInt256>`

      Parameters:
      :   `value` - The amount to divide this value by.

      Returns:
      :   `this / value`
    - #### divideCeil

      ```
      public UInt256 divideCeil(UInt256 value)
      ```

      Description copied from interface: `UInt256Value`

      Returns a value that is `ceiling(this / value)`.

      Specified by:
      :   `divideCeil` in interface `UInt256Value<UInt256>`

      Parameters:
      :   `value` - The amount to divide this value by.

      Returns:
      :   `this / value + ( this % value == 0 ? 0 : 1)`
    - #### divideCeil

      ```
      public UInt256 divideCeil(long value)
      ```

      Description copied from interface: `UInt256Value`

      Returns a value that is `ceiling(this / value)`.

      Specified by:
      :   `divideCeil` in interface `UInt256Value<UInt256>`

      Parameters:
      :   `value` - The amount to divide this value by.

      Returns:
      :   `this / value + ( this % value == 0 ? 0 : 1)`
    - #### pow

      ```
      public UInt256 pow(UInt256 exponent)
      ```

      Description copied from interface: `UInt256Value`

      Returns a value that is `(this<sup>exponent</sup> mod 2<sup>256</sup>)`

      This calculates an exponentiation over the modulus of `2^256`.

      Note that `exponent` is an [`UInt256`](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256.html "class in org.tron.trident.crypto.tuwenitypes") rather than of the type `T`.

      Specified by:
      :   `pow` in interface `UInt256Value<UInt256>`

      Parameters:
      :   `exponent` - The exponent to which this value is to be raised.

      Returns:
      :   `this<sup>exponent</sup> mod 2<sup>256</sup>`
    - #### pow

      ```
      public UInt256 pow(long exponent)
      ```

      Description copied from interface: `UInt256Value`

      Returns a value that is `(this<sup>exponent</sup> mod 2<sup>256</sup>)`

      This calculates an exponentiation over the modulus of `2^256`.

      Specified by:
      :   `pow` in interface `UInt256Value<UInt256>`

      Parameters:
      :   `exponent` - The exponent to which this value is to be raised.

      Returns:
      :   `this<sup>exponent</sup> mod 2<sup>256</sup>`
    - #### mod

      ```
      public UInt256 mod(UInt256 modulus)
      ```

      Description copied from interface: `UInt256Value`

      Returns a value that is `(this mod modulus)`.

      Specified by:
      :   `mod` in interface `UInt256Value<UInt256>`

      Parameters:
      :   `modulus` - The modulus.

      Returns:
      :   `this mod modulus`.
    - #### mod

      ```
      public UInt256 mod(long modulus)
      ```

      Description copied from interface: `UInt256Value`

      Returns a value that is `(this mod modulus)`.

      Specified by:
      :   `mod` in interface `UInt256Value<UInt256>`

      Parameters:
      :   `modulus` - The modulus.

      Returns:
      :   `this mod modulus`.
    - #### mod0

      ```
      public UInt256 mod0(UInt256 modulus)
      ```

      Description copied from interface: `UInt256Value`

      Returns a value that is `(this mod modulus)`, or 0 if modulus is 0.

      Specified by:
      :   `mod0` in interface `UInt256Value<UInt256>`

      Parameters:
      :   `modulus` - The modulus.

      Returns:
      :   `this mod modulus`.
    - #### mod0

      ```
      public UInt256 mod0(long modulus)
      ```

      Description copied from interface: `UInt256Value`

      Returns a value that is `(this mod modulus)`, or 0 if modulus is 0.

      Specified by:
      :   `mod0` in interface `UInt256Value<UInt256>`

      Parameters:
      :   `modulus` - The modulus.

      Returns:
      :   `this mod modulus`.
    - #### and

      ```
      public UInt256 and(UInt256 value)
      ```

      Return a bit-wise AND of this value and the supplied value.

      Parameters:
      :   `value` - the value to perform the operation with

      Returns:
      :   the result of a bit-wise AND
    - #### and

      ```
      public UInt256 and(Bytes32 bytes)
      ```

      Return a bit-wise AND of this value and the supplied bytes.

      Parameters:
      :   `bytes` - the bytes to perform the operation with

      Returns:
      :   the result of a bit-wise AND
    - #### or

      ```
      public UInt256 or(UInt256 value)
      ```

      Return a bit-wise OR of this value and the supplied value.

      Parameters:
      :   `value` - the value to perform the operation with

      Returns:
      :   the result of a bit-wise OR
    - #### or

      ```
      public UInt256 or(Bytes32 bytes)
      ```

      Return a bit-wise OR of this value and the supplied bytes.

      Parameters:
      :   `bytes` - the bytes to perform the operation with

      Returns:
      :   the result of a bit-wise OR
    - #### xor

      ```
      public UInt256 xor(UInt256 value)
      ```

      Return a bit-wise XOR of this value and the supplied value.

      Parameters:
      :   `value` - the value to perform the operation with

      Returns:
      :   the result of a bit-wise XOR
    - #### xor

      ```
      public UInt256 xor(Bytes32 bytes)
      ```

      Return a bit-wise XOR of this value and the supplied bytes.

      Parameters:
      :   `bytes` - the bytes to perform the operation with

      Returns:
      :   the result of a bit-wise XOR
    - #### not

      ```
      public UInt256 not()
      ```

      Return a bit-wise NOT of this value.

      Returns:
      :   the result of a bit-wise NOT
    - #### shiftRight

      ```
      public UInt256 shiftRight(int distance)
      ```

      Shift all bits in this value to the right.

      Parameters:
      :   `distance` - The number of bits to shift by.

      Returns:
      :   A value containing the shifted bits.
    - #### shiftLeft

      ```
      public UInt256 shiftLeft(int distance)
      ```

      Shift all bits in this value to the left.

      Parameters:
      :   `distance` - The number of bits to shift by.

      Returns:
      :   A value containing the shifted bits.
    - #### equals

      ```
      public boolean equals(java.lang.Object object)
      ```

      Overrides:
      :   `equals` in class `java.lang.Object`
    - #### hashCode

      ```
      public int hashCode()
      ```

      Overrides:
      :   `hashCode` in class `java.lang.Object`
    - #### compareTo

      ```
      public int compareTo(UInt256 other)
      ```

      Specified by:
      :   `compareTo` in interface `java.lang.Comparable<UInt256>`
    - #### fitsInt

      ```
      public boolean fitsInt()
      ```

      Description copied from interface: `UInt256Value`

      Returns true if the value can fit in an int.

      Specified by:
      :   `fitsInt` in interface `UInt256Value<UInt256>`

      Returns:
      :   True if this value fits a java `int` (i.e. is less or equal to `Integer.MAX_VALUE`).
    - #### intValue

      ```
      public int intValue()
      ```

      Description copied from interface: `UInt256Value`

      Provides this value as an int.

      Specified by:
      :   `intValue` in interface `UInt256Value<UInt256>`

      Returns:
      :   This value as a java `int` assuming it is small enough to fit an `int`.
    - #### fitsLong

      ```
      public boolean fitsLong()
      ```

      Description copied from interface: `UInt256Value`

      Returns true if the value can fit in a long.

      Specified by:
      :   `fitsLong` in interface `UInt256Value<UInt256>`

      Returns:
      :   True if this value fits a java `long` (i.e. is less or equal to `Long.MAX_VALUE`).
    - #### toLong

      ```
      public long toLong()
      ```

      Description copied from interface: `UInt256Value`

      Provides the value as a long.

      Specified by:
      :   `toLong` in interface `UInt256Value<UInt256>`

      Returns:
      :   This value as a java `long` assuming it is small enough to fit a `long`.
    - #### toString

      ```
      public java.lang.String toString()
      ```

      Overrides:
      :   `toString` in class `java.lang.Object`
    - #### toBigInteger

      ```
      public java.math.BigInteger toBigInteger()
      ```

      Description copied from interface: `UInt256Value`

      Provides the value as a BigInteger.

      Specified by:
      :   `toBigInteger` in interface `UInt256Value<UInt256>`

      Returns:
      :   This value as a `BigInteger`.
    - #### toUInt256

      ```
      public UInt256 toUInt256()
      ```

      Description copied from interface: `UInt256Value`

      Convert this value to a [`UInt256`](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256.html "class in org.tron.trident.crypto.tuwenitypes").

      Specified by:
      :   `toUInt256` in interface `UInt256Value<UInt256>`

      Returns:
      :   This value as a [`UInt256`](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256.html "class in org.tron.trident.crypto.tuwenitypes").
    - #### toBytes

      ```
      public Bytes32 toBytes()
      ```

      Description copied from interface: `UInt256Value`

      Provides the value as bytes.

      Specified by:
      :   `toBytes` in interface `UInt256Value<UInt256>`

      Returns:
      :   The value as bytes.
    - #### toMinimalBytes

      ```
      public Bytes toMinimalBytes()
      ```

      Description copied from interface: `UInt256Value`

      Provides the value as bytes without any leading zero bytes.

      Specified by:
      :   `toMinimalBytes` in interface `UInt256Value<UInt256>`

      Returns:
      :   The value as bytes without any leading zero bytes.
    - #### numberOfLeadingZeros

      ```
      public int numberOfLeadingZeros()
      ```

      Description copied from interface: `UInt256Value`

      Provides the number of zero bits preceding the highest-order one-bit.

      Specified by:
      :   `numberOfLeadingZeros` in interface `UInt256Value<UInt256>`

      Returns:
      :   the number of zero bits preceding the highest-order ("leftmost") one-bit in the binary representation of
          this value, or 256 if the value is equal to zero.
    - #### bitLength

      ```
      public int bitLength()
      ```

      Description copied from interface: `UInt256Value`

      Provides the number of bits following and including the highest-order ("leftmost") one-bit in the binary
      representation of this value, or zero if all bits are zero.

      Specified by:
      :   `bitLength` in interface `UInt256Value<UInt256>`

      Returns:
      :   The number of bits following and including the highest-order ("leftmost") one-bit in the binary
          representation of this value, or zero if all bits are zero.