

org.tron.trident.abi.datatypes

## Class Bool

* java.lang.Object
* + org.tron.trident.abi.datatypes.Bool

* All Implemented Interfaces:
  :   [Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")<java.lang.Boolean>

  ---

    

  ```
  public class Bool
  extends java.lang.Object
  implements Type<java.lang.Boolean>
  ```

  Boolean type.

* + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static Bool` | `DEFAULT` |
    | `static java.lang.String` | `TYPE_NAME` |

    - ### Fields inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `MAX_BIT_LENGTH, MAX_BYTE_LENGTH`
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `Bool(boolean value)` |
    | `Bool(java.lang.Boolean value)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `boolean` | `equals(java.lang.Object o)` |
    | `java.lang.String` | `getTypeAsString()` |
    | `java.lang.Boolean` | `getValue()` |
    | `int` | `hashCode()` |

    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`
    - ### Methods inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `bytes32PaddedLength`

* + ### Field Detail

    - #### TYPE\_NAME

      ```
      public static final java.lang.String TYPE_NAME
      ```

      See Also:
      :   [Constant Field Values](../../../../../constant-values.html#org.tron.trident.abi.datatypes.Bool.TYPE_NAME)
    - #### DEFAULT

      ```
      public static final Bool DEFAULT
      ```
  + ### Constructor Detail

    - #### Bool

      ```
      public Bool(boolean value)
      ```
    - #### Bool

      ```
      public Bool(java.lang.Boolean value)
      ```
  + ### Method Detail

    - #### getTypeAsString

      ```
      public java.lang.String getTypeAsString()
      ```

      Specified by:
      :   `getTypeAsString` in interface `Type<java.lang.Boolean>`
    - #### getValue

      ```
      public java.lang.Boolean getValue()
      ```

      Specified by:
      :   `getValue` in interface `Type<java.lang.Boolean>`
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