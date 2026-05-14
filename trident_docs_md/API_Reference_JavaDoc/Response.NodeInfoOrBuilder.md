

org.tron.trident.proto

## Interface Response.NodeInfoOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.NodeInfo](../../../../org/tron/trident/proto/Response.NodeInfo.html "class in org.tron.trident.proto"), [Response.NodeInfo.Builder](../../../../org/tron/trident/proto/Response.NodeInfo.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.NodeInfoOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `boolean` | `containsCheatWitnessInfoMap(java.lang.String key)` `map<string, string> cheatWitnessInfoMap = 11;` |
    | `int` | `getActiveConnectCount()` `int32 activeConnectCount = 5;` |
    | `long` | `getBeginSyncNum()` `int64 beginSyncNum = 1;` |
    | `java.lang.String` | `getBlock()` `string block = 2;` |
    | `com.google.protobuf.ByteString` | `getBlockBytes()` `string block = 2;` |
    | `java.util.Map<java.lang.String,java.lang.String>` | `getCheatWitnessInfoMap()` Deprecated. |
    | `int` | `getCheatWitnessInfoMapCount()` `map<string, string> cheatWitnessInfoMap = 11;` |
    | `java.util.Map<java.lang.String,java.lang.String>` | `getCheatWitnessInfoMapMap()` `map<string, string> cheatWitnessInfoMap = 11;` |
    | `java.lang.String` | `getCheatWitnessInfoMapOrDefault(java.lang.String key, java.lang.String defaultValue)` `map<string, string> cheatWitnessInfoMap = 11;` |
    | `java.lang.String` | `getCheatWitnessInfoMapOrThrow(java.lang.String key)` `map<string, string> cheatWitnessInfoMap = 11;` |
    | `Response.NodeInfo.ConfigNodeInfo` | `getConfigNodeInfo()` `.protocol.NodeInfo.ConfigNodeInfo configNodeInfo = 9;` |
    | `Response.NodeInfo.ConfigNodeInfoOrBuilder` | `getConfigNodeInfoOrBuilder()` `.protocol.NodeInfo.ConfigNodeInfo configNodeInfo = 9;` |
    | `int` | `getCurrentConnectCount()` connect information |
    | `Response.NodeInfo.MachineInfo` | `getMachineInfo()` `.protocol.NodeInfo.MachineInfo machineInfo = 10;` |
    | `Response.NodeInfo.MachineInfoOrBuilder` | `getMachineInfoOrBuilder()` `.protocol.NodeInfo.MachineInfo machineInfo = 10;` |
    | `int` | `getPassiveConnectCount()` `int32 passiveConnectCount = 6;` |
    | `Response.NodeInfo.PeerInfo` | `getPeerInfoList(int index)` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `int` | `getPeerInfoListCount()` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `java.util.List<Response.NodeInfo.PeerInfo>` | `getPeerInfoListList()` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `Response.NodeInfo.PeerInfoOrBuilder` | `getPeerInfoListOrBuilder(int index)` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `java.util.List<? extends Response.NodeInfo.PeerInfoOrBuilder>` | `getPeerInfoListOrBuilderList()` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `java.lang.String` | `getSolidityBlock()` `string solidityBlock = 3;` |
    | `com.google.protobuf.ByteString` | `getSolidityBlockBytes()` `string solidityBlock = 3;` |
    | `long` | `getTotalFlow()` `int64 totalFlow = 7;` |
    | `boolean` | `hasConfigNodeInfo()` `.protocol.NodeInfo.ConfigNodeInfo configNodeInfo = 9;` |
    | `boolean` | `hasMachineInfo()` `.protocol.NodeInfo.MachineInfo machineInfo = 10;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getBeginSyncNum

      ```
      long getBeginSyncNum()
      ```

      `int64 beginSyncNum = 1;`

      Returns:
      :   The beginSyncNum.
    - #### getBlock

      ```
      java.lang.String getBlock()
      ```

      `string block = 2;`

      Returns:
      :   The block.
    - #### getBlockBytes

      ```
      com.google.protobuf.ByteString getBlockBytes()
      ```

      `string block = 2;`

      Returns:
      :   The bytes for block.
    - #### getSolidityBlock

      ```
      java.lang.String getSolidityBlock()
      ```

      `string solidityBlock = 3;`

      Returns:
      :   The solidityBlock.
    - #### getSolidityBlockBytes

      ```
      com.google.protobuf.ByteString getSolidityBlockBytes()
      ```

      `string solidityBlock = 3;`

      Returns:
      :   The bytes for solidityBlock.
    - #### getCurrentConnectCount

      ```
      int getCurrentConnectCount()
      ```

      ```
       connect information
      ```

      `int32 currentConnectCount = 4;`

      Returns:
      :   The currentConnectCount.
    - #### getActiveConnectCount

      ```
      int getActiveConnectCount()
      ```

      `int32 activeConnectCount = 5;`

      Returns:
      :   The activeConnectCount.
    - #### getPassiveConnectCount

      ```
      int getPassiveConnectCount()
      ```

      `int32 passiveConnectCount = 6;`

      Returns:
      :   The passiveConnectCount.
    - #### getTotalFlow

      ```
      long getTotalFlow()
      ```

      `int64 totalFlow = 7;`

      Returns:
      :   The totalFlow.
    - #### getPeerInfoListList

      ```
      java.util.List<Response.NodeInfo.PeerInfo> getPeerInfoListList()
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`
    - #### getPeerInfoList

      ```
      Response.NodeInfo.PeerInfo getPeerInfoList(int index)
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`
    - #### getPeerInfoListCount

      ```
      int getPeerInfoListCount()
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`
    - #### getPeerInfoListOrBuilderList

      ```
      java.util.List<? extends Response.NodeInfo.PeerInfoOrBuilder> getPeerInfoListOrBuilderList()
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`
    - #### getPeerInfoListOrBuilder

      ```
      Response.NodeInfo.PeerInfoOrBuilder getPeerInfoListOrBuilder(int index)
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`
    - #### hasConfigNodeInfo

      ```
      boolean hasConfigNodeInfo()
      ```

      `.protocol.NodeInfo.ConfigNodeInfo configNodeInfo = 9;`

      Returns:
      :   Whether the configNodeInfo field is set.
    - #### getConfigNodeInfo

      ```
      Response.NodeInfo.ConfigNodeInfo getConfigNodeInfo()
      ```

      `.protocol.NodeInfo.ConfigNodeInfo configNodeInfo = 9;`

      Returns:
      :   The configNodeInfo.
    - #### getConfigNodeInfoOrBuilder

      ```
      Response.NodeInfo.ConfigNodeInfoOrBuilder getConfigNodeInfoOrBuilder()
      ```

      `.protocol.NodeInfo.ConfigNodeInfo configNodeInfo = 9;`
    - #### hasMachineInfo

      ```
      boolean hasMachineInfo()
      ```

      `.protocol.NodeInfo.MachineInfo machineInfo = 10;`

      Returns:
      :   Whether the machineInfo field is set.
    - #### getMachineInfo

      ```
      Response.NodeInfo.MachineInfo getMachineInfo()
      ```

      `.protocol.NodeInfo.MachineInfo machineInfo = 10;`

      Returns:
      :   The machineInfo.
    - #### getMachineInfoOrBuilder

      ```
      Response.NodeInfo.MachineInfoOrBuilder getMachineInfoOrBuilder()
      ```

      `.protocol.NodeInfo.MachineInfo machineInfo = 10;`
    - #### getCheatWitnessInfoMapCount

      ```
      int getCheatWitnessInfoMapCount()
      ```

      `map<string, string> cheatWitnessInfoMap = 11;`
    - #### containsCheatWitnessInfoMap

      ```
      boolean containsCheatWitnessInfoMap(java.lang.String key)
      ```

      `map<string, string> cheatWitnessInfoMap = 11;`
    - #### getCheatWitnessInfoMap

      ```
      @Deprecated
      java.util.Map<java.lang.String,java.lang.String> getCheatWitnessInfoMap()
      ```

      Deprecated.

      Use [`getCheatWitnessInfoMapMap()`](../../../../org/tron/trident/proto/Response.NodeInfoOrBuilder.html#getCheatWitnessInfoMapMap--) instead.
    - #### getCheatWitnessInfoMapMap

      ```
      java.util.Map<java.lang.String,java.lang.String> getCheatWitnessInfoMapMap()
      ```

      `map<string, string> cheatWitnessInfoMap = 11;`
    - #### getCheatWitnessInfoMapOrDefault

      ```
      java.lang.String getCheatWitnessInfoMapOrDefault(java.lang.String key,
                                                       java.lang.String defaultValue)
      ```

      `map<string, string> cheatWitnessInfoMap = 11;`
    - #### getCheatWitnessInfoMapOrThrow

      ```
      java.lang.String getCheatWitnessInfoMapOrThrow(java.lang.String key)
      ```

      `map<string, string> cheatWitnessInfoMap = 11;`