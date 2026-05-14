

org.tron.trident.proto

## Interface Response.SmartContractDataWrapperOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.SmartContractDataWrapper](../../../../org/tron/trident/proto/Response.SmartContractDataWrapper.html "class in org.tron.trident.proto"), [Response.SmartContractDataWrapper.Builder](../../../../org/tron/trident/proto/Response.SmartContractDataWrapper.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.SmartContractDataWrapperOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Contract.ContractState` | `getContractState()` `.protocol.ContractState contract_state = 3;` |
    | `Contract.ContractStateOrBuilder` | `getContractStateOrBuilder()` `.protocol.ContractState contract_state = 3;` |
    | `com.google.protobuf.ByteString` | `getRuntimeCode()` `bytes runtime_code = 2;` |
    | `Common.SmartContract` | `getSmartContract()` `.protocol.SmartContract smart_contract = 1;` |
    | `Common.SmartContractOrBuilder` | `getSmartContractOrBuilder()` `.protocol.SmartContract smart_contract = 1;` |
    | `boolean` | `hasContractState()` `.protocol.ContractState contract_state = 3;` |
    | `boolean` | `hasSmartContract()` `.protocol.SmartContract smart_contract = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### hasSmartContract

      ```
      boolean hasSmartContract()
      ```

      `.protocol.SmartContract smart_contract = 1;`

      Returns:
      :   Whether the smartContract field is set.
    - #### getSmartContract

      ```
      Common.SmartContract getSmartContract()
      ```

      `.protocol.SmartContract smart_contract = 1;`

      Returns:
      :   The smartContract.
    - #### getSmartContractOrBuilder

      ```
      Common.SmartContractOrBuilder getSmartContractOrBuilder()
      ```

      `.protocol.SmartContract smart_contract = 1;`
    - #### getRuntimeCode

      ```
      com.google.protobuf.ByteString getRuntimeCode()
      ```

      `bytes runtime_code = 2;`

      Returns:
      :   The runtimeCode.
    - #### hasContractState

      ```
      boolean hasContractState()
      ```

      `.protocol.ContractState contract_state = 3;`

      Returns:
      :   Whether the contractState field is set.
    - #### getContractState

      ```
      Contract.ContractState getContractState()
      ```

      `.protocol.ContractState contract_state = 3;`

      Returns:
      :   The contractState.
    - #### getContractStateOrBuilder

      ```
      Contract.ContractStateOrBuilder getContractStateOrBuilder()
      ```

      `.protocol.ContractState contract_state = 3;`