

org.tron.trident.abi

## Class TypeReference<T extends [Type](../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")>

* java.lang.Object
* + org.tron.trident.abi.TypeReference<T>

* All Implemented Interfaces:
  :   java.lang.Comparable<[TypeReference](../../../../org/tron/trident/abi/TypeReference.html "class in org.tron.trident.abi")<T>>

  Direct Known Subclasses:
  :   [TypeReference.StaticArrayTypeReference](../../../../org/tron/trident/abi/TypeReference.StaticArrayTypeReference.html "class in org.tron.trident.abi")

  ---

    

  ```
  public abstract class TypeReference<T extends Type>
  extends java.lang.Object
  implements java.lang.Comparable<TypeReference<T>>
  ```

  Type wrapper to get around limitations of Java's type erasure. This is so that we can pass around
  Typed [`Array`](../../../../org/tron/trident/abi/datatypes/Array.html "class in org.tron.trident.abi.datatypes") types.

  See [this blog post](http://gafter.blogspot.com.au/2006/12/super-type-tokens.html)
  for further details.

  It may make sense to switch to using Java's reflection [Type](https://docs.oracle.com/javase/8/docs/api/java/lang/reflect/Type.html) to avoid
  working around this fundamental generics limitation.

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `TypeReference.StaticArrayTypeReference<T extends Type>` |
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `protected static java.util.regex.Pattern` | `ARRAY_SUFFIX` |
  + ### Constructor Summary

    Constructors

    | Modifier | Constructor and Description |
    | `protected` | `TypeReference()` |
    | `protected` | `TypeReference(boolean indexed)` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `int` | `compareTo(TypeReference<T> o)` |
    | `static <T extends Type> TypeReference<T>` | `create(java.lang.Class<T> cls)` |
    | `static <T extends Type> TypeReference<T>` | `create(java.lang.Class<T> cls, boolean indexed)` |
    | `protected static java.lang.Class<? extends Type>` | `getAtomicTypeClass(java.lang.String solidityType, boolean primitives)` This is a helper method that only works for atomic types (uint, bytes, etc). |
    | `java.lang.Class<T>` | `getClassType()` Workaround to ensure type does not come back as T due to erasure, this enables you to create a TypeReference via `Class<T>`. |
    | `java.lang.reflect.Type` | `getType()` |
    | `boolean` | `isIndexed()` |
    | `static TypeReference` | `makeTypeReference(java.lang.String solidityType)` |
    | `static TypeReference` | `makeTypeReference(java.lang.String solidityType, boolean indexed, boolean primitives)` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Field Detail

    - #### ARRAY\_SUFFIX

      ```
      protected static java.util.regex.Pattern ARRAY_SUFFIX
      ```
  + ### Constructor Detail

    - #### TypeReference

      ```
      protected TypeReference()
      ```
    - #### TypeReference

      ```
      protected TypeReference(boolean indexed)
      ```
  + ### Method Detail

    - #### compareTo

      ```
      public int compareTo(TypeReference<T> o)
      ```

      Specified by:
      :   `compareTo` in interface `java.lang.Comparable<TypeReference<T extends Type>>`
    - #### getType

      ```
      public java.lang.reflect.Type getType()
      ```
    - #### isIndexed

      ```
      public boolean isIndexed()
      ```
    - #### getClassType

      ```
      public java.lang.Class<T> getClassType()
                                      throws java.lang.ClassNotFoundException
      ```

      Workaround to ensure type does not come back as T due to erasure, this enables you to create
      a TypeReference via `Class<T>`.

      Returns:
      :   the parameterized Class type if applicable, otherwise a regular class

      Throws:
      :   `java.lang.ClassNotFoundException` - if the class type cannot be determined
    - #### create

      ```
      public static <T extends Type> TypeReference<T> create(java.lang.Class<T> cls)
      ```
    - #### create

      ```
      public static <T extends Type> TypeReference<T> create(java.lang.Class<T> cls,
                                                             boolean indexed)
      ```
    - #### getAtomicTypeClass

      ```
      protected static java.lang.Class<? extends Type> getAtomicTypeClass(java.lang.String solidityType,
                                                                          boolean primitives)
                                                                   throws java.lang.ClassNotFoundException
      ```

      This is a helper method that only works for atomic types (uint, bytes, etc). Array types must
      be wrapped by a `ParameterizedType`.

      Parameters:
      :   `solidityType` - the solidity as a string eg Address Int
      :   `primitives` - is it a primitive type

      Returns:
      :   returns

      Throws:
      :   `java.lang.ClassNotFoundException` - when the class cannot be found.
    - #### makeTypeReference

      ```
      public static TypeReference makeTypeReference(java.lang.String solidityType)
                                             throws java.lang.ClassNotFoundException
      ```

      Throws:
      :   `java.lang.ClassNotFoundException`
    - #### makeTypeReference

      ```
      public static TypeReference makeTypeReference(java.lang.String solidityType,
                                                    boolean indexed,
                                                    boolean primitives)
                                             throws java.lang.ClassNotFoundException
      ```

      Throws:
      :   `java.lang.ClassNotFoundException`