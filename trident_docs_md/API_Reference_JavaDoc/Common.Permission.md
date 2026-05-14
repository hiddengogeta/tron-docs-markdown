

org.tron.trident.proto

## Class Common.Permission

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Common.Permission

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Common.PermissionOrBuilder](../../../../org/tron/trident/proto/Common.PermissionOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Common](../../../../org/tron/trident/proto/Common.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Common.Permission
  extends com.google.protobuf.GeneratedMessageV3
  implements Common.PermissionOrBuilder
  ```

  Protobuf type `protocol.Permission`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Common.Permission)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Common.Permission.Builder` Protobuf type `protocol.Permission` |
    | `static class` | `Common.Permission.PermissionType` Protobuf enum `protocol.Permission.PermissionType` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `ID_FIELD_NUMBER` |
    | `static int` | `KEYS_FIELD_NUMBER` |
    | `static int` | `OPERATIONS_FIELD_NUMBER` |
    | `static int` | `PARENT_ID_FIELD_NUMBER` |
    | `static int` | `PERMISSION_NAME_FIELD_NUMBER` |
    | `static int` | `THRESHOLD_FIELD_NUMBER` |
    | `static int` | `TYPE_FIELD_NUMBER` |

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
    | `static Common.Permission` | `getDefaultInstance()` |
    | `Common.Permission` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `int` | `getId()` Owner id=0, Witness id=1, Active id start by 2 |
    | `Common.Key` | `getKeys(int index)` `repeated .protocol.Key keys = 7;` |
    | `int` | `getKeysCount()` `repeated .protocol.Key keys = 7;` |
    | `java.util.List<Common.Key>` | `getKeysList()` `repeated .protocol.Key keys = 7;` |
    | `Common.KeyOrBuilder` | `getKeysOrBuilder(int index)` `repeated .protocol.Key keys = 7;` |
    | `java.util.List<? extends Common.KeyOrBuilder>` | `getKeysOrBuilderList()` `repeated .protocol.Key keys = 7;` |
    | `com.google.protobuf.ByteString` | `getOperations()` 1 bit 1 contract |
    | `int` | `getParentId()` `int32 parent_id = 5;` |
    | `com.google.protobuf.Parser<Common.Permission>` | `getParserForType()` |
    | `java.lang.String` | `getPermissionName()` `string permission_name = 3;` |
    | `com.google.protobuf.ByteString` | `getPermissionNameBytes()` `string permission_name = 3;` |
    | `int` | `getSerializedSize()` |
    | `long` | `getThreshold()` `int64 threshold = 4;` |
    | `Common.Permission.PermissionType` | `getType()` `.protocol.Permission.PermissionType type = 1;` |
    | `int` | `getTypeValue()` `.protocol.Permission.PermissionType type = 1;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Common.Permission.Builder` | `newBuilder()` |
    | `static Common.Permission.Builder` | `newBuilder(Common.Permission prototype)` |
    | `Common.Permission.Builder` | `newBuilderForType()` |
    | `protected Common.Permission.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Common.Permission` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Common.Permission` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.Permission` | `parseFrom(byte[] data)` |
    | `static Common.Permission` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.Permission` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Common.Permission` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.Permission` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Common.Permission` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.Permission` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Common.Permission` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.Permission` | `parseFrom(java.io.InputStream input)` |
    | `static Common.Permission` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Common.Permission>` | `parser()` |
    | `Common.Permission.Builder` | `toBuilder()` |
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

    - #### TYPE\_FIELD\_NUMBER

      ```
      public static final int TYPE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.Permission.TYPE_FIELD_NUMBER)
    - #### ID\_FIELD\_NUMBER

      ```
      public static final int ID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.Permission.ID_FIELD_NUMBER)
    - #### PERMISSION\_NAME\_FIELD\_NUMBER

      ```
      public static final int PERMISSION_NAME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.Permission.PERMISSION_NAME_FIELD_NUMBER)
    - #### THRESHOLD\_FIELD\_NUMBER

      ```
      public static final int THRESHOLD_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.Permission.THRESHOLD_FIELD_NUMBER)
    - #### PARENT\_ID\_FIELD\_NUMBER

      ```
      public static final int PARENT_ID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.Permission.PARENT_ID_FIELD_NUMBER)
    - #### OPERATIONS\_FIELD\_NUMBER

      ```
      public static final int OPERATIONS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.Permission.OPERATIONS_FIELD_NUMBER)
    - #### KEYS\_FIELD\_NUMBER

      ```
      public static final int KEYS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.Permission.KEYS_FIELD_NUMBER)
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
    - #### getTypeValue

      ```
      public int getTypeValue()
      ```

      `.protocol.Permission.PermissionType type = 1;`

      Specified by:
      :   `getTypeValue` in interface `Common.PermissionOrBuilder`

      Returns:
      :   The enum numeric value on the wire for type.
    - #### getType

      ```
      public Common.Permission.PermissionType getType()
      ```

      `.protocol.Permission.PermissionType type = 1;`

      Specified by:
      :   `getType` in interface `Common.PermissionOrBuilder`

      Returns:
      :   The type.
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
    - #### getThreshold

      ```
      public long getThreshold()
      ```

      `int64 threshold = 4;`

      Specified by:
      :   `getThreshold` in interface `Common.PermissionOrBuilder`

      Returns:
      :   The threshold.
    - #### getParentId

      ```
      public int getParentId()
      ```

      `int32 parent_id = 5;`

      Specified by:
      :   `getParentId` in interface `Common.PermissionOrBuilder`

      Returns:
      :   The parentId.
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
    - #### getKeysList

      ```
      public java.util.List<Common.Key> getKeysList()
      ```

      `repeated .protocol.Key keys = 7;`

      Specified by:
      :   `getKeysList` in interface `Common.PermissionOrBuilder`
    - #### getKeysOrBuilderList

      ```
      public java.util.List<? extends Common.KeyOrBuilder> getKeysOrBuilderList()
      ```

      `repeated .protocol.Key keys = 7;`

      Specified by:
      :   `getKeysOrBuilderList` in interface `Common.PermissionOrBuilder`
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
    - #### getKeysOrBuilder

      ```
      public Common.KeyOrBuilder getKeysOrBuilder(int index)
      ```

      `repeated .protocol.Key keys = 7;`

      Specified by:
      :   `getKeysOrBuilder` in interface `Common.PermissionOrBuilder`
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
      public static Common.Permission parseFrom(java.nio.ByteBuffer data)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.Permission parseFrom(java.nio.ByteBuffer data,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.Permission parseFrom(com.google.protobuf.ByteString data)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.Permission parseFrom(com.google.protobuf.ByteString data,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.Permission parseFrom(byte[] data)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.Permission parseFrom(byte[] data,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.Permission parseFrom(java.io.InputStream input)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Common.Permission parseFrom(java.io.InputStream input,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Common.Permission parseDelimitedFrom(java.io.InputStream input)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Common.Permission parseDelimitedFrom(java.io.InputStream input,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Common.Permission parseFrom(com.google.protobuf.CodedInputStream input)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Common.Permission parseFrom(com.google.protobuf.CodedInputStream input,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Common.Permission.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Common.Permission.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Common.Permission.Builder newBuilder(Common.Permission prototype)
      ```
    - #### toBuilder

      ```
      public Common.Permission.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Common.Permission.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Common.Permission getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Common.Permission> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Common.Permission> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Common.Permission getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`