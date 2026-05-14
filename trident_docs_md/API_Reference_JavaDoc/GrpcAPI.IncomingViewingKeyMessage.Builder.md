

org.tron.trident.api

## Class GrpcAPI.IncomingViewingKeyMessage.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.IncomingViewingKeyMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.IncomingViewingKeyMessage.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.IncomingViewingKeyMessage.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.IncomingViewingKeyMessageOrBuilder](../../../../org/tron/trident/api/GrpcAPI.IncomingViewingKeyMessageOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.IncomingViewingKeyMessage](../../../../org/tron/trident/api/GrpcAPI.IncomingViewingKeyMessage.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.IncomingViewingKeyMessage.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyMessage.Builder>
  implements GrpcAPI.IncomingViewingKeyMessageOrBuilder
  ```

  Protobuf type `protocol.IncomingViewingKeyMessage`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.IncomingViewingKeyMessage.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.IncomingViewingKeyMessage` | `build()` |
    | `GrpcAPI.IncomingViewingKeyMessage` | `buildPartial()` |
    | `GrpcAPI.IncomingViewingKeyMessage.Builder` | `clear()` |
    | `GrpcAPI.IncomingViewingKeyMessage.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.IncomingViewingKeyMessage.Builder` | `clearIvk()` `bytes ivk = 1;` |
    | `GrpcAPI.IncomingViewingKeyMessage.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.IncomingViewingKeyMessage.Builder` | `clone()` |
    | `GrpcAPI.IncomingViewingKeyMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getIvk()` `bytes ivk = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.IncomingViewingKeyMessage.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.IncomingViewingKeyMessage.Builder` | `mergeFrom(GrpcAPI.IncomingViewingKeyMessage other)` |
    | `GrpcAPI.IncomingViewingKeyMessage.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.IncomingViewingKeyMessage.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.IncomingViewingKeyMessage.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.IncomingViewingKeyMessage.Builder` | `setIvk(com.google.protobuf.ByteString value)` `bytes ivk = 1;` |
    | `GrpcAPI.IncomingViewingKeyMessage.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.IncomingViewingKeyMessage.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyMessage.Builder>`
    - #### clear

      ```
      public GrpcAPI.IncomingViewingKeyMessage.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyMessage.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyMessage.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.IncomingViewingKeyMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.IncomingViewingKeyMessage build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.IncomingViewingKeyMessage buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.IncomingViewingKeyMessage.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyMessage.Builder>`
    - #### setField

      ```
      public GrpcAPI.IncomingViewingKeyMessage.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyMessage.Builder>`
    - #### clearField

      ```
      public GrpcAPI.IncomingViewingKeyMessage.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyMessage.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.IncomingViewingKeyMessage.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyMessage.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.IncomingViewingKeyMessage.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                        int index,
                                                                        java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyMessage.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.IncomingViewingKeyMessage.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                        java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.IncomingViewingKeyMessage.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.IncomingViewingKeyMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.IncomingViewingKeyMessage.Builder mergeFrom(GrpcAPI.IncomingViewingKeyMessage other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.IncomingViewingKeyMessage.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                 com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                          throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.IncomingViewingKeyMessage.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getIvk

      ```
      public com.google.protobuf.ByteString getIvk()
      ```

      `bytes ivk = 1;`

      Specified by:
      :   `getIvk` in interface `GrpcAPI.IncomingViewingKeyMessageOrBuilder`

      Returns:
      :   The ivk.
    - #### setIvk

      ```
      public GrpcAPI.IncomingViewingKeyMessage.Builder setIvk(com.google.protobuf.ByteString value)
      ```

      `bytes ivk = 1;`

      Parameters:
      :   `value` - The ivk to set.

      Returns:
      :   This builder for chaining.
    - #### clearIvk

      ```
      public GrpcAPI.IncomingViewingKeyMessage.Builder clearIvk()
      ```

      `bytes ivk = 1;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.IncomingViewingKeyMessage.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyMessage.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.IncomingViewingKeyMessage.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyMessage.Builder>`