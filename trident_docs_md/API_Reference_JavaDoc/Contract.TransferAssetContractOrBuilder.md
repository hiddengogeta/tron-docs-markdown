

org.tron.trident.proto

## Interface Contract.TransferAssetContractOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Contract.TransferAssetContract](../../../../org/tron/trident/proto/Contract.TransferAssetContract.html "class in org.tron.trident.proto"), [Contract.TransferAssetContract.Builder](../../../../org/tron/trident/proto/Contract.TransferAssetContract.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Contract.TransferAssetContractOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getAmount()` `int64 amount = 4;` |
    | `com.google.protobuf.ByteString` | `getAssetName()` this field is token name before the proposal |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` ALLOW\_SAME\_TOKEN\_NAME is active, otherwise it is token id and token is should be in string format. |
    | `com.google.protobuf.ByteString` | `getToAddress()` `bytes to_address = 3;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getAssetName

      ```
      com.google.protobuf.ByteString getAssetName()
      ```

      ```
       this field is token name before the proposal
      ```

      `bytes asset_name = 1;`

      Returns:
      :   The assetName.
    - #### getOwnerAddress

      ```
      com.google.protobuf.ByteString getOwnerAddress()
      ```

      ```
       ALLOW_SAME_TOKEN_NAME is active, otherwise it is
       token id and token is should be in string format.
      ```

      `bytes owner_address = 2;`

      Returns:
      :   The ownerAddress.
    - #### getToAddress

      ```
      com.google.protobuf.ByteString getToAddress()
      ```

      `bytes to_address = 3;`

      Returns:
      :   The toAddress.
    - #### getAmount

      ```
      long getAmount()
      ```

      `int64 amount = 4;`

      Returns:
      :   The amount.