

org.tron.trident.proto

## Class Response.TransactionExtention

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.TransactionExtention

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.TransactionExtentionOrBuilder](../../../../org/tron/trident/proto/Response.TransactionExtentionOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.TransactionExtention
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.TransactionExtentionOrBuilder
  ```

  Protobuf type `protocol.TransactionExtention`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.TransactionExtention)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.TransactionExtention.Builder` Protobuf type `protocol.TransactionExtention` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `CONSTANT_RESULT_FIELD_NUMBER` |
    | `static int` | `ENERGY_PENALTY_FIELD_NUMBER` |
    | `static int` | `ENERGY_USED_FIELD_NUMBER` |
    | `static int` | `INTERNAL_TRANSACTIONS_FIELD_NUMBER` |
    | `static int` | `LOGS_FIELD_NUMBER` |
    | `static int` | `RESULT_FIELD_NUMBER` |
    | `static int` | `TRANSACTION_FIELD_NUMBER` |
    | `static int` | `TXID_FIELD_NUMBER` |

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
    | `com.google.protobuf.ByteString` | `getConstantResult(int index)` `repeated bytes constant_result = 3;` |
    | `int` | `getConstantResultCount()` `repeated bytes constant_result = 3;` |
    | `java.util.List<com.google.protobuf.ByteString>` | `getConstantResultList()` `repeated bytes constant_result = 3;` |
    | `static Response.TransactionExtention` | `getDefaultInstance()` |
    | `Response.TransactionExtention` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `long` | `getEnergyPenalty()` `int64 energy_penalty = 8;` |
    | `long` | `getEnergyUsed()` `int64 energy_used = 5;` |
    | `Response.InternalTransaction` | `getInternalTransactions(int index)` `repeated .protocol.InternalTransaction internal_transactions = 7;` |
    | `int` | `getInternalTransactionsCount()` `repeated .protocol.InternalTransaction internal_transactions = 7;` |
    | `java.util.List<Response.InternalTransaction>` | `getInternalTransactionsList()` `repeated .protocol.InternalTransaction internal_transactions = 7;` |
    | `Response.InternalTransactionOrBuilder` | `getInternalTransactionsOrBuilder(int index)` `repeated .protocol.InternalTransaction internal_transactions = 7;` |
    | `java.util.List<? extends Response.InternalTransactionOrBuilder>` | `getInternalTransactionsOrBuilderList()` `repeated .protocol.InternalTransaction internal_transactions = 7;` |
    | `Response.TransactionInfo.Log` | `getLogs(int index)` `repeated .protocol.TransactionInfo.Log logs = 6;` |
    | `int` | `getLogsCount()` `repeated .protocol.TransactionInfo.Log logs = 6;` |
    | `java.util.List<Response.TransactionInfo.Log>` | `getLogsList()` `repeated .protocol.TransactionInfo.Log logs = 6;` |
    | `Response.TransactionInfo.LogOrBuilder` | `getLogsOrBuilder(int index)` `repeated .protocol.TransactionInfo.Log logs = 6;` |
    | `java.util.List<? extends Response.TransactionInfo.LogOrBuilder>` | `getLogsOrBuilderList()` `repeated .protocol.TransactionInfo.Log logs = 6;` |
    | `com.google.protobuf.Parser<Response.TransactionExtention>` | `getParserForType()` |
    | `Response.TransactionReturn` | `getResult()` `.protocol.TransactionReturn result = 4;` |
    | `Response.TransactionReturnOrBuilder` | `getResultOrBuilder()` `.protocol.TransactionReturn result = 4;` |
    | `int` | `getSerializedSize()` |
    | `Chain.Transaction` | `getTransaction()` `.protocol.Transaction transaction = 1;` |
    | `Chain.TransactionOrBuilder` | `getTransactionOrBuilder()` `.protocol.Transaction transaction = 1;` |
    | `com.google.protobuf.ByteString` | `getTxid()` transaction id = sha256(transaction.raw\_data) |
    | `int` | `hashCode()` |
    | `boolean` | `hasResult()` `.protocol.TransactionReturn result = 4;` |
    | `boolean` | `hasTransaction()` `.protocol.Transaction transaction = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Response.TransactionExtention.Builder` | `newBuilder()` |
    | `static Response.TransactionExtention.Builder` | `newBuilder(Response.TransactionExtention prototype)` |
    | `Response.TransactionExtention.Builder` | `newBuilderForType()` |
    | `protected Response.TransactionExtention.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.TransactionExtention` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.TransactionExtention` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.TransactionExtention` | `parseFrom(byte[] data)` |
    | `static Response.TransactionExtention` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.TransactionExtention` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.TransactionExtention` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.TransactionExtention` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.TransactionExtention` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.TransactionExtention` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.TransactionExtention` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.TransactionExtention` | `parseFrom(java.io.InputStream input)` |
    | `static Response.TransactionExtention` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.TransactionExtention>` | `parser()` |
    | `Response.TransactionExtention.Builder` | `toBuilder()` |
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

    - #### TRANSACTION\_FIELD\_NUMBER

      ```
      public static final int TRANSACTION_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionExtention.TRANSACTION_FIELD_NUMBER)
    - #### TXID\_FIELD\_NUMBER

      ```
      public static final int TXID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionExtention.TXID_FIELD_NUMBER)
    - #### CONSTANT\_RESULT\_FIELD\_NUMBER

      ```
      public static final int CONSTANT_RESULT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionExtention.CONSTANT_RESULT_FIELD_NUMBER)
    - #### RESULT\_FIELD\_NUMBER

      ```
      public static final int RESULT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionExtention.RESULT_FIELD_NUMBER)
    - #### ENERGY\_USED\_FIELD\_NUMBER

      ```
      public static final int ENERGY_USED_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionExtention.ENERGY_USED_FIELD_NUMBER)
    - #### LOGS\_FIELD\_NUMBER

      ```
      public static final int LOGS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionExtention.LOGS_FIELD_NUMBER)
    - #### INTERNAL\_TRANSACTIONS\_FIELD\_NUMBER

      ```
      public static final int INTERNAL_TRANSACTIONS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionExtention.INTERNAL_TRANSACTIONS_FIELD_NUMBER)
    - #### ENERGY\_PENALTY\_FIELD\_NUMBER

      ```
      public static final int ENERGY_PENALTY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionExtention.ENERGY_PENALTY_FIELD_NUMBER)
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
    - #### hasTransaction

      ```
      public boolean hasTransaction()
      ```

      `.protocol.Transaction transaction = 1;`

      Specified by:
      :   `hasTransaction` in interface `Response.TransactionExtentionOrBuilder`

      Returns:
      :   Whether the transaction field is set.
    - #### getTransaction

      ```
      public Chain.Transaction getTransaction()
      ```

      `.protocol.Transaction transaction = 1;`

      Specified by:
      :   `getTransaction` in interface `Response.TransactionExtentionOrBuilder`

      Returns:
      :   The transaction.
    - #### getTransactionOrBuilder

      ```
      public Chain.TransactionOrBuilder getTransactionOrBuilder()
      ```

      `.protocol.Transaction transaction = 1;`

      Specified by:
      :   `getTransactionOrBuilder` in interface `Response.TransactionExtentionOrBuilder`
    - #### getTxid

      ```
      public com.google.protobuf.ByteString getTxid()
      ```

      ```
       transaction id = sha256(transaction.raw_data)
      ```

      `bytes txid = 2;`

      Specified by:
      :   `getTxid` in interface `Response.TransactionExtentionOrBuilder`

      Returns:
      :   The txid.
    - #### getConstantResultList

      ```
      public java.util.List<com.google.protobuf.ByteString> getConstantResultList()
      ```

      `repeated bytes constant_result = 3;`

      Specified by:
      :   `getConstantResultList` in interface `Response.TransactionExtentionOrBuilder`

      Returns:
      :   A list containing the constantResult.
    - #### getConstantResultCount

      ```
      public int getConstantResultCount()
      ```

      `repeated bytes constant_result = 3;`

      Specified by:
      :   `getConstantResultCount` in interface `Response.TransactionExtentionOrBuilder`

      Returns:
      :   The count of constantResult.
    - #### getConstantResult

      ```
      public com.google.protobuf.ByteString getConstantResult(int index)
      ```

      `repeated bytes constant_result = 3;`

      Specified by:
      :   `getConstantResult` in interface `Response.TransactionExtentionOrBuilder`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The constantResult at the given index.
    - #### hasResult

      ```
      public boolean hasResult()
      ```

      `.protocol.TransactionReturn result = 4;`

      Specified by:
      :   `hasResult` in interface `Response.TransactionExtentionOrBuilder`

      Returns:
      :   Whether the result field is set.
    - #### getResult

      ```
      public Response.TransactionReturn getResult()
      ```

      `.protocol.TransactionReturn result = 4;`

      Specified by:
      :   `getResult` in interface `Response.TransactionExtentionOrBuilder`

      Returns:
      :   The result.
    - #### getResultOrBuilder

      ```
      public Response.TransactionReturnOrBuilder getResultOrBuilder()
      ```

      `.protocol.TransactionReturn result = 4;`

      Specified by:
      :   `getResultOrBuilder` in interface `Response.TransactionExtentionOrBuilder`
    - #### getEnergyUsed

      ```
      public long getEnergyUsed()
      ```

      `int64 energy_used = 5;`

      Specified by:
      :   `getEnergyUsed` in interface `Response.TransactionExtentionOrBuilder`

      Returns:
      :   The energyUsed.
    - #### getLogsList

      ```
      public java.util.List<Response.TransactionInfo.Log> getLogsList()
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`

      Specified by:
      :   `getLogsList` in interface `Response.TransactionExtentionOrBuilder`
    - #### getLogsOrBuilderList

      ```
      public java.util.List<? extends Response.TransactionInfo.LogOrBuilder> getLogsOrBuilderList()
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`

      Specified by:
      :   `getLogsOrBuilderList` in interface `Response.TransactionExtentionOrBuilder`
    - #### getLogsCount

      ```
      public int getLogsCount()
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`

      Specified by:
      :   `getLogsCount` in interface `Response.TransactionExtentionOrBuilder`
    - #### getLogs

      ```
      public Response.TransactionInfo.Log getLogs(int index)
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`

      Specified by:
      :   `getLogs` in interface `Response.TransactionExtentionOrBuilder`
    - #### getLogsOrBuilder

      ```
      public Response.TransactionInfo.LogOrBuilder getLogsOrBuilder(int index)
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`

      Specified by:
      :   `getLogsOrBuilder` in interface `Response.TransactionExtentionOrBuilder`
    - #### getInternalTransactionsList

      ```
      public java.util.List<Response.InternalTransaction> getInternalTransactionsList()
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`

      Specified by:
      :   `getInternalTransactionsList` in interface `Response.TransactionExtentionOrBuilder`
    - #### getInternalTransactionsOrBuilderList

      ```
      public java.util.List<? extends Response.InternalTransactionOrBuilder> getInternalTransactionsOrBuilderList()
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`

      Specified by:
      :   `getInternalTransactionsOrBuilderList` in interface `Response.TransactionExtentionOrBuilder`
    - #### getInternalTransactionsCount

      ```
      public int getInternalTransactionsCount()
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`

      Specified by:
      :   `getInternalTransactionsCount` in interface `Response.TransactionExtentionOrBuilder`
    - #### getInternalTransactions

      ```
      public Response.InternalTransaction getInternalTransactions(int index)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`

      Specified by:
      :   `getInternalTransactions` in interface `Response.TransactionExtentionOrBuilder`
    - #### getInternalTransactionsOrBuilder

      ```
      public Response.InternalTransactionOrBuilder getInternalTransactionsOrBuilder(int index)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`

      Specified by:
      :   `getInternalTransactionsOrBuilder` in interface `Response.TransactionExtentionOrBuilder`
    - #### getEnergyPenalty

      ```
      public long getEnergyPenalty()
      ```

      `int64 energy_penalty = 8;`

      Specified by:
      :   `getEnergyPenalty` in interface `Response.TransactionExtentionOrBuilder`

      Returns:
      :   The energyPenalty.
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
      public static Response.TransactionExtention parseFrom(java.nio.ByteBuffer data)
                                                     throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionExtention parseFrom(java.nio.ByteBuffer data,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionExtention parseFrom(com.google.protobuf.ByteString data)
                                                     throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionExtention parseFrom(com.google.protobuf.ByteString data,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionExtention parseFrom(byte[] data)
                                                     throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionExtention parseFrom(byte[] data,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionExtention parseFrom(java.io.InputStream input)
                                                     throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.TransactionExtention parseFrom(java.io.InputStream input,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.TransactionExtention parseDelimitedFrom(java.io.InputStream input)
                                                              throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.TransactionExtention parseDelimitedFrom(java.io.InputStream input,
                                                                     com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                              throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.TransactionExtention parseFrom(com.google.protobuf.CodedInputStream input)
                                                     throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.TransactionExtention parseFrom(com.google.protobuf.CodedInputStream input,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.TransactionExtention.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.TransactionExtention.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.TransactionExtention.Builder newBuilder(Response.TransactionExtention prototype)
      ```
    - #### toBuilder

      ```
      public Response.TransactionExtention.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.TransactionExtention.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.TransactionExtention getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.TransactionExtention> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.TransactionExtention> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.TransactionExtention getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`