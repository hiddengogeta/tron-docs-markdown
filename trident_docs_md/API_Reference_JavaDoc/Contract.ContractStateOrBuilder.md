

org.tron.trident.proto

## Interface Contract.ContractStateOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Contract.ContractState](../../../../org/tron/trident/proto/Contract.ContractState.html "class in org.tron.trident.proto"), [Contract.ContractState.Builder](../../../../org/tron/trident/proto/Contract.ContractState.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Contract.ContractStateOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getEnergyFactor()` `int64 energy_factor = 2;` |
    | `long` | `getEnergyUsage()` `int64 energy_usage = 1;` |
    | `long` | `getUpdateCycle()` `int64 update_cycle = 3;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getEnergyUsage

      ```
      long getEnergyUsage()
      ```

      `int64 energy_usage = 1;`

      Returns:
      :   The energyUsage.
    - #### getEnergyFactor

      ```
      long getEnergyFactor()
      ```

      `int64 energy_factor = 2;`

      Returns:
      :   The energyFactor.
    - #### getUpdateCycle

      ```
      long getUpdateCycle()
      ```

      `int64 update_cycle = 3;`

      Returns:
      :   The updateCycle.