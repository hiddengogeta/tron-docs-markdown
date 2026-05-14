

org.tron.trident.proto

## Interface Contract.MarketSellAssetContractOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Contract.MarketSellAssetContract](../../../../org/tron/trident/proto/Contract.MarketSellAssetContract.html "class in org.tron.trident.proto"), [Contract.MarketSellAssetContract.Builder](../../../../org/tron/trident/proto/Contract.MarketSellAssetContract.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Contract.MarketSellAssetContractOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getBuyTokenId()` `bytes buy_token_id = 4;` |
    | `long` | `getBuyTokenQuantity()` min to receive |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `com.google.protobuf.ByteString` | `getSellTokenId()` `bytes sell_token_id = 2;` |
    | `long` | `getSellTokenQuantity()` `int64 sell_token_quantity = 3;` |

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
    - #### getSellTokenId

      ```
      com.google.protobuf.ByteString getSellTokenId()
      ```

      `bytes sell_token_id = 2;`

      Returns:
      :   The sellTokenId.
    - #### getSellTokenQuantity

      ```
      long getSellTokenQuantity()
      ```

      `int64 sell_token_quantity = 3;`

      Returns:
      :   The sellTokenQuantity.
    - #### getBuyTokenId

      ```
      com.google.protobuf.ByteString getBuyTokenId()
      ```

      `bytes buy_token_id = 4;`

      Returns:
      :   The buyTokenId.
    - #### getBuyTokenQuantity

      ```
      long getBuyTokenQuantity()
      ```

      ```
       min to receive
      ```

      `int64 buy_token_quantity = 5;`

      Returns:
      :   The buyTokenQuantity.