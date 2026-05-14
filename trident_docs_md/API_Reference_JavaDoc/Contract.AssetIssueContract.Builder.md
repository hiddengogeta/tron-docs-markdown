

org.tron.trident.proto

## Class Contract.AssetIssueContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.AssetIssueContract.Builder](../../../../org/tron/trident/proto/Contract.AssetIssueContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.AssetIssueContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.AssetIssueContractOrBuilder](../../../../org/tron/trident/proto/Contract.AssetIssueContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.AssetIssueContract](../../../../org/tron/trident/proto/Contract.AssetIssueContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.AssetIssueContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.Builder>
  implements Contract.AssetIssueContractOrBuilder
  ```

  Protobuf type `protocol.AssetIssueContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.AssetIssueContract.Builder` | `addAllFrozenSupply(java.lang.Iterable<? extends Contract.AssetIssueContract.FrozenSupply> values)` `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;` |
    | `Contract.AssetIssueContract.Builder` | `addFrozenSupply(Contract.AssetIssueContract.FrozenSupply.Builder builderForValue)` `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;` |
    | `Contract.AssetIssueContract.Builder` | `addFrozenSupply(Contract.AssetIssueContract.FrozenSupply value)` `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;` |
    | `Contract.AssetIssueContract.Builder` | `addFrozenSupply(int index, Contract.AssetIssueContract.FrozenSupply.Builder builderForValue)` `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;` |
    | `Contract.AssetIssueContract.Builder` | `addFrozenSupply(int index, Contract.AssetIssueContract.FrozenSupply value)` `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;` |
    | `Contract.AssetIssueContract.FrozenSupply.Builder` | `addFrozenSupplyBuilder()` `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;` |
    | `Contract.AssetIssueContract.FrozenSupply.Builder` | `addFrozenSupplyBuilder(int index)` `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;` |
    | `Contract.AssetIssueContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.AssetIssueContract` | `build()` |
    | `Contract.AssetIssueContract` | `buildPartial()` |
    | `Contract.AssetIssueContract.Builder` | `clear()` |
    | `Contract.AssetIssueContract.Builder` | `clearAbbr()` `bytes abbr = 3;` |
    | `Contract.AssetIssueContract.Builder` | `clearDescription()` `bytes description = 20;` |
    | `Contract.AssetIssueContract.Builder` | `clearEndTime()` `int64 end_time = 10;` |
    | `Contract.AssetIssueContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.AssetIssueContract.Builder` | `clearFreeAssetNetLimit()` `int64 free_asset_net_limit = 22;` |
    | `Contract.AssetIssueContract.Builder` | `clearFrozenSupply()` `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;` |
    | `Contract.AssetIssueContract.Builder` | `clearId()` `string id = 41;` |
    | `Contract.AssetIssueContract.Builder` | `clearName()` `bytes name = 2;` |
    | `Contract.AssetIssueContract.Builder` | `clearNum()` `int32 num = 8;` |
    | `Contract.AssetIssueContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.AssetIssueContract.Builder` | `clearOrder()` useless |
    | `Contract.AssetIssueContract.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `Contract.AssetIssueContract.Builder` | `clearPrecision()` `int32 precision = 7;` |
    | `Contract.AssetIssueContract.Builder` | `clearPublicFreeAssetNetLimit()` `int64 public_free_asset_net_limit = 23;` |
    | `Contract.AssetIssueContract.Builder` | `clearPublicFreeAssetNetUsage()` `int64 public_free_asset_net_usage = 24;` |
    | `Contract.AssetIssueContract.Builder` | `clearPublicLatestFreeNetTime()` `int64 public_latest_free_net_time = 25;` |
    | `Contract.AssetIssueContract.Builder` | `clearStartTime()` `int64 start_time = 9;` |
    | `Contract.AssetIssueContract.Builder` | `clearTotalSupply()` `int64 total_supply = 4;` |
    | `Contract.AssetIssueContract.Builder` | `clearTrxNum()` `int32 trx_num = 6;` |
    | `Contract.AssetIssueContract.Builder` | `clearUrl()` `bytes url = 21;` |
    | `Contract.AssetIssueContract.Builder` | `clearVoteScore()` `int32 vote_score = 16;` |
    | `Contract.AssetIssueContract.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getAbbr()` `bytes abbr = 3;` |
    | `Contract.AssetIssueContract` | `getDefaultInstanceForType()` |
    | `com.google.protobuf.ByteString` | `getDescription()` `bytes description = 20;` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getEndTime()` `int64 end_time = 10;` |
    | `long` | `getFreeAssetNetLimit()` `int64 free_asset_net_limit = 22;` |
    | `Contract.AssetIssueContract.FrozenSupply` | `getFrozenSupply(int index)` `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;` |
    | `Contract.AssetIssueContract.FrozenSupply.Builder` | `getFrozenSupplyBuilder(int index)` `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;` |
    | `java.util.List<Contract.AssetIssueContract.FrozenSupply.Builder>` | `getFrozenSupplyBuilderList()` `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;` |
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
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.AssetIssueContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.AssetIssueContract.Builder` | `mergeFrom(Contract.AssetIssueContract other)` |
    | `Contract.AssetIssueContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.AssetIssueContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.AssetIssueContract.Builder` | `removeFrozenSupply(int index)` `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;` |
    | `Contract.AssetIssueContract.Builder` | `setAbbr(com.google.protobuf.ByteString value)` `bytes abbr = 3;` |
    | `Contract.AssetIssueContract.Builder` | `setDescription(com.google.protobuf.ByteString value)` `bytes description = 20;` |
    | `Contract.AssetIssueContract.Builder` | `setEndTime(long value)` `int64 end_time = 10;` |
    | `Contract.AssetIssueContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.AssetIssueContract.Builder` | `setFreeAssetNetLimit(long value)` `int64 free_asset_net_limit = 22;` |
    | `Contract.AssetIssueContract.Builder` | `setFrozenSupply(int index, Contract.AssetIssueContract.FrozenSupply.Builder builderForValue)` `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;` |
    | `Contract.AssetIssueContract.Builder` | `setFrozenSupply(int index, Contract.AssetIssueContract.FrozenSupply value)` `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;` |
    | `Contract.AssetIssueContract.Builder` | `setId(java.lang.String value)` `string id = 41;` |
    | `Contract.AssetIssueContract.Builder` | `setIdBytes(com.google.protobuf.ByteString value)` `string id = 41;` |
    | `Contract.AssetIssueContract.Builder` | `setName(com.google.protobuf.ByteString value)` `bytes name = 2;` |
    | `Contract.AssetIssueContract.Builder` | `setNum(int value)` `int32 num = 8;` |
    | `Contract.AssetIssueContract.Builder` | `setOrder(long value)` useless |
    | `Contract.AssetIssueContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `Contract.AssetIssueContract.Builder` | `setPrecision(int value)` `int32 precision = 7;` |
    | `Contract.AssetIssueContract.Builder` | `setPublicFreeAssetNetLimit(long value)` `int64 public_free_asset_net_limit = 23;` |
    | `Contract.AssetIssueContract.Builder` | `setPublicFreeAssetNetUsage(long value)` `int64 public_free_asset_net_usage = 24;` |
    | `Contract.AssetIssueContract.Builder` | `setPublicLatestFreeNetTime(long value)` `int64 public_latest_free_net_time = 25;` |
    | `Contract.AssetIssueContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.AssetIssueContract.Builder` | `setStartTime(long value)` `int64 start_time = 9;` |
    | `Contract.AssetIssueContract.Builder` | `setTotalSupply(long value)` `int64 total_supply = 4;` |
    | `Contract.AssetIssueContract.Builder` | `setTrxNum(int value)` `int32 trx_num = 6;` |
    | `Contract.AssetIssueContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.AssetIssueContract.Builder` | `setUrl(com.google.protobuf.ByteString value)` `bytes url = 21;` |
    | `Contract.AssetIssueContract.Builder` | `setVoteScore(int value)` `int32 vote_score = 16;` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.Builder>`
    - #### clear

      ```
      public Contract.AssetIssueContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.AssetIssueContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.AssetIssueContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.AssetIssueContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.AssetIssueContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.Builder>`
    - #### setField

      ```
      public Contract.AssetIssueContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                          java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.Builder>`
    - #### clearField

      ```
      public Contract.AssetIssueContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.Builder>`
    - #### clearOneof

      ```
      public Contract.AssetIssueContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.AssetIssueContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                  int index,
                                                                  java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.AssetIssueContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                  java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.AssetIssueContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.AssetIssueContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.AssetIssueContract.Builder mergeFrom(Contract.AssetIssueContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.AssetIssueContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.AssetIssueContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getId

      ```
      public java.lang.String getId()
      ```

      `string id = 41;`

      Specified by:
      :   `getId` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The id.
    - #### getIdBytes

      ```
      public com.google.protobuf.ByteString getIdBytes()
      ```

      `string id = 41;`

      Specified by:
      :   `getIdBytes` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The bytes for id.
    - #### setId

      ```
      public Contract.AssetIssueContract.Builder setId(java.lang.String value)
      ```

      `string id = 41;`

      Parameters:
      :   `value` - The id to set.

      Returns:
      :   This builder for chaining.
    - #### clearId

      ```
      public Contract.AssetIssueContract.Builder clearId()
      ```

      `string id = 41;`

      Returns:
      :   This builder for chaining.
    - #### setIdBytes

      ```
      public Contract.AssetIssueContract.Builder setIdBytes(com.google.protobuf.ByteString value)
      ```

      `string id = 41;`

      Parameters:
      :   `value` - The bytes for id to set.

      Returns:
      :   This builder for chaining.
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.AssetIssueContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.AssetIssueContract.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getName

      ```
      public com.google.protobuf.ByteString getName()
      ```

      `bytes name = 2;`

      Specified by:
      :   `getName` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The name.
    - #### setName

      ```
      public Contract.AssetIssueContract.Builder setName(com.google.protobuf.ByteString value)
      ```

      `bytes name = 2;`

      Parameters:
      :   `value` - The name to set.

      Returns:
      :   This builder for chaining.
    - #### clearName

      ```
      public Contract.AssetIssueContract.Builder clearName()
      ```

      `bytes name = 2;`

      Returns:
      :   This builder for chaining.
    - #### getAbbr

      ```
      public com.google.protobuf.ByteString getAbbr()
      ```

      `bytes abbr = 3;`

      Specified by:
      :   `getAbbr` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The abbr.
    - #### setAbbr

      ```
      public Contract.AssetIssueContract.Builder setAbbr(com.google.protobuf.ByteString value)
      ```

      `bytes abbr = 3;`

      Parameters:
      :   `value` - The abbr to set.

      Returns:
      :   This builder for chaining.
    - #### clearAbbr

      ```
      public Contract.AssetIssueContract.Builder clearAbbr()
      ```

      `bytes abbr = 3;`

      Returns:
      :   This builder for chaining.
    - #### getTotalSupply

      ```
      public long getTotalSupply()
      ```

      `int64 total_supply = 4;`

      Specified by:
      :   `getTotalSupply` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The totalSupply.
    - #### setTotalSupply

      ```
      public Contract.AssetIssueContract.Builder setTotalSupply(long value)
      ```

      `int64 total_supply = 4;`

      Parameters:
      :   `value` - The totalSupply to set.

      Returns:
      :   This builder for chaining.
    - #### clearTotalSupply

      ```
      public Contract.AssetIssueContract.Builder clearTotalSupply()
      ```

      `int64 total_supply = 4;`

      Returns:
      :   This builder for chaining.
    - #### getFrozenSupplyList

      ```
      public java.util.List<Contract.AssetIssueContract.FrozenSupply> getFrozenSupplyList()
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`

      Specified by:
      :   `getFrozenSupplyList` in interface `Contract.AssetIssueContractOrBuilder`
    - #### getFrozenSupplyCount

      ```
      public int getFrozenSupplyCount()
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`

      Specified by:
      :   `getFrozenSupplyCount` in interface `Contract.AssetIssueContractOrBuilder`
    - #### getFrozenSupply

      ```
      public Contract.AssetIssueContract.FrozenSupply getFrozenSupply(int index)
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`

      Specified by:
      :   `getFrozenSupply` in interface `Contract.AssetIssueContractOrBuilder`
    - #### setFrozenSupply

      ```
      public Contract.AssetIssueContract.Builder setFrozenSupply(int index,
                                                                 Contract.AssetIssueContract.FrozenSupply value)
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`
    - #### setFrozenSupply

      ```
      public Contract.AssetIssueContract.Builder setFrozenSupply(int index,
                                                                 Contract.AssetIssueContract.FrozenSupply.Builder builderForValue)
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`
    - #### addFrozenSupply

      ```
      public Contract.AssetIssueContract.Builder addFrozenSupply(Contract.AssetIssueContract.FrozenSupply value)
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`
    - #### addFrozenSupply

      ```
      public Contract.AssetIssueContract.Builder addFrozenSupply(int index,
                                                                 Contract.AssetIssueContract.FrozenSupply value)
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`
    - #### addFrozenSupply

      ```
      public Contract.AssetIssueContract.Builder addFrozenSupply(Contract.AssetIssueContract.FrozenSupply.Builder builderForValue)
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`
    - #### addFrozenSupply

      ```
      public Contract.AssetIssueContract.Builder addFrozenSupply(int index,
                                                                 Contract.AssetIssueContract.FrozenSupply.Builder builderForValue)
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`
    - #### addAllFrozenSupply

      ```
      public Contract.AssetIssueContract.Builder addAllFrozenSupply(java.lang.Iterable<? extends Contract.AssetIssueContract.FrozenSupply> values)
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`
    - #### clearFrozenSupply

      ```
      public Contract.AssetIssueContract.Builder clearFrozenSupply()
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`
    - #### removeFrozenSupply

      ```
      public Contract.AssetIssueContract.Builder removeFrozenSupply(int index)
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`
    - #### getFrozenSupplyBuilder

      ```
      public Contract.AssetIssueContract.FrozenSupply.Builder getFrozenSupplyBuilder(int index)
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`
    - #### getFrozenSupplyOrBuilder

      ```
      public Contract.AssetIssueContract.FrozenSupplyOrBuilder getFrozenSupplyOrBuilder(int index)
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`

      Specified by:
      :   `getFrozenSupplyOrBuilder` in interface `Contract.AssetIssueContractOrBuilder`
    - #### getFrozenSupplyOrBuilderList

      ```
      public java.util.List<? extends Contract.AssetIssueContract.FrozenSupplyOrBuilder> getFrozenSupplyOrBuilderList()
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`

      Specified by:
      :   `getFrozenSupplyOrBuilderList` in interface `Contract.AssetIssueContractOrBuilder`
    - #### addFrozenSupplyBuilder

      ```
      public Contract.AssetIssueContract.FrozenSupply.Builder addFrozenSupplyBuilder()
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`
    - #### addFrozenSupplyBuilder

      ```
      public Contract.AssetIssueContract.FrozenSupply.Builder addFrozenSupplyBuilder(int index)
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`
    - #### getFrozenSupplyBuilderList

      ```
      public java.util.List<Contract.AssetIssueContract.FrozenSupply.Builder> getFrozenSupplyBuilderList()
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`
    - #### getTrxNum

      ```
      public int getTrxNum()
      ```

      `int32 trx_num = 6;`

      Specified by:
      :   `getTrxNum` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The trxNum.
    - #### setTrxNum

      ```
      public Contract.AssetIssueContract.Builder setTrxNum(int value)
      ```

      `int32 trx_num = 6;`

      Parameters:
      :   `value` - The trxNum to set.

      Returns:
      :   This builder for chaining.
    - #### clearTrxNum

      ```
      public Contract.AssetIssueContract.Builder clearTrxNum()
      ```

      `int32 trx_num = 6;`

      Returns:
      :   This builder for chaining.
    - #### getPrecision

      ```
      public int getPrecision()
      ```

      `int32 precision = 7;`

      Specified by:
      :   `getPrecision` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The precision.
    - #### setPrecision

      ```
      public Contract.AssetIssueContract.Builder setPrecision(int value)
      ```

      `int32 precision = 7;`

      Parameters:
      :   `value` - The precision to set.

      Returns:
      :   This builder for chaining.
    - #### clearPrecision

      ```
      public Contract.AssetIssueContract.Builder clearPrecision()
      ```

      `int32 precision = 7;`

      Returns:
      :   This builder for chaining.
    - #### getNum

      ```
      public int getNum()
      ```

      `int32 num = 8;`

      Specified by:
      :   `getNum` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The num.
    - #### setNum

      ```
      public Contract.AssetIssueContract.Builder setNum(int value)
      ```

      `int32 num = 8;`

      Parameters:
      :   `value` - The num to set.

      Returns:
      :   This builder for chaining.
    - #### clearNum

      ```
      public Contract.AssetIssueContract.Builder clearNum()
      ```

      `int32 num = 8;`

      Returns:
      :   This builder for chaining.
    - #### getStartTime

      ```
      public long getStartTime()
      ```

      `int64 start_time = 9;`

      Specified by:
      :   `getStartTime` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The startTime.
    - #### setStartTime

      ```
      public Contract.AssetIssueContract.Builder setStartTime(long value)
      ```

      `int64 start_time = 9;`

      Parameters:
      :   `value` - The startTime to set.

      Returns:
      :   This builder for chaining.
    - #### clearStartTime

      ```
      public Contract.AssetIssueContract.Builder clearStartTime()
      ```

      `int64 start_time = 9;`

      Returns:
      :   This builder for chaining.
    - #### getEndTime

      ```
      public long getEndTime()
      ```

      `int64 end_time = 10;`

      Specified by:
      :   `getEndTime` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The endTime.
    - #### setEndTime

      ```
      public Contract.AssetIssueContract.Builder setEndTime(long value)
      ```

      `int64 end_time = 10;`

      Parameters:
      :   `value` - The endTime to set.

      Returns:
      :   This builder for chaining.
    - #### clearEndTime

      ```
      public Contract.AssetIssueContract.Builder clearEndTime()
      ```

      `int64 end_time = 10;`

      Returns:
      :   This builder for chaining.
    - #### getOrder

      ```
      public long getOrder()
      ```

      ```
       useless
      ```

      `int64 order = 11;`

      Specified by:
      :   `getOrder` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The order.
    - #### setOrder

      ```
      public Contract.AssetIssueContract.Builder setOrder(long value)
      ```

      ```
       useless
      ```

      `int64 order = 11;`

      Parameters:
      :   `value` - The order to set.

      Returns:
      :   This builder for chaining.
    - #### clearOrder

      ```
      public Contract.AssetIssueContract.Builder clearOrder()
      ```

      ```
       useless
      ```

      `int64 order = 11;`

      Returns:
      :   This builder for chaining.
    - #### getVoteScore

      ```
      public int getVoteScore()
      ```

      `int32 vote_score = 16;`

      Specified by:
      :   `getVoteScore` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The voteScore.
    - #### setVoteScore

      ```
      public Contract.AssetIssueContract.Builder setVoteScore(int value)
      ```

      `int32 vote_score = 16;`

      Parameters:
      :   `value` - The voteScore to set.

      Returns:
      :   This builder for chaining.
    - #### clearVoteScore

      ```
      public Contract.AssetIssueContract.Builder clearVoteScore()
      ```

      `int32 vote_score = 16;`

      Returns:
      :   This builder for chaining.
    - #### getDescription

      ```
      public com.google.protobuf.ByteString getDescription()
      ```

      `bytes description = 20;`

      Specified by:
      :   `getDescription` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The description.
    - #### setDescription

      ```
      public Contract.AssetIssueContract.Builder setDescription(com.google.protobuf.ByteString value)
      ```

      `bytes description = 20;`

      Parameters:
      :   `value` - The description to set.

      Returns:
      :   This builder for chaining.
    - #### clearDescription

      ```
      public Contract.AssetIssueContract.Builder clearDescription()
      ```

      `bytes description = 20;`

      Returns:
      :   This builder for chaining.
    - #### getUrl

      ```
      public com.google.protobuf.ByteString getUrl()
      ```

      `bytes url = 21;`

      Specified by:
      :   `getUrl` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The url.
    - #### setUrl

      ```
      public Contract.AssetIssueContract.Builder setUrl(com.google.protobuf.ByteString value)
      ```

      `bytes url = 21;`

      Parameters:
      :   `value` - The url to set.

      Returns:
      :   This builder for chaining.
    - #### clearUrl

      ```
      public Contract.AssetIssueContract.Builder clearUrl()
      ```

      `bytes url = 21;`

      Returns:
      :   This builder for chaining.
    - #### getFreeAssetNetLimit

      ```
      public long getFreeAssetNetLimit()
      ```

      `int64 free_asset_net_limit = 22;`

      Specified by:
      :   `getFreeAssetNetLimit` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The freeAssetNetLimit.
    - #### setFreeAssetNetLimit

      ```
      public Contract.AssetIssueContract.Builder setFreeAssetNetLimit(long value)
      ```

      `int64 free_asset_net_limit = 22;`

      Parameters:
      :   `value` - The freeAssetNetLimit to set.

      Returns:
      :   This builder for chaining.
    - #### clearFreeAssetNetLimit

      ```
      public Contract.AssetIssueContract.Builder clearFreeAssetNetLimit()
      ```

      `int64 free_asset_net_limit = 22;`

      Returns:
      :   This builder for chaining.
    - #### getPublicFreeAssetNetLimit

      ```
      public long getPublicFreeAssetNetLimit()
      ```

      `int64 public_free_asset_net_limit = 23;`

      Specified by:
      :   `getPublicFreeAssetNetLimit` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The publicFreeAssetNetLimit.
    - #### setPublicFreeAssetNetLimit

      ```
      public Contract.AssetIssueContract.Builder setPublicFreeAssetNetLimit(long value)
      ```

      `int64 public_free_asset_net_limit = 23;`

      Parameters:
      :   `value` - The publicFreeAssetNetLimit to set.

      Returns:
      :   This builder for chaining.
    - #### clearPublicFreeAssetNetLimit

      ```
      public Contract.AssetIssueContract.Builder clearPublicFreeAssetNetLimit()
      ```

      `int64 public_free_asset_net_limit = 23;`

      Returns:
      :   This builder for chaining.
    - #### getPublicFreeAssetNetUsage

      ```
      public long getPublicFreeAssetNetUsage()
      ```

      `int64 public_free_asset_net_usage = 24;`

      Specified by:
      :   `getPublicFreeAssetNetUsage` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The publicFreeAssetNetUsage.
    - #### setPublicFreeAssetNetUsage

      ```
      public Contract.AssetIssueContract.Builder setPublicFreeAssetNetUsage(long value)
      ```

      `int64 public_free_asset_net_usage = 24;`

      Parameters:
      :   `value` - The publicFreeAssetNetUsage to set.

      Returns:
      :   This builder for chaining.
    - #### clearPublicFreeAssetNetUsage

      ```
      public Contract.AssetIssueContract.Builder clearPublicFreeAssetNetUsage()
      ```

      `int64 public_free_asset_net_usage = 24;`

      Returns:
      :   This builder for chaining.
    - #### getPublicLatestFreeNetTime

      ```
      public long getPublicLatestFreeNetTime()
      ```

      `int64 public_latest_free_net_time = 25;`

      Specified by:
      :   `getPublicLatestFreeNetTime` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The publicLatestFreeNetTime.
    - #### setPublicLatestFreeNetTime

      ```
      public Contract.AssetIssueContract.Builder setPublicLatestFreeNetTime(long value)
      ```

      `int64 public_latest_free_net_time = 25;`

      Parameters:
      :   `value` - The publicLatestFreeNetTime to set.

      Returns:
      :   This builder for chaining.
    - #### clearPublicLatestFreeNetTime

      ```
      public Contract.AssetIssueContract.Builder clearPublicLatestFreeNetTime()
      ```

      `int64 public_latest_free_net_time = 25;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.AssetIssueContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.AssetIssueContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.Builder>`