

org.tron.trident.api

## Class GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.GetAvailableUnfreezeCountResponseMessageOrBuilder](../../../../org/tron/trident/api/GrpcAPI.GetAvailableUnfreezeCountResponseMessageOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.GetAvailableUnfreezeCountResponseMessage](../../../../org/tron/trident/api/GrpcAPI.GetAvailableUnfreezeCountResponseMessage.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder>
  implements GrpcAPI.GetAvailableUnfreezeCountResponseMessageOrBuilder
  ```

  Protobuf type `protocol.GetAvailableUnfreezeCountResponseMessage`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.GetAvailableUnfreezeCountResponseMessage` | `build()` |
    | `GrpcAPI.GetAvailableUnfreezeCountResponseMessage` | `buildPartial()` |
    | `GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder` | `clear()` |
    | `GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder` | `clearCount()` `int64 count = 1;` |
    | `GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder` | `clone()` |
    | `long` | `getCount()` `int64 count = 1;` |
    | `GrpcAPI.GetAvailableUnfreezeCountResponseMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder` | `mergeFrom(GrpcAPI.GetAvailableUnfreezeCountResponseMessage other)` |
    | `GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder` | `setCount(long value)` `int64 count = 1;` |
    | `GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder>`
    - #### clear

      ```
      public GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.GetAvailableUnfreezeCountResponseMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.GetAvailableUnfreezeCountResponseMessage build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.GetAvailableUnfreezeCountResponseMessage buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder>`
    - #### setField

      ```
      public GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder>`
    - #### clearField

      ```
      public GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                       int index,
                                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder mergeFrom(GrpcAPI.GetAvailableUnfreezeCountResponseMessage other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                         throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getCount

      ```
      public long getCount()
      ```

      `int64 count = 1;`

      Specified by:
      :   `getCount` in interface `GrpcAPI.GetAvailableUnfreezeCountResponseMessageOrBuilder`

      Returns:
      :   The count.
    - #### setCount

      ```
      public GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder setCount(long value)
      ```

      `int64 count = 1;`

      Parameters:
      :   `value` - The count to set.

      Returns:
      :   This builder for chaining.
    - #### clearCount

      ```
      public GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder clearCount()
      ```

      `int64 count = 1;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.GetAvailableUnfreezeCountResponseMessage.Builder>`