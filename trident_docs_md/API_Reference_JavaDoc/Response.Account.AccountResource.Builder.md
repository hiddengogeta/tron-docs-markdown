

org.tron.trident.proto

## Class Response.Account.AccountResource.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.Account.AccountResource.Builder](../../../../org/tron/trident/proto/Response.Account.AccountResource.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.Account.AccountResource.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.Account.AccountResourceOrBuilder](../../../../org/tron/trident/proto/Response.Account.AccountResourceOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.Account.AccountResource](../../../../org/tron/trident/proto/Response.Account.AccountResource.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.Account.AccountResource.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.AccountResource.Builder>
  implements Response.Account.AccountResourceOrBuilder
  ```

  Protobuf type `protocol.Account.AccountResource`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.Account.AccountResource.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.Account.AccountResource` | `build()` |
    | `Response.Account.AccountResource` | `buildPartial()` |
    | `Response.Account.AccountResource.Builder` | `clear()` |
    | `Response.Account.AccountResource.Builder` | `clearAcquiredDelegatedFrozenBalanceForEnergy()` Frozen balance provided by other accounts to this account |
    | `Response.Account.AccountResource.Builder` | `clearAcquiredDelegatedFrozenV2BalanceForEnergy()` `int64 acquired_delegated_frozenV2_balance_for_energy = 11;` |
    | `Response.Account.AccountResource.Builder` | `clearDelegatedFrozenBalanceForEnergy()` Frozen balances provided to other accounts |
    | `Response.Account.AccountResource.Builder` | `clearDelegatedFrozenV2BalanceForEnergy()` `int64 delegated_frozenV2_balance_for_energy = 10;` |
    | `Response.Account.AccountResource.Builder` | `clearEnergyUsage()` energy resource, get from frozen |
    | `Response.Account.AccountResource.Builder` | `clearEnergyWindowOptimized()` `bool energy_window_optimized = 12;` |
    | `Response.Account.AccountResource.Builder` | `clearEnergyWindowSize()` `int64 energy_window_size = 9;` |
    | `Response.Account.AccountResource.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.Account.AccountResource.Builder` | `clearFrozenBalanceForEnergy()` the frozen balance for energy |
    | `Response.Account.AccountResource.Builder` | `clearLatestConsumeTimeForEnergy()` `int64 latest_consume_time_for_energy = 3;` |
    | `Response.Account.AccountResource.Builder` | `clearLatestExchangeStorageTime()` `int64 latest_exchange_storage_time = 8;` |
    | `Response.Account.AccountResource.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.Account.AccountResource.Builder` | `clearStorageLimit()` storage resource, get from market |
    | `Response.Account.AccountResource.Builder` | `clearStorageUsage()` `int64 storage_usage = 7;` |
    | `Response.Account.AccountResource.Builder` | `clone()` |
    | `long` | `getAcquiredDelegatedFrozenBalanceForEnergy()` Frozen balance provided by other accounts to this account |
    | `long` | `getAcquiredDelegatedFrozenV2BalanceForEnergy()` `int64 acquired_delegated_frozenV2_balance_for_energy = 11;` |
    | `Response.Account.AccountResource` | `getDefaultInstanceForType()` |
    | `long` | `getDelegatedFrozenBalanceForEnergy()` Frozen balances provided to other accounts |
    | `long` | `getDelegatedFrozenV2BalanceForEnergy()` `int64 delegated_frozenV2_balance_for_energy = 10;` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getEnergyUsage()` energy resource, get from frozen |
    | `boolean` | `getEnergyWindowOptimized()` `bool energy_window_optimized = 12;` |
    | `long` | `getEnergyWindowSize()` `int64 energy_window_size = 9;` |
    | `Response.Account.Frozen` | `getFrozenBalanceForEnergy()` the frozen balance for energy |
    | `Response.Account.Frozen.Builder` | `getFrozenBalanceForEnergyBuilder()` the frozen balance for energy |
    | `Response.Account.FrozenOrBuilder` | `getFrozenBalanceForEnergyOrBuilder()` the frozen balance for energy |
    | `long` | `getLatestConsumeTimeForEnergy()` `int64 latest_consume_time_for_energy = 3;` |
    | `long` | `getLatestExchangeStorageTime()` `int64 latest_exchange_storage_time = 8;` |
    | `long` | `getStorageLimit()` storage resource, get from market |
    | `long` | `getStorageUsage()` `int64 storage_usage = 7;` |
    | `boolean` | `hasFrozenBalanceForEnergy()` the frozen balance for energy |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.Account.AccountResource.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.Account.AccountResource.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.Account.AccountResource.Builder` | `mergeFrom(Response.Account.AccountResource other)` |
    | `Response.Account.AccountResource.Builder` | `mergeFrozenBalanceForEnergy(Response.Account.Frozen value)` the frozen balance for energy |
    | `Response.Account.AccountResource.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.Account.AccountResource.Builder` | `setAcquiredDelegatedFrozenBalanceForEnergy(long value)` Frozen balance provided by other accounts to this account |
    | `Response.Account.AccountResource.Builder` | `setAcquiredDelegatedFrozenV2BalanceForEnergy(long value)` `int64 acquired_delegated_frozenV2_balance_for_energy = 11;` |
    | `Response.Account.AccountResource.Builder` | `setDelegatedFrozenBalanceForEnergy(long value)` Frozen balances provided to other accounts |
    | `Response.Account.AccountResource.Builder` | `setDelegatedFrozenV2BalanceForEnergy(long value)` `int64 delegated_frozenV2_balance_for_energy = 10;` |
    | `Response.Account.AccountResource.Builder` | `setEnergyUsage(long value)` energy resource, get from frozen |
    | `Response.Account.AccountResource.Builder` | `setEnergyWindowOptimized(boolean value)` `bool energy_window_optimized = 12;` |
    | `Response.Account.AccountResource.Builder` | `setEnergyWindowSize(long value)` `int64 energy_window_size = 9;` |
    | `Response.Account.AccountResource.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.Account.AccountResource.Builder` | `setFrozenBalanceForEnergy(Response.Account.Frozen.Builder builderForValue)` the frozen balance for energy |
    | `Response.Account.AccountResource.Builder` | `setFrozenBalanceForEnergy(Response.Account.Frozen value)` the frozen balance for energy |
    | `Response.Account.AccountResource.Builder` | `setLatestConsumeTimeForEnergy(long value)` `int64 latest_consume_time_for_energy = 3;` |
    | `Response.Account.AccountResource.Builder` | `setLatestExchangeStorageTime(long value)` `int64 latest_exchange_storage_time = 8;` |
    | `Response.Account.AccountResource.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.Account.AccountResource.Builder` | `setStorageLimit(long value)` storage resource, get from market |
    | `Response.Account.AccountResource.Builder` | `setStorageUsage(long value)` `int64 storage_usage = 7;` |
    | `Response.Account.AccountResource.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

    - ### Methods inherited from class com.google.protobuf.GeneratedMessageV3.Builder

      `getAllFields, getField, getFieldBuilder, getOneofFieldDescriptor, getParentForChildren, getRepeatedField, getRepeatedFieldBuilder, getRepeatedFieldCount, getUnknownFields, getUnknownFieldSetBuilder, hasField, hasOneof, internalGetMapField, internalGetMapFieldReflection, internalGetMutableMapField, internalGetMutableMapFieldReflection, isClean, markClean, mergeUnknownLengthDelimitedField, mergeUnknownVarintField, newBuilderForField, onBuilt, onChanged, parseUnknownField, setUnknownFieldSetBuilder, setUnknownFieldsProto3`
    - ### Methods inherited from class com.google.protobuf.AbstractMessage.Builder

      `findInitializationErrors, getInitializationErrorString, internalMergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, newUninitializedMessageException, toString`
    - ### Methods inherited from class com.google.protobuf.AbstractMessageLite.Builder

      `addAll, addAll, mergeDelimitedFrom, mergeDelimitedFrom, newUninitializedMessageException`
    - ### Methods inherited from class java.lang.Object

      `equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`
    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.Message.Builder

      `mergeDelimitedFrom, mergeDelimitedFrom`

* + ### Method Detail

    - #### getDescriptor

      ```
      public static final com.google.protobuf.Descriptors.Descriptor getDescriptor()
      ```
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.AccountResource.Builder>`
    - #### clear

      ```
      public Response.Account.AccountResource.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.AccountResource.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.AccountResource.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.Account.AccountResource getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.Account.AccountResource build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.Account.AccountResource buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.Account.AccountResource.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.AccountResource.Builder>`
    - #### setField

      ```
      public Response.Account.AccountResource.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.AccountResource.Builder>`
    - #### clearField

      ```
      public Response.Account.AccountResource.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.AccountResource.Builder>`
    - #### clearOneof

      ```
      public Response.Account.AccountResource.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.AccountResource.Builder>`
    - #### setRepeatedField

      ```
      public Response.Account.AccountResource.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                       int index,
                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.AccountResource.Builder>`
    - #### addRepeatedField

      ```
      public Response.Account.AccountResource.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.AccountResource.Builder>`
    - #### mergeFrom

      ```
      public Response.Account.AccountResource.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.Account.AccountResource.Builder>`
    - #### mergeFrom

      ```
      public Response.Account.AccountResource.Builder mergeFrom(Response.Account.AccountResource other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.AccountResource.Builder>`
    - #### mergeFrom

      ```
      public Response.Account.AccountResource.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.Account.AccountResource.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getEnergyUsage

      ```
      public long getEnergyUsage()
      ```

      ```
       energy resource, get from frozen
      ```

      `int64 energy_usage = 1;`

      Specified by:
      :   `getEnergyUsage` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The energyUsage.
    - #### setEnergyUsage

      ```
      public Response.Account.AccountResource.Builder setEnergyUsage(long value)
      ```

      ```
       energy resource, get from frozen
      ```

      `int64 energy_usage = 1;`

      Parameters:
      :   `value` - The energyUsage to set.

      Returns:
      :   This builder for chaining.
    - #### clearEnergyUsage

      ```
      public Response.Account.AccountResource.Builder clearEnergyUsage()
      ```

      ```
       energy resource, get from frozen
      ```

      `int64 energy_usage = 1;`

      Returns:
      :   This builder for chaining.
    - #### hasFrozenBalanceForEnergy

      ```
      public boolean hasFrozenBalanceForEnergy()
      ```

      ```
       the frozen balance for energy
      ```

      `.protocol.Account.Frozen frozen_balance_for_energy = 2;`

      Specified by:
      :   `hasFrozenBalanceForEnergy` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   Whether the frozenBalanceForEnergy field is set.
    - #### getFrozenBalanceForEnergy

      ```
      public Response.Account.Frozen getFrozenBalanceForEnergy()
      ```

      ```
       the frozen balance for energy
      ```

      `.protocol.Account.Frozen frozen_balance_for_energy = 2;`

      Specified by:
      :   `getFrozenBalanceForEnergy` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The frozenBalanceForEnergy.
    - #### setFrozenBalanceForEnergy

      ```
      public Response.Account.AccountResource.Builder setFrozenBalanceForEnergy(Response.Account.Frozen value)
      ```

      ```
       the frozen balance for energy
      ```

      `.protocol.Account.Frozen frozen_balance_for_energy = 2;`
    - #### setFrozenBalanceForEnergy

      ```
      public Response.Account.AccountResource.Builder setFrozenBalanceForEnergy(Response.Account.Frozen.Builder builderForValue)
      ```

      ```
       the frozen balance for energy
      ```

      `.protocol.Account.Frozen frozen_balance_for_energy = 2;`
    - #### mergeFrozenBalanceForEnergy

      ```
      public Response.Account.AccountResource.Builder mergeFrozenBalanceForEnergy(Response.Account.Frozen value)
      ```

      ```
       the frozen balance for energy
      ```

      `.protocol.Account.Frozen frozen_balance_for_energy = 2;`
    - #### clearFrozenBalanceForEnergy

      ```
      public Response.Account.AccountResource.Builder clearFrozenBalanceForEnergy()
      ```

      ```
       the frozen balance for energy
      ```

      `.protocol.Account.Frozen frozen_balance_for_energy = 2;`
    - #### getFrozenBalanceForEnergyBuilder

      ```
      public Response.Account.Frozen.Builder getFrozenBalanceForEnergyBuilder()
      ```

      ```
       the frozen balance for energy
      ```

      `.protocol.Account.Frozen frozen_balance_for_energy = 2;`
    - #### getFrozenBalanceForEnergyOrBuilder

      ```
      public Response.Account.FrozenOrBuilder getFrozenBalanceForEnergyOrBuilder()
      ```

      ```
       the frozen balance for energy
      ```

      `.protocol.Account.Frozen frozen_balance_for_energy = 2;`

      Specified by:
      :   `getFrozenBalanceForEnergyOrBuilder` in interface `Response.Account.AccountResourceOrBuilder`
    - #### getLatestConsumeTimeForEnergy

      ```
      public long getLatestConsumeTimeForEnergy()
      ```

      `int64 latest_consume_time_for_energy = 3;`

      Specified by:
      :   `getLatestConsumeTimeForEnergy` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The latestConsumeTimeForEnergy.
    - #### setLatestConsumeTimeForEnergy

      ```
      public Response.Account.AccountResource.Builder setLatestConsumeTimeForEnergy(long value)
      ```

      `int64 latest_consume_time_for_energy = 3;`

      Parameters:
      :   `value` - The latestConsumeTimeForEnergy to set.

      Returns:
      :   This builder for chaining.
    - #### clearLatestConsumeTimeForEnergy

      ```
      public Response.Account.AccountResource.Builder clearLatestConsumeTimeForEnergy()
      ```

      `int64 latest_consume_time_for_energy = 3;`

      Returns:
      :   This builder for chaining.
    - #### getAcquiredDelegatedFrozenBalanceForEnergy

      ```
      public long getAcquiredDelegatedFrozenBalanceForEnergy()
      ```

      ```
       Frozen balance provided by other accounts to this account
      ```

      `int64 acquired_delegated_frozen_balance_for_energy = 4;`

      Specified by:
      :   `getAcquiredDelegatedFrozenBalanceForEnergy` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The acquiredDelegatedFrozenBalanceForEnergy.
    - #### setAcquiredDelegatedFrozenBalanceForEnergy

      ```
      public Response.Account.AccountResource.Builder setAcquiredDelegatedFrozenBalanceForEnergy(long value)
      ```

      ```
       Frozen balance provided by other accounts to this account
      ```

      `int64 acquired_delegated_frozen_balance_for_energy = 4;`

      Parameters:
      :   `value` - The acquiredDelegatedFrozenBalanceForEnergy to set.

      Returns:
      :   This builder for chaining.
    - #### clearAcquiredDelegatedFrozenBalanceForEnergy

      ```
      public Response.Account.AccountResource.Builder clearAcquiredDelegatedFrozenBalanceForEnergy()
      ```

      ```
       Frozen balance provided by other accounts to this account
      ```

      `int64 acquired_delegated_frozen_balance_for_energy = 4;`

      Returns:
      :   This builder for chaining.
    - #### getDelegatedFrozenBalanceForEnergy

      ```
      public long getDelegatedFrozenBalanceForEnergy()
      ```

      ```
       Frozen balances provided to other accounts
      ```

      `int64 delegated_frozen_balance_for_energy = 5;`

      Specified by:
      :   `getDelegatedFrozenBalanceForEnergy` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The delegatedFrozenBalanceForEnergy.
    - #### setDelegatedFrozenBalanceForEnergy

      ```
      public Response.Account.AccountResource.Builder setDelegatedFrozenBalanceForEnergy(long value)
      ```

      ```
       Frozen balances provided to other accounts
      ```

      `int64 delegated_frozen_balance_for_energy = 5;`

      Parameters:
      :   `value` - The delegatedFrozenBalanceForEnergy to set.

      Returns:
      :   This builder for chaining.
    - #### clearDelegatedFrozenBalanceForEnergy

      ```
      public Response.Account.AccountResource.Builder clearDelegatedFrozenBalanceForEnergy()
      ```

      ```
       Frozen balances provided to other accounts
      ```

      `int64 delegated_frozen_balance_for_energy = 5;`

      Returns:
      :   This builder for chaining.
    - #### getStorageLimit

      ```
      public long getStorageLimit()
      ```

      ```
       storage resource, get from market
      ```

      `int64 storage_limit = 6;`

      Specified by:
      :   `getStorageLimit` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The storageLimit.
    - #### setStorageLimit

      ```
      public Response.Account.AccountResource.Builder setStorageLimit(long value)
      ```

      ```
       storage resource, get from market
      ```

      `int64 storage_limit = 6;`

      Parameters:
      :   `value` - The storageLimit to set.

      Returns:
      :   This builder for chaining.
    - #### clearStorageLimit

      ```
      public Response.Account.AccountResource.Builder clearStorageLimit()
      ```

      ```
       storage resource, get from market
      ```

      `int64 storage_limit = 6;`

      Returns:
      :   This builder for chaining.
    - #### getStorageUsage

      ```
      public long getStorageUsage()
      ```

      `int64 storage_usage = 7;`

      Specified by:
      :   `getStorageUsage` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The storageUsage.
    - #### setStorageUsage

      ```
      public Response.Account.AccountResource.Builder setStorageUsage(long value)
      ```

      `int64 storage_usage = 7;`

      Parameters:
      :   `value` - The storageUsage to set.

      Returns:
      :   This builder for chaining.
    - #### clearStorageUsage

      ```
      public Response.Account.AccountResource.Builder clearStorageUsage()
      ```

      `int64 storage_usage = 7;`

      Returns:
      :   This builder for chaining.
    - #### getLatestExchangeStorageTime

      ```
      public long getLatestExchangeStorageTime()
      ```

      `int64 latest_exchange_storage_time = 8;`

      Specified by:
      :   `getLatestExchangeStorageTime` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The latestExchangeStorageTime.
    - #### setLatestExchangeStorageTime

      ```
      public Response.Account.AccountResource.Builder setLatestExchangeStorageTime(long value)
      ```

      `int64 latest_exchange_storage_time = 8;`

      Parameters:
      :   `value` - The latestExchangeStorageTime to set.

      Returns:
      :   This builder for chaining.
    - #### clearLatestExchangeStorageTime

      ```
      public Response.Account.AccountResource.Builder clearLatestExchangeStorageTime()
      ```

      `int64 latest_exchange_storage_time = 8;`

      Returns:
      :   This builder for chaining.
    - #### getEnergyWindowSize

      ```
      public long getEnergyWindowSize()
      ```

      `int64 energy_window_size = 9;`

      Specified by:
      :   `getEnergyWindowSize` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The energyWindowSize.
    - #### setEnergyWindowSize

      ```
      public Response.Account.AccountResource.Builder setEnergyWindowSize(long value)
      ```

      `int64 energy_window_size = 9;`

      Parameters:
      :   `value` - The energyWindowSize to set.

      Returns:
      :   This builder for chaining.
    - #### clearEnergyWindowSize

      ```
      public Response.Account.AccountResource.Builder clearEnergyWindowSize()
      ```

      `int64 energy_window_size = 9;`

      Returns:
      :   This builder for chaining.
    - #### getDelegatedFrozenV2BalanceForEnergy

      ```
      public long getDelegatedFrozenV2BalanceForEnergy()
      ```

      `int64 delegated_frozenV2_balance_for_energy = 10;`

      Specified by:
      :   `getDelegatedFrozenV2BalanceForEnergy` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The delegatedFrozenV2BalanceForEnergy.
    - #### setDelegatedFrozenV2BalanceForEnergy

      ```
      public Response.Account.AccountResource.Builder setDelegatedFrozenV2BalanceForEnergy(long value)
      ```

      `int64 delegated_frozenV2_balance_for_energy = 10;`

      Parameters:
      :   `value` - The delegatedFrozenV2BalanceForEnergy to set.

      Returns:
      :   This builder for chaining.
    - #### clearDelegatedFrozenV2BalanceForEnergy

      ```
      public Response.Account.AccountResource.Builder clearDelegatedFrozenV2BalanceForEnergy()
      ```

      `int64 delegated_frozenV2_balance_for_energy = 10;`

      Returns:
      :   This builder for chaining.
    - #### getAcquiredDelegatedFrozenV2BalanceForEnergy

      ```
      public long getAcquiredDelegatedFrozenV2BalanceForEnergy()
      ```

      `int64 acquired_delegated_frozenV2_balance_for_energy = 11;`

      Specified by:
      :   `getAcquiredDelegatedFrozenV2BalanceForEnergy` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The acquiredDelegatedFrozenV2BalanceForEnergy.
    - #### setAcquiredDelegatedFrozenV2BalanceForEnergy

      ```
      public Response.Account.AccountResource.Builder setAcquiredDelegatedFrozenV2BalanceForEnergy(long value)
      ```

      `int64 acquired_delegated_frozenV2_balance_for_energy = 11;`

      Parameters:
      :   `value` - The acquiredDelegatedFrozenV2BalanceForEnergy to set.

      Returns:
      :   This builder for chaining.
    - #### clearAcquiredDelegatedFrozenV2BalanceForEnergy

      ```
      public Response.Account.AccountResource.Builder clearAcquiredDelegatedFrozenV2BalanceForEnergy()
      ```

      `int64 acquired_delegated_frozenV2_balance_for_energy = 11;`

      Returns:
      :   This builder for chaining.
    - #### getEnergyWindowOptimized

      ```
      public boolean getEnergyWindowOptimized()
      ```

      `bool energy_window_optimized = 12;`

      Specified by:
      :   `getEnergyWindowOptimized` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The energyWindowOptimized.
    - #### setEnergyWindowOptimized

      ```
      public Response.Account.AccountResource.Builder setEnergyWindowOptimized(boolean value)
      ```

      `bool energy_window_optimized = 12;`

      Parameters:
      :   `value` - The energyWindowOptimized to set.

      Returns:
      :   This builder for chaining.
    - #### clearEnergyWindowOptimized

      ```
      public Response.Account.AccountResource.Builder clearEnergyWindowOptimized()
      ```

      `bool energy_window_optimized = 12;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.Account.AccountResource.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.AccountResource.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.Account.AccountResource.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.AccountResource.Builder>`