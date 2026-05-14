

org.tron.trident.proto

## Interface Response.MarketOrderOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.MarketOrder](../../../../org/tron/trident/proto/Response.MarketOrder.html "class in org.tron.trident.proto"), [Response.MarketOrder.Builder](../../../../org/tron/trident/proto/Response.MarketOrder.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.MarketOrderOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getBuyTokenId()` `bytes buy_token_id = 6;` |
    | `long` | `getBuyTokenQuantity()` min to receive |
    | `long` | `getCreateTime()` `int64 create_time = 3;` |
    | `com.google.protobuf.ByteString` | `getNext()` `bytes next = 13;` |
    | `com.google.protobuf.ByteString` | `getOrderId()` `bytes order_id = 1;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 2;` |
    | `com.google.protobuf.ByteString` | `getPrev()` `bytes prev = 12;` |
    | `com.google.protobuf.ByteString` | `getSellTokenId()` `bytes sell_token_id = 4;` |
    | `long` | `getSellTokenQuantity()` `int64 sell_token_quantity = 5;` |
    | `long` | `getSellTokenQuantityRemain()` `int64 sell_token_quantity_remain = 9;` |
    | `long` | `getSellTokenQuantityReturn()` When state != ACTIVE and sell\_token\_quantity\_return !=0, it means that some sell tokens are returned to the account due to insufficient remaining amount |
    | `Response.MarketOrder.State` | `getState()` `.protocol.MarketOrder.State state = 11;` |
    | `int` | `getStateValue()` `.protocol.MarketOrder.State state = 11;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getOrderId

      ```
      com.google.protobuf.ByteString getOrderId()
      ```

      `bytes order_id = 1;`

      Returns:
      :   The orderId.
    - #### getOwnerAddress

      ```
      com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 2;`

      Returns:
      :   The ownerAddress.
    - #### getCreateTime

      ```
      long getCreateTime()
      ```

      `int64 create_time = 3;`

      Returns:
      :   The createTime.
    - #### getSellTokenId

      ```
      com.google.protobuf.ByteString getSellTokenId()
      ```

      `bytes sell_token_id = 4;`

      Returns:
      :   The sellTokenId.
    - #### getSellTokenQuantity

      ```
      long getSellTokenQuantity()
      ```

      `int64 sell_token_quantity = 5;`

      Returns:
      :   The sellTokenQuantity.
    - #### getBuyTokenId

      ```
      com.google.protobuf.ByteString getBuyTokenId()
      ```

      `bytes buy_token_id = 6;`

      Returns:
      :   The buyTokenId.
    - #### getBuyTokenQuantity

      ```
      long getBuyTokenQuantity()
      ```

      ```
       min to receive
      ```

      `int64 buy_token_quantity = 7;`

      Returns:
      :   The buyTokenQuantity.
    - #### getSellTokenQuantityRemain

      ```
      long getSellTokenQuantityRemain()
      ```

      `int64 sell_token_quantity_remain = 9;`

      Returns:
      :   The sellTokenQuantityRemain.
    - #### getSellTokenQuantityReturn

      ```
      long getSellTokenQuantityReturn()
      ```

      ```
       When state != ACTIVE and sell_token_quantity_return !=0,
       it means that some sell tokens are returned to the account due to
       insufficient remaining amount
      ```

      `int64 sell_token_quantity_return = 10;`

      Returns:
      :   The sellTokenQuantityReturn.
    - #### getStateValue

      ```
      int getStateValue()
      ```

      `.protocol.MarketOrder.State state = 11;`

      Returns:
      :   The enum numeric value on the wire for state.
    - #### getState

      ```
      Response.MarketOrder.State getState()
      ```

      `.protocol.MarketOrder.State state = 11;`

      Returns:
      :   The state.
    - #### getPrev

      ```
      com.google.protobuf.ByteString getPrev()
      ```

      `bytes prev = 12;`

      Returns:
      :   The prev.
    - #### getNext

      ```
      com.google.protobuf.ByteString getNext()
      ```

      `bytes next = 13;`

      Returns:
      :   The next.