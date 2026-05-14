

org.tron.trident.api

## Class GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.CanDelegatedMaxSizeResponseMessageOrBuilder](../../../../org/tron/trident/api/GrpcAPI.CanDelegatedMaxSizeResponseMessageOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.CanDelegatedMaxSizeResponseMessage](../../../../org/tron/trident/api/GrpcAPI.CanDelegatedMaxSizeResponseMessage.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder>
  implements GrpcAPI.CanDelegatedMaxSizeResponseMessageOrBuilder
  ```

  Protobuf type `protocol.CanDelegatedMaxSizeResponseMessage`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.CanDelegatedMaxSizeResponseMessage` | `build()` |
    | `GrpcAPI.CanDelegatedMaxSizeResponseMessage` | `buildPartial()` |
    | `GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder` | `clear()` |
    | `GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder` | `clearMaxSize()` `int64 max_size = 1;` |
    | `GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder` | `clone()` |
    | `GrpcAPI.CanDelegatedMaxSizeResponseMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getMaxSize()` `int64 max_size = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder` | `mergeFrom(GrpcAPI.CanDelegatedMaxSizeResponseMessage other)` |
    | `GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder` | `setMaxSize(long value)` `int64 max_size = 1;` |
    | `GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder>`
    - #### clear

      ```
      public GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.CanDelegatedMaxSizeResponseMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.CanDelegatedMaxSizeResponseMessage build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.CanDelegatedMaxSizeResponseMessage buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder>`
    - #### setField

      ```
      public GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                         java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder>`
    - #### clearField

      ```
      public GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                 int index,
                                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder mergeFrom(GrpcAPI.CanDelegatedMaxSizeResponseMessage other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                   throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getMaxSize

      ```
      public long getMaxSize()
      ```

      `int64 max_size = 1;`

      Specified by:
      :   `getMaxSize` in interface `GrpcAPI.CanDelegatedMaxSizeResponseMessageOrBuilder`

      Returns:
      :   The maxSize.
    - #### setMaxSize

      ```
      public GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder setMaxSize(long value)
      ```

      `int64 max_size = 1;`

      Parameters:
      :   `value` - The maxSize to set.

      Returns:
      :   This builder for chaining.
    - #### clearMaxSize

      ```
      public GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder clearMaxSize()
      ```

      `int64 max_size = 1;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder>`