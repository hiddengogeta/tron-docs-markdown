

org.tron.trident.abi.datatypes

## Class BytesType

* java.lang.Object
* + org.tron.trident.abi.datatypes.BytesType

* All Implemented Interfaces:
  :   [Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")<byte[]>

  Direct Known Subclasses:
  :   [Bytes](../../../../../org/tron/trident/abi/datatypes/Bytes.html "class in org.tron.trident.abi.datatypes"), [DynamicBytes](../../../../../org/tron/trident/abi/datatypes/DynamicBytes.html "class in org.tron.trident.abi.datatypes")

  ---

    

  ```
  public abstract class BytesType
  extends java.lang.Object
  implements Type<byte[]>
  ```

  Binary sequence of bytes.

* + ### Field Summary

    - ### Fields inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `MAX_BIT_LENGTH, MAX_BYTE_LENGTH`
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `BytesType(byte[] src, java.lang.String type)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `int` | `bytes32PaddedLength()` |
    | `boolean` | `equals(java.lang.Object o)` |
    | `java.lang.String` | `getTypeAsString()` |
    | `byte[]` | `getValue()` |
    | `int` | `hashCode()` |

    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### BytesType

      ```
      public BytesType(byte[] src,
                       java.lang.String type)
      ```
  + ### Method Detail

    - #### bytes32PaddedLength

      ```
      public int bytes32PaddedLength()
      ```

      Specified by:
      :   `bytes32PaddedLength` in interface `Type<byte[]>`
    - #### getValue

      ```
      public byte[] getValue()
      ```

      Specified by:
      :   `getValue` in interface `Type<byte[]>`
    - #### getTypeAsString

      ```
      public java.lang.String getTypeAsString()
      ```

      Specified by:
      :   `getTypeAsString` in interface `Type<byte[]>`
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