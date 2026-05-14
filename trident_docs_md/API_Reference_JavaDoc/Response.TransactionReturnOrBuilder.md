

org.tron.trident.proto

## Interface Response.TransactionReturnOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.TransactionReturn](../../../../org/tron/trident/proto/Response.TransactionReturn.html "class in org.tron.trident.proto"), [Response.TransactionReturn.Builder](../../../../org/tron/trident/proto/Response.TransactionReturn.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.TransactionReturnOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Response.TransactionReturn.response_code` | `getCode()` `.protocol.TransactionReturn.response_code code = 2;` |
    | `int` | `getCodeValue()` `.protocol.TransactionReturn.response_code code = 2;` |
    | `com.google.protobuf.ByteString` | `getMessage()` `bytes message = 3;` |
    | `boolean` | `getResult()` `bool result = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getResult

      ```
      boolean getResult()
      ```

      `bool result = 1;`

      Returns:
      :   The result.
    - #### getCodeValue

      ```
      int getCodeValue()
      ```

      `.protocol.TransactionReturn.response_code code = 2;`

      Returns:
      :   The enum numeric value on the wire for code.
    - #### getCode

      ```
      Response.TransactionReturn.response_code getCode()
      ```

      `.protocol.TransactionReturn.response_code code = 2;`

      Returns:
      :   The code.
    - #### getMessage

      ```
      com.google.protobuf.ByteString getMessage()
      ```

      `bytes message = 3;`

      Returns:
      :   The message.