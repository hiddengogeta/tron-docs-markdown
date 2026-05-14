

org.tron.trident.abi.datatypes

## Class DynamicStruct

* java.lang.Object
* + [org.tron.trident.abi.datatypes.Array](../../../../../org/tron/trident/abi/datatypes/Array.html "class in org.tron.trident.abi.datatypes")<T>
  + - [org.tron.trident.abi.datatypes.DynamicArray](../../../../../org/tron/trident/abi/datatypes/DynamicArray.html "class in org.tron.trident.abi.datatypes")<[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")>
    - * org.tron.trident.abi.datatypes.DynamicStruct

* All Implemented Interfaces:
  :   [StructType](../../../../../org/tron/trident/abi/datatypes/StructType.html "interface in org.tron.trident.abi.datatypes"), [Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")<java.util.List<[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")>>

  ---

    

  ```
  public class DynamicStruct
  extends DynamicArray<Type>
  implements StructType
  ```

* + ### Field Summary

    - ### Fields inherited from class org.tron.trident.abi.datatypes.[Array](../../../../../org/tron/trident/abi/datatypes/Array.html "class in org.tron.trident.abi.datatypes")

      `value`
    - ### Fields inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `MAX_BIT_LENGTH, MAX_BYTE_LENGTH`
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `DynamicStruct(java.lang.Class<Type> type, Type... values)` |
    | `DynamicStruct(java.util.List<Type> values)` |
    | `DynamicStruct(Type... values)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `int` | `bytes32PaddedLength()` |
    | `java.lang.String` | `getTypeAsString()` |

    - ### Methods inherited from class org.tron.trident.abi.datatypes.[DynamicArray](../../../../../org/tron/trident/abi/datatypes/DynamicArray.html "class in org.tron.trident.abi.datatypes")

      `empty`
    - ### Methods inherited from class org.tron.trident.abi.datatypes.[Array](../../../../../org/tron/trident/abi/datatypes/Array.html "class in org.tron.trident.abi.datatypes")

      `equals, getComponentType, getValue, hashCode`
    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### DynamicStruct

      ```
      public DynamicStruct(java.util.List<Type> values)
      ```
    - #### DynamicStruct

      ```
      public DynamicStruct(Type... values)
      ```
    - #### DynamicStruct

      ```
      @SafeVarargs
      public DynamicStruct(java.lang.Class<Type> type,
                                        Type... values)
      ```
  + ### Method Detail

    - #### bytes32PaddedLength

      ```
      public int bytes32PaddedLength()
      ```

      Specified by:
      :   `bytes32PaddedLength` in interface `Type<java.util.List<Type>>`

      Overrides:
      :   `bytes32PaddedLength` in class `DynamicArray<Type>`
    - #### getTypeAsString

      ```
      public java.lang.String getTypeAsString()
      ```

      Specified by:
      :   `getTypeAsString` in interface `Type<java.util.List<Type>>`

      Overrides:
      :   `getTypeAsString` in class `DynamicArray<Type>`