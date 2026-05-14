

org.tron.trident.abi.datatypes.primitive

## Class PrimitiveType<T extends java.io.Serializable & java.lang.Comparable<T>>

* java.lang.Object
* + org.tron.trident.abi.datatypes.primitive.PrimitiveType<T>

* All Implemented Interfaces:
  :   [Type](../../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")<T>

  Direct Known Subclasses:
  :   [Byte](../../../../../../org/tron/trident/abi/datatypes/primitive/Byte.html "class in org.tron.trident.abi.datatypes.primitive"), [Char](../../../../../../org/tron/trident/abi/datatypes/primitive/Char.html "class in org.tron.trident.abi.datatypes.primitive"), [Number](../../../../../../org/tron/trident/abi/datatypes/primitive/Number.html "class in org.tron.trident.abi.datatypes.primitive")

  ---

    

  ```
  public abstract class PrimitiveType<T extends java.io.Serializable & java.lang.Comparable<T>>
  extends java.lang.Object
  implements Type<T>
  ```

* + ### Field Summary

    - ### Fields inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `MAX_BIT_LENGTH, MAX_BYTE_LENGTH`
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `boolean` | `equals(java.lang.Object o)` |
    | `java.lang.String` | `getTypeAsString()` |
    | `T` | `getValue()` |
    | `int` | `hashCode()` |
    | `abstract Type` | `toSolidityType()` |

    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`
    - ### Methods inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `bytes32PaddedLength`

* + ### Method Detail

    - #### getValue

      ```
      public T getValue()
      ```

      Specified by:
      :   `getValue` in interface `Type<T extends java.io.Serializable & java.lang.Comparable<T>>`
    - #### getTypeAsString

      ```
      public java.lang.String getTypeAsString()
      ```

      Specified by:
      :   `getTypeAsString` in interface `Type<T extends java.io.Serializable & java.lang.Comparable<T>>`
    - #### toSolidityType

      ```
      public abstract Type toSolidityType()
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