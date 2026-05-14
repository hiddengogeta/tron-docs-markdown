

org.tron.trident.proto

## Class Response.Account

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.Account

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.AccountOrBuilder](../../../../org/tron/trident/proto/Response.AccountOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.Account
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.AccountOrBuilder
  ```

  ```
   Account
  ```

  Protobuf type `protocol.Account`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.Account)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.Account.AccountResource` Protobuf type `protocol.Account.AccountResource` |
    | `static interface` | `Response.Account.AccountResourceOrBuilder` |
    | `static class` | `Response.Account.Builder` Account |
    | `static class` | `Response.Account.FreezeV2` Protobuf type `protocol.Account.FreezeV2` |
    | `static interface` | `Response.Account.FreezeV2OrBuilder` |
    | `static class` | `Response.Account.Frozen` frozen balance |
    | `static interface` | `Response.Account.FrozenOrBuilder` |
    | `static class` | `Response.Account.UnFreezeV2` Protobuf type `protocol.Account.UnFreezeV2` |
    | `static interface` | `Response.Account.UnFreezeV2OrBuilder` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `ACCOUNT_ID_FIELD_NUMBER` |
    | `static int` | `ACCOUNT_NAME_FIELD_NUMBER` |
    | `static int` | `ACCOUNT_RESOURCE_FIELD_NUMBER` |
    | `static int` | `ACQUIRED_DELEGATED_FROZEN_BALANCE_FOR_BANDWIDTH_FIELD_NUMBER` |
    | `static int` | `ACQUIRED_DELEGATED_FROZENV2_BALANCE_FOR_BANDWIDTH_FIELD_NUMBER` |
    | `static int` | `ACTIVE_PERMISSION_FIELD_NUMBER` |
    | `static int` | `ADDRESS_FIELD_NUMBER` |
    | `static int` | `ALLOWANCE_FIELD_NUMBER` |
    | `static int` | `ASSET_FIELD_NUMBER` |
    | `static int` | `ASSET_ISSUED_ID_FIELD_NUMBER` |
    | `static int` | `ASSET_ISSUED_NAME_FIELD_NUMBER` |
    | `static int` | `ASSET_OPTIMIZED_FIELD_NUMBER` |
    | `static int` | `ASSETV2_FIELD_NUMBER` |
    | `static int` | `BALANCE_FIELD_NUMBER` |
    | `static int` | `CODE_FIELD_NUMBER` |
    | `static int` | `CODEHASH_FIELD_NUMBER` |
    | `static int` | `CREATE_TIME_FIELD_NUMBER` |
    | `static int` | `DELEGATED_FROZEN_BALANCE_FOR_BANDWIDTH_FIELD_NUMBER` |
    | `static int` | `DELEGATED_FROZENV2_BALANCE_FOR_BANDWIDTH_FIELD_NUMBER` |
    | `static int` | `FREE_ASSET_NET_USAGE_FIELD_NUMBER` |
    | `static int` | `FREE_ASSET_NET_USAGEV2_FIELD_NUMBER` |
    | `static int` | `FREE_NET_USAGE_FIELD_NUMBER` |
    | `static int` | `FROZEN_FIELD_NUMBER` |
    | `static int` | `FROZEN_SUPPLY_FIELD_NUMBER` |
    | `static int` | `FROZENV2_FIELD_NUMBER` |
    | `static int` | `IS_COMMITTEE_FIELD_NUMBER` |
    | `static int` | `IS_WITNESS_FIELD_NUMBER` |
    | `static int` | `LATEST_ASSET_OPERATION_TIME_FIELD_NUMBER` |
    | `static int` | `LATEST_ASSET_OPERATION_TIMEV2_FIELD_NUMBER` |
    | `static int` | `LATEST_CONSUME_FREE_TIME_FIELD_NUMBER` |
    | `static int` | `LATEST_CONSUME_TIME_FIELD_NUMBER` |
    | `static int` | `LATEST_OPRATION_TIME_FIELD_NUMBER` |
    | `static int` | `LATEST_WITHDRAW_TIME_FIELD_NUMBER` |
    | `static int` | `NET_USAGE_FIELD_NUMBER` |
    | `static int` | `NET_WINDOW_OPTIMIZED_FIELD_NUMBER` |
    | `static int` | `NET_WINDOW_SIZE_FIELD_NUMBER` |
    | `static int` | `OLD_TRON_POWER_FIELD_NUMBER` |
    | `static int` | `OWNER_PERMISSION_FIELD_NUMBER` |
    | `static int` | `TRON_POWER_FIELD_NUMBER` |
    | `static int` | `TYPE_FIELD_NUMBER` |
    | `static int` | `UNFROZENV2_FIELD_NUMBER` |
    | `static int` | `VOTES_FIELD_NUMBER` |
    | `static int` | `WITNESS_PERMISSION_FIELD_NUMBER` |

    - ### Fields inherited from class com.google.protobuf.GeneratedMessageV3

      `alwaysUseFieldBuilders, unknownFields`
    - ### Fields inherited from class com.google.protobuf.AbstractMessage

      `memoizedSize`
    - ### Fields inherited from class com.google.protobuf.AbstractMessageLite

      `memoizedHashCode`
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `boolean` | `containsAsset(java.lang.String key)` the other asset owned by this account |
    | `boolean` | `containsAssetV2(java.lang.String key)` the other asset owned by this account，key is assetId |
    | `boolean` | `containsFreeAssetNetUsage(java.lang.String key)` `map<string, int64> free_asset_net_usage = 20;` |
    | `boolean` | `containsFreeAssetNetUsageV2(java.lang.String key)` `map<string, int64> free_asset_net_usageV2 = 59;` |
    | `boolean` | `containsLatestAssetOperationTime(java.lang.String key)` `map<string, int64> latest_asset_operation_time = 18;` |
    | `boolean` | `containsLatestAssetOperationTimeV2(java.lang.String key)` `map<string, int64> latest_asset_operation_timeV2 = 58;` |
    | `boolean` | `equals(java.lang.Object obj)` |
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
    | `static Response.Account` | `getDefaultInstance()` |
    | `Response.Account` | `getDefaultInstanceForType()` |
    | `long` | `getDelegatedFrozenBalanceForBandwidth()` Freeze and provide balances to other accounts |
    | `long` | `getDelegatedFrozenV2BalanceForBandwidth()` `int64 delegated_frozenV2_balance_for_bandwidth = 36;` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
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
    | `com.google.protobuf.Parser<Response.Account>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
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
    | `int` | `hashCode()` |
    | `boolean` | `hasOwnerPermission()` `.protocol.Permission owner_permission = 31;` |
    | `boolean` | `hasTronPower()` `.protocol.Account.Frozen tron_power = 47;` |
    | `boolean` | `hasWitnessPermission()` `.protocol.Permission witness_permission = 32;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMapFieldReflection(int number)` |
    | `boolean` | `isInitialized()` |
    | `static Response.Account.Builder` | `newBuilder()` |
    | `static Response.Account.Builder` | `newBuilder(Response.Account prototype)` |
    | `Response.Account.Builder` | `newBuilderForType()` |
    | `protected Response.Account.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.Account` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.Account` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Account` | `parseFrom(byte[] data)` |
    | `static Response.Account` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Account` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.Account` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Account` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.Account` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Account` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.Account` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Account` | `parseFrom(java.io.InputStream input)` |
    | `static Response.Account` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.Account>` | `parser()` |
    | `Response.Account.Builder` | `toBuilder()` |
    | `void` | `writeTo(com.google.protobuf.CodedOutputStream output)` |

    - ### Methods inherited from class com.google.protobuf.GeneratedMessageV3

      `canUseUnsafe, computeStringSize, computeStringSizeNoTag, emptyBooleanList, emptyDoubleList, emptyFloatList, emptyIntList, emptyList, emptyLongList, getAllFields, getDescriptorForType, getField, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof, internalGetMapField, isStringEmpty, makeExtensionsImmutable, makeMutableCopy, makeMutableCopy, mergeFromAndMakeImmutableInternal, mutableCopy, mutableCopy, mutableCopy, mutableCopy, mutableCopy, newBooleanList, newBuilderForType, newDoubleList, newFloatList, newIntList, newLongList, parseDelimitedWithIOException, parseDelimitedWithIOException, parseUnknownField, parseUnknownFieldProto3, parseWithIOException, parseWithIOException, parseWithIOException, parseWithIOException, serializeBooleanMapTo, serializeIntegerMapTo, serializeLongMapTo, serializeStringMapTo, writeReplace, writeString, writeStringNoTag`
    - ### Methods inherited from class com.google.protobuf.AbstractMessage

      `findInitializationErrors, getInitializationErrorString, hashBoolean, hashEnum, hashEnumList, hashFields, hashLong, toString`
    - ### Methods inherited from class com.google.protobuf.AbstractMessageLite

      `addAll, addAll, checkByteStringIsUtf8, toByteArray, toByteString, writeDelimitedTo, writeTo`
    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, wait, wait, wait`
    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLite

      `toByteArray, toByteString, writeDelimitedTo, writeTo`

* + ### Field Detail

    - #### ACCOUNT\_NAME\_FIELD\_NUMBER

      ```
      public static final int ACCOUNT_NAME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.ACCOUNT_NAME_FIELD_NUMBER)
    - #### TYPE\_FIELD\_NUMBER

      ```
      public static final int TYPE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.TYPE_FIELD_NUMBER)
    - #### ADDRESS\_FIELD\_NUMBER

      ```
      public static final int ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.ADDRESS_FIELD_NUMBER)
    - #### BALANCE\_FIELD\_NUMBER

      ```
      public static final int BALANCE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.BALANCE_FIELD_NUMBER)
    - #### VOTES\_FIELD\_NUMBER

      ```
      public static final int VOTES_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.VOTES_FIELD_NUMBER)
    - #### ASSET\_FIELD\_NUMBER

      ```
      public static final int ASSET_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.ASSET_FIELD_NUMBER)
    - #### ASSETV2\_FIELD\_NUMBER

      ```
      public static final int ASSETV2_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.ASSETV2_FIELD_NUMBER)
    - #### FROZEN\_FIELD\_NUMBER

      ```
      public static final int FROZEN_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.FROZEN_FIELD_NUMBER)
    - #### NET\_USAGE\_FIELD\_NUMBER

      ```
      public static final int NET_USAGE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.NET_USAGE_FIELD_NUMBER)
    - #### ACQUIRED\_DELEGATED\_FROZEN\_BALANCE\_FOR\_BANDWIDTH\_FIELD\_NUMBER

      ```
      public static final int ACQUIRED_DELEGATED_FROZEN_BALANCE_FOR_BANDWIDTH_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.ACQUIRED_DELEGATED_FROZEN_BALANCE_FOR_BANDWIDTH_FIELD_NUMBER)
    - #### DELEGATED\_FROZEN\_BALANCE\_FOR\_BANDWIDTH\_FIELD\_NUMBER

      ```
      public static final int DELEGATED_FROZEN_BALANCE_FOR_BANDWIDTH_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.DELEGATED_FROZEN_BALANCE_FOR_BANDWIDTH_FIELD_NUMBER)
    - #### OLD\_TRON\_POWER\_FIELD\_NUMBER

      ```
      public static final int OLD_TRON_POWER_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.OLD_TRON_POWER_FIELD_NUMBER)
    - #### TRON\_POWER\_FIELD\_NUMBER

      ```
      public static final int TRON_POWER_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.TRON_POWER_FIELD_NUMBER)
    - #### ASSET\_OPTIMIZED\_FIELD\_NUMBER

      ```
      public static final int ASSET_OPTIMIZED_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.ASSET_OPTIMIZED_FIELD_NUMBER)
    - #### CREATE\_TIME\_FIELD\_NUMBER

      ```
      public static final int CREATE_TIME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.CREATE_TIME_FIELD_NUMBER)
    - #### LATEST\_OPRATION\_TIME\_FIELD\_NUMBER

      ```
      public static final int LATEST_OPRATION_TIME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.LATEST_OPRATION_TIME_FIELD_NUMBER)
    - #### ALLOWANCE\_FIELD\_NUMBER

      ```
      public static final int ALLOWANCE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.ALLOWANCE_FIELD_NUMBER)
    - #### LATEST\_WITHDRAW\_TIME\_FIELD\_NUMBER

      ```
      public static final int LATEST_WITHDRAW_TIME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.LATEST_WITHDRAW_TIME_FIELD_NUMBER)
    - #### CODE\_FIELD\_NUMBER

      ```
      public static final int CODE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.CODE_FIELD_NUMBER)
    - #### IS\_WITNESS\_FIELD\_NUMBER

      ```
      public static final int IS_WITNESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.IS_WITNESS_FIELD_NUMBER)
    - #### IS\_COMMITTEE\_FIELD\_NUMBER

      ```
      public static final int IS_COMMITTEE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.IS_COMMITTEE_FIELD_NUMBER)
    - #### FROZEN\_SUPPLY\_FIELD\_NUMBER

      ```
      public static final int FROZEN_SUPPLY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.FROZEN_SUPPLY_FIELD_NUMBER)
    - #### ASSET\_ISSUED\_NAME\_FIELD\_NUMBER

      ```
      public static final int ASSET_ISSUED_NAME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.ASSET_ISSUED_NAME_FIELD_NUMBER)
    - #### ASSET\_ISSUED\_ID\_FIELD\_NUMBER

      ```
      public static final int ASSET_ISSUED_ID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.ASSET_ISSUED_ID_FIELD_NUMBER)
    - #### LATEST\_ASSET\_OPERATION\_TIME\_FIELD\_NUMBER

      ```
      public static final int LATEST_ASSET_OPERATION_TIME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.LATEST_ASSET_OPERATION_TIME_FIELD_NUMBER)
    - #### LATEST\_ASSET\_OPERATION\_TIMEV2\_FIELD\_NUMBER

      ```
      public static final int LATEST_ASSET_OPERATION_TIMEV2_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.LATEST_ASSET_OPERATION_TIMEV2_FIELD_NUMBER)
    - #### FREE\_NET\_USAGE\_FIELD\_NUMBER

      ```
      public static final int FREE_NET_USAGE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.FREE_NET_USAGE_FIELD_NUMBER)
    - #### FREE\_ASSET\_NET\_USAGE\_FIELD\_NUMBER

      ```
      public static final int FREE_ASSET_NET_USAGE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.FREE_ASSET_NET_USAGE_FIELD_NUMBER)
    - #### FREE\_ASSET\_NET\_USAGEV2\_FIELD\_NUMBER

      ```
      public static final int FREE_ASSET_NET_USAGEV2_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.FREE_ASSET_NET_USAGEV2_FIELD_NUMBER)
    - #### LATEST\_CONSUME\_TIME\_FIELD\_NUMBER

      ```
      public static final int LATEST_CONSUME_TIME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.LATEST_CONSUME_TIME_FIELD_NUMBER)
    - #### LATEST\_CONSUME\_FREE\_TIME\_FIELD\_NUMBER

      ```
      public static final int LATEST_CONSUME_FREE_TIME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.LATEST_CONSUME_FREE_TIME_FIELD_NUMBER)
    - #### ACCOUNT\_ID\_FIELD\_NUMBER

      ```
      public static final int ACCOUNT_ID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.ACCOUNT_ID_FIELD_NUMBER)
    - #### NET\_WINDOW\_SIZE\_FIELD\_NUMBER

      ```
      public static final int NET_WINDOW_SIZE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.NET_WINDOW_SIZE_FIELD_NUMBER)
    - #### NET\_WINDOW\_OPTIMIZED\_FIELD\_NUMBER

      ```
      public static final int NET_WINDOW_OPTIMIZED_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.NET_WINDOW_OPTIMIZED_FIELD_NUMBER)
    - #### ACCOUNT\_RESOURCE\_FIELD\_NUMBER

      ```
      public static final int ACCOUNT_RESOURCE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.ACCOUNT_RESOURCE_FIELD_NUMBER)
    - #### CODEHASH\_FIELD\_NUMBER

      ```
      public static final int CODEHASH_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.CODEHASH_FIELD_NUMBER)
    - #### OWNER\_PERMISSION\_FIELD\_NUMBER

      ```
      public static final int OWNER_PERMISSION_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.OWNER_PERMISSION_FIELD_NUMBER)
    - #### WITNESS\_PERMISSION\_FIELD\_NUMBER

      ```
      public static final int WITNESS_PERMISSION_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.WITNESS_PERMISSION_FIELD_NUMBER)
    - #### ACTIVE\_PERMISSION\_FIELD\_NUMBER

      ```
      public static final int ACTIVE_PERMISSION_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.ACTIVE_PERMISSION_FIELD_NUMBER)
    - #### FROZENV2\_FIELD\_NUMBER

      ```
      public static final int FROZENV2_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.FROZENV2_FIELD_NUMBER)
    - #### UNFROZENV2\_FIELD\_NUMBER

      ```
      public static final int UNFROZENV2_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.UNFROZENV2_FIELD_NUMBER)
    - #### DELEGATED\_FROZENV2\_BALANCE\_FOR\_BANDWIDTH\_FIELD\_NUMBER

      ```
      public static final int DELEGATED_FROZENV2_BALANCE_FOR_BANDWIDTH_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.DELEGATED_FROZENV2_BALANCE_FOR_BANDWIDTH_FIELD_NUMBER)
    - #### ACQUIRED\_DELEGATED\_FROZENV2\_BALANCE\_FOR\_BANDWIDTH\_FIELD\_NUMBER

      ```
      public static final int ACQUIRED_DELEGATED_FROZENV2_BALANCE_FOR_BANDWIDTH_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.ACQUIRED_DELEGATED_FROZENV2_BALANCE_FOR_BANDWIDTH_FIELD_NUMBER)
  + ### Method Detail

    - #### newInstance

      ```
      protected java.lang.Object newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)
      ```

      Overrides:
      :   `newInstance` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDescriptor

      ```
      public static final com.google.protobuf.Descriptors.Descriptor getDescriptor()
      ```
    - #### internalGetMapFieldReflection

      ```
      protected com.google.protobuf.MapFieldReflectionAccessor internalGetMapFieldReflection(int number)
      ```

      Overrides:
      :   `internalGetMapFieldReflection` in class `com.google.protobuf.GeneratedMessageV3`
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3`
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
    - #### getTypeValue

      ```
      public int getTypeValue()
      ```

      `.protocol.AccountType type = 2;`

      Specified by:
      :   `getTypeValue` in interface `Response.AccountOrBuilder`

      Returns:
      :   The enum numeric value on the wire for type.
    - #### getType

      ```
      public Common.AccountType getType()
      ```

      `.protocol.AccountType type = 2;`

      Specified by:
      :   `getType` in interface `Response.AccountOrBuilder`

      Returns:
      :   The type.
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

      Use [`getAssetMap()`](../../../../org/tron/trident/proto/Response.Account.html#getAssetMap--) instead.

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

      Use [`getAssetV2Map()`](../../../../org/tron/trident/proto/Response.Account.html#getAssetV2Map--) instead.

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
    - #### getOldTronPower

      ```
      public long getOldTronPower()
      ```

      `int64 old_tron_power = 46;`

      Specified by:
      :   `getOldTronPower` in interface `Response.AccountOrBuilder`

      Returns:
      :   The oldTronPower.
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
    - #### getIsWitness

      ```
      public boolean getIsWitness()
      ```

      `bool is_witness = 14;`

      Specified by:
      :   `getIsWitness` in interface `Response.AccountOrBuilder`

      Returns:
      :   The isWitness.
    - #### getIsCommittee

      ```
      public boolean getIsCommittee()
      ```

      `bool is_committee = 15;`

      Specified by:
      :   `getIsCommittee` in interface `Response.AccountOrBuilder`

      Returns:
      :   The isCommittee.
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
    - #### getAssetIssuedID

      ```
      public com.google.protobuf.ByteString getAssetIssuedID()
      ```

      `bytes asset_issued_ID = 57;`

      Specified by:
      :   `getAssetIssuedID` in interface `Response.AccountOrBuilder`

      Returns:
      :   The assetIssuedID.
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

      Use [`getLatestAssetOperationTimeMap()`](../../../../org/tron/trident/proto/Response.Account.html#getLatestAssetOperationTimeMap--) instead.

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

      Use [`getLatestAssetOperationTimeV2Map()`](../../../../org/tron/trident/proto/Response.Account.html#getLatestAssetOperationTimeV2Map--) instead.

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
    - #### getFreeNetUsage

      ```
      public long getFreeNetUsage()
      ```

      `int64 free_net_usage = 19;`

      Specified by:
      :   `getFreeNetUsage` in interface `Response.AccountOrBuilder`

      Returns:
      :   The freeNetUsage.
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

      Use [`getFreeAssetNetUsageMap()`](../../../../org/tron/trident/proto/Response.Account.html#getFreeAssetNetUsageMap--) instead.

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

      Use [`getFreeAssetNetUsageV2Map()`](../../../../org/tron/trident/proto/Response.Account.html#getFreeAssetNetUsageV2Map--) instead.

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
    - #### getLatestConsumeTime

      ```
      public long getLatestConsumeTime()
      ```

      `int64 latest_consume_time = 21;`

      Specified by:
      :   `getLatestConsumeTime` in interface `Response.AccountOrBuilder`

      Returns:
      :   The latestConsumeTime.
    - #### getLatestConsumeFreeTime

      ```
      public long getLatestConsumeFreeTime()
      ```

      `int64 latest_consume_free_time = 22;`

      Specified by:
      :   `getLatestConsumeFreeTime` in interface `Response.AccountOrBuilder`

      Returns:
      :   The latestConsumeFreeTime.
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
    - #### getNetWindowSize

      ```
      public long getNetWindowSize()
      ```

      `int64 net_window_size = 24;`

      Specified by:
      :   `getNetWindowSize` in interface `Response.AccountOrBuilder`

      Returns:
      :   The netWindowSize.
    - #### getNetWindowOptimized

      ```
      public boolean getNetWindowOptimized()
      ```

      `bool net_window_optimized = 25;`

      Specified by:
      :   `getNetWindowOptimized` in interface `Response.AccountOrBuilder`

      Returns:
      :   The netWindowOptimized.
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
    - #### getActivePermissionOrBuilderList

      ```
      public java.util.List<? extends Common.PermissionOrBuilder> getActivePermissionOrBuilderList()
      ```

      `repeated .protocol.Permission active_permission = 33;`

      Specified by:
      :   `getActivePermissionOrBuilderList` in interface `Response.AccountOrBuilder`
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
    - #### getActivePermissionOrBuilder

      ```
      public Common.PermissionOrBuilder getActivePermissionOrBuilder(int index)
      ```

      `repeated .protocol.Permission active_permission = 33;`

      Specified by:
      :   `getActivePermissionOrBuilder` in interface `Response.AccountOrBuilder`
    - #### getFrozenV2List

      ```
      public java.util.List<Response.Account.FreezeV2> getFrozenV2List()
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`

      Specified by:
      :   `getFrozenV2List` in interface `Response.AccountOrBuilder`
    - #### getFrozenV2OrBuilderList

      ```
      public java.util.List<? extends Response.Account.FreezeV2OrBuilder> getFrozenV2OrBuilderList()
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`

      Specified by:
      :   `getFrozenV2OrBuilderList` in interface `Response.AccountOrBuilder`
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
    - #### getFrozenV2OrBuilder

      ```
      public Response.Account.FreezeV2OrBuilder getFrozenV2OrBuilder(int index)
      ```

      `repeated .protocol.Account.FreezeV2 frozenV2 = 34;`

      Specified by:
      :   `getFrozenV2OrBuilder` in interface `Response.AccountOrBuilder`
    - #### getUnfrozenV2List

      ```
      public java.util.List<Response.Account.UnFreezeV2> getUnfrozenV2List()
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`

      Specified by:
      :   `getUnfrozenV2List` in interface `Response.AccountOrBuilder`
    - #### getUnfrozenV2OrBuilderList

      ```
      public java.util.List<? extends Response.Account.UnFreezeV2OrBuilder> getUnfrozenV2OrBuilderList()
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`

      Specified by:
      :   `getUnfrozenV2OrBuilderList` in interface `Response.AccountOrBuilder`
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
    - #### getUnfrozenV2OrBuilder

      ```
      public Response.Account.UnFreezeV2OrBuilder getUnfrozenV2OrBuilder(int index)
      ```

      `repeated .protocol.Account.UnFreezeV2 unfrozenV2 = 35;`

      Specified by:
      :   `getUnfrozenV2OrBuilder` in interface `Response.AccountOrBuilder`
    - #### getDelegatedFrozenV2BalanceForBandwidth

      ```
      public long getDelegatedFrozenV2BalanceForBandwidth()
      ```

      `int64 delegated_frozenV2_balance_for_bandwidth = 36;`

      Specified by:
      :   `getDelegatedFrozenV2BalanceForBandwidth` in interface `Response.AccountOrBuilder`

      Returns:
      :   The delegatedFrozenV2BalanceForBandwidth.
    - #### getAcquiredDelegatedFrozenV2BalanceForBandwidth

      ```
      public long getAcquiredDelegatedFrozenV2BalanceForBandwidth()
      ```

      `int64 acquired_delegated_frozenV2_balance_for_bandwidth = 37;`

      Specified by:
      :   `getAcquiredDelegatedFrozenV2BalanceForBandwidth` in interface `Response.AccountOrBuilder`

      Returns:
      :   The acquiredDelegatedFrozenV2BalanceForBandwidth.
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3`
    - #### writeTo

      ```
      public void writeTo(com.google.protobuf.CodedOutputStream output)
                   throws java.io.IOException
      ```

      Specified by:
      :   `writeTo` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `writeTo` in class `com.google.protobuf.GeneratedMessageV3`

      Throws:
      :   `java.io.IOException`
    - #### getSerializedSize

      ```
      public int getSerializedSize()
      ```

      Specified by:
      :   `getSerializedSize` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getSerializedSize` in class `com.google.protobuf.GeneratedMessageV3`
    - #### equals

      ```
      public boolean equals(java.lang.Object obj)
      ```

      Specified by:
      :   `equals` in interface `com.google.protobuf.Message`

      Overrides:
      :   `equals` in class `com.google.protobuf.AbstractMessage`
    - #### hashCode

      ```
      public int hashCode()
      ```

      Specified by:
      :   `hashCode` in interface `com.google.protobuf.Message`

      Overrides:
      :   `hashCode` in class `com.google.protobuf.AbstractMessage`
    - #### parseFrom

      ```
      public static Response.Account parseFrom(java.nio.ByteBuffer data)
                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Account parseFrom(java.nio.ByteBuffer data,
                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Account parseFrom(com.google.protobuf.ByteString data)
                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Account parseFrom(com.google.protobuf.ByteString data,
                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Account parseFrom(byte[] data)
                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Account parseFrom(byte[] data,
                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Account parseFrom(java.io.InputStream input)
                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.Account parseFrom(java.io.InputStream input,
                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.Account parseDelimitedFrom(java.io.InputStream input)
                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.Account parseDelimitedFrom(java.io.InputStream input,
                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.Account parseFrom(com.google.protobuf.CodedInputStream input)
                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.Account parseFrom(com.google.protobuf.CodedInputStream input,
                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.Account.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.Account.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.Account.Builder newBuilder(Response.Account prototype)
      ```
    - #### toBuilder

      ```
      public Response.Account.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.Account.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.Account getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.Account> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.Account> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.Account getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`