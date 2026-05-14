

org.tron.trident.proto

## Interface Response.Account.AccountResourceOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.Account.AccountResource](../../../../org/tron/trident/proto/Response.Account.AccountResource.html "class in org.tron.trident.proto"), [Response.Account.AccountResource.Builder](../../../../org/tron/trident/proto/Response.Account.AccountResource.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response.Account](../../../../org/tron/trident/proto/Response.Account.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.Account.AccountResourceOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getAcquiredDelegatedFrozenBalanceForEnergy()` Frozen balance provided by other accounts to this account |
    | `long` | `getAcquiredDelegatedFrozenV2BalanceForEnergy()` `int64 acquired_delegated_frozenV2_balance_for_energy = 11;` |
    | `long` | `getDelegatedFrozenBalanceForEnergy()` Frozen balances provided to other accounts |
    | `long` | `getDelegatedFrozenV2BalanceForEnergy()` `int64 delegated_frozenV2_balance_for_energy = 10;` |
    | `long` | `getEnergyUsage()` energy resource, get from frozen |
    | `boolean` | `getEnergyWindowOptimized()` `bool energy_window_optimized = 12;` |
    | `long` | `getEnergyWindowSize()` `int64 energy_window_size = 9;` |
    | `Response.Account.Frozen` | `getFrozenBalanceForEnergy()` the frozen balance for energy |
    | `Response.Account.FrozenOrBuilder` | `getFrozenBalanceForEnergyOrBuilder()` the frozen balance for energy |
    | `long` | `getLatestConsumeTimeForEnergy()` `int64 latest_consume_time_for_energy = 3;` |
    | `long` | `getLatestExchangeStorageTime()` `int64 latest_exchange_storage_time = 8;` |
    | `long` | `getStorageLimit()` storage resource, get from market |
    | `long` | `getStorageUsage()` `int64 storage_usage = 7;` |
    | `boolean` | `hasFrozenBalanceForEnergy()` the frozen balance for energy |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getEnergyUsage

      ```
      long getEnergyUsage()
      ```

      ```
       energy resource, get from frozen
      ```

      `int64 energy_usage = 1;`

      Returns:
      :   The energyUsage.
    - #### hasFrozenBalanceForEnergy

      ```
      boolean hasFrozenBalanceForEnergy()
      ```

      ```
       the frozen balance for energy
      ```

      `.protocol.Account.Frozen frozen_balance_for_energy = 2;`

      Returns:
      :   Whether the frozenBalanceForEnergy field is set.
    - #### getFrozenBalanceForEnergy

      ```
      Response.Account.Frozen getFrozenBalanceForEnergy()
      ```

      ```
       the frozen balance for energy
      ```

      `.protocol.Account.Frozen frozen_balance_for_energy = 2;`

      Returns:
      :   The frozenBalanceForEnergy.
    - #### getFrozenBalanceForEnergyOrBuilder

      ```
      Response.Account.FrozenOrBuilder getFrozenBalanceForEnergyOrBuilder()
      ```

      ```
       the frozen balance for energy
      ```

      `.protocol.Account.Frozen frozen_balance_for_energy = 2;`
    - #### getLatestConsumeTimeForEnergy

      ```
      long getLatestConsumeTimeForEnergy()
      ```

      `int64 latest_consume_time_for_energy = 3;`

      Returns:
      :   The latestConsumeTimeForEnergy.
    - #### getAcquiredDelegatedFrozenBalanceForEnergy

      ```
      long getAcquiredDelegatedFrozenBalanceForEnergy()
      ```

      ```
       Frozen balance provided by other accounts to this account
      ```

      `int64 acquired_delegated_frozen_balance_for_energy = 4;`

      Returns:
      :   The acquiredDelegatedFrozenBalanceForEnergy.
    - #### getDelegatedFrozenBalanceForEnergy

      ```
      long getDelegatedFrozenBalanceForEnergy()
      ```

      ```
       Frozen balances provided to other accounts
      ```

      `int64 delegated_frozen_balance_for_energy = 5;`

      Returns:
      :   The delegatedFrozenBalanceForEnergy.
    - #### getStorageLimit

      ```
      long getStorageLimit()
      ```

      ```
       storage resource, get from market
      ```

      `int64 storage_limit = 6;`

      Returns:
      :   The storageLimit.
    - #### getStorageUsage

      ```
      long getStorageUsage()
      ```

      `int64 storage_usage = 7;`

      Returns:
      :   The storageUsage.
    - #### getLatestExchangeStorageTime

      ```
      long getLatestExchangeStorageTime()
      ```

      `int64 latest_exchange_storage_time = 8;`

      Returns:
      :   The latestExchangeStorageTime.
    - #### getEnergyWindowSize

      ```
      long getEnergyWindowSize()
      ```

      `int64 energy_window_size = 9;`

      Returns:
      :   The energyWindowSize.
    - #### getDelegatedFrozenV2BalanceForEnergy

      ```
      long getDelegatedFrozenV2BalanceForEnergy()
      ```

      `int64 delegated_frozenV2_balance_for_energy = 10;`

      Returns:
      :   The delegatedFrozenV2BalanceForEnergy.
    - #### getAcquiredDelegatedFrozenV2BalanceForEnergy

      ```
      long getAcquiredDelegatedFrozenV2BalanceForEnergy()
      ```

      `int64 acquired_delegated_frozenV2_balance_for_energy = 11;`

      Returns:
      :   The acquiredDelegatedFrozenV2BalanceForEnergy.
    - #### getEnergyWindowOptimized

      ```
      boolean getEnergyWindowOptimized()
      ```

      `bool energy_window_optimized = 12;`

      Returns:
      :   The energyWindowOptimized.