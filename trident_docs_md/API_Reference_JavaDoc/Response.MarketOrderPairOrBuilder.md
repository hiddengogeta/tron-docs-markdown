

org.tron.trident.proto

## Interface Response.MarketOrderPairOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.MarketOrderPair](../../../../org/tron/trident/proto/Response.MarketOrderPair.html "class in org.tron.trident.proto"), [Response.MarketOrderPair.Builder](../../../../org/tron/trident/proto/Response.MarketOrderPair.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.MarketOrderPairOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getBuyTokenId()` `bytes buy_token_id = 2;` |
    | `com.google.protobuf.ByteString` | `getSellTokenId()` `bytes sell_token_id = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getSellTokenId

      ```
      com.google.protobuf.ByteString getSellTokenId()
      ```

      `bytes sell_token_id = 1;`

      Returns:
      :   The sellTokenId.
    - #### getBuyTokenId

      ```
      com.google.protobuf.ByteString getBuyTokenId()
      ```

      `bytes buy_token_id = 2;`

      Returns:
      :   The buyTokenId.