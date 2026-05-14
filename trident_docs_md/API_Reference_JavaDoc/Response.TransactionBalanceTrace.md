

org.tron.trident.proto

## Class Response.TransactionBalanceTrace

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.TransactionBalanceTrace

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.TransactionBalanceTraceOrBuilder](../../../../org/tron/trident/proto/Response.TransactionBalanceTraceOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.TransactionBalanceTrace
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.TransactionBalanceTraceOrBuilder
  ```

  Protobuf type `protocol.TransactionBalanceTrace`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.TransactionBalanceTrace)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.TransactionBalanceTrace.Builder` Protobuf type `protocol.TransactionBalanceTrace` |
    | `static class` | `Response.TransactionBalanceTrace.Operation` Protobuf type `protocol.TransactionBalanceTrace.Operation` |
    | `static interface` | `Response.TransactionBalanceTrace.OperationOrBuilder` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `OPERATION_FIELD_NUMBER` |
    | `static int` | `STATUS_FIELD_NUMBER` |
    | `static int` | `TRANSACTION_IDENTIFIER_FIELD_NUMBER` |
    | `static int` | `TYPE_FIELD_NUMBER` |

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
    | `static Response.TransactionBalanceTrace` | `getDefaultInstance()` |
    | `Response.TransactionBalanceTrace` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `Response.TransactionBalanceTrace.Operation` | `getOperation(int index)` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `int` | `getOperationCount()` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `java.util.List<Response.TransactionBalanceTrace.Operation>` | `getOperationList()` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `Response.TransactionBalanceTrace.OperationOrBuilder` | `getOperationOrBuilder(int index)` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `java.util.List<? extends Response.TransactionBalanceTrace.OperationOrBuilder>` | `getOperationOrBuilderList()` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `com.google.protobuf.Parser<Response.TransactionBalanceTrace>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `java.lang.String` | `getStatus()` `string status = 4;` |
    | `com.google.protobuf.ByteString` | `getStatusBytes()` `string status = 4;` |
    | `com.google.protobuf.ByteString` | `getTransactionIdentifier()` `bytes transaction_identifier = 1;` |
    | `java.lang.String` | `getType()` `string type = 3;` |
    | `com.google.protobuf.ByteString` | `getTypeBytes()` `string type = 3;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Response.TransactionBalanceTrace.Builder` | `newBuilder()` |
    | `static Response.TransactionBalanceTrace.Builder` | `newBuilder(Response.TransactionBalanceTrace prototype)` |
    | `Response.TransactionBalanceTrace.Builder` | `newBuilderForType()` |
    | `protected Response.TransactionBalanceTrace.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.TransactionBalanceTrace` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.TransactionBalanceTrace` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.TransactionBalanceTrace` | `parseFrom(byte[] data)` |
    | `static Response.TransactionBalanceTrace` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.TransactionBalanceTrace` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.TransactionBalanceTrace` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.TransactionBalanceTrace` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.TransactionBalanceTrace` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.TransactionBalanceTrace` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.TransactionBalanceTrace` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.TransactionBalanceTrace` | `parseFrom(java.io.InputStream input)` |
    | `static Response.TransactionBalanceTrace` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.TransactionBalanceTrace>` | `parser()` |
    | `Response.TransactionBalanceTrace.Builder` | `toBuilder()` |
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

    - #### TRANSACTION\_IDENTIFIER\_FIELD\_NUMBER

      ```
      public static final int TRANSACTION_IDENTIFIER_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionBalanceTrace.TRANSACTION_IDENTIFIER_FIELD_NUMBER)
    - #### OPERATION\_FIELD\_NUMBER

      ```
      public static final int OPERATION_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionBalanceTrace.OPERATION_FIELD_NUMBER)
    - #### TYPE\_FIELD\_NUMBER

      ```
      public static final int TYPE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionBalanceTrace.TYPE_FIELD_NUMBER)
    - #### STATUS\_FIELD\_NUMBER

      ```
      public static final int STATUS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionBalanceTrace.STATUS_FIELD_NUMBER)
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
    - #### getTransactionIdentifier

      ```
      public com.google.protobuf.ByteString getTransactionIdentifier()
      ```

      `bytes transaction_identifier = 1;`

      Specified by:
      :   `getTransactionIdentifier` in interface `Response.TransactionBalanceTraceOrBuilder`

      Returns:
      :   The transactionIdentifier.
    - #### getOperationList

      ```
      public java.util.List<Response.TransactionBalanceTrace.Operation> getOperationList()
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`

      Specified by:
      :   `getOperationList` in interface `Response.TransactionBalanceTraceOrBuilder`
    - #### getOperationOrBuilderList

      ```
      public java.util.List<? extends Response.TransactionBalanceTrace.OperationOrBuilder> getOperationOrBuilderList()
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`

      Specified by:
      :   `getOperationOrBuilderList` in interface `Response.TransactionBalanceTraceOrBuilder`
    - #### getOperationCount

      ```
      public int getOperationCount()
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`

      Specified by:
      :   `getOperationCount` in interface `Response.TransactionBalanceTraceOrBuilder`
    - #### getOperation

      ```
      public Response.TransactionBalanceTrace.Operation getOperation(int index)
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`

      Specified by:
      :   `getOperation` in interface `Response.TransactionBalanceTraceOrBuilder`
    - #### getOperationOrBuilder

      ```
      public Response.TransactionBalanceTrace.OperationOrBuilder getOperationOrBuilder(int index)
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`

      Specified by:
      :   `getOperationOrBuilder` in interface `Response.TransactionBalanceTraceOrBuilder`
    - #### getType

      ```
      public java.lang.String getType()
      ```

      `string type = 3;`

      Specified by:
      :   `getType` in interface `Response.TransactionBalanceTraceOrBuilder`

      Returns:
      :   The type.
    - #### getTypeBytes

      ```
      public com.google.protobuf.ByteString getTypeBytes()
      ```

      `string type = 3;`

      Specified by:
      :   `getTypeBytes` in interface `Response.TransactionBalanceTraceOrBuilder`

      Returns:
      :   The bytes for type.
    - #### getStatus

      ```
      public java.lang.String getStatus()
      ```

      `string status = 4;`

      Specified by:
      :   `getStatus` in interface `Response.TransactionBalanceTraceOrBuilder`

      Returns:
      :   The status.
    - #### getStatusBytes

      ```
      public com.google.protobuf.ByteString getStatusBytes()
      ```

      `string status = 4;`

      Specified by:
      :   `getStatusBytes` in interface `Response.TransactionBalanceTraceOrBuilder`

      Returns:
      :   The bytes for status.
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
      public static Response.TransactionBalanceTrace parseFrom(java.nio.ByteBuffer data)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionBalanceTrace parseFrom(java.nio.ByteBuffer data,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionBalanceTrace parseFrom(com.google.protobuf.ByteString data)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionBalanceTrace parseFrom(com.google.protobuf.ByteString data,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionBalanceTrace parseFrom(byte[] data)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionBalanceTrace parseFrom(byte[] data,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionBalanceTrace parseFrom(java.io.InputStream input)
                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.TransactionBalanceTrace parseFrom(java.io.InputStream input,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.TransactionBalanceTrace parseDelimitedFrom(java.io.InputStream input)
                                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.TransactionBalanceTrace parseDelimitedFrom(java.io.InputStream input,
                                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.TransactionBalanceTrace parseFrom(com.google.protobuf.CodedInputStream input)
                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.TransactionBalanceTrace parseFrom(com.google.protobuf.CodedInputStream input,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.TransactionBalanceTrace.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.TransactionBalanceTrace.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.TransactionBalanceTrace.Builder newBuilder(Response.TransactionBalanceTrace prototype)
      ```
    - #### toBuilder

      ```
      public Response.TransactionBalanceTrace.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.TransactionBalanceTrace.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.TransactionBalanceTrace getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.TransactionBalanceTrace> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.TransactionBalanceTrace> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.TransactionBalanceTrace getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`