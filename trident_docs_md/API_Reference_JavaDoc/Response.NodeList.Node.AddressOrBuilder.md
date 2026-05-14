

org.tron.trident.proto

## Interface Response.NodeList.Node.AddressOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.NodeList.Node.Address](../../../../org/tron/trident/proto/Response.NodeList.Node.Address.html "class in org.tron.trident.proto"), [Response.NodeList.Node.Address.Builder](../../../../org/tron/trident/proto/Response.NodeList.Node.Address.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response.NodeList.Node](../../../../org/tron/trident/proto/Response.NodeList.Node.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.NodeList.Node.AddressOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getHost()` `bytes host = 1;` |
    | `int` | `getPort()` `int32 port = 2;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getHost

      ```
      com.google.protobuf.ByteString getHost()
      ```

      `bytes host = 1;`

      Returns:
      :   The host.
    - #### getPort

      ```
      int getPort()
      ```

      `int32 port = 2;`

      Returns:
      :   The port.