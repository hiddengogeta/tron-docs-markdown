

org.tron.trident.proto

## Interface Response.BlockExtentionOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.BlockExtention](../../../../org/tron/trident/proto/Response.BlockExtention.html "class in org.tron.trident.proto"), [Response.BlockExtention.Builder](../../../../org/tron/trident/proto/Response.BlockExtention.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.BlockExtentionOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Chain.BlockHeader` | `getBlockHeader()` `.protocol.BlockHeader block_header = 2;` |
    | `Chain.BlockHeaderOrBuilder` | `getBlockHeaderOrBuilder()` `.protocol.BlockHeader block_header = 2;` |
    | `com.google.protobuf.ByteString` | `getBlockid()` `bytes blockid = 3;` |
    | `Response.TransactionExtention` | `getTransactions(int index)` `repeated .protocol.TransactionExtention transactions = 1;` |
    | `int` | `getTransactionsCount()` `repeated .protocol.TransactionExtention transactions = 1;` |
    | `java.util.List<Response.TransactionExtention>` | `getTransactionsList()` `repeated .protocol.TransactionExtention transactions = 1;` |
    | `Response.TransactionExtentionOrBuilder` | `getTransactionsOrBuilder(int index)` `repeated .protocol.TransactionExtention transactions = 1;` |
    | `java.util.List<? extends Response.TransactionExtentionOrBuilder>` | `getTransactionsOrBuilderList()` `repeated .protocol.TransactionExtention transactions = 1;` |
    | `boolean` | `hasBlockHeader()` `.protocol.BlockHeader block_header = 2;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getTransactionsList

      ```
      java.util.List<Response.TransactionExtention> getTransactionsList()
      ```

      `repeated .protocol.TransactionExtention transactions = 1;`
    - #### getTransactions

      ```
      Response.TransactionExtention getTransactions(int index)
      ```

      `repeated .protocol.TransactionExtention transactions = 1;`
    - #### getTransactionsCount

      ```
      int getTransactionsCount()
      ```

      `repeated .protocol.TransactionExtention transactions = 1;`
    - #### getTransactionsOrBuilderList

      ```
      java.util.List<? extends Response.TransactionExtentionOrBuilder> getTransactionsOrBuilderList()
      ```

      `repeated .protocol.TransactionExtention transactions = 1;`
    - #### getTransactionsOrBuilder

      ```
      Response.TransactionExtentionOrBuilder getTransactionsOrBuilder(int index)
      ```

      `repeated .protocol.TransactionExtention transactions = 1;`
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
    - #### getBlockid

      ```
      com.google.protobuf.ByteString getBlockid()
      ```

      `bytes blockid = 3;`

      Returns:
      :   The blockid.