

org.tron.trident.api

## Interface GrpcAPI.CanWithdrawUnfreezeAmountRequestMessageOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage](../../../../org/tron/trident/api/GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.html "class in org.tron.trident.api"), [GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.CanWithdrawUnfreezeAmountRequestMessageOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `long` | `getTimestamp()` `int64 timestamp = 2;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getOwnerAddress

      ```
      com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   The ownerAddress.
    - #### getTimestamp

      ```
      long getTimestamp()
      ```

      `int64 timestamp = 2;`

      Returns:
      :   The timestamp.