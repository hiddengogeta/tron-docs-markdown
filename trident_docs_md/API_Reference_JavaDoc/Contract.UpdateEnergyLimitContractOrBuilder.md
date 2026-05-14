

org.tron.trident.proto

## Interface Contract.UpdateEnergyLimitContractOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Contract.UpdateEnergyLimitContract](../../../../org/tron/trident/proto/Contract.UpdateEnergyLimitContract.html "class in org.tron.trident.proto"), [Contract.UpdateEnergyLimitContract.Builder](../../../../org/tron/trident/proto/Contract.UpdateEnergyLimitContract.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Contract.UpdateEnergyLimitContractOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getContractAddress()` `bytes contract_address = 2;` |
    | `long` | `getOriginEnergyLimit()` `int64 origin_energy_limit = 3;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |

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
    - #### getOriginEnergyLimit

      ```
      long getOriginEnergyLimit()
      ```

      `int64 origin_energy_limit = 3;`

      Returns:
      :   The originEnergyLimit.