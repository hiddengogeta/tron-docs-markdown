

org.tron.trident.api

## Class GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.CanDelegatedMaxSizeRequestMessageOrBuilder](../../../../org/tron/trident/api/GrpcAPI.CanDelegatedMaxSizeRequestMessageOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.CanDelegatedMaxSizeRequestMessage](../../../../org/tron/trident/api/GrpcAPI.CanDelegatedMaxSizeRequestMessage.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder>
  implements GrpcAPI.CanDelegatedMaxSizeRequestMessageOrBuilder
  ```

  Protobuf type `protocol.CanDelegatedMaxSizeRequestMessage`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.CanDelegatedMaxSizeRequestMessage` | `build()` |
    | `GrpcAPI.CanDelegatedMaxSizeRequestMessage` | `buildPartial()` |
    | `GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder` | `clear()` |
    | `GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder` | `clearOwnerAddress()` `bytes owner_address = 2;` |
    | `GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder` | `clearType()` `int32 type = 1;` |
    | `GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder` | `clone()` |
    | `GrpcAPI.CanDelegatedMaxSizeRequestMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 2;` |
    | `int` | `getType()` `int32 type = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder` | `mergeFrom(GrpcAPI.CanDelegatedMaxSizeRequestMessage other)` |
    | `GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 2;` |
    | `GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder` | `setType(int value)` `int32 type = 1;` |
    | `GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder>`
    - #### clear

      ```
      public GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.CanDelegatedMaxSizeRequestMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.CanDelegatedMaxSizeRequestMessage build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.CanDelegatedMaxSizeRequestMessage buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder>`
    - #### setField

      ```
      public GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                        java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder>`
    - #### clearField

      ```
      public GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                int index,
                                                                                java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder mergeFrom(GrpcAPI.CanDelegatedMaxSizeRequestMessage other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                  throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getType

      ```
      public int getType()
      ```

      `int32 type = 1;`

      Specified by:
      :   `getType` in interface `GrpcAPI.CanDelegatedMaxSizeRequestMessageOrBuilder`

      Returns:
      :   The type.
    - #### setType

      ```
      public GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder setType(int value)
      ```

      `int32 type = 1;`

      Parameters:
      :   `value` - The type to set.

      Returns:
      :   This builder for chaining.
    - #### clearType

      ```
      public GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder clearType()
      ```

      `int32 type = 1;`

      Returns:
      :   This builder for chaining.
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 2;`

      Specified by:
      :   `getOwnerAddress` in interface `GrpcAPI.CanDelegatedMaxSizeRequestMessageOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 2;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeRequestMessage.Builder>`