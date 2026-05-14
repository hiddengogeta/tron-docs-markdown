

org.tron.trident.proto

## Class Response.TransactionExtention.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.TransactionExtention.Builder](../../../../org/tron/trident/proto/Response.TransactionExtention.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.TransactionExtention.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.TransactionExtentionOrBuilder](../../../../org/tron/trident/proto/Response.TransactionExtentionOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.TransactionExtention](../../../../org/tron/trident/proto/Response.TransactionExtention.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.TransactionExtention.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionExtention.Builder>
  implements Response.TransactionExtentionOrBuilder
  ```

  Protobuf type `protocol.TransactionExtention`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.TransactionExtention.Builder` | `addAllConstantResult(java.lang.Iterable<? extends com.google.protobuf.ByteString> values)` `repeated bytes constant_result = 3;` |
    | `Response.TransactionExtention.Builder` | `addAllInternalTransactions(java.lang.Iterable<? extends Response.InternalTransaction> values)` `repeated .protocol.InternalTransaction internal_transactions = 7;` |
    | `Response.TransactionExtention.Builder` | `addAllLogs(java.lang.Iterable<? extends Response.TransactionInfo.Log> values)` `repeated .protocol.TransactionInfo.Log logs = 6;` |
    | `Response.TransactionExtention.Builder` | `addConstantResult(com.google.protobuf.ByteString value)` `repeated bytes constant_result = 3;` |
    | `Response.TransactionExtention.Builder` | `addInternalTransactions(int index, Response.InternalTransaction.Builder builderForValue)` `repeated .protocol.InternalTransaction internal_transactions = 7;` |
    | `Response.TransactionExtention.Builder` | `addInternalTransactions(int index, Response.InternalTransaction value)` `repeated .protocol.InternalTransaction internal_transactions = 7;` |
    | `Response.TransactionExtention.Builder` | `addInternalTransactions(Response.InternalTransaction.Builder builderForValue)` `repeated .protocol.InternalTransaction internal_transactions = 7;` |
    | `Response.TransactionExtention.Builder` | `addInternalTransactions(Response.InternalTransaction value)` `repeated .protocol.InternalTransaction internal_transactions = 7;` |
    | `Response.InternalTransaction.Builder` | `addInternalTransactionsBuilder()` `repeated .protocol.InternalTransaction internal_transactions = 7;` |
    | `Response.InternalTransaction.Builder` | `addInternalTransactionsBuilder(int index)` `repeated .protocol.InternalTransaction internal_transactions = 7;` |
    | `Response.TransactionExtention.Builder` | `addLogs(int index, Response.TransactionInfo.Log.Builder builderForValue)` `repeated .protocol.TransactionInfo.Log logs = 6;` |
    | `Response.TransactionExtention.Builder` | `addLogs(int index, Response.TransactionInfo.Log value)` `repeated .protocol.TransactionInfo.Log logs = 6;` |
    | `Response.TransactionExtention.Builder` | `addLogs(Response.TransactionInfo.Log.Builder builderForValue)` `repeated .protocol.TransactionInfo.Log logs = 6;` |
    | `Response.TransactionExtention.Builder` | `addLogs(Response.TransactionInfo.Log value)` `repeated .protocol.TransactionInfo.Log logs = 6;` |
    | `Response.TransactionInfo.Log.Builder` | `addLogsBuilder()` `repeated .protocol.TransactionInfo.Log logs = 6;` |
    | `Response.TransactionInfo.Log.Builder` | `addLogsBuilder(int index)` `repeated .protocol.TransactionInfo.Log logs = 6;` |
    | `Response.TransactionExtention.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionExtention` | `build()` |
    | `Response.TransactionExtention` | `buildPartial()` |
    | `Response.TransactionExtention.Builder` | `clear()` |
    | `Response.TransactionExtention.Builder` | `clearConstantResult()` `repeated bytes constant_result = 3;` |
    | `Response.TransactionExtention.Builder` | `clearEnergyPenalty()` `int64 energy_penalty = 8;` |
    | `Response.TransactionExtention.Builder` | `clearEnergyUsed()` `int64 energy_used = 5;` |
    | `Response.TransactionExtention.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.TransactionExtention.Builder` | `clearInternalTransactions()` `repeated .protocol.InternalTransaction internal_transactions = 7;` |
    | `Response.TransactionExtention.Builder` | `clearLogs()` `repeated .protocol.TransactionInfo.Log logs = 6;` |
    | `Response.TransactionExtention.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.TransactionExtention.Builder` | `clearResult()` `.protocol.TransactionReturn result = 4;` |
    | `Response.TransactionExtention.Builder` | `clearTransaction()` `.protocol.Transaction transaction = 1;` |
    | `Response.TransactionExtention.Builder` | `clearTxid()` transaction id = sha256(transaction.raw\_data) |
    | `Response.TransactionExtention.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getConstantResult(int index)` `repeated bytes constant_result = 3;` |
    | `int` | `getConstantResultCount()` `repeated bytes constant_result = 3;` |
    | `java.util.List<com.google.protobuf.ByteString>` | `getConstantResultList()` `repeated bytes constant_result = 3;` |
    | `Response.TransactionExtention` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getEnergyPenalty()` `int64 energy_penalty = 8;` |
    | `long` | `getEnergyUsed()` `int64 energy_used = 5;` |
    | `Response.InternalTransaction` | `getInternalTransactions(int index)` `repeated .protocol.InternalTransaction internal_transactions = 7;` |
    | `Response.InternalTransaction.Builder` | `getInternalTransactionsBuilder(int index)` `repeated .protocol.InternalTransaction internal_transactions = 7;` |
    | `java.util.List<Response.InternalTransaction.Builder>` | `getInternalTransactionsBuilderList()` `repeated .protocol.InternalTransaction internal_transactions = 7;` |
    | `int` | `getInternalTransactionsCount()` `repeated .protocol.InternalTransaction internal_transactions = 7;` |
    | `java.util.List<Response.InternalTransaction>` | `getInternalTransactionsList()` `repeated .protocol.InternalTransaction internal_transactions = 7;` |
    | `Response.InternalTransactionOrBuilder` | `getInternalTransactionsOrBuilder(int index)` `repeated .protocol.InternalTransaction internal_transactions = 7;` |
    | `java.util.List<? extends Response.InternalTransactionOrBuilder>` | `getInternalTransactionsOrBuilderList()` `repeated .protocol.InternalTransaction internal_transactions = 7;` |
    | `Response.TransactionInfo.Log` | `getLogs(int index)` `repeated .protocol.TransactionInfo.Log logs = 6;` |
    | `Response.TransactionInfo.Log.Builder` | `getLogsBuilder(int index)` `repeated .protocol.TransactionInfo.Log logs = 6;` |
    | `java.util.List<Response.TransactionInfo.Log.Builder>` | `getLogsBuilderList()` `repeated .protocol.TransactionInfo.Log logs = 6;` |
    | `int` | `getLogsCount()` `repeated .protocol.TransactionInfo.Log logs = 6;` |
    | `java.util.List<Response.TransactionInfo.Log>` | `getLogsList()` `repeated .protocol.TransactionInfo.Log logs = 6;` |
    | `Response.TransactionInfo.LogOrBuilder` | `getLogsOrBuilder(int index)` `repeated .protocol.TransactionInfo.Log logs = 6;` |
    | `java.util.List<? extends Response.TransactionInfo.LogOrBuilder>` | `getLogsOrBuilderList()` `repeated .protocol.TransactionInfo.Log logs = 6;` |
    | `Response.TransactionReturn` | `getResult()` `.protocol.TransactionReturn result = 4;` |
    | `Response.TransactionReturn.Builder` | `getResultBuilder()` `.protocol.TransactionReturn result = 4;` |
    | `Response.TransactionReturnOrBuilder` | `getResultOrBuilder()` `.protocol.TransactionReturn result = 4;` |
    | `Chain.Transaction` | `getTransaction()` `.protocol.Transaction transaction = 1;` |
    | `Chain.Transaction.Builder` | `getTransactionBuilder()` `.protocol.Transaction transaction = 1;` |
    | `Chain.TransactionOrBuilder` | `getTransactionOrBuilder()` `.protocol.Transaction transaction = 1;` |
    | `com.google.protobuf.ByteString` | `getTxid()` transaction id = sha256(transaction.raw\_data) |
    | `boolean` | `hasResult()` `.protocol.TransactionReturn result = 4;` |
    | `boolean` | `hasTransaction()` `.protocol.Transaction transaction = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.TransactionExtention.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.TransactionExtention.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.TransactionExtention.Builder` | `mergeFrom(Response.TransactionExtention other)` |
    | `Response.TransactionExtention.Builder` | `mergeResult(Response.TransactionReturn value)` `.protocol.TransactionReturn result = 4;` |
    | `Response.TransactionExtention.Builder` | `mergeTransaction(Chain.Transaction value)` `.protocol.Transaction transaction = 1;` |
    | `Response.TransactionExtention.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.TransactionExtention.Builder` | `removeInternalTransactions(int index)` `repeated .protocol.InternalTransaction internal_transactions = 7;` |
    | `Response.TransactionExtention.Builder` | `removeLogs(int index)` `repeated .protocol.TransactionInfo.Log logs = 6;` |
    | `Response.TransactionExtention.Builder` | `setConstantResult(int index, com.google.protobuf.ByteString value)` `repeated bytes constant_result = 3;` |
    | `Response.TransactionExtention.Builder` | `setEnergyPenalty(long value)` `int64 energy_penalty = 8;` |
    | `Response.TransactionExtention.Builder` | `setEnergyUsed(long value)` `int64 energy_used = 5;` |
    | `Response.TransactionExtention.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionExtention.Builder` | `setInternalTransactions(int index, Response.InternalTransaction.Builder builderForValue)` `repeated .protocol.InternalTransaction internal_transactions = 7;` |
    | `Response.TransactionExtention.Builder` | `setInternalTransactions(int index, Response.InternalTransaction value)` `repeated .protocol.InternalTransaction internal_transactions = 7;` |
    | `Response.TransactionExtention.Builder` | `setLogs(int index, Response.TransactionInfo.Log.Builder builderForValue)` `repeated .protocol.TransactionInfo.Log logs = 6;` |
    | `Response.TransactionExtention.Builder` | `setLogs(int index, Response.TransactionInfo.Log value)` `repeated .protocol.TransactionInfo.Log logs = 6;` |
    | `Response.TransactionExtention.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.TransactionExtention.Builder` | `setResult(Response.TransactionReturn.Builder builderForValue)` `.protocol.TransactionReturn result = 4;` |
    | `Response.TransactionExtention.Builder` | `setResult(Response.TransactionReturn value)` `.protocol.TransactionReturn result = 4;` |
    | `Response.TransactionExtention.Builder` | `setTransaction(Chain.Transaction.Builder builderForValue)` `.protocol.Transaction transaction = 1;` |
    | `Response.TransactionExtention.Builder` | `setTransaction(Chain.Transaction value)` `.protocol.Transaction transaction = 1;` |
    | `Response.TransactionExtention.Builder` | `setTxid(com.google.protobuf.ByteString value)` transaction id = sha256(transaction.raw\_data) |
    | `Response.TransactionExtention.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionExtention.Builder>`
    - #### clear

      ```
      public Response.TransactionExtention.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionExtention.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionExtention.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.TransactionExtention getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.TransactionExtention build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.TransactionExtention buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.TransactionExtention.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionExtention.Builder>`
    - #### setField

      ```
      public Response.TransactionExtention.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                            java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionExtention.Builder>`
    - #### clearField

      ```
      public Response.TransactionExtention.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionExtention.Builder>`
    - #### clearOneof

      ```
      public Response.TransactionExtention.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionExtention.Builder>`
    - #### setRepeatedField

      ```
      public Response.TransactionExtention.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                    int index,
                                                                    java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionExtention.Builder>`
    - #### addRepeatedField

      ```
      public Response.TransactionExtention.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                    java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionExtention.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionExtention.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionExtention.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionExtention.Builder mergeFrom(Response.TransactionExtention other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionExtention.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionExtention.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                             com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                      throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionExtention.Builder>`

      Throws:
      :   `java.io.IOException`
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
    - #### setTransaction

      ```
      public Response.TransactionExtention.Builder setTransaction(Chain.Transaction value)
      ```

      `.protocol.Transaction transaction = 1;`
    - #### setTransaction

      ```
      public Response.TransactionExtention.Builder setTransaction(Chain.Transaction.Builder builderForValue)
      ```

      `.protocol.Transaction transaction = 1;`
    - #### mergeTransaction

      ```
      public Response.TransactionExtention.Builder mergeTransaction(Chain.Transaction value)
      ```

      `.protocol.Transaction transaction = 1;`
    - #### clearTransaction

      ```
      public Response.TransactionExtention.Builder clearTransaction()
      ```

      `.protocol.Transaction transaction = 1;`
    - #### getTransactionBuilder

      ```
      public Chain.Transaction.Builder getTransactionBuilder()
      ```

      `.protocol.Transaction transaction = 1;`
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
    - #### setTxid

      ```
      public Response.TransactionExtention.Builder setTxid(com.google.protobuf.ByteString value)
      ```

      ```
       transaction id = sha256(transaction.raw_data)
      ```

      `bytes txid = 2;`

      Parameters:
      :   `value` - The txid to set.

      Returns:
      :   This builder for chaining.
    - #### clearTxid

      ```
      public Response.TransactionExtention.Builder clearTxid()
      ```

      ```
       transaction id = sha256(transaction.raw_data)
      ```

      `bytes txid = 2;`

      Returns:
      :   This builder for chaining.
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
    - #### setConstantResult

      ```
      public Response.TransactionExtention.Builder setConstantResult(int index,
                                                                     com.google.protobuf.ByteString value)
      ```

      `repeated bytes constant_result = 3;`

      Parameters:
      :   `index` - The index to set the value at.
      :   `value` - The constantResult to set.

      Returns:
      :   This builder for chaining.
    - #### addConstantResult

      ```
      public Response.TransactionExtention.Builder addConstantResult(com.google.protobuf.ByteString value)
      ```

      `repeated bytes constant_result = 3;`

      Parameters:
      :   `value` - The constantResult to add.

      Returns:
      :   This builder for chaining.
    - #### addAllConstantResult

      ```
      public Response.TransactionExtention.Builder addAllConstantResult(java.lang.Iterable<? extends com.google.protobuf.ByteString> values)
      ```

      `repeated bytes constant_result = 3;`

      Parameters:
      :   `values` - The constantResult to add.

      Returns:
      :   This builder for chaining.
    - #### clearConstantResult

      ```
      public Response.TransactionExtention.Builder clearConstantResult()
      ```

      `repeated bytes constant_result = 3;`

      Returns:
      :   This builder for chaining.
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
    - #### setResult

      ```
      public Response.TransactionExtention.Builder setResult(Response.TransactionReturn value)
      ```

      `.protocol.TransactionReturn result = 4;`
    - #### setResult

      ```
      public Response.TransactionExtention.Builder setResult(Response.TransactionReturn.Builder builderForValue)
      ```

      `.protocol.TransactionReturn result = 4;`
    - #### mergeResult

      ```
      public Response.TransactionExtention.Builder mergeResult(Response.TransactionReturn value)
      ```

      `.protocol.TransactionReturn result = 4;`
    - #### clearResult

      ```
      public Response.TransactionExtention.Builder clearResult()
      ```

      `.protocol.TransactionReturn result = 4;`
    - #### getResultBuilder

      ```
      public Response.TransactionReturn.Builder getResultBuilder()
      ```

      `.protocol.TransactionReturn result = 4;`
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
    - #### setEnergyUsed

      ```
      public Response.TransactionExtention.Builder setEnergyUsed(long value)
      ```

      `int64 energy_used = 5;`

      Parameters:
      :   `value` - The energyUsed to set.

      Returns:
      :   This builder for chaining.
    - #### clearEnergyUsed

      ```
      public Response.TransactionExtention.Builder clearEnergyUsed()
      ```

      `int64 energy_used = 5;`

      Returns:
      :   This builder for chaining.
    - #### getLogsList

      ```
      public java.util.List<Response.TransactionInfo.Log> getLogsList()
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`

      Specified by:
      :   `getLogsList` in interface `Response.TransactionExtentionOrBuilder`
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
    - #### setLogs

      ```
      public Response.TransactionExtention.Builder setLogs(int index,
                                                           Response.TransactionInfo.Log value)
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`
    - #### setLogs

      ```
      public Response.TransactionExtention.Builder setLogs(int index,
                                                           Response.TransactionInfo.Log.Builder builderForValue)
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`
    - #### addLogs

      ```
      public Response.TransactionExtention.Builder addLogs(Response.TransactionInfo.Log value)
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`
    - #### addLogs

      ```
      public Response.TransactionExtention.Builder addLogs(int index,
                                                           Response.TransactionInfo.Log value)
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`
    - #### addLogs

      ```
      public Response.TransactionExtention.Builder addLogs(Response.TransactionInfo.Log.Builder builderForValue)
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`
    - #### addLogs

      ```
      public Response.TransactionExtention.Builder addLogs(int index,
                                                           Response.TransactionInfo.Log.Builder builderForValue)
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`
    - #### addAllLogs

      ```
      public Response.TransactionExtention.Builder addAllLogs(java.lang.Iterable<? extends Response.TransactionInfo.Log> values)
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`
    - #### clearLogs

      ```
      public Response.TransactionExtention.Builder clearLogs()
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`
    - #### removeLogs

      ```
      public Response.TransactionExtention.Builder removeLogs(int index)
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`
    - #### getLogsBuilder

      ```
      public Response.TransactionInfo.Log.Builder getLogsBuilder(int index)
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`
    - #### getLogsOrBuilder

      ```
      public Response.TransactionInfo.LogOrBuilder getLogsOrBuilder(int index)
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`

      Specified by:
      :   `getLogsOrBuilder` in interface `Response.TransactionExtentionOrBuilder`
    - #### getLogsOrBuilderList

      ```
      public java.util.List<? extends Response.TransactionInfo.LogOrBuilder> getLogsOrBuilderList()
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`

      Specified by:
      :   `getLogsOrBuilderList` in interface `Response.TransactionExtentionOrBuilder`
    - #### addLogsBuilder

      ```
      public Response.TransactionInfo.Log.Builder addLogsBuilder()
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`
    - #### addLogsBuilder

      ```
      public Response.TransactionInfo.Log.Builder addLogsBuilder(int index)
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`
    - #### getLogsBuilderList

      ```
      public java.util.List<Response.TransactionInfo.Log.Builder> getLogsBuilderList()
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`
    - #### getInternalTransactionsList

      ```
      public java.util.List<Response.InternalTransaction> getInternalTransactionsList()
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`

      Specified by:
      :   `getInternalTransactionsList` in interface `Response.TransactionExtentionOrBuilder`
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
    - #### setInternalTransactions

      ```
      public Response.TransactionExtention.Builder setInternalTransactions(int index,
                                                                           Response.InternalTransaction value)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`
    - #### setInternalTransactions

      ```
      public Response.TransactionExtention.Builder setInternalTransactions(int index,
                                                                           Response.InternalTransaction.Builder builderForValue)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`
    - #### addInternalTransactions

      ```
      public Response.TransactionExtention.Builder addInternalTransactions(Response.InternalTransaction value)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`
    - #### addInternalTransactions

      ```
      public Response.TransactionExtention.Builder addInternalTransactions(int index,
                                                                           Response.InternalTransaction value)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`
    - #### addInternalTransactions

      ```
      public Response.TransactionExtention.Builder addInternalTransactions(Response.InternalTransaction.Builder builderForValue)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`
    - #### addInternalTransactions

      ```
      public Response.TransactionExtention.Builder addInternalTransactions(int index,
                                                                           Response.InternalTransaction.Builder builderForValue)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`
    - #### addAllInternalTransactions

      ```
      public Response.TransactionExtention.Builder addAllInternalTransactions(java.lang.Iterable<? extends Response.InternalTransaction> values)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`
    - #### clearInternalTransactions

      ```
      public Response.TransactionExtention.Builder clearInternalTransactions()
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`
    - #### removeInternalTransactions

      ```
      public Response.TransactionExtention.Builder removeInternalTransactions(int index)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`
    - #### getInternalTransactionsBuilder

      ```
      public Response.InternalTransaction.Builder getInternalTransactionsBuilder(int index)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`
    - #### getInternalTransactionsOrBuilder

      ```
      public Response.InternalTransactionOrBuilder getInternalTransactionsOrBuilder(int index)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`

      Specified by:
      :   `getInternalTransactionsOrBuilder` in interface `Response.TransactionExtentionOrBuilder`
    - #### getInternalTransactionsOrBuilderList

      ```
      public java.util.List<? extends Response.InternalTransactionOrBuilder> getInternalTransactionsOrBuilderList()
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`

      Specified by:
      :   `getInternalTransactionsOrBuilderList` in interface `Response.TransactionExtentionOrBuilder`
    - #### addInternalTransactionsBuilder

      ```
      public Response.InternalTransaction.Builder addInternalTransactionsBuilder()
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`
    - #### addInternalTransactionsBuilder

      ```
      public Response.InternalTransaction.Builder addInternalTransactionsBuilder(int index)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`
    - #### getInternalTransactionsBuilderList

      ```
      public java.util.List<Response.InternalTransaction.Builder> getInternalTransactionsBuilderList()
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`
    - #### getEnergyPenalty

      ```
      public long getEnergyPenalty()
      ```

      `int64 energy_penalty = 8;`

      Specified by:
      :   `getEnergyPenalty` in interface `Response.TransactionExtentionOrBuilder`

      Returns:
      :   The energyPenalty.
    - #### setEnergyPenalty

      ```
      public Response.TransactionExtention.Builder setEnergyPenalty(long value)
      ```

      `int64 energy_penalty = 8;`

      Parameters:
      :   `value` - The energyPenalty to set.

      Returns:
      :   This builder for chaining.
    - #### clearEnergyPenalty

      ```
      public Response.TransactionExtention.Builder clearEnergyPenalty()
      ```

      `int64 energy_penalty = 8;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.TransactionExtention.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionExtention.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.TransactionExtention.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionExtention.Builder>`