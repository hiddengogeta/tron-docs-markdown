

org.tron.trident.proto

## Class Response.NodeInfo.PeerInfo

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.NodeInfo.PeerInfo

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.NodeInfo.PeerInfoOrBuilder](../../../../org/tron/trident/proto/Response.NodeInfo.PeerInfoOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.NodeInfo](../../../../org/tron/trident/proto/Response.NodeInfo.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.NodeInfo.PeerInfo
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.NodeInfo.PeerInfoOrBuilder
  ```

  Protobuf type `protocol.NodeInfo.PeerInfo`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.NodeInfo.PeerInfo.Builder` Protobuf type `protocol.NodeInfo.PeerInfo` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `AVGLATENCY_FIELD_NUMBER` |
    | `static int` | `BLOCKINPORCSIZE_FIELD_NUMBER` |
    | `static int` | `CONNECTTIME_FIELD_NUMBER` |
    | `static int` | `DISCONNECTTIMES_FIELD_NUMBER` |
    | `static int` | `HEADBLOCKTIMEWEBOTHHAVE_FIELD_NUMBER` |
    | `static int` | `HEADBLOCKWEBOTHHAVE_FIELD_NUMBER` |
    | `static int` | `HOST_FIELD_NUMBER` |
    | `static int` | `INFLOW_FIELD_NUMBER` |
    | `static int` | `ISACTIVE_FIELD_NUMBER` |
    | `static int` | `LASTBLOCKUPDATETIME_FIELD_NUMBER` |
    | `static int` | `LASTSYNCBLOCK_FIELD_NUMBER` |
    | `static int` | `LOCALDISCONNECTREASON_FIELD_NUMBER` |
    | `static int` | `NEEDSYNCFROMPEER_FIELD_NUMBER` |
    | `static int` | `NEEDSYNCFROMUS_FIELD_NUMBER` |
    | `static int` | `NODECOUNT_FIELD_NUMBER` |
    | `static int` | `NODEID_FIELD_NUMBER` |
    | `static int` | `PORT_FIELD_NUMBER` |
    | `static int` | `REMAINNUM_FIELD_NUMBER` |
    | `static int` | `REMOTEDISCONNECTREASON_FIELD_NUMBER` |
    | `static int` | `SCORE_FIELD_NUMBER` |
    | `static int` | `SYNCBLOCKREQUESTEDSIZE_FIELD_NUMBER` |
    | `static int` | `SYNCFLAG_FIELD_NUMBER` |
    | `static int` | `SYNCTOFETCHSIZE_FIELD_NUMBER` |
    | `static int` | `SYNCTOFETCHSIZEPEEKNUM_FIELD_NUMBER` |
    | `static int` | `UNFETCHSYNNUM_FIELD_NUMBER` |

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
    | `double` | `getAvgLatency()` `double avgLatency = 12;` |
    | `int` | `getBlockInPorcSize()` `int32 blockInPorcSize = 17;` |
    | `long` | `getConnectTime()` `int64 connectTime = 11;` |
    | `static Response.NodeInfo.PeerInfo` | `getDefaultInstance()` |
    | `Response.NodeInfo.PeerInfo` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `int` | `getDisconnectTimes()` `int32 disconnectTimes = 23;` |
    | `long` | `getHeadBlockTimeWeBothHave()` `int64 headBlockTimeWeBothHave = 5;` |
    | `java.lang.String` | `getHeadBlockWeBothHave()` `string headBlockWeBothHave = 18;` |
    | `com.google.protobuf.ByteString` | `getHeadBlockWeBothHaveBytes()` `string headBlockWeBothHave = 18;` |
    | `java.lang.String` | `getHost()` `string host = 8;` |
    | `com.google.protobuf.ByteString` | `getHostBytes()` `string host = 8;` |
    | `long` | `getInFlow()` `int64 inFlow = 22;` |
    | `boolean` | `getIsActive()` `bool isActive = 19;` |
    | `long` | `getLastBlockUpdateTime()` `int64 lastBlockUpdateTime = 3;` |
    | `java.lang.String` | `getLastSyncBlock()` `string lastSyncBlock = 1;` |
    | `com.google.protobuf.ByteString` | `getLastSyncBlockBytes()` `string lastSyncBlock = 1;` |
    | `java.lang.String` | `getLocalDisconnectReason()` `string localDisconnectReason = 24;` |
    | `com.google.protobuf.ByteString` | `getLocalDisconnectReasonBytes()` `string localDisconnectReason = 24;` |
    | `boolean` | `getNeedSyncFromPeer()` `bool needSyncFromPeer = 6;` |
    | `boolean` | `getNeedSyncFromUs()` `bool needSyncFromUs = 7;` |
    | `int` | `getNodeCount()` `int32 nodeCount = 21;` |
    | `java.lang.String` | `getNodeId()` `string nodeId = 10;` |
    | `com.google.protobuf.ByteString` | `getNodeIdBytes()` `string nodeId = 10;` |
    | `com.google.protobuf.Parser<Response.NodeInfo.PeerInfo>` | `getParserForType()` |
    | `int` | `getPort()` `int32 port = 9;` |
    | `long` | `getRemainNum()` `int64 remainNum = 2;` |
    | `java.lang.String` | `getRemoteDisconnectReason()` `string remoteDisconnectReason = 25;` |
    | `com.google.protobuf.ByteString` | `getRemoteDisconnectReasonBytes()` `string remoteDisconnectReason = 25;` |
    | `int` | `getScore()` `int32 score = 20;` |
    | `int` | `getSerializedSize()` |
    | `int` | `getSyncBlockRequestedSize()` `int32 syncBlockRequestedSize = 15;` |
    | `boolean` | `getSyncFlag()` `bool syncFlag = 4;` |
    | `int` | `getSyncToFetchSize()` `int32 syncToFetchSize = 13;` |
    | `long` | `getSyncToFetchSizePeekNum()` `int64 syncToFetchSizePeekNum = 14;` |
    | `long` | `getUnFetchSynNum()` `int64 unFetchSynNum = 16;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Response.NodeInfo.PeerInfo.Builder` | `newBuilder()` |
    | `static Response.NodeInfo.PeerInfo.Builder` | `newBuilder(Response.NodeInfo.PeerInfo prototype)` |
    | `Response.NodeInfo.PeerInfo.Builder` | `newBuilderForType()` |
    | `protected Response.NodeInfo.PeerInfo.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.NodeInfo.PeerInfo` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.NodeInfo.PeerInfo` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.PeerInfo` | `parseFrom(byte[] data)` |
    | `static Response.NodeInfo.PeerInfo` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.PeerInfo` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.NodeInfo.PeerInfo` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.PeerInfo` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.NodeInfo.PeerInfo` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.PeerInfo` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.NodeInfo.PeerInfo` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.PeerInfo` | `parseFrom(java.io.InputStream input)` |
    | `static Response.NodeInfo.PeerInfo` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.NodeInfo.PeerInfo>` | `parser()` |
    | `Response.NodeInfo.PeerInfo.Builder` | `toBuilder()` |
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

    - #### LASTSYNCBLOCK\_FIELD\_NUMBER

      ```
      public static final int LASTSYNCBLOCK_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.LASTSYNCBLOCK_FIELD_NUMBER)
    - #### REMAINNUM\_FIELD\_NUMBER

      ```
      public static final int REMAINNUM_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.REMAINNUM_FIELD_NUMBER)
    - #### LASTBLOCKUPDATETIME\_FIELD\_NUMBER

      ```
      public static final int LASTBLOCKUPDATETIME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.LASTBLOCKUPDATETIME_FIELD_NUMBER)
    - #### SYNCFLAG\_FIELD\_NUMBER

      ```
      public static final int SYNCFLAG_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.SYNCFLAG_FIELD_NUMBER)
    - #### HEADBLOCKTIMEWEBOTHHAVE\_FIELD\_NUMBER

      ```
      public static final int HEADBLOCKTIMEWEBOTHHAVE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.HEADBLOCKTIMEWEBOTHHAVE_FIELD_NUMBER)
    - #### NEEDSYNCFROMPEER\_FIELD\_NUMBER

      ```
      public static final int NEEDSYNCFROMPEER_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.NEEDSYNCFROMPEER_FIELD_NUMBER)
    - #### NEEDSYNCFROMUS\_FIELD\_NUMBER

      ```
      public static final int NEEDSYNCFROMUS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.NEEDSYNCFROMUS_FIELD_NUMBER)
    - #### HOST\_FIELD\_NUMBER

      ```
      public static final int HOST_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.HOST_FIELD_NUMBER)
    - #### PORT\_FIELD\_NUMBER

      ```
      public static final int PORT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.PORT_FIELD_NUMBER)
    - #### NODEID\_FIELD\_NUMBER

      ```
      public static final int NODEID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.NODEID_FIELD_NUMBER)
    - #### CONNECTTIME\_FIELD\_NUMBER

      ```
      public static final int CONNECTTIME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.CONNECTTIME_FIELD_NUMBER)
    - #### AVGLATENCY\_FIELD\_NUMBER

      ```
      public static final int AVGLATENCY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.AVGLATENCY_FIELD_NUMBER)
    - #### SYNCTOFETCHSIZE\_FIELD\_NUMBER

      ```
      public static final int SYNCTOFETCHSIZE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.SYNCTOFETCHSIZE_FIELD_NUMBER)
    - #### SYNCTOFETCHSIZEPEEKNUM\_FIELD\_NUMBER

      ```
      public static final int SYNCTOFETCHSIZEPEEKNUM_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.SYNCTOFETCHSIZEPEEKNUM_FIELD_NUMBER)
    - #### SYNCBLOCKREQUESTEDSIZE\_FIELD\_NUMBER

      ```
      public static final int SYNCBLOCKREQUESTEDSIZE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.SYNCBLOCKREQUESTEDSIZE_FIELD_NUMBER)
    - #### UNFETCHSYNNUM\_FIELD\_NUMBER

      ```
      public static final int UNFETCHSYNNUM_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.UNFETCHSYNNUM_FIELD_NUMBER)
    - #### BLOCKINPORCSIZE\_FIELD\_NUMBER

      ```
      public static final int BLOCKINPORCSIZE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.BLOCKINPORCSIZE_FIELD_NUMBER)
    - #### HEADBLOCKWEBOTHHAVE\_FIELD\_NUMBER

      ```
      public static final int HEADBLOCKWEBOTHHAVE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.HEADBLOCKWEBOTHHAVE_FIELD_NUMBER)
    - #### ISACTIVE\_FIELD\_NUMBER

      ```
      public static final int ISACTIVE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.ISACTIVE_FIELD_NUMBER)
    - #### SCORE\_FIELD\_NUMBER

      ```
      public static final int SCORE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.SCORE_FIELD_NUMBER)
    - #### NODECOUNT\_FIELD\_NUMBER

      ```
      public static final int NODECOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.NODECOUNT_FIELD_NUMBER)
    - #### INFLOW\_FIELD\_NUMBER

      ```
      public static final int INFLOW_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.INFLOW_FIELD_NUMBER)
    - #### DISCONNECTTIMES\_FIELD\_NUMBER

      ```
      public static final int DISCONNECTTIMES_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.DISCONNECTTIMES_FIELD_NUMBER)
    - #### LOCALDISCONNECTREASON\_FIELD\_NUMBER

      ```
      public static final int LOCALDISCONNECTREASON_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.LOCALDISCONNECTREASON_FIELD_NUMBER)
    - #### REMOTEDISCONNECTREASON\_FIELD\_NUMBER

      ```
      public static final int REMOTEDISCONNECTREASON_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PeerInfo.REMOTEDISCONNECTREASON_FIELD_NUMBER)
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
    - #### getLastSyncBlock

      ```
      public java.lang.String getLastSyncBlock()
      ```

      `string lastSyncBlock = 1;`

      Specified by:
      :   `getLastSyncBlock` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The lastSyncBlock.
    - #### getLastSyncBlockBytes

      ```
      public com.google.protobuf.ByteString getLastSyncBlockBytes()
      ```

      `string lastSyncBlock = 1;`

      Specified by:
      :   `getLastSyncBlockBytes` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The bytes for lastSyncBlock.
    - #### getRemainNum

      ```
      public long getRemainNum()
      ```

      `int64 remainNum = 2;`

      Specified by:
      :   `getRemainNum` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The remainNum.
    - #### getLastBlockUpdateTime

      ```
      public long getLastBlockUpdateTime()
      ```

      `int64 lastBlockUpdateTime = 3;`

      Specified by:
      :   `getLastBlockUpdateTime` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The lastBlockUpdateTime.
    - #### getSyncFlag

      ```
      public boolean getSyncFlag()
      ```

      `bool syncFlag = 4;`

      Specified by:
      :   `getSyncFlag` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The syncFlag.
    - #### getHeadBlockTimeWeBothHave

      ```
      public long getHeadBlockTimeWeBothHave()
      ```

      `int64 headBlockTimeWeBothHave = 5;`

      Specified by:
      :   `getHeadBlockTimeWeBothHave` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The headBlockTimeWeBothHave.
    - #### getNeedSyncFromPeer

      ```
      public boolean getNeedSyncFromPeer()
      ```

      `bool needSyncFromPeer = 6;`

      Specified by:
      :   `getNeedSyncFromPeer` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The needSyncFromPeer.
    - #### getNeedSyncFromUs

      ```
      public boolean getNeedSyncFromUs()
      ```

      `bool needSyncFromUs = 7;`

      Specified by:
      :   `getNeedSyncFromUs` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The needSyncFromUs.
    - #### getHost

      ```
      public java.lang.String getHost()
      ```

      `string host = 8;`

      Specified by:
      :   `getHost` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The host.
    - #### getHostBytes

      ```
      public com.google.protobuf.ByteString getHostBytes()
      ```

      `string host = 8;`

      Specified by:
      :   `getHostBytes` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The bytes for host.
    - #### getPort

      ```
      public int getPort()
      ```

      `int32 port = 9;`

      Specified by:
      :   `getPort` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The port.
    - #### getNodeId

      ```
      public java.lang.String getNodeId()
      ```

      `string nodeId = 10;`

      Specified by:
      :   `getNodeId` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The nodeId.
    - #### getNodeIdBytes

      ```
      public com.google.protobuf.ByteString getNodeIdBytes()
      ```

      `string nodeId = 10;`

      Specified by:
      :   `getNodeIdBytes` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The bytes for nodeId.
    - #### getConnectTime

      ```
      public long getConnectTime()
      ```

      `int64 connectTime = 11;`

      Specified by:
      :   `getConnectTime` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The connectTime.
    - #### getAvgLatency

      ```
      public double getAvgLatency()
      ```

      `double avgLatency = 12;`

      Specified by:
      :   `getAvgLatency` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The avgLatency.
    - #### getSyncToFetchSize

      ```
      public int getSyncToFetchSize()
      ```

      `int32 syncToFetchSize = 13;`

      Specified by:
      :   `getSyncToFetchSize` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The syncToFetchSize.
    - #### getSyncToFetchSizePeekNum

      ```
      public long getSyncToFetchSizePeekNum()
      ```

      `int64 syncToFetchSizePeekNum = 14;`

      Specified by:
      :   `getSyncToFetchSizePeekNum` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The syncToFetchSizePeekNum.
    - #### getSyncBlockRequestedSize

      ```
      public int getSyncBlockRequestedSize()
      ```

      `int32 syncBlockRequestedSize = 15;`

      Specified by:
      :   `getSyncBlockRequestedSize` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The syncBlockRequestedSize.
    - #### getUnFetchSynNum

      ```
      public long getUnFetchSynNum()
      ```

      `int64 unFetchSynNum = 16;`

      Specified by:
      :   `getUnFetchSynNum` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The unFetchSynNum.
    - #### getBlockInPorcSize

      ```
      public int getBlockInPorcSize()
      ```

      `int32 blockInPorcSize = 17;`

      Specified by:
      :   `getBlockInPorcSize` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The blockInPorcSize.
    - #### getHeadBlockWeBothHave

      ```
      public java.lang.String getHeadBlockWeBothHave()
      ```

      `string headBlockWeBothHave = 18;`

      Specified by:
      :   `getHeadBlockWeBothHave` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The headBlockWeBothHave.
    - #### getHeadBlockWeBothHaveBytes

      ```
      public com.google.protobuf.ByteString getHeadBlockWeBothHaveBytes()
      ```

      `string headBlockWeBothHave = 18;`

      Specified by:
      :   `getHeadBlockWeBothHaveBytes` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The bytes for headBlockWeBothHave.
    - #### getIsActive

      ```
      public boolean getIsActive()
      ```

      `bool isActive = 19;`

      Specified by:
      :   `getIsActive` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The isActive.
    - #### getScore

      ```
      public int getScore()
      ```

      `int32 score = 20;`

      Specified by:
      :   `getScore` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The score.
    - #### getNodeCount

      ```
      public int getNodeCount()
      ```

      `int32 nodeCount = 21;`

      Specified by:
      :   `getNodeCount` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The nodeCount.
    - #### getInFlow

      ```
      public long getInFlow()
      ```

      `int64 inFlow = 22;`

      Specified by:
      :   `getInFlow` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The inFlow.
    - #### getDisconnectTimes

      ```
      public int getDisconnectTimes()
      ```

      `int32 disconnectTimes = 23;`

      Specified by:
      :   `getDisconnectTimes` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The disconnectTimes.
    - #### getLocalDisconnectReason

      ```
      public java.lang.String getLocalDisconnectReason()
      ```

      `string localDisconnectReason = 24;`

      Specified by:
      :   `getLocalDisconnectReason` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The localDisconnectReason.
    - #### getLocalDisconnectReasonBytes

      ```
      public com.google.protobuf.ByteString getLocalDisconnectReasonBytes()
      ```

      `string localDisconnectReason = 24;`

      Specified by:
      :   `getLocalDisconnectReasonBytes` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The bytes for localDisconnectReason.
    - #### getRemoteDisconnectReason

      ```
      public java.lang.String getRemoteDisconnectReason()
      ```

      `string remoteDisconnectReason = 25;`

      Specified by:
      :   `getRemoteDisconnectReason` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The remoteDisconnectReason.
    - #### getRemoteDisconnectReasonBytes

      ```
      public com.google.protobuf.ByteString getRemoteDisconnectReasonBytes()
      ```

      `string remoteDisconnectReason = 25;`

      Specified by:
      :   `getRemoteDisconnectReasonBytes` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The bytes for remoteDisconnectReason.
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
      public static Response.NodeInfo.PeerInfo parseFrom(java.nio.ByteBuffer data)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.PeerInfo parseFrom(java.nio.ByteBuffer data,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.PeerInfo parseFrom(com.google.protobuf.ByteString data)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.PeerInfo parseFrom(com.google.protobuf.ByteString data,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.PeerInfo parseFrom(byte[] data)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.PeerInfo parseFrom(byte[] data,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.PeerInfo parseFrom(java.io.InputStream input)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.PeerInfo parseFrom(java.io.InputStream input,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.NodeInfo.PeerInfo parseDelimitedFrom(java.io.InputStream input)
                                                           throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.NodeInfo.PeerInfo parseDelimitedFrom(java.io.InputStream input,
                                                                  com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                           throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.PeerInfo parseFrom(com.google.protobuf.CodedInputStream input)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.PeerInfo parseFrom(com.google.protobuf.CodedInputStream input,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.NodeInfo.PeerInfo.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.NodeInfo.PeerInfo.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.NodeInfo.PeerInfo.Builder newBuilder(Response.NodeInfo.PeerInfo prototype)
      ```
    - #### toBuilder

      ```
      public Response.NodeInfo.PeerInfo.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.NodeInfo.PeerInfo.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.NodeInfo.PeerInfo getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.NodeInfo.PeerInfo> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.NodeInfo.PeerInfo> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.NodeInfo.PeerInfo getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`