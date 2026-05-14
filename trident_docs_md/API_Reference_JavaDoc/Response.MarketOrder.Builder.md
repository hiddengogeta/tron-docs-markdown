

org.tron.trident.proto

## Class Response.MarketOrder.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.MarketOrder.Builder](../../../../org/tron/trident/proto/Response.MarketOrder.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.MarketOrder.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.MarketOrderOrBuilder](../../../../org/tron/trident/proto/Response.MarketOrderOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.MarketOrder](../../../../org/tron/trident/proto/Response.MarketOrder.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.MarketOrder.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrder.Builder>
  implements Response.MarketOrderOrBuilder
  ```

  Protobuf type `protocol.MarketOrder`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.MarketOrder.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.MarketOrder` | `build()` |
    | `Response.MarketOrder` | `buildPartial()` |
    | `Response.MarketOrder.Builder` | `clear()` |
    | `Response.MarketOrder.Builder` | `clearBuyTokenId()` `bytes buy_token_id = 6;` |
    | `Response.MarketOrder.Builder` | `clearBuyTokenQuantity()` min to receive |
    | `Response.MarketOrder.Builder` | `clearCreateTime()` `int64 create_time = 3;` |
    | `Response.MarketOrder.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.MarketOrder.Builder` | `clearNext()` `bytes next = 13;` |
    | `Response.MarketOrder.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.MarketOrder.Builder` | `clearOrderId()` `bytes order_id = 1;` |
    | `Response.MarketOrder.Builder` | `clearOwnerAddress()` `bytes owner_address = 2;` |
    | `Response.MarketOrder.Builder` | `clearPrev()` `bytes prev = 12;` |
    | `Response.MarketOrder.Builder` | `clearSellTokenId()` `bytes sell_token_id = 4;` |
    | `Response.MarketOrder.Builder` | `clearSellTokenQuantity()` `int64 sell_token_quantity = 5;` |
    | `Response.MarketOrder.Builder` | `clearSellTokenQuantityRemain()` `int64 sell_token_quantity_remain = 9;` |
    | `Response.MarketOrder.Builder` | `clearSellTokenQuantityReturn()` When state != ACTIVE and sell\_token\_quantity\_return !=0, it means that some sell tokens are returned to the account due to insufficient remaining amount |
    | `Response.MarketOrder.Builder` | `clearState()` `.protocol.MarketOrder.State state = 11;` |
    | `Response.MarketOrder.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getBuyTokenId()` `bytes buy_token_id = 6;` |
    | `long` | `getBuyTokenQuantity()` min to receive |
    | `long` | `getCreateTime()` `int64 create_time = 3;` |
    | `Response.MarketOrder` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
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
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.MarketOrder.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.MarketOrder.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.MarketOrder.Builder` | `mergeFrom(Response.MarketOrder other)` |
    | `Response.MarketOrder.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.MarketOrder.Builder` | `setBuyTokenId(com.google.protobuf.ByteString value)` `bytes buy_token_id = 6;` |
    | `Response.MarketOrder.Builder` | `setBuyTokenQuantity(long value)` min to receive |
    | `Response.MarketOrder.Builder` | `setCreateTime(long value)` `int64 create_time = 3;` |
    | `Response.MarketOrder.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.MarketOrder.Builder` | `setNext(com.google.protobuf.ByteString value)` `bytes next = 13;` |
    | `Response.MarketOrder.Builder` | `setOrderId(com.google.protobuf.ByteString value)` `bytes order_id = 1;` |
    | `Response.MarketOrder.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 2;` |
    | `Response.MarketOrder.Builder` | `setPrev(com.google.protobuf.ByteString value)` `bytes prev = 12;` |
    | `Response.MarketOrder.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.MarketOrder.Builder` | `setSellTokenId(com.google.protobuf.ByteString value)` `bytes sell_token_id = 4;` |
    | `Response.MarketOrder.Builder` | `setSellTokenQuantity(long value)` `int64 sell_token_quantity = 5;` |
    | `Response.MarketOrder.Builder` | `setSellTokenQuantityRemain(long value)` `int64 sell_token_quantity_remain = 9;` |
    | `Response.MarketOrder.Builder` | `setSellTokenQuantityReturn(long value)` When state != ACTIVE and sell\_token\_quantity\_return !=0, it means that some sell tokens are returned to the account due to insufficient remaining amount |
    | `Response.MarketOrder.Builder` | `setState(Response.MarketOrder.State value)` `.protocol.MarketOrder.State state = 11;` |
    | `Response.MarketOrder.Builder` | `setStateValue(int value)` `.protocol.MarketOrder.State state = 11;` |
    | `Response.MarketOrder.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrder.Builder>`
    - #### clear

      ```
      public Response.MarketOrder.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrder.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrder.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.MarketOrder getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.MarketOrder build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.MarketOrder buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.MarketOrder.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrder.Builder>`
    - #### setField

      ```
      public Response.MarketOrder.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                   java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrder.Builder>`
    - #### clearField

      ```
      public Response.MarketOrder.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrder.Builder>`
    - #### clearOneof

      ```
      public Response.MarketOrder.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrder.Builder>`
    - #### setRepeatedField

      ```
      public Response.MarketOrder.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                           int index,
                                                           java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrder.Builder>`
    - #### addRepeatedField

      ```
      public Response.MarketOrder.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                           java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrder.Builder>`
    - #### mergeFrom

      ```
      public Response.MarketOrder.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.MarketOrder.Builder>`
    - #### mergeFrom

      ```
      public Response.MarketOrder.Builder mergeFrom(Response.MarketOrder other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrder.Builder>`
    - #### mergeFrom

      ```
      public Response.MarketOrder.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                    com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                             throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.MarketOrder.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOrderId

      ```
      public com.google.protobuf.ByteString getOrderId()
      ```

      `bytes order_id = 1;`

      Specified by:
      :   `getOrderId` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The orderId.
    - #### setOrderId

      ```
      public Response.MarketOrder.Builder setOrderId(com.google.protobuf.ByteString value)
      ```

      `bytes order_id = 1;`

      Parameters:
      :   `value` - The orderId to set.

      Returns:
      :   This builder for chaining.
    - #### clearOrderId

      ```
      public Response.MarketOrder.Builder clearOrderId()
      ```

      `bytes order_id = 1;`

      Returns:
      :   This builder for chaining.
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 2;`

      Specified by:
      :   `getOwnerAddress` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Response.MarketOrder.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 2;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Response.MarketOrder.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 2;`

      Returns:
      :   This builder for chaining.
    - #### getCreateTime

      ```
      public long getCreateTime()
      ```

      `int64 create_time = 3;`

      Specified by:
      :   `getCreateTime` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The createTime.
    - #### setCreateTime

      ```
      public Response.MarketOrder.Builder setCreateTime(long value)
      ```

      `int64 create_time = 3;`

      Parameters:
      :   `value` - The createTime to set.

      Returns:
      :   This builder for chaining.
    - #### clearCreateTime

      ```
      public Response.MarketOrder.Builder clearCreateTime()
      ```

      `int64 create_time = 3;`

      Returns:
      :   This builder for chaining.
    - #### getSellTokenId

      ```
      public com.google.protobuf.ByteString getSellTokenId()
      ```

      `bytes sell_token_id = 4;`

      Specified by:
      :   `getSellTokenId` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The sellTokenId.
    - #### setSellTokenId

      ```
      public Response.MarketOrder.Builder setSellTokenId(com.google.protobuf.ByteString value)
      ```

      `bytes sell_token_id = 4;`

      Parameters:
      :   `value` - The sellTokenId to set.

      Returns:
      :   This builder for chaining.
    - #### clearSellTokenId

      ```
      public Response.MarketOrder.Builder clearSellTokenId()
      ```

      `bytes sell_token_id = 4;`

      Returns:
      :   This builder for chaining.
    - #### getSellTokenQuantity

      ```
      public long getSellTokenQuantity()
      ```

      `int64 sell_token_quantity = 5;`

      Specified by:
      :   `getSellTokenQuantity` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The sellTokenQuantity.
    - #### setSellTokenQuantity

      ```
      public Response.MarketOrder.Builder setSellTokenQuantity(long value)
      ```

      `int64 sell_token_quantity = 5;`

      Parameters:
      :   `value` - The sellTokenQuantity to set.

      Returns:
      :   This builder for chaining.
    - #### clearSellTokenQuantity

      ```
      public Response.MarketOrder.Builder clearSellTokenQuantity()
      ```

      `int64 sell_token_quantity = 5;`

      Returns:
      :   This builder for chaining.
    - #### getBuyTokenId

      ```
      public com.google.protobuf.ByteString getBuyTokenId()
      ```

      `bytes buy_token_id = 6;`

      Specified by:
      :   `getBuyTokenId` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The buyTokenId.
    - #### setBuyTokenId

      ```
      public Response.MarketOrder.Builder setBuyTokenId(com.google.protobuf.ByteString value)
      ```

      `bytes buy_token_id = 6;`

      Parameters:
      :   `value` - The buyTokenId to set.

      Returns:
      :   This builder for chaining.
    - #### clearBuyTokenId

      ```
      public Response.MarketOrder.Builder clearBuyTokenId()
      ```

      `bytes buy_token_id = 6;`

      Returns:
      :   This builder for chaining.
    - #### getBuyTokenQuantity

      ```
      public long getBuyTokenQuantity()
      ```

      ```
       min to receive
      ```

      `int64 buy_token_quantity = 7;`

      Specified by:
      :   `getBuyTokenQuantity` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The buyTokenQuantity.
    - #### setBuyTokenQuantity

      ```
      public Response.MarketOrder.Builder setBuyTokenQuantity(long value)
      ```

      ```
       min to receive
      ```

      `int64 buy_token_quantity = 7;`

      Parameters:
      :   `value` - The buyTokenQuantity to set.

      Returns:
      :   This builder for chaining.
    - #### clearBuyTokenQuantity

      ```
      public Response.MarketOrder.Builder clearBuyTokenQuantity()
      ```

      ```
       min to receive
      ```

      `int64 buy_token_quantity = 7;`

      Returns:
      :   This builder for chaining.
    - #### getSellTokenQuantityRemain

      ```
      public long getSellTokenQuantityRemain()
      ```

      `int64 sell_token_quantity_remain = 9;`

      Specified by:
      :   `getSellTokenQuantityRemain` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The sellTokenQuantityRemain.
    - #### setSellTokenQuantityRemain

      ```
      public Response.MarketOrder.Builder setSellTokenQuantityRemain(long value)
      ```

      `int64 sell_token_quantity_remain = 9;`

      Parameters:
      :   `value` - The sellTokenQuantityRemain to set.

      Returns:
      :   This builder for chaining.
    - #### clearSellTokenQuantityRemain

      ```
      public Response.MarketOrder.Builder clearSellTokenQuantityRemain()
      ```

      `int64 sell_token_quantity_remain = 9;`

      Returns:
      :   This builder for chaining.
    - #### getSellTokenQuantityReturn

      ```
      public long getSellTokenQuantityReturn()
      ```

      ```
       When state != ACTIVE and sell_token_quantity_return !=0,
       it means that some sell tokens are returned to the account due to
       insufficient remaining amount
      ```

      `int64 sell_token_quantity_return = 10;`

      Specified by:
      :   `getSellTokenQuantityReturn` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The sellTokenQuantityReturn.
    - #### setSellTokenQuantityReturn

      ```
      public Response.MarketOrder.Builder setSellTokenQuantityReturn(long value)
      ```

      ```
       When state != ACTIVE and sell_token_quantity_return !=0,
       it means that some sell tokens are returned to the account due to
       insufficient remaining amount
      ```

      `int64 sell_token_quantity_return = 10;`

      Parameters:
      :   `value` - The sellTokenQuantityReturn to set.

      Returns:
      :   This builder for chaining.
    - #### clearSellTokenQuantityReturn

      ```
      public Response.MarketOrder.Builder clearSellTokenQuantityReturn()
      ```

      ```
       When state != ACTIVE and sell_token_quantity_return !=0,
       it means that some sell tokens are returned to the account due to
       insufficient remaining amount
      ```

      `int64 sell_token_quantity_return = 10;`

      Returns:
      :   This builder for chaining.
    - #### getStateValue

      ```
      public int getStateValue()
      ```

      `.protocol.MarketOrder.State state = 11;`

      Specified by:
      :   `getStateValue` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The enum numeric value on the wire for state.
    - #### setStateValue

      ```
      public Response.MarketOrder.Builder setStateValue(int value)
      ```

      `.protocol.MarketOrder.State state = 11;`

      Parameters:
      :   `value` - The enum numeric value on the wire for state to set.

      Returns:
      :   This builder for chaining.
    - #### getState

      ```
      public Response.MarketOrder.State getState()
      ```

      `.protocol.MarketOrder.State state = 11;`

      Specified by:
      :   `getState` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The state.
    - #### setState

      ```
      public Response.MarketOrder.Builder setState(Response.MarketOrder.State value)
      ```

      `.protocol.MarketOrder.State state = 11;`

      Parameters:
      :   `value` - The state to set.

      Returns:
      :   This builder for chaining.
    - #### clearState

      ```
      public Response.MarketOrder.Builder clearState()
      ```

      `.protocol.MarketOrder.State state = 11;`

      Returns:
      :   This builder for chaining.
    - #### getPrev

      ```
      public com.google.protobuf.ByteString getPrev()
      ```

      `bytes prev = 12;`

      Specified by:
      :   `getPrev` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The prev.
    - #### setPrev

      ```
      public Response.MarketOrder.Builder setPrev(com.google.protobuf.ByteString value)
      ```

      `bytes prev = 12;`

      Parameters:
      :   `value` - The prev to set.

      Returns:
      :   This builder for chaining.
    - #### clearPrev

      ```
      public Response.MarketOrder.Builder clearPrev()
      ```

      `bytes prev = 12;`

      Returns:
      :   This builder for chaining.
    - #### getNext

      ```
      public com.google.protobuf.ByteString getNext()
      ```

      `bytes next = 13;`

      Specified by:
      :   `getNext` in interface `Response.MarketOrderOrBuilder`

      Returns:
      :   The next.
    - #### setNext

      ```
      public Response.MarketOrder.Builder setNext(com.google.protobuf.ByteString value)
      ```

      `bytes next = 13;`

      Parameters:
      :   `value` - The next to set.

      Returns:
      :   This builder for chaining.
    - #### clearNext

      ```
      public Response.MarketOrder.Builder clearNext()
      ```

      `bytes next = 13;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.MarketOrder.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrder.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.MarketOrder.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrder.Builder>`