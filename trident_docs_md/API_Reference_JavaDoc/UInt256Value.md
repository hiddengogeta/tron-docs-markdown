

org.tron.trident.crypto.tuwenitypes

## Interface UInt256Value<T extends UInt256Value<T>>

* Type Parameters:
  :   `T` - The concrete type of the value.

  All Superinterfaces:
  :   java.lang.Comparable<T>

  All Known Implementing Classes:
  :   [UInt256](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256.html "class in org.tron.trident.crypto.tuwenitypes")

  ---

    

  ```
  public interface UInt256Value<T extends UInt256Value<T>>
  extends java.lang.Comparable<T>
  ```

  Represents a 256-bit (32 bytes) unsigned integer value.

  A [`UInt256Value`](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256Value.html "interface in org.tron.trident.crypto.tuwenitypes") is an unsigned integer value stored with 32 bytes, so whose value can range between 0 and
  2^256-1.

  This interface defines operations for value types with a 256-bit precision range. The methods provided by this
  interface take parameters of the same type (and also `long`. This provides type safety by ensuring calculations
  cannot mix different `UInt256Value` types.

  Where only a pure numerical 256-bit value is required, [`UInt256`](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256.html "class in org.tron.trident.crypto.tuwenitypes") should be used.

  It is strongly advised to extend BaseUInt256Value rather than implementing this interface directly. Doing so
  provides type safety in that quantities of different units cannot be mixed accidentally.

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Default Methods](javascript:show(16);)

    | Modifier and Type | Method and Description |
    | `T` | `add(long value)` Returns a value that is `(this + value)`. |
    | `T` | `add(T value)` Returns a value that is `(this + value)`. |
    | `default T` | `addExact(long value)` Returns a value that is `(this + value)`. |
    | `default T` | `addExact(T value)` Returns a value that is `(this + value)`. |
    | `T` | `addMod(long value, long modulus)` Returns a value equivalent to `((this + value) mod modulus)`. |
    | `T` | `addMod(long value, UInt256 modulus)` Returns a value equivalent to `((this + value) mod modulus)`. |
    | `T` | `addMod(T value, UInt256 modulus)` Returns a value equivalent to `((this + value) mod modulus)`. |
    | `default int` | `bitLength()` Provides the number of bits following and including the highest-order ("leftmost") one-bit in the binary representation of this value, or zero if all bits are zero. |
    | `T` | `divide(long value)` Returns a value that is `(this / value)`. |
    | `T` | `divide(T value)` Returns a value that is `(this / value)`. |
    | `T` | `divideCeil(long value)` Returns a value that is `ceiling(this / value)`. |
    | `T` | `divideCeil(T value)` Returns a value that is `ceiling(this / value)`. |
    | `default boolean` | `fitsInt()` Returns true if the value can fit in an int. |
    | `default boolean` | `fitsLong()` Returns true if the value can fit in a long. |
    | `default int` | `intValue()` Provides this value as an int. |
    | `default boolean` | `isZero()` Returns true is the value is 0. |
    | `T` | `mod(long modulus)` Returns a value that is `(this mod modulus)`. |
    | `T` | `mod(UInt256 modulus)` Returns a value that is `(this mod modulus)`. |
    | `T` | `mod0(long modulus)` Returns a value that is `(this mod modulus)`, or 0 if modulus is 0. |
    | `T` | `mod0(UInt256 modulus)` Returns a value that is `(this mod modulus)`, or 0 if modulus is 0. |
    | `T` | `multiply(long value)` Returns a value that is `(this * value)`. |
    | `T` | `multiply(T value)` Returns a value that is `(this * value)`. |
    | `T` | `multiplyMod(long value, long modulus)` Returns a value that is `((this * value) mod modulus)`. |
    | `T` | `multiplyMod(long value, UInt256 modulus)` Returns a value that is `((this * value) mod modulus)`. |
    | `T` | `multiplyMod(T value, UInt256 modulus)` Returns a value that is `((this * value) mod modulus)`. |
    | `default int` | `numberOfLeadingZeros()` Provides the number of zero bits preceding the highest-order one-bit. |
    | `default T` | `plus(long value)` Returns a value that is `(this + value)`. |
    | `default T` | `plus(T value)` Returns a value that is `(this + value)`. |
    | `T` | `pow(long exponent)` Returns a value that is `(this<sup>exponent</sup> mod 2<sup>256</sup>)` |
    | `T` | `pow(UInt256 exponent)` Returns a value that is `(this<sup>exponent</sup> mod 2<sup>256</sup>)` |
    | `T` | `subtract(long value)` Returns a value that is `(this - value)`. |
    | `T` | `subtract(T value)` Returns a value that is `(this - value)`. |
    | `default T` | `subtractExact(long value)` Returns a value that is `(this - value)`. |
    | `default T` | `subtractExact(T value)` Returns a value that is `(this - value)`. |
    | `default java.math.BigInteger` | `toBigInteger()` Provides the value as a BigInteger. |
    | `Bytes32` | `toBytes()` Provides the value as bytes. |
    | `default java.lang.String` | `toHexString()` This value represented as an hexadecimal string. |
    | `default long` | `toLong()` Provides the value as a long. |
    | `Bytes` | `toMinimalBytes()` Provides the value as bytes without any leading zero bytes. |
    | `default java.lang.String` | `toShortHexString()` Returns this value represented as a minimal hexadecimal string (without any leading zero) |
    | `UInt256` | `toUInt256()` Convert this value to a [`UInt256`](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256.html "class in org.tron.trident.crypto.tuwenitypes"). |

    - ### Methods inherited from interface java.lang.Comparable

      `compareTo`

