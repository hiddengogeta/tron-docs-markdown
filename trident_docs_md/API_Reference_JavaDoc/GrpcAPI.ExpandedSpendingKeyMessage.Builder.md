

org.tron.trident.api

## Class GrpcAPI.ExpandedSpendingKeyMessage.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.ExpandedSpendingKeyMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.ExpandedSpendingKeyMessage.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.ExpandedSpendingKeyMessage.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.ExpandedSpendingKeyMessageOrBuilder](../../../../org/tron/trident/api/GrpcAPI.ExpandedSpendingKeyMessageOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.ExpandedSpendingKeyMessage](../../../../org/tron/trident/api/GrpcAPI.ExpandedSpendingKeyMessage.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.ExpandedSpendingKeyMessage.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ExpandedSpendingKeyMessage.Builder>
  implements GrpcAPI.ExpandedSpendingKeyMessageOrBuilder
  ```

  Protobuf type `protocol.ExpandedSpendingKeyMessage`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.ExpandedSpendingKeyMessage.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.ExpandedSpendingKeyMessage` | `build()` |
    | `GrpcAPI.ExpandedSpendingKeyMessage` | `buildPartial()` |
    | `GrpcAPI.ExpandedSpendingKeyMessage.Builder` | `clear()` |
    | `GrpcAPI.ExpandedSpendingKeyMessage.Builder` | `clearAsk()` `bytes ask = 1;` |
    | `GrpcAPI.ExpandedSpendingKeyMessage.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.ExpandedSpendingKeyMessage.Builder` | `clearNsk()` `bytes nsk = 2;` |
    | `GrpcAPI.ExpandedSpendingKeyMessage.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.ExpandedSpendingKeyMessage.Builder` | `clearOvk()` `bytes ovk = 3;` |
    | `GrpcAPI.ExpandedSpendingKeyMessage.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getAsk()` `bytes ask = 1;` |
    | `GrpcAPI.ExpandedSpendingKeyMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getNsk()` `bytes nsk = 2;` |
    | `com.google.protobuf.ByteString` | `getOvk()` `bytes ovk = 3;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.ExpandedSpendingKeyMessage.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.ExpandedSpendingKeyMessage.Builder` | `mergeFrom(GrpcAPI.ExpandedSpendingKeyMessage other)` |
    | `GrpcAPI.ExpandedSpendingKeyMessage.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.ExpandedSpendingKeyMessage.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.ExpandedSpendingKeyMessage.Builder` | `setAsk(com.google.protobuf.ByteString value)` `bytes ask = 1;` |
    | `GrpcAPI.ExpandedSpendingKeyMessage.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.ExpandedSpendingKeyMessage.Builder` | `setNsk(com.google.protobuf.ByteString value)` `bytes nsk = 2;` |
    | `GrpcAPI.ExpandedSpendingKeyMessage.Builder` | `setOvk(com.google.protobuf.ByteString value)` `bytes ovk = 3;` |
    | `GrpcAPI.ExpandedSpendingKeyMessage.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.ExpandedSpendingKeyMessage.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ExpandedSpendingKeyMessage.Builder>`
    - #### clear

      ```
      public GrpcAPI.ExpandedSpendingKeyMessage.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ExpandedSpendingKeyMessage.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ExpandedSpendingKeyMessage.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.ExpandedSpendingKeyMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.ExpandedSpendingKeyMessage build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.ExpandedSpendingKeyMessage buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.ExpandedSpendingKeyMessage.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ExpandedSpendingKeyMessage.Builder>`
    - #### setField

      ```
      public GrpcAPI.ExpandedSpendingKeyMessage.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ExpandedSpendingKeyMessage.Builder>`
    - #### clearField

      ```
      public GrpcAPI.ExpandedSpendingKeyMessage.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ExpandedSpendingKeyMessage.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.ExpandedSpendingKeyMessage.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ExpandedSpendingKeyMessage.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.ExpandedSpendingKeyMessage.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                         int index,
                                                                         java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ExpandedSpendingKeyMessage.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.ExpandedSpendingKeyMessage.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                         java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ExpandedSpendingKeyMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.ExpandedSpendingKeyMessage.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.ExpandedSpendingKeyMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.ExpandedSpendingKeyMessage.Builder mergeFrom(GrpcAPI.ExpandedSpendingKeyMessage other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ExpandedSpendingKeyMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.ExpandedSpendingKeyMessage.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                  com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                           throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.ExpandedSpendingKeyMessage.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getAsk

      ```
      public com.google.protobuf.ByteString getAsk()
      ```

      `bytes ask = 1;`

      Specified by:
      :   `getAsk` in interface `GrpcAPI.ExpandedSpendingKeyMessageOrBuilder`

      Returns:
      :   The ask.
    - #### setAsk

      ```
      public GrpcAPI.ExpandedSpendingKeyMessage.Builder setAsk(com.google.protobuf.ByteString value)
      ```

      `bytes ask = 1;`

      Parameters:
      :   `value` - The ask to set.

      Returns:
      :   This builder for chaining.
    - #### clearAsk

      ```
      public GrpcAPI.ExpandedSpendingKeyMessage.Builder clearAsk()
      ```

      `bytes ask = 1;`

      Returns:
      :   This builder for chaining.
    - #### getNsk

      ```
      public com.google.protobuf.ByteString getNsk()
      ```

      `bytes nsk = 2;`

      Specified by:
      :   `getNsk` in interface `GrpcAPI.ExpandedSpendingKeyMessageOrBuilder`

      Returns:
      :   The nsk.
    - #### setNsk

      ```
      public GrpcAPI.ExpandedSpendingKeyMessage.Builder setNsk(com.google.protobuf.ByteString value)
      ```

      `bytes nsk = 2;`

      Parameters:
      :   `value` - The nsk to set.

      Returns:
      :   This builder for chaining.
    - #### clearNsk

      ```
      public GrpcAPI.ExpandedSpendingKeyMessage.Builder clearNsk()
      ```

      `bytes nsk = 2;`

      Returns:
      :   This builder for chaining.
    - #### getOvk

      ```
      public com.google.protobuf.ByteString getOvk()
      ```

      `bytes ovk = 3;`

      Specified by:
      :   `getOvk` in interface `GrpcAPI.ExpandedSpendingKeyMessageOrBuilder`

      Returns:
      :   The ovk.
    - #### setOvk

      ```
      public GrpcAPI.ExpandedSpendingKeyMessage.Builder setOvk(com.google.protobuf.ByteString value)
      ```

      `bytes ovk = 3;`

      Parameters:
      :   `value` - The ovk to set.

      Returns:
      :   This builder for chaining.
    - #### clearOvk

      ```
      public GrpcAPI.ExpandedSpendingKeyMessage.Builder clearOvk()
      ```

      `bytes ovk = 3;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.ExpandedSpendingKeyMessage.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ExpandedSpendingKeyMessage.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.ExpandedSpendingKeyMessage.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ExpandedSpendingKeyMessage.Builder>`