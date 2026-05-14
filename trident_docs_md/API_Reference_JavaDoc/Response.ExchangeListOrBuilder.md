

org.tron.trident.proto

## Interface Response.ExchangeListOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.ExchangeList](../../../../org/tron/trident/proto/Response.ExchangeList.html "class in org.tron.trident.proto"), [Response.ExchangeList.Builder](../../../../org/tron/trident/proto/Response.ExchangeList.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.ExchangeListOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Response.Exchange` | `getExchanges(int index)` `repeated .protocol.Exchange exchanges = 1;` |
    | `int` | `getExchangesCount()` `repeated .protocol.Exchange exchanges = 1;` |
    | `java.util.List<Response.Exchange>` | `getExchangesList()` `repeated .protocol.Exchange exchanges = 1;` |
    | `Response.ExchangeOrBuilder` | `getExchangesOrBuilder(int index)` `repeated .protocol.Exchange exchanges = 1;` |
    | `java.util.List<? extends Response.ExchangeOrBuilder>` | `getExchangesOrBuilderList()` `repeated .protocol.Exchange exchanges = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getExchangesList

      ```
      java.util.List<Response.Exchange> getExchangesList()
      ```

      `repeated .protocol.Exchange exchanges = 1;`
    - #### getExchanges

      ```
      Response.Exchange getExchanges(int index)
      ```

      `repeated .protocol.Exchange exchanges = 1;`
    - #### getExchangesCount

      ```
      int getExchangesCount()
      ```

      `repeated .protocol.Exchange exchanges = 1;`
    - #### getExchangesOrBuilderList

      ```
      java.util.List<? extends Response.ExchangeOrBuilder> getExchangesOrBuilderList()
      ```

      `repeated .protocol.Exchange exchanges = 1;`
    - #### getExchangesOrBuilder

      ```
      Response.ExchangeOrBuilder getExchangesOrBuilder(int index)
      ```

      `repeated .protocol.Exchange exchanges = 1;`