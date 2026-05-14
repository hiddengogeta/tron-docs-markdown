

org.tron.trident.proto

## Class Response.NodeInfo.ConfigNodeInfo

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.NodeInfo.ConfigNodeInfo

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.NodeInfo.ConfigNodeInfoOrBuilder](../../../../org/tron/trident/proto/Response.NodeInfo.ConfigNodeInfoOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.NodeInfo](../../../../org/tron/trident/proto/Response.NodeInfo.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.NodeInfo.ConfigNodeInfo
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.NodeInfo.ConfigNodeInfoOrBuilder
  ```

  Protobuf type `protocol.NodeInfo.ConfigNodeInfo`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.NodeInfo.ConfigNodeInfo)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.NodeInfo.ConfigNodeInfo.Builder` Protobuf type `protocol.NodeInfo.ConfigNodeInfo` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `ACTIVENODESIZE_FIELD_NUMBER` |
    | `static int` | `ALLOWADAPTIVEENERGY_FIELD_NUMBER` |
    | `static int` | `ALLOWCREATIONOFCONTRACTS_FIELD_NUMBER` |
    | `static int` | `BACKUPLISTENPORT_FIELD_NUMBER` |
    | `static int` | `BACKUPMEMBERSIZE_FIELD_NUMBER` |
    | `static int` | `BACKUPPRIORITY_FIELD_NUMBER` |
    | `static int` | `CODEVERSION_FIELD_NUMBER` |
    | `static int` | `DBVERSION_FIELD_NUMBER` |
    | `static int` | `DISCOVERENABLE_FIELD_NUMBER` |
    | `static int` | `LISTENPORT_FIELD_NUMBER` |
    | `static int` | `MAXCONNECTCOUNT_FIELD_NUMBER` |
    | `static int` | `MAXTIMERATIO_FIELD_NUMBER` |
    | `static int` | `MINPARTICIPATIONRATE_FIELD_NUMBER` |
    | `static int` | `MINTIMERATIO_FIELD_NUMBER` |
    | `static int` | `P2PVERSION_FIELD_NUMBER` |
    | `static int` | `PASSIVENODESIZE_FIELD_NUMBER` |
    | `static int` | `SAMEIPMAXCONNECTCOUNT_FIELD_NUMBER` |
    | `static int` | `SENDNODESIZE_FIELD_NUMBER` |
    | `static int` | `SUPPORTCONSTANT_FIELD_NUMBER` |

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
    | `int` | `getActiveNodeSize()` `int32 activeNodeSize = 5;` |
    | `long` | `getAllowAdaptiveEnergy()` `int64 allowAdaptiveEnergy = 19;` |
    | `long` | `getAllowCreationOfContracts()` `int64 allowCreationOfContracts = 18;` |
    | `int` | `getBackupListenPort()` `int32 backupListenPort = 10;` |
    | `int` | `getBackupMemberSize()` `int32 backupMemberSize = 11;` |
    | `int` | `getBackupPriority()` `int32 backupPriority = 12;` |
    | `java.lang.String` | `getCodeVersion()` `string codeVersion = 1;` |
    | `com.google.protobuf.ByteString` | `getCodeVersionBytes()` `string codeVersion = 1;` |
    | `int` | `getDbVersion()` `int32 dbVersion = 13;` |
    | `static Response.NodeInfo.ConfigNodeInfo` | `getDefaultInstance()` |
    | `Response.NodeInfo.ConfigNodeInfo` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `boolean` | `getDiscoverEnable()` `bool discoverEnable = 4;` |
    | `int` | `getListenPort()` `int32 listenPort = 3;` |
    | `int` | `getMaxConnectCount()` `int32 maxConnectCount = 8;` |
    | `double` | `getMaxTimeRatio()` `double maxTimeRatio = 17;` |
    | `int` | `getMinParticipationRate()` `int32 minParticipationRate = 14;` |
    | `double` | `getMinTimeRatio()` `double minTimeRatio = 16;` |
    | `java.lang.String` | `getP2PVersion()` `string p2pVersion = 2;` |
    | `com.google.protobuf.ByteString` | `getP2PVersionBytes()` `string p2pVersion = 2;` |
    | `com.google.protobuf.Parser<Response.NodeInfo.ConfigNodeInfo>` | `getParserForType()` |
    | `int` | `getPassiveNodeSize()` `int32 passiveNodeSize = 6;` |
    | `int` | `getSameIpMaxConnectCount()` `int32 sameIpMaxConnectCount = 9;` |
    | `int` | `getSendNodeSize()` `int32 sendNodeSize = 7;` |
    | `int` | `getSerializedSize()` |
    | `boolean` | `getSupportConstant()` `bool supportConstant = 15;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Response.NodeInfo.ConfigNodeInfo.Builder` | `newBuilder()` |
    | `static Response.NodeInfo.ConfigNodeInfo.Builder` | `newBuilder(Response.NodeInfo.ConfigNodeInfo prototype)` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `newBuilderForType()` |
    | `protected Response.NodeInfo.ConfigNodeInfo.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.NodeInfo.ConfigNodeInfo` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.NodeInfo.ConfigNodeInfo` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.ConfigNodeInfo` | `parseFrom(byte[] data)` |
    | `static Response.NodeInfo.ConfigNodeInfo` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.ConfigNodeInfo` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.NodeInfo.ConfigNodeInfo` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.ConfigNodeInfo` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.NodeInfo.ConfigNodeInfo` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.ConfigNodeInfo` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.NodeInfo.ConfigNodeInfo` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.ConfigNodeInfo` | `parseFrom(java.io.InputStream input)` |
    | `static Response.NodeInfo.ConfigNodeInfo` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.NodeInfo.ConfigNodeInfo>` | `parser()` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `toBuilder()` |
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

    - #### CODEVERSION\_FIELD\_NUMBER

      ```
      public static final int CODEVERSION_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.ConfigNodeInfo.CODEVERSION_FIELD_NUMBER)
    - #### P2PVERSION\_FIELD\_NUMBER

      ```
      public static final int P2PVERSION_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.ConfigNodeInfo.P2PVERSION_FIELD_NUMBER)
    - #### LISTENPORT\_FIELD\_NUMBER

      ```
      public static final int LISTENPORT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.ConfigNodeInfo.LISTENPORT_FIELD_NUMBER)
    - #### DISCOVERENABLE\_FIELD\_NUMBER

      ```
      public static final int DISCOVERENABLE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.ConfigNodeInfo.DISCOVERENABLE_FIELD_NUMBER)
    - #### ACTIVENODESIZE\_FIELD\_NUMBER

      ```
      public static final int ACTIVENODESIZE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.ConfigNodeInfo.ACTIVENODESIZE_FIELD_NUMBER)
    - #### PASSIVENODESIZE\_FIELD\_NUMBER

      ```
      public static final int PASSIVENODESIZE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.ConfigNodeInfo.PASSIVENODESIZE_FIELD_NUMBER)
    - #### SENDNODESIZE\_FIELD\_NUMBER

      ```
      public static final int SENDNODESIZE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.ConfigNodeInfo.SENDNODESIZE_FIELD_NUMBER)
    - #### MAXCONNECTCOUNT\_FIELD\_NUMBER

      ```
      public static final int MAXCONNECTCOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.ConfigNodeInfo.MAXCONNECTCOUNT_FIELD_NUMBER)
    - #### SAMEIPMAXCONNECTCOUNT\_FIELD\_NUMBER

      ```
      public static final int SAMEIPMAXCONNECTCOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.ConfigNodeInfo.SAMEIPMAXCONNECTCOUNT_FIELD_NUMBER)
    - #### BACKUPLISTENPORT\_FIELD\_NUMBER

      ```
      public static final int BACKUPLISTENPORT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.ConfigNodeInfo.BACKUPLISTENPORT_FIELD_NUMBER)
    - #### BACKUPMEMBERSIZE\_FIELD\_NUMBER

      ```
      public static final int BACKUPMEMBERSIZE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.ConfigNodeInfo.BACKUPMEMBERSIZE_FIELD_NUMBER)
    - #### BACKUPPRIORITY\_FIELD\_NUMBER

      ```
      public static final int BACKUPPRIORITY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.ConfigNodeInfo.BACKUPPRIORITY_FIELD_NUMBER)
    - #### DBVERSION\_FIELD\_NUMBER

      ```
      public static final int DBVERSION_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.ConfigNodeInfo.DBVERSION_FIELD_NUMBER)
    - #### MINPARTICIPATIONRATE\_FIELD\_NUMBER

      ```
      public static final int MINPARTICIPATIONRATE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.ConfigNodeInfo.MINPARTICIPATIONRATE_FIELD_NUMBER)
    - #### SUPPORTCONSTANT\_FIELD\_NUMBER

      ```
      public static final int SUPPORTCONSTANT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.ConfigNodeInfo.SUPPORTCONSTANT_FIELD_NUMBER)
    - #### MINTIMERATIO\_FIELD\_NUMBER

      ```
      public static final int MINTIMERATIO_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.ConfigNodeInfo.MINTIMERATIO_FIELD_NUMBER)
    - #### MAXTIMERATIO\_FIELD\_NUMBER

      ```
      public static final int MAXTIMERATIO_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.ConfigNodeInfo.MAXTIMERATIO_FIELD_NUMBER)
    - #### ALLOWCREATIONOFCONTRACTS\_FIELD\_NUMBER

      ```
      public static final int ALLOWCREATIONOFCONTRACTS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.ConfigNodeInfo.ALLOWCREATIONOFCONTRACTS_FIELD_NUMBER)
    - #### ALLOWADAPTIVEENERGY\_FIELD\_NUMBER

      ```
      public static final int ALLOWADAPTIVEENERGY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.ConfigNodeInfo.ALLOWADAPTIVEENERGY_FIELD_NUMBER)
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
    - #### getCodeVersion

      ```
      public java.lang.String getCodeVersion()
      ```

      `string codeVersion = 1;`

      Specified by:
      :   `getCodeVersion` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The codeVersion.
    - #### getCodeVersionBytes

      ```
      public com.google.protobuf.ByteString getCodeVersionBytes()
      ```

      `string codeVersion = 1;`

      Specified by:
      :   `getCodeVersionBytes` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The bytes for codeVersion.
    - #### getP2PVersion

      ```
      public java.lang.String getP2PVersion()
      ```

      `string p2pVersion = 2;`

      Specified by:
      :   `getP2PVersion` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The p2pVersion.
    - #### getP2PVersionBytes

      ```
      public com.google.protobuf.ByteString getP2PVersionBytes()
      ```

      `string p2pVersion = 2;`

      Specified by:
      :   `getP2PVersionBytes` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The bytes for p2pVersion.
    - #### getListenPort

      ```
      public int getListenPort()
      ```

      `int32 listenPort = 3;`

      Specified by:
      :   `getListenPort` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The listenPort.
    - #### getDiscoverEnable

      ```
      public boolean getDiscoverEnable()
      ```

      `bool discoverEnable = 4;`

      Specified by:
      :   `getDiscoverEnable` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The discoverEnable.
    - #### getActiveNodeSize

      ```
      public int getActiveNodeSize()
      ```

      `int32 activeNodeSize = 5;`

      Specified by:
      :   `getActiveNodeSize` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The activeNodeSize.
    - #### getPassiveNodeSize

      ```
      public int getPassiveNodeSize()
      ```

      `int32 passiveNodeSize = 6;`

      Specified by:
      :   `getPassiveNodeSize` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The passiveNodeSize.
    - #### getSendNodeSize

      ```
      public int getSendNodeSize()
      ```

      `int32 sendNodeSize = 7;`

      Specified by:
      :   `getSendNodeSize` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The sendNodeSize.
    - #### getMaxConnectCount

      ```
      public int getMaxConnectCount()
      ```

      `int32 maxConnectCount = 8;`

      Specified by:
      :   `getMaxConnectCount` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The maxConnectCount.
    - #### getSameIpMaxConnectCount

      ```
      public int getSameIpMaxConnectCount()
      ```

      `int32 sameIpMaxConnectCount = 9;`

      Specified by:
      :   `getSameIpMaxConnectCount` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The sameIpMaxConnectCount.
    - #### getBackupListenPort

      ```
      public int getBackupListenPort()
      ```

      `int32 backupListenPort = 10;`

      Specified by:
      :   `getBackupListenPort` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The backupListenPort.
    - #### getBackupMemberSize

      ```
      public int getBackupMemberSize()
      ```

      `int32 backupMemberSize = 11;`

      Specified by:
      :   `getBackupMemberSize` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The backupMemberSize.
    - #### getBackupPriority

      ```
      public int getBackupPriority()
      ```

      `int32 backupPriority = 12;`

      Specified by:
      :   `getBackupPriority` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The backupPriority.
    - #### getDbVersion

      ```
      public int getDbVersion()
      ```

      `int32 dbVersion = 13;`

      Specified by:
      :   `getDbVersion` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The dbVersion.
    - #### getMinParticipationRate

      ```
      public int getMinParticipationRate()
      ```

      `int32 minParticipationRate = 14;`

      Specified by:
      :   `getMinParticipationRate` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The minParticipationRate.
    - #### getSupportConstant

      ```
      public boolean getSupportConstant()
      ```

      `bool supportConstant = 15;`

      Specified by:
      :   `getSupportConstant` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The supportConstant.
    - #### getMinTimeRatio

      ```
      public double getMinTimeRatio()
      ```

      `double minTimeRatio = 16;`

      Specified by:
      :   `getMinTimeRatio` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The minTimeRatio.
    - #### getMaxTimeRatio

      ```
      public double getMaxTimeRatio()
      ```

      `double maxTimeRatio = 17;`

      Specified by:
      :   `getMaxTimeRatio` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The maxTimeRatio.
    - #### getAllowCreationOfContracts

      ```
      public long getAllowCreationOfContracts()
      ```

      `int64 allowCreationOfContracts = 18;`

      Specified by:
      :   `getAllowCreationOfContracts` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The allowCreationOfContracts.
    - #### getAllowAdaptiveEnergy

      ```
      public long getAllowAdaptiveEnergy()
      ```

      `int64 allowAdaptiveEnergy = 19;`

      Specified by:
      :   `getAllowAdaptiveEnergy` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The allowAdaptiveEnergy.
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
      public static Response.NodeInfo.ConfigNodeInfo parseFrom(java.nio.ByteBuffer data)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.ConfigNodeInfo parseFrom(java.nio.ByteBuffer data,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.ConfigNodeInfo parseFrom(com.google.protobuf.ByteString data)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.ConfigNodeInfo parseFrom(com.google.protobuf.ByteString data,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.ConfigNodeInfo parseFrom(byte[] data)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.ConfigNodeInfo parseFrom(byte[] data,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.ConfigNodeInfo parseFrom(java.io.InputStream input)
                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.ConfigNodeInfo parseFrom(java.io.InputStream input,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.NodeInfo.ConfigNodeInfo parseDelimitedFrom(java.io.InputStream input)
                                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.NodeInfo.ConfigNodeInfo parseDelimitedFrom(java.io.InputStream input,
                                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.ConfigNodeInfo parseFrom(com.google.protobuf.CodedInputStream input)
                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.ConfigNodeInfo parseFrom(com.google.protobuf.CodedInputStream input,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.NodeInfo.ConfigNodeInfo.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.NodeInfo.ConfigNodeInfo.Builder newBuilder(Response.NodeInfo.ConfigNodeInfo prototype)
      ```
    - #### toBuilder

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.NodeInfo.ConfigNodeInfo.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.NodeInfo.ConfigNodeInfo getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.NodeInfo.ConfigNodeInfo> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.NodeInfo.ConfigNodeInfo> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.NodeInfo.ConfigNodeInfo getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`