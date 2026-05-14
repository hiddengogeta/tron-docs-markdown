

org.tron.trident.proto

## Interface Response.TransactionSignOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.TransactionSign](../../../../org/tron/trident/proto/Response.TransactionSign.html "class in org.tron.trident.proto"), [Response.TransactionSign.Builder](../../../../org/tron/trident/proto/Response.TransactionSign.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.TransactionSignOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getPrivateKey()` `bytes privateKey = 2;` |
    | `Chain.Transaction` | `getTransaction()` `.protocol.Transaction transaction = 1;` |
    | `Chain.TransactionOrBuilder` | `getTransactionOrBuilder()` `.protocol.Transaction transaction = 1;` |
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
    - #### getPrivateKey

      ```
      com.google.protobuf.ByteString getPrivateKey()
      ```

      `bytes privateKey = 2;`

      Returns:
      :   The privateKey.