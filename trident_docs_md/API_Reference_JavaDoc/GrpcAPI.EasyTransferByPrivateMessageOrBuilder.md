

org.tron.trident.api

## Interface GrpcAPI.EasyTransferByPrivateMessageOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.EasyTransferByPrivateMessage](../../../../org/tron/trident/api/GrpcAPI.EasyTransferByPrivateMessage.html "class in org.tron.trident.api"), [GrpcAPI.EasyTransferByPrivateMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.EasyTransferByPrivateMessage.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.EasyTransferByPrivateMessageOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getAmount()` `int64 amount = 3;` |
    | `com.google.protobuf.ByteString` | `getPrivateKey()` `bytes privateKey = 1;` |
    | `com.google.protobuf.ByteString` | `getToAddress()` `bytes toAddress = 2;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getPrivateKey

      ```
      com.google.protobuf.ByteString getPrivateKey()
      ```

      `bytes privateKey = 1;`

      Returns:
      :   The privateKey.
    - #### getToAddress

      ```
      com.google.protobuf.ByteString getToAddress()
      ```

      `bytes toAddress = 2;`

      Returns:
      :   The toAddress.
    - #### getAmount

      ```
      long getAmount()
      ```

      `int64 amount = 3;`

      Returns:
      :   The amount.