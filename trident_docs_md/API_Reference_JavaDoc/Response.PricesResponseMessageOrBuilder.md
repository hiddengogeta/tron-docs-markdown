

org.tron.trident.proto

## Interface Response.PricesResponseMessageOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.PricesResponseMessage](../../../../org/tron/trident/proto/Response.PricesResponseMessage.html "class in org.tron.trident.proto"), [Response.PricesResponseMessage.Builder](../../../../org/tron/trident/proto/Response.PricesResponseMessage.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.PricesResponseMessageOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `java.lang.String` | `getPrices()` `string prices = 1;` |
    | `com.google.protobuf.ByteString` | `getPricesBytes()` `string prices = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getPrices

      ```
      java.lang.String getPrices()
      ```

      `string prices = 1;`

      Returns:
      :   The prices.
    - #### getPricesBytes

      ```
      com.google.protobuf.ByteString getPricesBytes()
      ```

      `string prices = 1;`

      Returns:
      :   The bytes for prices.