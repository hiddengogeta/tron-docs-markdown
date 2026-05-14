

org.tron.trident.proto

## Interface Response.TransactionExtentionOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.TransactionExtention](../../../../org/tron/trident/proto/Response.TransactionExtention.html "class in org.tron.trident.proto"), [Response.TransactionExtention.Builder](../../../../org/tron/trident/proto/Response.TransactionExtention.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.TransactionExtentionOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getConstantResult(int index)` `repeated bytes constant_result = 3;` |
    | `int` | `getConstantResultCount()` `repeated bytes constant_result = 3;` |
    | `java.util.List<com.google.protobuf.ByteString>` | `getConstantResultList()` `repeated bytes constant_result = 3;` |
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
    | `Response.TransactionReturn` | `getResult()` `.protocol.TransactionReturn result = 4;` |
    | `Response.TransactionReturnOrBuilder` | `getResultOrBuilder()` `.protocol.TransactionReturn result = 4;` |
    | `Chain.Transaction` | `getTransaction()` `.protocol.Transaction transaction = 1;` |
    | `Chain.TransactionOrBuilder` | `getTransactionOrBuilder()` `.protocol.Transaction transaction = 1;` |
    | `com.google.protobuf.ByteString` | `getTxid()` transaction id = sha256(transaction.raw\_data) |
    | `boolean` | `hasResult()` `.protocol.TransactionReturn result = 4;` |
    | `boolean` | `hasTransaction()` `.protocol.Transaction transaction = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### hasTransaction

      ```
      boolean hasTransaction()
      ```

      `.protocol.Transaction transaction = 1;`

      Returns:
      :   Whether the transaction field is set.
    - #### getTransaction

      ```
      Chain.Transaction getTransaction()
      ```

      `.protocol.Transaction transaction = 1;`

      Returns:
      :   The transaction.
    - #### getTransactionOrBuilder

      ```
      Chain.TransactionOrBuilder getTransactionOrBuilder()
      ```

      `.protocol.Transaction transaction = 1;`
    - #### getTxid

      ```
      com.google.protobuf.ByteString getTxid()
      ```

      ```
       transaction id = sha256(transaction.raw_data)
      ```

      `bytes txid = 2;`

      Returns:
      :   The txid.
    - #### getConstantResultList

      ```
      java.util.List<com.google.protobuf.ByteString> getConstantResultList()
      ```

      `repeated bytes constant_result = 3;`

      Returns:
      :   A list containing the constantResult.
    - #### getConstantResultCount

      ```
      int getConstantResultCount()
      ```

      `repeated bytes constant_result = 3;`

      Returns:
      :   The count of constantResult.
    - #### getConstantResult

      ```
      com.google.protobuf.ByteString getConstantResult(int index)
      ```

      `repeated bytes constant_result = 3;`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The constantResult at the given index.
    - #### hasResult

      ```
      boolean hasResult()
      ```

      `.protocol.TransactionReturn result = 4;`

      Returns:
      :   Whether the result field is set.
    - #### getResult

      ```
      Response.TransactionReturn getResult()
      ```

      `.protocol.TransactionReturn result = 4;`

      Returns:
      :   The result.
    - #### getResultOrBuilder

      ```
      Response.TransactionReturnOrBuilder getResultOrBuilder()
      ```

      `.protocol.TransactionReturn result = 4;`
    - #### getEnergyUsed

      ```
      long getEnergyUsed()
      ```

      `int64 energy_used = 5;`

      Returns:
      :   The energyUsed.
    - #### getLogsList

      ```
      java.util.List<Response.TransactionInfo.Log> getLogsList()
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`
    - #### getLogs

      ```
      Response.TransactionInfo.Log getLogs(int index)
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`
    - #### getLogsCount

      ```
      int getLogsCount()
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`
    - #### getLogsOrBuilderList

      ```
      java.util.List<? extends Response.TransactionInfo.LogOrBuilder> getLogsOrBuilderList()
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`
    - #### getLogsOrBuilder

      ```
      Response.TransactionInfo.LogOrBuilder getLogsOrBuilder(int index)
      ```

      `repeated .protocol.TransactionInfo.Log logs = 6;`
    - #### getInternalTransactionsList

      ```
      java.util.List<Response.InternalTransaction> getInternalTransactionsList()
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`
    - #### getInternalTransactions

      ```
      Response.InternalTransaction getInternalTransactions(int index)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`
    - #### getInternalTransactionsCount

      ```
      int getInternalTransactionsCount()
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`
    - #### getInternalTransactionsOrBuilderList

      ```
      java.util.List<? extends Response.InternalTransactionOrBuilder> getInternalTransactionsOrBuilderList()
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`
    - #### getInternalTransactionsOrBuilder

      ```
      Response.InternalTransactionOrBuilder getInternalTransactionsOrBuilder(int index)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 7;`
    - #### getEnergyPenalty

      ```
      long getEnergyPenalty()
      ```

      `int64 energy_penalty = 8;`

      Returns:
      :   The energyPenalty.