

org.tron.trident.api

## Interface GrpcAPI.EasyTransferAssetMessageOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.EasyTransferAssetMessage](../../../../org/tron/trident/api/GrpcAPI.EasyTransferAssetMessage.html "class in org.tron.trident.api"), [GrpcAPI.EasyTransferAssetMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.EasyTransferAssetMessage.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.EasyTransferAssetMessageOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getAmount()` `int64 amount = 4;` |
    | `java.lang.String` | `getAssetId()` `string assetId = 3;` |
    | `com.google.protobuf.ByteString` | `getAssetIdBytes()` `string assetId = 3;` |
    | `com.google.protobuf.ByteString` | `getPassPhrase()` `bytes passPhrase = 1;` |
    | `com.google.protobuf.ByteString` | `getToAddress()` `bytes toAddress = 2;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getPassPhrase

      ```
      com.google.protobuf.ByteString getPassPhrase()
      ```

      `bytes passPhrase = 1;`

      Returns:
      :   The passPhrase.
    - #### getToAddress

      ```
      com.google.protobuf.ByteString getToAddress()
      ```

      `bytes toAddress = 2;`

      Returns:
      :   The toAddress.
    - #### getAssetId

      ```
      java.lang.String getAssetId()
      ```

      `string assetId = 3;`

      Returns:
      :   The assetId.
    - #### getAssetIdBytes

      ```
      com.google.protobuf.ByteString getAssetIdBytes()
      ```

      `string assetId = 3;`

      Returns:
      :   The bytes for assetId.
    - #### getAmount

      ```
      long getAmount()
      ```

      `int64 amount = 4;`

      Returns:
      :   The amount.