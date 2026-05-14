

org.tron.trident.proto

## Class Response.MarketPriceList.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.MarketPriceList.Builder](../../../../org/tron/trident/proto/Response.MarketPriceList.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.MarketPriceList.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.MarketPriceListOrBuilder](../../../../org/tron/trident/proto/Response.MarketPriceListOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.MarketPriceList](../../../../org/tron/trident/proto/Response.MarketPriceList.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.MarketPriceList.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPriceList.Builder>
  implements Response.MarketPriceListOrBuilder
  ```

  Protobuf type `protocol.MarketPriceList`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.MarketPriceList.Builder` | `addAllPrices(java.lang.Iterable<? extends Response.MarketPrice> values)` `repeated .protocol.MarketPrice prices = 3;` |
    | `Response.MarketPriceList.Builder` | `addPrices(int index, Response.MarketPrice.Builder builderForValue)` `repeated .protocol.MarketPrice prices = 3;` |
    | `Response.MarketPriceList.Builder` | `addPrices(int index, Response.MarketPrice value)` `repeated .protocol.MarketPrice prices = 3;` |
    | `Response.MarketPriceList.Builder` | `addPrices(Response.MarketPrice.Builder builderForValue)` `repeated .protocol.MarketPrice prices = 3;` |
    | `Response.MarketPriceList.Builder` | `addPrices(Response.MarketPrice value)` `repeated .protocol.MarketPrice prices = 3;` |
    | `Response.MarketPrice.Builder` | `addPricesBuilder()` `repeated .protocol.MarketPrice prices = 3;` |
    | `Response.MarketPrice.Builder` | `addPricesBuilder(int index)` `repeated .protocol.MarketPrice prices = 3;` |
    | `Response.MarketPriceList.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.MarketPriceList` | `build()` |
    | `Response.MarketPriceList` | `buildPartial()` |
    | `Response.MarketPriceList.Builder` | `clear()` |
    | `Response.MarketPriceList.Builder` | `clearBuyTokenId()` `bytes buy_token_id = 2;` |
    | `Response.MarketPriceList.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.MarketPriceList.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.MarketPriceList.Builder` | `clearPrices()` `repeated .protocol.MarketPrice prices = 3;` |
    | `Response.MarketPriceList.Builder` | `clearSellTokenId()` `bytes sell_token_id = 1;` |
    | `Response.MarketPriceList.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getBuyTokenId()` `bytes buy_token_id = 2;` |
    | `Response.MarketPriceList` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Response.MarketPrice` | `getPrices(int index)` `repeated .protocol.MarketPrice prices = 3;` |
    | `Response.MarketPrice.Builder` | `getPricesBuilder(int index)` `repeated .protocol.MarketPrice prices = 3;` |
    | `java.util.List<Response.MarketPrice.Builder>` | `getPricesBuilderList()` `repeated .protocol.MarketPrice prices = 3;` |
    | `int` | `getPricesCount()` `repeated .protocol.MarketPrice prices = 3;` |
    | `java.util.List<Response.MarketPrice>` | `getPricesList()` `repeated .protocol.MarketPrice prices = 3;` |
    | `Response.MarketPriceOrBuilder` | `getPricesOrBuilder(int index)` `repeated .protocol.MarketPrice prices = 3;` |
    | `java.util.List<? extends Response.MarketPriceOrBuilder>` | `getPricesOrBuilderList()` `repeated .protocol.MarketPrice prices = 3;` |
    | `com.google.protobuf.ByteString` | `getSellTokenId()` `bytes sell_token_id = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.MarketPriceList.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.MarketPriceList.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.MarketPriceList.Builder` | `mergeFrom(Response.MarketPriceList other)` |
    | `Response.MarketPriceList.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.MarketPriceList.Builder` | `removePrices(int index)` `repeated .protocol.MarketPrice prices = 3;` |
    | `Response.MarketPriceList.Builder` | `setBuyTokenId(com.google.protobuf.ByteString value)` `bytes buy_token_id = 2;` |
    | `Response.MarketPriceList.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.MarketPriceList.Builder` | `setPrices(int index, Response.MarketPrice.Builder builderForValue)` `repeated .protocol.MarketPrice prices = 3;` |
    | `Response.MarketPriceList.Builder` | `setPrices(int index, Response.MarketPrice value)` `repeated .protocol.MarketPrice prices = 3;` |
    | `Response.MarketPriceList.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.MarketPriceList.Builder` | `setSellTokenId(com.google.protobuf.ByteString value)` `bytes sell_token_id = 1;` |
    | `Response.MarketPriceList.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

    - ### Methods inherited from class com.google.protobuf.GeneratedMessageV3.Builder

      `getAllFields, getField, getFieldBuilder, getOneofFieldDescriptor, getParentForChildren, getRepeatedField, getRepeatedFieldBuilder, getRepeatedFieldCount, getUnknownFields, getUnknownFieldSetBuilder, hasField, hasOneof, internalGetMapField, internalGetMapFieldReflection, internalGetMutableMapField, internalGetMutableMapFieldReflection, isClean, markClean, mergeUnknownLengthDelimitedField, mergeUnknownVarintField, newBuilderForField, onBuilt, onChanged, parseUnknownField, setUnknownFieldSetBuilder, setUnknownFieldsProto3`
    - ### Methods inherited from class com.google.protobuf.AbstractMessage.Builder

      `findInitializationErrors, getInitializationErrorString, internalMergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, newUninitializedMessageException, toString`
    - ### Methods inherited from class com.google.protobuf.AbstractMessageLite.Builder

      `addAll, addAll, mergeDelimitedFrom, mergeDelimitedFrom, newUninitializedMessageException`
    - ### Methods inherited from class java.lang.Object

      `equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`
    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.Message.Builder

      `mergeDelimitedFrom, mergeDelimitedFrom`

