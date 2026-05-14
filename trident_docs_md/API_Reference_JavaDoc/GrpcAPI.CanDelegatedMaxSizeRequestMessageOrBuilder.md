

org.tron.trident.api

## Interface GrpcAPI.CanDelegatedMaxSizeRequestMessageOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.CanDelegatedMaxSizeRequestMessage](../../../../org/tron/trident/api/GrpcAPI.CanDelegatedMaxSizeRequestMessage.html "class in org.tron.trident.api"), [GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.CanDelegatedMaxSizeRequestMessageOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 2;` |
    | `int` | `getType()` `int32 type = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getType

      ```
      int getType()
      ```

      `int32 type = 1;`

      Returns:
      :   The type.
    - #### getOwnerAddress

      ```
      com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 2;`

      Returns:
      :   The ownerAddress.