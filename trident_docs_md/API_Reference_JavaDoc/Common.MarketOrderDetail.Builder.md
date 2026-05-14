

org.tron.trident.proto

## Class Common.MarketOrderDetail.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Common.MarketOrderDetail.Builder](../../../../org/tron/trident/proto/Common.MarketOrderDetail.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Common.MarketOrderDetail.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Common.MarketOrderDetailOrBuilder](../../../../org/tron/trident/proto/Common.MarketOrderDetailOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Common.MarketOrderDetail](../../../../org/tron/trident/proto/Common.MarketOrderDetail.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Common.MarketOrderDetail.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Common.MarketOrderDetail.Builder>
  implements Common.MarketOrderDetailOrBuilder
  ```

  Protobuf type `protocol.MarketOrderDetail`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Common.MarketOrderDetail.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Common.MarketOrderDetail` | `build()` |
    | `Common.MarketOrderDetail` | `buildPartial()` |
    | `Common.MarketOrderDetail.Builder` | `clear()` |
    | `Common.MarketOrderDetail.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Common.MarketOrderDetail.Builder` | `clearFillBuyQuantity()` `int64 fillBuyQuantity = 4;` |
    | `Common.MarketOrderDetail.Builder` | `clearFillSellQuantity()` `int64 fillSellQuantity = 3;` |
    | `Common.MarketOrderDetail.Builder` | `clearMakerOrderId()` `bytes makerOrderId = 1;` |
    | `Common.MarketOrderDetail.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Common.MarketOrderDetail.Builder` | `clearTakerOrderId()` `bytes takerOrderId = 2;` |
    | `Common.MarketOrderDetail.Builder` | `clone()` |
    | `Common.MarketOrderDetail` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getFillBuyQuantity()` `int64 fillBuyQuantity = 4;` |
    | `long` | `getFillSellQuantity()` `int64 fillSellQuantity = 3;` |
    | `com.google.protobuf.ByteString` | `getMakerOrderId()` `bytes makerOrderId = 1;` |
    | `com.google.protobuf.ByteString` | `getTakerOrderId()` `bytes takerOrderId = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Common.MarketOrderDetail.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Common.MarketOrderDetail.Builder` | `mergeFrom(Common.MarketOrderDetail other)` |
    | `Common.MarketOrderDetail.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Common.MarketOrderDetail.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Common.MarketOrderDetail.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Common.MarketOrderDetail.Builder` | `setFillBuyQuantity(long value)` `int64 fillBuyQuantity = 4;` |
    | `Common.MarketOrderDetail.Builder` | `setFillSellQuantity(long value)` `int64 fillSellQuantity = 3;` |
    | `Common.MarketOrderDetail.Builder` | `setMakerOrderId(com.google.protobuf.ByteString value)` `bytes makerOrderId = 1;` |
    | `Common.MarketOrderDetail.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Common.MarketOrderDetail.Builder` | `setTakerOrderId(com.google.protobuf.ByteString value)` `bytes takerOrderId = 2;` |
    | `Common.MarketOrderDetail.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.MarketOrderDetail.Builder>`
    - #### clear

      ```
      public Common.MarketOrderDetail.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.MarketOrderDetail.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.MarketOrderDetail.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Common.MarketOrderDetail getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Common.MarketOrderDetail build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Common.MarketOrderDetail buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Common.MarketOrderDetail.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.MarketOrderDetail.Builder>`
    - #### setField

      ```
      public Common.MarketOrderDetail.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.MarketOrderDetail.Builder>`
    - #### clearField

      ```
      public Common.MarketOrderDetail.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.MarketOrderDetail.Builder>`
    - #### clearOneof

      ```
      public Common.MarketOrderDetail.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.MarketOrderDetail.Builder>`
    - #### setRepeatedField

      ```
      public Common.MarketOrderDetail.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               int index,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.MarketOrderDetail.Builder>`
    - #### addRepeatedField

      ```
      public Common.MarketOrderDetail.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.MarketOrderDetail.Builder>`
    - #### mergeFrom

      ```
      public Common.MarketOrderDetail.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Common.MarketOrderDetail.Builder>`
    - #### mergeFrom

      ```
      public Common.MarketOrderDetail.Builder mergeFrom(Common.MarketOrderDetail other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.MarketOrderDetail.Builder>`
    - #### mergeFrom

      ```
      public Common.MarketOrderDetail.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                 throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Common.MarketOrderDetail.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getMakerOrderId

      ```
      public com.google.protobuf.ByteString getMakerOrderId()
      ```

      `bytes makerOrderId = 1;`

      Specified by:
      :   `getMakerOrderId` in interface `Common.MarketOrderDetailOrBuilder`

      Returns:
      :   The makerOrderId.
    - #### setMakerOrderId

      ```
      public Common.MarketOrderDetail.Builder setMakerOrderId(com.google.protobuf.ByteString value)
      ```

      `bytes makerOrderId = 1;`

      Parameters:
      :   `value` - The makerOrderId to set.

      Returns:
      :   This builder for chaining.
    - #### clearMakerOrderId

      ```
      public Common.MarketOrderDetail.Builder clearMakerOrderId()
      ```

      `bytes makerOrderId = 1;`

      Returns:
      :   This builder for chaining.
    - #### getTakerOrderId

      ```
      public com.google.protobuf.ByteString getTakerOrderId()
      ```

      `bytes takerOrderId = 2;`

      Specified by:
      :   `getTakerOrderId` in interface `Common.MarketOrderDetailOrBuilder`

      Returns:
      :   The takerOrderId.
    - #### setTakerOrderId

      ```
      public Common.MarketOrderDetail.Builder setTakerOrderId(com.google.protobuf.ByteString value)
      ```

      `bytes takerOrderId = 2;`

      Parameters:
      :   `value` - The takerOrderId to set.

      Returns:
      :   This builder for chaining.
    - #### clearTakerOrderId

      ```
      public Common.MarketOrderDetail.Builder clearTakerOrderId()
      ```

      `bytes takerOrderId = 2;`

      Returns:
      :   This builder for chaining.
    - #### getFillSellQuantity

      ```
      public long getFillSellQuantity()
      ```

      `int64 fillSellQuantity = 3;`

      Specified by:
      :   `getFillSellQuantity` in interface `Common.MarketOrderDetailOrBuilder`

      Returns:
      :   The fillSellQuantity.
    - #### setFillSellQuantity

      ```
      public Common.MarketOrderDetail.Builder setFillSellQuantity(long value)
      ```

      `int64 fillSellQuantity = 3;`

      Parameters:
      :   `value` - The fillSellQuantity to set.

      Returns:
      :   This builder for chaining.
    - #### clearFillSellQuantity

      ```
      public Common.MarketOrderDetail.Builder clearFillSellQuantity()
      ```

      `int64 fillSellQuantity = 3;`

      Returns:
      :   This builder for chaining.
    - #### getFillBuyQuantity

      ```
      public long getFillBuyQuantity()
      ```

      `int64 fillBuyQuantity = 4;`

      Specified by:
      :   `getFillBuyQuantity` in interface `Common.MarketOrderDetailOrBuilder`

      Returns:
      :   The fillBuyQuantity.
    - #### setFillBuyQuantity

      ```
      public Common.MarketOrderDetail.Builder setFillBuyQuantity(long value)
      ```

      `int64 fillBuyQuantity = 4;`

      Parameters:
      :   `value` - The fillBuyQuantity to set.

      Returns:
      :   This builder for chaining.
    - #### clearFillBuyQuantity

      ```
      public Common.MarketOrderDetail.Builder clearFillBuyQuantity()
      ```

      `int64 fillBuyQuantity = 4;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Common.MarketOrderDetail.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.MarketOrderDetail.Builder>`
    - #### mergeUnknownFields

      ```
      public final Common.MarketOrderDetail.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.MarketOrderDetail.Builder>`