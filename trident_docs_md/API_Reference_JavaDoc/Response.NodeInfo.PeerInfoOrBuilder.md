

org.tron.trident.proto

## Interface Response.NodeInfo.PeerInfoOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.NodeInfo.PeerInfo](../../../../org/tron/trident/proto/Response.NodeInfo.PeerInfo.html "class in org.tron.trident.proto"), [Response.NodeInfo.PeerInfo.Builder](../../../../org/tron/trident/proto/Response.NodeInfo.PeerInfo.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response.NodeInfo](../../../../org/tron/trident/proto/Response.NodeInfo.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.NodeInfo.PeerInfoOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `double` | `getAvgLatency()` `double avgLatency = 12;` |
    | `int` | `getBlockInPorcSize()` `int32 blockInPorcSize = 17;` |
    | `long` | `getConnectTime()` `int64 connectTime = 11;` |
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

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getLastSyncBlock

      ```
      java.lang.String getLastSyncBlock()
      ```

      `string lastSyncBlock = 1;`

      Returns:
      :   The lastSyncBlock.
    - #### getLastSyncBlockBytes

      ```
      com.google.protobuf.ByteString getLastSyncBlockBytes()
      ```

      `string lastSyncBlock = 1;`

      Returns:
      :   The bytes for lastSyncBlock.
    - #### getRemainNum

      ```
      long getRemainNum()
      ```

      `int64 remainNum = 2;`

      Returns:
      :   The remainNum.
    - #### getLastBlockUpdateTime

      ```
      long getLastBlockUpdateTime()
      ```

      `int64 lastBlockUpdateTime = 3;`

      Returns:
      :   The lastBlockUpdateTime.
    - #### getSyncFlag

      ```
      boolean getSyncFlag()
      ```

      `bool syncFlag = 4;`

      Returns:
      :   The syncFlag.
    - #### getHeadBlockTimeWeBothHave

      ```
      long getHeadBlockTimeWeBothHave()
      ```

      `int64 headBlockTimeWeBothHave = 5;`

      Returns:
      :   The headBlockTimeWeBothHave.
    - #### getNeedSyncFromPeer

      ```
      boolean getNeedSyncFromPeer()
      ```

      `bool needSyncFromPeer = 6;`

      Returns:
      :   The needSyncFromPeer.
    - #### getNeedSyncFromUs

      ```
      boolean getNeedSyncFromUs()
      ```

      `bool needSyncFromUs = 7;`

      Returns:
      :   The needSyncFromUs.
    - #### getHost

      ```
      java.lang.String getHost()
      ```

      `string host = 8;`

      Returns:
      :   The host.
    - #### getHostBytes

      ```
      com.google.protobuf.ByteString getHostBytes()
      ```

      `string host = 8;`

      Returns:
      :   The bytes for host.
    - #### getPort

      ```
      int getPort()
      ```

      `int32 port = 9;`

      Returns:
      :   The port.
    - #### getNodeId

      ```
      java.lang.String getNodeId()
      ```

      `string nodeId = 10;`

      Returns:
      :   The nodeId.
    - #### getNodeIdBytes

      ```
      com.google.protobuf.ByteString getNodeIdBytes()
      ```

      `string nodeId = 10;`

      Returns:
      :   The bytes for nodeId.
    - #### getConnectTime

      ```
      long getConnectTime()
      ```

      `int64 connectTime = 11;`

      Returns:
      :   The connectTime.
    - #### getAvgLatency

      ```
      double getAvgLatency()
      ```

      `double avgLatency = 12;`

      Returns:
      :   The avgLatency.
    - #### getSyncToFetchSize

      ```
      int getSyncToFetchSize()
      ```

      `int32 syncToFetchSize = 13;`

      Returns:
      :   The syncToFetchSize.
    - #### getSyncToFetchSizePeekNum

      ```
      long getSyncToFetchSizePeekNum()
      ```

      `int64 syncToFetchSizePeekNum = 14;`

      Returns:
      :   The syncToFetchSizePeekNum.
    - #### getSyncBlockRequestedSize

      ```
      int getSyncBlockRequestedSize()
      ```

      `int32 syncBlockRequestedSize = 15;`

      Returns:
      :   The syncBlockRequestedSize.
    - #### getUnFetchSynNum

      ```
      long getUnFetchSynNum()
      ```

      `int64 unFetchSynNum = 16;`

      Returns:
      :   The unFetchSynNum.
    - #### getBlockInPorcSize

      ```
      int getBlockInPorcSize()
      ```

      `int32 blockInPorcSize = 17;`

      Returns:
      :   The blockInPorcSize.
    - #### getHeadBlockWeBothHave

      ```
      java.lang.String getHeadBlockWeBothHave()
      ```

      `string headBlockWeBothHave = 18;`

      Returns:
      :   The headBlockWeBothHave.
    - #### getHeadBlockWeBothHaveBytes

      ```
      com.google.protobuf.ByteString getHeadBlockWeBothHaveBytes()
      ```

      `string headBlockWeBothHave = 18;`

      Returns:
      :   The bytes for headBlockWeBothHave.
    - #### getIsActive

      ```
      boolean getIsActive()
      ```

      `bool isActive = 19;`

      Returns:
      :   The isActive.
    - #### getScore

      ```
      int getScore()
      ```

      `int32 score = 20;`

      Returns:
      :   The score.
    - #### getNodeCount

      ```
      int getNodeCount()
      ```

      `int32 nodeCount = 21;`

      Returns:
      :   The nodeCount.
    - #### getInFlow

      ```
      long getInFlow()
      ```

      `int64 inFlow = 22;`

      Returns:
      :   The inFlow.
    - #### getDisconnectTimes

      ```
      int getDisconnectTimes()
      ```

      `int32 disconnectTimes = 23;`

      Returns:
      :   The disconnectTimes.
    - #### getLocalDisconnectReason

      ```
      java.lang.String getLocalDisconnectReason()
      ```

      `string localDisconnectReason = 24;`

      Returns:
      :   The localDisconnectReason.
    - #### getLocalDisconnectReasonBytes

      ```
      com.google.protobuf.ByteString getLocalDisconnectReasonBytes()
      ```

      `string localDisconnectReason = 24;`

      Returns:
      :   The bytes for localDisconnectReason.
    - #### getRemoteDisconnectReason

      ```
      java.lang.String getRemoteDisconnectReason()
      ```

      `string remoteDisconnectReason = 25;`

      Returns:
      :   The remoteDisconnectReason.
    - #### getRemoteDisconnectReasonBytes

      ```
      com.google.protobuf.ByteString getRemoteDisconnectReasonBytes()
      ```

      `string remoteDisconnectReason = 25;`

      Returns:
      :   The bytes for remoteDisconnectReason.