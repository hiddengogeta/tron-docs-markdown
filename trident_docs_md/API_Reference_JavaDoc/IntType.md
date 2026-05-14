

org.tron.trident.abi.datatypes

## Class IntType

* java.lang.Object
* + [org.tron.trident.abi.datatypes.NumericType](../../../../../org/tron/trident/abi/datatypes/NumericType.html "class in org.tron.trident.abi.datatypes")
  + - org.tron.trident.abi.datatypes.IntType

* All Implemented Interfaces:
  :   [Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")<java.math.BigInteger>

  Direct Known Subclasses:
  :   [Int](../../../../../org/tron/trident/abi/datatypes/Int.html "class in org.tron.trident.abi.datatypes"), [TrcToken](../../../../../org/tron/trident/abi/datatypes/TrcToken.html "class in org.tron.trident.abi.datatypes"), [Uint](../../../../../org/tron/trident/abi/datatypes/Uint.html "class in org.tron.trident.abi.datatypes")

  ---

    

  ```
  public abstract class IntType
  extends NumericType
  ```

  Common integer properties.

* + ### Field Summary

    - ### Fields inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `MAX_BIT_LENGTH, MAX_BYTE_LENGTH`
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `IntType(java.lang.String typePrefix, int bitSize, java.math.BigInteger value)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `int` | `getBitSize()` |
    | `protected boolean` | `valid()` |

    - ### Methods inherited from class org.tron.trident.abi.datatypes.[NumericType](../../../../../org/tron/trident/abi/datatypes/NumericType.html "class in org.tron.trident.abi.datatypes")

      `equals, getTypeAsString, getValue, hashCode`
    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`
    - ### Methods inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `bytes32PaddedLength`

* + ### Constructor Detail

    - #### IntType

      ```
      public IntType(java.lang.String typePrefix,
                     int bitSize,
                     java.math.BigInteger value)
      ```
  + ### Method Detail

    - #### getBitSize

      ```
      public int getBitSize()
      ```

      Specified by:
      :   `getBitSize` in class `NumericType`
    - #### valid

      ```
      protected boolean valid()
      ```