

org.tron.trident.api

## Interface GrpcAPI.IncomingViewingKeyMessageOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.IncomingViewingKeyMessage](../../../../org/tron/trident/api/GrpcAPI.IncomingViewingKeyMessage.html "class in org.tron.trident.api"), [GrpcAPI.IncomingViewingKeyMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.IncomingViewingKeyMessage.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.IncomingViewingKeyMessageOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getIvk()` `bytes ivk = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getIvk

      ```
      com.google.protobuf.ByteString getIvk()
      ```

      `bytes ivk = 1;`

      Returns:
      :   The ivk.