

org.tron.trident.proto

## Interface Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.NodeInfo.MachineInfo.MemoryDescInfo](../../../../org/tron/trident/proto/Response.NodeInfo.MachineInfo.MemoryDescInfo.html "class in org.tron.trident.proto"), [Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder](../../../../org/tron/trident/proto/Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response.NodeInfo.MachineInfo](../../../../org/tron/trident/proto/Response.NodeInfo.MachineInfo.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getInitSize()` `int64 initSize = 2;` |
    | `long` | `getMaxSize()` `int64 maxSize = 4;` |
    | `java.lang.String` | `getName()` `string name = 1;` |
    | `com.google.protobuf.ByteString` | `getNameBytes()` `string name = 1;` |
    | `double` | `getUseRate()` `double useRate = 5;` |
    | `long` | `getUseSize()` `int64 useSize = 3;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getName

      ```
      java.lang.String getName()
      ```

      `string name = 1;`

      Returns:
      :   The name.
    - #### getNameBytes

      ```
      com.google.protobuf.ByteString getNameBytes()
      ```

      `string name = 1;`

      Returns:
      :   The bytes for name.
    - #### getInitSize

      ```
      long getInitSize()
      ```

      `int64 initSize = 2;`

      Returns:
      :   The initSize.
    - #### getUseSize

      ```
      long getUseSize()
      ```

      `int64 useSize = 3;`

      Returns:
      :   The useSize.
    - #### getMaxSize

      ```
      long getMaxSize()
      ```

      `int64 maxSize = 4;`

      Returns:
      :   The maxSize.
    - #### getUseRate

      ```
      double getUseRate()
      ```

      `double useRate = 5;`

      Returns:
      :   The useRate.