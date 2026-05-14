

org.tron.trident.proto

## Class Common.AccountId.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Common.AccountId.Builder](../../../../org/tron/trident/proto/Common.AccountId.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Common.AccountId.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Common.AccountIdOrBuilder](../../../../org/tron/trident/proto/Common.AccountIdOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Common.AccountId](../../../../org/tron/trident/proto/Common.AccountId.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Common.AccountId.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Common.AccountId.Builder>
  implements Common.AccountIdOrBuilder
  ```

  Protobuf type `protocol.AccountId`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Common.AccountId.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Common.AccountId` | `build()` |
    | `Common.AccountId` | `buildPartial()` |
    | `Common.AccountId.Builder` | `clear()` |
    | `Common.AccountId.Builder` | `clearAddress()` `bytes address = 2;` |
    | `Common.AccountId.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Common.AccountId.Builder` | `clearName()` `bytes name = 1;` |
    | `Common.AccountId.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Common.AccountId.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getAddress()` `bytes address = 2;` |
    | `Common.AccountId` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getName()` `bytes name = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Common.AccountId.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Common.AccountId.Builder` | `mergeFrom(Common.AccountId other)` |
    | `Common.AccountId.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Common.AccountId.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Common.AccountId.Builder` | `setAddress(com.google.protobuf.ByteString value)` `bytes address = 2;` |
    | `Common.AccountId.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Common.AccountId.Builder` | `setName(com.google.protobuf.ByteString value)` `bytes name = 1;` |
    | `Common.AccountId.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Common.AccountId.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.AccountId.Builder>`
    - #### clear

      ```
      public Common.AccountId.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.AccountId.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.AccountId.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Common.AccountId getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Common.AccountId build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Common.AccountId buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Common.AccountId.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.AccountId.Builder>`
    - #### setField

      ```
      public Common.AccountId.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                               java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.AccountId.Builder>`
    - #### clearField

      ```
      public Common.AccountId.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.AccountId.Builder>`
    - #### clearOneof

      ```
      public Common.AccountId.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.AccountId.Builder>`
    - #### setRepeatedField

      ```
      public Common.AccountId.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       int index,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.AccountId.Builder>`
    - #### addRepeatedField

      ```
      public Common.AccountId.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.AccountId.Builder>`
    - #### mergeFrom

      ```
      public Common.AccountId.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Common.AccountId.Builder>`
    - #### mergeFrom

      ```
      public Common.AccountId.Builder mergeFrom(Common.AccountId other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.AccountId.Builder>`
    - #### mergeFrom

      ```
      public Common.AccountId.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Common.AccountId.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getName

      ```
      public com.google.protobuf.ByteString getName()
      ```

      `bytes name = 1;`

      Specified by:
      :   `getName` in interface `Common.AccountIdOrBuilder`

      Returns:
      :   The name.
    - #### setName

      ```
      public Common.AccountId.Builder setName(com.google.protobuf.ByteString value)
      ```

      `bytes name = 1;`

      Parameters:
      :   `value` - The name to set.

      Returns:
      :   This builder for chaining.
    - #### clearName

      ```
      public Common.AccountId.Builder clearName()
      ```

      `bytes name = 1;`

      Returns:
      :   This builder for chaining.
    - #### getAddress

      ```
      public com.google.protobuf.ByteString getAddress()
      ```

      `bytes address = 2;`

      Specified by:
      :   `getAddress` in interface `Common.AccountIdOrBuilder`

      Returns:
      :   The address.
    - #### setAddress

      ```
      public Common.AccountId.Builder setAddress(com.google.protobuf.ByteString value)
      ```

      `bytes address = 2;`

      Parameters:
      :   `value` - The address to set.

      Returns:
      :   This builder for chaining.
    - #### clearAddress

      ```
      public Common.AccountId.Builder clearAddress()
      ```

      `bytes address = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Common.AccountId.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.AccountId.Builder>`
    - #### mergeUnknownFields

      ```
      public final Common.AccountId.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.AccountId.Builder>`