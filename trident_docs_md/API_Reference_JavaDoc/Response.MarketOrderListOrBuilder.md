

org.tron.trident.proto

## Interface Response.MarketOrderListOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.MarketOrderList](../../../../org/tron/trident/proto/Response.MarketOrderList.html "class in org.tron.trident.proto"), [Response.MarketOrderList.Builder](../../../../org/tron/trident/proto/Response.MarketOrderList.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.MarketOrderListOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Response.MarketOrder` | `getOrders(int index)` `repeated .protocol.MarketOrder orders = 1;` |
    | `int` | `getOrdersCount()` `repeated .protocol.MarketOrder orders = 1;` |
    | `java.util.List<Response.MarketOrder>` | `getOrdersList()` `repeated .protocol.MarketOrder orders = 1;` |
    | `Response.MarketOrderOrBuilder` | `getOrdersOrBuilder(int index)` `repeated .protocol.MarketOrder orders = 1;` |
    | `java.util.List<? extends Response.MarketOrderOrBuilder>` | `getOrdersOrBuilderList()` `repeated .protocol.MarketOrder orders = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getOrdersList

      ```
      java.util.List<Response.MarketOrder> getOrdersList()
      ```

      `repeated .protocol.MarketOrder orders = 1;`
    - #### getOrders

      ```
      Response.MarketOrder getOrders(int index)
      ```

      `repeated .protocol.MarketOrder orders = 1;`
    - #### getOrdersCount

      ```
      int getOrdersCount()
      ```

      `repeated .protocol.MarketOrder orders = 1;`
    - #### getOrdersOrBuilderList

      ```
      java.util.List<? extends Response.MarketOrderOrBuilder> getOrdersOrBuilderList()
      ```

      `repeated .protocol.MarketOrder orders = 1;`
    - #### getOrdersOrBuilder

      ```
      Response.MarketOrderOrBuilder getOrdersOrBuilder(int index)
      ```

      `repeated .protocol.MarketOrder orders = 1;`