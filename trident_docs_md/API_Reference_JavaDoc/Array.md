

org.tron.trident.abi.datatypes

## Class Array<T extends [Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")>

* java.lang.Object
* + org.tron.trident.abi.datatypes.Array<T>

* All Implemented Interfaces:
  :   [Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")<java.util.List<T>>

  Direct Known Subclasses:
  :   [DynamicArray](../../../../../org/tron/trident/abi/datatypes/DynamicArray.html "class in org.tron.trident.abi.datatypes"), [StaticArray](../../../../../org/tron/trident/abi/datatypes/StaticArray.html "class in org.tron.trident.abi.datatypes")

  ---

    

  ```
  public abstract class Array<T extends Type>
  extends java.lang.Object
  implements Type<java.util.List<T>>
  ```

  Fixed size array.

* + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `protected java.util.List<T>` | `value` |

    - ### Fields inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `MAX_BIT_LENGTH, MAX_BYTE_LENGTH`
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `int` | `bytes32PaddedLength()` |
    | `boolean` | `equals(java.lang.Object o)` |
    | `java.lang.Class<T>` | `getComponentType()` |
    | `abstract java.lang.String` | `getTypeAsString()` |
    | `java.util.List<T>` | `getValue()` |
    | `int` | `hashCode()` |

    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

* + ### Field Detail

    - #### value

      ```
      protected final java.util.List<T extends Type> value
      ```
  + ### Method Detail

    - #### bytes32PaddedLength

      ```
      public int bytes32PaddedLength()
      ```

      Specified by:
      :   `bytes32PaddedLength` in interface `Type<java.util.List<T extends Type>>`
    - #### getValue

      ```
      public java.util.List<T> getValue()
      ```

      Specified by:
      :   `getValue` in interface `Type<java.util.List<T extends Type>>`
    - #### getComponentType

      ```
      public java.lang.Class<T> getComponentType()
      ```
    - #### getTypeAsString

      ```
      public abstract java.lang.String getTypeAsString()
      ```

      Specified by:
      :   `getTypeAsString` in interface `Type<java.util.List<T extends Type>>`
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