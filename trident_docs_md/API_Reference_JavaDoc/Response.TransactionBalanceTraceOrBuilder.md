

org.tron.trident.proto

## Interface Response.TransactionBalanceTraceOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.TransactionBalanceTrace](../../../../org/tron/trident/proto/Response.TransactionBalanceTrace.html "class in org.tron.trident.proto"), [Response.TransactionBalanceTrace.Builder](../../../../org/tron/trident/proto/Response.TransactionBalanceTrace.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.TransactionBalanceTraceOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Response.TransactionBalanceTrace.Operation` | `getOperation(int index)` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `int` | `getOperationCount()` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `java.util.List<Response.TransactionBalanceTrace.Operation>` | `getOperationList()` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `Response.TransactionBalanceTrace.OperationOrBuilder` | `getOperationOrBuilder(int index)` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `java.util.List<? extends Response.TransactionBalanceTrace.OperationOrBuilder>` | `getOperationOrBuilderList()` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `java.lang.String` | `getStatus()` `string status = 4;` |
    | `com.google.protobuf.ByteString` | `getStatusBytes()` `string status = 4;` |
    | `com.google.protobuf.ByteString` | `getTransactionIdentifier()` `bytes transaction_identifier = 1;` |
    | `java.lang.String` | `getType()` `string type = 3;` |
    | `com.google.protobuf.ByteString` | `getTypeBytes()` `string type = 3;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getTransactionIdentifier

      ```
      com.google.protobuf.ByteString getTransactionIdentifier()
      ```

      `bytes transaction_identifier = 1;`

      Returns:
      :   The transactionIdentifier.
    - #### getOperationList

      ```
      java.util.List<Response.TransactionBalanceTrace.Operation> getOperationList()
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`
    - #### getOperation

      ```
      Response.TransactionBalanceTrace.Operation getOperation(int index)
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`
    - #### getOperationCount

      ```
      int getOperationCount()
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`
    - #### getOperationOrBuilderList

      ```
      java.util.List<? extends Response.TransactionBalanceTrace.OperationOrBuilder> getOperationOrBuilderList()
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`
    - #### getOperationOrBuilder

      ```
      Response.TransactionBalanceTrace.OperationOrBuilder getOperationOrBuilder(int index)
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`
    - #### getType

      ```
      java.lang.String getType()
      ```

      `string type = 3;`

      Returns:
      :   The type.
    - #### getTypeBytes

      ```
      com.google.protobuf.ByteString getTypeBytes()
      ```

      `string type = 3;`

      Returns:
      :   The bytes for type.
    - #### getStatus

      ```
      java.lang.String getStatus()
      ```

      `string status = 4;`

      Returns:
      :   The status.
    - #### getStatusBytes

      ```
      com.google.protobuf.ByteString getStatusBytes()
      ```

      `string status = 4;`

      Returns:
      :   The bytes for status.