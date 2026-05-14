

org.tron.trident.proto

## Interface Contract.UpdateAssetContractOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Contract.UpdateAssetContract](../../../../org/tron/trident/proto/Contract.UpdateAssetContract.html "class in org.tron.trident.proto"), [Contract.UpdateAssetContract.Builder](../../../../org/tron/trident/proto/Contract.UpdateAssetContract.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Contract.UpdateAssetContractOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getDescription()` `bytes description = 2;` |
    | `long` | `getNewLimit()` `int64 new_limit = 4;` |
    | `long` | `getNewPublicLimit()` `int64 new_public_limit = 5;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `com.google.protobuf.ByteString` | `getUrl()` `bytes url = 3;` |

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
    - #### getDescription

      ```
      com.google.protobuf.ByteString getDescription()
      ```

      `bytes description = 2;`

      Returns:
      :   The description.
    - #### getUrl

      ```
      com.google.protobuf.ByteString getUrl()
      ```

      `bytes url = 3;`

      Returns:
      :   The url.
    - #### getNewLimit

      ```
      long getNewLimit()
      ```

      `int64 new_limit = 4;`

      Returns:
      :   The newLimit.
    - #### getNewPublicLimit

      ```
      long getNewPublicLimit()
      ```

      `int64 new_public_limit = 5;`

      Returns:
      :   The newPublicLimit.