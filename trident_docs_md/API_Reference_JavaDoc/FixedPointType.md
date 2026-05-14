

org.tron.trident.abi.datatypes

## Class FixedPointType

* java.lang.Object
* + [org.tron.trident.abi.datatypes.NumericType](../../../../../org/tron/trident/abi/datatypes/NumericType.html "class in org.tron.trident.abi.datatypes")
  + - org.tron.trident.abi.datatypes.FixedPointType

* All Implemented Interfaces:
  :   [Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")<java.math.BigInteger>

  Direct Known Subclasses:
  :   [Fixed](../../../../../org/tron/trident/abi/datatypes/Fixed.html "class in org.tron.trident.abi.datatypes"), [Ufixed](../../../../../org/tron/trident/abi/datatypes/Ufixed.html "class in org.tron.trident.abi.datatypes")

  ---

    

  ```
  public abstract class FixedPointType
  extends NumericType
  ```

  Common fixed-point type properties.

* + ### Field Summary

    - ### Fields inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `MAX_BIT_LENGTH, MAX_BYTE_LENGTH`
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `FixedPointType(java.lang.String typePrefix, int mBitSize, int nBitSize, java.math.BigInteger value)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `int` | `getBitSize()` |

    - ### Methods inherited from class org.tron.trident.abi.datatypes.[NumericType](../../../../../org/tron/trident/abi/datatypes/NumericType.html "class in org.tron.trident.abi.datatypes")

      `equals, getTypeAsString, getValue, hashCode`
    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`
    - ### Methods inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `bytes32PaddedLength`

* + ### Constructor Detail

    - #### FixedPointType

      ```
      public FixedPointType(java.lang.String typePrefix,
                            int mBitSize,
                            int nBitSize,
                            java.math.BigInteger value)
      ```
  + ### Method Detail

    - #### getBitSize

      ```
      public int getBitSize()
      ```

      Specified by:
      :   `getBitSize` in class `NumericType`