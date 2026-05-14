

org.tron.trident.proto

## Interface Common.PermissionOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Common.Permission](../../../../org/tron/trident/proto/Common.Permission.html "class in org.tron.trident.proto"), [Common.Permission.Builder](../../../../org/tron/trident/proto/Common.Permission.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Common](../../../../org/tron/trident/proto/Common.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Common.PermissionOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `int` | `getId()` Owner id=0, Witness id=1, Active id start by 2 |
    | `Common.Key` | `getKeys(int index)` `repeated .protocol.Key keys = 7;` |
    | `int` | `getKeysCount()` `repeated .protocol.Key keys = 7;` |
    | `java.util.List<Common.Key>` | `getKeysList()` `repeated .protocol.Key keys = 7;` |
    | `Common.KeyOrBuilder` | `getKeysOrBuilder(int index)` `repeated .protocol.Key keys = 7;` |
    | `java.util.List<? extends Common.KeyOrBuilder>` | `getKeysOrBuilderList()` `repeated .protocol.Key keys = 7;` |
    | `com.google.protobuf.ByteString` | `getOperations()` 1 bit 1 contract |
    | `int` | `getParentId()` `int32 parent_id = 5;` |
    | `java.lang.String` | `getPermissionName()` `string permission_name = 3;` |
    | `com.google.protobuf.ByteString` | `getPermissionNameBytes()` `string permission_name = 3;` |
    | `long` | `getThreshold()` `int64 threshold = 4;` |
    | `Common.Permission.PermissionType` | `getType()` `.protocol.Permission.PermissionType type = 1;` |
    | `int` | `getTypeValue()` `.protocol.Permission.PermissionType type = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getTypeValue

      ```
      int getTypeValue()
      ```

      `.protocol.Permission.PermissionType type = 1;`

      Returns:
      :   The enum numeric value on the wire for type.
    - #### getType

      ```
      Common.Permission.PermissionType getType()
      ```

      `.protocol.Permission.PermissionType type = 1;`

      Returns:
      :   The type.
    - #### getId

      ```
      int getId()
      ```

      ```
       Owner id=0, Witness id=1, Active id start by 2
      ```

      `int32 id = 2;`

      Returns:
      :   The id.
    - #### getPermissionName

      ```
      java.lang.String getPermissionName()
      ```

      `string permission_name = 3;`

      Returns:
      :   The permissionName.
    - #### getPermissionNameBytes

      ```
      com.google.protobuf.ByteString getPermissionNameBytes()
      ```

      `string permission_name = 3;`

      Returns:
      :   The bytes for permissionName.
    - #### getThreshold

      ```
      long getThreshold()
      ```

      `int64 threshold = 4;`

      Returns:
      :   The threshold.
    - #### getParentId

      ```
      int getParentId()
      ```

      `int32 parent_id = 5;`

      Returns:
      :   The parentId.
    - #### getOperations

      ```
      com.google.protobuf.ByteString getOperations()
      ```

      ```
       1 bit 1 contract
      ```

      `bytes operations = 6;`

      Returns:
      :   The operations.
    - #### getKeysList

      ```
      java.util.List<Common.Key> getKeysList()
      ```

      `repeated .protocol.Key keys = 7;`
    - #### getKeys

      ```
      Common.Key getKeys(int index)
      ```

      `repeated .protocol.Key keys = 7;`
    - #### getKeysCount

      ```
      int getKeysCount()
      ```

      `repeated .protocol.Key keys = 7;`
    - #### getKeysOrBuilderList

      ```
      java.util.List<? extends Common.KeyOrBuilder> getKeysOrBuilderList()
      ```

      `repeated .protocol.Key keys = 7;`
    - #### getKeysOrBuilder

      ```
      Common.KeyOrBuilder getKeysOrBuilder(int index)
      ```

      `repeated .protocol.Key keys = 7;`