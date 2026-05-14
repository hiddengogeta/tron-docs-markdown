

org.tron.trident.proto

## Interface Contract.TriggerSmartContractOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Contract.TriggerSmartContract](../../../../org/tron/trident/proto/Contract.TriggerSmartContract.html "class in org.tron.trident.proto"), [Contract.TriggerSmartContract.Builder](../../../../org/tron/trident/proto/Contract.TriggerSmartContract.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Contract.TriggerSmartContractOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getCallTokenValue()` `int64 call_token_value = 5;` |
    | `long` | `getCallValue()` `int64 call_value = 3;` |
    | `com.google.protobuf.ByteString` | `getContractAddress()` `bytes contract_address = 2;` |
    | `com.google.protobuf.ByteString` | `getData()` `bytes data = 4;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `long` | `getTokenId()` `int64 token_id = 6;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getOwnerAddress

      ```
      com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   The ownerAddress.
    - #### getContractAddress

      ```
      com.google.protobuf.ByteString getContractAddress()
      ```

      `bytes contract_address = 2;`

      Returns:
      :   The contractAddress.
    - #### getCallValue

      ```
      long getCallValue()
      ```

      `int64 call_value = 3;`

      Returns:
      :   The callValue.
    - #### getData

      ```
      com.google.protobuf.ByteString getData()
      ```

      `bytes data = 4;`

      Returns:
      :   The data.
    - #### getCallTokenValue

      ```
      long getCallTokenValue()
      ```

      `int64 call_token_value = 5;`

      Returns:
      :   The callTokenValue.
    - #### getTokenId

      ```
      long getTokenId()
      ```

      `int64 token_id = 6;`

      Returns:
      :   The tokenId.