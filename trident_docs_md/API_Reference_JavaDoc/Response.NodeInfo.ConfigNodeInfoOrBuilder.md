

org.tron.trident.proto

## Interface Response.NodeInfo.ConfigNodeInfoOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.NodeInfo.ConfigNodeInfo](../../../../org/tron/trident/proto/Response.NodeInfo.ConfigNodeInfo.html "class in org.tron.trident.proto"), [Response.NodeInfo.ConfigNodeInfo.Builder](../../../../org/tron/trident/proto/Response.NodeInfo.ConfigNodeInfo.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response.NodeInfo](../../../../org/tron/trident/proto/Response.NodeInfo.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.NodeInfo.ConfigNodeInfoOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `int` | `getActiveNodeSize()` `int32 activeNodeSize = 5;` |
    | `long` | `getAllowAdaptiveEnergy()` `int64 allowAdaptiveEnergy = 19;` |
    | `long` | `getAllowCreationOfContracts()` `int64 allowCreationOfContracts = 18;` |
    | `int` | `getBackupListenPort()` `int32 backupListenPort = 10;` |
    | `int` | `getBackupMemberSize()` `int32 backupMemberSize = 11;` |
    | `int` | `getBackupPriority()` `int32 backupPriority = 12;` |
    | `java.lang.String` | `getCodeVersion()` `string codeVersion = 1;` |
    | `com.google.protobuf.ByteString` | `getCodeVersionBytes()` `string codeVersion = 1;` |
    | `int` | `getDbVersion()` `int32 dbVersion = 13;` |
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

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getCodeVersion

      ```
      java.lang.String getCodeVersion()
      ```

      `string codeVersion = 1;`

      Returns:
      :   The codeVersion.
    - #### getCodeVersionBytes

      ```
      com.google.protobuf.ByteString getCodeVersionBytes()
      ```

      `string codeVersion = 1;`

      Returns:
      :   The bytes for codeVersion.
    - #### getP2PVersion

      ```
      java.lang.String getP2PVersion()
      ```

      `string p2pVersion = 2;`

      Returns:
      :   The p2pVersion.
    - #### getP2PVersionBytes

      ```
      com.google.protobuf.ByteString getP2PVersionBytes()
      ```

      `string p2pVersion = 2;`

      Returns:
      :   The bytes for p2pVersion.
    - #### getListenPort

      ```
      int getListenPort()
      ```

      `int32 listenPort = 3;`

      Returns:
      :   The listenPort.
    - #### getDiscoverEnable

      ```
      boolean getDiscoverEnable()
      ```

      `bool discoverEnable = 4;`

      Returns:
      :   The discoverEnable.
    - #### getActiveNodeSize

      ```
      int getActiveNodeSize()
      ```

      `int32 activeNodeSize = 5;`

      Returns:
      :   The activeNodeSize.
    - #### getPassiveNodeSize

      ```
      int getPassiveNodeSize()
      ```

      `int32 passiveNodeSize = 6;`

      Returns:
      :   The passiveNodeSize.
    - #### getSendNodeSize

      ```
      int getSendNodeSize()
      ```

      `int32 sendNodeSize = 7;`

      Returns:
      :   The sendNodeSize.
    - #### getMaxConnectCount

      ```
      int getMaxConnectCount()
      ```

      `int32 maxConnectCount = 8;`

      Returns:
      :   The maxConnectCount.
    - #### getSameIpMaxConnectCount

      ```
      int getSameIpMaxConnectCount()
      ```

      `int32 sameIpMaxConnectCount = 9;`

      Returns:
      :   The sameIpMaxConnectCount.
    - #### getBackupListenPort

      ```
      int getBackupListenPort()
      ```

      `int32 backupListenPort = 10;`

      Returns:
      :   The backupListenPort.
    - #### getBackupMemberSize

      ```
      int getBackupMemberSize()
      ```

      `int32 backupMemberSize = 11;`

      Returns:
      :   The backupMemberSize.
    - #### getBackupPriority

      ```
      int getBackupPriority()
      ```

      `int32 backupPriority = 12;`

      Returns:
      :   The backupPriority.
    - #### getDbVersion

      ```
      int getDbVersion()
      ```

      `int32 dbVersion = 13;`

      Returns:
      :   The dbVersion.
    - #### getMinParticipationRate

      ```
      int getMinParticipationRate()
      ```

      `int32 minParticipationRate = 14;`

      Returns:
      :   The minParticipationRate.
    - #### getSupportConstant

      ```
      boolean getSupportConstant()
      ```

      `bool supportConstant = 15;`

      Returns:
      :   The supportConstant.
    - #### getMinTimeRatio

      ```
      double getMinTimeRatio()
      ```

      `double minTimeRatio = 16;`

      Returns:
      :   The minTimeRatio.
    - #### getMaxTimeRatio

      ```
      double getMaxTimeRatio()
      ```

      `double maxTimeRatio = 17;`

      Returns:
      :   The maxTimeRatio.
    - #### getAllowCreationOfContracts

      ```
      long getAllowCreationOfContracts()
      ```

      `int64 allowCreationOfContracts = 18;`

      Returns:
      :   The allowCreationOfContracts.
    - #### getAllowAdaptiveEnergy

      ```
      long getAllowAdaptiveEnergy()
      ```

      `int64 allowAdaptiveEnergy = 19;`

      Returns:
      :   The allowAdaptiveEnergy.