

org.tron.trident.proto

## Interface Response.TransactionApprovedList.ResultOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.TransactionApprovedList.Result](../../../../org/tron/trident/proto/Response.TransactionApprovedList.Result.html "class in org.tron.trident.proto"), [Response.TransactionApprovedList.Result.Builder](../../../../org/tron/trident/proto/Response.TransactionApprovedList.Result.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response.TransactionApprovedList](../../../../org/tron/trident/proto/Response.TransactionApprovedList.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.TransactionApprovedList.ResultOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Response.TransactionApprovedList.Result.response_code` | `getCode()` `.protocol.TransactionApprovedList.Result.response_code code = 1;` |
    | `int` | `getCodeValue()` `.protocol.TransactionApprovedList.Result.response_code code = 1;` |
    | `java.lang.String` | `getMessage()` `string message = 2;` |
    | `com.google.protobuf.ByteString` | `getMessageBytes()` `string message = 2;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getCodeValue

      ```
      int getCodeValue()
      ```

      `.protocol.TransactionApprovedList.Result.response_code code = 1;`

      Returns:
      :   The enum numeric value on the wire for code.
    - #### getCode

      ```
      Response.TransactionApprovedList.Result.response_code getCode()
      ```

      `.protocol.TransactionApprovedList.Result.response_code code = 1;`

      Returns:
      :   The code.
    - #### getMessage

      ```
      java.lang.String getMessage()
      ```

      `string message = 2;`

      Returns:
      :   The message.
    - #### getMessageBytes

      ```
      com.google.protobuf.ByteString getMessageBytes()
      ```

      `string message = 2;`

      Returns:
      :   The bytes for message.