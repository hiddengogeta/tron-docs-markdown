

org.tron.trident.abi.datatypes.generated

## Class StaticArray24<T extends [Type](../../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")>

* java.lang.Object
* + [org.tron.trident.abi.datatypes.Array](../../../../../../org/tron/trident/abi/datatypes/Array.html "class in org.tron.trident.abi.datatypes")<T>
  + - [org.tron.trident.abi.datatypes.StaticArray](../../../../../../org/tron/trident/abi/datatypes/StaticArray.html "class in org.tron.trident.abi.datatypes")<T>
    - * org.tron.trident.abi.datatypes.generated.StaticArray24<T>

* All Implemented Interfaces:
  :   [Type](../../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")<java.util.List<T>>

  ---

    

  ```
  public class StaticArray24<T extends Type>
  extends StaticArray<T>
  ```

  Auto generated code.

  **Do not modifiy!**

  Please use org.tron.trident.codegen.AbiTypesGenerator in the
  [codegen module](https://github.com/web3j/web3j/tree/master/codegen) to update.

* + ### Field Summary

    - ### Fields inherited from class org.tron.trident.abi.datatypes.[StaticArray](../../../../../../org/tron/trident/abi/datatypes/StaticArray.html "class in org.tron.trident.abi.datatypes")

      `MAX_SIZE_OF_STATIC_ARRAY`
    - ### Fields inherited from class org.tron.trident.abi.datatypes.[Array](../../../../../../org/tron/trident/abi/datatypes/Array.html "class in org.tron.trident.abi.datatypes")

      `value`
    - ### Fields inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `MAX_BIT_LENGTH, MAX_BYTE_LENGTH`
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `StaticArray24(java.lang.Class<T> type, java.util.List<T> values)` |
    | `StaticArray24(java.lang.Class<T> type, T... values)` |
    | `StaticArray24(java.util.List<T> values)` Deprecated. |
    | `StaticArray24(T... values)` Deprecated. |
  + ### Method Summary

    - ### Methods inherited from class org.tron.trident.abi.datatypes.[StaticArray](../../../../../../org/tron/trident/abi/datatypes/StaticArray.html "class in org.tron.trident.abi.datatypes")

      `getTypeAsString, getValue`
    - ### Methods inherited from class org.tron.trident.abi.datatypes.[Array](../../../../../../org/tron/trident/abi/datatypes/Array.html "class in org.tron.trident.abi.datatypes")

      `bytes32PaddedLength, equals, getComponentType, hashCode`
    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### StaticArray24

      ```
      @Deprecated
      public StaticArray24(java.util.List<T> values)
      ```

      Deprecated.
    - #### StaticArray24

      ```
      @Deprecated
       @SafeVarargs
      public StaticArray24(T... values)
      ```

      Deprecated.
    - #### StaticArray24

      ```
      public StaticArray24(java.lang.Class<T> type,
                           java.util.List<T> values)
      ```
    - #### StaticArray24

      ```
      @SafeVarargs
      public StaticArray24(java.lang.Class<T> type,
                                        T... values)
      ```