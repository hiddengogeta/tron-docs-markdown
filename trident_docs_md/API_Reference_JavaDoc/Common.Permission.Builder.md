

org.tron.trident.proto

## Class Common.Permission.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Common.Permission.Builder](../../../../org/tron/trident/proto/Common.Permission.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Common.Permission.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Common.PermissionOrBuilder](../../../../org/tron/trident/proto/Common.PermissionOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Common.Permission](../../../../org/tron/trident/proto/Common.Permission.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Common.Permission.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Common.Permission.Builder>
  implements Common.PermissionOrBuilder
  ```

  Protobuf type `protocol.Permission`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Common.Permission.Builder` | `addAllKeys(java.lang.Iterable<? extends Common.Key> values)` `repeated .protocol.Key keys = 7;` |
    | `Common.Permission.Builder` | `addKeys(Common.Key.Builder builderForValue)` `repeated .protocol.Key keys = 7;` |
    | `Common.Permission.Builder` | `addKeys(Common.Key value)` `repeated .protocol.Key keys = 7;` |
    | `Common.Permission.Builder` | `addKeys(int index, Common.Key.Builder builderForValue)` `repeated .protocol.Key keys = 7;` |
    | `Common.Permission.Builder` | `addKeys(int index, Common.Key value)` `repeated .protocol.Key keys = 7;` |
    | `Common.Key.Builder` | `addKeysBuilder()` `repeated .protocol.Key keys = 7;` |
    | `Common.Key.Builder` | `addKeysBuilder(int index)` `repeated .protocol.Key keys = 7;` |
    | `Common.Permission.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Common.Permission` | `build()` |
    | `Common.Permission` | `buildPartial()` |
    | `Common.Permission.Builder` | `clear()` |
    | `Common.Permission.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Common.Permission.Builder` | `clearId()` Owner id=0, Witness id=1, Active id start by 2 |
    | `Common.Permission.Builder` | `clearKeys()` `repeated .protocol.Key keys = 7;` |
    | `Common.Permission.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Common.Permission.Builder` | `clearOperations()` 1 bit 1 contract |
    | `Common.Permission.Builder` | `clearParentId()` `int32 parent_id = 5;` |
    | `Common.Permission.Builder` | `clearPermissionName()` `string permission_name = 3;` |
    | `Common.Permission.Builder` | `clearThreshold()` `int64 threshold = 4;` |
    | `Common.Permission.Builder` | `clearType()` `.protocol.Permission.PermissionType type = 1;` |
    | `Common.Permission.Builder` | `clone()` |
    | `Common.Permission` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `int` | `getId()` Owner id=0, Witness id=1, Active id start by 2 |
    | `Common.Key` | `getKeys(int index)` `repeated .protocol.Key keys = 7;` |
    | `Common.Key.Builder` | `getKeysBuilder(int index)` `repeated .protocol.Key keys = 7;` |
    | `java.util.List<Common.Key.Builder>` | `getKeysBuilderList()` `repeated .protocol.Key keys = 7;` |
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
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Common.Permission.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Common.Permission.Builder` | `mergeFrom(Common.Permission other)` |
    | `Common.Permission.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Common.Permission.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Common.Permission.Builder` | `removeKeys(int index)` `repeated .protocol.Key keys = 7;` |
    | `Common.Permission.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Common.Permission.Builder` | `setId(int value)` Owner id=0, Witness id=1, Active id start by 2 |
    | `Common.Permission.Builder` | `setKeys(int index, Common.Key.Builder builderForValue)` `repeated .protocol.Key keys = 7;` |
    | `Common.Permission.Builder` | `setKeys(int index, Common.Key value)` `repeated .protocol.Key keys = 7;` |
    | `Common.Permission.Builder` | `setOperations(com.google.protobuf.ByteString value)` 1 bit 1 contract |
    | `Common.Permission.Builder` | `setParentId(int value)` `int32 parent_id = 5;` |
    | `Common.Permission.Builder` | `setPermissionName(java.lang.String value)` `string permission_name = 3;` |
    | `Common.Permission.Builder` | `setPermissionNameBytes(com.google.protobuf.ByteString value)` `string permission_name = 3;` |
    | `Common.Permission.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Common.Permission.Builder` | `setThreshold(long value)` `int64 threshold = 4;` |
    | `Common.Permission.Builder` | `setType(Common.Permission.PermissionType value)` `.protocol.Permission.PermissionType type = 1;` |
    | `Common.Permission.Builder` | `setTypeValue(int value)` `.protocol.Permission.PermissionType type = 1;` |
    | `Common.Permission.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Permission.Builder>`
    - #### clear

      ```
      public Common.Permission.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Permission.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Permission.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Common.Permission getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Common.Permission build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Common.Permission buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Common.Permission.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Permission.Builder>`
    - #### setField

      ```
      public Common.Permission.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Permission.Builder>`
    - #### clearField

      ```
      public Common.Permission.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Permission.Builder>`
    - #### clearOneof

      ```
      public Common.Permission.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Permission.Builder>`
    - #### setRepeatedField

      ```
      public Common.Permission.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                        int index,
                                                        java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Permission.Builder>`
    - #### addRepeatedField

      ```
      public Common.Permission.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                        java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Permission.Builder>`
    - #### mergeFrom

      ```
      public Common.Permission.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Common.Permission.Builder>`
    - #### mergeFrom

      ```
      public Common.Permission.Builder mergeFrom(Common.Permission other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Permission.Builder>`
    - #### mergeFrom

      ```
      public Common.Permission.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                 com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                          throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Common.Permission.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getTypeValue

      ```
      public int getTypeValue()
      ```

      `.protocol.Permission.PermissionType type = 1;`

      Specified by:
      :   `getTypeValue` in interface `Common.PermissionOrBuilder`

      Returns:
      :   The enum numeric value on the wire for type.
    - #### setTypeValue

      ```
      public Common.Permission.Builder setTypeValue(int value)
      ```

      `.protocol.Permission.PermissionType type = 1;`

      Parameters:
      :   `value` - The enum numeric value on the wire for type to set.

      Returns:
      :   This builder for chaining.
    - #### getType

      ```
      public Common.Permission.PermissionType getType()
      ```

      `.protocol.Permission.PermissionType type = 1;`

      Specified by:
      :   `getType` in interface `Common.PermissionOrBuilder`

      Returns:
      :   The type.
    - #### setType

      ```
      public Common.Permission.Builder setType(Common.Permission.PermissionType value)
      ```

      `.protocol.Permission.PermissionType type = 1;`

      Parameters:
      :   `value` - The type to set.

      Returns:
      :   This builder for chaining.
    - #### clearType

      ```
      public Common.Permission.Builder clearType()
      ```

      `.protocol.Permission.PermissionType type = 1;`

      Returns:
      :   This builder for chaining.
    - #### getId

      ```
      public int getId()
      ```

      ```
       Owner id=0, Witness id=1, Active id start by 2
      ```

      `int32 id = 2;`

      Specified by:
      :   `getId` in interface `Common.PermissionOrBuilder`

      Returns:
      :   The id.
    - #### setId

      ```
      public Common.Permission.Builder setId(int value)
      ```

      ```
       Owner id=0, Witness id=1, Active id start by 2
      ```

      `int32 id = 2;`

      Parameters:
      :   `value` - The id to set.

      Returns:
      :   This builder for chaining.
    - #### clearId

      ```
      public Common.Permission.Builder clearId()
      ```

      ```
       Owner id=0, Witness id=1, Active id start by 2
      ```

      `int32 id = 2;`

      Returns:
      :   This builder for chaining.
    - #### getPermissionName

      ```
      public java.lang.String getPermissionName()
      ```

      `string permission_name = 3;`

      Specified by:
      :   `getPermissionName` in interface `Common.PermissionOrBuilder`

      Returns:
      :   The permissionName.
    - #### getPermissionNameBytes

      ```
      public com.google.protobuf.ByteString getPermissionNameBytes()
      ```

      `string permission_name = 3;`

      Specified by:
      :   `getPermissionNameBytes` in interface `Common.PermissionOrBuilder`

      Returns:
      :   The bytes for permissionName.
    - #### setPermissionName

      ```
      public Common.Permission.Builder setPermissionName(java.lang.String value)
      ```

      `string permission_name = 3;`

      Parameters:
      :   `value` - The permissionName to set.

      Returns:
      :   This builder for chaining.
    - #### clearPermissionName

      ```
      public Common.Permission.Builder clearPermissionName()
      ```

      `string permission_name = 3;`

      Returns:
      :   This builder for chaining.
    - #### setPermissionNameBytes

      ```
      public Common.Permission.Builder setPermissionNameBytes(com.google.protobuf.ByteString value)
      ```

      `string permission_name = 3;`

      Parameters:
      :   `value` - The bytes for permissionName to set.

      Returns:
      :   This builder for chaining.
    - #### getThreshold

      ```
      public long getThreshold()
      ```

      `int64 threshold = 4;`

      Specified by:
      :   `getThreshold` in interface `Common.PermissionOrBuilder`

      Returns:
      :   The threshold.
    - #### setThreshold

      ```
      public Common.Permission.Builder setThreshold(long value)
      ```

      `int64 threshold = 4;`

      Parameters:
      :   `value` - The threshold to set.

      Returns:
      :   This builder for chaining.
    - #### clearThreshold

      ```
      public Common.Permission.Builder clearThreshold()
      ```

      `int64 threshold = 4;`

      Returns:
      :   This builder for chaining.
    - #### getParentId

      ```
      public int getParentId()
      ```

      `int32 parent_id = 5;`

      Specified by:
      :   `getParentId` in interface `Common.PermissionOrBuilder`

      Returns:
      :   The parentId.
    - #### setParentId

      ```
      public Common.Permission.Builder setParentId(int value)
      ```

      `int32 parent_id = 5;`

      Parameters:
      :   `value` - The parentId to set.

      Returns:
      :   This builder for chaining.
    - #### clearParentId

      ```
      public Common.Permission.Builder clearParentId()
      ```

      `int32 parent_id = 5;`

      Returns:
      :   This builder for chaining.
    - #### getOperations

      ```
      public com.google.protobuf.ByteString getOperations()
      ```

      ```
       1 bit 1 contract
      ```

      `bytes operations = 6;`

      Specified by:
      :   `getOperations` in interface `Common.PermissionOrBuilder`

      Returns:
      :   The operations.
    - #### setOperations

      ```
      public Common.Permission.Builder setOperations(com.google.protobuf.ByteString value)
      ```

      ```
       1 bit 1 contract
      ```

      `bytes operations = 6;`

      Parameters:
      :   `value` - The operations to set.

      Returns:
      :   This builder for chaining.
    - #### clearOperations

      ```
      public Common.Permission.Builder clearOperations()
      ```

      ```
       1 bit 1 contract
      ```

      `bytes operations = 6;`

      Returns:
      :   This builder for chaining.
    - #### getKeysList

      ```
      public java.util.List<Common.Key> getKeysList()
      ```

      `repeated .protocol.Key keys = 7;`

      Specified by:
      :   `getKeysList` in interface `Common.PermissionOrBuilder`
    - #### getKeysCount

      ```
      public int getKeysCount()
      ```

      `repeated .protocol.Key keys = 7;`

      Specified by:
      :   `getKeysCount` in interface `Common.PermissionOrBuilder`
    - #### getKeys

      ```
      public Common.Key getKeys(int index)
      ```

      `repeated .protocol.Key keys = 7;`

      Specified by:
      :   `getKeys` in interface `Common.PermissionOrBuilder`
    - #### setKeys

      ```
      public Common.Permission.Builder setKeys(int index,
                                               Common.Key value)
      ```

      `repeated .protocol.Key keys = 7;`
    - #### setKeys

      ```
      public Common.Permission.Builder setKeys(int index,
                                               Common.Key.Builder builderForValue)
      ```

      `repeated .protocol.Key keys = 7;`
    - #### addKeys

      ```
      public Common.Permission.Builder addKeys(Common.Key value)
      ```

      `repeated .protocol.Key keys = 7;`
    - #### addKeys

      ```
      public Common.Permission.Builder addKeys(int index,
                                               Common.Key value)
      ```

      `repeated .protocol.Key keys = 7;`
    - #### addKeys

      ```
      public Common.Permission.Builder addKeys(Common.Key.Builder builderForValue)
      ```

      `repeated .protocol.Key keys = 7;`
    - #### addKeys

      ```
      public Common.Permission.Builder addKeys(int index,
                                               Common.Key.Builder builderForValue)
      ```

      `repeated .protocol.Key keys = 7;`
    - #### addAllKeys

      ```
      public Common.Permission.Builder addAllKeys(java.lang.Iterable<? extends Common.Key> values)
      ```

      `repeated .protocol.Key keys = 7;`
    - #### clearKeys

      ```
      public Common.Permission.Builder clearKeys()
      ```

      `repeated .protocol.Key keys = 7;`
    - #### removeKeys

      ```
      public Common.Permission.Builder removeKeys(int index)
      ```

      `repeated .protocol.Key keys = 7;`
    - #### getKeysBuilder

      ```
      public Common.Key.Builder getKeysBuilder(int index)
      ```

      `repeated .protocol.Key keys = 7;`
    - #### getKeysOrBuilder

      ```
      public Common.KeyOrBuilder getKeysOrBuilder(int index)
      ```

      `repeated .protocol.Key keys = 7;`

      Specified by:
      :   `getKeysOrBuilder` in interface `Common.PermissionOrBuilder`
    - #### getKeysOrBuilderList

      ```
      public java.util.List<? extends Common.KeyOrBuilder> getKeysOrBuilderList()
      ```

      `repeated .protocol.Key keys = 7;`

      Specified by:
      :   `getKeysOrBuilderList` in interface `Common.PermissionOrBuilder`
    - #### addKeysBuilder

      ```
      public Common.Key.Builder addKeysBuilder()
      ```

      `repeated .protocol.Key keys = 7;`
    - #### addKeysBuilder

      ```
      public Common.Key.Builder addKeysBuilder(int index)
      ```

      `repeated .protocol.Key keys = 7;`
    - #### getKeysBuilderList

      ```
      public java.util.List<Common.Key.Builder> getKeysBuilderList()
      ```

      `repeated .protocol.Key keys = 7;`
    - #### setUnknownFields

      ```
      public final Common.Permission.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Permission.Builder>`
    - #### mergeUnknownFields

      ```
      public final Common.Permission.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Permission.Builder>`