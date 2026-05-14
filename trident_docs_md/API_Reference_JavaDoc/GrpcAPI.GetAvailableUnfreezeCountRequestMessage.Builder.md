

org.tron.trident.api

## Class GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.GetAvailableUnfreezeCountRequestMessageOrBuilder](../../../../org/tron/trident/api/GrpcAPI.GetAvailableUnfreezeCountRequestMessageOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.GetAvailableUnfreezeCountRequestMessage](../../../../org/tron/trident/api/GrpcAPI.GetAvailableUnfreezeCountRequestMessage.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder>
  implements GrpcAPI.GetAvailableUnfreezeCountRequestMessageOrBuilder
  ```

  Protobuf type `protocol.GetAvailableUnfreezeCountRequestMessage`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.GetAvailableUnfreezeCountRequestMessage` | `build()` |
    | `GrpcAPI.GetAvailableUnfreezeCountRequestMessage` | `buildPartial()` |
    | `GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder` | `clear()` |
    | `GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder` | `clone()` |
    | `GrpcAPI.GetAvailableUnfreezeCountRequestMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder` | `mergeFrom(GrpcAPI.GetAvailableUnfreezeCountRequestMessage other)` |
    | `GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder>`
    - #### clear

      ```
      public GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.GetAvailableUnfreezeCountRequestMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.GetAvailableUnfreezeCountRequestMessage build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.GetAvailableUnfreezeCountRequestMessage buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder>`
    - #### setField

      ```
      public GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                              java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder>`
    - #### clearField

      ```
      public GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                      int index,
                                                                                      java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                      java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder mergeFrom(GrpcAPI.GetAvailableUnfreezeCountRequestMessage other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                        throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `GrpcAPI.GetAvailableUnfreezeCountRequestMessageOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountRequestMessage.Builder>`