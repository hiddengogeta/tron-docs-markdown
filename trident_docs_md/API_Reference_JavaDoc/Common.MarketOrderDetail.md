

org.tron.trident.proto

## Class Common.MarketOrderDetail

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Common.MarketOrderDetail

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Common.MarketOrderDetailOrBuilder](../../../../org/tron/trident/proto/Common.MarketOrderDetailOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Common](../../../../org/tron/trident/proto/Common.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Common.MarketOrderDetail
  extends com.google.protobuf.GeneratedMessageV3
  implements Common.MarketOrderDetailOrBuilder
  ```

  Protobuf type `protocol.MarketOrderDetail`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Common.MarketOrderDetail)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Common.MarketOrderDetail.Builder` Protobuf type `protocol.MarketOrderDetail` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `FILLBUYQUANTITY_FIELD_NUMBER` |
    | `static int` | `FILLSELLQUANTITY_FIELD_NUMBER` |
    | `static int` | `MAKERORDERID_FIELD_NUMBER` |
    | `static int` | `TAKERORDERID_FIELD_NUMBER` |

    - ### Fields inherited from class com.google.protobuf.GeneratedMessageV3

      `alwaysUseFieldBuilders, unknownFields`
    - ### Fields inherited from class com.google.protobuf.AbstractMessage

      `memoizedSize`
    - ### Fields inherited from class com.google.protobuf.AbstractMessageLite

      `memoizedHashCode`
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `boolean` | `equals(java.lang.Object obj)` |
    | `static Common.MarketOrderDetail` | `getDefaultInstance()` |
    | `Common.MarketOrderDetail` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `long` | `getFillBuyQuantity()` `int64 fillBuyQuantity = 4;` |
    | `long` | `getFillSellQuantity()` `int64 fillSellQuantity = 3;` |
    | `com.google.protobuf.ByteString` | `getMakerOrderId()` `bytes makerOrderId = 1;` |
    | `com.google.protobuf.Parser<Common.MarketOrderDetail>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `com.google.protobuf.ByteString` | `getTakerOrderId()` `bytes takerOrderId = 2;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Common.MarketOrderDetail.Builder` | `newBuilder()` |
    | `static Common.MarketOrderDetail.Builder` | `newBuilder(Common.MarketOrderDetail prototype)` |
    | `Common.MarketOrderDetail.Builder` | `newBuilderForType()` |
    | `protected Common.MarketOrderDetail.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Common.MarketOrderDetail` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Common.MarketOrderDetail` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.MarketOrderDetail` | `parseFrom(byte[] data)` |
    | `static Common.MarketOrderDetail` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.MarketOrderDetail` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Common.MarketOrderDetail` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.MarketOrderDetail` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Common.MarketOrderDetail` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.MarketOrderDetail` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Common.MarketOrderDetail` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.MarketOrderDetail` | `parseFrom(java.io.InputStream input)` |
    | `static Common.MarketOrderDetail` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Common.MarketOrderDetail>` | `parser()` |
    | `Common.MarketOrderDetail.Builder` | `toBuilder()` |
    | `void` | `writeTo(com.google.protobuf.CodedOutputStream output)` |

    - ### Methods inherited from class com.google.protobuf.GeneratedMessageV3

      `canUseUnsafe, computeStringSize, computeStringSizeNoTag, emptyBooleanList, emptyDoubleList, emptyFloatList, emptyIntList, emptyList, emptyLongList, getAllFields, getDescriptorForType, getField, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof, internalGetMapField, internalGetMapFieldReflection, isStringEmpty, makeExtensionsImmutable, makeMutableCopy, makeMutableCopy, mergeFromAndMakeImmutableInternal, mutableCopy, mutableCopy, mutableCopy, mutableCopy, mutableCopy, newBooleanList, newBuilderForType, newDoubleList, newFloatList, newIntList, newLongList, parseDelimitedWithIOException, parseDelimitedWithIOException, parseUnknownField, parseUnknownFieldProto3, parseWithIOException, parseWithIOException, parseWithIOException, parseWithIOException, serializeBooleanMapTo, serializeIntegerMapTo, serializeLongMapTo, serializeStringMapTo, writeReplace, writeString, writeStringNoTag`
    - ### Methods inherited from class com.google.protobuf.AbstractMessage

      `findInitializationErrors, getInitializationErrorString, hashBoolean, hashEnum, hashEnumList, hashFields, hashLong, toString`
    - ### Methods inherited from class com.google.protobuf.AbstractMessageLite

      `addAll, addAll, checkByteStringIsUtf8, toByteArray, toByteString, writeDelimitedTo, writeTo`
    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, wait, wait, wait`
    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLite

      `toByteArray, toByteString, writeDelimitedTo, writeTo`

* + ### Field Detail

    - #### MAKERORDERID\_FIELD\_NUMBER

      ```
      public static final int MAKERORDERID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.MarketOrderDetail.MAKERORDERID_FIELD_NUMBER)
    - #### TAKERORDERID\_FIELD\_NUMBER

      ```
      public static final int TAKERORDERID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.MarketOrderDetail.TAKERORDERID_FIELD_NUMBER)
    - #### FILLSELLQUANTITY\_FIELD\_NUMBER

      ```
      public static final int FILLSELLQUANTITY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.MarketOrderDetail.FILLSELLQUANTITY_FIELD_NUMBER)
    - #### FILLBUYQUANTITY\_FIELD\_NUMBER

      ```
      public static final int FILLBUYQUANTITY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.MarketOrderDetail.FILLBUYQUANTITY_FIELD_NUMBER)
  + ### Method Detail

    - #### newInstance

      ```
      protected java.lang.Object newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)
      ```

      Overrides:
      :   `newInstance` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDescriptor

      ```
      public static final com.google.protobuf.Descriptors.Descriptor getDescriptor()
      ```
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getMakerOrderId

      ```
      public com.google.protobuf.ByteString getMakerOrderId()
      ```

      `bytes makerOrderId = 1;`

      Specified by:
      :   `getMakerOrderId` in interface `Common.MarketOrderDetailOrBuilder`

      Returns:
      :   The makerOrderId.
    - #### getTakerOrderId

      ```
      public com.google.protobuf.ByteString getTakerOrderId()
      ```

      `bytes takerOrderId = 2;`

      Specified by:
      :   `getTakerOrderId` in interface `Common.MarketOrderDetailOrBuilder`

      Returns:
      :   The takerOrderId.
    - #### getFillSellQuantity

      ```
      public long getFillSellQuantity()
      ```

      `int64 fillSellQuantity = 3;`

      Specified by:
      :   `getFillSellQuantity` in interface `Common.MarketOrderDetailOrBuilder`

      Returns:
      :   The fillSellQuantity.
    - #### getFillBuyQuantity

      ```
      public long getFillBuyQuantity()
      ```

      `int64 fillBuyQuantity = 4;`

      Specified by:
      :   `getFillBuyQuantity` in interface `Common.MarketOrderDetailOrBuilder`

      Returns:
      :   The fillBuyQuantity.
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3`
    - #### writeTo

      ```
      public void writeTo(com.google.protobuf.CodedOutputStream output)
                   throws java.io.IOException
      ```

      Specified by:
      :   `writeTo` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `writeTo` in class `com.google.protobuf.GeneratedMessageV3`

      Throws:
      :   `java.io.IOException`
    - #### getSerializedSize

      ```
      public int getSerializedSize()
      ```

      Specified by:
      :   `getSerializedSize` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getSerializedSize` in class `com.google.protobuf.GeneratedMessageV3`
    - #### equals

      ```
      public boolean equals(java.lang.Object obj)
      ```

      Specified by:
      :   `equals` in interface `com.google.protobuf.Message`

      Overrides:
      :   `equals` in class `com.google.protobuf.AbstractMessage`
    - #### hashCode

      ```
      public int hashCode()
      ```

      Specified by:
      :   `hashCode` in interface `com.google.protobuf.Message`

      Overrides:
      :   `hashCode` in class `com.google.protobuf.AbstractMessage`
    - #### parseFrom

      ```
      public static Common.MarketOrderDetail parseFrom(java.nio.ByteBuffer data)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.MarketOrderDetail parseFrom(java.nio.ByteBuffer data,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.MarketOrderDetail parseFrom(com.google.protobuf.ByteString data)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.MarketOrderDetail parseFrom(com.google.protobuf.ByteString data,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.MarketOrderDetail parseFrom(byte[] data)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.MarketOrderDetail parseFrom(byte[] data,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.MarketOrderDetail parseFrom(java.io.InputStream input)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Common.MarketOrderDetail parseFrom(java.io.InputStream input,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Common.MarketOrderDetail parseDelimitedFrom(java.io.InputStream input)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Common.MarketOrderDetail parseDelimitedFrom(java.io.InputStream input,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Common.MarketOrderDetail parseFrom(com.google.protobuf.CodedInputStream input)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Common.MarketOrderDetail parseFrom(com.google.protobuf.CodedInputStream input,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Common.MarketOrderDetail.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Common.MarketOrderDetail.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Common.MarketOrderDetail.Builder newBuilder(Common.MarketOrderDetail prototype)
      ```
    - #### toBuilder

      ```
      public Common.MarketOrderDetail.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Common.MarketOrderDetail.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Common.MarketOrderDetail getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Common.MarketOrderDetail> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Common.MarketOrderDetail> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Common.MarketOrderDetail getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`