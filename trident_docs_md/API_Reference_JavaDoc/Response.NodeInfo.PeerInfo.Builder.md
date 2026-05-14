

org.tron.trident.proto

## Class Response.NodeInfo.PeerInfo.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.NodeInfo.PeerInfo.Builder](../../../../org/tron/trident/proto/Response.NodeInfo.PeerInfo.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.NodeInfo.PeerInfo.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.NodeInfo.PeerInfoOrBuilder](../../../../org/tron/trident/proto/Response.NodeInfo.PeerInfoOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.NodeInfo.PeerInfo](../../../../org/tron/trident/proto/Response.NodeInfo.PeerInfo.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.NodeInfo.PeerInfo.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.PeerInfo.Builder>
  implements Response.NodeInfo.PeerInfoOrBuilder
  ```

  Protobuf type `protocol.NodeInfo.PeerInfo`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.NodeInfo.PeerInfo.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.NodeInfo.PeerInfo` | `build()` |
    | `Response.NodeInfo.PeerInfo` | `buildPartial()` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clear()` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearAvgLatency()` `double avgLatency = 12;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearBlockInPorcSize()` `int32 blockInPorcSize = 17;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearConnectTime()` `int64 connectTime = 11;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearDisconnectTimes()` `int32 disconnectTimes = 23;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearHeadBlockTimeWeBothHave()` `int64 headBlockTimeWeBothHave = 5;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearHeadBlockWeBothHave()` `string headBlockWeBothHave = 18;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearHost()` `string host = 8;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearInFlow()` `int64 inFlow = 22;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearIsActive()` `bool isActive = 19;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearLastBlockUpdateTime()` `int64 lastBlockUpdateTime = 3;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearLastSyncBlock()` `string lastSyncBlock = 1;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearLocalDisconnectReason()` `string localDisconnectReason = 24;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearNeedSyncFromPeer()` `bool needSyncFromPeer = 6;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearNeedSyncFromUs()` `bool needSyncFromUs = 7;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearNodeCount()` `int32 nodeCount = 21;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearNodeId()` `string nodeId = 10;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearPort()` `int32 port = 9;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearRemainNum()` `int64 remainNum = 2;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearRemoteDisconnectReason()` `string remoteDisconnectReason = 25;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearScore()` `int32 score = 20;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearSyncBlockRequestedSize()` `int32 syncBlockRequestedSize = 15;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearSyncFlag()` `bool syncFlag = 4;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearSyncToFetchSize()` `int32 syncToFetchSize = 13;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearSyncToFetchSizePeekNum()` `int64 syncToFetchSizePeekNum = 14;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clearUnFetchSynNum()` `int64 unFetchSynNum = 16;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `clone()` |
    | `double` | `getAvgLatency()` `double avgLatency = 12;` |
    | `int` | `getBlockInPorcSize()` `int32 blockInPorcSize = 17;` |
    | `long` | `getConnectTime()` `int64 connectTime = 11;` |
    | `Response.NodeInfo.PeerInfo` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
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
    | `int` | `getPort()` `int32 port = 9;` |
    | `long` | `getRemainNum()` `int64 remainNum = 2;` |
    | `java.lang.String` | `getRemoteDisconnectReason()` `string remoteDisconnectReason = 25;` |
    | `com.google.protobuf.ByteString` | `getRemoteDisconnectReasonBytes()` `string remoteDisconnectReason = 25;` |
    | `int` | `getScore()` `int32 score = 20;` |
    | `int` | `getSyncBlockRequestedSize()` `int32 syncBlockRequestedSize = 15;` |
    | `boolean` | `getSyncFlag()` `bool syncFlag = 4;` |
    | `int` | `getSyncToFetchSize()` `int32 syncToFetchSize = 13;` |
    | `long` | `getSyncToFetchSizePeekNum()` `int64 syncToFetchSizePeekNum = 14;` |
    | `long` | `getUnFetchSynNum()` `int64 unFetchSynNum = 16;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.NodeInfo.PeerInfo.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.NodeInfo.PeerInfo.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.NodeInfo.PeerInfo.Builder` | `mergeFrom(Response.NodeInfo.PeerInfo other)` |
    | `Response.NodeInfo.PeerInfo.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setAvgLatency(double value)` `double avgLatency = 12;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setBlockInPorcSize(int value)` `int32 blockInPorcSize = 17;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setConnectTime(long value)` `int64 connectTime = 11;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setDisconnectTimes(int value)` `int32 disconnectTimes = 23;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setHeadBlockTimeWeBothHave(long value)` `int64 headBlockTimeWeBothHave = 5;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setHeadBlockWeBothHave(java.lang.String value)` `string headBlockWeBothHave = 18;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setHeadBlockWeBothHaveBytes(com.google.protobuf.ByteString value)` `string headBlockWeBothHave = 18;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setHost(java.lang.String value)` `string host = 8;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setHostBytes(com.google.protobuf.ByteString value)` `string host = 8;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setInFlow(long value)` `int64 inFlow = 22;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setIsActive(boolean value)` `bool isActive = 19;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setLastBlockUpdateTime(long value)` `int64 lastBlockUpdateTime = 3;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setLastSyncBlock(java.lang.String value)` `string lastSyncBlock = 1;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setLastSyncBlockBytes(com.google.protobuf.ByteString value)` `string lastSyncBlock = 1;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setLocalDisconnectReason(java.lang.String value)` `string localDisconnectReason = 24;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setLocalDisconnectReasonBytes(com.google.protobuf.ByteString value)` `string localDisconnectReason = 24;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setNeedSyncFromPeer(boolean value)` `bool needSyncFromPeer = 6;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setNeedSyncFromUs(boolean value)` `bool needSyncFromUs = 7;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setNodeCount(int value)` `int32 nodeCount = 21;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setNodeId(java.lang.String value)` `string nodeId = 10;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setNodeIdBytes(com.google.protobuf.ByteString value)` `string nodeId = 10;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setPort(int value)` `int32 port = 9;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setRemainNum(long value)` `int64 remainNum = 2;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setRemoteDisconnectReason(java.lang.String value)` `string remoteDisconnectReason = 25;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setRemoteDisconnectReasonBytes(com.google.protobuf.ByteString value)` `string remoteDisconnectReason = 25;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setScore(int value)` `int32 score = 20;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setSyncBlockRequestedSize(int value)` `int32 syncBlockRequestedSize = 15;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setSyncFlag(boolean value)` `bool syncFlag = 4;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setSyncToFetchSize(int value)` `int32 syncToFetchSize = 13;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setSyncToFetchSizePeekNum(long value)` `int64 syncToFetchSizePeekNum = 14;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setUnFetchSynNum(long value)` `int64 unFetchSynNum = 16;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.PeerInfo.Builder>`
    - #### clear

      ```
      public Response.NodeInfo.PeerInfo.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.PeerInfo.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.PeerInfo.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.NodeInfo.PeerInfo getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.NodeInfo.PeerInfo build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.NodeInfo.PeerInfo buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.NodeInfo.PeerInfo.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.PeerInfo.Builder>`
    - #### setField

      ```
      public Response.NodeInfo.PeerInfo.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                         java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.PeerInfo.Builder>`
    - #### clearField

      ```
      public Response.NodeInfo.PeerInfo.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.PeerInfo.Builder>`
    - #### clearOneof

      ```
      public Response.NodeInfo.PeerInfo.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.PeerInfo.Builder>`
    - #### setRepeatedField

      ```
      public Response.NodeInfo.PeerInfo.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                 int index,
                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.PeerInfo.Builder>`
    - #### addRepeatedField

      ```
      public Response.NodeInfo.PeerInfo.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.PeerInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeInfo.PeerInfo.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.NodeInfo.PeerInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeInfo.PeerInfo.Builder mergeFrom(Response.NodeInfo.PeerInfo other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.PeerInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeInfo.PeerInfo.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.NodeInfo.PeerInfo.Builder>`

      Throws:
      :   `java.io.IOException`
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
    - #### setLastSyncBlock

      ```
      public Response.NodeInfo.PeerInfo.Builder setLastSyncBlock(java.lang.String value)
      ```

      `string lastSyncBlock = 1;`

      Parameters:
      :   `value` - The lastSyncBlock to set.

      Returns:
      :   This builder for chaining.
    - #### clearLastSyncBlock

      ```
      public Response.NodeInfo.PeerInfo.Builder clearLastSyncBlock()
      ```

      `string lastSyncBlock = 1;`

      Returns:
      :   This builder for chaining.
    - #### setLastSyncBlockBytes

      ```
      public Response.NodeInfo.PeerInfo.Builder setLastSyncBlockBytes(com.google.protobuf.ByteString value)
      ```

      `string lastSyncBlock = 1;`

      Parameters:
      :   `value` - The bytes for lastSyncBlock to set.

      Returns:
      :   This builder for chaining.
    - #### getRemainNum

      ```
      public long getRemainNum()
      ```

      `int64 remainNum = 2;`

      Specified by:
      :   `getRemainNum` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The remainNum.
    - #### setRemainNum

      ```
      public Response.NodeInfo.PeerInfo.Builder setRemainNum(long value)
      ```

      `int64 remainNum = 2;`

      Parameters:
      :   `value` - The remainNum to set.

      Returns:
      :   This builder for chaining.
    - #### clearRemainNum

      ```
      public Response.NodeInfo.PeerInfo.Builder clearRemainNum()
      ```

      `int64 remainNum = 2;`

      Returns:
      :   This builder for chaining.
    - #### getLastBlockUpdateTime

      ```
      public long getLastBlockUpdateTime()
      ```

      `int64 lastBlockUpdateTime = 3;`

      Specified by:
      :   `getLastBlockUpdateTime` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The lastBlockUpdateTime.
    - #### setLastBlockUpdateTime

      ```
      public Response.NodeInfo.PeerInfo.Builder setLastBlockUpdateTime(long value)
      ```

      `int64 lastBlockUpdateTime = 3;`

      Parameters:
      :   `value` - The lastBlockUpdateTime to set.

      Returns:
      :   This builder for chaining.
    - #### clearLastBlockUpdateTime

      ```
      public Response.NodeInfo.PeerInfo.Builder clearLastBlockUpdateTime()
      ```

      `int64 lastBlockUpdateTime = 3;`

      Returns:
      :   This builder for chaining.
    - #### getSyncFlag

      ```
      public boolean getSyncFlag()
      ```

      `bool syncFlag = 4;`

      Specified by:
      :   `getSyncFlag` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The syncFlag.
    - #### setSyncFlag

      ```
      public Response.NodeInfo.PeerInfo.Builder setSyncFlag(boolean value)
      ```

      `bool syncFlag = 4;`

      Parameters:
      :   `value` - The syncFlag to set.

      Returns:
      :   This builder for chaining.
    - #### clearSyncFlag

      ```
      public Response.NodeInfo.PeerInfo.Builder clearSyncFlag()
      ```

      `bool syncFlag = 4;`

      Returns:
      :   This builder for chaining.
    - #### getHeadBlockTimeWeBothHave

      ```
      public long getHeadBlockTimeWeBothHave()
      ```

      `int64 headBlockTimeWeBothHave = 5;`

      Specified by:
      :   `getHeadBlockTimeWeBothHave` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The headBlockTimeWeBothHave.
    - #### setHeadBlockTimeWeBothHave

      ```
      public Response.NodeInfo.PeerInfo.Builder setHeadBlockTimeWeBothHave(long value)
      ```

      `int64 headBlockTimeWeBothHave = 5;`

      Parameters:
      :   `value` - The headBlockTimeWeBothHave to set.

      Returns:
      :   This builder for chaining.
    - #### clearHeadBlockTimeWeBothHave

      ```
      public Response.NodeInfo.PeerInfo.Builder clearHeadBlockTimeWeBothHave()
      ```

      `int64 headBlockTimeWeBothHave = 5;`

      Returns:
      :   This builder for chaining.
    - #### getNeedSyncFromPeer

      ```
      public boolean getNeedSyncFromPeer()
      ```

      `bool needSyncFromPeer = 6;`

      Specified by:
      :   `getNeedSyncFromPeer` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The needSyncFromPeer.
    - #### setNeedSyncFromPeer

      ```
      public Response.NodeInfo.PeerInfo.Builder setNeedSyncFromPeer(boolean value)
      ```

      `bool needSyncFromPeer = 6;`

      Parameters:
      :   `value` - The needSyncFromPeer to set.

      Returns:
      :   This builder for chaining.
    - #### clearNeedSyncFromPeer

      ```
      public Response.NodeInfo.PeerInfo.Builder clearNeedSyncFromPeer()
      ```

      `bool needSyncFromPeer = 6;`

      Returns:
      :   This builder for chaining.
    - #### getNeedSyncFromUs

      ```
      public boolean getNeedSyncFromUs()
      ```

      `bool needSyncFromUs = 7;`

      Specified by:
      :   `getNeedSyncFromUs` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The needSyncFromUs.
    - #### setNeedSyncFromUs

      ```
      public Response.NodeInfo.PeerInfo.Builder setNeedSyncFromUs(boolean value)
      ```

      `bool needSyncFromUs = 7;`

      Parameters:
      :   `value` - The needSyncFromUs to set.

      Returns:
      :   This builder for chaining.
    - #### clearNeedSyncFromUs

      ```
      public Response.NodeInfo.PeerInfo.Builder clearNeedSyncFromUs()
      ```

      `bool needSyncFromUs = 7;`

      Returns:
      :   This builder for chaining.
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
    - #### setHost

      ```
      public Response.NodeInfo.PeerInfo.Builder setHost(java.lang.String value)
      ```

      `string host = 8;`

      Parameters:
      :   `value` - The host to set.

      Returns:
      :   This builder for chaining.
    - #### clearHost

      ```
      public Response.NodeInfo.PeerInfo.Builder clearHost()
      ```

      `string host = 8;`

      Returns:
      :   This builder for chaining.
    - #### setHostBytes

      ```
      public Response.NodeInfo.PeerInfo.Builder setHostBytes(com.google.protobuf.ByteString value)
      ```

      `string host = 8;`

      Parameters:
      :   `value` - The bytes for host to set.

      Returns:
      :   This builder for chaining.
    - #### getPort

      ```
      public int getPort()
      ```

      `int32 port = 9;`

      Specified by:
      :   `getPort` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The port.
    - #### setPort

      ```
      public Response.NodeInfo.PeerInfo.Builder setPort(int value)
      ```

      `int32 port = 9;`

      Parameters:
      :   `value` - The port to set.

      Returns:
      :   This builder for chaining.
    - #### clearPort

      ```
      public Response.NodeInfo.PeerInfo.Builder clearPort()
      ```

      `int32 port = 9;`

      Returns:
      :   This builder for chaining.
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
    - #### setNodeId

      ```
      public Response.NodeInfo.PeerInfo.Builder setNodeId(java.lang.String value)
      ```

      `string nodeId = 10;`

      Parameters:
      :   `value` - The nodeId to set.

      Returns:
      :   This builder for chaining.
    - #### clearNodeId

      ```
      public Response.NodeInfo.PeerInfo.Builder clearNodeId()
      ```

      `string nodeId = 10;`

      Returns:
      :   This builder for chaining.
    - #### setNodeIdBytes

      ```
      public Response.NodeInfo.PeerInfo.Builder setNodeIdBytes(com.google.protobuf.ByteString value)
      ```

      `string nodeId = 10;`

      Parameters:
      :   `value` - The bytes for nodeId to set.

      Returns:
      :   This builder for chaining.
    - #### getConnectTime

      ```
      public long getConnectTime()
      ```

      `int64 connectTime = 11;`

      Specified by:
      :   `getConnectTime` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The connectTime.
    - #### setConnectTime

      ```
      public Response.NodeInfo.PeerInfo.Builder setConnectTime(long value)
      ```

      `int64 connectTime = 11;`

      Parameters:
      :   `value` - The connectTime to set.

      Returns:
      :   This builder for chaining.
    - #### clearConnectTime

      ```
      public Response.NodeInfo.PeerInfo.Builder clearConnectTime()
      ```

      `int64 connectTime = 11;`

      Returns:
      :   This builder for chaining.
    - #### getAvgLatency

      ```
      public double getAvgLatency()
      ```

      `double avgLatency = 12;`

      Specified by:
      :   `getAvgLatency` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The avgLatency.
    - #### setAvgLatency

      ```
      public Response.NodeInfo.PeerInfo.Builder setAvgLatency(double value)
      ```

      `double avgLatency = 12;`

      Parameters:
      :   `value` - The avgLatency to set.

      Returns:
      :   This builder for chaining.
    - #### clearAvgLatency

      ```
      public Response.NodeInfo.PeerInfo.Builder clearAvgLatency()
      ```

      `double avgLatency = 12;`

      Returns:
      :   This builder for chaining.
    - #### getSyncToFetchSize

      ```
      public int getSyncToFetchSize()
      ```

      `int32 syncToFetchSize = 13;`

      Specified by:
      :   `getSyncToFetchSize` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The syncToFetchSize.
    - #### setSyncToFetchSize

      ```
      public Response.NodeInfo.PeerInfo.Builder setSyncToFetchSize(int value)
      ```

      `int32 syncToFetchSize = 13;`

      Parameters:
      :   `value` - The syncToFetchSize to set.

      Returns:
      :   This builder for chaining.
    - #### clearSyncToFetchSize

      ```
      public Response.NodeInfo.PeerInfo.Builder clearSyncToFetchSize()
      ```

      `int32 syncToFetchSize = 13;`

      Returns:
      :   This builder for chaining.
    - #### getSyncToFetchSizePeekNum

      ```
      public long getSyncToFetchSizePeekNum()
      ```

      `int64 syncToFetchSizePeekNum = 14;`

      Specified by:
      :   `getSyncToFetchSizePeekNum` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The syncToFetchSizePeekNum.
    - #### setSyncToFetchSizePeekNum

      ```
      public Response.NodeInfo.PeerInfo.Builder setSyncToFetchSizePeekNum(long value)
      ```

      `int64 syncToFetchSizePeekNum = 14;`

      Parameters:
      :   `value` - The syncToFetchSizePeekNum to set.

      Returns:
      :   This builder for chaining.
    - #### clearSyncToFetchSizePeekNum

      ```
      public Response.NodeInfo.PeerInfo.Builder clearSyncToFetchSizePeekNum()
      ```

      `int64 syncToFetchSizePeekNum = 14;`

      Returns:
      :   This builder for chaining.
    - #### getSyncBlockRequestedSize

      ```
      public int getSyncBlockRequestedSize()
      ```

      `int32 syncBlockRequestedSize = 15;`

      Specified by:
      :   `getSyncBlockRequestedSize` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The syncBlockRequestedSize.
    - #### setSyncBlockRequestedSize

      ```
      public Response.NodeInfo.PeerInfo.Builder setSyncBlockRequestedSize(int value)
      ```

      `int32 syncBlockRequestedSize = 15;`

      Parameters:
      :   `value` - The syncBlockRequestedSize to set.

      Returns:
      :   This builder for chaining.
    - #### clearSyncBlockRequestedSize

      ```
      public Response.NodeInfo.PeerInfo.Builder clearSyncBlockRequestedSize()
      ```

      `int32 syncBlockRequestedSize = 15;`

      Returns:
      :   This builder for chaining.
    - #### getUnFetchSynNum

      ```
      public long getUnFetchSynNum()
      ```

      `int64 unFetchSynNum = 16;`

      Specified by:
      :   `getUnFetchSynNum` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The unFetchSynNum.
    - #### setUnFetchSynNum

      ```
      public Response.NodeInfo.PeerInfo.Builder setUnFetchSynNum(long value)
      ```

      `int64 unFetchSynNum = 16;`

      Parameters:
      :   `value` - The unFetchSynNum to set.

      Returns:
      :   This builder for chaining.
    - #### clearUnFetchSynNum

      ```
      public Response.NodeInfo.PeerInfo.Builder clearUnFetchSynNum()
      ```

      `int64 unFetchSynNum = 16;`

      Returns:
      :   This builder for chaining.
    - #### getBlockInPorcSize

      ```
      public int getBlockInPorcSize()
      ```

      `int32 blockInPorcSize = 17;`

      Specified by:
      :   `getBlockInPorcSize` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The blockInPorcSize.
    - #### setBlockInPorcSize

      ```
      public Response.NodeInfo.PeerInfo.Builder setBlockInPorcSize(int value)
      ```

      `int32 blockInPorcSize = 17;`

      Parameters:
      :   `value` - The blockInPorcSize to set.

      Returns:
      :   This builder for chaining.
    - #### clearBlockInPorcSize

      ```
      public Response.NodeInfo.PeerInfo.Builder clearBlockInPorcSize()
      ```

      `int32 blockInPorcSize = 17;`

      Returns:
      :   This builder for chaining.
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
    - #### setHeadBlockWeBothHave

      ```
      public Response.NodeInfo.PeerInfo.Builder setHeadBlockWeBothHave(java.lang.String value)
      ```

      `string headBlockWeBothHave = 18;`

      Parameters:
      :   `value` - The headBlockWeBothHave to set.

      Returns:
      :   This builder for chaining.
    - #### clearHeadBlockWeBothHave

      ```
      public Response.NodeInfo.PeerInfo.Builder clearHeadBlockWeBothHave()
      ```

      `string headBlockWeBothHave = 18;`

      Returns:
      :   This builder for chaining.
    - #### setHeadBlockWeBothHaveBytes

      ```
      public Response.NodeInfo.PeerInfo.Builder setHeadBlockWeBothHaveBytes(com.google.protobuf.ByteString value)
      ```

      `string headBlockWeBothHave = 18;`

      Parameters:
      :   `value` - The bytes for headBlockWeBothHave to set.

      Returns:
      :   This builder for chaining.
    - #### getIsActive

      ```
      public boolean getIsActive()
      ```

      `bool isActive = 19;`

      Specified by:
      :   `getIsActive` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The isActive.
    - #### setIsActive

      ```
      public Response.NodeInfo.PeerInfo.Builder setIsActive(boolean value)
      ```

      `bool isActive = 19;`

      Parameters:
      :   `value` - The isActive to set.

      Returns:
      :   This builder for chaining.
    - #### clearIsActive

      ```
      public Response.NodeInfo.PeerInfo.Builder clearIsActive()
      ```

      `bool isActive = 19;`

      Returns:
      :   This builder for chaining.
    - #### getScore

      ```
      public int getScore()
      ```

      `int32 score = 20;`

      Specified by:
      :   `getScore` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The score.
    - #### setScore

      ```
      public Response.NodeInfo.PeerInfo.Builder setScore(int value)
      ```

      `int32 score = 20;`

      Parameters:
      :   `value` - The score to set.

      Returns:
      :   This builder for chaining.
    - #### clearScore

      ```
      public Response.NodeInfo.PeerInfo.Builder clearScore()
      ```

      `int32 score = 20;`

      Returns:
      :   This builder for chaining.
    - #### getNodeCount

      ```
      public int getNodeCount()
      ```

      `int32 nodeCount = 21;`

      Specified by:
      :   `getNodeCount` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The nodeCount.
    - #### setNodeCount

      ```
      public Response.NodeInfo.PeerInfo.Builder setNodeCount(int value)
      ```

      `int32 nodeCount = 21;`

      Parameters:
      :   `value` - The nodeCount to set.

      Returns:
      :   This builder for chaining.
    - #### clearNodeCount

      ```
      public Response.NodeInfo.PeerInfo.Builder clearNodeCount()
      ```

      `int32 nodeCount = 21;`

      Returns:
      :   This builder for chaining.
    - #### getInFlow

      ```
      public long getInFlow()
      ```

      `int64 inFlow = 22;`

      Specified by:
      :   `getInFlow` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The inFlow.
    - #### setInFlow

      ```
      public Response.NodeInfo.PeerInfo.Builder setInFlow(long value)
      ```

      `int64 inFlow = 22;`

      Parameters:
      :   `value` - The inFlow to set.

      Returns:
      :   This builder for chaining.
    - #### clearInFlow

      ```
      public Response.NodeInfo.PeerInfo.Builder clearInFlow()
      ```

      `int64 inFlow = 22;`

      Returns:
      :   This builder for chaining.
    - #### getDisconnectTimes

      ```
      public int getDisconnectTimes()
      ```

      `int32 disconnectTimes = 23;`

      Specified by:
      :   `getDisconnectTimes` in interface `Response.NodeInfo.PeerInfoOrBuilder`

      Returns:
      :   The disconnectTimes.
    - #### setDisconnectTimes

      ```
      public Response.NodeInfo.PeerInfo.Builder setDisconnectTimes(int value)
      ```

      `int32 disconnectTimes = 23;`

      Parameters:
      :   `value` - The disconnectTimes to set.

      Returns:
      :   This builder for chaining.
    - #### clearDisconnectTimes

      ```
      public Response.NodeInfo.PeerInfo.Builder clearDisconnectTimes()
      ```

      `int32 disconnectTimes = 23;`

      Returns:
      :   This builder for chaining.
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
    - #### setLocalDisconnectReason

      ```
      public Response.NodeInfo.PeerInfo.Builder setLocalDisconnectReason(java.lang.String value)
      ```

      `string localDisconnectReason = 24;`

      Parameters:
      :   `value` - The localDisconnectReason to set.

      Returns:
      :   This builder for chaining.
    - #### clearLocalDisconnectReason

      ```
      public Response.NodeInfo.PeerInfo.Builder clearLocalDisconnectReason()
      ```

      `string localDisconnectReason = 24;`

      Returns:
      :   This builder for chaining.
    - #### setLocalDisconnectReasonBytes

      ```
      public Response.NodeInfo.PeerInfo.Builder setLocalDisconnectReasonBytes(com.google.protobuf.ByteString value)
      ```

      `string localDisconnectReason = 24;`

      Parameters:
      :   `value` - The bytes for localDisconnectReason to set.

      Returns:
      :   This builder for chaining.
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
    - #### setRemoteDisconnectReason

      ```
      public Response.NodeInfo.PeerInfo.Builder setRemoteDisconnectReason(java.lang.String value)
      ```

      `string remoteDisconnectReason = 25;`

      Parameters:
      :   `value` - The remoteDisconnectReason to set.

      Returns:
      :   This builder for chaining.
    - #### clearRemoteDisconnectReason

      ```
      public Response.NodeInfo.PeerInfo.Builder clearRemoteDisconnectReason()
      ```

      `string remoteDisconnectReason = 25;`

      Returns:
      :   This builder for chaining.
    - #### setRemoteDisconnectReasonBytes

      ```
      public Response.NodeInfo.PeerInfo.Builder setRemoteDisconnectReasonBytes(com.google.protobuf.ByteString value)
      ```

      `string remoteDisconnectReason = 25;`

      Parameters:
      :   `value` - The bytes for remoteDisconnectReason to set.

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.NodeInfo.PeerInfo.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.PeerInfo.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.NodeInfo.PeerInfo.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.PeerInfo.Builder>`