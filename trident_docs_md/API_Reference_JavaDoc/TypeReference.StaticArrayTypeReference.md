

org.tron.trident.abi

## Class TypeReference.StaticArrayTypeReference<T extends [Type](../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")>

* java.lang.Object
* + [org.tron.trident.abi.TypeReference](../../../../org/tron/trident/abi/TypeReference.html "class in org.tron.trident.abi")<T>
  + - org.tron.trident.abi.TypeReference.StaticArrayTypeReference<T>

* All Implemented Interfaces:
  :   java.lang.Comparable<[TypeReference](../../../../org/tron/trident/abi/TypeReference.html "class in org.tron.trident.abi")<T>>

  Enclosing class:
  :   [TypeReference](../../../../org/tron/trident/abi/TypeReference.html "class in org.tron.trident.abi")<[T](../../../../org/tron/trident/abi/TypeReference.html "type parameter in TypeReference") extends [Type](../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")>

  ---

    

  ```
  public abstract static class TypeReference.StaticArrayTypeReference<T extends Type>
  extends TypeReference<T>
  ```

* + ### Nested Class Summary

    - ### Nested classes/interfaces inherited from class org.tron.trident.abi.[TypeReference](../../../../org/tron/trident/abi/TypeReference.html "class in org.tron.trident.abi")

      `TypeReference.StaticArrayTypeReference<T extends Type>`
  + ### Field Summary

    - ### Fields inherited from class org.tron.trident.abi.[TypeReference](../../../../org/tron/trident/abi/TypeReference.html "class in org.tron.trident.abi")

      `ARRAY_SUFFIX`
  + ### Constructor Summary

    Constructors

    | Modifier | Constructor and Description |
    | `protected` | `StaticArrayTypeReference(int size)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `int` | `getSize()` |

    - ### Methods inherited from class org.tron.trident.abi.[TypeReference](../../../../org/tron/trident/abi/TypeReference.html "class in org.tron.trident.abi")

      `compareTo, create, create, getAtomicTypeClass, getClassType, getType, isIndexed, makeTypeReference, makeTypeReference`
    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### StaticArrayTypeReference

      ```
      protected StaticArrayTypeReference(int size)
      ```
  + ### Method Detail

    - #### getSize

      ```
      public int getSize()
      ```