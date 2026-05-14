

org.tron.trident.abi.datatypes

## Class DynamicArray<T extends [Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")>

* java.lang.Object
* + [org.tron.trident.abi.datatypes.Array](../../../../../org/tron/trident/abi/datatypes/Array.html "class in org.tron.trident.abi.datatypes")<T>
  + - org.tron.trident.abi.datatypes.DynamicArray<T>

* All Implemented Interfaces:
  :   [Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")<java.util.List<T>>

  Direct Known Subclasses:
  :   [DynamicStruct](../../../../../org/tron/trident/abi/datatypes/DynamicStruct.html "class in org.tron.trident.abi.datatypes")

  ---

    

  ```
  public class DynamicArray<T extends Type>
  extends Array<T>
  ```

  Dynamic array type.

* + ### Field Summary

    - ### Fields inherited from class org.tron.trident.abi.datatypes.[Array](../../../../../org/tron/trident/abi/datatypes/Array.html "class in org.tron.trident.abi.datatypes")

      `value`
    - ### Fields inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `MAX_BIT_LENGTH, MAX_BYTE_LENGTH`
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `DynamicArray(java.lang.Class<T> type, java.util.List<T> values)` |
    | `DynamicArray(java.lang.Class<T> type, T... values)` |
    | `DynamicArray(java.util.List<T> values)` Deprecated. |
    | `DynamicArray(T... values)` Deprecated. |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `int` | `bytes32PaddedLength()` |
    | `static DynamicArray` | `empty(java.lang.String type)` Deprecated. |
    | `java.lang.String` | `getTypeAsString()` |

    - ### Methods inherited from class org.tron.trident.abi.datatypes.[Array](../../../../../org/tron/trident/abi/datatypes/Array.html "class in org.tron.trident.abi.datatypes")

      `equals, getComponentType, getValue, hashCode`
    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### DynamicArray

      ```
      @Deprecated
       @SafeVarargs
      public DynamicArray(T... values)
      ```

      Deprecated.
    - #### DynamicArray

      ```
      @Deprecated
      public DynamicArray(java.util.List<T> values)
      ```

      Deprecated.
    - #### DynamicArray

      ```
      public DynamicArray(java.lang.Class<T> type,
                          java.util.List<T> values)
      ```
    - #### DynamicArray

      ```
      @SafeVarargs
      public DynamicArray(java.lang.Class<T> type,
                                       T... values)
      ```
  + ### Method Detail

    - #### empty

      ```
      @Deprecated
      public static DynamicArray empty(java.lang.String type)
      ```

      Deprecated.
    - #### bytes32PaddedLength

      ```
      public int bytes32PaddedLength()
      ```

      Specified by:
      :   `bytes32PaddedLength` in interface `Type<java.util.List<T extends Type>>`

      Overrides:
      :   `bytes32PaddedLength` in class `Array<T extends Type>`
    - #### getTypeAsString

      ```
      public java.lang.String getTypeAsString()
      ```

      Specified by:
      :   `getTypeAsString` in interface `Type<java.util.List<T extends Type>>`

      Specified by:
      :   `getTypeAsString` in class `Array<T extends Type>`