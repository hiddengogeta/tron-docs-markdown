

org.tron.trident.abi.datatypes

## Class StaticStruct

* java.lang.Object
* + [org.tron.trident.abi.datatypes.Array](../../../../../org/tron/trident/abi/datatypes/Array.html "class in org.tron.trident.abi.datatypes")<T>
  + - [org.tron.trident.abi.datatypes.StaticArray](../../../../../org/tron/trident/abi/datatypes/StaticArray.html "class in org.tron.trident.abi.datatypes")<[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")>
    - * org.tron.trident.abi.datatypes.StaticStruct

* All Implemented Interfaces:
  :   [StructType](../../../../../org/tron/trident/abi/datatypes/StructType.html "interface in org.tron.trident.abi.datatypes"), [Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")<java.util.List<[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")>>

  ---

    

  ```
  public class StaticStruct
  extends StaticArray<Type>
  implements StructType
  ```

* + ### Field Summary

    - ### Fields inherited from class org.tron.trident.abi.datatypes.[StaticArray](../../../../../org/tron/trident/abi/datatypes/StaticArray.html "class in org.tron.trident.abi.datatypes")

      `MAX_SIZE_OF_STATIC_ARRAY`
    - ### Fields inherited from class org.tron.trident.abi.datatypes.[Array](../../../../../org/tron/trident/abi/datatypes/Array.html "class in org.tron.trident.abi.datatypes")

      `value`
    - ### Fields inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `MAX_BIT_LENGTH, MAX_BYTE_LENGTH`
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `StaticStruct(java.util.List<Type> values)` |
    | `StaticStruct(Type... values)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `java.lang.String` | `getTypeAsString()` |

    - ### Methods inherited from class org.tron.trident.abi.datatypes.[StaticArray](../../../../../org/tron/trident/abi/datatypes/StaticArray.html "class in org.tron.trident.abi.datatypes")

      `getValue`
    - ### Methods inherited from class org.tron.trident.abi.datatypes.[Array](../../../../../org/tron/trident/abi/datatypes/Array.html "class in org.tron.trident.abi.datatypes")

      `bytes32PaddedLength, equals, getComponentType, hashCode`
    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### StaticStruct

      ```
      public StaticStruct(java.util.List<Type> values)
      ```
    - #### StaticStruct

      ```
      @SafeVarargs
      public StaticStruct(Type... values)
      ```
  + ### Method Detail

    - #### getTypeAsString

      ```
      public java.lang.String getTypeAsString()
      ```

      Specified by:
      :   `getTypeAsString` in interface `Type<java.util.List<Type>>`

      Overrides:
      :   `getTypeAsString` in class `StaticArray<Type>`