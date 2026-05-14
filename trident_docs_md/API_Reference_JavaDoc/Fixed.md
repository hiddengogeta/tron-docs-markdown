

org.tron.trident.abi.datatypes

## Class Fixed

* java.lang.Object
* + [org.tron.trident.abi.datatypes.NumericType](../../../../../org/tron/trident/abi/datatypes/NumericType.html "class in org.tron.trident.abi.datatypes")
  + - [org.tron.trident.abi.datatypes.FixedPointType](../../../../../org/tron/trident/abi/datatypes/FixedPointType.html "class in org.tron.trident.abi.datatypes")
    - * org.tron.trident.abi.datatypes.Fixed

* All Implemented Interfaces:
  :   [Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")<java.math.BigInteger>

  ---

    

  ```
  public class Fixed
  extends FixedPointType
  ```

  Signed fixed type.

* + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static Fixed` | `DEFAULT` |
    | `static java.lang.String` | `TYPE_NAME` |

    - ### Fields inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `MAX_BIT_LENGTH, MAX_BYTE_LENGTH`
  + ### Constructor Summary

    Constructors

    | Modifier | Constructor and Description |
    |  | `Fixed(java.math.BigInteger value)` |
    |  | `Fixed(java.math.BigInteger m, java.math.BigInteger n)` |
    | `protected` | `Fixed(int mBitSize, int nBitSize, java.math.BigInteger value)` |
    | `protected` | `Fixed(int mBitSize, int nBitSize, java.math.BigInteger m, java.math.BigInteger n)` |
  + ### Method Summary

    - ### Methods inherited from class org.tron.trident.abi.datatypes.[FixedPointType](../../../../../org/tron/trident/abi/datatypes/FixedPointType.html "class in org.tron.trident.abi.datatypes")

      `getBitSize`
    - ### Methods inherited from class org.tron.trident.abi.datatypes.[NumericType](../../../../../org/tron/trident/abi/datatypes/NumericType.html "class in org.tron.trident.abi.datatypes")

      `equals, getTypeAsString, getValue, hashCode`
    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`
    - ### Methods inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `bytes32PaddedLength`

* + ### Field Detail

    - #### TYPE\_NAME

      ```
      public static final java.lang.String TYPE_NAME
      ```

      See Also:
      :   [Constant Field Values](../../../../../constant-values.html#org.tron.trident.abi.datatypes.Fixed.TYPE_NAME)
    - #### DEFAULT

      ```
      public static final Fixed DEFAULT
      ```
  + ### Constructor Detail

    - #### Fixed

      ```
      protected Fixed(int mBitSize,
                      int nBitSize,
                      java.math.BigInteger value)
      ```
    - #### Fixed

      ```
      public Fixed(java.math.BigInteger value)
      ```
    - #### Fixed

      ```
      public Fixed(java.math.BigInteger m,
                   java.math.BigInteger n)
      ```
    - #### Fixed

      ```
      protected Fixed(int mBitSize,
                      int nBitSize,
                      java.math.BigInteger m,
                      java.math.BigInteger n)
      ```