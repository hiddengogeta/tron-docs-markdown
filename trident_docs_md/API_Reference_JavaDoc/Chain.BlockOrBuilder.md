

org.tron.trident.proto

## Interface Chain.BlockOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Chain.Block](../../../../org/tron/trident/proto/Chain.Block.html "class in org.tron.trident.proto"), [Chain.Block.Builder](../../../../org/tron/trident/proto/Chain.Block.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Chain](../../../../org/tron/trident/proto/Chain.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Chain.BlockOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Chain.BlockHeader` | `getBlockHeader()` `.protocol.BlockHeader block_header = 2;` |
    | `Chain.BlockHeaderOrBuilder` | `getBlockHeaderOrBuilder()` `.protocol.BlockHeader block_header = 2;` |
    | `Chain.Transaction` | `getTransactions(int index)` `repeated .protocol.Transaction transactions = 1;` |
    | `int` | `getTransactionsCount()` `repeated .protocol.Transaction transactions = 1;` |
    | `java.util.List<Chain.Transaction>` | `getTransactionsList()` `repeated .protocol.Transaction transactions = 1;` |
    | `Chain.TransactionOrBuilder` | `getTransactionsOrBuilder(int index)` `repeated .protocol.Transaction transactions = 1;` |
    | `java.util.List<? extends Chain.TransactionOrBuilder>` | `getTransactionsOrBuilderList()` `repeated .protocol.Transaction transactions = 1;` |
    | `boolean` | `hasBlockHeader()` `.protocol.BlockHeader block_header = 2;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getTransactionsList

      ```
      java.util.List<Chain.Transaction> getTransactionsList()
      ```

      `repeated .protocol.Transaction transactions = 1;`
    - #### getTransactions

      ```
      Chain.Transaction getTransactions(int index)
      ```

      `repeated .protocol.Transaction transactions = 1;`
    - #### getTransactionsCount

      ```
      int getTransactionsCount()
      ```

      `repeated .protocol.Transaction transactions = 1;`
    - #### getTransactionsOrBuilderList

      ```
      java.util.List<? extends Chain.TransactionOrBuilder> getTransactionsOrBuilderList()
      ```

      `repeated .protocol.Transaction transactions = 1;`
    - #### getTransactionsOrBuilder

      ```
      Chain.TransactionOrBuilder getTransactionsOrBuilder(int index)
      ```

      `repeated .protocol.Transaction transactions = 1;`
    - #### hasBlockHeader

      ```
      boolean hasBlockHeader()
      ```

      `.protocol.BlockHeader block_header = 2;`

      Returns:
      :   Whether the blockHeader field is set.
    - #### getBlockHeader

      ```
      Chain.BlockHeader getBlockHeader()
      ```

      `.protocol.BlockHeader block_header = 2;`

      Returns:
      :   The blockHeader.
    - #### getBlockHeaderOrBuilder

      ```
      Chain.BlockHeaderOrBuilder getBlockHeaderOrBuilder()
      ```

      `.protocol.BlockHeader block_header = 2;`