

org.tron.trident.api

## Interface GrpcAPI.TransactionIdListOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.TransactionIdList](../../../../org/tron/trident/api/GrpcAPI.TransactionIdList.html "class in org.tron.trident.api"), [GrpcAPI.TransactionIdList.Builder](../../../../org/tron/trident/api/GrpcAPI.TransactionIdList.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.TransactionIdListOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `java.lang.String` | `getTxId(int index)` `repeated string txId = 1;` |
    | `com.google.protobuf.ByteString` | `getTxIdBytes(int index)` `repeated string txId = 1;` |
    | `int` | `getTxIdCount()` `repeated string txId = 1;` |
    | `java.util.List<java.lang.String>` | `getTxIdList()` `repeated string txId = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getTxIdList

      ```
      java.util.List<java.lang.String> getTxIdList()
      ```

      `repeated string txId = 1;`

      Returns:
      :   A list containing the txId.
    - #### getTxIdCount

      ```
      int getTxIdCount()
      ```

      `repeated string txId = 1;`

      Returns:
      :   The count of txId.
    - #### getTxId

      ```
      java.lang.String getTxId(int index)
      ```

      `repeated string txId = 1;`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The txId at the given index.
    - #### getTxIdBytes

      ```
      com.google.protobuf.ByteString getTxIdBytes(int index)
      ```

      `repeated string txId = 1;`

      Parameters:
      :   `index` - The index of the value to return.

      Returns:
      :   The bytes of the txId at the given index.