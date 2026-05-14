

org.tron.trident.proto

## Interface Response.MarketOrderPairListOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.MarketOrderPairList](../../../../org/tron/trident/proto/Response.MarketOrderPairList.html "class in org.tron.trident.proto"), [Response.MarketOrderPairList.Builder](../../../../org/tron/trident/proto/Response.MarketOrderPairList.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.MarketOrderPairListOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Response.MarketOrderPair` | `getOrderPair(int index)` `repeated .protocol.MarketOrderPair orderPair = 1;` |
    | `int` | `getOrderPairCount()` `repeated .protocol.MarketOrderPair orderPair = 1;` |
    | `java.util.List<Response.MarketOrderPair>` | `getOrderPairList()` `repeated .protocol.MarketOrderPair orderPair = 1;` |
    | `Response.MarketOrderPairOrBuilder` | `getOrderPairOrBuilder(int index)` `repeated .protocol.MarketOrderPair orderPair = 1;` |
    | `java.util.List<? extends Response.MarketOrderPairOrBuilder>` | `getOrderPairOrBuilderList()` `repeated .protocol.MarketOrderPair orderPair = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getOrderPairList

      ```
      java.util.List<Response.MarketOrderPair> getOrderPairList()
      ```

      `repeated .protocol.MarketOrderPair orderPair = 1;`
    - #### getOrderPair

      ```
      Response.MarketOrderPair getOrderPair(int index)
      ```

      `repeated .protocol.MarketOrderPair orderPair = 1;`
    - #### getOrderPairCount

      ```
      int getOrderPairCount()
      ```

      `repeated .protocol.MarketOrderPair orderPair = 1;`
    - #### getOrderPairOrBuilderList

      ```
      java.util.List<? extends Response.MarketOrderPairOrBuilder> getOrderPairOrBuilderList()
      ```

      `repeated .protocol.MarketOrderPair orderPair = 1;`
    - #### getOrderPairOrBuilder

      ```
      Response.MarketOrderPairOrBuilder getOrderPairOrBuilder(int index)
      ```

      `repeated .protocol.MarketOrderPair orderPair = 1;`