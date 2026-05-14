

org.tron.trident.api

## Class GrpcAPI.PaginatedMessage.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.PaginatedMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.PaginatedMessage.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.PaginatedMessage.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.PaginatedMessageOrBuilder](../../../../org/tron/trident/api/GrpcAPI.PaginatedMessageOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.PaginatedMessage](../../../../org/tron/trident/api/GrpcAPI.PaginatedMessage.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.PaginatedMessage.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaginatedMessage.Builder>
  implements GrpcAPI.PaginatedMessageOrBuilder
  ```

  ```
   FLAW: Paginated APIs are usless.
  ```

  Protobuf type `protocol.PaginatedMessage`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.PaginatedMessage.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.PaginatedMessage` | `build()` |
    | `GrpcAPI.PaginatedMessage` | `buildPartial()` |
    | `GrpcAPI.PaginatedMessage.Builder` | `clear()` |
    | `GrpcAPI.PaginatedMessage.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.PaginatedMessage.Builder` | `clearLimit()` `int64 limit = 2;` |
    | `GrpcAPI.PaginatedMessage.Builder` | `clearOffset()` `int64 offset = 1;` |
    | `GrpcAPI.PaginatedMessage.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.PaginatedMessage.Builder` | `clone()` |
    | `GrpcAPI.PaginatedMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getLimit()` `int64 limit = 2;` |
    | `long` | `getOffset()` `int64 offset = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.PaginatedMessage.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.PaginatedMessage.Builder` | `mergeFrom(GrpcAPI.PaginatedMessage other)` |
    | `GrpcAPI.PaginatedMessage.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.PaginatedMessage.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.PaginatedMessage.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.PaginatedMessage.Builder` | `setLimit(long value)` `int64 limit = 2;` |
    | `GrpcAPI.PaginatedMessage.Builder` | `setOffset(long value)` `int64 offset = 1;` |
    | `GrpcAPI.PaginatedMessage.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.PaginatedMessage.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaginatedMessage.Builder>`
    - #### clear

      ```
      public GrpcAPI.PaginatedMessage.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaginatedMessage.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaginatedMessage.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.PaginatedMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.PaginatedMessage build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.PaginatedMessage buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.PaginatedMessage.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaginatedMessage.Builder>`
    - #### setField

      ```
      public GrpcAPI.PaginatedMessage.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaginatedMessage.Builder>`
    - #### clearField

      ```
      public GrpcAPI.PaginatedMessage.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaginatedMessage.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.PaginatedMessage.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaginatedMessage.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.PaginatedMessage.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               int index,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaginatedMessage.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.PaginatedMessage.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaginatedMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.PaginatedMessage.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.PaginatedMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.PaginatedMessage.Builder mergeFrom(GrpcAPI.PaginatedMessage other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaginatedMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.PaginatedMessage.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                 throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.PaginatedMessage.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOffset

      ```
      public long getOffset()
      ```

      `int64 offset = 1;`

      Specified by:
      :   `getOffset` in interface `GrpcAPI.PaginatedMessageOrBuilder`

      Returns:
      :   The offset.
    - #### setOffset

      ```
      public GrpcAPI.PaginatedMessage.Builder setOffset(long value)
      ```

      `int64 offset = 1;`

      Parameters:
      :   `value` - The offset to set.

      Returns:
      :   This builder for chaining.
    - #### clearOffset

      ```
      public GrpcAPI.PaginatedMessage.Builder clearOffset()
      ```

      `int64 offset = 1;`

      Returns:
      :   This builder for chaining.
    - #### getLimit

      ```
      public long getLimit()
      ```

      `int64 limit = 2;`

      Specified by:
      :   `getLimit` in interface `GrpcAPI.PaginatedMessageOrBuilder`

      Returns:
      :   The limit.
    - #### setLimit

      ```
      public GrpcAPI.PaginatedMessage.Builder setLimit(long value)
      ```

      `int64 limit = 2;`

      Parameters:
      :   `value` - The limit to set.

      Returns:
      :   This builder for chaining.
    - #### clearLimit

      ```
      public GrpcAPI.PaginatedMessage.Builder clearLimit()
      ```

      `int64 limit = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.PaginatedMessage.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaginatedMessage.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.PaginatedMessage.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaginatedMessage.Builder>`