

org.tron.trident.proto

## Class Response.ResourceReceipt

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.ResourceReceipt

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.ResourceReceiptOrBuilder](../../../../org/tron/trident/proto/Response.ResourceReceiptOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.ResourceReceipt
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.ResourceReceiptOrBuilder
  ```

  Protobuf type `protocol.ResourceReceipt`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.ResourceReceipt)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.ResourceReceipt.Builder` Protobuf type `protocol.ResourceReceipt` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `ENERGY_FEE_FIELD_NUMBER` |
    | `static int` | `ENERGY_PENALTY_TOTAL_FIELD_NUMBER` |
    | `static int` | `ENERGY_USAGE_FIELD_NUMBER` |
    | `static int` | `ENERGY_USAGE_TOTAL_FIELD_NUMBER` |
    | `static int` | `NET_FEE_FIELD_NUMBER` |
    | `static int` | `NET_USAGE_FIELD_NUMBER` |
    | `static int` | `ORIGIN_ENERGY_USAGE_FIELD_NUMBER` |
    | `static int` | `RESULT_FIELD_NUMBER` |

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
    | `static Response.ResourceReceipt` | `getDefaultInstance()` |
    | `Response.ResourceReceipt` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `long` | `getEnergyFee()` `int64 energy_fee = 2;` |
    | `long` | `getEnergyPenaltyTotal()` `int64 energy_penalty_total = 8;` |
    | `long` | `getEnergyUsage()` `int64 energy_usage = 1;` |
    | `long` | `getEnergyUsageTotal()` `int64 energy_usage_total = 4;` |
    | `long` | `getNetFee()` `int64 net_fee = 6;` |
    | `long` | `getNetUsage()` `int64 net_usage = 5;` |
    | `long` | `getOriginEnergyUsage()` `int64 origin_energy_usage = 3;` |
    | `com.google.protobuf.Parser<Response.ResourceReceipt>` | `getParserForType()` |
    | `Chain.Transaction.Result.contractResult` | `getResult()` `.protocol.Transaction.Result.contractResult result = 7;` |
    | `int` | `getResultValue()` `.protocol.Transaction.Result.contractResult result = 7;` |
    | `int` | `getSerializedSize()` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Response.ResourceReceipt.Builder` | `newBuilder()` |
    | `static Response.ResourceReceipt.Builder` | `newBuilder(Response.ResourceReceipt prototype)` |
    | `Response.ResourceReceipt.Builder` | `newBuilderForType()` |
    | `protected Response.ResourceReceipt.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.ResourceReceipt` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.ResourceReceipt` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.ResourceReceipt` | `parseFrom(byte[] data)` |
    | `static Response.ResourceReceipt` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.ResourceReceipt` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.ResourceReceipt` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.ResourceReceipt` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.ResourceReceipt` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.ResourceReceipt` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.ResourceReceipt` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.ResourceReceipt` | `parseFrom(java.io.InputStream input)` |
    | `static Response.ResourceReceipt` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.ResourceReceipt>` | `parser()` |
    | `Response.ResourceReceipt.Builder` | `toBuilder()` |
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

    - #### ENERGY\_USAGE\_FIELD\_NUMBER

      ```
      public static final int ENERGY_USAGE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.ResourceReceipt.ENERGY_USAGE_FIELD_NUMBER)
    - #### ENERGY\_FEE\_FIELD\_NUMBER

      ```
      public static final int ENERGY_FEE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.ResourceReceipt.ENERGY_FEE_FIELD_NUMBER)
    - #### ORIGIN\_ENERGY\_USAGE\_FIELD\_NUMBER

      ```
      public static final int ORIGIN_ENERGY_USAGE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.ResourceReceipt.ORIGIN_ENERGY_USAGE_FIELD_NUMBER)
    - #### ENERGY\_USAGE\_TOTAL\_FIELD\_NUMBER

      ```
      public static final int ENERGY_USAGE_TOTAL_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.ResourceReceipt.ENERGY_USAGE_TOTAL_FIELD_NUMBER)
    - #### NET\_USAGE\_FIELD\_NUMBER

      ```
      public static final int NET_USAGE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.ResourceReceipt.NET_USAGE_FIELD_NUMBER)
    - #### NET\_FEE\_FIELD\_NUMBER

      ```
      public static final int NET_FEE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.ResourceReceipt.NET_FEE_FIELD_NUMBER)
    - #### RESULT\_FIELD\_NUMBER

      ```
      public static final int RESULT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.ResourceReceipt.RESULT_FIELD_NUMBER)
    - #### ENERGY\_PENALTY\_TOTAL\_FIELD\_NUMBER

      ```
      public static final int ENERGY_PENALTY_TOTAL_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.ResourceReceipt.ENERGY_PENALTY_TOTAL_FIELD_NUMBER)
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
    - #### getEnergyUsage

      ```
      public long getEnergyUsage()
      ```

      `int64 energy_usage = 1;`

      Specified by:
      :   `getEnergyUsage` in interface `Response.ResourceReceiptOrBuilder`

      Returns:
      :   The energyUsage.
    - #### getEnergyFee

      ```
      public long getEnergyFee()
      ```

      `int64 energy_fee = 2;`

      Specified by:
      :   `getEnergyFee` in interface `Response.ResourceReceiptOrBuilder`

      Returns:
      :   The energyFee.
    - #### getOriginEnergyUsage

      ```
      public long getOriginEnergyUsage()
      ```

      `int64 origin_energy_usage = 3;`

      Specified by:
      :   `getOriginEnergyUsage` in interface `Response.ResourceReceiptOrBuilder`

      Returns:
      :   The originEnergyUsage.
    - #### getEnergyUsageTotal

      ```
      public long getEnergyUsageTotal()
      ```

      `int64 energy_usage_total = 4;`

      Specified by:
      :   `getEnergyUsageTotal` in interface `Response.ResourceReceiptOrBuilder`

      Returns:
      :   The energyUsageTotal.
    - #### getNetUsage

      ```
      public long getNetUsage()
      ```

      `int64 net_usage = 5;`

      Specified by:
      :   `getNetUsage` in interface `Response.ResourceReceiptOrBuilder`

      Returns:
      :   The netUsage.
    - #### getNetFee

      ```
      public long getNetFee()
      ```

      `int64 net_fee = 6;`

      Specified by:
      :   `getNetFee` in interface `Response.ResourceReceiptOrBuilder`

      Returns:
      :   The netFee.
    - #### getResultValue

      ```
      public int getResultValue()
      ```

      `.protocol.Transaction.Result.contractResult result = 7;`

      Specified by:
      :   `getResultValue` in interface `Response.ResourceReceiptOrBuilder`

      Returns:
      :   The enum numeric value on the wire for result.
    - #### getResult

      ```
      public Chain.Transaction.Result.contractResult getResult()
      ```

      `.protocol.Transaction.Result.contractResult result = 7;`

      Specified by:
      :   `getResult` in interface `Response.ResourceReceiptOrBuilder`

      Returns:
      :   The result.
    - #### getEnergyPenaltyTotal

      ```
      public long getEnergyPenaltyTotal()
      ```

      `int64 energy_penalty_total = 8;`

      Specified by:
      :   `getEnergyPenaltyTotal` in interface `Response.ResourceReceiptOrBuilder`

      Returns:
      :   The energyPenaltyTotal.
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
      public static Response.ResourceReceipt parseFrom(java.nio.ByteBuffer data)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.ResourceReceipt parseFrom(java.nio.ByteBuffer data,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.ResourceReceipt parseFrom(com.google.protobuf.ByteString data)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.ResourceReceipt parseFrom(com.google.protobuf.ByteString data,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.ResourceReceipt parseFrom(byte[] data)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.ResourceReceipt parseFrom(byte[] data,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.ResourceReceipt parseFrom(java.io.InputStream input)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.ResourceReceipt parseFrom(java.io.InputStream input,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.ResourceReceipt parseDelimitedFrom(java.io.InputStream input)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.ResourceReceipt parseDelimitedFrom(java.io.InputStream input,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.ResourceReceipt parseFrom(com.google.protobuf.CodedInputStream input)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.ResourceReceipt parseFrom(com.google.protobuf.CodedInputStream input,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.ResourceReceipt.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.ResourceReceipt.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.ResourceReceipt.Builder newBuilder(Response.ResourceReceipt prototype)
      ```
    - #### toBuilder

      ```
      public Response.ResourceReceipt.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.ResourceReceipt.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.ResourceReceipt getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.ResourceReceipt> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.ResourceReceipt> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.ResourceReceipt getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`