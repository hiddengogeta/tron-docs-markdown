

org.tron.trident.proto

## Class Response.Account.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.Account.Builder](../../../../org/tron/trident/proto/Response.Account.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.Account.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.AccountOrBuilder](../../../../org/tron/trident/proto/Response.AccountOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.Account](../../../../org/tron/trident/proto/Response.Account.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.Account.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Builder>
  implements Response.AccountOrBuilder
  ```

  ```
   Account
  ```

  Protobuf type `protocol.Account`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `Response.Account.Builder` | `addActivePermission(Common.Permission.Builder builderForValue)` `repeated .protocol.Permission active_permission = 33;` |
    | `Response.Account.Builder` | `addActivePermission(Common.Permission value)` `repeated .protocol.Permission active_permission = 33;` |
    | `Response.Account.Builder` | `addActivePermission(int index, Common.Permission.Builder builderForValue)` `repeated .protocol.Permission active_permission = 33;` |
    | `Response.Account.Builder` | `addActivePermission(int index, Common.Permission value)` `repeated .protocol.Permission active_permission = 33;` |
    | `Common.Permission.Builder` | `addActivePermissionBuilder()` `repeated .protocol.Permission active_permission = 33;` |
    | `Common.Permission.Builder` | `addActivePermissionBuilder(int index)` `repeated .protocol.Permission active_permission = 33;` |
    | `Response.Account.Builder` | `addAllActivePermission(java.lang.Iterable<? extends Common.Permission> values)` `repeated .protocol.Permission active_permission = 33;` |
    | `Response.Account.Builder` | `addAllFrozen(java.lang.Iterable<? extends Response.Account.Frozen> values)` the frozen balance for bandwidth |
    | `Response.Account.Builder` | `addAllFrozenSupply(java.lang.Iterable<? extends Response.Account.Frozen> values)` frozen asset(for asset issuer) |
    | `Response.Account.Builder` | `addAllFrozenV2(java.lang.Iterable<? extends Response.Account.FreezeV2> values)` `repeated .protocol.Account.FreezeV2 frozenV2 = 34;` |
    | `Response.Account.Builder` | `addAllUnfrozenV2(java.lang.Iterable<? extends Response.Account.UnFreezeV2> values)` `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;` |
    | `Response.Account.Builder` | `addAllVotes(java.lang.Iterable<? extends Common.Vote> values)` the votes |
    | `Response.Account.Builder` | `addFrozen(int index, Response.Account.Frozen.Builder builderForValue)` the frozen balance for bandwidth |
    | `Response.Account.Builder` | `addFrozen(int index, Response.Account.Frozen value)` the frozen balance for bandwidth |
    | `Response.Account.Builder` | `addFrozen(Response.Account.Frozen.Builder builderForValue)` the frozen balance for bandwidth |
    | `Response.Account.Builder` | `addFrozen(Response.Account.Frozen value)` the frozen balance for bandwidth |
    | `Response.Account.Frozen.Builder` | `addFrozenBuilder()` the frozen balance for bandwidth |
    | `Response.Account.Frozen.Builder` | `addFrozenBuilder(int index)` the frozen balance for bandwidth |
    | `Response.Account.Builder` | `addFrozenSupply(int index, Response.Account.Frozen.Builder builderForValue)` frozen asset(for asset issuer) |
    | `Response.Account.Builder` | `addFrozenSupply(int index, Response.Account.Frozen value)` frozen asset(for asset issuer) |
    | `Response.Account.Builder` | `addFrozenSupply(Response.Account.Frozen.Builder builderForValue)` frozen asset(for asset issuer) |
    | `Response.Account.Builder` | `addFrozenSupply(Response.Account.Frozen value)` frozen asset(for asset issuer) |
    | `Response.Account.Frozen.Builder` | `addFrozenSupplyBuilder()` frozen asset(for asset issuer) |
    | `Response.Account.Frozen.Builder` | `addFrozenSupplyBuilder(int index)` frozen asset(for asset issuer) |
    | `Response.Account.Builder` | `addFrozenV2(int index, Response.Account.FreezeV2.Builder builderForValue)` `repeated .protocol.Account.FreezeV2 frozenV2 = 34;` |
    | `Response.Account.Builder` | `addFrozenV2(int index, Response.Account.FreezeV2 value)` `repeated .protocol.Account.FreezeV2 frozenV2 = 34;` |
    | `Response.Account.Builder` | `addFrozenV2(Response.Account.FreezeV2.Builder builderForValue)` `repeated .protocol.Account.FreezeV2 frozenV2 = 34;` |
    | `Response.Account.Builder` | `addFrozenV2(Response.Account.FreezeV2 value)` `repeated .protocol.Account.FreezeV2 frozenV2 = 34;` |
    | `Response.Account.FreezeV2.Builder` | `addFrozenV2Builder()` `repeated .protocol.Account.FreezeV2 frozenV2 = 34;` |
    | `Response.Account.FreezeV2.Builder` | `addFrozenV2Builder(int index)` `repeated .protocol.Account.FreezeV2 frozenV2 = 34;` |
    | `Response.Account.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.Account.Builder` | `addUnfrozenV2(int index, Response.Account.UnFreezeV2.Builder builderForValue)` `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;` |
    | `Response.Account.Builder` | `addUnfrozenV2(int index, Response.Account.UnFreezeV2 value)` `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;` |
    | `Response.Account.Builder` | `addUnfrozenV2(Response.Account.UnFreezeV2.Builder builderForValue)` `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;` |
    | `Response.Account.Builder` | `addUnfrozenV2(Response.Account.UnFreezeV2 value)` `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;` |
    | `Response.Account.UnFreezeV2.Builder` | `addUnfrozenV2Builder()` `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;` |
    | `Response.Account.UnFreezeV2.Builder` | `addUnfrozenV2Builder(int index)` `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;` |
    | `Response.Account.Builder` | `addVotes(Common.Vote.Builder builderForValue)` the votes |
    | `Response.Account.Builder` | `addVotes(Common.Vote value)` the votes |
    | `Response.Account.Builder` | `addVotes(int index, Common.Vote.Builder builderForValue)` the votes |
    | `Response.Account.Builder` | `addVotes(int index, Common.Vote value)` the votes |
    | `Common.Vote.Builder` | `addVotesBuilder()` the votes |
    | `Common.Vote.Builder` | `addVotesBuilder(int index)` the votes |
    | `Response.Account` | `build()` |
    | `Response.Account` | `buildPartial()` |
    | `Response.Account.Builder` | `clear()` |
    | `Response.Account.Builder` | `clearAccountId()` the identity of this account, case insensitive |
    | `Response.Account.Builder` | `clearAccountName()` account nick name |
    | `Response.Account.Builder` | `clearAccountResource()` `.protocol.Account.AccountResource account_resource = 26;` |
    | `Response.Account.Builder` | `clearAcquiredDelegatedFrozenBalanceForBandwidth()` Frozen balance provided by other accounts to this account |
    | `Response.Account.Builder` | `clearAcquiredDelegatedFrozenV2BalanceForBandwidth()` `int64 acquired_delegated_frozenV2_balance_for_bandwidth = 37;` |
    | `Response.Account.Builder` | `clearActivePermission()` `repeated .protocol.Permission active_permission = 33;` |
    | `Response.Account.Builder` | `clearAddress()` the create address |
    | `Response.Account.Builder` | `clearAllowance()` witness block producing allowance |
    | `Response.Account.Builder` | `clearAsset()` |
    | `Response.Account.Builder` | `clearAssetIssuedID()` `bytes asset_issued_ID = 57;` |
    | `Response.Account.Builder` | `clearAssetIssuedName()` asset\_issued\_name |
    | `Response.Account.Builder` | `clearAssetOptimized()` `bool asset_optimized = 60;` |
    | `Response.Account.Builder` | `clearAssetV2()` |
    | `Response.Account.Builder` | `clearBalance()` the trx balance |
    | `Response.Account.Builder` | `clearCode()` not used so far |
    | `Response.Account.Builder` | `clearCodeHash()` `bytes codeHash = 30;` |
    | `Response.Account.Builder` | `clearCreateTime()` this account create time |
    | `Response.Account.Builder` | `clearDelegatedFrozenBalanceForBandwidth()` Freeze and provide balances to other accounts |
    | `Response.Account.Builder` | `clearDelegatedFrozenV2BalanceForBandwidth()` `int64 delegated_frozenV2_balance_for_bandwidth = 36;` |
    | `Response.Account.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.Account.Builder` | `clearFreeAssetNetUsage()` |
    | `Response.Account.Builder` | `clearFreeAssetNetUsageV2()` |
    | `Response.Account.Builder` | `clearFreeNetUsage()` `int64 free_net_usage = 19;` |
    | `Response.Account.Builder` | `clearFrozen()` the frozen balance for bandwidth |
    | `Response.Account.Builder` | `clearFrozenSupply()` frozen asset(for asset issuer) |
    | `Response.Account.Builder` | `clearFrozenV2()` `repeated .protocol.Account.FreezeV2 frozenV2 = 34;` |
    | `Response.Account.Builder` | `clearIsCommittee()` `bool is_committee = 15;` |
    | `Response.Account.Builder` | `clearIsWitness()` `bool is_witness = 14;` |
    | `Response.Account.Builder` | `clearLatestAssetOperationTime()` |
    | `Response.Account.Builder` | `clearLatestAssetOperationTimeV2()` |
    | `Response.Account.Builder` | `clearLatestConsumeFreeTime()` `int64 latest_consume_free_time = 22;` |
    | `Response.Account.Builder` | `clearLatestConsumeTime()` `int64 latest_consume_time = 21;` |
    | `Response.Account.Builder` | `clearLatestOprationTime()` this last operation time, including transfer, voting and so on. |
    | `Response.Account.Builder` | `clearLatestWithdrawTime()` last withdraw time |
    | `Response.Account.Builder` | `clearNetUsage()` bandwidth, get from frozen |
    | `Response.Account.Builder` | `clearNetWindowOptimized()` `bool net_window_optimized = 25;` |
    | `Response.Account.Builder` | `clearNetWindowSize()` `int64 net_window_size = 24;` |
    | `Response.Account.Builder` | `clearOldTronPower()` `int64 old_tron_power = 46;` |
    | `Response.Account.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.Account.Builder` | `clearOwnerPermission()` `.protocol.Permission owner_permission = 31;` |
    | `Response.Account.Builder` | `clearTronPower()` `.protocol.Account.Frozen tron_power = 47;` |
    | `Response.Account.Builder` | `clearType()` `.protocol.AccountType type = 2;` |
    | `Response.Account.Builder` | `clearUnfrozenV2()` `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;` |
    | `Response.Account.Builder` | `clearVotes()` the votes |
    | `Response.Account.Builder` | `clearWitnessPermission()` `.protocol.Permission witness_permission = 32;` |
    | `Response.Account.Builder` | `clone()` |
    | `boolean` | `containsAsset(java.lang.String key)` the other asset owned by this account |
    | `boolean` | `containsAssetV2(java.lang.String key)` the other asset owned by this account，key is assetId |
    | `boolean` | `containsFreeAssetNetUsage(java.lang.String key)` `map<string, int64> free_asset_net_usage = 20;` |
    | `boolean` | `containsFreeAssetNetUsageV2(java.lang.String key)` `map<string, int64> free_asset_net_usageV2 = 59;` |
    | `boolean` | `containsLatestAssetOperationTime(java.lang.String key)` `map<string, int64> latest_asset_operation_time = 18;` |
    | `boolean` | `containsLatestAssetOperationTimeV2(java.lang.String key)` `map<string, int64> latest_asset_operation_timeV2 = 58;` |
    | `com.google.protobuf.ByteString` | `getAccountId()` the identity of this account, case insensitive |
    | `com.google.protobuf.ByteString` | `getAccountName()` account nick name |
    | `Response.Account.AccountResource` | `getAccountResource()` `.protocol.Account.AccountResource account_resource = 26;` |
    | `Response.Account.AccountResource.Builder` | `getAccountResourceBuilder()` `.protocol.Account.AccountResource account_resource = 26;` |
    | `Response.Account.AccountResourceOrBuilder` | `getAccountResourceOrBuilder()` `.protocol.Account.AccountResource account_resource = 26;` |
    | `long` | `getAcquiredDelegatedFrozenBalanceForBandwidth()` Frozen balance provided by other accounts to this account |
    | `long` | `getAcquiredDelegatedFrozenV2BalanceForBandwidth()` `int64 acquired_delegated_frozenV2_balance_for_bandwidth = 37;` |
    | `Common.Permission` | `getActivePermission(int index)` `repeated .protocol.Permission active_permission = 33;` |
    | `Common.Permission.Builder` | `getActivePermissionBuilder(int index)` `repeated .protocol.Permission active_permission = 33;` |
    | `java.util.List<Common.Permission.Builder>` | `getActivePermissionBuilderList()` `repeated .protocol.Permission active_permission = 33;` |
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
    | `Response.Account` | `getDefaultInstanceForType()` |
    | `long` | `getDelegatedFrozenBalanceForBandwidth()` Freeze and provide balances to other accounts |
    | `long` | `getDelegatedFrozenV2BalanceForBandwidth()` `int64 delegated_frozenV2_balance_for_bandwidth = 36;` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
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
    | `Response.Account.Frozen.Builder` | `getFrozenBuilder(int index)` the frozen balance for bandwidth |
    | `java.util.List<Response.Account.Frozen.Builder>` | `getFrozenBuilderList()` the frozen balance for bandwidth |
    | `int` | `getFrozenCount()` the frozen balance for bandwidth |
    | `java.util.List<Response.Account.Frozen>` | `getFrozenList()` the frozen balance for bandwidth |
    | `Response.Account.FrozenOrBuilder` | `getFrozenOrBuilder(int index)` the frozen balance for bandwidth |
    | `java.util.List<? extends Response.Account.FrozenOrBuilder>` | `getFrozenOrBuilderList()` the frozen balance for bandwidth |
    | `Response.Account.Frozen` | `getFrozenSupply(int index)` frozen asset(for asset issuer) |
    | `Response.Account.Frozen.Builder` | `getFrozenSupplyBuilder(int index)` frozen asset(for asset issuer) |
    | `java.util.List<Response.Account.Frozen.Builder>` | `getFrozenSupplyBuilderList()` frozen asset(for asset issuer) |
    | `int` | `getFrozenSupplyCount()` frozen asset(for asset issuer) |
    | `java.util.List<Response.Account.Frozen>` | `getFrozenSupplyList()` frozen asset(for asset issuer) |
    | `Response.Account.FrozenOrBuilder` | `getFrozenSupplyOrBuilder(int index)` frozen asset(for asset issuer) |
    | `java.util.List<? extends Response.Account.FrozenOrBuilder>` | `getFrozenSupplyOrBuilderList()` frozen asset(for asset issuer) |
    | `Response.Account.FreezeV2` | `getFrozenV2(int index)` `repeated .protocol.Account.FreezeV2 frozenV2 = 34;` |
    | `Response.Account.FreezeV2.Builder` | `getFrozenV2Builder(int index)` `repeated .protocol.Account.FreezeV2 frozenV2 = 34;` |
    | `java.util.List<Response.Account.FreezeV2.Builder>` | `getFrozenV2BuilderList()` `repeated .protocol.Account.FreezeV2 frozenV2 = 34;` |
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
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getMutableAsset()` Deprecated. |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getMutableAssetV2()` Deprecated. |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getMutableFreeAssetNetUsage()` Deprecated. |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getMutableFreeAssetNetUsageV2()` Deprecated. |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getMutableLatestAssetOperationTime()` Deprecated. |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getMutableLatestAssetOperationTimeV2()` Deprecated. |
    | `long` | `getNetUsage()` bandwidth, get from frozen |
    | `boolean` | `getNetWindowOptimized()` `bool net_window_optimized = 25;` |
    | `long` | `getNetWindowSize()` `int64 net_window_size = 24;` |
    | `long` | `getOldTronPower()` `int64 old_tron_power = 46;` |
    | `Common.Permission` | `getOwnerPermission()` `.protocol.Permission owner_permission = 31;` |
    | `Common.Permission.Builder` | `getOwnerPermissionBuilder()` `.protocol.Permission owner_permission = 31;` |
    | `Common.PermissionOrBuilder` | `getOwnerPermissionOrBuilder()` `.protocol.Permission owner_permission = 31;` |
    | `Response.Account.Frozen` | `getTronPower()` `.protocol.Account.Frozen tron_power = 47;` |
    | `Response.Account.Frozen.Builder` | `getTronPowerBuilder()` `.protocol.Account.Frozen tron_power = 47;` |
    | `Response.Account.FrozenOrBuilder` | `getTronPowerOrBuilder()` `.protocol.Account.Frozen tron_power = 47;` |
    | `Common.AccountType` | `getType()` `.protocol.AccountType type = 2;` |
    | `int` | `getTypeValue()` `.protocol.AccountType type = 2;` |
    | `Response.Account.UnFreezeV2` | `getUnfrozenV2(int index)` `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;` |
    | `Response.Account.UnFreezeV2.Builder` | `getUnfrozenV2Builder(int index)` `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;` |
    | `java.util.List<Response.Account.UnFreezeV2.Builder>` | `getUnfrozenV2BuilderList()` `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;` |
    | `int` | `getUnfrozenV2Count()` `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;` |
    | `java.util.List<Response.Account.UnFreezeV2>` | `getUnfrozenV2List()` `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;` |
    | `Response.Account.UnFreezeV2OrBuilder` | `getUnfrozenV2OrBuilder(int index)` `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;` |
    | `java.util.List<? extends Response.Account.UnFreezeV2OrBuilder>` | `getUnfrozenV2OrBuilderList()` `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;` |
    | `Common.Vote` | `getVotes(int index)` the votes |
    | `Common.Vote.Builder` | `getVotesBuilder(int index)` the votes |
    | `java.util.List<Common.Vote.Builder>` | `getVotesBuilderList()` the votes |
    | `int` | `getVotesCount()` the votes |
    | `java.util.List<Common.Vote>` | `getVotesList()` the votes |
    | `Common.VoteOrBuilder` | `getVotesOrBuilder(int index)` the votes |
    | `java.util.List<? extends Common.VoteOrBuilder>` | `getVotesOrBuilderList()` the votes |
    | `Common.Permission` | `getWitnessPermission()` `.protocol.Permission witness_permission = 32;` |
    | `Common.Permission.Builder` | `getWitnessPermissionBuilder()` `.protocol.Permission witness_permission = 32;` |
    | `Common.PermissionOrBuilder` | `getWitnessPermissionOrBuilder()` `.protocol.Permission witness_permission = 32;` |
    | `boolean` | `hasAccountResource()` `.protocol.Account.AccountResource account_resource = 26;` |
    | `boolean` | `hasOwnerPermission()` `.protocol.Permission owner_permission = 31;` |
    | `boolean` | `hasTronPower()` `.protocol.Account.Frozen tron_power = 47;` |
    | `boolean` | `hasWitnessPermission()` `.protocol.Permission witness_permission = 32;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMapFieldReflection(int number)` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMutableMapFieldReflection(int number)` |
    | `boolean` | `isInitialized()` |
    | `Response.Account.Builder` | `mergeAccountResource(Response.Account.AccountResource value)` `.protocol.Account.AccountResource account_resource = 26;` |
    | `Response.Account.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.Account.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.Account.Builder` | `mergeFrom(Response.Account other)` |
    | `Response.Account.Builder` | `mergeOwnerPermission(Common.Permission value)` `.protocol.Permission owner_permission = 31;` |
    | `Response.Account.Builder` | `mergeTronPower(Response.Account.Frozen value)` `.protocol.Account.Frozen tron_power = 47;` |
    | `Response.Account.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.Account.Builder` | `mergeWitnessPermission(Common.Permission value)` `.protocol.Permission witness_permission = 32;` |
    | `Response.Account.Builder` | `putAllAsset(java.util.Map<java.lang.String,java.lang.Long> values)` the other asset owned by this account |
    | `Response.Account.Builder` | `putAllAssetV2(java.util.Map<java.lang.String,java.lang.Long> values)` the other asset owned by this account，key is assetId |
    | `Response.Account.Builder` | `putAllFreeAssetNetUsage(java.util.Map<java.lang.String,java.lang.Long> values)` `map<string, int64> free_asset_net_usage = 20;` |
    | `Response.Account.Builder` | `putAllFreeAssetNetUsageV2(java.util.Map<java.lang.String,java.lang.Long> values)` `map<string, int64> free_asset_net_usageV2 = 59;` |
    | `Response.Account.Builder` | `putAllLatestAssetOperationTime(java.util.Map<java.lang.String,java.lang.Long> values)` `map<string, int64> latest_asset_operation_time = 18;` |
    | `Response.Account.Builder` | `putAllLatestAssetOperationTimeV2(java.util.Map<java.lang.String,java.lang.Long> values)` `map<string, int64> latest_asset_operation_timeV2 = 58;` |
    | `Response.Account.Builder` | `putAsset(java.lang.String key, long value)` the other asset owned by this account |
    | `Response.Account.Builder` | `putAssetV2(java.lang.String key, long value)` the other asset owned by this account，key is assetId |
    | `Response.Account.Builder` | `putFreeAssetNetUsage(java.lang.String key, long value)` `map<string, int64> free_asset_net_usage = 20;` |
    | `Response.Account.Builder` | `putFreeAssetNetUsageV2(java.lang.String key, long value)` `map<string, int64> free_asset_net_usageV2 = 59;` |
    | `Response.Account.Builder` | `putLatestAssetOperationTime(java.lang.String key, long value)` `map<string, int64> latest_asset_operation_time = 18;` |
    | `Response.Account.Builder` | `putLatestAssetOperationTimeV2(java.lang.String key, long value)` `map<string, int64> latest_asset_operation_timeV2 = 58;` |
    | `Response.Account.Builder` | `removeActivePermission(int index)` `repeated .protocol.Permission active_permission = 33;` |
    | `Response.Account.Builder` | `removeAsset(java.lang.String key)` the other asset owned by this account |
    | `Response.Account.Builder` | `removeAssetV2(java.lang.String key)` the other asset owned by this account，key is assetId |
    | `Response.Account.Builder` | `removeFreeAssetNetUsage(java.lang.String key)` `map<string, int64> free_asset_net_usage = 20;` |
    | `Response.Account.Builder` | `removeFreeAssetNetUsageV2(java.lang.String key)` `map<string, int64> free_asset_net_usageV2 = 59;` |
    | `Response.Account.Builder` | `removeFrozen(int index)` the frozen balance for bandwidth |
    | `Response.Account.Builder` | `removeFrozenSupply(int index)` frozen asset(for asset issuer) |
    | `Response.Account.Builder` | `removeFrozenV2(int index)` `repeated .protocol.Account.FreezeV2 frozenV2 = 34;` |
    | `Response.Account.Builder` | `removeLatestAssetOperationTime(java.lang.String key)` `map<string, int64> latest_asset_operation_time = 18;` |
    | `Response.Account.Builder` | `removeLatestAssetOperationTimeV2(java.lang.String key)` `map<string, int64> latest_asset_operation_timeV2 = 58;` |
    | `Response.Account.Builder` | `removeUnfrozenV2(int index)` `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;` |
    | `Response.Account.Builder` | `removeVotes(int index)` the votes |
    | `Response.Account.Builder` | `setAccountId(com.google.protobuf.ByteString value)` the identity of this account, case insensitive |
    | `Response.Account.Builder` | `setAccountName(com.google.protobuf.ByteString value)` account nick name |
    | `Response.Account.Builder` | `setAccountResource(Response.Account.AccountResource.Builder builderForValue)` `.protocol.Account.AccountResource account_resource = 26;` |
    | `Response.Account.Builder` | `setAccountResource(Response.Account.AccountResource value)` `.protocol.Account.AccountResource account_resource = 26;` |
    | `Response.Account.Builder` | `setAcquiredDelegatedFrozenBalanceForBandwidth(long value)` Frozen balance provided by other accounts to this account |
    | `Response.Account.Builder` | `setAcquiredDelegatedFrozenV2BalanceForBandwidth(long value)` `int64 acquired_delegated_frozenV2_balance_for_bandwidth = 37;` |
    | `Response.Account.Builder` | `setActivePermission(int index, Common.Permission.Builder builderForValue)` `repeated .protocol.Permission active_permission = 33;` |
    | `Response.Account.Builder` | `setActivePermission(int index, Common.Permission value)` `repeated .protocol.Permission active_permission = 33;` |
    | `Response.Account.Builder` | `setAddress(com.google.protobuf.ByteString value)` the create address |
    | `Response.Account.Builder` | `setAllowance(long value)` witness block producing allowance |
    | `Response.Account.Builder` | `setAssetIssuedID(com.google.protobuf.ByteString value)` `bytes asset_issued_ID = 57;` |
    | `Response.Account.Builder` | `setAssetIssuedName(com.google.protobuf.ByteString value)` asset\_issued\_name |
    | `Response.Account.Builder` | `setAssetOptimized(boolean value)` `bool asset_optimized = 60;` |
    | `Response.Account.Builder` | `setBalance(long value)` the trx balance |
    | `Response.Account.Builder` | `setCode(com.google.protobuf.ByteString value)` not used so far |
    | `Response.Account.Builder` | `setCodeHash(com.google.protobuf.ByteString value)` `bytes codeHash = 30;` |
    | `Response.Account.Builder` | `setCreateTime(long value)` this account create time |
    | `Response.Account.Builder` | `setDelegatedFrozenBalanceForBandwidth(long value)` Freeze and provide balances to other accounts |
    | `Response.Account.Builder` | `setDelegatedFrozenV2BalanceForBandwidth(long value)` `int64 delegated_frozenV2_balance_for_bandwidth = 36;` |
    | `Response.Account.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.Account.Builder` | `setFreeNetUsage(long value)` `int64 free_net_usage = 19;` |
    | `Response.Account.Builder` | `setFrozen(int index, Response.Account.Frozen.Builder builderForValue)` the frozen balance for bandwidth |
    | `Response.Account.Builder` | `setFrozen(int index, Response.Account.Frozen value)` the frozen balance for bandwidth |
    | `Response.Account.Builder` | `setFrozenSupply(int index, Response.Account.Frozen.Builder builderForValue)` frozen asset(for asset issuer) |
    | `Response.Account.Builder` | `setFrozenSupply(int index, Response.Account.Frozen value)` frozen asset(for asset issuer) |
    | `Response.Account.Builder` | `setFrozenV2(int index, Response.Account.FreezeV2.Builder builderForValue)` `repeated .protocol.Account.FreezeV2 frozenV2 = 34;` |
    | `Response.Account.Builder` | `setFrozenV2(int index, Response.Account.FreezeV2 value)` `repeated .protocol.Account.FreezeV2 frozenV2 = 34;` |
    | `Response.Account.Builder` | `setIsCommittee(boolean value)` `bool is_committee = 15;` |
    | `Response.Account.Builder` | `setIsWitness(boolean value)` `bool is_witness = 14;` |
    | `Response.Account.Builder` | `setLatestConsumeFreeTime(long value)` `int64 latest_consume_free_time = 22;` |
    | `Response.Account.Builder` | `setLatestConsumeTime(long value)` `int64 latest_consume_time = 21;` |
    | `Response.Account.Builder` | `setLatestOprationTime(long value)` this last operation time, including transfer, voting and so on. |
    | `Response.Account.Builder` | `setLatestWithdrawTime(long value)` last withdraw time |
    | `Response.Account.Builder` | `setNetUsage(long value)` bandwidth, get from frozen |
    | `Response.Account.Builder` | `setNetWindowOptimized(boolean value)` `bool net_window_optimized = 25;` |
    | `Response.Account.Builder` | `setNetWindowSize(long value)` `int64 net_window_size = 24;` |
    | `Response.Account.Builder` | `setOldTronPower(long value)` `int64 old_tron_power = 46;` |
    | `Response.Account.Builder` | `setOwnerPermission(Common.Permission.Builder builderForValue)` `.protocol.Permission owner_permission = 31;` |
    | `Response.Account.Builder` | `setOwnerPermission(Common.Permission value)` `.protocol.Permission owner_permission = 31;` |
    | `Response.Account.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.Account.Builder` | `setTronPower(Response.Account.Frozen.Builder builderForValue)` `.protocol.Account.Frozen tron_power = 47;` |
    | `Response.Account.Builder` | `setTronPower(Response.Account.Frozen value)` `.protocol.Account.Frozen tron_power = 47;` |
    | `Response.Account.Builder` | `setType(Common.AccountType value)` `.protocol.AccountType type = 2;` |
    | `Response.Account.Builder` | `setTypeValue(int value)` `.protocol.AccountType type = 2;` |
    | `Response.Account.Builder` | `setUnfrozenV2(int index, Response.Account.UnFreezeV2.Builder builderForValue)` `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;` |
    | `Response.Account.Builder` | `setUnfrozenV2(int index, Response.Account.UnFreezeV2 value)` `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;` |
    | `Response.Account.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.Account.Builder` | `setVotes(int index, Common.Vote.Builder builderForValue)` the votes |
    | `Response.Account.Builder` | `setVotes(int index, Common.Vote value)` the votes |
    | `Response.Account.Builder` | `setWitnessPermission(Common.Permission.Builder builderForValue)` `.protocol.Permission witness_permission = 32;` |
    | `Response.Account.Builder` | `setWitnessPermission(Common.Permission value)` `.protocol.Permission witness_permission = 32;` |

    - ### Methods inherited from class com.google.protobuf.GeneratedMessageV3.Builder

      `getAllFields, getField, getFieldBuilder, getOneofFieldDescriptor, getParentForChildren, getRepeatedField, getRepeatedFieldBuilder, getRepeatedFieldCount, getUnknownFields, getUnknownFieldSetBuilder, hasField, hasOneof, internalGetMapField, internalGetMutableMapField, isClean, markClean, mergeUnknownLengthDelimitedField, mergeUnknownVarintField, newBuilderForField, onBuilt, onChanged, parseUnknownField, setUnknownFieldSetBuilder, setUnknownFieldsProto3`
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
    - #### internalGetMapFieldReflection

      ```
      protected com.google.protobuf.MapFieldReflectionAccessor internalGetMapFieldReflection(int number)
      ```

      Overrides:
      :   `internalGetMapFieldReflection` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Builder>`
    - #### internalGetMutableMapFieldReflection

      ```
      protected com.google.protobuf.MapFieldReflectionAccessor internalGetMutableMapFieldReflection(int number)
      ```

      Overrides:
      :   `internalGetMutableMapFieldReflection` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Builder>`
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Builder>`
    - #### clear

      ```
      public Response.Account.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.Account getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.Account build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.Account buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.Account.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Builder>`
    - #### setField

      ```
      public Response.Account.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                               java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Builder>`
    - #### clearField

      ```
      public Response.Account.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Builder>`
    - #### clearOneof

      ```
      public Response.Account.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Builder>`
    - #### setRepeatedField

      ```
      public Response.Account.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       int index,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Builder>`
    - #### addRepeatedField

      ```
      public Response.Account.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Builder>`
    - #### mergeFrom

      ```
      public Response.Account.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.Account.Builder>`
    - #### mergeFrom

      ```
      public Response.Account.Builder mergeFrom(Response.Account other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Builder>`
    - #### mergeFrom

      ```
      public Response.Account.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.Account.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getAccountName

      ```
      public com.google.protobuf.ByteString getAccountName()
      ```

      ```
       account nick name
      ```

      `bytes account_name = 1;`

      Specified by:
      :   `getAccountName` in interface `Response.AccountOrBuilder`

      Returns:
      :   The accountName.
    - #### setAccountName

      ```
      public Response.Account.Builder setAccountName(com.google.protobuf.ByteString value)
      ```

      ```
       account nick name
      ```

      `bytes account_name = 1;`

      Parameters:
      :   `value` - The accountName to set.

      Returns:
      :   This builder for chaining.
    - #### clearAccountName

      ```
      public Response.Account.Builder clearAccountName()
      ```

      ```
       account nick name
      ```

      `bytes account_name = 1;`

      Returns:
      :   This builder for chaining.
    - #### getTypeValue

      ```
      public int getTypeValue()
      ```

      `.protocol.AccountType type = 2;`

      Specified by:
      :   `getTypeValue` in interface `Response.AccountOrBuilder`

      Returns:
      :   The enum numeric value on the wire for type.
    - #### setTypeValue

      ```
      public Response.Account.Builder setTypeValue(int value)
      ```

      `.protocol.AccountType type = 2;`

      Parameters:
      :   `value` - The enum numeric value on the wire for type to set.

      Returns:
      :   This builder for chaining.
    - #### getType

      ```
      public Common.AccountType getType()
      ```

      `.protocol.AccountType type = 2;`

      Specified by:
      :   `getType` in interface `Response.AccountOrBuilder`

      Returns:
      :   The type.
    - #### setType

      ```
      public Response.Account.Builder setType(Common.AccountType value)
      ```

      `.protocol.AccountType type = 2;`

      Parameters:
      :   `value` - The type to set.

      Returns:
      :   This builder for chaining.
    - #### clearType

      ```
      public Response.Account.Builder clearType()
      ```

      `.protocol.AccountType type = 2;`

      Returns:
      :   This builder for chaining.
    - #### getAddress

      ```
      public com.google.protobuf.ByteString getAddress()
      ```

      ```
       the create address
      ```

      `bytes address = 3;`

      Specified by:
      :   `getAddress` in interface `Response.AccountOrBuilder`

      Returns:
      :   The address.
    - #### setAddress

      ```
      public Response.Account.Builder setAddress(com.google.protobuf.ByteString value)
      ```

      ```
       the create address
      ```

      `bytes address = 3;`

      Parameters:
      :   `value` - The address to set.

      Returns:
      :   This builder for chaining.
    - #### clearAddress

      ```
      public Response.Account.Builder clearAddress()
      ```

      ```
       the create address
      ```

      `bytes address = 3;`

      Returns:
      :   This builder for chaining.
    - #### getBalance

      ```
      public long getBalance()
      ```

      ```
       the trx balance
      ```

      `int64 balance = 4;`

      Specified by:
      :   `getBalance` in interface `Response.AccountOrBuilder`

      Returns:
      :   The balance.
    - #### setBalance

      ```
      public Response.Account.Builder setBalance(long value)
      ```

      ```
       the trx balance
      ```

      `int64 balance = 4;`

      Parameters:
      :   `value` - The balance to set.

      Returns:
      :   This builder for chaining.
    - #### clearBalance

      ```
      public Response.Account.Builder clearBalance()
      ```

      ```
       the trx balance
      ```

      `int64 balance = 4;`

      Returns:
      :   This builder for chaining.
    - #### getVotesList

      ```
      public java.util.List<Common.Vote> getVotesList()
      ```

      ```
       the votes
      ```

      `repeated .protocol.Vote votes = 5;`

      Specified by:
      :   `getVotesList` in interface `Response.AccountOrBuilder`
    - #### getVotesCount

      ```
      public int getVotesCount()
      ```

      ```
       the votes
      ```

      `repeated .protocol.Vote votes = 5;`

      Specified by:
      :   `getVotesCount` in interface `Response.AccountOrBuilder`
    - #### getVotes

      ```
      public Common.Vote getVotes(int index)
      ```

      ```
       the votes
      ```

      `repeated .protocol.Vote votes = 5;`

      Specified by:
      :   `getVotes` in interface `Response.AccountOrBuilder`
    - #### setVotes

      ```
      public Response.Account.Builder setVotes(int index,
                                               Common.Vote value)
      ```

      ```
       the votes
      ```

      `repeated .protocol.Vote votes = 5;`
    - #### setVotes

      ```
      public Response.Account.Builder setVotes(int index,
                                               Common.Vote.Builder builderForValue)
      ```

      ```
       the votes
      ```

      `repeated .protocol.Vote votes = 5;`
    - #### addVotes

      ```
      public Response.Account.Builder addVotes(Common.Vote value)
      ```

      ```
       the votes
      ```

      `repeated .protocol.Vote votes = 5;`
    - #### addVotes

      ```
      public Response.Account.Builder addVotes(int index,
                                               Common.Vote value)
      ```

      ```
       the votes
      ```

      `repeated .protocol.Vote votes = 5;`
    - #### addVotes

      ```
      public Response.Account.Builder addVotes(Common.Vote.Builder builderForValue)
      ```

      ```
       the votes
      ```

      `repeated .protocol.Vote votes = 5;`
    - #### addVotes

      ```
      public Response.Account.Builder addVotes(int index,
                                               Common.Vote.Builder builderForValue)
      ```

      ```
       the votes
      ```

      `repeated .protocol.Vote votes = 5;`
    - #### addAllVotes

      ```
      public Response.Account.Builder addAllVotes(java.lang.Iterable<? extends Common.Vote> values)
      ```

      ```
       the votes
      ```

      `repeated .protocol.Vote votes = 5;`
    - #### clearVotes

      ```
      public Response.Account.Builder clearVotes()
      ```

      ```
       the votes
      ```

      `repeated .protocol.Vote votes = 5;`
    - #### removeVotes

      ```
      public Response.Account.Builder removeVotes(int index)
      ```

      ```
       the votes
      ```

      `repeated .protocol.Vote votes = 5;`
    - #### getVotesBuilder

      ```
      public Common.Vote.Builder getVotesBuilder(int index)
      ```

      ```
       the votes
      ```

      `repeated .protocol.Vote votes = 5;`
    - #### getVotesOrBuilder

      ```
      public Common.VoteOrBuilder getVotesOrBuilder(int index)
      ```

      ```
       the votes
      ```

      `repeated .protocol.Vote votes = 5;`

      Specified by:
      :   `getVotesOrBuilder` in interface `Response.AccountOrBuilder`
    - #### getVotesOrBuilderList

      ```
      public java.util.List<? extends Common.VoteOrBuilder> getVotesOrBuilderList()
      ```

      ```
       the votes
      ```

      `repeated .protocol.Vote votes = 5;`

      Specified by:
      :   `getVotesOrBuilderList` in interface `Response.AccountOrBuilder`
    - #### addVotesBuilder

      ```
      public Common.Vote.Builder addVotesBuilder()
      ```

      ```
       the votes
      ```

      `repeated .protocol.Vote votes = 5;`
    - #### addVotesBuilder

      ```
      public Common.Vote.Builder addVotesBuilder(int index)
      ```

      ```
       the votes
      ```

      `repeated .protocol.Vote votes = 5;`
    - #### getVotesBuilderList

      ```
      public java.util.List<Common.Vote.Builder> getVotesBuilderList()
      ```

      ```
       the votes
      ```

      `repeated .protocol.Vote votes = 5;`
    - #### getAssetCount

      ```
      public int getAssetCount()
      ```

      Description copied from interface: `Response.AccountOrBuilder`

      ```
       the other asset owned by this account
      ```

      `map<string, int64> asset = 6;`

      Specified by:
      :   `getAssetCount` in interface `Response.AccountOrBuilder`
    - #### containsAsset

      ```
      public boolean containsAsset(java.lang.String key)
      ```

      ```
       the other asset owned by this account
      ```

      `map<string, int64> asset = 6;`

      Specified by:
      :   `containsAsset` in interface `Response.AccountOrBuilder`
    - #### getAsset

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getAsset()
      ```

      Deprecated.

      Use [`getAssetMap()`](../../../../org/tron/trident/proto/Response.Account.Builder.html#getAssetMap--) instead.

      Specified by:
      :   `getAsset` in interface `Response.AccountOrBuilder`
    - #### getAssetMap

      ```
      public java.util.Map<java.lang.String,java.lang.Long> getAssetMap()
      ```

      ```
       the other asset owned by this account
      ```

      `map<string, int64> asset = 6;`

      Specified by:
      :   `getAssetMap` in interface `Response.AccountOrBuilder`
    - #### getAssetOrDefault

      ```
      public long getAssetOrDefault(java.lang.String key,
                                    long defaultValue)
      ```

      ```
       the other asset owned by this account
      ```

      `map<string, int64> asset = 6;`

      Specified by:
      :   `getAssetOrDefault` in interface `Response.AccountOrBuilder`
    - #### getAssetOrThrow

      ```
      public long getAssetOrThrow(java.lang.String key)
      ```

      ```
       the other asset owned by this account
      ```

      `map<string, int64> asset = 6;`

      Specified by:
      :   `getAssetOrThrow` in interface `Response.AccountOrBuilder`
    - #### clearAsset

      ```
      public Response.Account.Builder clearAsset()
      ```
    - #### removeAsset

      ```
      public Response.Account.Builder removeAsset(java.lang.String key)
      ```

      ```
       the other asset owned by this account
      ```

      `map<string, int64> asset = 6;`
    - #### getMutableAsset

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getMutableAsset()
      ```

      Deprecated.

      Use alternate mutation accessors instead.
    - #### putAsset

      ```
      public Response.Account.Builder putAsset(java.lang.String key,
                                               long value)
      ```

      ```
       the other asset owned by this account
      ```

      `map<string, int64> asset = 6;`
    - #### putAllAsset

      ```
      public Response.Account.Builder putAllAsset(java.util.Map<java.lang.String,java.lang.Long> values)
      ```

      ```
       the other asset owned by this account
      ```

      `map<string, int64> asset = 6;`
    - #### getAssetV2Count

      ```
      public int getAssetV2Count()
      ```

      Description copied from interface: `Response.AccountOrBuilder`

      ```
       the other asset owned by this account，key is assetId
      ```

      `map<string, int64> assetV2 = 56;`

      Specified by:
      :   `getAssetV2Count` in interface `Response.AccountOrBuilder`
    - #### containsAssetV2

      ```
      public boolean containsAssetV2(java.lang.String key)
      ```

      ```
       the other asset owned by this account，key is assetId
      ```

      `map<string, int64> assetV2 = 56;`

      Specified by:
      :   `containsAssetV2` in interface `Response.AccountOrBuilder`
    - #### getAssetV2

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getAssetV2()
      ```

      Deprecated.

      Use [`getAssetV2Map()`](../../../../org/tron/trident/proto/Response.Account.Builder.html#getAssetV2Map--) instead.

      Specified by:
      :   `getAssetV2` in interface `Response.AccountOrBuilder`
    - #### getAssetV2Map

      ```
      public java.util.Map<java.lang.String,java.lang.Long> getAssetV2Map()
      ```

      ```
       the other asset owned by this account，key is assetId
      ```

      `map<string, int64> assetV2 = 56;`

      Specified by:
      :   `getAssetV2Map` in interface `Response.AccountOrBuilder`
    - #### getAssetV2OrDefault

      ```
      public long getAssetV2OrDefault(java.lang.String key,
                                      long defaultValue)
      ```

      ```
       the other asset owned by this account，key is assetId
      ```

      `map<string, int64> assetV2 = 56;`

      Specified by:
      :   `getAssetV2OrDefault` in interface `Response.AccountOrBuilder`
    - #### getAssetV2OrThrow

      ```
      public long getAssetV2OrThrow(java.lang.String key)
      ```

      ```
       the other asset owned by this account，key is assetId
      ```

      `map<string, int64> assetV2 = 56;`

      Specified by:
      :   `getAssetV2OrThrow` in interface `Response.AccountOrBuilder`
    - #### clearAssetV2

      ```
      public Response.Account.Builder clearAssetV2()
      ```
    - #### removeAssetV2

      ```
      public Response.Account.Builder removeAssetV2(java.lang.String key)
      ```

      ```
       the other asset owned by this account，key is assetId
      ```

      `map<string, int64> assetV2 = 56;`
    - #### getMutableAssetV2

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getMutableAssetV2()
      ```

      Deprecated.

      Use alternate mutation accessors instead.
    - #### putAssetV2

      ```
      public Response.Account.Builder putAssetV2(java.lang.String key,
                                                 long value)
      ```

      ```
       the other asset owned by this account，key is assetId
      ```

      `map<string, int64> assetV2 = 56;`
    - #### putAllAssetV2

      ```
      public Response.Account.Builder putAllAssetV2(java.util.Map<java.lang.String,java.lang.Long> values)
      ```

      ```
       the other asset owned by this account，key is assetId
      ```

      `map<string, int64> assetV2 = 56;`
    - #### getFrozenList

      ```
      public java.util.List<Response.Account.Frozen> getFrozenList()
      ```

      ```
       the frozen balance for bandwidth
      ```

      `repeated .protocol.Account.Frozen frozen = 7;`

      Specified by:
      :   `getFrozenList` in interface `Response.AccountOrBuilder`
    - #### getFrozenCount

      ```
      public int getFrozenCount()
      ```

      ```
       the frozen balance for bandwidth
      ```

      `repeated .protocol.Account.Frozen frozen = 7;`

      Specified by:
      :   `getFrozenCount` in interface `Response.AccountOrBuilder`
    - #### getFrozen

      ```
      public Response.Account.Frozen getFrozen(int index)
      ```

      ```
       the frozen balance for bandwidth
      ```

      `repeated .protocol.Account.Frozen frozen = 7;`

      Specified by:
      :   `getFrozen` in interface `Response.AccountOrBuilder`
    - #### setFrozen

      ```
      public Response.Account.Builder setFrozen(int index,
                                                Response.Account.Frozen value)
      ```

      ```
       the frozen balance for bandwidth
      ```

      `repeated .protocol.Account.Frozen frozen = 7;`
    - #### setFrozen

      ```
      public Response.Account.Builder setFrozen(int index,
                                                Response.Account.Frozen.Builder builderForValue)
      ```

      ```
       the frozen balance for bandwidth
      ```

      `repeated .protocol.Account.Frozen frozen = 7;`
    - #### addFrozen

      ```
      public Response.Account.Builder addFrozen(Response.Account.Frozen value)
      ```

      ```
       the frozen balance for bandwidth
      ```

      `repeated .protocol.Account.Frozen frozen = 7;`
    - #### addFrozen

      ```
      public Response.Account.Builder addFrozen(int index,
                                                Response.Account.Frozen value)
      ```

      ```
       the frozen balance for bandwidth
      ```

      `repeated .protocol.Account.Frozen frozen = 7;`
    - #### addFrozen

      ```
      public Response.Account.Builder addFrozen(Response.Account.Frozen.Builder builderForValue)
      ```

      ```
       the frozen balance for bandwidth
      ```

      `repeated .protocol.Account.Frozen frozen = 7;`
    - #### addFrozen

      ```
      public Response.Account.Builder addFrozen(int index,
                                                Response.Account.Frozen.Builder builderForValue)
      ```

      ```
       the frozen balance for bandwidth
      ```

      `repeated .protocol.Account.Frozen frozen = 7;`
    - #### addAllFrozen

      ```
      public Response.Account.Builder addAllFrozen(java.lang.Iterable<? extends Response.Account.Frozen> values)
      ```

      ```
       the frozen balance for bandwidth
      ```

      `repeated .protocol.Account.Frozen frozen = 7;`
    - #### clearFrozen

      ```
      public Response.Account.Builder clearFrozen()
      ```

      ```
       the frozen balance for bandwidth
      ```

      `repeated .protocol.Account.Frozen frozen = 7;`
    - #### removeFrozen

      ```
      public Response.Account.Builder removeFrozen(int index)
      ```

      ```
       the frozen balance for bandwidth
      ```

      `repeated .protocol.Account.Frozen frozen = 7;`
    - #### getFrozenBuilder

      ```
      public Response.Account.Frozen.Builder getFrozenBuilder(int index)
      ```

      ```
       the frozen balance for bandwidth
      ```

      `repeated .protocol.Account.Frozen frozen = 7;`
    - #### getFrozenOrBuilder

      ```
      public Response.Account.FrozenOrBuilder getFrozenOrBuilder(int index)
      ```

      ```
       the frozen balance for bandwidth
      ```

      `repeated .protocol.Account.Frozen frozen = 7;`

      Specified by:
      :   `getFrozenOrBuilder` in interface `Response.AccountOrBuilder`
    - #### getFrozenOrBuilderList

      ```
      public java.util.List<? extends Response.Account.FrozenOrBuilder> getFrozenOrBuilderList()
      ```

      ```
       the frozen balance for bandwidth
      ```

      `repeated .protocol.Account.Frozen frozen = 7;`

      Specified by:
      :   `getFrozenOrBuilderList` in interface `Response.AccountOrBuilder`
    - #### addFrozenBuilder

      ```
      public Response.Account.Frozen.Builder addFrozenBuilder()
      ```

      ```
       the frozen balance for bandwidth
      ```

      `repeated .protocol.Account.Frozen frozen = 7;`
    - #### addFrozenBuilder

      ```
      public Response.Account.Frozen.Builder addFrozenBuilder(int index)
      ```

      ```
       the frozen balance for bandwidth
      ```

      `repeated .protocol.Account.Frozen frozen = 7;`
    - #### getFrozenBuilderList

      ```
      public java.util.List<Response.Account.Frozen.Builder> getFrozenBuilderList()
      ```

      ```
       the frozen balance for bandwidth
      ```

      `repeated .protocol.Account.Frozen frozen = 7;`
    - #### getNetUsage

      ```
      public long getNetUsage()
      ```

      ```
       bandwidth, get from frozen
      ```

      `int64 net_usage = 8;`

      Specified by:
      :   `getNetUsage` in interface `Response.AccountOrBuilder`

      Returns:
      :   The netUsage.
    - #### setNetUsage

      ```
      public Response.Account.Builder setNetUsage(long value)
      ```

      ```
       bandwidth, get from frozen
      ```

      `int64 net_usage = 8;`

      Parameters:
      :   `value` - The netUsage to set.

      Returns:
      :   This builder for chaining.
    - #### clearNetUsage

      ```
      public Response.Account.Builder clearNetUsage()
      ```

      ```
       bandwidth, get from frozen
      ```

      `int64 net_usage = 8;`

      Returns:
      :   This builder for chaining.
    - #### getAcquiredDelegatedFrozenBalanceForBandwidth

      ```
      public long getAcquiredDelegatedFrozenBalanceForBandwidth()
      ```

      ```
       Frozen balance provided by other accounts to this account
      ```

      `int64 acquired_delegated_frozen_balance_for_bandwidth = 41;`

      Specified by:
      :   `getAcquiredDelegatedFrozenBalanceForBandwidth` in interface `Response.AccountOrBuilder`

      Returns:
      :   The acquiredDelegatedFrozenBalanceForBandwidth.
    - #### setAcquiredDelegatedFrozenBalanceForBandwidth

      ```
      public Response.Account.Builder setAcquiredDelegatedFrozenBalanceForBandwidth(long value)
      ```

      ```
       Frozen balance provided by other accounts to this account
      ```

      `int64 acquired_delegated_frozen_balance_for_bandwidth = 41;`

      Parameters:
      :   `value` - The acquiredDelegatedFrozenBalanceForBandwidth to set.

      Returns:
      :   This builder for chaining.
    - #### clearAcquiredDelegatedFrozenBalanceForBandwidth

      ```
      public Response.Account.Builder clearAcquiredDelegatedFrozenBalanceForBandwidth()
      ```

      ```
       Frozen balance provided by other accounts to this account
      ```

      `int64 acquired_delegated_frozen_balance_for_bandwidth = 41;`

      Returns:
      :   This builder for chaining.
    - #### getDelegatedFrozenBalanceForBandwidth

      ```
      public long getDelegatedFrozenBalanceForBandwidth()
      ```

      ```
       Freeze and provide balances to other accounts
      ```

      `int64 delegated_frozen_balance_for_bandwidth = 42;`

      Specified by:
      :   `getDelegatedFrozenBalanceForBandwidth` in interface `Response.AccountOrBuilder`

      Returns:
      :   The delegatedFrozenBalanceForBandwidth.
    - #### setDelegatedFrozenBalanceForBandwidth

      ```
      public Response.Account.Builder setDelegatedFrozenBalanceForBandwidth(long value)
      ```

      ```
       Freeze and provide balances to other accounts
      ```

      `int64 delegated_frozen_balance_for_bandwidth = 42;`

      Parameters:
      :   `value` - The delegatedFrozenBalanceForBandwidth to set.

      Returns:
      :   This builder for chaining.
    - #### clearDelegatedFrozenBalanceForBandwidth

      ```
      public Response.Account.Builder clearDelegatedFrozenBalanceForBandwidth()
      ```

      ```
       Freeze and provide balances to other accounts
      ```

      `int64 delegated_frozen_balance_for_bandwidth = 42;`

      Returns:
      :   This builder for chaining.
    - #### getOldTronPower

      ```
      public long getOldTronPower()
      ```

      `int64 old_tron_power = 46;`

      Specified by:
      :   `getOldTronPower` in interface `Response.AccountOrBuilder`

      Returns:
      :   The oldTronPower.
    - #### setOldTronPower

      ```
      public Response.Account.Builder setOldTronPower(long value)
      ```

      `int64 old_tron_power = 46;`

      Parameters:
      :   `value` - The oldTronPower to set.

      Returns:
      :   This builder for chaining.
    - #### clearOldTronPower

      ```
      public Response.Account.Builder clearOldTronPower()
      ```

      `int64 old_tron_power = 46;`

      Returns:
      :   This builder for chaining.
    - #### hasTronPower

      ```
      public boolean hasTronPower()
      ```

      `.protocol.Account.Frozen tron_power = 47;`

      Specified by:
      :   `hasTronPower` in interface `Response.AccountOrBuilder`

      Returns:
      :   Whether the tronPower field is set.
    - #### getTronPower

      ```
      public Response.Account.Frozen getTronPower()
      ```

      `.protocol.Account.Frozen tron_power = 47;`

      Specified by:
      :   `getTronPower` in interface `Response.AccountOrBuilder`

      Returns:
      :   The tronPower.
    - #### setTronPower

      ```
      public Response.Account.Builder setTronPower(Response.Account.Frozen value)
      ```

      `.protocol.Account.Frozen tron_power = 47;`
    - #### setTronPower

      ```
      public Response.Account.Builder setTronPower(Response.Account.Frozen.Builder builderForValue)
      ```

      `.protocol.Account.Frozen tron_power = 47;`
    - #### mergeTronPower

      ```
      public Response.Account.Builder mergeTronPower(Response.Account.Frozen value)
      ```

      `.protocol.Account.Frozen tron_power = 47;`
    - #### clearTronPower

      ```
      public Response.Account.Builder clearTronPower()
      ```

      `.protocol.Account.Frozen tron_power = 47;`
    - #### getTronPowerBuilder

      ```
      public Response.Account.Frozen.Builder getTronPowerBuilder()
      ```

      `.protocol.Account.Frozen tron_power = 47;`
    - #### getTronPowerOrBuilder

      ```
      public Response.Account.FrozenOrBuilder getTronPowerOrBuilder()
      ```

      `.protocol.Account.Frozen tron_power = 47;`

      Specified by:
      :   `getTronPowerOrBuilder` in interface `Response.AccountOrBuilder`
    - #### getAssetOptimized

      ```
      public boolean getAssetOptimized()
      ```

      `bool asset_optimized = 60;`

      Specified by:
      :   `getAssetOptimized` in interface `Response.AccountOrBuilder`

      Returns:
      :   The assetOptimized.
    - #### setAssetOptimized

      ```
      public Response.Account.Builder setAssetOptimized(boolean value)
      ```

      `bool asset_optimized = 60;`

      Parameters:
      :   `value` - The assetOptimized to set.

      Returns:
      :   This builder for chaining.
    - #### clearAssetOptimized

      ```
      public Response.Account.Builder clearAssetOptimized()
      ```

      `bool asset_optimized = 60;`

      Returns:
      :   This builder for chaining.
    - #### getCreateTime

      ```
      public long getCreateTime()
      ```

      ```
       this account create time
      ```

      `int64 create_time = 9;`

      Specified by:
      :   `getCreateTime` in interface `Response.AccountOrBuilder`

      Returns:
      :   The createTime.
    - #### setCreateTime

      ```
      public Response.Account.Builder setCreateTime(long value)
      ```

      ```
       this account create time
      ```

      `int64 create_time = 9;`

      Parameters:
      :   `value` - The createTime to set.

      Returns:
      :   This builder for chaining.
    - #### clearCreateTime

      ```
      public Response.Account.Builder clearCreateTime()
      ```

      ```
       this account create time
      ```

      `int64 create_time = 9;`

      Returns:
      :   This builder for chaining.
    - #### getLatestOprationTime

      ```
      public long getLatestOprationTime()
      ```

      ```
       this last operation time, including transfer, voting and so on. //FIXME fix
       grammar
      ```

      `int64 latest_opration_time = 10;`

      Specified by:
      :   `getLatestOprationTime` in interface `Response.AccountOrBuilder`

      Returns:
      :   The latestOprationTime.
    - #### setLatestOprationTime

      ```
      public Response.Account.Builder setLatestOprationTime(long value)
      ```

      ```
       this last operation time, including transfer, voting and so on. //FIXME fix
       grammar
      ```

      `int64 latest_opration_time = 10;`

      Parameters:
      :   `value` - The latestOprationTime to set.

      Returns:
      :   This builder for chaining.
    - #### clearLatestOprationTime

      ```
      public Response.Account.Builder clearLatestOprationTime()
      ```

      ```
       this last operation time, including transfer, voting and so on. //FIXME fix
       grammar
      ```

      `int64 latest_opration_time = 10;`

      Returns:
      :   This builder for chaining.
    - #### getAllowance

      ```
      public long getAllowance()
      ```

      ```
       witness block producing allowance
      ```

      `int64 allowance = 11;`

      Specified by:
      :   `getAllowance` in interface `Response.AccountOrBuilder`

      Returns:
      :   The allowance.
    - #### setAllowance

      ```
      public Response.Account.Builder setAllowance(long value)
      ```

      ```
       witness block producing allowance
      ```

      `int64 allowance = 11;`

      Parameters:
      :   `value` - The allowance to set.

      Returns:
      :   This builder for chaining.
    - #### clearAllowance

      ```
      public Response.Account.Builder clearAllowance()
      ```

      ```
       witness block producing allowance
      ```

      `int64 allowance = 11;`

      Returns:
      :   This builder for chaining.
    - #### getLatestWithdrawTime

      ```
      public long getLatestWithdrawTime()
      ```

      ```
       last withdraw time
      ```

      `int64 latest_withdraw_time = 12;`

      Specified by:
      :   `getLatestWithdrawTime` in interface `Response.AccountOrBuilder`

      Returns:
      :   The latestWithdrawTime.
    - #### setLatestWithdrawTime

      ```
      public Response.Account.Builder setLatestWithdrawTime(long value)
      ```

      ```
       last withdraw time
      ```

      `int64 latest_withdraw_time = 12;`

      Parameters:
      :   `value` - The latestWithdrawTime to set.

      Returns:
      :   This builder for chaining.
    - #### clearLatestWithdrawTime

      ```
      public Response.Account.Builder clearLatestWithdrawTime()
      ```

      ```
       last withdraw time
      ```

      `int64 latest_withdraw_time = 12;`

      Returns:
      :   This builder for chaining.
    - #### getCode

      ```
      public com.google.protobuf.ByteString getCode()
      ```

      ```
       not used so far
      ```

      `bytes code = 13;`

      Specified by:
      :   `getCode` in interface `Response.AccountOrBuilder`

      Returns:
      :   The code.
    - #### setCode

      ```
      public Response.Account.Builder setCode(com.google.protobuf.ByteString value)
      ```

      ```
       not used so far
      ```

      `bytes code = 13;`

      Parameters:
      :   `value` - The code to set.

      Returns:
      :   This builder for chaining.
    - #### clearCode

      ```
      public Response.Account.Builder clearCode()
      ```

      ```
       not used so far
      ```

      `bytes code = 13;`

      Returns:
      :   This builder for chaining.
    - #### getIsWitness

      ```
      public boolean getIsWitness()
      ```

      `bool is_witness = 14;`

      Specified by:
      :   `getIsWitness` in interface `Response.AccountOrBuilder`

      Returns:
      :   The isWitness.
    - #### setIsWitness

      ```
      public Response.Account.Builder setIsWitness(boolean value)
      ```

      `bool is_witness = 14;`

      Parameters:
      :   `value` - The isWitness to set.

      Returns:
      :   This builder for chaining.
    - #### clearIsWitness

      ```
      public Response.Account.Builder clearIsWitness()
      ```

      `bool is_witness = 14;`

      Returns:
      :   This builder for chaining.
    - #### getIsCommittee

      ```
      public boolean getIsCommittee()
      ```

      `bool is_committee = 15;`

      Specified by:
      :   `getIsCommittee` in interface `Response.AccountOrBuilder`

      Returns:
      :   The isCommittee.
    - #### setIsCommittee

      ```
      public Response.Account.Builder setIsCommittee(boolean value)
      ```

      `bool is_committee = 15;`

      Parameters:
      :   `value` - The isCommittee to set.

      Returns:
      :   This builder for chaining.
    - #### clearIsCommittee

      ```
      public Response.Account.Builder clearIsCommittee()
      ```

      `bool is_committee = 15;`

      Returns:
      :   This builder for chaining.
    - #### getFrozenSupplyList

      ```
      public java.util.List<Response.Account.Frozen> getFrozenSupplyList()
      ```

      ```
       frozen asset(for asset issuer)
      ```

      `repeated .protocol.Account.Frozen frozen_supply = 16;`

      Specified by:
      :   `getFrozenSupplyList` in interface `Response.AccountOrBuilder`
    - #### getFrozenSupplyCount

      ```
      public int getFrozenSupplyCount()
      ```

      ```
       frozen asset(for asset issuer)
      ```

      `repeated .protocol.Account.Frozen frozen_supply = 16;`

      Specified by:
      :   `getFrozenSupplyCount` in interface `Response.AccountOrBuilder`
    - #### getFrozenSupply

      ```
      public Response.Account.Frozen getFrozenSupply(int index)
      ```

      ```
       frozen asset(for asset issuer)
      ```

      `repeated .protocol.Account.Frozen frozen_supply = 16;`

      Specified by:
      :   `getFrozenSupply` in interface `Response.AccountOrBuilder`
    - #### setFrozenSupply

      ```
      public Response.Account.Builder setFrozenSupply(int index,
                                                      Response.Account.Frozen value)
      ```

      ```
       frozen asset(for asset issuer)
      ```

      `repeated .protocol.Account.Frozen frozen_supply = 16;`
    - #### setFrozenSupply

      ```
      public Response.Account.Builder setFrozenSupply(int index,
                                                      Response.Account.Frozen.Builder builderForValue)
      ```

      ```
       frozen asset(for asset issuer)
      ```

      `repeated .protocol.Account.Frozen frozen_supply = 16;`
    - #### addFrozenSupply

      ```
      public Response.Account.Builder addFrozenSupply(Response.Account.Frozen value)
      ```

      ```
       frozen asset(for asset issuer)
      ```

      `repeated .protocol.Account.Frozen frozen_supply = 16;`
    - #### addFrozenSupply

      ```
      public Response.Account.Builder addFrozenSupply(int index,
                                                      Response.Account.Frozen value)
      ```

      ```
       frozen asset(for asset issuer)
      ```

      `repeated .protocol.Account.Frozen frozen_supply = 16;`
    - #### addFrozenSupply

      ```
      public Response.Account.Builder addFrozenSupply(Response.Account.Frozen.Builder builderForValue)
      ```

      ```
       frozen asset(for asset issuer)
      ```

      `repeated .protocol.Account.Frozen frozen_supply = 16;`
    - #### addFrozenSupply

      ```
      public Response.Account.Builder addFrozenSupply(int index,
                                                      Response.Account.Frozen.Builder builderForValue)
      ```

      ```
       frozen asset(for asset issuer)
      ```

      `repeated .protocol.Account.Frozen frozen_supply = 16;`
    - #### addAllFrozenSupply

      ```
      public Response.Account.Builder addAllFrozenSupply(java.lang.Iterable<? extends Response.Account.Frozen> values)
      ```

      ```
       frozen asset(for asset issuer)
      ```

      `repeated .protocol.Account.Frozen frozen_supply = 16;`
    - #### clearFrozenSupply

      ```
      public Response.Account.Builder clearFrozenSupply()
      ```

      ```
       frozen asset(for asset issuer)
      ```

      `repeated .protocol.Account.Frozen frozen_supply = 16;`
    - #### removeFrozenSupply

      ```
      public Response.Account.Builder removeFrozenSupply(int index)
      ```

      ```
       frozen asset(for asset issuer)
      ```

      `repeated .protocol.Account.Frozen frozen_supply = 16;`
    - #### getFrozenSupplyBuilder

      ```
      public Response.Account.Frozen.Builder getFrozenSupplyBuilder(int index)
      ```

      ```
       frozen asset(for asset issuer)
      ```

      `repeated .protocol.Account.Frozen frozen_supply = 16;`
    - #### getFrozenSupplyOrBuilder

      ```
      public Response.Account.FrozenOrBuilder getFrozenSupplyOrBuilder(int index)
      ```

      ```
       frozen asset(for asset issuer)
      ```

      `repeated .protocol.Account.Frozen frozen_supply = 16;`

      Specified by:
      :   `getFrozenSupplyOrBuilder` in interface `Response.AccountOrBuilder`
    - #### getFrozenSupplyOrBuilderList

      ```
      public java.util.List<? extends Response.Account.FrozenOrBuilder> getFrozenSupplyOrBuilderList()
      ```

      ```
       frozen asset(for asset issuer)
      ```

      `repeated .protocol.Account.Frozen frozen_supply = 16;`

      Specified by:
      :   `getFrozenSupplyOrBuilderList` in interface `Response.AccountOrBuilder`
    - #### addFrozenSupplyBuilder

      ```
      public Response.Account.Frozen.Builder addFrozenSupplyBuilder()
      ```

      ```
       frozen asset(for asset issuer)
      ```

      `repeated .protocol.Account.Frozen frozen_supply = 16;`
    - #### addFrozenSupplyBuilder

      ```
      public Response.Account.Frozen.Builder addFrozenSupplyBuilder(int index)
      ```

      ```
       frozen asset(for asset issuer)
      ```

      `repeated .protocol.Account.Frozen frozen_supply = 16;`
    - #### getFrozenSupplyBuilderList

      ```
      public java.util.List<Response.Account.Frozen.Builder> getFrozenSupplyBuilderList()
      ```

      ```
       frozen asset(for asset issuer)
      ```

      `repeated .protocol.Account.Frozen frozen_supply = 16;`
    - #### getAssetIssuedName

      ```
      public com.google.protobuf.ByteString getAssetIssuedName()
      ```

      ```
       asset_issued_name
      ```

      `bytes asset_issued_name = 17;`

      Specified by:
      :   `getAssetIssuedName` in interface `Response.AccountOrBuilder`

      Returns:
      :   The assetIssuedName.
    - #### setAssetIssuedName

      ```
      public Response.Account.Builder setAssetIssuedName(com.google.protobuf.ByteString value)
      ```

      ```
       asset_issued_name
      ```

      `bytes asset_issued_name = 17;`

      Parameters:
      :   `value` - The assetIssuedName to set.

      Returns:
      :   This builder for chaining.
    - #### clearAssetIssuedName

      ```
      public Response.Account.Builder clearAssetIssuedName()
      ```

      ```
       asset_issued_name
      ```

      `bytes asset_issued_name = 17;`

      Returns:
      :   This builder for chaining.
    - #### getAssetIssuedID

      ```
      public com.google.protobuf.ByteString getAssetIssuedID()
      ```

      `bytes asset_issued_ID = 57;`

      Specified by:
      :   `getAssetIssuedID` in interface `Response.AccountOrBuilder`

      Returns:
      :   The assetIssuedID.
    - #### setAssetIssuedID

      ```
      public Response.Account.Builder setAssetIssuedID(com.google.protobuf.ByteString value)
      ```

      `bytes asset_issued_ID = 57;`

      Parameters:
      :   `value` - The assetIssuedID to set.

      Returns:
      :   This builder for chaining.
    - #### clearAssetIssuedID

      ```
      public Response.Account.Builder clearAssetIssuedID()
      ```

      `bytes asset_issued_ID = 57;`

      Returns:
      :   This builder for chaining.
    - #### getLatestAssetOperationTimeCount

      ```
      public int getLatestAssetOperationTimeCount()
      ```

      Description copied from interface: `Response.AccountOrBuilder`

      `map<string, int64> latest_asset_operation_time = 18;`

      Specified by:
      :   `getLatestAssetOperationTimeCount` in interface `Response.AccountOrBuilder`
    - #### containsLatestAssetOperationTime

      ```
      public boolean containsLatestAssetOperationTime(java.lang.String key)
      ```

      `map<string, int64> latest_asset_operation_time = 18;`

      Specified by:
      :   `containsLatestAssetOperationTime` in interface `Response.AccountOrBuilder`
    - #### getLatestAssetOperationTime

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getLatestAssetOperationTime()
      ```

      Deprecated.

      Use [`getLatestAssetOperationTimeMap()`](../../../../org/tron/trident/proto/Response.Account.Builder.html#getLatestAssetOperationTimeMap--) instead.

      Specified by:
      :   `getLatestAssetOperationTime` in interface `Response.AccountOrBuilder`
    - #### getLatestAssetOperationTimeMap

      ```
      public java.util.Map<java.lang.String,java.lang.Long> getLatestAssetOperationTimeMap()
      ```

      `map<string, int64> latest_asset_operation_time = 18;`

      Specified by:
      :   `getLatestAssetOperationTimeMap` in interface `Response.AccountOrBuilder`
    - #### getLatestAssetOperationTimeOrDefault

      ```
      public long getLatestAssetOperationTimeOrDefault(java.lang.String key,
                                                       long defaultValue)
      ```

      `map<string, int64> latest_asset_operation_time = 18;`

      Specified by:
      :   `getLatestAssetOperationTimeOrDefault` in interface `Response.AccountOrBuilder`
    - #### getLatestAssetOperationTimeOrThrow

      ```
      public long getLatestAssetOperationTimeOrThrow(java.lang.String key)
      ```

      `map<string, int64> latest_asset_operation_time = 18;`

      Specified by:
      :   `getLatestAssetOperationTimeOrThrow` in interface `Response.AccountOrBuilder`
    - #### clearLatestAssetOperationTime

      ```
      public Response.Account.Builder clearLatestAssetOperationTime()
      ```
    - #### removeLatestAssetOperationTime

      ```
      public Response.Account.Builder removeLatestAssetOperationTime(java.lang.String key)
      ```

      `map<string, int64> latest_asset_operation_time = 18;`
    - #### getMutableLatestAssetOperationTime

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getMutableLatestAssetOperationTime()
      ```

      Deprecated.

      Use alternate mutation accessors instead.
    - #### putLatestAssetOperationTime

      ```
      public Response.Account.Builder putLatestAssetOperationTime(java.lang.String key,
                                                                  long value)
      ```

      `map<string, int64> latest_asset_operation_time = 18;`
    - #### putAllLatestAssetOperationTime

      ```
      public Response.Account.Builder putAllLatestAssetOperationTime(java.util.Map<java.lang.String,java.lang.Long> values)
      ```

      `map<string, int64> latest_asset_operation_time = 18;`
    - #### getLatestAssetOperationTimeV2Count

      ```
      public int getLatestAssetOperationTimeV2Count()
      ```

      Description copied from interface: `Response.AccountOrBuilder`

      `map<string, int64> latest_asset_operation_timeV2 = 58;`

      Specified by:
      :   `getLatestAssetOperationTimeV2Count` in interface `Response.AccountOrBuilder`
    - #### containsLatestAssetOperationTimeV2

      ```
      public boolean containsLatestAssetOperationTimeV2(java.lang.String key)
      ```

      `map<string, int64> latest_asset_operation_timeV2 = 58;`

      Specified by:
      :   `containsLatestAssetOperationTimeV2` in interface `Response.AccountOrBuilder`
    - #### getLatestAssetOperationTimeV2

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getLatestAssetOperationTimeV2()
      ```

      Deprecated.

      Use [`getLatestAssetOperationTimeV2Map()`](../../../../org/tron/trident/proto/Response.Account.Builder.html#getLatestAssetOperationTimeV2Map--) instead.

      Specified by:
      :   `getLatestAssetOperationTimeV2` in interface `Response.AccountOrBuilder`
    - #### getLatestAssetOperationTimeV2Map

      ```
      public java.util.Map<java.lang.String,java.lang.Long> getLatestAssetOperationTimeV2Map()
      ```

      `map<string, int64> latest_asset_operation_timeV2 = 58;`

      Specified by:
      :   `getLatestAssetOperationTimeV2Map` in interface `Response.AccountOrBuilder`
    - #### getLatestAssetOperationTimeV2OrDefault

      ```
      public long getLatestAssetOperationTimeV2OrDefault(java.lang.String key,
                                                         long defaultValue)
      ```

      `map<string, int64> latest_asset_operation_timeV2 = 58;`

      Specified by:
      :   `getLatestAssetOperationTimeV2OrDefault` in interface `Response.AccountOrBuilder`
    - #### getLatestAssetOperationTimeV2OrThrow

      ```
      public long getLatestAssetOperationTimeV2OrThrow(java.lang.String key)
      ```

      `map<string, int64> latest_asset_operation_timeV2 = 58;`

      Specified by:
      :   `getLatestAssetOperationTimeV2OrThrow` in interface `Response.AccountOrBuilder`
    - #### clearLatestAssetOperationTimeV2

      ```
      public Response.Account.Builder clearLatestAssetOperationTimeV2()
      ```
    - #### removeLatestAssetOperationTimeV2

      ```
      public Response.Account.Builder removeLatestAssetOperationTimeV2(java.lang.String key)
      ```

      `map<string, int64> latest_asset_operation_timeV2 = 58;`
    - #### getMutableLatestAssetOperationTimeV2

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getMutableLatestAssetOperationTimeV2()
      ```

      Deprecated.

      Use alternate mutation accessors instead.
    - #### putLatestAssetOperationTimeV2

      ```
      public Response.Account.Builder putLatestAssetOperationTimeV2(java.lang.String key,
                                                                    long value)
      ```

      `map<string, int64> latest_asset_operation_timeV2 = 58;`
    - #### putAllLatestAssetOperationTimeV2

      ```
      public Response.Account.Builder putAllLatestAssetOperationTimeV2(java.util.Map<java.lang.String,java.lang.Long> values)
      ```

      `map<string, int64> latest_asset_operation_timeV2 = 58;`
    - #### getFreeNetUsage

      ```
      public long getFreeNetUsage()
      ```

      `int64 free_net_usage = 19;`

      Specified by:
      :   `getFreeNetUsage` in interface `Response.AccountOrBuilder`

      Returns:
      :   The freeNetUsage.
    - #### setFreeNetUsage

      ```
      public Response.Account.Builder setFreeNetUsage(long value)
      ```

      `int64 free_net_usage = 19;`

      Parameters:
      :   `value` - The freeNetUsage to set.

      Returns:
      :   This builder for chaining.
    - #### clearFreeNetUsage

      ```
      public Response.Account.Builder clearFreeNetUsage()
      ```

      `int64 free_net_usage = 19;`

      Returns:
      :   This builder for chaining.
    - #### getFreeAssetNetUsageCount

      ```
      public int getFreeAssetNetUsageCount()
      ```

      Description copied from interface: `Response.AccountOrBuilder`

      `map<string, int64> free_asset_net_usage = 20;`

      Specified by:
      :   `getFreeAssetNetUsageCount` in interface `Response.AccountOrBuilder`
    - #### containsFreeAssetNetUsage

      ```
      public boolean containsFreeAssetNetUsage(java.lang.String key)
      ```

      `map<string, int64> free_asset_net_usage = 20;`

      Specified by:
      :   `containsFreeAssetNetUsage` in interface `Response.AccountOrBuilder`
    - #### getFreeAssetNetUsage

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getFreeAssetNetUsage()
      ```

      Deprecated.

      Use [`getFreeAssetNetUsageMap()`](../../../../org/tron/trident/proto/Response.Account.Builder.html#getFreeAssetNetUsageMap--) instead.

      Specified by:
      :   `getFreeAssetNetUsage` in interface `Response.AccountOrBuilder`
    - #### getFreeAssetNetUsageMap

      ```
      public java.util.Map<java.lang.String,java.lang.Long> getFreeAssetNetUsageMap()
      ```

      `map<string, int64> free_asset_net_usage = 20;`

      Specified by:
      :   `getFreeAssetNetUsageMap` in interface `Response.AccountOrBuilder`
    - #### getFreeAssetNetUsageOrDefault

      ```
      public long getFreeAssetNetUsageOrDefault(java.lang.String key,
                                                long defaultValue)
      ```

      `map<string, int64> free_asset_net_usage = 20;`

      Specified by:
      :   `getFreeAssetNetUsageOrDefault` in interface `Response.AccountOrBuilder`
    - #### getFreeAssetNetUsageOrThrow

      ```
      public long getFreeAssetNetUsageOrThrow(java.lang.String key)
      ```

      `map<string, int64> free_asset_net_usage = 20;`

      Specified by:
      :   `getFreeAssetNetUsageOrThrow` in interface `Response.AccountOrBuilder`
    - #### clearFreeAssetNetUsage

      ```
      public Response.Account.Builder clearFreeAssetNetUsage()
      ```
    - #### removeFreeAssetNetUsage

      ```
      public Response.Account.Builder removeFreeAssetNetUsage(java.lang.String key)
      ```

      `map<string, int64> free_asset_net_usage = 20;`
    - #### getMutableFreeAssetNetUsage

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getMutableFreeAssetNetUsage()
      ```

      Deprecated.

      Use alternate mutation accessors instead.
    - #### putFreeAssetNetUsage

      ```
      public Response.Account.Builder putFreeAssetNetUsage(java.lang.String key,
                                                           long value)
      ```

      `map<string, int64> free_asset_net_usage = 20;`
    - #### putAllFreeAssetNetUsage

      ```
      public Response.Account.Builder putAllFreeAssetNetUsage(java.util.Map<java.lang.String,java.lang.Long> values)
      ```

      `map<string, int64> free_asset_net_usage = 20;`
    - #### getFreeAssetNetUsageV2Count

      ```
      public int getFreeAssetNetUsageV2Count()
      ```

      Description copied from interface: `Response.AccountOrBuilder`

      `map<string, int64> free_asset_net_usageV2 = 59;`

      Specified by:
      :   `getFreeAssetNetUsageV2Count` in interface `Response.AccountOrBuilder`
    - #### containsFreeAssetNetUsageV2

      ```
      public boolean containsFreeAssetNetUsageV2(java.lang.String key)
      ```

      `map<string, int64> free_asset_net_usageV2 = 59;`

      Specified by:
      :   `containsFreeAssetNetUsageV2` in interface `Response.AccountOrBuilder`
    - #### getFreeAssetNetUsageV2

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getFreeAssetNetUsageV2()
      ```

      Deprecated.

      Use [`getFreeAssetNetUsageV2Map()`](../../../../org/tron/trident/proto/Response.Account.Builder.html#getFreeAssetNetUsageV2Map--) instead.

      Specified by:
      :   `getFreeAssetNetUsageV2` in interface `Response.AccountOrBuilder`
    - #### getFreeAssetNetUsageV2Map

      ```
      public java.util.Map<java.lang.String,java.lang.Long> getFreeAssetNetUsageV2Map()
      ```

      `map<string, int64> free_asset_net_usageV2 = 59;`

      Specified by:
      :   `getFreeAssetNetUsageV2Map` in interface `Response.AccountOrBuilder`
    - #### getFreeAssetNetUsageV2OrDefault

      ```
      public long getFreeAssetNetUsageV2OrDefault(java.lang.String key,
                                                  long defaultValue)
      ```

      `map<string, int64> free_asset_net_usageV2 = 59;`

      Specified by:
      :   `getFreeAssetNetUsageV2OrDefault` in interface `Response.AccountOrBuilder`
    - #### getFreeAssetNetUsageV2OrThrow

      ```
      public long getFreeAssetNetUsageV2OrThrow(java.lang.String key)
      ```

      `map<string, int64> free_asset_net_usageV2 = 59;`

      Specified by:
      :   `getFreeAssetNetUsageV2OrThrow` in interface `Response.AccountOrBuilder`
    - #### clearFreeAssetNetUsageV2

      ```
      public Response.Account.Builder clearFreeAssetNetUsageV2()
      ```
    - #### removeFreeAssetNetUsageV2

      ```
      public Response.Account.Builder removeFreeAssetNetUsageV2(java.lang.String key)
      ```

      `map<string, int64> free_asset_net_usageV2 = 59;`
    - #### getMutableFreeAssetNetUsageV2

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getMutableFreeAssetNetUsageV2()
      ```

      Deprecated.

      Use alternate mutation accessors instead.
    - #### putFreeAssetNetUsageV2

      ```
      public Response.Account.Builder putFreeAssetNetUsageV2(java.lang.String key,
                                                             long value)
      ```

      `map<string, int64> free_asset_net_usageV2 = 59;`
    - #### putAllFreeAssetNetUsageV2

      ```
      public Response.Account.Builder putAllFreeAssetNetUsageV2(java.util.Map<java.lang.String,java.lang.Long> values)
      ```

      `map<string, int64> free_asset_net_usageV2 = 59;`
    - #### getLatestConsumeTime

      ```
      public long getLatestConsumeTime()
      ```

      `int64 latest_consume_time = 21;`

      Specified by:
      :   `getLatestConsumeTime` in interface `Response.AccountOrBuilder`

      Returns:
      :   The latestConsumeTime.
    - #### setLatestConsumeTime

      ```
      public Response.Account.Builder setLatestConsumeTime(long value)
      ```

      `int64 latest_consume_time = 21;`

      Parameters:
      :   `value` - The latestConsumeTime to set.

      Returns:
      :   This builder for chaining.
    - #### clearLatestConsumeTime

      ```
      public Response.Account.Builder clearLatestConsumeTime()
      ```

      `int64 latest_consume_time = 21;`

      Returns:
      :   This builder for chaining.
    - #### getLatestConsumeFreeTime

      ```
      public long getLatestConsumeFreeTime()
      ```

      `int64 latest_consume_free_time = 22;`

      Specified by:
      :   `getLatestConsumeFreeTime` in interface `Response.AccountOrBuilder`

      Returns:
      :   The latestConsumeFreeTime.
    - #### setLatestConsumeFreeTime

      ```
      public Response.Account.Builder setLatestConsumeFreeTime(long value)
      ```

      `int64 latest_consume_free_time = 22;`

      Parameters:
      :   `value` - The latestConsumeFreeTime to set.

      Returns:
      :   This builder for chaining.
    - #### clearLatestConsumeFreeTime

      ```
      public Response.Account.Builder clearLatestConsumeFreeTime()
      ```

      `int64 latest_consume_free_time = 22;`

      Returns:
      :   This builder for chaining.
    - #### getAccountId

      ```
      public com.google.protobuf.ByteString getAccountId()
      ```

      ```
       the identity of this account, case insensitive
      ```

      `bytes account_id = 23;`

      Specified by:
      :   `getAccountId` in interface `Response.AccountOrBuilder`

      Returns:
      :   The accountId.
    - #### setAccountId

      ```
      public Response.Account.Builder setAccountId(com.google.protobuf.ByteString value)
      ```

      ```
       the identity of this account, case insensitive
      ```

      `bytes account_id = 23;`

      Parameters:
      :   `value` - The accountId to set.

      Returns:
      :   This builder for chaining.
    - #### clearAccountId

      ```
      public Response.Account.Builder clearAccountId()
      ```

      ```
       the identity of this account, case insensitive
      ```

      `bytes account_id = 23;`

      Returns:
      :   This builder for chaining.
    - #### getNetWindowSize

      ```
      public long getNetWindowSize()
      ```

      `int64 net_window_size = 24;`

      Specified by:
      :   `getNetWindowSize` in interface `Response.AccountOrBuilder`

      Returns:
      :   The netWindowSize.
    - #### setNetWindowSize

      ```
      public Response.Account.Builder setNetWindowSize(long value)
      ```

      `int64 net_window_size = 24;`

      Parameters:
      :   `value` - The netWindowSize to set.

      Returns:
      :   This builder for chaining.
    - #### clearNetWindowSize

      ```
      public Response.Account.Builder clearNetWindowSize()
      ```

      `int64 net_window_size = 24;`

      Returns:
      :   This builder for chaining.
    - #### getNetWindowOptimized

      ```
      public boolean getNetWindowOptimized()
      ```

      `bool net_window_optimized = 25;`

      Specified by:
      :   `getNetWindowOptimized` in interface `Response.AccountOrBuilder`

      Returns:
      :   The netWindowOptimized.
    - #### setNetWindowOptimized

      ```
      public Response.Account.Builder setNetWindowOptimized(boolean value)
      ```

      `bool net_window_optimized = 25;`

      Parameters:
      :   `value` - The netWindowOptimized to set.

      Returns:
      :   This builder for chaining.
    - #### clearNetWindowOptimized

      ```
      public Response.Account.Builder clearNetWindowOptimized()
      ```

      `bool net_window_optimized = 25;`

      Returns:
      :   This builder for chaining.
    - #### hasAccountResource

      ```
      public boolean hasAccountResource()
      ```

      `.protocol.Account.AccountResource account_resource = 26;`

      Specified by:
      :   `hasAccountResource` in interface `Response.AccountOrBuilder`

      Returns:
      :   Whether the accountResource field is set.
    - #### getAccountResource

      ```
      public Response.Account.AccountResource getAccountResource()
      ```

      `.protocol.Account.AccountResource account_resource = 26;`

      Specified by:
      :   `getAccountResource` in interface `Response.AccountOrBuilder`

      Returns:
      :   The accountResource.
    - #### setAccountResource

      ```
      public Response.Account.Builder setAccountResource(Response.Account.AccountResource value)
      ```

      `.protocol.Account.AccountResource account_resource = 26;`
    - #### setAccountResource

      ```
      public Response.Account.Builder setAccountResource(Response.Account.AccountResource.Builder builderForValue)
      ```

      `.protocol.Account.AccountResource account_resource = 26;`
    - #### mergeAccountResource

      ```
      public Response.Account.Builder mergeAccountResource(Response.Account.AccountResource value)
      ```

      `.protocol.Account.AccountResource account_resource = 26;`
    - #### clearAccountResource

      ```
      public Response.Account.Builder clearAccountResource()
      ```

      `.protocol.Account.AccountResource account_resource = 26;`
    - #### getAccountResourceBuilder

      ```
      public Response.Account.AccountResource.Builder getAccountResourceBuilder()
      ```

      `.protocol.Account.AccountResource account_resource = 26;`
    - #### getAccountResourceOrBuilder

      ```
      public Response.Account.AccountResourceOrBuilder getAccountResourceOrBuilder()
      ```

      `.protocol.Account.AccountResource account_resource = 26;`

      Specified by:
      :   `getAccountResourceOrBuilder` in interface `Response.AccountOrBuilder`
    - #### getCodeHash

      ```
      public com.google.protobuf.ByteString getCodeHash()
      ```

      `bytes codeHash = 30;`

      Specified by:
      :   `getCodeHash` in interface `Response.AccountOrBuilder`

      Returns:
      :   The codeHash.
    - #### setCodeHash

      ```
      public Response.Account.Builder setCodeHash(com.google.protobuf.ByteString value)
      ```

      `bytes codeHash = 30;`

      Parameters:
      :   `value` - The codeHash to set.

      Returns:
      :   This builder for chaining.
    - #### clearCodeHash

      ```
      public Response.Account.Builder clearCodeHash()
      ```

      `bytes codeHash = 30;`

      Returns:
      :   This builder for chaining.
    - #### hasOwnerPermission

      ```
      public boolean hasOwnerPermission()
      ```

      `.protocol.Permission owner_permission = 31;`

      Specified by:
      :   `hasOwnerPermission` in interface `Response.AccountOrBuilder`

      Returns:
      :   Whether the ownerPermission field is set.
    - #### getOwnerPermission

      ```
      public Common.Permission getOwnerPermission()
      ```

      `.protocol.Permission owner_permission = 31;`

      Specified by:
      :   `getOwnerPermission` in interface `Response.AccountOrBuilder`

      Returns:
      :   The ownerPermission.
    - #### setOwnerPermission

      ```
      public Response.Account.Builder setOwnerPermission(Common.Permission value)
      ```

      `.protocol.Permission owner_permission = 31;`
    - #### setOwnerPermission

      ```
      public Response.Account.Builder setOwnerPermission(Common.Permission.Builder builderForValue)
      ```

      `.protocol.Permission owner_permission = 31;`
    - #### mergeOwnerPermission

      ```
      public Response.Account.Builder mergeOwnerPermission(Common.Permission value)
      ```

      `.protocol.Permission owner_permission = 31;`
    - #### clearOwnerPermission

      ```
      public Response.Account.Builder clearOwnerPermission()
      ```

      `.protocol.Permission owner_permission = 31;`
    - #### getOwnerPermissionBuilder

      ```
      public Common.Permission.Builder getOwnerPermissionBuilder()
      ```

      `.protocol.Permission owner_permission = 31;`
    - #### getOwnerPermissionOrBuilder

      ```
      public Common.PermissionOrBuilder getOwnerPermissionOrBuilder()
      ```

      `.protocol.Permission owner_permission = 31;`

      Specified by:
      :   `getOwnerPermissionOrBuilder` in interface `Response.AccountOrBuilder`
    - #### hasWitnessPermission

      ```
      public boolean hasWitnessPermission()
      ```

      `.protocol.Permission witness_permission = 32;`

      Specified by:
      :   `hasWitnessPermission` in interface `Response.AccountOrBuilder`

      Returns:
      :   Whether the witnessPermission field is set.
    - #### getWitnessPermission

      ```
      public Common.Permission getWitnessPermission()
      ```

      `.protocol.Permission witness_permission = 32;`

      Specified by:
      :   `getWitnessPermission` in interface `Response.AccountOrBuilder`

      Returns:
      :   The witnessPermission.
    - #### setWitnessPermission

      ```
      public Response.Account.Builder setWitnessPermission(Common.Permission value)
      ```

      `.protocol.Permission witness_permission = 32;`
    - #### setWitnessPermission

      ```
      public Response.Account.Builder setWitnessPermission(Common.Permission.Builder builderForValue)
      ```

      `.protocol.Permission witness_permission = 32;`
    - #### mergeWitnessPermission

      ```
      public Response.Account.Builder mergeWitnessPermission(Common.Permission value)
      ```

      `.protocol.Permission witness_permission = 32;`
    - #### clearWitnessPermission

      ```
      public Response.Account.Builder clearWitnessPermission()
      ```

      `.protocol.Permission witness_permission = 32;`
    - #### getWitnessPermissionBuilder

      ```
      public Common.Permission.Builder getWitnessPermissionBuilder()
      ```

      `.protocol.Permission witness_permission = 32;`
    - #### getWitnessPermissionOrBuilder

      ```
      public Common.PermissionOrBuilder getWitnessPermissionOrBuilder()
      ```

      `.protocol.Permission witness_permission = 32;`

      Specified by:
      :   `getWitnessPermissionOrBuilder` in interface `Response.AccountOrBuilder`
    - #### getActivePermissionList

      ```
      public java.util.List<Common.Permission> getActivePermissionList()
      ```

      `repeated .protocol.Permission active_permission = 33;`

      Specified by:
      :   `getActivePermissionList` in interface `Response.AccountOrBuilder`
    - #### getActivePermissionCount

      ```
      public int getActivePermissionCount()
      ```

      `repeated .protocol.Permission active_permission = 33;`

      Specified by:
      :   `getActivePermissionCount` in interface `Response.AccountOrBuilder`
    - #### getActivePermission

      ```
      public Common.Permission getActivePermission(int index)
      ```

      `repeated .protocol.Permission active_permission = 33;`

      Specified by:
      :   `getActivePermission` in interface `Response.AccountOrBuilder`
    - #### setActivePermission

      ```
      public Response.Account.Builder setActivePermission(int index,
                                                          Common.Permission value)
      ```

      `repeated .protocol.Permission active_permission = 33;`
    - #### setActivePermission

      ```
      public Response.Account.Builder setActivePermission(int index,
                                                          Common.Permission.Builder builderForValue)
      ```

      `repeated .protocol.Permission active_permission = 33;`
    - #### addActivePermission

      ```
      public Response.Account.Builder addActivePermission(Common.Permission value)
      ```

      `repeated .protocol.Permission active_permission = 33;`
    - #### addActivePermission

      ```
      public Response.Account.Builder addActivePermission(int index,
                                                          Common.Permission value)
      ```

      `repeated .protocol.Permission active_permission = 33;`
    - #### addActivePermission

      ```
      public Response.Account.Builder addActivePermission(Common.Permission.Builder builderForValue)
      ```

      `repeated .protocol.Permission active_permission = 33;`
    - #### addActivePermission

      ```
      public Response.Account.Builder addActivePermission(int index,
                                                          Common.Permission.Builder builderForValue)
      ```

      `repeated .protocol.Permission active_permission = 33;`
    - #### addAllActivePermission

      ```
      public Response.Account.Builder addAllActivePermission(java.lang.Iterable<? extends Common.Permission> values)
      ```

      `repeated .protocol.Permission active_permission = 33;`
    - #### clearActivePermission

      ```
      public Response.Account.Builder clearActivePermission()
      ```

      `repeated .protocol.Permission active_permission = 33;`
    - #### removeActivePermission

      ```
      public Response.Account.Builder removeActivePermission(int index)
      ```

      `repeated .protocol.Permission active_permission = 33;`
    - #### getActivePermissionBuilder

      ```
      public Common.Permission.Builder getActivePermissionBuilder(int index)
      ```

      `repeated .protocol.Permission active_permission = 33;`
    - #### getActivePermissionOrBuilder

      ```
      public Common.PermissionOrBuilder getActivePermissionOrBuilder(int index)
      ```

      `repeated .protocol.Permission active_permission = 33;`

      Specified by:
      :   `getActivePermissionOrBuilder` in interface `Response.AccountOrBuilder`
    - #### getActivePermissionOrBuilderList

      ```
      public java.util.List<? extends Common.PermissionOrBuilder> getActivePermissionOrBuilderList()
      ```

      `repeated .protocol.Permission active_permission = 33;`

      Specified by:
      :   `getActivePermissionOrBuilderList` in interface `Response.AccountOrBuilder`
    - #### addActivePermissionBuilder

      ```
      public Common.Permission.Builder addActivePermissionBuilder()
      ```

      `repeated .protocol.Permission active_permission = 33;`
    - #### addActivePermissionBuilder

      ```
      public Common.Permission.Builder addActivePermissionBuilder(int index)
      ```

      `repeated .protocol.Permission active_permission = 33;`
    - #### getActivePermissionBuilderList

      ```
      public java.util.List<Common.Permission.Builder> getActivePermissionBuilderList()
      ```

      `repeated .protocol.Permission active_permission = 33;`
    - #### getFrozenV2List

      ```
      public java.util.List<Response.Account.FreezeV2> getFrozenV2List()
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`

      Specified by:
      :   `getFrozenV2List` in interface `Response.AccountOrBuilder`
    - #### getFrozenV2Count

      ```
      public int getFrozenV2Count()
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`

      Specified by:
      :   `getFrozenV2Count` in interface `Response.AccountOrBuilder`
    - #### getFrozenV2

      ```
      public Response.Account.FreezeV2 getFrozenV2(int index)
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`

      Specified by:
      :   `getFrozenV2` in interface `Response.AccountOrBuilder`
    - #### setFrozenV2

      ```
      public Response.Account.Builder setFrozenV2(int index,
                                                  Response.Account.FreezeV2 value)
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`
    - #### setFrozenV2

      ```
      public Response.Account.Builder setFrozenV2(int index,
                                                  Response.Account.FreezeV2.Builder builderForValue)
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`
    - #### addFrozenV2

      ```
      public Response.Account.Builder addFrozenV2(Response.Account.FreezeV2 value)
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`
    - #### addFrozenV2

      ```
      public Response.Account.Builder addFrozenV2(int index,
                                                  Response.Account.FreezeV2 value)
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`
    - #### addFrozenV2

      ```
      public Response.Account.Builder addFrozenV2(Response.Account.FreezeV2.Builder builderForValue)
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`
    - #### addFrozenV2

      ```
      public Response.Account.Builder addFrozenV2(int index,
                                                  Response.Account.FreezeV2.Builder builderForValue)
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`
    - #### addAllFrozenV2

      ```
      public Response.Account.Builder addAllFrozenV2(java.lang.Iterable<? extends Response.Account.FreezeV2> values)
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`
    - #### clearFrozenV2

      ```
      public Response.Account.Builder clearFrozenV2()
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`
    - #### removeFrozenV2

      ```
      public Response.Account.Builder removeFrozenV2(int index)
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`
    - #### getFrozenV2Builder

      ```
      public Response.Account.FreezeV2.Builder getFrozenV2Builder(int index)
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`
    - #### getFrozenV2OrBuilder

      ```
      public Response.Account.FreezeV2OrBuilder getFrozenV2OrBuilder(int index)
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`

      Specified by:
      :   `getFrozenV2OrBuilder` in interface `Response.AccountOrBuilder`
    - #### getFrozenV2OrBuilderList

      ```
      public java.util.List<? extends Response.Account.FreezeV2OrBuilder> getFrozenV2OrBuilderList()
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`

      Specified by:
      :   `getFrozenV2OrBuilderList` in interface `Response.AccountOrBuilder`
    - #### addFrozenV2Builder

      ```
      public Response.Account.FreezeV2.Builder addFrozenV2Builder()
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`
    - #### addFrozenV2Builder

      ```
      public Response.Account.FreezeV2.Builder addFrozenV2Builder(int index)
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`
    - #### getFrozenV2BuilderList

      ```
      public java.util.List<Response.Account.FreezeV2.Builder> getFrozenV2BuilderList()
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`
    - #### getUnfrozenV2List

      ```
      public java.util.List<Response.Account.UnFreezeV2> getUnfrozenV2List()
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`

      Specified by:
      :   `getUnfrozenV2List` in interface `Response.AccountOrBuilder`
    - #### getUnfrozenV2Count

      ```
      public int getUnfrozenV2Count()
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`

      Specified by:
      :   `getUnfrozenV2Count` in interface `Response.AccountOrBuilder`
    - #### getUnfrozenV2

      ```
      public Response.Account.UnFreezeV2 getUnfrozenV2(int index)
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`

      Specified by:
      :   `getUnfrozenV2` in interface `Response.AccountOrBuilder`
    - #### setUnfrozenV2

      ```
      public Response.Account.Builder setUnfrozenV2(int index,
                                                    Response.Account.UnFreezeV2 value)
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`
    - #### setUnfrozenV2

      ```
      public Response.Account.Builder setUnfrozenV2(int index,
                                                    Response.Account.UnFreezeV2.Builder builderForValue)
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`
    - #### addUnfrozenV2

      ```
      public Response.Account.Builder addUnfrozenV2(Response.Account.UnFreezeV2 value)
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`
    - #### addUnfrozenV2

      ```
      public Response.Account.Builder addUnfrozenV2(int index,
                                                    Response.Account.UnFreezeV2 value)
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`
    - #### addUnfrozenV2

      ```
      public Response.Account.Builder addUnfrozenV2(Response.Account.UnFreezeV2.Builder builderForValue)
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`
    - #### addUnfrozenV2

      ```
      public Response.Account.Builder addUnfrozenV2(int index,
                                                    Response.Account.UnFreezeV2.Builder builderForValue)
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`
    - #### addAllUnfrozenV2

      ```
      public Response.Account.Builder addAllUnfrozenV2(java.lang.Iterable<? extends Response.Account.UnFreezeV2> values)
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`
    - #### clearUnfrozenV2

      ```
      public Response.Account.Builder clearUnfrozenV2()
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`
    - #### removeUnfrozenV2

      ```
      public Response.Account.Builder removeUnfrozenV2(int index)
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`
    - #### getUnfrozenV2Builder

      ```
      public Response.Account.UnFreezeV2.Builder getUnfrozenV2Builder(int index)
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`
    - #### getUnfrozenV2OrBuilder

      ```
      public Response.Account.UnFreezeV2OrBuilder getUnfrozenV2OrBuilder(int index)
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`

      Specified by:
      :   `getUnfrozenV2OrBuilder` in interface `Response.AccountOrBuilder`
    - #### getUnfrozenV2OrBuilderList

      ```
      public java.util.List<? extends Response.Account.UnFreezeV2OrBuilder> getUnfrozenV2OrBuilderList()
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`

      Specified by:
      :   `getUnfrozenV2OrBuilderList` in interface `Response.AccountOrBuilder`
    - #### addUnfrozenV2Builder

      ```
      public Response.Account.UnFreezeV2.Builder addUnfrozenV2Builder()
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`
    - #### addUnfrozenV2Builder

      ```
      public Response.Account.UnFreezeV2.Builder addUnfrozenV2Builder(int index)
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`
    - #### getUnfrozenV2BuilderList

      ```
      public java.util.List<Response.Account.UnFreezeV2.Builder> getUnfrozenV2BuilderList()
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`
    - #### getDelegatedFrozenV2BalanceForBandwidth

      ```
      public long getDelegatedFrozenV2BalanceForBandwidth()
      ```

      `int64 delegated_frozenV2_balance_for_bandwidth = 36;`

      Specified by:
      :   `getDelegatedFrozenV2BalanceForBandwidth` in interface `Response.AccountOrBuilder`

      Returns:
      :   The delegatedFrozenV2BalanceForBandwidth.
    - #### setDelegatedFrozenV2BalanceForBandwidth

      ```
      public Response.Account.Builder setDelegatedFrozenV2BalanceForBandwidth(long value)
      ```

      `int64 delegated_frozenV2_balance_for_bandwidth = 36;`

      Parameters:
      :   `value` - The delegatedFrozenV2BalanceForBandwidth to set.

      Returns:
      :   This builder for chaining.
    - #### clearDelegatedFrozenV2BalanceForBandwidth

      ```
      public Response.Account.Builder clearDelegatedFrozenV2BalanceForBandwidth()
      ```

      `int64 delegated_frozenV2_balance_for_bandwidth = 36;`

      Returns:
      :   This builder for chaining.
    - #### getAcquiredDelegatedFrozenV2BalanceForBandwidth

      ```
      public long getAcquiredDelegatedFrozenV2BalanceForBandwidth()
      ```

      `int64 acquired_delegated_frozenV2_balance_for_bandwidth = 37;`

      Specified by:
      :   `getAcquiredDelegatedFrozenV2BalanceForBandwidth` in interface `Response.AccountOrBuilder`

      Returns:
      :   The acquiredDelegatedFrozenV2BalanceForBandwidth.
    - #### setAcquiredDelegatedFrozenV2BalanceForBandwidth

      ```
      public Response.Account.Builder setAcquiredDelegatedFrozenV2BalanceForBandwidth(long value)
      ```

      `int64 acquired_delegated_frozenV2_balance_for_bandwidth = 37;`

      Parameters:
      :   `value` - The acquiredDelegatedFrozenV2BalanceForBandwidth to set.

      Returns:
      :   This builder for chaining.
    - #### clearAcquiredDelegatedFrozenV2BalanceForBandwidth

      ```
      public Response.Account.Builder clearAcquiredDelegatedFrozenV2BalanceForBandwidth()
      ```

      `int64 acquired_delegated_frozenV2_balance_for_bandwidth = 37;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.Account.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.Account.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Builder>`