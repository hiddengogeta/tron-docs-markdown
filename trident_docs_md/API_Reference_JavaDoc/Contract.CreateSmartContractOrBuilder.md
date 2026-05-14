

org.tron.trident.proto

## Interface Contract.CreateSmartContractOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Contract.CreateSmartContract](../../../../org/tron/trident/proto/Contract.CreateSmartContract.html "class in org.tron.trident.proto"), [Contract.CreateSmartContract.Builder](../../../../org/tron/trident/proto/Contract.CreateSmartContract.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Contract.CreateSmartContractOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getCallTokenValue()` `int64 call_token_value = 3;` |
    | `Common.SmartContract` | `getNewContract()` `.protocol.SmartContract new_contract = 2;` |
    | `Common.SmartContractOrBuilder` | `getNewContractOrBuilder()` `.protocol.SmartContract new_contract = 2;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `long` | `getTokenId()` `int64 token_id = 4;` |
    | `boolean` | `hasNewContract()` `.protocol.SmartContract new_contract = 2;` |

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
    - #### hasNewContract

      ```
      boolean hasNewContract()
      ```

      `.protocol.SmartContract new_contract = 2;`

      Returns:
      :   Whether the newContract field is set.
    - #### getNewContract

      ```
      Common.SmartContract getNewContract()
      ```

      `.protocol.SmartContract new_contract = 2;`

      Returns:
      :   The newContract.
    - #### getNewContractOrBuilder

      ```
      Common.SmartContractOrBuilder getNewContractOrBuilder()
      ```

      `.protocol.SmartContract new_contract = 2;`
    - #### getCallTokenValue

      ```
      long getCallTokenValue()
      ```

      `int64 call_token_value = 3;`

      Returns:
      :   The callTokenValue.
    - #### getTokenId

      ```
      long getTokenId()
      ```

      `int64 token_id = 4;`

      Returns:
      :   The tokenId.