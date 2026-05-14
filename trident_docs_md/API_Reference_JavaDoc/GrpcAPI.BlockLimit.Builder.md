

org.tron.trident.api

## Class GrpcAPI.BlockLimit.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.BlockLimit.Builder](../../../../org/tron/trident/api/GrpcAPI.BlockLimit.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.BlockLimit.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.BlockLimitOrBuilder](../../../../org/tron/trident/api/GrpcAPI.BlockLimitOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.BlockLimit](../../../../org/tron/trident/api/GrpcAPI.BlockLimit.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.BlockLimit.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockLimit.Builder>
  implements GrpcAPI.BlockLimitOrBuilder
  ```

  Protobuf type `protocol.BlockLimit`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.BlockLimit.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.BlockLimit` | `build()` |
    | `GrpcAPI.BlockLimit` | `buildPartial()` |
    | `GrpcAPI.BlockLimit.Builder` | `clear()` |
    | `GrpcAPI.BlockLimit.Builder` | `clearEndNum()` `int64 endNum = 2;` |
    | `GrpcAPI.BlockLimit.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.BlockLimit.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.BlockLimit.Builder` | `clearStartNum()` `int64 startNum = 1;` |
    | `GrpcAPI.BlockLimit.Builder` | `clone()` |
    | `GrpcAPI.BlockLimit` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getEndNum()` `int64 endNum = 2;` |
    | `long` | `getStartNum()` `int64 startNum = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.BlockLimit.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.BlockLimit.Builder` | `mergeFrom(GrpcAPI.BlockLimit other)` |
    | `GrpcAPI.BlockLimit.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.BlockLimit.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.BlockLimit.Builder` | `setEndNum(long value)` `int64 endNum = 2;` |
    | `GrpcAPI.BlockLimit.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.BlockLimit.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.BlockLimit.Builder` | `setStartNum(long value)` `int64 startNum = 1;` |
    | `GrpcAPI.BlockLimit.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockLimit.Builder>`
    - #### clear

      ```
      public GrpcAPI.BlockLimit.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockLimit.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockLimit.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.BlockLimit getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.BlockLimit build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.BlockLimit buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.BlockLimit.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockLimit.Builder>`
    - #### setField

      ```
      public GrpcAPI.BlockLimit.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                 java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockLimit.Builder>`
    - #### clearField

      ```
      public GrpcAPI.BlockLimit.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockLimit.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.BlockLimit.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockLimit.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.BlockLimit.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                         int index,
                                                         java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockLimit.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.BlockLimit.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                         java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockLimit.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.BlockLimit.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.BlockLimit.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.BlockLimit.Builder mergeFrom(GrpcAPI.BlockLimit other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockLimit.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.BlockLimit.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                  com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                           throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.BlockLimit.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getStartNum

      ```
      public long getStartNum()
      ```

      `int64 startNum = 1;`

      Specified by:
      :   `getStartNum` in interface `GrpcAPI.BlockLimitOrBuilder`

      Returns:
      :   The startNum.
    - #### setStartNum

      ```
      public GrpcAPI.BlockLimit.Builder setStartNum(long value)
      ```

      `int64 startNum = 1;`

      Parameters:
      :   `value` - The startNum to set.

      Returns:
      :   This builder for chaining.
    - #### clearStartNum

      ```
      public GrpcAPI.BlockLimit.Builder clearStartNum()
      ```

      `int64 startNum = 1;`

      Returns:
      :   This builder for chaining.
    - #### getEndNum

      ```
      public long getEndNum()
      ```

      `int64 endNum = 2;`

      Specified by:
      :   `getEndNum` in interface `GrpcAPI.BlockLimitOrBuilder`

      Returns:
      :   The endNum.
    - #### setEndNum

      ```
      public GrpcAPI.BlockLimit.Builder setEndNum(long value)
      ```

      `int64 endNum = 2;`

      Parameters:
      :   `value` - The endNum to set.

      Returns:
      :   This builder for chaining.
    - #### clearEndNum

      ```
      public GrpcAPI.BlockLimit.Builder clearEndNum()
      ```

      `int64 endNum = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.BlockLimit.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockLimit.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.BlockLimit.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockLimit.Builder>`