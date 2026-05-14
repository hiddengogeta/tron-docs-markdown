

org.tron.trident.proto

## Interface Response.TransactionInfoListOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.TransactionInfoList](../../../../org/tron/trident/proto/Response.TransactionInfoList.html "class in org.tron.trident.proto"), [Response.TransactionInfoList.Builder](../../../../org/tron/trident/proto/Response.TransactionInfoList.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.TransactionInfoListOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Response.TransactionInfo` | `getTransactionInfo(int index)` `repeated .protocol.TransactionInfo transactionInfo = 1;` |
    | `int` | `getTransactionInfoCount()` `repeated .protocol.TransactionInfo transactionInfo = 1;` |
    | `java.util.List<Response.TransactionInfo>` | `getTransactionInfoList()` `repeated .protocol.TransactionInfo transactionInfo = 1;` |
    | `Response.TransactionInfoOrBuilder` | `getTransactionInfoOrBuilder(int index)` `repeated .protocol.TransactionInfo transactionInfo = 1;` |
    | `java.util.List<? extends Response.TransactionInfoOrBuilder>` | `getTransactionInfoOrBuilderList()` `repeated .protocol.TransactionInfo transactionInfo = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getTransactionInfoList

      ```
      java.util.List<Response.TransactionInfo> getTransactionInfoList()
      ```

      `repeated .protocol.TransactionInfo transactionInfo = 1;`
    - #### getTransactionInfo

      ```
      Response.TransactionInfo getTransactionInfo(int index)
      ```

      `repeated .protocol.TransactionInfo transactionInfo = 1;`
    - #### getTransactionInfoCount

      ```
      int getTransactionInfoCount()
      ```

      `repeated .protocol.TransactionInfo transactionInfo = 1;`
    - #### getTransactionInfoOrBuilderList

      ```
      java.util.List<? extends Response.TransactionInfoOrBuilder> getTransactionInfoOrBuilderList()
      ```

      `repeated .protocol.TransactionInfo transactionInfo = 1;`
    - #### getTransactionInfoOrBuilder

      ```
      Response.TransactionInfoOrBuilder getTransactionInfoOrBuilder(int index)
      ```

      `repeated .protocol.TransactionInfo transactionInfo = 1;`