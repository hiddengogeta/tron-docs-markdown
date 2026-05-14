

org.tron.trident.abi.datatypes

## Class Ufixed

* java.lang.Object
* + [org.tron.trident.abi.datatypes.NumericType](../../../../../org/tron/trident/abi/datatypes/NumericType.html "class in org.tron.trident.abi.datatypes")
  + - [org.tron.trident.abi.datatypes.FixedPointType](../../../../../org/tron/trident/abi/datatypes/FixedPointType.html "class in org.tron.trident.abi.datatypes")
    - * org.tron.trident.abi.datatypes.Ufixed

* All Implemented Interfaces:
  :   [Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")<java.math.BigInteger>

  ---

    

  ```
  public class Ufixed
  extends FixedPointType
  ```

  Signed fixed type.

* + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static Ufixed` | `DEFAULT` |
    | `static java.lang.String` | `TYPE_NAME` |

    - ### Fields inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `MAX_BIT_LENGTH, MAX_BYTE_LENGTH`
  + ### Constructor Summary

    Constructors

    | Modifier | Constructor and Description |
    |  | `Ufixed(java.math.BigInteger value)` |
    |  | `Ufixed(java.math.BigInteger m, java.math.BigInteger n)` |
    | `protected` | `Ufixed(int mBitSize, int nBitSize, java.math.BigInteger value)` |
    | `protected` | `Ufixed(int mBitSize, int nBitSize, java.math.BigInteger m, java.math.BigInteger n)` |
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
      :   [Constant Field Values](../../../../../constant-values.html#org.tron.trident.abi.datatypes.Ufixed.TYPE_NAME)
    - #### DEFAULT

      ```
      public static final Ufixed DEFAULT
      ```
  + ### Constructor Detail

    - #### Ufixed

      ```
      protected Ufixed(int mBitSize,
                       int nBitSize,
                       java.math.BigInteger value)
      ```
    - #### Ufixed

      ```
      public Ufixed(java.math.BigInteger value)
      ```
    - #### Ufixed

      ```
      public Ufixed(java.math.BigInteger m,
                    java.math.BigInteger n)
      ```
    - #### Ufixed

      ```
      protected Ufixed(int mBitSize,
                       int nBitSize,
                       java.math.BigInteger m,
                       java.math.BigInteger n)
      ```