* + ### Method Detail

    - #### getDescriptor

      ```
      public static final com.google.protobuf.Descriptors.Descriptor getDescriptor()
      ```
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPriceList.Builder>`
    - #### clear

      ```
      public Response.MarketPriceList.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPriceList.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPriceList.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.MarketPriceList getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.MarketPriceList build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.MarketPriceList buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.MarketPriceList.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPriceList.Builder>`
    - #### setField

      ```
      public Response.MarketPriceList.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPriceList.Builder>`
    - #### clearField

      ```
      public Response.MarketPriceList.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPriceList.Builder>`
    - #### clearOneof

      ```
      public Response.MarketPriceList.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPriceList.Builder>`
    - #### setRepeatedField

      ```
      public Response.MarketPriceList.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               int index,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPriceList.Builder>`
    - #### addRepeatedField

      ```
      public Response.MarketPriceList.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPriceList.Builder>`
    - #### mergeFrom

      ```
      public Response.MarketPriceList.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.MarketPriceList.Builder>`
    - #### mergeFrom

      ```
      public Response.MarketPriceList.Builder mergeFrom(Response.MarketPriceList other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPriceList.Builder>`
    - #### mergeFrom

      ```
      public Response.MarketPriceList.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                 throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.MarketPriceList.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getSellTokenId

      ```
      public com.google.protobuf.ByteString getSellTokenId()
      ```

      `bytes sell_token_id = 1;`

      Specified by:
      :   `getSellTokenId` in interface `Response.MarketPriceListOrBuilder`

      Returns:
      :   The sellTokenId.
    - #### setSellTokenId

      ```
      public Response.MarketPriceList.Builder setSellTokenId(com.google.protobuf.ByteString value)
      ```

      `bytes sell_token_id = 1;`

      Parameters:
      :   `value` - The sellTokenId to set.

      Returns:
      :   This builder for chaining.
    - #### clearSellTokenId

      ```
      public Response.MarketPriceList.Builder clearSellTokenId()
      ```

      `bytes sell_token_id = 1;`

      Returns:
      :   This builder for chaining.
    - #### getBuyTokenId

      ```
      public com.google.protobuf.ByteString getBuyTokenId()
      ```

      `bytes buy_token_id = 2;`

      Specified by:
      :   `getBuyTokenId` in interface `Response.MarketPriceListOrBuilder`

      Returns:
      :   The buyTokenId.
    - #### setBuyTokenId

      ```
      public Response.MarketPriceList.Builder setBuyTokenId(com.google.protobuf.ByteString value)
      ```

      `bytes buy_token_id = 2;`

      Parameters:
      :   `value` - The buyTokenId to set.

      Returns:
      :   This builder for chaining.
    - #### clearBuyTokenId

      ```
      public Response.MarketPriceList.Builder clearBuyTokenId()
      ```

      `bytes buy_token_id = 2;`

      Returns:
      :   This builder for chaining.
    - #### getPricesList

      ```
      public java.util.List<Response.MarketPrice> getPricesList()
      ```

      `repeated .protocol.MarketPrice prices = 3;`

      Specified by:
      :   `getPricesList` in interface `Response.MarketPriceListOrBuilder`
    - #### getPricesCount

      ```
      public int getPricesCount()
      ```

      `repeated .protocol.MarketPrice prices = 3;`

      Specified by:
      :   `getPricesCount` in interface `Response.MarketPriceListOrBuilder`
    - #### getPrices

      ```
      public Response.MarketPrice getPrices(int index)
      ```

      `repeated .protocol.MarketPrice prices = 3;`

      Specified by:
      :   `getPrices` in interface `Response.MarketPriceListOrBuilder`
    - #### setPrices

      ```
      public Response.MarketPriceList.Builder setPrices(int index,
                                                        Response.MarketPrice value)
      ```

      `repeated .protocol.MarketPrice prices = 3;`
    - #### setPrices

      ```
      public Response.MarketPriceList.Builder setPrices(int index,
                                                        Response.MarketPrice.Builder builderForValue)
      ```

      `repeated .protocol.MarketPrice prices = 3;`
    - #### addPrices

      ```
      public Response.MarketPriceList.Builder addPrices(Response.MarketPrice value)
      ```

      `repeated .protocol.MarketPrice prices = 3;`
    - #### addPrices

      ```
      public Response.MarketPriceList.Builder addPrices(int index,
                                                        Response.MarketPrice value)
      ```

      `repeated .protocol.MarketPrice prices = 3;`
    - #### addPrices

      ```
      public Response.MarketPriceList.Builder addPrices(Response.MarketPrice.Builder builderForValue)
      ```

      `repeated .protocol.MarketPrice prices = 3;`
    - #### addPrices

      ```
      public Response.MarketPriceList.Builder addPrices(int index,
                                                        Response.MarketPrice.Builder builderForValue)
      ```

      `repeated .protocol.MarketPrice prices = 3;`
    - #### addAllPrices

      ```
      public Response.MarketPriceList.Builder addAllPrices(java.lang.Iterable<? extends Response.MarketPrice> values)
      ```

      `repeated .protocol.MarketPrice prices = 3;`
    - #### clearPrices

      ```
      public Response.MarketPriceList.Builder clearPrices()
      ```

      `repeated .protocol.MarketPrice prices = 3;`
    - #### removePrices

      ```
      public Response.MarketPriceList.Builder removePrices(int index)
      ```

      `repeated .protocol.MarketPrice prices = 3;`
    - #### getPricesBuilder

      ```
      public Response.MarketPrice.Builder getPricesBuilder(int index)
      ```

      `repeated .protocol.MarketPrice prices = 3;`
    - #### getPricesOrBuilder

      ```
      public Response.MarketPriceOrBuilder getPricesOrBuilder(int index)
      ```

      `repeated .protocol.MarketPrice prices = 3;`

      Specified by:
      :   `getPricesOrBuilder` in interface `Response.MarketPriceListOrBuilder`
    - #### getPricesOrBuilderList

      ```
      public java.util.List<? extends Response.MarketPriceOrBuilder> getPricesOrBuilderList()
      ```

      `repeated .protocol.MarketPrice prices = 3;`

      Specified by:
      :   `getPricesOrBuilderList` in interface `Response.MarketPriceListOrBuilder`
    - #### addPricesBuilder

      ```
      public Response.MarketPrice.Builder addPricesBuilder()
      ```

      `repeated .protocol.MarketPrice prices = 3;`
    - #### addPricesBuilder

      ```
      public Response.MarketPrice.Builder addPricesBuilder(int index)
      ```

      `repeated .protocol.MarketPrice prices = 3;`
    - #### getPricesBuilderList

      ```
      public java.util.List<Response.MarketPrice.Builder> getPricesBuilderList()
      ```

      `repeated .protocol.MarketPrice prices = 3;`
    - #### setUnknownFields

      ```
      public final Response.MarketPriceList.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPriceList.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.MarketPriceList.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPriceList.Builder>`