

org.tron.trident.proto

## Class Response.Exchange.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.Exchange.Builder](../../../../org/tron/trident/proto/Response.Exchange.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.Exchange.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.ExchangeOrBuilder](../../../../org/tron/trident/proto/Response.ExchangeOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.Exchange](../../../../org/tron/trident/proto/Response.Exchange.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.Exchange.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.Exchange.Builder>
  implements Response.ExchangeOrBuilder
  ```

  Protobuf type `protocol.Exchange`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.Exchange.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.Exchange` | `build()` |
    | `Response.Exchange` | `buildPartial()` |
    | `Response.Exchange.Builder` | `clear()` |
    | `Response.Exchange.Builder` | `clearCreateTime()` `int64 create_time = 3;` |
    | `Response.Exchange.Builder` | `clearCreatorAddress()` `bytes creator_address = 2;` |
    | `Response.Exchange.Builder` | `clearExchangeId()` `int64 exchange_id = 1;` |
    | `Response.Exchange.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.Exchange.Builder` | `clearFirstTokenBalance()` `int64 first_token_balance = 7;` |
    | `Response.Exchange.Builder` | `clearFirstTokenId()` `bytes first_token_id = 6;` |
    | `Response.Exchange.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.Exchange.Builder` | `clearSecondTokenBalance()` `int64 second_token_balance = 9;` |
    | `Response.Exchange.Builder` | `clearSecondTokenId()` `bytes second_token_id = 8;` |
    | `Response.Exchange.Builder` | `clone()` |
    | `long` | `getCreateTime()` `int64 create_time = 3;` |
    | `com.google.protobuf.ByteString` | `getCreatorAddress()` `bytes creator_address = 2;` |
    | `Response.Exchange` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getExchangeId()` `int64 exchange_id = 1;` |
    | `long` | `getFirstTokenBalance()` `int64 first_token_balance = 7;` |
    | `com.google.protobuf.ByteString` | `getFirstTokenId()` `bytes first_token_id = 6;` |
    | `long` | `getSecondTokenBalance()` `int64 second_token_balance = 9;` |
    | `com.google.protobuf.ByteString` | `getSecondTokenId()` `bytes second_token_id = 8;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.Exchange.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.Exchange.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.Exchange.Builder` | `mergeFrom(Response.Exchange other)` |
    | `Response.Exchange.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.Exchange.Builder` | `setCreateTime(long value)` `int64 create_time = 3;` |
    | `Response.Exchange.Builder` | `setCreatorAddress(com.google.protobuf.ByteString value)` `bytes creator_address = 2;` |
    | `Response.Exchange.Builder` | `setExchangeId(long value)` `int64 exchange_id = 1;` |
    | `Response.Exchange.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.Exchange.Builder` | `setFirstTokenBalance(long value)` `int64 first_token_balance = 7;` |
    | `Response.Exchange.Builder` | `setFirstTokenId(com.google.protobuf.ByteString value)` `bytes first_token_id = 6;` |
    | `Response.Exchange.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.Exchange.Builder` | `setSecondTokenBalance(long value)` `int64 second_token_balance = 9;` |
    | `Response.Exchange.Builder` | `setSecondTokenId(com.google.protobuf.ByteString value)` `bytes second_token_id = 8;` |
    | `Response.Exchange.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Exchange.Builder>`
    - #### clear

      ```
      public Response.Exchange.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Exchange.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Exchange.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.Exchange getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.Exchange build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.Exchange buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.Exchange.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Exchange.Builder>`
    - #### setField

      ```
      public Response.Exchange.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Exchange.Builder>`
    - #### clearField

      ```
      public Response.Exchange.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Exchange.Builder>`
    - #### clearOneof

      ```
      public Response.Exchange.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Exchange.Builder>`
    - #### setRepeatedField

      ```
      public Response.Exchange.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                        int index,
                                                        java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Exchange.Builder>`
    - #### addRepeatedField

      ```
      public Response.Exchange.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                        java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Exchange.Builder>`
    - #### mergeFrom

      ```
      public Response.Exchange.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.Exchange.Builder>`
    - #### mergeFrom

      ```
      public Response.Exchange.Builder mergeFrom(Response.Exchange other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Exchange.Builder>`
    - #### mergeFrom

      ```
      public Response.Exchange.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                 com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                          throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.Exchange.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getExchangeId

      ```
      public long getExchangeId()
      ```

      `int64 exchange_id = 1;`

      Specified by:
      :   `getExchangeId` in interface `Response.ExchangeOrBuilder`

      Returns:
      :   The exchangeId.
    - #### setExchangeId

      ```
      public Response.Exchange.Builder setExchangeId(long value)
      ```

      `int64 exchange_id = 1;`

      Parameters:
      :   `value` - The exchangeId to set.

      Returns:
      :   This builder for chaining.
    - #### clearExchangeId

      ```
      public Response.Exchange.Builder clearExchangeId()
      ```

      `int64 exchange_id = 1;`

      Returns:
      :   This builder for chaining.
    - #### getCreatorAddress

      ```
      public com.google.protobuf.ByteString getCreatorAddress()
      ```

      `bytes creator_address = 2;`

      Specified by:
      :   `getCreatorAddress` in interface `Response.ExchangeOrBuilder`

      Returns:
      :   The creatorAddress.
    - #### setCreatorAddress

      ```
      public Response.Exchange.Builder setCreatorAddress(com.google.protobuf.ByteString value)
      ```

      `bytes creator_address = 2;`

      Parameters:
      :   `value` - The creatorAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearCreatorAddress

      ```
      public Response.Exchange.Builder clearCreatorAddress()
      ```

      `bytes creator_address = 2;`

      Returns:
      :   This builder for chaining.
    - #### getCreateTime

      ```
      public long getCreateTime()
      ```

      `int64 create_time = 3;`

      Specified by:
      :   `getCreateTime` in interface `Response.ExchangeOrBuilder`

      Returns:
      :   The createTime.
    - #### setCreateTime

      ```
      public Response.Exchange.Builder setCreateTime(long value)
      ```

      `int64 create_time = 3;`

      Parameters:
      :   `value` - The createTime to set.

      Returns:
      :   This builder for chaining.
    - #### clearCreateTime

      ```
      public Response.Exchange.Builder clearCreateTime()
      ```

      `int64 create_time = 3;`

      Returns:
      :   This builder for chaining.
    - #### getFirstTokenId

      ```
      public com.google.protobuf.ByteString getFirstTokenId()
      ```

      `bytes first_token_id = 6;`

      Specified by:
      :   `getFirstTokenId` in interface `Response.ExchangeOrBuilder`

      Returns:
      :   The firstTokenId.
    - #### setFirstTokenId

      ```
      public Response.Exchange.Builder setFirstTokenId(com.google.protobuf.ByteString value)
      ```

      `bytes first_token_id = 6;`

      Parameters:
      :   `value` - The firstTokenId to set.

      Returns:
      :   This builder for chaining.
    - #### clearFirstTokenId

      ```
      public Response.Exchange.Builder clearFirstTokenId()
      ```

      `bytes first_token_id = 6;`

      Returns:
      :   This builder for chaining.
    - #### getFirstTokenBalance

      ```
      public long getFirstTokenBalance()
      ```

      `int64 first_token_balance = 7;`

      Specified by:
      :   `getFirstTokenBalance` in interface `Response.ExchangeOrBuilder`

      Returns:
      :   The firstTokenBalance.
    - #### setFirstTokenBalance

      ```
      public Response.Exchange.Builder setFirstTokenBalance(long value)
      ```

      `int64 first_token_balance = 7;`

      Parameters:
      :   `value` - The firstTokenBalance to set.

      Returns:
      :   This builder for chaining.
    - #### clearFirstTokenBalance

      ```
      public Response.Exchange.Builder clearFirstTokenBalance()
      ```

      `int64 first_token_balance = 7;`

      Returns:
      :   This builder for chaining.
    - #### getSecondTokenId

      ```
      public com.google.protobuf.ByteString getSecondTokenId()
      ```

      `bytes second_token_id = 8;`

      Specified by:
      :   `getSecondTokenId` in interface `Response.ExchangeOrBuilder`

      Returns:
      :   The secondTokenId.
    - #### setSecondTokenId

      ```
      public Response.Exchange.Builder setSecondTokenId(com.google.protobuf.ByteString value)
      ```

      `bytes second_token_id = 8;`

      Parameters:
      :   `value` - The secondTokenId to set.

      Returns:
      :   This builder for chaining.
    - #### clearSecondTokenId

      ```
      public Response.Exchange.Builder clearSecondTokenId()
      ```

      `bytes second_token_id = 8;`

      Returns:
      :   This builder for chaining.
    - #### getSecondTokenBalance

      ```
      public long getSecondTokenBalance()
      ```

      `int64 second_token_balance = 9;`

      Specified by:
      :   `getSecondTokenBalance` in interface `Response.ExchangeOrBuilder`

      Returns:
      :   The secondTokenBalance.
    - #### setSecondTokenBalance

      ```
      public Response.Exchange.Builder setSecondTokenBalance(long value)
      ```

      `int64 second_token_balance = 9;`

      Parameters:
      :   `value` - The secondTokenBalance to set.

      Returns:
      :   This builder for chaining.
    - #### clearSecondTokenBalance

      ```
      public Response.Exchange.Builder clearSecondTokenBalance()
      ```

      `int64 second_token_balance = 9;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.Exchange.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Exchange.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.Exchange.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Exchange.Builder>`