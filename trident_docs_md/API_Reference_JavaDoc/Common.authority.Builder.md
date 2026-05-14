

org.tron.trident.proto

## Class Common.authority.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Common.authority.Builder](../../../../org/tron/trident/proto/Common.authority.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Common.authority.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Common.authorityOrBuilder](../../../../org/tron/trident/proto/Common.authorityOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Common.authority](../../../../org/tron/trident/proto/Common.authority.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Common.authority.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Common.authority.Builder>
  implements Common.authorityOrBuilder
  ```

  Protobuf type `protocol.authority`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Common.authority.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Common.authority` | `build()` |
    | `Common.authority` | `buildPartial()` |
    | `Common.authority.Builder` | `clear()` |
    | `Common.authority.Builder` | `clearAccount()` `.protocol.AccountId account = 1;` |
    | `Common.authority.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Common.authority.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Common.authority.Builder` | `clearPermissionName()` `bytes permission_name = 2;` |
    | `Common.authority.Builder` | `clone()` |
    | `Common.AccountId` | `getAccount()` `.protocol.AccountId account = 1;` |
    | `Common.AccountId.Builder` | `getAccountBuilder()` `.protocol.AccountId account = 1;` |
    | `Common.AccountIdOrBuilder` | `getAccountOrBuilder()` `.protocol.AccountId account = 1;` |
    | `Common.authority` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getPermissionName()` `bytes permission_name = 2;` |
    | `boolean` | `hasAccount()` `.protocol.AccountId account = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Common.authority.Builder` | `mergeAccount(Common.AccountId value)` `.protocol.AccountId account = 1;` |
    | `Common.authority.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Common.authority.Builder` | `mergeFrom(Common.authority other)` |
    | `Common.authority.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Common.authority.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Common.authority.Builder` | `setAccount(Common.AccountId.Builder builderForValue)` `.protocol.AccountId account = 1;` |
    | `Common.authority.Builder` | `setAccount(Common.AccountId value)` `.protocol.AccountId account = 1;` |
    | `Common.authority.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Common.authority.Builder` | `setPermissionName(com.google.protobuf.ByteString value)` `bytes permission_name = 2;` |
    | `Common.authority.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Common.authority.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.authority.Builder>`
    - #### clear

      ```
      public Common.authority.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.authority.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.authority.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Common.authority getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Common.authority build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Common.authority buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Common.authority.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.authority.Builder>`
    - #### setField

      ```
      public Common.authority.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                               java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.authority.Builder>`
    - #### clearField

      ```
      public Common.authority.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.authority.Builder>`
    - #### clearOneof

      ```
      public Common.authority.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.authority.Builder>`
    - #### setRepeatedField

      ```
      public Common.authority.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       int index,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.authority.Builder>`
    - #### addRepeatedField

      ```
      public Common.authority.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.authority.Builder>`
    - #### mergeFrom

      ```
      public Common.authority.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Common.authority.Builder>`
    - #### mergeFrom

      ```
      public Common.authority.Builder mergeFrom(Common.authority other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.authority.Builder>`
    - #### mergeFrom

      ```
      public Common.authority.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Common.authority.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### hasAccount

      ```
      public boolean hasAccount()
      ```

      `.protocol.AccountId account = 1;`

      Specified by:
      :   `hasAccount` in interface `Common.authorityOrBuilder`

      Returns:
      :   Whether the account field is set.
    - #### getAccount

      ```
      public Common.AccountId getAccount()
      ```

      `.protocol.AccountId account = 1;`

      Specified by:
      :   `getAccount` in interface `Common.authorityOrBuilder`

      Returns:
      :   The account.
    - #### setAccount

      ```
      public Common.authority.Builder setAccount(Common.AccountId value)
      ```

      `.protocol.AccountId account = 1;`
    - #### setAccount

      ```
      public Common.authority.Builder setAccount(Common.AccountId.Builder builderForValue)
      ```

      `.protocol.AccountId account = 1;`
    - #### mergeAccount

      ```
      public Common.authority.Builder mergeAccount(Common.AccountId value)
      ```

      `.protocol.AccountId account = 1;`
    - #### clearAccount

      ```
      public Common.authority.Builder clearAccount()
      ```

      `.protocol.AccountId account = 1;`
    - #### getAccountBuilder

      ```
      public Common.AccountId.Builder getAccountBuilder()
      ```

      `.protocol.AccountId account = 1;`
    - #### getAccountOrBuilder

      ```
      public Common.AccountIdOrBuilder getAccountOrBuilder()
      ```

      `.protocol.AccountId account = 1;`

      Specified by:
      :   `getAccountOrBuilder` in interface `Common.authorityOrBuilder`
    - #### getPermissionName

      ```
      public com.google.protobuf.ByteString getPermissionName()
      ```

      `bytes permission_name = 2;`

      Specified by:
      :   `getPermissionName` in interface `Common.authorityOrBuilder`

      Returns:
      :   The permissionName.
    - #### setPermissionName

      ```
      public Common.authority.Builder setPermissionName(com.google.protobuf.ByteString value)
      ```

      `bytes permission_name = 2;`

      Parameters:
      :   `value` - The permissionName to set.

      Returns:
      :   This builder for chaining.
    - #### clearPermissionName

      ```
      public Common.authority.Builder clearPermissionName()
      ```

      `bytes permission_name = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Common.authority.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.authority.Builder>`
    - #### mergeUnknownFields

      ```
      public final Common.authority.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.authority.Builder>`