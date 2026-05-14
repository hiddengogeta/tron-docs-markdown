

org.tron.trident.abi.datatypes

## Class Utf8String

* java.lang.Object
* + org.tron.trident.abi.datatypes.Utf8String

* All Implemented Interfaces:
  :   [Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")<java.lang.String>

  ---

    

  ```
  public class Utf8String
  extends java.lang.Object
  implements Type<java.lang.String>
  ```

  UTF-8 encoded string type.

* + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static Utf8String` | `DEFAULT` |
    | `static java.lang.String` | `TYPE_NAME` |

    - ### Fields inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `MAX_BIT_LENGTH, MAX_BYTE_LENGTH`
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `Utf8String(java.lang.String value)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `int` | `bytes32PaddedLength()` |
    | `boolean` | `equals(java.lang.Object o)` |
    | `java.lang.String` | `getTypeAsString()` |
    | `java.lang.String` | `getValue()` |
    | `int` | `hashCode()` |
    | `java.lang.String` | `toString()` |

    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

* + ### Field Detail

    - #### TYPE\_NAME

      ```
      public static final java.lang.String TYPE_NAME
      ```

      See Also:
      :   [Constant Field Values](../../../../../constant-values.html#org.tron.trident.abi.datatypes.Utf8String.TYPE_NAME)
    - #### DEFAULT

      ```
      public static final Utf8String DEFAULT
      ```
  + ### Constructor Detail

    - #### Utf8String

      ```
      public Utf8String(java.lang.String value)
      ```
  + ### Method Detail

    - #### bytes32PaddedLength

      ```
      public int bytes32PaddedLength()
      ```

      Specified by:
      :   `bytes32PaddedLength` in interface `Type<java.lang.String>`
    - #### getValue

      ```
      public java.lang.String getValue()
      ```

      Specified by:
      :   `getValue` in interface `Type<java.lang.String>`
    - #### getTypeAsString

      ```
      public java.lang.String getTypeAsString()
      ```

      Specified by:
      :   `getTypeAsString` in interface `Type<java.lang.String>`
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
    - #### toString

      ```
      public java.lang.String toString()
      ```

      Overrides:
      :   `toString` in class `java.lang.Object`