

org.tron.trident.proto

## Interface Contract.AssetIssueContractOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Contract.AssetIssueContract](../../../../org/tron/trident/proto/Contract.AssetIssueContract.html "class in org.tron.trident.proto"), [Contract.AssetIssueContract.Builder](../../../../org/tron/trident/proto/Contract.AssetIssueContract.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Contract.AssetIssueContractOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getAbbr()` `bytes abbr = 3;` |
    | `com.google.protobuf.ByteString` | `getDescription()` `bytes description = 20;` |
    | `long` | `getEndTime()` `int64 end_time = 10;` |
    | `long` | `getFreeAssetNetLimit()` `int64 free_asset_net_limit = 22;` |
    | `Contract.AssetIssueContract.FrozenSupply` | `getFrozenSupply(int index)` `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;` |
    | `int` | `getFrozenSupplyCount()` `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;` |
    | `java.util.List<Contract.AssetIssueContract.FrozenSupply>` | `getFrozenSupplyList()` `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;` |
    | `Contract.AssetIssueContract.FrozenSupplyOrBuilder` | `getFrozenSupplyOrBuilder(int index)` `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;` |
    | `java.util.List<? extends Contract.AssetIssueContract.FrozenSupplyOrBuilder>` | `getFrozenSupplyOrBuilderList()` `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;` |
    | `java.lang.String` | `getId()` `string id = 41;` |
    | `com.google.protobuf.ByteString` | `getIdBytes()` `string id = 41;` |
    | `com.google.protobuf.ByteString` | `getName()` `bytes name = 2;` |
    | `int` | `getNum()` `int32 num = 8;` |
    | `long` | `getOrder()` useless |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `int` | `getPrecision()` `int32 precision = 7;` |
    | `long` | `getPublicFreeAssetNetLimit()` `int64 public_free_asset_net_limit = 23;` |
    | `long` | `getPublicFreeAssetNetUsage()` `int64 public_free_asset_net_usage = 24;` |
    | `long` | `getPublicLatestFreeNetTime()` `int64 public_latest_free_net_time = 25;` |
    | `long` | `getStartTime()` `int64 start_time = 9;` |
    | `long` | `getTotalSupply()` `int64 total_supply = 4;` |
    | `int` | `getTrxNum()` `int32 trx_num = 6;` |
    | `com.google.protobuf.ByteString` | `getUrl()` `bytes url = 21;` |
    | `int` | `getVoteScore()` `int32 vote_score = 16;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getId

      ```
      java.lang.String getId()
      ```

      `string id = 41;`

      Returns:
      :   The id.
    - #### getIdBytes

      ```
      com.google.protobuf.ByteString getIdBytes()
      ```

      `string id = 41;`

      Returns:
      :   The bytes for id.
    - #### getOwnerAddress

      ```
      com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   The ownerAddress.
    - #### getName

      ```
      com.google.protobuf.ByteString getName()
      ```

      `bytes name = 2;`

      Returns:
      :   The name.
    - #### getAbbr

      ```
      com.google.protobuf.ByteString getAbbr()
      ```

      `bytes abbr = 3;`

      Returns:
      :   The abbr.
    - #### getTotalSupply

      ```
      long getTotalSupply()
      ```

      `int64 total_supply = 4;`

      Returns:
      :   The totalSupply.
    - #### getFrozenSupplyList

      ```
      java.util.List<Contract.AssetIssueContract.FrozenSupply> getFrozenSupplyList()
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`
    - #### getFrozenSupply

      ```
      Contract.AssetIssueContract.FrozenSupply getFrozenSupply(int index)
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`
    - #### getFrozenSupplyCount

      ```
      int getFrozenSupplyCount()
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`
    - #### getFrozenSupplyOrBuilderList

      ```
      java.util.List<? extends Contract.AssetIssueContract.FrozenSupplyOrBuilder> getFrozenSupplyOrBuilderList()
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`
    - #### getFrozenSupplyOrBuilder

      ```
      Contract.AssetIssueContract.FrozenSupplyOrBuilder getFrozenSupplyOrBuilder(int index)
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`
    - #### getTrxNum

      ```
      int getTrxNum()
      ```

      `int32 trx_num = 6;`

      Returns:
      :   The trxNum.
    - #### getPrecision

      ```
      int getPrecision()
      ```

      `int32 precision = 7;`

      Returns:
      :   The precision.
    - #### getNum

      ```
      int getNum()
      ```

      `int32 num = 8;`

      Returns:
      :   The num.
    - #### getStartTime

      ```
      long getStartTime()
      ```

      `int64 start_time = 9;`

      Returns:
      :   The startTime.
    - #### getEndTime

      ```
      long getEndTime()
      ```

      `int64 end_time = 10;`

      Returns:
      :   The endTime.
    - #### getOrder

      ```
      long getOrder()
      ```

      ```
       useless
      ```

      `int64 order = 11;`

      Returns:
      :   The order.
    - #### getVoteScore

      ```
      int getVoteScore()
      ```

      `int32 vote_score = 16;`

      Returns:
      :   The voteScore.
    - #### getDescription

      ```
      com.google.protobuf.ByteString getDescription()
      ```

      `bytes description = 20;`

      Returns:
      :   The description.
    - #### getUrl

      ```
      com.google.protobuf.ByteString getUrl()
      ```

      `bytes url = 21;`

      Returns:
      :   The url.
    - #### getFreeAssetNetLimit

      ```
      long getFreeAssetNetLimit()
      ```

      `int64 free_asset_net_limit = 22;`

      Returns:
      :   The freeAssetNetLimit.
    - #### getPublicFreeAssetNetLimit

      ```
      long getPublicFreeAssetNetLimit()
      ```

      `int64 public_free_asset_net_limit = 23;`

      Returns:
      :   The publicFreeAssetNetLimit.
    - #### getPublicFreeAssetNetUsage

      ```
      long getPublicFreeAssetNetUsage()
      ```

      `int64 public_free_asset_net_usage = 24;`

      Returns:
      :   The publicFreeAssetNetUsage.
    - #### getPublicLatestFreeNetTime

      ```
      long getPublicLatestFreeNetTime()
      ```

      `int64 public_latest_free_net_time = 25;`

      Returns:
      :   The publicLatestFreeNetTime.