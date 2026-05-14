

org.tron.trident.abi.datatypes.primitive

## Class Char

* java.lang.Object
* + [org.tron.trident.abi.datatypes.primitive.PrimitiveType](../../../../../../org/tron/trident/abi/datatypes/primitive/PrimitiveType.html "class in org.tron.trident.abi.datatypes.primitive")<java.lang.Character>
  + - org.tron.trident.abi.datatypes.primitive.Char

* All Implemented Interfaces:
  :   [Type](../../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")<java.lang.Character>

  ---

    

  ```
  public final class Char
  extends PrimitiveType<java.lang.Character>
  ```

* + ### Field Summary

    - ### Fields inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `MAX_BIT_LENGTH, MAX_BYTE_LENGTH`
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `Char(char value)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Type` | `toSolidityType()` |

    - ### Methods inherited from class org.tron.trident.abi.datatypes.primitive.[PrimitiveType](../../../../../../org/tron/trident/abi/datatypes/primitive/PrimitiveType.html "class in org.tron.trident.abi.datatypes.primitive")

      `equals, getTypeAsString, getValue, hashCode`
    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`
    - ### Methods inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `bytes32PaddedLength`

* + ### Constructor Detail

    - #### Char

      ```
      public Char(char value)
      ```
  + ### Method Detail

    - #### toSolidityType

      ```
      public Type toSolidityType()
      ```

      Specified by:
      :   `toSolidityType` in class `PrimitiveType<java.lang.Character>`