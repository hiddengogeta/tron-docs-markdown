

org.tron.trident.abi.datatypes

## Class DynamicBytes

* java.lang.Object
* + [org.tron.trident.abi.datatypes.BytesType](../../../../../org/tron/trident/abi/datatypes/BytesType.html "class in org.tron.trident.abi.datatypes")
  + - org.tron.trident.abi.datatypes.DynamicBytes

* All Implemented Interfaces:
  :   [Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")<byte[]>

  ---

    

  ```
  public class DynamicBytes
  extends BytesType
  ```

  Dynamically allocated sequence of bytes.

* + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static DynamicBytes` | `DEFAULT` |
    | `static java.lang.String` | `TYPE_NAME` |

    - ### Fields inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `MAX_BIT_LENGTH, MAX_BYTE_LENGTH`
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `DynamicBytes(byte[] value)` |
  + ### Method Summary

    - ### Methods inherited from class org.tron.trident.abi.datatypes.[BytesType](../../../../../org/tron/trident/abi/datatypes/BytesType.html "class in org.tron.trident.abi.datatypes")

      `bytes32PaddedLength, equals, getTypeAsString, getValue, hashCode`
    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

* + ### Field Detail

    - #### TYPE\_NAME

      ```
      public static final java.lang.String TYPE_NAME
      ```

      See Also:
      :   [Constant Field Values](../../../../../constant-values.html#org.tron.trident.abi.datatypes.DynamicBytes.TYPE_NAME)
    - #### DEFAULT

      ```
      public static final DynamicBytes DEFAULT
      ```
  + ### Constructor Detail

    - #### DynamicBytes

      ```
      public DynamicBytes(byte[] value)
      ```