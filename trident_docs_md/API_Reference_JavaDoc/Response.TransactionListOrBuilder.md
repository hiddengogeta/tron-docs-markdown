

org.tron.trident.proto

## Interface Response.TransactionListOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.TransactionList](../../../../org/tron/trident/proto/Response.TransactionList.html "class in org.tron.trident.proto"), [Response.TransactionList.Builder](../../../../org/tron/trident/proto/Response.TransactionList.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.TransactionListOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Chain.Transaction` | `getTransaction(int index)` `repeated .protocol.Transaction transaction = 1;` |
    | `int` | `getTransactionCount()` `repeated .protocol.Transaction transaction = 1;` |
    | `java.util.List<Chain.Transaction>` | `getTransactionList()` `repeated .protocol.Transaction transaction = 1;` |
    | `Chain.TransactionOrBuilder` | `getTransactionOrBuilder(int index)` `repeated .protocol.Transaction transaction = 1;` |
    | `java.util.List<? extends Chain.TransactionOrBuilder>` | `getTransactionOrBuilderList()` `repeated .protocol.Transaction transaction = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getTransactionList

      ```
      java.util.List<Chain.Transaction> getTransactionList()
      ```

      `repeated .protocol.Transaction transaction = 1;`
    - #### getTransaction

      ```
      Chain.Transaction getTransaction(int index)
      ```

      `repeated .protocol.Transaction transaction = 1;`
    - #### getTransactionCount

      ```
      int getTransactionCount()
      ```

      `repeated .protocol.Transaction transaction = 1;`
    - #### getTransactionOrBuilderList

      ```
      java.util.List<? extends Chain.TransactionOrBuilder> getTransactionOrBuilderList()
      ```

      `repeated .protocol.Transaction transaction = 1;`
    - #### getTransactionOrBuilder

      ```
      Chain.TransactionOrBuilder getTransactionOrBuilder(int index)
      ```

      `repeated .protocol.Transaction transaction = 1;`