

org.tron.trident.proto

## Class Response.MarketPrice.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.MarketPrice.Builder](../../../../org/tron/trident/proto/Response.MarketPrice.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.MarketPrice.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.MarketPriceOrBuilder](../../../../org/tron/trident/proto/Response.MarketPriceOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.MarketPrice](../../../../org/tron/trident/proto/Response.MarketPrice.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.MarketPrice.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPrice.Builder>
  implements Response.MarketPriceOrBuilder
  ```

  Protobuf type `protocol.MarketPrice`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.MarketPrice.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.MarketPrice` | `build()` |
    | `Response.MarketPrice` | `buildPartial()` |
    | `Response.MarketPrice.Builder` | `clear()` |
    | `Response.MarketPrice.Builder` | `clearBuyTokenQuantity()` `int64 buy_token_quantity = 2;` |
    | `Response.MarketPrice.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.MarketPrice.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.MarketPrice.Builder` | `clearSellTokenQuantity()` `int64 sell_token_quantity = 1;` |
    | `Response.MarketPrice.Builder` | `clone()` |
    | `long` | `getBuyTokenQuantity()` `int64 buy_token_quantity = 2;` |
    | `Response.MarketPrice` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getSellTokenQuantity()` `int64 sell_token_quantity = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.MarketPrice.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.MarketPrice.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.MarketPrice.Builder` | `mergeFrom(Response.MarketPrice other)` |
    | `Response.MarketPrice.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.MarketPrice.Builder` | `setBuyTokenQuantity(long value)` `int64 buy_token_quantity = 2;` |
    | `Response.MarketPrice.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.MarketPrice.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.MarketPrice.Builder` | `setSellTokenQuantity(long value)` `int64 sell_token_quantity = 1;` |
    | `Response.MarketPrice.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPrice.Builder>`
    - #### clear

      ```
      public Response.MarketPrice.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPrice.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPrice.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.MarketPrice getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.MarketPrice build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.MarketPrice buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.MarketPrice.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPrice.Builder>`
    - #### setField

      ```
      public Response.MarketPrice.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                   java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPrice.Builder>`
    - #### clearField

      ```
      public Response.MarketPrice.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPrice.Builder>`
    - #### clearOneof

      ```
      public Response.MarketPrice.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPrice.Builder>`
    - #### setRepeatedField

      ```
      public Response.MarketPrice.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                           int index,
                                                           java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPrice.Builder>`
    - #### addRepeatedField

      ```
      public Response.MarketPrice.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                           java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPrice.Builder>`
    - #### mergeFrom

      ```
      public Response.MarketPrice.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.MarketPrice.Builder>`
    - #### mergeFrom

      ```
      public Response.MarketPrice.Builder mergeFrom(Response.MarketPrice other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPrice.Builder>`
    - #### mergeFrom

      ```
      public Response.MarketPrice.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                    com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                             throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.MarketPrice.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getSellTokenQuantity

      ```
      public long getSellTokenQuantity()
      ```

      `int64 sell_token_quantity = 1;`

      Specified by:
      :   `getSellTokenQuantity` in interface `Response.MarketPriceOrBuilder`

      Returns:
      :   The sellTokenQuantity.
    - #### setSellTokenQuantity

      ```
      public Response.MarketPrice.Builder setSellTokenQuantity(long value)
      ```

      `int64 sell_token_quantity = 1;`

      Parameters:
      :   `value` - The sellTokenQuantity to set.

      Returns:
      :   This builder for chaining.
    - #### clearSellTokenQuantity

      ```
      public Response.MarketPrice.Builder clearSellTokenQuantity()
      ```

      `int64 sell_token_quantity = 1;`

      Returns:
      :   This builder for chaining.
    - #### getBuyTokenQuantity

      ```
      public long getBuyTokenQuantity()
      ```

      `int64 buy_token_quantity = 2;`

      Specified by:
      :   `getBuyTokenQuantity` in interface `Response.MarketPriceOrBuilder`

      Returns:
      :   The buyTokenQuantity.
    - #### setBuyTokenQuantity

      ```
      public Response.MarketPrice.Builder setBuyTokenQuantity(long value)
      ```

      `int64 buy_token_quantity = 2;`

      Parameters:
      :   `value` - The buyTokenQuantity to set.

      Returns:
      :   This builder for chaining.
    - #### clearBuyTokenQuantity

      ```
      public Response.MarketPrice.Builder clearBuyTokenQuantity()
      ```

      `int64 buy_token_quantity = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.MarketPrice.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPrice.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.MarketPrice.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketPrice.Builder>`