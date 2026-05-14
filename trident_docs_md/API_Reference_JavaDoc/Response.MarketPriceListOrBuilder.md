

org.tron.trident.proto

## Interface Response.MarketPriceListOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.MarketPriceList](../../../../org/tron/trident/proto/Response.MarketPriceList.html "class in org.tron.trident.proto"), [Response.MarketPriceList.Builder](../../../../org/tron/trident/proto/Response.MarketPriceList.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.MarketPriceListOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getBuyTokenId()` `bytes buy_token_id = 2;` |
    | `Response.MarketPrice` | `getPrices(int index)` `repeated .protocol.MarketPrice prices = 3;` |
    | `int` | `getPricesCount()` `repeated .protocol.MarketPrice prices = 3;` |
    | `java.util.List<Response.MarketPrice>` | `getPricesList()` `repeated .protocol.MarketPrice prices = 3;` |
    | `Response.MarketPriceOrBuilder` | `getPricesOrBuilder(int index)` `repeated .protocol.MarketPrice prices = 3;` |
    | `java.util.List<? extends Response.MarketPriceOrBuilder>` | `getPricesOrBuilderList()` `repeated .protocol.MarketPrice prices = 3;` |
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
    - #### getPricesList

      ```
      java.util.List<Response.MarketPrice> getPricesList()
      ```

      `repeated .protocol.MarketPrice prices = 3;`
    - #### getPrices

      ```
      Response.MarketPrice getPrices(int index)
      ```

      `repeated .protocol.MarketPrice prices = 3;`
    - #### getPricesCount

      ```
      int getPricesCount()
      ```

      `repeated .protocol.MarketPrice prices = 3;`
    - #### getPricesOrBuilderList

      ```
      java.util.List<? extends Response.MarketPriceOrBuilder> getPricesOrBuilderList()
      ```

      `repeated .protocol.MarketPrice prices = 3;`
    - #### getPricesOrBuilder

      ```
      Response.MarketPriceOrBuilder getPricesOrBuilder(int index)
      ```

      `repeated .protocol.MarketPrice prices = 3;`