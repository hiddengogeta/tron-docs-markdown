

org.tron.trident.proto

## Interface Response.TransactionBalanceTrace.OperationOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.TransactionBalanceTrace.Operation](../../../../org/tron/trident/proto/Response.TransactionBalanceTrace.Operation.html "class in org.tron.trident.proto"), [Response.TransactionBalanceTrace.Operation.Builder](../../../../org/tron/trident/proto/Response.TransactionBalanceTrace.Operation.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response.TransactionBalanceTrace](../../../../org/tron/trident/proto/Response.TransactionBalanceTrace.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.TransactionBalanceTrace.OperationOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getAddress()` `bytes address = 2;` |
    | `long` | `getAmount()` `int64 amount = 3;` |
    | `long` | `getOperationIdentifier()` `int64 operation_identifier = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getOperationIdentifier

      ```
      long getOperationIdentifier()
      ```

      `int64 operation_identifier = 1;`

      Returns:
      :   The operationIdentifier.
    - #### getAddress

      ```
      com.google.protobuf.ByteString getAddress()
      ```

      `bytes address = 2;`

      Returns:
      :   The address.
    - #### getAmount

      ```
      long getAmount()
      ```

      `int64 amount = 3;`

      Returns:
      :   The amount.