

org.tron.trident.proto

## Interface Response.InternalTransaction.CallValueInfoOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.InternalTransaction.CallValueInfo](../../../../org/tron/trident/proto/Response.InternalTransaction.CallValueInfo.html "class in org.tron.trident.proto"), [Response.InternalTransaction.CallValueInfo.Builder](../../../../org/tron/trident/proto/Response.InternalTransaction.CallValueInfo.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response.InternalTransaction](../../../../org/tron/trident/proto/Response.InternalTransaction.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.InternalTransaction.CallValueInfoOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getCallValue()` trx (TBD: or token) value |
    | `java.lang.String` | `getTokenId()` TBD: tokenName, trx should be empty |
    | `com.google.protobuf.ByteString` | `getTokenIdBytes()` TBD: tokenName, trx should be empty |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getCallValue

      ```
      long getCallValue()
      ```

      ```
       trx (TBD: or token) value
      ```

      `int64 callValue = 1;`

      Returns:
      :   The callValue.
    - #### getTokenId

      ```
      java.lang.String getTokenId()
      ```

      ```
       TBD: tokenName, trx should be empty
      ```

      `string tokenId = 2;`

      Returns:
      :   The tokenId.
    - #### getTokenIdBytes

      ```
      com.google.protobuf.ByteString getTokenIdBytes()
      ```

      ```
       TBD: tokenName, trx should be empty
      ```

      `string tokenId = 2;`

      Returns:
      :   The bytes for tokenId.