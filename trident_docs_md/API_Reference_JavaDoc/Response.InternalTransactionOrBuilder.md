

org.tron.trident.proto

## Interface Response.InternalTransactionOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.InternalTransaction](../../../../org/tron/trident/proto/Response.InternalTransaction.html "class in org.tron.trident.proto"), [Response.InternalTransaction.Builder](../../../../org/tron/trident/proto/Response.InternalTransaction.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.InternalTransactionOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getCallerAddress()` the one send trx (TBD: or token) via function |
    | `Response.InternalTransaction.CallValueInfo` | `getCallValueInfo(int index)` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `int` | `getCallValueInfoCount()` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `java.util.List<Response.InternalTransaction.CallValueInfo>` | `getCallValueInfoList()` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `Response.InternalTransaction.CallValueInfoOrBuilder` | `getCallValueInfoOrBuilder(int index)` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `java.util.List<? extends Response.InternalTransaction.CallValueInfoOrBuilder>` | `getCallValueInfoOrBuilderList()` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `java.lang.String` | `getExtra()` `string extra = 7;` |
    | `com.google.protobuf.ByteString` | `getExtraBytes()` `string extra = 7;` |
    | `com.google.protobuf.ByteString` | `getHash()` internalTransaction identity, the root InternalTransaction hash should equals to root transaction id. |
    | `com.google.protobuf.ByteString` | `getNote()` `bytes note = 5;` |
    | `boolean` | `getRejected()` `bool rejected = 6;` |
    | `com.google.protobuf.ByteString` | `getTransferToAddress()` the one recieve trx (TBD: or token) via function |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getHash

      ```
      com.google.protobuf.ByteString getHash()
      ```

      ```
       internalTransaction identity, the root InternalTransaction hash
       should equals to root transaction id.
      ```

      `bytes hash = 1;`

      Returns:
      :   The hash.
    - #### getCallerAddress

      ```
      com.google.protobuf.ByteString getCallerAddress()
      ```

      ```
       the one send trx (TBD: or token) via function
      ```

      `bytes caller_address = 2;`

      Returns:
      :   The callerAddress.
    - #### getTransferToAddress

      ```
      com.google.protobuf.ByteString getTransferToAddress()
      ```

      ```
       the one recieve trx (TBD: or token) via function
      ```

      `bytes transferTo_address = 3;`

      Returns:
      :   The transferToAddress.
    - #### getCallValueInfoList

      ```
      java.util.List<Response.InternalTransaction.CallValueInfo> getCallValueInfoList()
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`
    - #### getCallValueInfo

      ```
      Response.InternalTransaction.CallValueInfo getCallValueInfo(int index)
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`
    - #### getCallValueInfoCount

      ```
      int getCallValueInfoCount()
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`
    - #### getCallValueInfoOrBuilderList

      ```
      java.util.List<? extends Response.InternalTransaction.CallValueInfoOrBuilder> getCallValueInfoOrBuilderList()
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`
    - #### getCallValueInfoOrBuilder

      ```
      Response.InternalTransaction.CallValueInfoOrBuilder getCallValueInfoOrBuilder(int index)
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`
    - #### getNote

      ```
      com.google.protobuf.ByteString getNote()
      ```

      `bytes note = 5;`

      Returns:
      :   The note.
    - #### getRejected

      ```
      boolean getRejected()
      ```

      `bool rejected = 6;`

      Returns:
      :   The rejected.
    - #### getExtra

      ```
      java.lang.String getExtra()
      ```

      `string extra = 7;`

      Returns:
      :   The extra.
    - #### getExtraBytes

      ```
      com.google.protobuf.ByteString getExtraBytes()
      ```

      `string extra = 7;`

      Returns:
      :   The bytes for extra.