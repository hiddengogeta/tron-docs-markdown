

org.tron.trident.abi.datatypes.primitive

## Class Float

* java.lang.Object
* + [org.tron.trident.abi.datatypes.primitive.PrimitiveType](../../../../../../org/tron/trident/abi/datatypes/primitive/PrimitiveType.html "class in org.tron.trident.abi.datatypes.primitive")<T>
  + - [org.tron.trident.abi.datatypes.primitive.Number](../../../../../../org/tron/trident/abi/datatypes/primitive/Number.html "class in org.tron.trident.abi.datatypes.primitive")<java.lang.Float>
    - * org.tron.trident.abi.datatypes.primitive.Float

* All Implemented Interfaces:
  :   [Type](../../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")<java.lang.Float>

  ---

    

  ```
  public class Float
  extends Number<java.lang.Float>
  ```

* + ### Field Summary

    - ### Fields inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `MAX_BIT_LENGTH, MAX_BYTE_LENGTH`
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `Float(float value)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `NumericType` | `toSolidityType()` |

    - ### Methods inherited from class org.tron.trident.abi.datatypes.primitive.[PrimitiveType](../../../../../../org/tron/trident/abi/datatypes/primitive/PrimitiveType.html "class in org.tron.trident.abi.datatypes.primitive")

      `equals, getTypeAsString, getValue, hashCode`
    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`
    - ### Methods inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `bytes32PaddedLength`

* + ### Constructor Detail

    - #### Float

      ```
      public Float(float value)
      ```
  + ### Method Detail

    - #### toSolidityType

      ```
      public NumericType toSolidityType()
      ```

      Specified by:
      :   `toSolidityType` in class `Number<java.lang.Float>`