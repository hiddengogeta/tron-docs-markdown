

org.tron.trident.proto

## Interface Common.SmartContractOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Common.SmartContract](../../../../org/tron/trident/proto/Common.SmartContract.html "class in org.tron.trident.proto"), [Common.SmartContract.Builder](../../../../org/tron/trident/proto/Common.SmartContract.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Common](../../../../org/tron/trident/proto/Common.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Common.SmartContractOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Common.SmartContract.ABI` | `getAbi()` `.protocol.SmartContract.ABI abi = 3;` |
    | `Common.SmartContract.ABIOrBuilder` | `getAbiOrBuilder()` `.protocol.SmartContract.ABI abi = 3;` |
    | `com.google.protobuf.ByteString` | `getBytecode()` `bytes bytecode = 4;` |
    | `long` | `getCallValue()` `int64 call_value = 5;` |
    | `com.google.protobuf.ByteString` | `getCodeHash()` `bytes code_hash = 9;` |
    | `long` | `getConsumeUserResourcePercent()` `int64 consume_user_resource_percent = 6;` |
    | `com.google.protobuf.ByteString` | `getContractAddress()` `bytes contract_address = 2;` |
    | `java.lang.String` | `getName()` `string name = 7;` |
    | `com.google.protobuf.ByteString` | `getNameBytes()` `string name = 7;` |
    | `com.google.protobuf.ByteString` | `getOriginAddress()` `bytes origin_address = 1;` |
    | `long` | `getOriginEnergyLimit()` `int64 origin_energy_limit = 8;` |
    | `com.google.protobuf.ByteString` | `getTrxHash()` `bytes trx_hash = 10;` |
    | `int` | `getVersion()` `int32 version = 11;` |
    | `boolean` | `hasAbi()` `.protocol.SmartContract.ABI abi = 3;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getOriginAddress

      ```
      com.google.protobuf.ByteString getOriginAddress()
      ```

      `bytes origin_address = 1;`

      Returns:
      :   The originAddress.
    - #### getContractAddress

      ```
      com.google.protobuf.ByteString getContractAddress()
      ```

      `bytes contract_address = 2;`

      Returns:
      :   The contractAddress.
    - #### hasAbi

      ```
      boolean hasAbi()
      ```

      `.protocol.SmartContract.ABI abi = 3;`

      Returns:
      :   Whether the abi field is set.
    - #### getAbi

      ```
      Common.SmartContract.ABI getAbi()
      ```

      `.protocol.SmartContract.ABI abi = 3;`

      Returns:
      :   The abi.
    - #### getAbiOrBuilder

      ```
      Common.SmartContract.ABIOrBuilder getAbiOrBuilder()
      ```

      `.protocol.SmartContract.ABI abi = 3;`
    - #### getBytecode

      ```
      com.google.protobuf.ByteString getBytecode()
      ```

      `bytes bytecode = 4;`

      Returns:
      :   The bytecode.
    - #### getCallValue

      ```
      long getCallValue()
      ```

      `int64 call_value = 5;`

      Returns:
      :   The callValue.
    - #### getConsumeUserResourcePercent

      ```
      long getConsumeUserResourcePercent()
      ```

      `int64 consume_user_resource_percent = 6;`

      Returns:
      :   The consumeUserResourcePercent.
    - #### getName

      ```
      java.lang.String getName()
      ```

      `string name = 7;`

      Returns:
      :   The name.
    - #### getNameBytes

      ```
      com.google.protobuf.ByteString getNameBytes()
      ```

      `string name = 7;`

      Returns:
      :   The bytes for name.
    - #### getOriginEnergyLimit

      ```
      long getOriginEnergyLimit()
      ```

      `int64 origin_energy_limit = 8;`

      Returns:
      :   The originEnergyLimit.
    - #### getCodeHash

      ```
      com.google.protobuf.ByteString getCodeHash()
      ```

      `bytes code_hash = 9;`

      Returns:
      :   The codeHash.
    - #### getTrxHash

      ```
      com.google.protobuf.ByteString getTrxHash()
      ```

      `bytes trx_hash = 10;`

      Returns:
      :   The trxHash.
    - #### getVersion

      ```
      int getVersion()
      ```

      `int32 version = 11;`

      Returns:
      :   The version.