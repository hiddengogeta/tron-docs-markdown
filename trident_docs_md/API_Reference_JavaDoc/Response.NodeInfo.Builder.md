

org.tron.trident.proto

## Class Response.NodeInfo.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.NodeInfo.Builder](../../../../org/tron/trident/proto/Response.NodeInfo.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.NodeInfo.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.NodeInfoOrBuilder](../../../../org/tron/trident/proto/Response.NodeInfoOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.NodeInfo](../../../../org/tron/trident/proto/Response.NodeInfo.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.NodeInfo.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.Builder>
  implements Response.NodeInfoOrBuilder
  ```

  Protobuf type `protocol.NodeInfo`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `Response.NodeInfo.Builder` | `addAllPeerInfoList(java.lang.Iterable<? extends Response.NodeInfo.PeerInfo> values)` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `Response.NodeInfo.Builder` | `addPeerInfoList(int index, Response.NodeInfo.PeerInfo.Builder builderForValue)` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `Response.NodeInfo.Builder` | `addPeerInfoList(int index, Response.NodeInfo.PeerInfo value)` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `Response.NodeInfo.Builder` | `addPeerInfoList(Response.NodeInfo.PeerInfo.Builder builderForValue)` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `Response.NodeInfo.Builder` | `addPeerInfoList(Response.NodeInfo.PeerInfo value)` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `addPeerInfoListBuilder()` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `addPeerInfoListBuilder(int index)` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `Response.NodeInfo.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.NodeInfo` | `build()` |
    | `Response.NodeInfo` | `buildPartial()` |
    | `Response.NodeInfo.Builder` | `clear()` |
    | `Response.NodeInfo.Builder` | `clearActiveConnectCount()` `int32 activeConnectCount = 5;` |
    | `Response.NodeInfo.Builder` | `clearBeginSyncNum()` `int64 beginSyncNum = 1;` |
    | `Response.NodeInfo.Builder` | `clearBlock()` `string block = 2;` |
    | `Response.NodeInfo.Builder` | `clearCheatWitnessInfoMap()` |
    | `Response.NodeInfo.Builder` | `clearConfigNodeInfo()` `.protocol.NodeInfo.ConfigNodeInfo configNodeInfo = 9;` |
    | `Response.NodeInfo.Builder` | `clearCurrentConnectCount()` connect information |
    | `Response.NodeInfo.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.NodeInfo.Builder` | `clearMachineInfo()` `.protocol.NodeInfo.MachineInfo machineInfo = 10;` |
    | `Response.NodeInfo.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.NodeInfo.Builder` | `clearPassiveConnectCount()` `int32 passiveConnectCount = 6;` |
    | `Response.NodeInfo.Builder` | `clearPeerInfoList()` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `Response.NodeInfo.Builder` | `clearSolidityBlock()` `string solidityBlock = 3;` |
    | `Response.NodeInfo.Builder` | `clearTotalFlow()` `int64 totalFlow = 7;` |
    | `Response.NodeInfo.Builder` | `clone()` |
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
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `getConfigNodeInfoBuilder()` `.protocol.NodeInfo.ConfigNodeInfo configNodeInfo = 9;` |
    | `Response.NodeInfo.ConfigNodeInfoOrBuilder` | `getConfigNodeInfoOrBuilder()` `.protocol.NodeInfo.ConfigNodeInfo configNodeInfo = 9;` |
    | `int` | `getCurrentConnectCount()` connect information |
    | `Response.NodeInfo` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Response.NodeInfo.MachineInfo` | `getMachineInfo()` `.protocol.NodeInfo.MachineInfo machineInfo = 10;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `getMachineInfoBuilder()` `.protocol.NodeInfo.MachineInfo machineInfo = 10;` |
    | `Response.NodeInfo.MachineInfoOrBuilder` | `getMachineInfoOrBuilder()` `.protocol.NodeInfo.MachineInfo machineInfo = 10;` |
    | `java.util.Map<java.lang.String,java.lang.String>` | `getMutableCheatWitnessInfoMap()` Deprecated. |
    | `int` | `getPassiveConnectCount()` `int32 passiveConnectCount = 6;` |
    | `Response.NodeInfo.PeerInfo` | `getPeerInfoList(int index)` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `Response.NodeInfo.PeerInfo.Builder` | `getPeerInfoListBuilder(int index)` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `java.util.List<Response.NodeInfo.PeerInfo.Builder>` | `getPeerInfoListBuilderList()` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `int` | `getPeerInfoListCount()` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `java.util.List<Response.NodeInfo.PeerInfo>` | `getPeerInfoListList()` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `Response.NodeInfo.PeerInfoOrBuilder` | `getPeerInfoListOrBuilder(int index)` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `java.util.List<? extends Response.NodeInfo.PeerInfoOrBuilder>` | `getPeerInfoListOrBuilderList()` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `java.lang.String` | `getSolidityBlock()` `string solidityBlock = 3;` |
    | `com.google.protobuf.ByteString` | `getSolidityBlockBytes()` `string solidityBlock = 3;` |
    | `long` | `getTotalFlow()` `int64 totalFlow = 7;` |
    | `boolean` | `hasConfigNodeInfo()` `.protocol.NodeInfo.ConfigNodeInfo configNodeInfo = 9;` |
    | `boolean` | `hasMachineInfo()` `.protocol.NodeInfo.MachineInfo machineInfo = 10;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMapFieldReflection(int number)` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMutableMapFieldReflection(int number)` |
    | `boolean` | `isInitialized()` |
    | `Response.NodeInfo.Builder` | `mergeConfigNodeInfo(Response.NodeInfo.ConfigNodeInfo value)` `.protocol.NodeInfo.ConfigNodeInfo configNodeInfo = 9;` |
    | `Response.NodeInfo.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.NodeInfo.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.NodeInfo.Builder` | `mergeFrom(Response.NodeInfo other)` |
    | `Response.NodeInfo.Builder` | `mergeMachineInfo(Response.NodeInfo.MachineInfo value)` `.protocol.NodeInfo.MachineInfo machineInfo = 10;` |
    | `Response.NodeInfo.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.NodeInfo.Builder` | `putAllCheatWitnessInfoMap(java.util.Map<java.lang.String,java.lang.String> values)` `map<string, string> cheatWitnessInfoMap = 11;` |
    | `Response.NodeInfo.Builder` | `putCheatWitnessInfoMap(java.lang.String key, java.lang.String value)` `map<string, string> cheatWitnessInfoMap = 11;` |
    | `Response.NodeInfo.Builder` | `removeCheatWitnessInfoMap(java.lang.String key)` `map<string, string> cheatWitnessInfoMap = 11;` |
    | `Response.NodeInfo.Builder` | `removePeerInfoList(int index)` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `Response.NodeInfo.Builder` | `setActiveConnectCount(int value)` `int32 activeConnectCount = 5;` |
    | `Response.NodeInfo.Builder` | `setBeginSyncNum(long value)` `int64 beginSyncNum = 1;` |
    | `Response.NodeInfo.Builder` | `setBlock(java.lang.String value)` `string block = 2;` |
    | `Response.NodeInfo.Builder` | `setBlockBytes(com.google.protobuf.ByteString value)` `string block = 2;` |
    | `Response.NodeInfo.Builder` | `setConfigNodeInfo(Response.NodeInfo.ConfigNodeInfo.Builder builderForValue)` `.protocol.NodeInfo.ConfigNodeInfo configNodeInfo = 9;` |
    | `Response.NodeInfo.Builder` | `setConfigNodeInfo(Response.NodeInfo.ConfigNodeInfo value)` `.protocol.NodeInfo.ConfigNodeInfo configNodeInfo = 9;` |
    | `Response.NodeInfo.Builder` | `setCurrentConnectCount(int value)` connect information |
    | `Response.NodeInfo.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.NodeInfo.Builder` | `setMachineInfo(Response.NodeInfo.MachineInfo.Builder builderForValue)` `.protocol.NodeInfo.MachineInfo machineInfo = 10;` |
    | `Response.NodeInfo.Builder` | `setMachineInfo(Response.NodeInfo.MachineInfo value)` `.protocol.NodeInfo.MachineInfo machineInfo = 10;` |
    | `Response.NodeInfo.Builder` | `setPassiveConnectCount(int value)` `int32 passiveConnectCount = 6;` |
    | `Response.NodeInfo.Builder` | `setPeerInfoList(int index, Response.NodeInfo.PeerInfo.Builder builderForValue)` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `Response.NodeInfo.Builder` | `setPeerInfoList(int index, Response.NodeInfo.PeerInfo value)` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `Response.NodeInfo.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.NodeInfo.Builder` | `setSolidityBlock(java.lang.String value)` `string solidityBlock = 3;` |
    | `Response.NodeInfo.Builder` | `setSolidityBlockBytes(com.google.protobuf.ByteString value)` `string solidityBlock = 3;` |
    | `Response.NodeInfo.Builder` | `setTotalFlow(long value)` `int64 totalFlow = 7;` |
    | `Response.NodeInfo.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetMapFieldReflection` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.Builder>`
    - #### internalGetMutableMapFieldReflection

      ```
      protected com.google.protobuf.MapFieldReflectionAccessor internalGetMutableMapFieldReflection(int number)
      ```

      Overrides:
      :   `internalGetMutableMapFieldReflection` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.Builder>`
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.Builder>`
    - #### clear

      ```
      public Response.NodeInfo.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.NodeInfo getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.NodeInfo build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.NodeInfo buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.NodeInfo.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.Builder>`
    - #### setField

      ```
      public Response.NodeInfo.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.Builder>`
    - #### clearField

      ```
      public Response.NodeInfo.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.Builder>`
    - #### clearOneof

      ```
      public Response.NodeInfo.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.Builder>`
    - #### setRepeatedField

      ```
      public Response.NodeInfo.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                        int index,
                                                        java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.Builder>`
    - #### addRepeatedField

      ```
      public Response.NodeInfo.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                        java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeInfo.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.NodeInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeInfo.Builder mergeFrom(Response.NodeInfo other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeInfo.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                 com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                          throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.NodeInfo.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getBeginSyncNum

      ```
      public long getBeginSyncNum()
      ```

      `int64 beginSyncNum = 1;`

      Specified by:
      :   `getBeginSyncNum` in interface `Response.NodeInfoOrBuilder`

      Returns:
      :   The beginSyncNum.
    - #### setBeginSyncNum

      ```
      public Response.NodeInfo.Builder setBeginSyncNum(long value)
      ```

      `int64 beginSyncNum = 1;`

      Parameters:
      :   `value` - The beginSyncNum to set.

      Returns:
      :   This builder for chaining.
    - #### clearBeginSyncNum

      ```
      public Response.NodeInfo.Builder clearBeginSyncNum()
      ```

      `int64 beginSyncNum = 1;`

      Returns:
      :   This builder for chaining.
    - #### getBlock

      ```
      public java.lang.String getBlock()
      ```

      `string block = 2;`

      Specified by:
      :   `getBlock` in interface `Response.NodeInfoOrBuilder`

      Returns:
      :   The block.
    - #### getBlockBytes

      ```
      public com.google.protobuf.ByteString getBlockBytes()
      ```

      `string block = 2;`

      Specified by:
      :   `getBlockBytes` in interface `Response.NodeInfoOrBuilder`

      Returns:
      :   The bytes for block.
    - #### setBlock

      ```
      public Response.NodeInfo.Builder setBlock(java.lang.String value)
      ```

      `string block = 2;`

      Parameters:
      :   `value` - The block to set.

      Returns:
      :   This builder for chaining.
    - #### clearBlock

      ```
      public Response.NodeInfo.Builder clearBlock()
      ```

      `string block = 2;`

      Returns:
      :   This builder for chaining.
    - #### setBlockBytes

      ```
      public Response.NodeInfo.Builder setBlockBytes(com.google.protobuf.ByteString value)
      ```

      `string block = 2;`

      Parameters:
      :   `value` - The bytes for block to set.

      Returns:
      :   This builder for chaining.
    - #### getSolidityBlock

      ```
      public java.lang.String getSolidityBlock()
      ```

      `string solidityBlock = 3;`

      Specified by:
      :   `getSolidityBlock` in interface `Response.NodeInfoOrBuilder`

      Returns:
      :   The solidityBlock.
    - #### getSolidityBlockBytes

      ```
      public com.google.protobuf.ByteString getSolidityBlockBytes()
      ```

      `string solidityBlock = 3;`

      Specified by:
      :   `getSolidityBlockBytes` in interface `Response.NodeInfoOrBuilder`

      Returns:
      :   The bytes for solidityBlock.
    - #### setSolidityBlock

      ```
      public Response.NodeInfo.Builder setSolidityBlock(java.lang.String value)
      ```

      `string solidityBlock = 3;`

      Parameters:
      :   `value` - The solidityBlock to set.

      Returns:
      :   This builder for chaining.
    - #### clearSolidityBlock

      ```
      public Response.NodeInfo.Builder clearSolidityBlock()
      ```

      `string solidityBlock = 3;`

      Returns:
      :   This builder for chaining.
    - #### setSolidityBlockBytes

      ```
      public Response.NodeInfo.Builder setSolidityBlockBytes(com.google.protobuf.ByteString value)
      ```

      `string solidityBlock = 3;`

      Parameters:
      :   `value` - The bytes for solidityBlock to set.

      Returns:
      :   This builder for chaining.
    - #### getCurrentConnectCount

      ```
      public int getCurrentConnectCount()
      ```

      ```
       connect information
      ```

      `int32 currentConnectCount = 4;`

      Specified by:
      :   `getCurrentConnectCount` in interface `Response.NodeInfoOrBuilder`

      Returns:
      :   The currentConnectCount.
    - #### setCurrentConnectCount

      ```
      public Response.NodeInfo.Builder setCurrentConnectCount(int value)
      ```

      ```
       connect information
      ```

      `int32 currentConnectCount = 4;`

      Parameters:
      :   `value` - The currentConnectCount to set.

      Returns:
      :   This builder for chaining.
    - #### clearCurrentConnectCount

      ```
      public Response.NodeInfo.Builder clearCurrentConnectCount()
      ```

      ```
       connect information
      ```

      `int32 currentConnectCount = 4;`

      Returns:
      :   This builder for chaining.
    - #### getActiveConnectCount

      ```
      public int getActiveConnectCount()
      ```

      `int32 activeConnectCount = 5;`

      Specified by:
      :   `getActiveConnectCount` in interface `Response.NodeInfoOrBuilder`

      Returns:
      :   The activeConnectCount.
    - #### setActiveConnectCount

      ```
      public Response.NodeInfo.Builder setActiveConnectCount(int value)
      ```

      `int32 activeConnectCount = 5;`

      Parameters:
      :   `value` - The activeConnectCount to set.

      Returns:
      :   This builder for chaining.
    - #### clearActiveConnectCount

      ```
      public Response.NodeInfo.Builder clearActiveConnectCount()
      ```

      `int32 activeConnectCount = 5;`

      Returns:
      :   This builder for chaining.
    - #### getPassiveConnectCount

      ```
      public int getPassiveConnectCount()
      ```

      `int32 passiveConnectCount = 6;`

      Specified by:
      :   `getPassiveConnectCount` in interface `Response.NodeInfoOrBuilder`

      Returns:
      :   The passiveConnectCount.
    - #### setPassiveConnectCount

      ```
      public Response.NodeInfo.Builder setPassiveConnectCount(int value)
      ```

      `int32 passiveConnectCount = 6;`

      Parameters:
      :   `value` - The passiveConnectCount to set.

      Returns:
      :   This builder for chaining.
    - #### clearPassiveConnectCount

      ```
      public Response.NodeInfo.Builder clearPassiveConnectCount()
      ```

      `int32 passiveConnectCount = 6;`

      Returns:
      :   This builder for chaining.
    - #### getTotalFlow

      ```
      public long getTotalFlow()
      ```

      `int64 totalFlow = 7;`

      Specified by:
      :   `getTotalFlow` in interface `Response.NodeInfoOrBuilder`

      Returns:
      :   The totalFlow.
    - #### setTotalFlow

      ```
      public Response.NodeInfo.Builder setTotalFlow(long value)
      ```

      `int64 totalFlow = 7;`

      Parameters:
      :   `value` - The totalFlow to set.

      Returns:
      :   This builder for chaining.
    - #### clearTotalFlow

      ```
      public Response.NodeInfo.Builder clearTotalFlow()
      ```

      `int64 totalFlow = 7;`

      Returns:
      :   This builder for chaining.
    - #### getPeerInfoListList

      ```
      public java.util.List<Response.NodeInfo.PeerInfo> getPeerInfoListList()
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`

      Specified by:
      :   `getPeerInfoListList` in interface `Response.NodeInfoOrBuilder`
    - #### getPeerInfoListCount

      ```
      public int getPeerInfoListCount()
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`

      Specified by:
      :   `getPeerInfoListCount` in interface `Response.NodeInfoOrBuilder`
    - #### getPeerInfoList

      ```
      public Response.NodeInfo.PeerInfo getPeerInfoList(int index)
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`

      Specified by:
      :   `getPeerInfoList` in interface `Response.NodeInfoOrBuilder`
    - #### setPeerInfoList

      ```
      public Response.NodeInfo.Builder setPeerInfoList(int index,
                                                       Response.NodeInfo.PeerInfo value)
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`
    - #### setPeerInfoList

      ```
      public Response.NodeInfo.Builder setPeerInfoList(int index,
                                                       Response.NodeInfo.PeerInfo.Builder builderForValue)
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`
    - #### addPeerInfoList

      ```
      public Response.NodeInfo.Builder addPeerInfoList(Response.NodeInfo.PeerInfo value)
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`
    - #### addPeerInfoList

      ```
      public Response.NodeInfo.Builder addPeerInfoList(int index,
                                                       Response.NodeInfo.PeerInfo value)
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`
    - #### addPeerInfoList

      ```
      public Response.NodeInfo.Builder addPeerInfoList(Response.NodeInfo.PeerInfo.Builder builderForValue)
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`
    - #### addPeerInfoList

      ```
      public Response.NodeInfo.Builder addPeerInfoList(int index,
                                                       Response.NodeInfo.PeerInfo.Builder builderForValue)
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`
    - #### addAllPeerInfoList

      ```
      public Response.NodeInfo.Builder addAllPeerInfoList(java.lang.Iterable<? extends Response.NodeInfo.PeerInfo> values)
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`
    - #### clearPeerInfoList

      ```
      public Response.NodeInfo.Builder clearPeerInfoList()
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`
    - #### removePeerInfoList

      ```
      public Response.NodeInfo.Builder removePeerInfoList(int index)
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`
    - #### getPeerInfoListBuilder

      ```
      public Response.NodeInfo.PeerInfo.Builder getPeerInfoListBuilder(int index)
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`
    - #### getPeerInfoListOrBuilder

      ```
      public Response.NodeInfo.PeerInfoOrBuilder getPeerInfoListOrBuilder(int index)
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`

      Specified by:
      :   `getPeerInfoListOrBuilder` in interface `Response.NodeInfoOrBuilder`
    - #### getPeerInfoListOrBuilderList

      ```
      public java.util.List<? extends Response.NodeInfo.PeerInfoOrBuilder> getPeerInfoListOrBuilderList()
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`

      Specified by:
      :   `getPeerInfoListOrBuilderList` in interface `Response.NodeInfoOrBuilder`
    - #### addPeerInfoListBuilder

      ```
      public Response.NodeInfo.PeerInfo.Builder addPeerInfoListBuilder()
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`
    - #### addPeerInfoListBuilder

      ```
      public Response.NodeInfo.PeerInfo.Builder addPeerInfoListBuilder(int index)
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`
    - #### getPeerInfoListBuilderList

      ```
      public java.util.List<Response.NodeInfo.PeerInfo.Builder> getPeerInfoListBuilderList()
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`
    - #### hasConfigNodeInfo

      ```
      public boolean hasConfigNodeInfo()
      ```

      `.protocol.NodeInfo.ConfigNodeInfo configNodeInfo = 9;`

      Specified by:
      :   `hasConfigNodeInfo` in interface `Response.NodeInfoOrBuilder`

      Returns:
      :   Whether the configNodeInfo field is set.
    - #### getConfigNodeInfo

      ```
      public Response.NodeInfo.ConfigNodeInfo getConfigNodeInfo()
      ```

      `.protocol.NodeInfo.ConfigNodeInfo configNodeInfo = 9;`

      Specified by:
      :   `getConfigNodeInfo` in interface `Response.NodeInfoOrBuilder`

      Returns:
      :   The configNodeInfo.
    - #### setConfigNodeInfo

      ```
      public Response.NodeInfo.Builder setConfigNodeInfo(Response.NodeInfo.ConfigNodeInfo value)
      ```

      `.protocol.NodeInfo.ConfigNodeInfo configNodeInfo = 9;`
    - #### setConfigNodeInfo

      ```
      public Response.NodeInfo.Builder setConfigNodeInfo(Response.NodeInfo.ConfigNodeInfo.Builder builderForValue)
      ```

      `.protocol.NodeInfo.ConfigNodeInfo configNodeInfo = 9;`
    - #### mergeConfigNodeInfo

      ```
      public Response.NodeInfo.Builder mergeConfigNodeInfo(Response.NodeInfo.ConfigNodeInfo value)
      ```

      `.protocol.NodeInfo.ConfigNodeInfo configNodeInfo = 9;`
    - #### clearConfigNodeInfo

      ```
      public Response.NodeInfo.Builder clearConfigNodeInfo()
      ```

      `.protocol.NodeInfo.ConfigNodeInfo configNodeInfo = 9;`
    - #### getConfigNodeInfoBuilder

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder getConfigNodeInfoBuilder()
      ```

      `.protocol.NodeInfo.ConfigNodeInfo configNodeInfo = 9;`
    - #### getConfigNodeInfoOrBuilder

      ```
      public Response.NodeInfo.ConfigNodeInfoOrBuilder getConfigNodeInfoOrBuilder()
      ```

      `.protocol.NodeInfo.ConfigNodeInfo configNodeInfo = 9;`

      Specified by:
      :   `getConfigNodeInfoOrBuilder` in interface `Response.NodeInfoOrBuilder`
    - #### hasMachineInfo

      ```
      public boolean hasMachineInfo()
      ```

      `.protocol.NodeInfo.MachineInfo machineInfo = 10;`

      Specified by:
      :   `hasMachineInfo` in interface `Response.NodeInfoOrBuilder`

      Returns:
      :   Whether the machineInfo field is set.
    - #### getMachineInfo

      ```
      public Response.NodeInfo.MachineInfo getMachineInfo()
      ```

      `.protocol.NodeInfo.MachineInfo machineInfo = 10;`

      Specified by:
      :   `getMachineInfo` in interface `Response.NodeInfoOrBuilder`

      Returns:
      :   The machineInfo.
    - #### setMachineInfo

      ```
      public Response.NodeInfo.Builder setMachineInfo(Response.NodeInfo.MachineInfo value)
      ```

      `.protocol.NodeInfo.MachineInfo machineInfo = 10;`
    - #### setMachineInfo

      ```
      public Response.NodeInfo.Builder setMachineInfo(Response.NodeInfo.MachineInfo.Builder builderForValue)
      ```

      `.protocol.NodeInfo.MachineInfo machineInfo = 10;`
    - #### mergeMachineInfo

      ```
      public Response.NodeInfo.Builder mergeMachineInfo(Response.NodeInfo.MachineInfo value)
      ```

      `.protocol.NodeInfo.MachineInfo machineInfo = 10;`
    - #### clearMachineInfo

      ```
      public Response.NodeInfo.Builder clearMachineInfo()
      ```

      `.protocol.NodeInfo.MachineInfo machineInfo = 10;`
    - #### getMachineInfoBuilder

      ```
      public Response.NodeInfo.MachineInfo.Builder getMachineInfoBuilder()
      ```

      `.protocol.NodeInfo.MachineInfo machineInfo = 10;`
    - #### getMachineInfoOrBuilder

      ```
      public Response.NodeInfo.MachineInfoOrBuilder getMachineInfoOrBuilder()
      ```

      `.protocol.NodeInfo.MachineInfo machineInfo = 10;`

      Specified by:
      :   `getMachineInfoOrBuilder` in interface `Response.NodeInfoOrBuilder`
    - #### getCheatWitnessInfoMapCount

      ```
      public int getCheatWitnessInfoMapCount()
      ```

      Description copied from interface: `Response.NodeInfoOrBuilder`

      `map<string, string> cheatWitnessInfoMap = 11;`

      Specified by:
      :   `getCheatWitnessInfoMapCount` in interface `Response.NodeInfoOrBuilder`
    - #### containsCheatWitnessInfoMap

      ```
      public boolean containsCheatWitnessInfoMap(java.lang.String key)
      ```

      `map<string, string> cheatWitnessInfoMap = 11;`

      Specified by:
      :   `containsCheatWitnessInfoMap` in interface `Response.NodeInfoOrBuilder`
    - #### getCheatWitnessInfoMap

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.String> getCheatWitnessInfoMap()
      ```

      Deprecated.

      Use [`getCheatWitnessInfoMapMap()`](../../../../org/tron/trident/proto/Response.NodeInfo.Builder.html#getCheatWitnessInfoMapMap--) instead.

      Specified by:
      :   `getCheatWitnessInfoMap` in interface `Response.NodeInfoOrBuilder`
    - #### getCheatWitnessInfoMapMap

      ```
      public java.util.Map<java.lang.String,java.lang.String> getCheatWitnessInfoMapMap()
      ```

      `map<string, string> cheatWitnessInfoMap = 11;`

      Specified by:
      :   `getCheatWitnessInfoMapMap` in interface `Response.NodeInfoOrBuilder`
    - #### getCheatWitnessInfoMapOrDefault

      ```
      public java.lang.String getCheatWitnessInfoMapOrDefault(java.lang.String key,
                                                              java.lang.String defaultValue)
      ```

      `map<string, string> cheatWitnessInfoMap = 11;`

      Specified by:
      :   `getCheatWitnessInfoMapOrDefault` in interface `Response.NodeInfoOrBuilder`
    - #### getCheatWitnessInfoMapOrThrow

      ```
      public java.lang.String getCheatWitnessInfoMapOrThrow(java.lang.String key)
      ```

      `map<string, string> cheatWitnessInfoMap = 11;`

      Specified by:
      :   `getCheatWitnessInfoMapOrThrow` in interface `Response.NodeInfoOrBuilder`
    - #### clearCheatWitnessInfoMap

      ```
      public Response.NodeInfo.Builder clearCheatWitnessInfoMap()
      ```
    - #### removeCheatWitnessInfoMap

      ```
      public Response.NodeInfo.Builder removeCheatWitnessInfoMap(java.lang.String key)
      ```

      `map<string, string> cheatWitnessInfoMap = 11;`
    - #### getMutableCheatWitnessInfoMap

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.String> getMutableCheatWitnessInfoMap()
      ```

      Deprecated.

      Use alternate mutation accessors instead.
    - #### putCheatWitnessInfoMap

      ```
      public Response.NodeInfo.Builder putCheatWitnessInfoMap(java.lang.String key,
                                                              java.lang.String value)
      ```

      `map<string, string> cheatWitnessInfoMap = 11;`
    - #### putAllCheatWitnessInfoMap

      ```
      public Response.NodeInfo.Builder putAllCheatWitnessInfoMap(java.util.Map<java.lang.String,java.lang.String> values)
      ```

      `map<string, string> cheatWitnessInfoMap = 11;`
    - #### setUnknownFields

      ```
      public final Response.NodeInfo.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.NodeInfo.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.Builder>`