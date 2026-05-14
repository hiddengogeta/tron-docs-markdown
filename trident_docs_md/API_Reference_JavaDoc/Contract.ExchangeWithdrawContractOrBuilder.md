

org.tron.trident.proto

## Interface Contract.ExchangeWithdrawContractOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Contract.ExchangeWithdrawContract](../../../../org/tron/trident/proto/Contract.ExchangeWithdrawContract.html "class in org.tron.trident.proto"), [Contract.ExchangeWithdrawContract.Builder](../../../../org/tron/trident/proto/Contract.ExchangeWithdrawContract.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Contract.ExchangeWithdrawContractOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getExchangeId()` `int64 exchange_id = 2;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `long` | `getQuant()` `int64 quant = 4;` |
    | `com.google.protobuf.ByteString` | `getTokenId()` `bytes token_id = 3;` |

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
    - #### getExchangeId

      ```
      long getExchangeId()
      ```

      `int64 exchange_id = 2;`

      Returns:
      :   The exchangeId.
    - #### getTokenId

      ```
      com.google.protobuf.ByteString getTokenId()
      ```

      `bytes token_id = 3;`

      Returns:
      :   The tokenId.
    - #### getQuant

      ```
      long getQuant()
      ```

      `int64 quant = 4;`

      Returns:
      :   The quant.