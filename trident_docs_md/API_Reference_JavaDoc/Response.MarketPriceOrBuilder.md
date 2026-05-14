

org.tron.trident.proto

## Interface Response.MarketPriceOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.MarketPrice](../../../../org/tron/trident/proto/Response.MarketPrice.html "class in org.tron.trident.proto"), [Response.MarketPrice.Builder](../../../../org/tron/trident/proto/Response.MarketPrice.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.MarketPriceOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getBuyTokenQuantity()` `int64 buy_token_quantity = 2;` |
    | `long` | `getSellTokenQuantity()` `int64 sell_token_quantity = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getSellTokenQuantity

      ```
      long getSellTokenQuantity()
      ```

      `int64 sell_token_quantity = 1;`

      Returns:
      :   The sellTokenQuantity.
    - #### getBuyTokenQuantity

      ```
      long getBuyTokenQuantity()
      ```

      `int64 buy_token_quantity = 2;`

      Returns:
      :   The buyTokenQuantity.