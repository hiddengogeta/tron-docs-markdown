

org.tron.trident.abi.datatypes

## Class NumericType

* java.lang.Object
* + org.tron.trident.abi.datatypes.NumericType

* All Implemented Interfaces:
  :   [Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")<java.math.BigInteger>

  Direct Known Subclasses:
  :   [FixedPointType](../../../../../org/tron/trident/abi/datatypes/FixedPointType.html "class in org.tron.trident.abi.datatypes"), [IntType](../../../../../org/tron/trident/abi/datatypes/IntType.html "class in org.tron.trident.abi.datatypes")

  ---

    

  ```
  public abstract class NumericType
  extends java.lang.Object
  implements Type<java.math.BigInteger>
  ```

  Common numeric type.

* + ### Field Summary

    - ### Fields inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `MAX_BIT_LENGTH, MAX_BYTE_LENGTH`
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `NumericType(java.lang.String type, java.math.BigInteger value)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `boolean` | `equals(java.lang.Object o)` |
    | `abstract int` | `getBitSize()` |
    | `java.lang.String` | `getTypeAsString()` |
    | `java.math.BigInteger` | `getValue()` |
    | `int` | `hashCode()` |

    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`
    - ### Methods inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `bytes32PaddedLength`

* + ### Constructor Detail

    - #### NumericType

      ```
      public NumericType(java.lang.String type,
                         java.math.BigInteger value)
      ```
  + ### Method Detail

    - #### getTypeAsString

      ```
      public java.lang.String getTypeAsString()
      ```

      Specified by:
      :   `getTypeAsString` in interface `Type<java.math.BigInteger>`
    - #### getValue

      ```
      public java.math.BigInteger getValue()
      ```

      Specified by:
      :   `getValue` in interface `Type<java.math.BigInteger>`
    - #### getBitSize

      ```
      public abstract int getBitSize()
      ```
    - #### equals

      ```
      public boolean equals(java.lang.Object o)
      ```

      Overrides:
      :   `equals` in class `java.lang.Object`
    - #### hashCode

      ```
      public int hashCode()
      ```

      Overrides:
      :   `hashCode` in class `java.lang.Object`