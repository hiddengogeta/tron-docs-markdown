

org.tron.trident.proto

## Class Response.MarketOrderPair.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.MarketOrderPair.Builder](../../../../org/tron/trident/proto/Response.MarketOrderPair.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.MarketOrderPair.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.MarketOrderPairOrBuilder](../../../../org/tron/trident/proto/Response.MarketOrderPairOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.MarketOrderPair](../../../../org/tron/trident/proto/Response.MarketOrderPair.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.MarketOrderPair.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPair.Builder>
  implements Response.MarketOrderPairOrBuilder
  ```

  Protobuf type `protocol.MarketOrderPair`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.MarketOrderPair.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.MarketOrderPair` | `build()` |
    | `Response.MarketOrderPair` | `buildPartial()` |
    | `Response.MarketOrderPair.Builder` | `clear()` |
    | `Response.MarketOrderPair.Builder` | `clearBuyTokenId()` `bytes buy_token_id = 2;` |
    | `Response.MarketOrderPair.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.MarketOrderPair.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.MarketOrderPair.Builder` | `clearSellTokenId()` `bytes sell_token_id = 1;` |
    | `Response.MarketOrderPair.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getBuyTokenId()` `bytes buy_token_id = 2;` |
    | `Response.MarketOrderPair` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getSellTokenId()` `bytes sell_token_id = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.MarketOrderPair.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.MarketOrderPair.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.MarketOrderPair.Builder` | `mergeFrom(Response.MarketOrderPair other)` |
    | `Response.MarketOrderPair.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.MarketOrderPair.Builder` | `setBuyTokenId(com.google.protobuf.ByteString value)` `bytes buy_token_id = 2;` |
    | `Response.MarketOrderPair.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.MarketOrderPair.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.MarketOrderPair.Builder` | `setSellTokenId(com.google.protobuf.ByteString value)` `bytes sell_token_id = 1;` |
    | `Response.MarketOrderPair.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPair.Builder>`
    - #### clear

      ```
      public Response.MarketOrderPair.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPair.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPair.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.MarketOrderPair getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.MarketOrderPair build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.MarketOrderPair buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.MarketOrderPair.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPair.Builder>`
    - #### setField

      ```
      public Response.MarketOrderPair.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPair.Builder>`
    - #### clearField

      ```
      public Response.MarketOrderPair.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPair.Builder>`
    - #### clearOneof

      ```
      public Response.MarketOrderPair.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPair.Builder>`
    - #### setRepeatedField

      ```
      public Response.MarketOrderPair.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               int index,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPair.Builder>`
    - #### addRepeatedField

      ```
      public Response.MarketOrderPair.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPair.Builder>`
    - #### mergeFrom

      ```
      public Response.MarketOrderPair.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.MarketOrderPair.Builder>`
    - #### mergeFrom

      ```
      public Response.MarketOrderPair.Builder mergeFrom(Response.MarketOrderPair other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPair.Builder>`
    - #### mergeFrom

      ```
      public Response.MarketOrderPair.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                 throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.MarketOrderPair.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getSellTokenId

      ```
      public com.google.protobuf.ByteString getSellTokenId()
      ```

      `bytes sell_token_id = 1;`

      Specified by:
      :   `getSellTokenId` in interface `Response.MarketOrderPairOrBuilder`

      Returns:
      :   The sellTokenId.
    - #### setSellTokenId

      ```
      public Response.MarketOrderPair.Builder setSellTokenId(com.google.protobuf.ByteString value)
      ```

      `bytes sell_token_id = 1;`

      Parameters:
      :   `value` - The sellTokenId to set.

      Returns:
      :   This builder for chaining.
    - #### clearSellTokenId

      ```
      public Response.MarketOrderPair.Builder clearSellTokenId()
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
      :   `getBuyTokenId` in interface `Response.MarketOrderPairOrBuilder`

      Returns:
      :   The buyTokenId.
    - #### setBuyTokenId

      ```
      public Response.MarketOrderPair.Builder setBuyTokenId(com.google.protobuf.ByteString value)
      ```

      `bytes buy_token_id = 2;`

      Parameters:
      :   `value` - The buyTokenId to set.

      Returns:
      :   This builder for chaining.
    - #### clearBuyTokenId

      ```
      public Response.MarketOrderPair.Builder clearBuyTokenId()
      ```

      `bytes buy_token_id = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.MarketOrderPair.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPair.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.MarketOrderPair.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPair.Builder>`