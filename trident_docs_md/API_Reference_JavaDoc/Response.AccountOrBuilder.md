

org.tron.trident.proto

## Interface Response.AccountOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.Account](../../../../org/tron/trident/proto/Response.Account.html "class in org.tron.trident.proto"), [Response.Account.Builder](../../../../org/tron/trident/proto/Response.Account.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.AccountOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `boolean` | `containsAsset(java.lang.String key)` the other asset owned by this account |
    | `boolean` | `containsAssetV2(java.lang.String key)` the other asset owned by this account，key is assetId |
    | `boolean` | `containsFreeAssetNetUsage(java.lang.String key)` `map<string, int64> free_asset_net_usage = 20;` |
    | `boolean` | `containsFreeAssetNetUsageV2(java.lang.String key)` `map<string, int64> free_asset_net_usageV2 = 59;` |
    | `boolean` | `containsLatestAssetOperationTime(java.lang.String key)` `map<string, int64> latest_asset_operation_time = 18;` |
    | `boolean` | `containsLatestAssetOperationTimeV2(java.lang.String key)` `map<string, int64> latest_asset_operation_timeV2 = 58;` |
    | `com.google.protobuf.ByteString` | `getAccountId()` the identity of this account, case insensitive |
    | `com.google.protobuf.ByteString` | `getAccountName()` account nick name |
    | `Response.Account.AccountResource` | `getAccountResource()` `.protocol.Account.AccountResource account_resource = 26;` |
    | `Response.Account.AccountResourceOrBuilder` | `getAccountResourceOrBuilder()` `.protocol.Account.AccountResource account_resource = 26;` |
    | `long` | `getAcquiredDelegatedFrozenBalanceForBandwidth()` Frozen balance provided by other accounts to this account |
    | `long` | `getAcquiredDelegatedFrozenV2BalanceForBandwidth()` `int64 acquired_delegated_frozenV2_balance_for_bandwidth = 37;` |
    | `Common.Permission` | `getActivePermission(int index)` `repeated .protocol.Permission active_permission = 33;` |
    | `int` | `getActivePermissionCount()` `repeated .protocol.Permission active_permission = 33;` |
    | `java.util.List<Common.Permission>` | `getActivePermissionList()` `repeated .protocol.Permission active_permission = 33;` |
    | `Common.PermissionOrBuilder` | `getActivePermissionOrBuilder(int index)` `repeated .protocol.Permission active_permission = 33;` |
    | `java.util.List<? extends Common.PermissionOrBuilder>` | `getActivePermissionOrBuilderList()` `repeated .protocol.Permission active_permission = 33;` |
    | `com.google.protobuf.ByteString` | `getAddress()` the create address |
    | `long` | `getAllowance()` witness block producing allowance |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getAsset()` Deprecated. |
    | `int` | `getAssetCount()` the other asset owned by this account |
    | `com.google.protobuf.ByteString` | `getAssetIssuedID()` `bytes asset_issued_ID = 57;` |
    | `com.google.protobuf.ByteString` | `getAssetIssuedName()` asset\_issued\_name |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getAssetMap()` the other asset owned by this account |
    | `boolean` | `getAssetOptimized()` `bool asset_optimized = 60;` |
    | `long` | `getAssetOrDefault(java.lang.String key, long defaultValue)` the other asset owned by this account |
    | `long` | `getAssetOrThrow(java.lang.String key)` the other asset owned by this account |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getAssetV2()` Deprecated. |
    | `int` | `getAssetV2Count()` the other asset owned by this account，key is assetId |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getAssetV2Map()` the other asset owned by this account，key is assetId |
    | `long` | `getAssetV2OrDefault(java.lang.String key, long defaultValue)` the other asset owned by this account，key is assetId |
    | `long` | `getAssetV2OrThrow(java.lang.String key)` the other asset owned by this account，key is assetId |
    | `long` | `getBalance()` the trx balance |
    | `com.google.protobuf.ByteString` | `getCode()` not used so far |
    | `com.google.protobuf.ByteString` | `getCodeHash()` `bytes codeHash = 30;` |
    | `long` | `getCreateTime()` this account create time |
    | `long` | `getDelegatedFrozenBalanceForBandwidth()` Freeze and provide balances to other accounts |
    | `long` | `getDelegatedFrozenV2BalanceForBandwidth()` `int64 delegated_frozenV2_balance_for_bandwidth = 36;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getFreeAssetNetUsage()` Deprecated. |
    | `int` | `getFreeAssetNetUsageCount()` `map<string, int64> free_asset_net_usage = 20;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getFreeAssetNetUsageMap()` `map<string, int64> free_asset_net_usage = 20;` |
    | `long` | `getFreeAssetNetUsageOrDefault(java.lang.String key, long defaultValue)` `map<string, int64> free_asset_net_usage = 20;` |
    | `long` | `getFreeAssetNetUsageOrThrow(java.lang.String key)` `map<string, int64> free_asset_net_usage = 20;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getFreeAssetNetUsageV2()` Deprecated. |
    | `int` | `getFreeAssetNetUsageV2Count()` `map<string, int64> free_asset_net_usageV2 = 59;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getFreeAssetNetUsageV2Map()` `map<string, int64> free_asset_net_usageV2 = 59;` |
    | `long` | `getFreeAssetNetUsageV2OrDefault(java.lang.String key, long defaultValue)` `map<string, int64> free_asset_net_usageV2 = 59;` |
    | `long` | `getFreeAssetNetUsageV2OrThrow(java.lang.String key)` `map<string, int64> free_asset_net_usageV2 = 59;` |
    | `long` | `getFreeNetUsage()` `int64 free_net_usage = 19;` |
    | `Response.Account.Frozen` | `getFrozen(int index)` the frozen balance for bandwidth |
    | `int` | `getFrozenCount()` the frozen balance for bandwidth |
    | `java.util.List<Response.Account.Frozen>` | `getFrozenList()` the frozen balance for bandwidth |
    | `Response.Account.FrozenOrBuilder` | `getFrozenOrBuilder(int index)` the frozen balance for bandwidth |
    | `java.util.List<? extends Response.Account.FrozenOrBuilder>` | `getFrozenOrBuilderList()` the frozen balance for bandwidth |
    | `Response.Account.Frozen` | `getFrozenSupply(int index)` frozen asset(for asset issuer) |
    | `int` | `getFrozenSupplyCount()` frozen asset(for asset issuer) |
    | `java.util.List<Response.Account.Frozen>` | `getFrozenSupplyList()` frozen asset(for asset issuer) |
    | `Response.Account.FrozenOrBuilder` | `getFrozenSupplyOrBuilder(int index)` frozen asset(for asset issuer) |
    | `java.util.List<? extends Response.Account.FrozenOrBuilder>` | `getFrozenSupplyOrBuilderList()` frozen asset(for asset issuer) |
    | `Response.Account.FreezeV2` | `getFrozenV2(int index)` `repeated .protocol.Account.FreezeV2 frozenV2 = 34;` |
    | `int` | `getFrozenV2Count()` `repeated .protocol.Account.FreezeV2 frozenV2 = 34;` |
    | `java.util.List<Response.Account.FreezeV2>` | `getFrozenV2List()` `repeated .protocol.Account.FreezeV2 frozenV2 = 34;` |
    | `Response.Account.FreezeV2OrBuilder` | `getFrozenV2OrBuilder(int index)` `repeated .protocol.Account.FreezeV2 frozenV2 = 34;` |
    | `java.util.List<? extends Response.Account.FreezeV2OrBuilder>` | `getFrozenV2OrBuilderList()` `repeated .protocol.Account.FreezeV2 frozenV2 = 34;` |
    | `boolean` | `getIsCommittee()` `bool is_committee = 15;` |
    | `boolean` | `getIsWitness()` `bool is_witness = 14;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getLatestAssetOperationTime()` Deprecated. |
    | `int` | `getLatestAssetOperationTimeCount()` `map<string, int64> latest_asset_operation_time = 18;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getLatestAssetOperationTimeMap()` `map<string, int64> latest_asset_operation_time = 18;` |
    | `long` | `getLatestAssetOperationTimeOrDefault(java.lang.String key, long defaultValue)` `map<string, int64> latest_asset_operation_time = 18;` |
    | `long` | `getLatestAssetOperationTimeOrThrow(java.lang.String key)` `map<string, int64> latest_asset_operation_time = 18;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getLatestAssetOperationTimeV2()` Deprecated. |
    | `int` | `getLatestAssetOperationTimeV2Count()` `map<string, int64> latest_asset_operation_timeV2 = 58;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getLatestAssetOperationTimeV2Map()` `map<string, int64> latest_asset_operation_timeV2 = 58;` |
    | `long` | `getLatestAssetOperationTimeV2OrDefault(java.lang.String key, long defaultValue)` `map<string, int64> latest_asset_operation_timeV2 = 58;` |
    | `long` | `getLatestAssetOperationTimeV2OrThrow(java.lang.String key)` `map<string, int64> latest_asset_operation_timeV2 = 58;` |
    | `long` | `getLatestConsumeFreeTime()` `int64 latest_consume_free_time = 22;` |
    | `long` | `getLatestConsumeTime()` `int64 latest_consume_time = 21;` |
    | `long` | `getLatestOprationTime()` this last operation time, including transfer, voting and so on. |
    | `long` | `getLatestWithdrawTime()` last withdraw time |
    | `long` | `getNetUsage()` bandwidth, get from frozen |
    | `boolean` | `getNetWindowOptimized()` `bool net_window_optimized = 25;` |
    | `long` | `getNetWindowSize()` `int64 net_window_size = 24;` |
    | `long` | `getOldTronPower()` `int64 old_tron_power = 46;` |
    | `Common.Permission` | `getOwnerPermission()` `.protocol.Permission owner_permission = 31;` |
    | `Common.PermissionOrBuilder` | `getOwnerPermissionOrBuilder()` `.protocol.Permission owner_permission = 31;` |
    | `Response.Account.Frozen` | `getTronPower()` `.protocol.Account.Frozen tron_power = 47;` |
    | `Response.Account.FrozenOrBuilder` | `getTronPowerOrBuilder()` `.protocol.Account.Frozen tron_power = 47;` |
    | `Common.AccountType` | `getType()` `.protocol.AccountType type = 2;` |
    | `int` | `getTypeValue()` `.protocol.AccountType type = 2;` |
    | `Response.Account.UnFreezeV2` | `getUnfrozenV2(int index)` `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;` |
    | `int` | `getUnfrozenV2Count()` `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;` |
    | `java.util.List<Response.Account.UnFreezeV2>` | `getUnfrozenV2List()` `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;` |
    | `Response.Account.UnFreezeV2OrBuilder` | `getUnfrozenV2OrBuilder(int index)` `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;` |
    | `java.util.List<? extends Response.Account.UnFreezeV2OrBuilder>` | `getUnfrozenV2OrBuilderList()` `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;` |
    | `Common.Vote` | `getVotes(int index)` the votes |
    | `int` | `getVotesCount()` the votes |
    | `java.util.List<Common.Vote>` | `getVotesList()` the votes |
    | `Common.VoteOrBuilder` | `getVotesOrBuilder(int index)` the votes |
    | `java.util.List<? extends Common.VoteOrBuilder>` | `getVotesOrBuilderList()` the votes |
    | `Common.Permission` | `getWitnessPermission()` `.protocol.Permission witness_permission = 32;` |
    | `Common.PermissionOrBuilder` | `getWitnessPermissionOrBuilder()` `.protocol.Permission witness_permission = 32;` |
    | `boolean` | `hasAccountResource()` `.protocol.Account.AccountResource account_resource = 26;` |
    | `boolean` | `hasOwnerPermission()` `.protocol.Permission owner_permission = 31;` |
    | `boolean` | `hasTronPower()` `.protocol.Account.Frozen tron_power = 47;` |
    | `boolean` | `hasWitnessPermission()` `.protocol.Permission witness_permission = 32;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getAccountName

      ```
      com.google.protobuf.ByteString getAccountName()
      ```

      ```
       account nick name
      ```

      `bytes account_name = 1;`

      Returns:
      :   The accountName.
    - #### getTypeValue

      ```
      int getTypeValue()
      ```

      `.protocol.AccountType type = 2;`

      Returns:
      :   The enum numeric value on the wire for type.
    - #### getType

      ```
      Common.AccountType getType()
      ```

      `.protocol.AccountType type = 2;`

      Returns:
      :   The type.
    - #### getAddress

      ```
      com.google.protobuf.ByteString getAddress()
      ```

      ```
       the create address
      ```

      `bytes address = 3;`

      Returns:
      :   The address.
    - #### getBalance

      ```
      long getBalance()
      ```

      ```
       the trx balance
      ```

      `int64 balance = 4;`

      Returns:
      :   The balance.
    - #### getVotesList

      ```
      java.util.List<Common.Vote> getVotesList()
      ```

      ```
       the votes
      ```

      `repeated .protocol.Vote votes = 5;`
    - #### getVotes

      ```
      Common.Vote getVotes(int index)
      ```

      ```
       the votes
      ```

      `repeated .protocol.Vote votes = 5;`
    - #### getVotesCount

      ```
      int getVotesCount()
      ```

      ```
       the votes
      ```

      `repeated .protocol.Vote votes = 5;`
    - #### getVotesOrBuilderList

      ```
      java.util.List<? extends Common.VoteOrBuilder> getVotesOrBuilderList()
      ```

      ```
       the votes
      ```

      `repeated .protocol.Vote votes = 5;`
    - #### getVotesOrBuilder

      ```
      Common.VoteOrBuilder getVotesOrBuilder(int index)
      ```

      ```
       the votes
      ```

      `repeated .protocol.Vote votes = 5;`
    - #### getAssetCount

      ```
      int getAssetCount()
      ```

      ```
       the other asset owned by this account
      ```

      `map<string, int64> asset = 6;`
    - #### containsAsset

      ```
      boolean containsAsset(java.lang.String key)
      ```

      ```
       the other asset owned by this account
      ```

      `map<string, int64> asset = 6;`
    - #### getAsset

      ```
      @Deprecated
      java.util.Map<java.lang.String,java.lang.Long> getAsset()
      ```

      Deprecated.

      Use [`getAssetMap()`](../../../../org/tron/trident/proto/Response.AccountOrBuilder.html#getAssetMap--) instead.
    - #### getAssetMap

      ```
      java.util.Map<java.lang.String,java.lang.Long> getAssetMap()
      ```

      ```
       the other asset owned by this account
      ```

      `map<string, int64> asset = 6;`
    - #### getAssetOrDefault

      ```
      long getAssetOrDefault(java.lang.String key,
                             long defaultValue)
      ```

      ```
       the other asset owned by this account
      ```

      `map<string, int64> asset = 6;`
    - #### getAssetOrThrow

      ```
      long getAssetOrThrow(java.lang.String key)
      ```

      ```
       the other asset owned by this account
      ```

      `map<string, int64> asset = 6;`
    - #### getAssetV2Count

      ```
      int getAssetV2Count()
      ```

      ```
       the other asset owned by this account，key is assetId
      ```

      `map<string, int64> assetV2 = 56;`
    - #### containsAssetV2

      ```
      boolean containsAssetV2(java.lang.String key)
      ```

      ```
       the other asset owned by this account，key is assetId
      ```

      `map<string, int64> assetV2 = 56;`
    - #### getAssetV2

      ```
      @Deprecated
      java.util.Map<java.lang.String,java.lang.Long> getAssetV2()
      ```

      Deprecated.

      Use [`getAssetV2Map()`](../../../../org/tron/trident/proto/Response.AccountOrBuilder.html#getAssetV2Map--) instead.
    - #### getAssetV2Map

      ```
      java.util.Map<java.lang.String,java.lang.Long> getAssetV2Map()
      ```

      ```
       the other asset owned by this account，key is assetId
      ```

      `map<string, int64> assetV2 = 56;`
    - #### getAssetV2OrDefault

      ```
      long getAssetV2OrDefault(java.lang.String key,
                               long defaultValue)
      ```

      ```
       the other asset owned by this account，key is assetId
      ```

      `map<string, int64> assetV2 = 56;`
    - #### getAssetV2OrThrow

      ```
      long getAssetV2OrThrow(java.lang.String key)
      ```

      ```
       the other asset owned by this account，key is assetId
      ```

      `map<string, int64> assetV2 = 56;`
    - #### getFrozenList

      ```
      java.util.List<Response.Account.Frozen> getFrozenList()
      ```

      ```
       the frozen balance for bandwidth
      ```

      `repeated .protocol.Account.Frozen frozen = 7;`
    - #### getFrozen

      ```
      Response.Account.Frozen getFrozen(int index)
      ```

      ```
       the frozen balance for bandwidth
      ```

      `repeated .protocol.Account.Frozen frozen = 7;`
    - #### getFrozenCount

      ```
      int getFrozenCount()
      ```

      ```
       the frozen balance for bandwidth
      ```

      `repeated .protocol.Account.Frozen frozen = 7;`
    - #### getFrozenOrBuilderList

      ```
      java.util.List<? extends Response.Account.FrozenOrBuilder> getFrozenOrBuilderList()
      ```

      ```
       the frozen balance for bandwidth
      ```

      `repeated .protocol.Account.Frozen frozen = 7;`
    - #### getFrozenOrBuilder

      ```
      Response.Account.FrozenOrBuilder getFrozenOrBuilder(int index)
      ```

      ```
       the frozen balance for bandwidth
      ```

      `repeated .protocol.Account.Frozen frozen = 7;`
    - #### getNetUsage

      ```
      long getNetUsage()
      ```

      ```
       bandwidth, get from frozen
      ```

      `int64 net_usage = 8;`

      Returns:
      :   The netUsage.
    - #### getAcquiredDelegatedFrozenBalanceForBandwidth

      ```
      long getAcquiredDelegatedFrozenBalanceForBandwidth()
      ```

      ```
       Frozen balance provided by other accounts to this account
      ```

      `int64 acquired_delegated_frozen_balance_for_bandwidth = 41;`

      Returns:
      :   The acquiredDelegatedFrozenBalanceForBandwidth.
    - #### getDelegatedFrozenBalanceForBandwidth

      ```
      long getDelegatedFrozenBalanceForBandwidth()
      ```

      ```
       Freeze and provide balances to other accounts
      ```

      `int64 delegated_frozen_balance_for_bandwidth = 42;`

      Returns:
      :   The delegatedFrozenBalanceForBandwidth.
    - #### getOldTronPower

      ```
      long getOldTronPower()
      ```

      `int64 old_tron_power = 46;`

      Returns:
      :   The oldTronPower.
    - #### hasTronPower

      ```
      boolean hasTronPower()
      ```

      `.protocol.Account.Frozen tron_power = 47;`

      Returns:
      :   Whether the tronPower field is set.
    - #### getTronPower

      ```
      Response.Account.Frozen getTronPower()
      ```

      `.protocol.Account.Frozen tron_power = 47;`

      Returns:
      :   The tronPower.
    - #### getTronPowerOrBuilder

      ```
      Response.Account.FrozenOrBuilder getTronPowerOrBuilder()
      ```

      `.protocol.Account.Frozen tron_power = 47;`
    - #### getAssetOptimized

      ```
      boolean getAssetOptimized()
      ```

      `bool asset_optimized = 60;`

      Returns:
      :   The assetOptimized.
    - #### getCreateTime

      ```
      long getCreateTime()
      ```

      ```
       this account create time
      ```

      `int64 create_time = 9;`

      Returns:
      :   The createTime.
    - #### getLatestOprationTime

      ```
      long getLatestOprationTime()
      ```

      ```
       this last operation time, including transfer, voting and so on. //FIXME fix
       grammar
      ```

      `int64 latest_opration_time = 10;`

      Returns:
      :   The latestOprationTime.
    - #### getAllowance

      ```
      long getAllowance()
      ```

      ```
       witness block producing allowance
      ```

      `int64 allowance = 11;`

      Returns:
      :   The allowance.
    - #### getLatestWithdrawTime

      ```
      long getLatestWithdrawTime()
      ```

      ```
       last withdraw time
      ```

      `int64 latest_withdraw_time = 12;`

      Returns:
      :   The latestWithdrawTime.
    - #### getCode

      ```
      com.google.protobuf.ByteString getCode()
      ```

      ```
       not used so far
      ```

      `bytes code = 13;`

      Returns:
      :   The code.
    - #### getIsWitness

      ```
      boolean getIsWitness()
      ```

      `bool is_witness = 14;`

      Returns:
      :   The isWitness.
    - #### getIsCommittee

      ```
      boolean getIsCommittee()
      ```

      `bool is_committee = 15;`

      Returns:
      :   The isCommittee.
    - #### getFrozenSupplyList

      ```
      java.util.List<Response.Account.Frozen> getFrozenSupplyList()
      ```

      ```
       frozen asset(for asset issuer)
      ```

      `repeated .protocol.Account.Frozen frozen_supply = 16;`
    - #### getFrozenSupply

      ```
      Response.Account.Frozen getFrozenSupply(int index)
      ```

      ```
       frozen asset(for asset issuer)
      ```

      `repeated .protocol.Account.Frozen frozen_supply = 16;`
    - #### getFrozenSupplyCount

      ```
      int getFrozenSupplyCount()
      ```

      ```
       frozen asset(for asset issuer)
      ```

      `repeated .protocol.Account.Frozen frozen_supply = 16;`
    - #### getFrozenSupplyOrBuilderList

      ```
      java.util.List<? extends Response.Account.FrozenOrBuilder> getFrozenSupplyOrBuilderList()
      ```

      ```
       frozen asset(for asset issuer)
      ```

      `repeated .protocol.Account.Frozen frozen_supply = 16;`
    - #### getFrozenSupplyOrBuilder

      ```
      Response.Account.FrozenOrBuilder getFrozenSupplyOrBuilder(int index)
      ```

      ```
       frozen asset(for asset issuer)
      ```

      `repeated .protocol.Account.Frozen frozen_supply = 16;`
    - #### getAssetIssuedName

      ```
      com.google.protobuf.ByteString getAssetIssuedName()
      ```

      ```
       asset_issued_name
      ```

      `bytes asset_issued_name = 17;`

      Returns:
      :   The assetIssuedName.
    - #### getAssetIssuedID

      ```
      com.google.protobuf.ByteString getAssetIssuedID()
      ```

      `bytes asset_issued_ID = 57;`

      Returns:
      :   The assetIssuedID.
    - #### getLatestAssetOperationTimeCount

      ```
      int getLatestAssetOperationTimeCount()
      ```

      `map<string, int64> latest_asset_operation_time = 18;`
    - #### containsLatestAssetOperationTime

      ```
      boolean containsLatestAssetOperationTime(java.lang.String key)
      ```

      `map<string, int64> latest_asset_operation_time = 18;`
    - #### getLatestAssetOperationTime

      ```
      @Deprecated
      java.util.Map<java.lang.String,java.lang.Long> getLatestAssetOperationTime()
      ```

      Deprecated.

      Use [`getLatestAssetOperationTimeMap()`](../../../../org/tron/trident/proto/Response.AccountOrBuilder.html#getLatestAssetOperationTimeMap--) instead.
    - #### getLatestAssetOperationTimeMap

      ```
      java.util.Map<java.lang.String,java.lang.Long> getLatestAssetOperationTimeMap()
      ```

      `map<string, int64> latest_asset_operation_time = 18;`
    - #### getLatestAssetOperationTimeOrDefault

      ```
      long getLatestAssetOperationTimeOrDefault(java.lang.String key,
                                                long defaultValue)
      ```

      `map<string, int64> latest_asset_operation_time = 18;`
    - #### getLatestAssetOperationTimeOrThrow

      ```
      long getLatestAssetOperationTimeOrThrow(java.lang.String key)
      ```

      `map<string, int64> latest_asset_operation_time = 18;`
    - #### getLatestAssetOperationTimeV2Count

      ```
      int getLatestAssetOperationTimeV2Count()
      ```

      `map<string, int64> latest_asset_operation_timeV2 = 58;`
    - #### containsLatestAssetOperationTimeV2

      ```
      boolean containsLatestAssetOperationTimeV2(java.lang.String key)
      ```

      `map<string, int64> latest_asset_operation_timeV2 = 58;`
    - #### getLatestAssetOperationTimeV2

      ```
      @Deprecated
      java.util.Map<java.lang.String,java.lang.Long> getLatestAssetOperationTimeV2()
      ```

      Deprecated.

      Use [`getLatestAssetOperationTimeV2Map()`](../../../../org/tron/trident/proto/Response.AccountOrBuilder.html#getLatestAssetOperationTimeV2Map--) instead.
    - #### getLatestAssetOperationTimeV2Map

      ```
      java.util.Map<java.lang.String,java.lang.Long> getLatestAssetOperationTimeV2Map()
      ```

      `map<string, int64> latest_asset_operation_timeV2 = 58;`
    - #### getLatestAssetOperationTimeV2OrDefault

      ```
      long getLatestAssetOperationTimeV2OrDefault(java.lang.String key,
                                                  long defaultValue)
      ```

      `map<string, int64> latest_asset_operation_timeV2 = 58;`
    - #### getLatestAssetOperationTimeV2OrThrow

      ```
      long getLatestAssetOperationTimeV2OrThrow(java.lang.String key)
      ```

      `map<string, int64> latest_asset_operation_timeV2 = 58;`
    - #### getFreeNetUsage

      ```
      long getFreeNetUsage()
      ```

      `int64 free_net_usage = 19;`

      Returns:
      :   The freeNetUsage.
    - #### getFreeAssetNetUsageCount

      ```
      int getFreeAssetNetUsageCount()
      ```

      `map<string, int64> free_asset_net_usage = 20;`
    - #### containsFreeAssetNetUsage

      ```
      boolean containsFreeAssetNetUsage(java.lang.String key)
      ```

      `map<string, int64> free_asset_net_usage = 20;`
    - #### getFreeAssetNetUsage

      ```
      @Deprecated
      java.util.Map<java.lang.String,java.lang.Long> getFreeAssetNetUsage()
      ```

      Deprecated.

      Use [`getFreeAssetNetUsageMap()`](../../../../org/tron/trident/proto/Response.AccountOrBuilder.html#getFreeAssetNetUsageMap--) instead.
    - #### getFreeAssetNetUsageMap

      ```
      java.util.Map<java.lang.String,java.lang.Long> getFreeAssetNetUsageMap()
      ```

      `map<string, int64> free_asset_net_usage = 20;`
    - #### getFreeAssetNetUsageOrDefault

      ```
      long getFreeAssetNetUsageOrDefault(java.lang.String key,
                                         long defaultValue)
      ```

      `map<string, int64> free_asset_net_usage = 20;`
    - #### getFreeAssetNetUsageOrThrow

      ```
      long getFreeAssetNetUsageOrThrow(java.lang.String key)
      ```

      `map<string, int64> free_asset_net_usage = 20;`
    - #### getFreeAssetNetUsageV2Count

      ```
      int getFreeAssetNetUsageV2Count()
      ```

      `map<string, int64> free_asset_net_usageV2 = 59;`
    - #### containsFreeAssetNetUsageV2

      ```
      boolean containsFreeAssetNetUsageV2(java.lang.String key)
      ```

      `map<string, int64> free_asset_net_usageV2 = 59;`
    - #### getFreeAssetNetUsageV2

      ```
      @Deprecated
      java.util.Map<java.lang.String,java.lang.Long> getFreeAssetNetUsageV2()
      ```

      Deprecated.

      Use [`getFreeAssetNetUsageV2Map()`](../../../../org/tron/trident/proto/Response.AccountOrBuilder.html#getFreeAssetNetUsageV2Map--) instead.
    - #### getFreeAssetNetUsageV2Map

      ```
      java.util.Map<java.lang.String,java.lang.Long> getFreeAssetNetUsageV2Map()
      ```

      `map<string, int64> free_asset_net_usageV2 = 59;`
    - #### getFreeAssetNetUsageV2OrDefault

      ```
      long getFreeAssetNetUsageV2OrDefault(java.lang.String key,
                                           long defaultValue)
      ```

      `map<string, int64> free_asset_net_usageV2 = 59;`
    - #### getFreeAssetNetUsageV2OrThrow

      ```
      long getFreeAssetNetUsageV2OrThrow(java.lang.String key)
      ```

      `map<string, int64> free_asset_net_usageV2 = 59;`
    - #### getLatestConsumeTime

      ```
      long getLatestConsumeTime()
      ```

      `int64 latest_consume_time = 21;`

      Returns:
      :   The latestConsumeTime.
    - #### getLatestConsumeFreeTime

      ```
      long getLatestConsumeFreeTime()
      ```

      `int64 latest_consume_free_time = 22;`

      Returns:
      :   The latestConsumeFreeTime.
    - #### getAccountId

      ```
      com.google.protobuf.ByteString getAccountId()
      ```

      ```
       the identity of this account, case insensitive
      ```

      `bytes account_id = 23;`

      Returns:
      :   The accountId.
    - #### getNetWindowSize

      ```
      long getNetWindowSize()
      ```

      `int64 net_window_size = 24;`

      Returns:
      :   The netWindowSize.
    - #### getNetWindowOptimized

      ```
      boolean getNetWindowOptimized()
      ```

      `bool net_window_optimized = 25;`

      Returns:
      :   The netWindowOptimized.
    - #### hasAccountResource

      ```
      boolean hasAccountResource()
      ```

      `.protocol.Account.AccountResource account_resource = 26;`

      Returns:
      :   Whether the accountResource field is set.
    - #### getAccountResource

      ```
      Response.Account.AccountResource getAccountResource()
      ```

      `.protocol.Account.AccountResource account_resource = 26;`

      Returns:
      :   The accountResource.
    - #### getAccountResourceOrBuilder

      ```
      Response.Account.AccountResourceOrBuilder getAccountResourceOrBuilder()
      ```

      `.protocol.Account.AccountResource account_resource = 26;`
    - #### getCodeHash

      ```
      com.google.protobuf.ByteString getCodeHash()
      ```

      `bytes codeHash = 30;`

      Returns:
      :   The codeHash.
    - #### hasOwnerPermission

      ```
      boolean hasOwnerPermission()
      ```

      `.protocol.Permission owner_permission = 31;`

      Returns:
      :   Whether the ownerPermission field is set.
    - #### getOwnerPermission

      ```
      Common.Permission getOwnerPermission()
      ```

      `.protocol.Permission owner_permission = 31;`

      Returns:
      :   The ownerPermission.
    - #### getOwnerPermissionOrBuilder

      ```
      Common.PermissionOrBuilder getOwnerPermissionOrBuilder()
      ```

      `.protocol.Permission owner_permission = 31;`
    - #### hasWitnessPermission

      ```
      boolean hasWitnessPermission()
      ```

      `.protocol.Permission witness_permission = 32;`

      Returns:
      :   Whether the witnessPermission field is set.
    - #### getWitnessPermission

      ```
      Common.Permission getWitnessPermission()
      ```

      `.protocol.Permission witness_permission = 32;`

      Returns:
      :   The witnessPermission.
    - #### getWitnessPermissionOrBuilder

      ```
      Common.PermissionOrBuilder getWitnessPermissionOrBuilder()
      ```

      `.protocol.Permission witness_permission = 32;`
    - #### getActivePermissionList

      ```
      java.util.List<Common.Permission> getActivePermissionList()
      ```

      `repeated .protocol.Permission active_permission = 33;`
    - #### getActivePermission

      ```
      Common.Permission getActivePermission(int index)
      ```

      `repeated .protocol.Permission active_permission = 33;`
    - #### getActivePermissionCount

      ```
      int getActivePermissionCount()
      ```

      `repeated .protocol.Permission active_permission = 33;`
    - #### getActivePermissionOrBuilderList

      ```
      java.util.List<? extends Common.PermissionOrBuilder> getActivePermissionOrBuilderList()
      ```

      `repeated .protocol.Permission active_permission = 33;`
    - #### getActivePermissionOrBuilder

      ```
      Common.PermissionOrBuilder getActivePermissionOrBuilder(int index)
      ```

      `repeated .protocol.Permission active_permission = 33;`
    - #### getFrozenV2List

      ```
      java.util.List<Response.Account.FreezeV2> getFrozenV2List()
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`
    - #### getFrozenV2

      ```
      Response.Account.FreezeV2 getFrozenV2(int index)
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`
    - #### getFrozenV2Count

      ```
      int getFrozenV2Count()
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`
    - #### getFrozenV2OrBuilderList

      ```
      java.util.List<? extends Response.Account.FreezeV2OrBuilder> getFrozenV2OrBuilderList()
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`
    - #### getFrozenV2OrBuilder

      ```
      Response.Account.FreezeV2OrBuilder getFrozenV2OrBuilder(int index)
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`
    - #### getUnfrozenV2List

      ```
      java.util.List<Response.Account.UnFreezeV2> getUnfrozenV2List()
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`
    - #### getUnfrozenV2

      ```
      Response.Account.UnFreezeV2 getUnfrozenV2(int index)
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`
    - #### getUnfrozenV2Count

      ```
      int getUnfrozenV2Count()
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`
    - #### getUnfrozenV2OrBuilderList

      ```
      java.util.List<? extends Response.Account.UnFreezeV2OrBuilder> getUnfrozenV2OrBuilderList()
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`
    - #### getUnfrozenV2OrBuilder

      ```
      Response.Account.UnFreezeV2OrBuilder getUnfrozenV2OrBuilder(int index)
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`
    - #### getDelegatedFrozenV2BalanceForBandwidth

      ```
      long getDelegatedFrozenV2BalanceForBandwidth()
      ```

      `int64 delegated_frozenV2_balance_for_bandwidth = 36;`

      Returns:
      :   The delegatedFrozenV2BalanceForBandwidth.
    - #### getAcquiredDelegatedFrozenV2BalanceForBandwidth

      ```
      long getAcquiredDelegatedFrozenV2BalanceForBandwidth()
      ```

      `int64 acquired_delegated_frozenV2_balance_for_bandwidth = 37;`

      Returns:
      :   The acquiredDelegatedFrozenV2BalanceForBandwidth.