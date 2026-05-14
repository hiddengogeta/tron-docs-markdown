

org.tron.trident.proto

## Class Common.Key.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Common.Key.Builder](../../../../org/tron/trident/proto/Common.Key.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Common.Key.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Common.KeyOrBuilder](../../../../org/tron/trident/proto/Common.KeyOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Common.Key](../../../../org/tron/trident/proto/Common.Key.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Common.Key.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Common.Key.Builder>
  implements Common.KeyOrBuilder
  ```

  Protobuf type `protocol.Key`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Common.Key.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Common.Key` | `build()` |
    | `Common.Key` | `buildPartial()` |
    | `Common.Key.Builder` | `clear()` |
    | `Common.Key.Builder` | `clearAddress()` `bytes address = 1;` |
    | `Common.Key.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Common.Key.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Common.Key.Builder` | `clearWeight()` `int64 weight = 2;` |
    | `Common.Key.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getAddress()` `bytes address = 1;` |
    | `Common.Key` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getWeight()` `int64 weight = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Common.Key.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Common.Key.Builder` | `mergeFrom(Common.Key other)` |
    | `Common.Key.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Common.Key.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Common.Key.Builder` | `setAddress(com.google.protobuf.ByteString value)` `bytes address = 1;` |
    | `Common.Key.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Common.Key.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Common.Key.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Common.Key.Builder` | `setWeight(long value)` `int64 weight = 2;` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Key.Builder>`
    - #### clear

      ```
      public Common.Key.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Key.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Key.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Common.Key getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Common.Key build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Common.Key buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Common.Key.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Key.Builder>`
    - #### setField

      ```
      public Common.Key.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                         java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Key.Builder>`
    - #### clearField

      ```
      public Common.Key.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Key.Builder>`
    - #### clearOneof

      ```
      public Common.Key.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Key.Builder>`
    - #### setRepeatedField

      ```
      public Common.Key.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                 int index,
                                                 java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Key.Builder>`
    - #### addRepeatedField

      ```
      public Common.Key.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                 java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Key.Builder>`
    - #### mergeFrom

      ```
      public Common.Key.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Common.Key.Builder>`
    - #### mergeFrom

      ```
      public Common.Key.Builder mergeFrom(Common.Key other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Key.Builder>`
    - #### mergeFrom

      ```
      public Common.Key.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                   throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Common.Key.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getAddress

      ```
      public com.google.protobuf.ByteString getAddress()
      ```

      `bytes address = 1;`

      Specified by:
      :   `getAddress` in interface `Common.KeyOrBuilder`

      Returns:
      :   The address.
    - #### setAddress

      ```
      public Common.Key.Builder setAddress(com.google.protobuf.ByteString value)
      ```

      `bytes address = 1;`

      Parameters:
      :   `value` - The address to set.

      Returns:
      :   This builder for chaining.
    - #### clearAddress

      ```
      public Common.Key.Builder clearAddress()
      ```

      `bytes address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getWeight

      ```
      public long getWeight()
      ```

      `int64 weight = 2;`

      Specified by:
      :   `getWeight` in interface `Common.KeyOrBuilder`

      Returns:
      :   The weight.
    - #### setWeight

      ```
      public Common.Key.Builder setWeight(long value)
      ```

      `int64 weight = 2;`

      Parameters:
      :   `value` - The weight to set.

      Returns:
      :   This builder for chaining.
    - #### clearWeight

      ```
      public Common.Key.Builder clearWeight()
      ```

      `int64 weight = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Common.Key.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Key.Builder>`
    - #### mergeUnknownFields

      ```
      public final Common.Key.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Key.Builder>`