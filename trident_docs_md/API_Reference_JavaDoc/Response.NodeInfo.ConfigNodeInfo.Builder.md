

org.tron.trident.proto

## Class Response.NodeInfo.ConfigNodeInfo.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.NodeInfo.ConfigNodeInfo.Builder](../../../../org/tron/trident/proto/Response.NodeInfo.ConfigNodeInfo.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.NodeInfo.ConfigNodeInfo.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.NodeInfo.ConfigNodeInfoOrBuilder](../../../../org/tron/trident/proto/Response.NodeInfo.ConfigNodeInfoOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.NodeInfo.ConfigNodeInfo](../../../../org/tron/trident/proto/Response.NodeInfo.ConfigNodeInfo.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.NodeInfo.ConfigNodeInfo.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.ConfigNodeInfo.Builder>
  implements Response.NodeInfo.ConfigNodeInfoOrBuilder
  ```

  Protobuf type `protocol.NodeInfo.ConfigNodeInfo`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.NodeInfo.ConfigNodeInfo` | `build()` |
    | `Response.NodeInfo.ConfigNodeInfo` | `buildPartial()` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `clear()` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `clearActiveNodeSize()` `int32 activeNodeSize = 5;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `clearAllowAdaptiveEnergy()` `int64 allowAdaptiveEnergy = 19;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `clearAllowCreationOfContracts()` `int64 allowCreationOfContracts = 18;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `clearBackupListenPort()` `int32 backupListenPort = 10;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `clearBackupMemberSize()` `int32 backupMemberSize = 11;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `clearBackupPriority()` `int32 backupPriority = 12;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `clearCodeVersion()` `string codeVersion = 1;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `clearDbVersion()` `int32 dbVersion = 13;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `clearDiscoverEnable()` `bool discoverEnable = 4;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `clearListenPort()` `int32 listenPort = 3;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `clearMaxConnectCount()` `int32 maxConnectCount = 8;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `clearMaxTimeRatio()` `double maxTimeRatio = 17;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `clearMinParticipationRate()` `int32 minParticipationRate = 14;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `clearMinTimeRatio()` `double minTimeRatio = 16;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `clearP2PVersion()` `string p2pVersion = 2;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `clearPassiveNodeSize()` `int32 passiveNodeSize = 6;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `clearSameIpMaxConnectCount()` `int32 sameIpMaxConnectCount = 9;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `clearSendNodeSize()` `int32 sendNodeSize = 7;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `clearSupportConstant()` `bool supportConstant = 15;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `clone()` |
    | `int` | `getActiveNodeSize()` `int32 activeNodeSize = 5;` |
    | `long` | `getAllowAdaptiveEnergy()` `int64 allowAdaptiveEnergy = 19;` |
    | `long` | `getAllowCreationOfContracts()` `int64 allowCreationOfContracts = 18;` |
    | `int` | `getBackupListenPort()` `int32 backupListenPort = 10;` |
    | `int` | `getBackupMemberSize()` `int32 backupMemberSize = 11;` |
    | `int` | `getBackupPriority()` `int32 backupPriority = 12;` |
    | `java.lang.String` | `getCodeVersion()` `string codeVersion = 1;` |
    | `com.google.protobuf.ByteString` | `getCodeVersionBytes()` `string codeVersion = 1;` |
    | `int` | `getDbVersion()` `int32 dbVersion = 13;` |
    | `Response.NodeInfo.ConfigNodeInfo` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `boolean` | `getDiscoverEnable()` `bool discoverEnable = 4;` |
    | `int` | `getListenPort()` `int32 listenPort = 3;` |
    | `int` | `getMaxConnectCount()` `int32 maxConnectCount = 8;` |
    | `double` | `getMaxTimeRatio()` `double maxTimeRatio = 17;` |
    | `int` | `getMinParticipationRate()` `int32 minParticipationRate = 14;` |
    | `double` | `getMinTimeRatio()` `double minTimeRatio = 16;` |
    | `java.lang.String` | `getP2PVersion()` `string p2pVersion = 2;` |
    | `com.google.protobuf.ByteString` | `getP2PVersionBytes()` `string p2pVersion = 2;` |
    | `int` | `getPassiveNodeSize()` `int32 passiveNodeSize = 6;` |
    | `int` | `getSameIpMaxConnectCount()` `int32 sameIpMaxConnectCount = 9;` |
    | `int` | `getSendNodeSize()` `int32 sendNodeSize = 7;` |
    | `boolean` | `getSupportConstant()` `bool supportConstant = 15;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `mergeFrom(Response.NodeInfo.ConfigNodeInfo other)` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setActiveNodeSize(int value)` `int32 activeNodeSize = 5;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setAllowAdaptiveEnergy(long value)` `int64 allowAdaptiveEnergy = 19;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setAllowCreationOfContracts(long value)` `int64 allowCreationOfContracts = 18;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setBackupListenPort(int value)` `int32 backupListenPort = 10;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setBackupMemberSize(int value)` `int32 backupMemberSize = 11;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setBackupPriority(int value)` `int32 backupPriority = 12;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setCodeVersion(java.lang.String value)` `string codeVersion = 1;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setCodeVersionBytes(com.google.protobuf.ByteString value)` `string codeVersion = 1;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setDbVersion(int value)` `int32 dbVersion = 13;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setDiscoverEnable(boolean value)` `bool discoverEnable = 4;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setListenPort(int value)` `int32 listenPort = 3;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setMaxConnectCount(int value)` `int32 maxConnectCount = 8;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setMaxTimeRatio(double value)` `double maxTimeRatio = 17;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setMinParticipationRate(int value)` `int32 minParticipationRate = 14;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setMinTimeRatio(double value)` `double minTimeRatio = 16;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setP2PVersion(java.lang.String value)` `string p2pVersion = 2;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setP2PVersionBytes(com.google.protobuf.ByteString value)` `string p2pVersion = 2;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setPassiveNodeSize(int value)` `int32 passiveNodeSize = 6;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setSameIpMaxConnectCount(int value)` `int32 sameIpMaxConnectCount = 9;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setSendNodeSize(int value)` `int32 sendNodeSize = 7;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setSupportConstant(boolean value)` `bool supportConstant = 15;` |
    | `Response.NodeInfo.ConfigNodeInfo.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.ConfigNodeInfo.Builder>`
    - #### clear

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.ConfigNodeInfo.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.ConfigNodeInfo.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.NodeInfo.ConfigNodeInfo getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.NodeInfo.ConfigNodeInfo build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.NodeInfo.ConfigNodeInfo buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.ConfigNodeInfo.Builder>`
    - #### setField

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.ConfigNodeInfo.Builder>`
    - #### clearField

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.ConfigNodeInfo.Builder>`
    - #### clearOneof

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.ConfigNodeInfo.Builder>`
    - #### setRepeatedField

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                       int index,
                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.ConfigNodeInfo.Builder>`
    - #### addRepeatedField

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.ConfigNodeInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.NodeInfo.ConfigNodeInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder mergeFrom(Response.NodeInfo.ConfigNodeInfo other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.ConfigNodeInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.NodeInfo.ConfigNodeInfo.Builder>`

      Throws:
      :   `java.io.IOException`
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
    - #### setCodeVersion

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder setCodeVersion(java.lang.String value)
      ```

      `string codeVersion = 1;`

      Parameters:
      :   `value` - The codeVersion to set.

      Returns:
      :   This builder for chaining.
    - #### clearCodeVersion

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder clearCodeVersion()
      ```

      `string codeVersion = 1;`

      Returns:
      :   This builder for chaining.
    - #### setCodeVersionBytes

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder setCodeVersionBytes(com.google.protobuf.ByteString value)
      ```

      `string codeVersion = 1;`

      Parameters:
      :   `value` - The bytes for codeVersion to set.

      Returns:
      :   This builder for chaining.
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
    - #### setP2PVersion

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder setP2PVersion(java.lang.String value)
      ```

      `string p2pVersion = 2;`

      Parameters:
      :   `value` - The p2pVersion to set.

      Returns:
      :   This builder for chaining.
    - #### clearP2PVersion

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder clearP2PVersion()
      ```

      `string p2pVersion = 2;`

      Returns:
      :   This builder for chaining.
    - #### setP2PVersionBytes

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder setP2PVersionBytes(com.google.protobuf.ByteString value)
      ```

      `string p2pVersion = 2;`

      Parameters:
      :   `value` - The bytes for p2pVersion to set.

      Returns:
      :   This builder for chaining.
    - #### getListenPort

      ```
      public int getListenPort()
      ```

      `int32 listenPort = 3;`

      Specified by:
      :   `getListenPort` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The listenPort.
    - #### setListenPort

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder setListenPort(int value)
      ```

      `int32 listenPort = 3;`

      Parameters:
      :   `value` - The listenPort to set.

      Returns:
      :   This builder for chaining.
    - #### clearListenPort

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder clearListenPort()
      ```

      `int32 listenPort = 3;`

      Returns:
      :   This builder for chaining.
    - #### getDiscoverEnable

      ```
      public boolean getDiscoverEnable()
      ```

      `bool discoverEnable = 4;`

      Specified by:
      :   `getDiscoverEnable` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The discoverEnable.
    - #### setDiscoverEnable

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder setDiscoverEnable(boolean value)
      ```

      `bool discoverEnable = 4;`

      Parameters:
      :   `value` - The discoverEnable to set.

      Returns:
      :   This builder for chaining.
    - #### clearDiscoverEnable

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder clearDiscoverEnable()
      ```

      `bool discoverEnable = 4;`

      Returns:
      :   This builder for chaining.
    - #### getActiveNodeSize

      ```
      public int getActiveNodeSize()
      ```

      `int32 activeNodeSize = 5;`

      Specified by:
      :   `getActiveNodeSize` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The activeNodeSize.
    - #### setActiveNodeSize

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder setActiveNodeSize(int value)
      ```

      `int32 activeNodeSize = 5;`

      Parameters:
      :   `value` - The activeNodeSize to set.

      Returns:
      :   This builder for chaining.
    - #### clearActiveNodeSize

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder clearActiveNodeSize()
      ```

      `int32 activeNodeSize = 5;`

      Returns:
      :   This builder for chaining.
    - #### getPassiveNodeSize

      ```
      public int getPassiveNodeSize()
      ```

      `int32 passiveNodeSize = 6;`

      Specified by:
      :   `getPassiveNodeSize` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The passiveNodeSize.
    - #### setPassiveNodeSize

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder setPassiveNodeSize(int value)
      ```

      `int32 passiveNodeSize = 6;`

      Parameters:
      :   `value` - The passiveNodeSize to set.

      Returns:
      :   This builder for chaining.
    - #### clearPassiveNodeSize

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder clearPassiveNodeSize()
      ```

      `int32 passiveNodeSize = 6;`

      Returns:
      :   This builder for chaining.
    - #### getSendNodeSize

      ```
      public int getSendNodeSize()
      ```

      `int32 sendNodeSize = 7;`

      Specified by:
      :   `getSendNodeSize` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The sendNodeSize.
    - #### setSendNodeSize

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder setSendNodeSize(int value)
      ```

      `int32 sendNodeSize = 7;`

      Parameters:
      :   `value` - The sendNodeSize to set.

      Returns:
      :   This builder for chaining.
    - #### clearSendNodeSize

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder clearSendNodeSize()
      ```

      `int32 sendNodeSize = 7;`

      Returns:
      :   This builder for chaining.
    - #### getMaxConnectCount

      ```
      public int getMaxConnectCount()
      ```

      `int32 maxConnectCount = 8;`

      Specified by:
      :   `getMaxConnectCount` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The maxConnectCount.
    - #### setMaxConnectCount

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder setMaxConnectCount(int value)
      ```

      `int32 maxConnectCount = 8;`

      Parameters:
      :   `value` - The maxConnectCount to set.

      Returns:
      :   This builder for chaining.
    - #### clearMaxConnectCount

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder clearMaxConnectCount()
      ```

      `int32 maxConnectCount = 8;`

      Returns:
      :   This builder for chaining.
    - #### getSameIpMaxConnectCount

      ```
      public int getSameIpMaxConnectCount()
      ```

      `int32 sameIpMaxConnectCount = 9;`

      Specified by:
      :   `getSameIpMaxConnectCount` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The sameIpMaxConnectCount.
    - #### setSameIpMaxConnectCount

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder setSameIpMaxConnectCount(int value)
      ```

      `int32 sameIpMaxConnectCount = 9;`

      Parameters:
      :   `value` - The sameIpMaxConnectCount to set.

      Returns:
      :   This builder for chaining.
    - #### clearSameIpMaxConnectCount

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder clearSameIpMaxConnectCount()
      ```

      `int32 sameIpMaxConnectCount = 9;`

      Returns:
      :   This builder for chaining.
    - #### getBackupListenPort

      ```
      public int getBackupListenPort()
      ```

      `int32 backupListenPort = 10;`

      Specified by:
      :   `getBackupListenPort` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The backupListenPort.
    - #### setBackupListenPort

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder setBackupListenPort(int value)
      ```

      `int32 backupListenPort = 10;`

      Parameters:
      :   `value` - The backupListenPort to set.

      Returns:
      :   This builder for chaining.
    - #### clearBackupListenPort

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder clearBackupListenPort()
      ```

      `int32 backupListenPort = 10;`

      Returns:
      :   This builder for chaining.
    - #### getBackupMemberSize

      ```
      public int getBackupMemberSize()
      ```

      `int32 backupMemberSize = 11;`

      Specified by:
      :   `getBackupMemberSize` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The backupMemberSize.
    - #### setBackupMemberSize

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder setBackupMemberSize(int value)
      ```

      `int32 backupMemberSize = 11;`

      Parameters:
      :   `value` - The backupMemberSize to set.

      Returns:
      :   This builder for chaining.
    - #### clearBackupMemberSize

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder clearBackupMemberSize()
      ```

      `int32 backupMemberSize = 11;`

      Returns:
      :   This builder for chaining.
    - #### getBackupPriority

      ```
      public int getBackupPriority()
      ```

      `int32 backupPriority = 12;`

      Specified by:
      :   `getBackupPriority` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The backupPriority.
    - #### setBackupPriority

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder setBackupPriority(int value)
      ```

      `int32 backupPriority = 12;`

      Parameters:
      :   `value` - The backupPriority to set.

      Returns:
      :   This builder for chaining.
    - #### clearBackupPriority

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder clearBackupPriority()
      ```

      `int32 backupPriority = 12;`

      Returns:
      :   This builder for chaining.
    - #### getDbVersion

      ```
      public int getDbVersion()
      ```

      `int32 dbVersion = 13;`

      Specified by:
      :   `getDbVersion` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The dbVersion.
    - #### setDbVersion

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder setDbVersion(int value)
      ```

      `int32 dbVersion = 13;`

      Parameters:
      :   `value` - The dbVersion to set.

      Returns:
      :   This builder for chaining.
    - #### clearDbVersion

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder clearDbVersion()
      ```

      `int32 dbVersion = 13;`

      Returns:
      :   This builder for chaining.
    - #### getMinParticipationRate

      ```
      public int getMinParticipationRate()
      ```

      `int32 minParticipationRate = 14;`

      Specified by:
      :   `getMinParticipationRate` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The minParticipationRate.
    - #### setMinParticipationRate

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder setMinParticipationRate(int value)
      ```

      `int32 minParticipationRate = 14;`

      Parameters:
      :   `value` - The minParticipationRate to set.

      Returns:
      :   This builder for chaining.
    - #### clearMinParticipationRate

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder clearMinParticipationRate()
      ```

      `int32 minParticipationRate = 14;`

      Returns:
      :   This builder for chaining.
    - #### getSupportConstant

      ```
      public boolean getSupportConstant()
      ```

      `bool supportConstant = 15;`

      Specified by:
      :   `getSupportConstant` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The supportConstant.
    - #### setSupportConstant

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder setSupportConstant(boolean value)
      ```

      `bool supportConstant = 15;`

      Parameters:
      :   `value` - The supportConstant to set.

      Returns:
      :   This builder for chaining.
    - #### clearSupportConstant

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder clearSupportConstant()
      ```

      `bool supportConstant = 15;`

      Returns:
      :   This builder for chaining.
    - #### getMinTimeRatio

      ```
      public double getMinTimeRatio()
      ```

      `double minTimeRatio = 16;`

      Specified by:
      :   `getMinTimeRatio` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The minTimeRatio.
    - #### setMinTimeRatio

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder setMinTimeRatio(double value)
      ```

      `double minTimeRatio = 16;`

      Parameters:
      :   `value` - The minTimeRatio to set.

      Returns:
      :   This builder for chaining.
    - #### clearMinTimeRatio

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder clearMinTimeRatio()
      ```

      `double minTimeRatio = 16;`

      Returns:
      :   This builder for chaining.
    - #### getMaxTimeRatio

      ```
      public double getMaxTimeRatio()
      ```

      `double maxTimeRatio = 17;`

      Specified by:
      :   `getMaxTimeRatio` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The maxTimeRatio.
    - #### setMaxTimeRatio

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder setMaxTimeRatio(double value)
      ```

      `double maxTimeRatio = 17;`

      Parameters:
      :   `value` - The maxTimeRatio to set.

      Returns:
      :   This builder for chaining.
    - #### clearMaxTimeRatio

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder clearMaxTimeRatio()
      ```

      `double maxTimeRatio = 17;`

      Returns:
      :   This builder for chaining.
    - #### getAllowCreationOfContracts

      ```
      public long getAllowCreationOfContracts()
      ```

      `int64 allowCreationOfContracts = 18;`

      Specified by:
      :   `getAllowCreationOfContracts` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The allowCreationOfContracts.
    - #### setAllowCreationOfContracts

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder setAllowCreationOfContracts(long value)
      ```

      `int64 allowCreationOfContracts = 18;`

      Parameters:
      :   `value` - The allowCreationOfContracts to set.

      Returns:
      :   This builder for chaining.
    - #### clearAllowCreationOfContracts

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder clearAllowCreationOfContracts()
      ```

      `int64 allowCreationOfContracts = 18;`

      Returns:
      :   This builder for chaining.
    - #### getAllowAdaptiveEnergy

      ```
      public long getAllowAdaptiveEnergy()
      ```

      `int64 allowAdaptiveEnergy = 19;`

      Specified by:
      :   `getAllowAdaptiveEnergy` in interface `Response.NodeInfo.ConfigNodeInfoOrBuilder`

      Returns:
      :   The allowAdaptiveEnergy.
    - #### setAllowAdaptiveEnergy

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder setAllowAdaptiveEnergy(long value)
      ```

      `int64 allowAdaptiveEnergy = 19;`

      Parameters:
      :   `value` - The allowAdaptiveEnergy to set.

      Returns:
      :   This builder for chaining.
    - #### clearAllowAdaptiveEnergy

      ```
      public Response.NodeInfo.ConfigNodeInfo.Builder clearAllowAdaptiveEnergy()
      ```

      `int64 allowAdaptiveEnergy = 19;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.NodeInfo.ConfigNodeInfo.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.ConfigNodeInfo.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.NodeInfo.ConfigNodeInfo.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.ConfigNodeInfo.Builder>`