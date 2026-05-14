

org.tron.trident.proto

## Interface Response.EasyTransferResponseOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.EasyTransferResponse](../../../../org/tron/trident/proto/Response.EasyTransferResponse.html "class in org.tron.trident.proto"), [Response.EasyTransferResponse.Builder](../../../../org/tron/trident/proto/Response.EasyTransferResponse.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.EasyTransferResponseOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Response.TransactionReturn` | `getResult()` `.protocol.TransactionReturn result = 2;` |
    | `Response.TransactionReturnOrBuilder` | `getResultOrBuilder()` `.protocol.TransactionReturn result = 2;` |
    | `Chain.Transaction` | `getTransaction()` `.protocol.Transaction transaction = 1;` |
    | `Chain.TransactionOrBuilder` | `getTransactionOrBuilder()` `.protocol.Transaction transaction = 1;` |
    | `com.google.protobuf.ByteString` | `getTxid()` transaction id = sha256(transaction.raw\_data) |
    | `boolean` | `hasResult()` `.protocol.TransactionReturn result = 2;` |
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
    - #### hasResult

      ```
      boolean hasResult()
      ```

      `.protocol.TransactionReturn result = 2;`

      Returns:
      :   Whether the result field is set.
    - #### getResult

      ```
      Response.TransactionReturn getResult()
      ```

      `.protocol.TransactionReturn result = 2;`

      Returns:
      :   The result.
    - #### getResultOrBuilder

      ```
      Response.TransactionReturnOrBuilder getResultOrBuilder()
      ```

      `.protocol.TransactionReturn result = 2;`
    - #### getTxid

      ```
      com.google.protobuf.ByteString getTxid()
      ```

      ```
       transaction id = sha256(transaction.raw_data)
      ```

      `bytes txid = 3;`

      Returns:
      :   The txid.