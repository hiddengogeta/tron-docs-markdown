

org.tron.trident.proto

## Interface Response.BlockBalanceTraceOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.BlockBalanceTrace](../../../../org/tron/trident/proto/Response.BlockBalanceTrace.html "class in org.tron.trident.proto"), [Response.BlockBalanceTrace.Builder](../../../../org/tron/trident/proto/Response.BlockBalanceTrace.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.BlockBalanceTraceOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Response.BlockIdentifier` | `getBlockIdentifier()` `.protocol.BlockIdentifier block_identifier = 1;` |
    | `Response.BlockIdentifierOrBuilder` | `getBlockIdentifierOrBuilder()` `.protocol.BlockIdentifier block_identifier = 1;` |
    | `long` | `getTimestamp()` `int64 timestamp = 2;` |
    | `Response.TransactionBalanceTrace` | `getTransactionBalanceTrace(int index)` BlockIdentifier parent\_block\_identifier = 4; |
    | `int` | `getTransactionBalanceTraceCount()` BlockIdentifier parent\_block\_identifier = 4; |
    | `java.util.List<Response.TransactionBalanceTrace>` | `getTransactionBalanceTraceList()` BlockIdentifier parent\_block\_identifier = 4; |
    | `Response.TransactionBalanceTraceOrBuilder` | `getTransactionBalanceTraceOrBuilder(int index)` BlockIdentifier parent\_block\_identifier = 4; |
    | `java.util.List<? extends Response.TransactionBalanceTraceOrBuilder>` | `getTransactionBalanceTraceOrBuilderList()` BlockIdentifier parent\_block\_identifier = 4; |
    | `boolean` | `hasBlockIdentifier()` `.protocol.BlockIdentifier block_identifier = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### hasBlockIdentifier

      ```
      boolean hasBlockIdentifier()
      ```

      `.protocol.BlockIdentifier block_identifier = 1;`

      Returns:
      :   Whether the blockIdentifier field is set.
    - #### getBlockIdentifier

      ```
      Response.BlockIdentifier getBlockIdentifier()
      ```

      `.protocol.BlockIdentifier block_identifier = 1;`

      Returns:
      :   The blockIdentifier.
    - #### getBlockIdentifierOrBuilder

      ```
      Response.BlockIdentifierOrBuilder getBlockIdentifierOrBuilder()
      ```

      `.protocol.BlockIdentifier block_identifier = 1;`
    - #### getTimestamp

      ```
      long getTimestamp()
      ```

      `int64 timestamp = 2;`

      Returns:
      :   The timestamp.
    - #### getTransactionBalanceTraceList

      ```
      java.util.List<Response.TransactionBalanceTrace> getTransactionBalanceTraceList()
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`
    - #### getTransactionBalanceTrace

      ```
      Response.TransactionBalanceTrace getTransactionBalanceTrace(int index)
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`
    - #### getTransactionBalanceTraceCount

      ```
      int getTransactionBalanceTraceCount()
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`
    - #### getTransactionBalanceTraceOrBuilderList

      ```
      java.util.List<? extends Response.TransactionBalanceTraceOrBuilder> getTransactionBalanceTraceOrBuilderList()
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`
    - #### getTransactionBalanceTraceOrBuilder

      ```
      Response.TransactionBalanceTraceOrBuilder getTransactionBalanceTraceOrBuilder(int index)
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`