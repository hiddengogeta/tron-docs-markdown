

org.tron.trident.abi.datatypes

## Class StaticArray<T extends [Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")>

* java.lang.Object
* + [org.tron.trident.abi.datatypes.Array](../../../../../org/tron/trident/abi/datatypes/Array.html "class in org.tron.trident.abi.datatypes")<T>
  + - org.tron.trident.abi.datatypes.StaticArray<T>

* All Implemented Interfaces:
  :   [Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")<java.util.List<T>>

  Direct Known Subclasses:
  :   [StaticArray1](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray1.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray10](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray10.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray11](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray11.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray12](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray12.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray13](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray13.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray14](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray14.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray15](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray15.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray16](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray16.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray17](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray17.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray18](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray18.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray19](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray19.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray2](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray2.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray20](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray20.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray21](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray21.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray22](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray22.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray23](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray23.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray24](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray24.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray25](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray25.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray26](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray26.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray27](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray27.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray28](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray28.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray29](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray29.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray3](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray3.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray30](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray30.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray31](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray31.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray32](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray32.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray4](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray4.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray5](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray5.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray6](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray6.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray7](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray7.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray8](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray8.html "class in org.tron.trident.abi.datatypes.generated"), [StaticArray9](../../../../../org/tron/trident/abi/datatypes/generated/StaticArray9.html "class in org.tron.trident.abi.datatypes.generated"), [StaticStruct](../../../../../org/tron/trident/abi/datatypes/StaticStruct.html "class in org.tron.trident.abi.datatypes")

  ---

    

  ```
  public abstract class StaticArray<T extends Type>
  extends Array<T>
  ```

  Static array type.

* + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `MAX_SIZE_OF_STATIC_ARRAY` Warning: increasing this constant will cause more generated StaticArrayN types, see: org.tron.trident.codegen.AbiTypesGenerator#generateStaticArrayTypes |

    - ### Fields inherited from class org.tron.trident.abi.datatypes.[Array](../../../../../org/tron/trident/abi/datatypes/Array.html "class in org.tron.trident.abi.datatypes")

      `value`
    - ### Fields inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `MAX_BIT_LENGTH, MAX_BYTE_LENGTH`
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `StaticArray(java.lang.Class<T> type, int expectedSize, java.util.List<T> values)` |
    | `StaticArray(java.lang.Class<T> type, int expectedSize, T... values)` |
    | `StaticArray(java.lang.Class<T> type, java.util.List<T> values)` |
    | `StaticArray(java.lang.Class<T> type, T... values)` |
    | `StaticArray(int expectedSize, java.util.List<T> values)` Deprecated. |
    | `StaticArray(int expectedSize, T... values)` Deprecated. |
    | `StaticArray(java.util.List<T> values)` Deprecated. |
    | `StaticArray(T... values)` Deprecated. |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `java.lang.String` | `getTypeAsString()` |
    | `java.util.List<T>` | `getValue()` |

    - ### Methods inherited from class org.tron.trident.abi.datatypes.[Array](../../../../../org/tron/trident/abi/datatypes/Array.html "class in org.tron.trident.abi.datatypes")

      `bytes32PaddedLength, equals, getComponentType, hashCode`
    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

* + ### Field Detail

    - #### MAX\_SIZE\_OF\_STATIC\_ARRAY

      ```
      public static final int MAX_SIZE_OF_STATIC_ARRAY
      ```

      Warning: increasing this constant will cause more generated StaticArrayN types, see:
      org.tron.trident.codegen.AbiTypesGenerator#generateStaticArrayTypes

      See Also:
      :   [Constant Field Values](../../../../../constant-values.html#org.tron.trident.abi.datatypes.StaticArray.MAX_SIZE_OF_STATIC_ARRAY)
  + ### Constructor Detail

    - #### StaticArray

      ```
      @Deprecated
       @SafeVarargs
      public StaticArray(T... values)
      ```

      Deprecated.
    - #### StaticArray

      ```
      @Deprecated
       @SafeVarargs
      public StaticArray(int expectedSize,
                                                   T... values)
      ```

      Deprecated.
    - #### StaticArray

      ```
      @Deprecated
      public StaticArray(java.util.List<T> values)
      ```

      Deprecated.
    - #### StaticArray

      ```
      @Deprecated
      public StaticArray(int expectedSize,
                                     java.util.List<T> values)
      ```

      Deprecated.
    - #### StaticArray

      ```
      @SafeVarargs
      public StaticArray(java.lang.Class<T> type,
                                      T... values)
      ```
    - #### StaticArray

      ```
      @SafeVarargs
      public StaticArray(java.lang.Class<T> type,
                                      int expectedSize,
                                      T... values)
      ```
    - #### StaticArray

      ```
      public StaticArray(java.lang.Class<T> type,
                         java.util.List<T> values)
      ```
    - #### StaticArray

      ```
      public StaticArray(java.lang.Class<T> type,
                         int expectedSize,
                         java.util.List<T> values)
      ```
  + ### Method Detail

    - #### getValue

      ```
      public java.util.List<T> getValue()
      ```

      Specified by:
      :   `getValue` in interface `Type<java.util.List<T extends Type>>`

      Overrides:
      :   `getValue` in class `Array<T extends Type>`
    - #### getTypeAsString

      ```
      public java.lang.String getTypeAsString()
      ```

      Specified by:
      :   `getTypeAsString` in interface `Type<java.util.List<T extends Type>>`

      Specified by:
      :   `getTypeAsString` in class `Array<T extends Type>`