

org.tron.trident.proto

## Class Response.BlockBalanceTrace

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.BlockBalanceTrace

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.BlockBalanceTraceOrBuilder](../../../../org/tron/trident/proto/Response.BlockBalanceTraceOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.BlockBalanceTrace
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.BlockBalanceTraceOrBuilder
  ```

  Protobuf type `protocol.BlockBalanceTrace`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.BlockBalanceTrace)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.BlockBalanceTrace.Builder` Protobuf type `protocol.BlockBalanceTrace` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `BLOCK_IDENTIFIER_FIELD_NUMBER` |
    | `static int` | `TIMESTAMP_FIELD_NUMBER` |
    | `static int` | `TRANSACTION_BALANCE_TRACE_FIELD_NUMBER` |

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
    | `Response.BlockIdentifier` | `getBlockIdentifier()` `.protocol.BlockIdentifier block_identifier = 1;` |
    | `Response.BlockIdentifierOrBuilder` | `getBlockIdentifierOrBuilder()` `.protocol.BlockIdentifier block_identifier = 1;` |
    | `static Response.BlockBalanceTrace` | `getDefaultInstance()` |
    | `Response.BlockBalanceTrace` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Parser<Response.BlockBalanceTrace>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `long` | `getTimestamp()` `int64 timestamp = 2;` |
    | `Response.TransactionBalanceTrace` | `getTransactionBalanceTrace(int index)` BlockIdentifier parent\_block\_identifier = 4; |
    | `int` | `getTransactionBalanceTraceCount()` BlockIdentifier parent\_block\_identifier = 4; |
    | `java.util.List<Response.TransactionBalanceTrace>` | `getTransactionBalanceTraceList()` BlockIdentifier parent\_block\_identifier = 4; |
    | `Response.TransactionBalanceTraceOrBuilder` | `getTransactionBalanceTraceOrBuilder(int index)` BlockIdentifier parent\_block\_identifier = 4; |
    | `java.util.List<? extends Response.TransactionBalanceTraceOrBuilder>` | `getTransactionBalanceTraceOrBuilderList()` BlockIdentifier parent\_block\_identifier = 4; |
    | `boolean` | `hasBlockIdentifier()` `.protocol.BlockIdentifier block_identifier = 1;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Response.BlockBalanceTrace.Builder` | `newBuilder()` |
    | `static Response.BlockBalanceTrace.Builder` | `newBuilder(Response.BlockBalanceTrace prototype)` |
    | `Response.BlockBalanceTrace.Builder` | `newBuilderForType()` |
    | `protected Response.BlockBalanceTrace.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.BlockBalanceTrace` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.BlockBalanceTrace` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.BlockBalanceTrace` | `parseFrom(byte[] data)` |
    | `static Response.BlockBalanceTrace` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.BlockBalanceTrace` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.BlockBalanceTrace` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.BlockBalanceTrace` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.BlockBalanceTrace` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.BlockBalanceTrace` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.BlockBalanceTrace` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.BlockBalanceTrace` | `parseFrom(java.io.InputStream input)` |
    | `static Response.BlockBalanceTrace` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.BlockBalanceTrace>` | `parser()` |
    | `Response.BlockBalanceTrace.Builder` | `toBuilder()` |
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

    - #### BLOCK\_IDENTIFIER\_FIELD\_NUMBER

      ```
      public static final int BLOCK_IDENTIFIER_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.BlockBalanceTrace.BLOCK_IDENTIFIER_FIELD_NUMBER)
    - #### TIMESTAMP\_FIELD\_NUMBER

      ```
      public static final int TIMESTAMP_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.BlockBalanceTrace.TIMESTAMP_FIELD_NUMBER)
    - #### TRANSACTION\_BALANCE\_TRACE\_FIELD\_NUMBER

      ```
      public static final int TRANSACTION_BALANCE_TRACE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.BlockBalanceTrace.TRANSACTION_BALANCE_TRACE_FIELD_NUMBER)
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
    - #### hasBlockIdentifier

      ```
      public boolean hasBlockIdentifier()
      ```

      `.protocol.BlockIdentifier block_identifier = 1;`

      Specified by:
      :   `hasBlockIdentifier` in interface `Response.BlockBalanceTraceOrBuilder`

      Returns:
      :   Whether the blockIdentifier field is set.
    - #### getBlockIdentifier

      ```
      public Response.BlockIdentifier getBlockIdentifier()
      ```

      `.protocol.BlockIdentifier block_identifier = 1;`

      Specified by:
      :   `getBlockIdentifier` in interface `Response.BlockBalanceTraceOrBuilder`

      Returns:
      :   The blockIdentifier.
    - #### getBlockIdentifierOrBuilder

      ```
      public Response.BlockIdentifierOrBuilder getBlockIdentifierOrBuilder()
      ```

      `.protocol.BlockIdentifier block_identifier = 1;`

      Specified by:
      :   `getBlockIdentifierOrBuilder` in interface `Response.BlockBalanceTraceOrBuilder`
    - #### getTimestamp

      ```
      public long getTimestamp()
      ```

      `int64 timestamp = 2;`

      Specified by:
      :   `getTimestamp` in interface `Response.BlockBalanceTraceOrBuilder`

      Returns:
      :   The timestamp.
    - #### getTransactionBalanceTraceList

      ```
      public java.util.List<Response.TransactionBalanceTrace> getTransactionBalanceTraceList()
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`

      Specified by:
      :   `getTransactionBalanceTraceList` in interface `Response.BlockBalanceTraceOrBuilder`
    - #### getTransactionBalanceTraceOrBuilderList

      ```
      public java.util.List<? extends Response.TransactionBalanceTraceOrBuilder> getTransactionBalanceTraceOrBuilderList()
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`

      Specified by:
      :   `getTransactionBalanceTraceOrBuilderList` in interface `Response.BlockBalanceTraceOrBuilder`
    - #### getTransactionBalanceTraceCount

      ```
      public int getTransactionBalanceTraceCount()
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`

      Specified by:
      :   `getTransactionBalanceTraceCount` in interface `Response.BlockBalanceTraceOrBuilder`
    - #### getTransactionBalanceTrace

      ```
      public Response.TransactionBalanceTrace getTransactionBalanceTrace(int index)
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`

      Specified by:
      :   `getTransactionBalanceTrace` in interface `Response.BlockBalanceTraceOrBuilder`
    - #### getTransactionBalanceTraceOrBuilder

      ```
      public Response.TransactionBalanceTraceOrBuilder getTransactionBalanceTraceOrBuilder(int index)
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`

      Specified by:
      :   `getTransactionBalanceTraceOrBuilder` in interface `Response.BlockBalanceTraceOrBuilder`
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
      public static Response.BlockBalanceTrace parseFrom(java.nio.ByteBuffer data)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.BlockBalanceTrace parseFrom(java.nio.ByteBuffer data,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.BlockBalanceTrace parseFrom(com.google.protobuf.ByteString data)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.BlockBalanceTrace parseFrom(com.google.protobuf.ByteString data,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.BlockBalanceTrace parseFrom(byte[] data)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.BlockBalanceTrace parseFrom(byte[] data,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.BlockBalanceTrace parseFrom(java.io.InputStream input)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.BlockBalanceTrace parseFrom(java.io.InputStream input,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.BlockBalanceTrace parseDelimitedFrom(java.io.InputStream input)
                                                           throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.BlockBalanceTrace parseDelimitedFrom(java.io.InputStream input,
                                                                  com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                           throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.BlockBalanceTrace parseFrom(com.google.protobuf.CodedInputStream input)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.BlockBalanceTrace parseFrom(com.google.protobuf.CodedInputStream input,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.BlockBalanceTrace.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.BlockBalanceTrace.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.BlockBalanceTrace.Builder newBuilder(Response.BlockBalanceTrace prototype)
      ```
    - #### toBuilder

      ```
      public Response.BlockBalanceTrace.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.BlockBalanceTrace.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.BlockBalanceTrace getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.BlockBalanceTrace> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.BlockBalanceTrace> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.BlockBalanceTrace getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`