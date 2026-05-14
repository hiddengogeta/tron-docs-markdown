

org.tron.trident.proto

## Interface Common.MarketOrderDetailOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Common.MarketOrderDetail](../../../../org/tron/trident/proto/Common.MarketOrderDetail.html "class in org.tron.trident.proto"), [Common.MarketOrderDetail.Builder](../../../../org/tron/trident/proto/Common.MarketOrderDetail.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Common](../../../../org/tron/trident/proto/Common.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Common.MarketOrderDetailOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getFillBuyQuantity()` `int64 fillBuyQuantity = 4;` |
    | `long` | `getFillSellQuantity()` `int64 fillSellQuantity = 3;` |
    | `com.google.protobuf.ByteString` | `getMakerOrderId()` `bytes makerOrderId = 1;` |
    | `com.google.protobuf.ByteString` | `getTakerOrderId()` `bytes takerOrderId = 2;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getMakerOrderId

      ```
      com.google.protobuf.ByteString getMakerOrderId()
      ```

      `bytes makerOrderId = 1;`

      Returns:
      :   The makerOrderId.
    - #### getTakerOrderId

      ```
      com.google.protobuf.ByteString getTakerOrderId()
      ```

      `bytes takerOrderId = 2;`

      Returns:
      :   The takerOrderId.
    - #### getFillSellQuantity

      ```
      long getFillSellQuantity()
      ```

      `int64 fillSellQuantity = 3;`

      Returns:
      :   The fillSellQuantity.
    - #### getFillBuyQuantity

      ```
      long getFillBuyQuantity()
      ```

      `int64 fillBuyQuantity = 4;`

      Returns:
      :   The fillBuyQuantity.