

org.tron.trident.proto

## Class Response.NodeInfo

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.NodeInfo

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.NodeInfoOrBuilder](../../../../org/tron/trident/proto/Response.NodeInfoOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.NodeInfo
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.NodeInfoOrBuilder
  ```

  Protobuf type `protocol.NodeInfo`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.NodeInfo)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.NodeInfo.Builder` Protobuf type `protocol.NodeInfo` |
    | `static class` | `Response.NodeInfo.ConfigNodeInfo` Protobuf type `protocol.NodeInfo.ConfigNodeInfo` |
    | `static interface` | `Response.NodeInfo.ConfigNodeInfoOrBuilder` |
    | `static class` | `Response.NodeInfo.MachineInfo` Protobuf type `protocol.NodeInfo.MachineInfo` |
    | `static interface` | `Response.NodeInfo.MachineInfoOrBuilder` |
    | `static class` | `Response.NodeInfo.PeerInfo` Protobuf type `protocol.NodeInfo.PeerInfo` |
    | `static interface` | `Response.NodeInfo.PeerInfoOrBuilder` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `ACTIVECONNECTCOUNT_FIELD_NUMBER` |
    | `static int` | `BEGINSYNCNUM_FIELD_NUMBER` |
    | `static int` | `BLOCK_FIELD_NUMBER` |
    | `static int` | `CHEATWITNESSINFOMAP_FIELD_NUMBER` |
    | `static int` | `CONFIGNODEINFO_FIELD_NUMBER` |
    | `static int` | `CURRENTCONNECTCOUNT_FIELD_NUMBER` |
    | `static int` | `MACHINEINFO_FIELD_NUMBER` |
    | `static int` | `PASSIVECONNECTCOUNT_FIELD_NUMBER` |
    | `static int` | `PEERINFOLIST_FIELD_NUMBER` |
    | `static int` | `SOLIDITYBLOCK_FIELD_NUMBER` |
    | `static int` | `TOTALFLOW_FIELD_NUMBER` |

    - ### Fields inherited from class com.google.protobuf.GeneratedMessageV3

      `alwaysUseFieldBuilders, unknownFields`
    - ### Fields inherited from class com.google.protobuf.AbstractMessage

      `memoizedSize`
    - ### Fields inherited from class com.google.protobuf.AbstractMessageLite

      `memoizedHashCode`
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `boolean` | `containsCheatWitnessInfoMap(java.lang.String key)` `map<string, string> cheatWitnessInfoMap = 11;` |
    | `boolean` | `equals(java.lang.Object obj)` |
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
    | `static Response.NodeInfo` | `getDefaultInstance()` |
    | `Response.NodeInfo` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `Response.NodeInfo.MachineInfo` | `getMachineInfo()` `.protocol.NodeInfo.MachineInfo machineInfo = 10;` |
    | `Response.NodeInfo.MachineInfoOrBuilder` | `getMachineInfoOrBuilder()` `.protocol.NodeInfo.MachineInfo machineInfo = 10;` |
    | `com.google.protobuf.Parser<Response.NodeInfo>` | `getParserForType()` |
    | `int` | `getPassiveConnectCount()` `int32 passiveConnectCount = 6;` |
    | `Response.NodeInfo.PeerInfo` | `getPeerInfoList(int index)` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `int` | `getPeerInfoListCount()` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `java.util.List<Response.NodeInfo.PeerInfo>` | `getPeerInfoListList()` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `Response.NodeInfo.PeerInfoOrBuilder` | `getPeerInfoListOrBuilder(int index)` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `java.util.List<? extends Response.NodeInfo.PeerInfoOrBuilder>` | `getPeerInfoListOrBuilderList()` `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;` |
    | `int` | `getSerializedSize()` |
    | `java.lang.String` | `getSolidityBlock()` `string solidityBlock = 3;` |
    | `com.google.protobuf.ByteString` | `getSolidityBlockBytes()` `string solidityBlock = 3;` |
    | `long` | `getTotalFlow()` `int64 totalFlow = 7;` |
    | `boolean` | `hasConfigNodeInfo()` `.protocol.NodeInfo.ConfigNodeInfo configNodeInfo = 9;` |
    | `int` | `hashCode()` |
    | `boolean` | `hasMachineInfo()` `.protocol.NodeInfo.MachineInfo machineInfo = 10;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMapFieldReflection(int number)` |
    | `boolean` | `isInitialized()` |
    | `static Response.NodeInfo.Builder` | `newBuilder()` |
    | `static Response.NodeInfo.Builder` | `newBuilder(Response.NodeInfo prototype)` |
    | `Response.NodeInfo.Builder` | `newBuilderForType()` |
    | `protected Response.NodeInfo.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.NodeInfo` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.NodeInfo` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo` | `parseFrom(byte[] data)` |
    | `static Response.NodeInfo` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.NodeInfo` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.NodeInfo` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.NodeInfo` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo` | `parseFrom(java.io.InputStream input)` |
    | `static Response.NodeInfo` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.NodeInfo>` | `parser()` |
    | `Response.NodeInfo.Builder` | `toBuilder()` |
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

    - #### BEGINSYNCNUM\_FIELD\_NUMBER

      ```
      public static final int BEGINSYNCNUM_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.BEGINSYNCNUM_FIELD_NUMBER)
    - #### BLOCK\_FIELD\_NUMBER

      ```
      public static final int BLOCK_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.BLOCK_FIELD_NUMBER)
    - #### SOLIDITYBLOCK\_FIELD\_NUMBER

      ```
      public static final int SOLIDITYBLOCK_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.SOLIDITYBLOCK_FIELD_NUMBER)
    - #### CURRENTCONNECTCOUNT\_FIELD\_NUMBER

      ```
      public static final int CURRENTCONNECTCOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.CURRENTCONNECTCOUNT_FIELD_NUMBER)
    - #### ACTIVECONNECTCOUNT\_FIELD\_NUMBER

      ```
      public static final int ACTIVECONNECTCOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.ACTIVECONNECTCOUNT_FIELD_NUMBER)
    - #### PASSIVECONNECTCOUNT\_FIELD\_NUMBER

      ```
      public static final int PASSIVECONNECTCOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PASSIVECONNECTCOUNT_FIELD_NUMBER)
    - #### TOTALFLOW\_FIELD\_NUMBER

      ```
      public static final int TOTALFLOW_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.TOTALFLOW_FIELD_NUMBER)
    - #### PEERINFOLIST\_FIELD\_NUMBER

      ```
      public static final int PEERINFOLIST_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.PEERINFOLIST_FIELD_NUMBER)
    - #### CONFIGNODEINFO\_FIELD\_NUMBER

      ```
      public static final int CONFIGNODEINFO_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.CONFIGNODEINFO_FIELD_NUMBER)
    - #### MACHINEINFO\_FIELD\_NUMBER

      ```
      public static final int MACHINEINFO_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MACHINEINFO_FIELD_NUMBER)
    - #### CHEATWITNESSINFOMAP\_FIELD\_NUMBER

      ```
      public static final int CHEATWITNESSINFOMAP_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.CHEATWITNESSINFOMAP_FIELD_NUMBER)
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
    - #### getBeginSyncNum

      ```
      public long getBeginSyncNum()
      ```

      `int64 beginSyncNum = 1;`

      Specified by:
      :   `getBeginSyncNum` in interface `Response.NodeInfoOrBuilder`

      Returns:
      :   The beginSyncNum.
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
    - #### getActiveConnectCount

      ```
      public int getActiveConnectCount()
      ```

      `int32 activeConnectCount = 5;`

      Specified by:
      :   `getActiveConnectCount` in interface `Response.NodeInfoOrBuilder`

      Returns:
      :   The activeConnectCount.
    - #### getPassiveConnectCount

      ```
      public int getPassiveConnectCount()
      ```

      `int32 passiveConnectCount = 6;`

      Specified by:
      :   `getPassiveConnectCount` in interface `Response.NodeInfoOrBuilder`

      Returns:
      :   The passiveConnectCount.
    - #### getTotalFlow

      ```
      public long getTotalFlow()
      ```

      `int64 totalFlow = 7;`

      Specified by:
      :   `getTotalFlow` in interface `Response.NodeInfoOrBuilder`

      Returns:
      :   The totalFlow.
    - #### getPeerInfoListList

      ```
      public java.util.List<Response.NodeInfo.PeerInfo> getPeerInfoListList()
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`

      Specified by:
      :   `getPeerInfoListList` in interface `Response.NodeInfoOrBuilder`
    - #### getPeerInfoListOrBuilderList

      ```
      public java.util.List<? extends Response.NodeInfo.PeerInfoOrBuilder> getPeerInfoListOrBuilderList()
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`

      Specified by:
      :   `getPeerInfoListOrBuilderList` in interface `Response.NodeInfoOrBuilder`
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
    - #### getPeerInfoListOrBuilder

      ```
      public Response.NodeInfo.PeerInfoOrBuilder getPeerInfoListOrBuilder(int index)
      ```

      `repeated .protocol.NodeInfo.PeerInfo peerInfoList = 8;`

      Specified by:
      :   `getPeerInfoListOrBuilder` in interface `Response.NodeInfoOrBuilder`
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

      Use [`getCheatWitnessInfoMapMap()`](../../../../org/tron/trident/proto/Response.NodeInfo.html#getCheatWitnessInfoMapMap--) instead.

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
      public static Response.NodeInfo parseFrom(java.nio.ByteBuffer data)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo parseFrom(java.nio.ByteBuffer data,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo parseFrom(com.google.protobuf.ByteString data)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo parseFrom(com.google.protobuf.ByteString data,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo parseFrom(byte[] data)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo parseFrom(byte[] data,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo parseFrom(java.io.InputStream input)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.NodeInfo parseFrom(java.io.InputStream input,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.NodeInfo parseDelimitedFrom(java.io.InputStream input)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.NodeInfo parseDelimitedFrom(java.io.InputStream input,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.NodeInfo parseFrom(com.google.protobuf.CodedInputStream input)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.NodeInfo parseFrom(com.google.protobuf.CodedInputStream input,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.NodeInfo.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.NodeInfo.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.NodeInfo.Builder newBuilder(Response.NodeInfo prototype)
      ```
    - #### toBuilder

      ```
      public Response.NodeInfo.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.NodeInfo.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.NodeInfo getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.NodeInfo> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.NodeInfo> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.NodeInfo getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`