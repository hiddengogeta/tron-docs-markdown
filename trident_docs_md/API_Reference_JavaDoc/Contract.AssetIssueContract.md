

org.tron.trident.proto

## Class Contract.AssetIssueContract

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Contract.AssetIssueContract

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Contract.AssetIssueContractOrBuilder](../../../../org/tron/trident/proto/Contract.AssetIssueContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.AssetIssueContract
  extends com.google.protobuf.GeneratedMessageV3
  implements Contract.AssetIssueContractOrBuilder
  ```

  Protobuf type `protocol.AssetIssueContract`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Contract.AssetIssueContract)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Contract.AssetIssueContract.Builder` Protobuf type `protocol.AssetIssueContract` |
    | `static class` | `Contract.AssetIssueContract.FrozenSupply` Protobuf type `protocol.AssetIssueContract.FrozenSupply` |
    | `static interface` | `Contract.AssetIssueContract.FrozenSupplyOrBuilder` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `ABBR_FIELD_NUMBER` |
    | `static int` | `DESCRIPTION_FIELD_NUMBER` |
    | `static int` | `END_TIME_FIELD_NUMBER` |
    | `static int` | `FREE_ASSET_NET_LIMIT_FIELD_NUMBER` |
    | `static int` | `FROZEN_SUPPLY_FIELD_NUMBER` |
    | `static int` | `ID_FIELD_NUMBER` |
    | `static int` | `NAME_FIELD_NUMBER` |
    | `static int` | `NUM_FIELD_NUMBER` |
    | `static int` | `ORDER_FIELD_NUMBER` |
    | `static int` | `OWNER_ADDRESS_FIELD_NUMBER` |
    | `static int` | `PRECISION_FIELD_NUMBER` |
    | `static int` | `PUBLIC_FREE_ASSET_NET_LIMIT_FIELD_NUMBER` |
    | `static int` | `PUBLIC_FREE_ASSET_NET_USAGE_FIELD_NUMBER` |
    | `static int` | `PUBLIC_LATEST_FREE_NET_TIME_FIELD_NUMBER` |
    | `static int` | `START_TIME_FIELD_NUMBER` |
    | `static int` | `TOTAL_SUPPLY_FIELD_NUMBER` |
    | `static int` | `TRX_NUM_FIELD_NUMBER` |
    | `static int` | `URL_FIELD_NUMBER` |
    | `static int` | `VOTE_SCORE_FIELD_NUMBER` |

    - ### Fields inherited from class com.google.protobuf.GeneratedMessageV3

      `alwaysUseFieldBuilders, unknownFields`
    - ### Fields inherited from class com.google.protobuf.AbstractMessage

      `memoizedSize`
    - ### Fields inherited from class com.google.protobuf.AbstractMessageLite

      `memoizedHashCode`
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `boolean` | `equals(java.lang.Object obj)` |
    | `com.google.protobuf.ByteString` | `getAbbr()` `bytes abbr = 3;` |
    | `static Contract.AssetIssueContract` | `getDefaultInstance()` |
    | `Contract.AssetIssueContract` | `getDefaultInstanceForType()` |
    | `com.google.protobuf.ByteString` | `getDescription()` `bytes description = 20;` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
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
    | `com.google.protobuf.Parser<Contract.AssetIssueContract>` | `getParserForType()` |
    | `int` | `getPrecision()` `int32 precision = 7;` |
    | `long` | `getPublicFreeAssetNetLimit()` `int64 public_free_asset_net_limit = 23;` |
    | `long` | `getPublicFreeAssetNetUsage()` `int64 public_free_asset_net_usage = 24;` |
    | `long` | `getPublicLatestFreeNetTime()` `int64 public_latest_free_net_time = 25;` |
    | `int` | `getSerializedSize()` |
    | `long` | `getStartTime()` `int64 start_time = 9;` |
    | `long` | `getTotalSupply()` `int64 total_supply = 4;` |
    | `int` | `getTrxNum()` `int32 trx_num = 6;` |
    | `com.google.protobuf.ByteString` | `getUrl()` `bytes url = 21;` |
    | `int` | `getVoteScore()` `int32 vote_score = 16;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Contract.AssetIssueContract.Builder` | `newBuilder()` |
    | `static Contract.AssetIssueContract.Builder` | `newBuilder(Contract.AssetIssueContract prototype)` |
    | `Contract.AssetIssueContract.Builder` | `newBuilderForType()` |
    | `protected Contract.AssetIssueContract.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Contract.AssetIssueContract` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Contract.AssetIssueContract` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.AssetIssueContract` | `parseFrom(byte[] data)` |
    | `static Contract.AssetIssueContract` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.AssetIssueContract` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Contract.AssetIssueContract` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.AssetIssueContract` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Contract.AssetIssueContract` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.AssetIssueContract` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Contract.AssetIssueContract` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.AssetIssueContract` | `parseFrom(java.io.InputStream input)` |
    | `static Contract.AssetIssueContract` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Contract.AssetIssueContract>` | `parser()` |
    | `Contract.AssetIssueContract.Builder` | `toBuilder()` |
    | `void` | `writeTo(com.google.protobuf.CodedOutputStream output)` |

    - ### Methods inherited from class com.google.protobuf.GeneratedMessageV3

      `canUseUnsafe, computeStringSize, computeStringSizeNoTag, emptyBooleanList, emptyDoubleList, emptyFloatList, emptyIntList, emptyList, emptyLongList, getAllFields, getDescriptorForType, getField, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof, internalGetMapField, internalGetMapFieldReflection, isStringEmpty, makeExtensionsImmutable, makeMutableCopy, makeMutableCopy, mergeFromAndMakeImmutableInternal, mutableCopy, mutableCopy, mutableCopy, mutableCopy, mutableCopy, newBooleanList, newBuilderForType, newDoubleList, newFloatList, newIntList, newLongList, parseDelimitedWithIOException, parseDelimitedWithIOException, parseUnknownField, parseUnknownFieldProto3, parseWithIOException, parseWithIOException, parseWithIOException, parseWithIOException, serializeBooleanMapTo, serializeIntegerMapTo, serializeLongMapTo, serializeStringMapTo, writeReplace, writeString, writeStringNoTag`
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

    - #### ID\_FIELD\_NUMBER

      ```
      public static final int ID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.AssetIssueContract.ID_FIELD_NUMBER)
    - #### OWNER\_ADDRESS\_FIELD\_NUMBER

      ```
      public static final int OWNER_ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.AssetIssueContract.OWNER_ADDRESS_FIELD_NUMBER)
    - #### NAME\_FIELD\_NUMBER

      ```
      public static final int NAME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.AssetIssueContract.NAME_FIELD_NUMBER)
    - #### ABBR\_FIELD\_NUMBER

      ```
      public static final int ABBR_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.AssetIssueContract.ABBR_FIELD_NUMBER)
    - #### TOTAL\_SUPPLY\_FIELD\_NUMBER

      ```
      public static final int TOTAL_SUPPLY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.AssetIssueContract.TOTAL_SUPPLY_FIELD_NUMBER)
    - #### FROZEN\_SUPPLY\_FIELD\_NUMBER

      ```
      public static final int FROZEN_SUPPLY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.AssetIssueContract.FROZEN_SUPPLY_FIELD_NUMBER)
    - #### TRX\_NUM\_FIELD\_NUMBER

      ```
      public static final int TRX_NUM_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.AssetIssueContract.TRX_NUM_FIELD_NUMBER)
    - #### PRECISION\_FIELD\_NUMBER

      ```
      public static final int PRECISION_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.AssetIssueContract.PRECISION_FIELD_NUMBER)
    - #### NUM\_FIELD\_NUMBER

      ```
      public static final int NUM_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.AssetIssueContract.NUM_FIELD_NUMBER)
    - #### START\_TIME\_FIELD\_NUMBER

      ```
      public static final int START_TIME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.AssetIssueContract.START_TIME_FIELD_NUMBER)
    - #### END\_TIME\_FIELD\_NUMBER

      ```
      public static final int END_TIME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.AssetIssueContract.END_TIME_FIELD_NUMBER)
    - #### ORDER\_FIELD\_NUMBER

      ```
      public static final int ORDER_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.AssetIssueContract.ORDER_FIELD_NUMBER)
    - #### VOTE\_SCORE\_FIELD\_NUMBER

      ```
      public static final int VOTE_SCORE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.AssetIssueContract.VOTE_SCORE_FIELD_NUMBER)
    - #### DESCRIPTION\_FIELD\_NUMBER

      ```
      public static final int DESCRIPTION_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.AssetIssueContract.DESCRIPTION_FIELD_NUMBER)
    - #### URL\_FIELD\_NUMBER

      ```
      public static final int URL_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.AssetIssueContract.URL_FIELD_NUMBER)
    - #### FREE\_ASSET\_NET\_LIMIT\_FIELD\_NUMBER

      ```
      public static final int FREE_ASSET_NET_LIMIT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.AssetIssueContract.FREE_ASSET_NET_LIMIT_FIELD_NUMBER)
    - #### PUBLIC\_FREE\_ASSET\_NET\_LIMIT\_FIELD\_NUMBER

      ```
      public static final int PUBLIC_FREE_ASSET_NET_LIMIT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.AssetIssueContract.PUBLIC_FREE_ASSET_NET_LIMIT_FIELD_NUMBER)
    - #### PUBLIC\_FREE\_ASSET\_NET\_USAGE\_FIELD\_NUMBER

      ```
      public static final int PUBLIC_FREE_ASSET_NET_USAGE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.AssetIssueContract.PUBLIC_FREE_ASSET_NET_USAGE_FIELD_NUMBER)
    - #### PUBLIC\_LATEST\_FREE\_NET\_TIME\_FIELD\_NUMBER

      ```
      public static final int PUBLIC_LATEST_FREE_NET_TIME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.AssetIssueContract.PUBLIC_LATEST_FREE_NET_TIME_FIELD_NUMBER)
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
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3`
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
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### getName

      ```
      public com.google.protobuf.ByteString getName()
      ```

      `bytes name = 2;`

      Specified by:
      :   `getName` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The name.
    - #### getAbbr

      ```
      public com.google.protobuf.ByteString getAbbr()
      ```

      `bytes abbr = 3;`

      Specified by:
      :   `getAbbr` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The abbr.
    - #### getTotalSupply

      ```
      public long getTotalSupply()
      ```

      `int64 total_supply = 4;`

      Specified by:
      :   `getTotalSupply` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The totalSupply.
    - #### getFrozenSupplyList

      ```
      public java.util.List<Contract.AssetIssueContract.FrozenSupply> getFrozenSupplyList()
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`

      Specified by:
      :   `getFrozenSupplyList` in interface `Contract.AssetIssueContractOrBuilder`
    - #### getFrozenSupplyOrBuilderList

      ```
      public java.util.List<? extends Contract.AssetIssueContract.FrozenSupplyOrBuilder> getFrozenSupplyOrBuilderList()
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`

      Specified by:
      :   `getFrozenSupplyOrBuilderList` in interface `Contract.AssetIssueContractOrBuilder`
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
    - #### getFrozenSupplyOrBuilder

      ```
      public Contract.AssetIssueContract.FrozenSupplyOrBuilder getFrozenSupplyOrBuilder(int index)
      ```

      `repeated .protocol.AssetIssueContract.FrozenSupply frozen_supply = 5;`

      Specified by:
      :   `getFrozenSupplyOrBuilder` in interface `Contract.AssetIssueContractOrBuilder`
    - #### getTrxNum

      ```
      public int getTrxNum()
      ```

      `int32 trx_num = 6;`

      Specified by:
      :   `getTrxNum` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The trxNum.
    - #### getPrecision

      ```
      public int getPrecision()
      ```

      `int32 precision = 7;`

      Specified by:
      :   `getPrecision` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The precision.
    - #### getNum

      ```
      public int getNum()
      ```

      `int32 num = 8;`

      Specified by:
      :   `getNum` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The num.
    - #### getStartTime

      ```
      public long getStartTime()
      ```

      `int64 start_time = 9;`

      Specified by:
      :   `getStartTime` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The startTime.
    - #### getEndTime

      ```
      public long getEndTime()
      ```

      `int64 end_time = 10;`

      Specified by:
      :   `getEndTime` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The endTime.
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
    - #### getVoteScore

      ```
      public int getVoteScore()
      ```

      `int32 vote_score = 16;`

      Specified by:
      :   `getVoteScore` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The voteScore.
    - #### getDescription

      ```
      public com.google.protobuf.ByteString getDescription()
      ```

      `bytes description = 20;`

      Specified by:
      :   `getDescription` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The description.
    - #### getUrl

      ```
      public com.google.protobuf.ByteString getUrl()
      ```

      `bytes url = 21;`

      Specified by:
      :   `getUrl` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The url.
    - #### getFreeAssetNetLimit

      ```
      public long getFreeAssetNetLimit()
      ```

      `int64 free_asset_net_limit = 22;`

      Specified by:
      :   `getFreeAssetNetLimit` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The freeAssetNetLimit.
    - #### getPublicFreeAssetNetLimit

      ```
      public long getPublicFreeAssetNetLimit()
      ```

      `int64 public_free_asset_net_limit = 23;`

      Specified by:
      :   `getPublicFreeAssetNetLimit` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The publicFreeAssetNetLimit.
    - #### getPublicFreeAssetNetUsage

      ```
      public long getPublicFreeAssetNetUsage()
      ```

      `int64 public_free_asset_net_usage = 24;`

      Specified by:
      :   `getPublicFreeAssetNetUsage` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The publicFreeAssetNetUsage.
    - #### getPublicLatestFreeNetTime

      ```
      public long getPublicLatestFreeNetTime()
      ```

      `int64 public_latest_free_net_time = 25;`

      Specified by:
      :   `getPublicLatestFreeNetTime` in interface `Contract.AssetIssueContractOrBuilder`

      Returns:
      :   The publicLatestFreeNetTime.
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
      public static Contract.AssetIssueContract parseFrom(java.nio.ByteBuffer data)
                                                   throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.AssetIssueContract parseFrom(java.nio.ByteBuffer data,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.AssetIssueContract parseFrom(com.google.protobuf.ByteString data)
                                                   throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.AssetIssueContract parseFrom(com.google.protobuf.ByteString data,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.AssetIssueContract parseFrom(byte[] data)
                                                   throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.AssetIssueContract parseFrom(byte[] data,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.AssetIssueContract parseFrom(java.io.InputStream input)
                                                   throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.AssetIssueContract parseFrom(java.io.InputStream input,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Contract.AssetIssueContract parseDelimitedFrom(java.io.InputStream input)
                                                            throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Contract.AssetIssueContract parseDelimitedFrom(java.io.InputStream input,
                                                                   com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                            throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.AssetIssueContract parseFrom(com.google.protobuf.CodedInputStream input)
                                                   throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.AssetIssueContract parseFrom(com.google.protobuf.CodedInputStream input,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Contract.AssetIssueContract.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Contract.AssetIssueContract.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Contract.AssetIssueContract.Builder newBuilder(Contract.AssetIssueContract prototype)
      ```
    - #### toBuilder

      ```
      public Contract.AssetIssueContract.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Contract.AssetIssueContract.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Contract.AssetIssueContract getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Contract.AssetIssueContract> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Contract.AssetIssueContract> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Contract.AssetIssueContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`