* + ### Method Detail

    - #### isZero

      ```
      default boolean isZero()
      ```

      Returns true is the value is 0.

      Returns:
      :   True if this is the value 0.
    - #### add

      ```
      T add(T value)
      ```

      Returns a value that is `(this + value)`.

      Parameters:
      :   `value` - The amount to be added to this value.

      Returns:
      :   `this + value`
    - #### add

      ```
      T add(long value)
      ```

      Returns a value that is `(this + value)`.

      Parameters:
      :   `value` - The amount to be added to this value.

      Returns:
      :   `this + value`
    - #### plus

      ```
      default T plus(T value)
      ```

      Returns a value that is `(this + value)`.

      This notation can be used in Kotlin with the `+` operator.

      Parameters:
      :   `value` - The amount to be added to this value.

      Returns:
      :   `this + value`
    - #### plus

      ```
      default T plus(long value)
      ```

      Returns a value that is `(this + value)`.

      This notation can be used in Kotlin with the `+` operator.

      Parameters:
      :   `value` - The amount to be added to this value.

      Returns:
      :   `this + value`
    - #### addExact

      ```
      default T addExact(T value)
      ```

      Returns a value that is `(this + value)`.

      Parameters:
      :   `value` - the amount to be added to this value

      Returns:
      :   `this + value`

      Throws:
      :   `java.lang.ArithmeticException` - if the result of the addition overflows
    - #### addExact

      ```
      default T addExact(long value)
      ```

      Returns a value that is `(this + value)`.

      Parameters:
      :   `value` - the amount to be added to this value

      Returns:
      :   `this + value`

      Throws:
      :   `java.lang.ArithmeticException` - if the result of the addition overflows
    - #### addMod

      ```
      T addMod(T value,
               UInt256 modulus)
      ```

      Returns a value equivalent to `((this + value) mod modulus)`.

      Parameters:
      :   `value` - The amount to be added to this value.
      :   `modulus` - The modulus.

      Returns:
      :   `(this + value) mod modulus`

      Throws:
      :   `java.lang.ArithmeticException` - `modulus` == 0.
    - #### addMod

      ```
      T addMod(long value,
               UInt256 modulus)
      ```

      Returns a value equivalent to `((this + value) mod modulus)`.

      Parameters:
      :   `value` - The amount to be added to this value.
      :   `modulus` - The modulus.

      Returns:
      :   `(this + value) mod modulus`

      Throws:
      :   `java.lang.ArithmeticException` - `modulus` == 0.
    - #### addMod

      ```
      T addMod(long value,
               long modulus)
      ```

      Returns a value equivalent to `((this + value) mod modulus)`.

      Parameters:
      :   `value` - The amount to be added to this value.
      :   `modulus` - The modulus.

      Returns:
      :   `(this + value) mod modulus`

      Throws:
      :   `java.lang.ArithmeticException` - `modulus` ≤ 0.
    - #### subtract

      ```
      T subtract(T value)
      ```

      Returns a value that is `(this - value)`.

      Parameters:
      :   `value` - The amount to be subtracted from this value.

      Returns:
      :   `this - value`
    - #### subtract

      ```
      T subtract(long value)
      ```

      Returns a value that is `(this - value)`.

      Parameters:
      :   `value` - The amount to be subtracted from this value.

      Returns:
      :   `this - value`
    - #### subtractExact

      ```
      default T subtractExact(T value)
      ```

      Returns a value that is `(this - value)`.

      Parameters:
      :   `value` - the amount to be subtracted to this value

      Returns:
      :   `this - value`

      Throws:
      :   `java.lang.ArithmeticException` - if the result of the addition overflows
    - #### subtractExact

      ```
      default T subtractExact(long value)
      ```

      Returns a value that is `(this - value)`.

      Parameters:
      :   `value` - the amount to be subtracted to this value

      Returns:
      :   `this - value`

      Throws:
      :   `java.lang.ArithmeticException` - if the result of the addition overflows
    - #### multiply

      ```
      T multiply(T value)
      ```

      Returns a value that is `(this * value)`.

      Parameters:
      :   `value` - The amount to multiply this value by.

      Returns:
      :   `this * value`
    - #### multiply

      ```
      T multiply(long value)
      ```

      Returns a value that is `(this * value)`.

      Parameters:
      :   `value` - The amount to multiply this value by.

      Returns:
      :   `this * value`

      Throws:
      :   `java.lang.ArithmeticException` - `value` < 0.
    - #### multiplyMod

      ```
      T multiplyMod(T value,
                    UInt256 modulus)
      ```

      Returns a value that is `((this * value) mod modulus)`.

      Parameters:
      :   `value` - The amount to multiply this value by.
      :   `modulus` - The modulus.

      Returns:
      :   `(this * value) mod modulus`

      Throws:
      :   `java.lang.ArithmeticException` - `value` < 0 or `modulus` == 0.
    - #### multiplyMod

      ```
      T multiplyMod(long value,
                    UInt256 modulus)
      ```

      Returns a value that is `((this * value) mod modulus)`.

      Parameters:
      :   `value` - The amount to multiply this value by.
      :   `modulus` - The modulus.

      Returns:
      :   `(this * value) mod modulus`

      Throws:
      :   `java.lang.ArithmeticException` - `value` < 0 or `modulus` == 0.
    - #### multiplyMod

      ```
      T multiplyMod(long value,
                    long modulus)
      ```

      Returns a value that is `((this * value) mod modulus)`.

      Parameters:
      :   `value` - The amount to multiply this value by.
      :   `modulus` - The modulus.

      Returns:
      :   `(this * value) mod modulus`

      Throws:
      :   `java.lang.ArithmeticException` - `value` < 0 or `modulus` ≤ 0.
    - #### divide

      ```
      T divide(T value)
      ```

      Returns a value that is `(this / value)`.

      Parameters:
      :   `value` - The amount to divide this value by.

      Returns:
      :   `this / value`

      Throws:
      :   `java.lang.ArithmeticException` - `value` == 0.
    - #### divide

      ```
      T divide(long value)
      ```

      Returns a value that is `(this / value)`.

      Parameters:
      :   `value` - The amount to divide this value by.

      Returns:
      :   `this / value`

      Throws:
      :   `java.lang.ArithmeticException` - `value` ≤ 0.
    - #### divideCeil

      ```
      T divideCeil(T value)
      ```

      Returns a value that is `ceiling(this / value)`.

      Parameters:
      :   `value` - The amount to divide this value by.

      Returns:
      :   `this / value + ( this % value == 0 ? 0 : 1)`

      Throws:
      :   `java.lang.ArithmeticException` - `value` == 0.
    - #### divideCeil

      ```
      T divideCeil(long value)
      ```

      Returns a value that is `ceiling(this / value)`.

      Parameters:
      :   `value` - The amount to divide this value by.

      Returns:
      :   `this / value + ( this % value == 0 ? 0 : 1)`

      Throws:
      :   `java.lang.ArithmeticException` - `value` == 0.
    - #### pow

      ```
      T pow(UInt256 exponent)
      ```

      Returns a value that is `(this<sup>exponent</sup> mod 2<sup>256</sup>)`

      This calculates an exponentiation over the modulus of `2^256`.

      Note that `exponent` is an [`UInt256`](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256.html "class in org.tron.trident.crypto.tuwenitypes") rather than of the type `T`.

      Parameters:
      :   `exponent` - The exponent to which this value is to be raised.

      Returns:
      :   `this<sup>exponent</sup> mod 2<sup>256</sup>`
    - #### pow

      ```
      T pow(long exponent)
      ```

      Returns a value that is `(this<sup>exponent</sup> mod 2<sup>256</sup>)`

      This calculates an exponentiation over the modulus of `2^256`.

      Parameters:
      :   `exponent` - The exponent to which this value is to be raised.

      Returns:
      :   `this<sup>exponent</sup> mod 2<sup>256</sup>`
    - #### mod

      ```
      T mod(UInt256 modulus)
      ```

      Returns a value that is `(this mod modulus)`.

      Parameters:
      :   `modulus` - The modulus.

      Returns:
      :   `this mod modulus`.

      Throws:
      :   `java.lang.ArithmeticException` - `modulus` == 0.
    - #### mod

      ```
      T mod(long modulus)
      ```

      Returns a value that is `(this mod modulus)`.

      Parameters:
      :   `modulus` - The modulus.

      Returns:
      :   `this mod modulus`.

      Throws:
      :   `java.lang.ArithmeticException` - `modulus` ≤ 0.
    - #### mod0

      ```
      T mod0(UInt256 modulus)
      ```

      Returns a value that is `(this mod modulus)`, or 0 if modulus is 0.

      Parameters:
      :   `modulus` - The modulus.

      Returns:
      :   `this mod modulus`.
    - #### mod0

      ```
      T mod0(long modulus)
      ```

      Returns a value that is `(this mod modulus)`, or 0 if modulus is 0.

      Parameters:
      :   `modulus` - The modulus.

      Returns:
      :   `this mod modulus`.
    - #### fitsInt

      ```
      default boolean fitsInt()
      ```

      Returns true if the value can fit in an int.

      Returns:
      :   True if this value fits a java `int` (i.e. is less or equal to `Integer.MAX_VALUE`).
    - #### intValue

      ```
      default int intValue()
      ```

      Provides this value as an int.

      Returns:
      :   This value as a java `int` assuming it is small enough to fit an `int`.

      Throws:
      :   `java.lang.ArithmeticException` - If the value does not fit an `int`, that is if `!fitsInt()`.
    - #### fitsLong

      ```
      default boolean fitsLong()
      ```

      Returns true if the value can fit in a long.

      Returns:
      :   True if this value fits a java `long` (i.e. is less or equal to `Long.MAX_VALUE`).
    - #### toLong

      ```
      default long toLong()
      ```

      Provides the value as a long.

      Returns:
      :   This value as a java `long` assuming it is small enough to fit a `long`.

      Throws:
      :   `java.lang.ArithmeticException` - If the value does not fit a `long`, that is if `!fitsLong()`.
    - #### toBigInteger

      ```
      default java.math.BigInteger toBigInteger()
      ```

      Provides the value as a BigInteger.

      Returns:
      :   This value as a `BigInteger`.
    - #### toHexString

      ```
      default java.lang.String toHexString()
      ```

      This value represented as an hexadecimal string.

      Note that this representation includes all the 32 underlying bytes, no matter what the integer actually represents
      (in other words, it can have many leading zeros). For a shorter representation that don't include leading zeros,
      use [`toShortHexString()`](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256Value.html#toShortHexString--).

      Returns:
      :   This value represented as an hexadecimal string.
    - #### toShortHexString

      ```
      default java.lang.String toShortHexString()
      ```

      Returns this value represented as a minimal hexadecimal string (without any leading zero)

      Returns:
      :   This value represented as a minimal hexadecimal string (without any leading zero).
    - #### toUInt256

      ```
      UInt256 toUInt256()
      ```

      Convert this value to a [`UInt256`](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256.html "class in org.tron.trident.crypto.tuwenitypes").

      Returns:
      :   This value as a [`UInt256`](../../../../../org/tron/trident/crypto/tuwenitypes/UInt256.html "class in org.tron.trident.crypto.tuwenitypes").
    - #### toBytes

      ```
      Bytes32 toBytes()
      ```

      Provides the value as bytes.

      Returns:
      :   The value as bytes.
    - #### toMinimalBytes

      ```
      Bytes toMinimalBytes()
      ```

      Provides the value as bytes without any leading zero bytes.

      Returns:
      :   The value as bytes without any leading zero bytes.
    - #### numberOfLeadingZeros

      ```
      default int numberOfLeadingZeros()
      ```

      Provides the number of zero bits preceding the highest-order one-bit.

      Returns:
      :   the number of zero bits preceding the highest-order ("leftmost") one-bit in the binary representation of
          this value, or 256 if the value is equal to zero.
    - #### bitLength

      ```
      default int bitLength()
      ```

      Provides the number of bits following and including the highest-order ("leftmost") one-bit in the binary
      representation of this value, or zero if all bits are zero.

      Returns:
      :   The number of bits following and including the highest-order ("leftmost") one-bit in the binary
          representation of this value, or zero if all bits are zero.