

org.tron.trident.api

## Class GrpcAPI.ViewingKeyMessage.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.ViewingKeyMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.ViewingKeyMessage.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.ViewingKeyMessage.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.ViewingKeyMessageOrBuilder](../../../../org/tron/trident/api/GrpcAPI.ViewingKeyMessageOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.ViewingKeyMessage](../../../../org/tron/trident/api/GrpcAPI.ViewingKeyMessage.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.ViewingKeyMessage.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ViewingKeyMessage.Builder>
  implements GrpcAPI.ViewingKeyMessageOrBuilder
  ```

  ```
   - Shielded TRC20
  ```

  Protobuf type `protocol.ViewingKeyMessage`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.ViewingKeyMessage.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.ViewingKeyMessage` | `build()` |
    | `GrpcAPI.ViewingKeyMessage` | `buildPartial()` |
    | `GrpcAPI.ViewingKeyMessage.Builder` | `clear()` |
    | `GrpcAPI.ViewingKeyMessage.Builder` | `clearAk()` `bytes ak = 1;` |
    | `GrpcAPI.ViewingKeyMessage.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.ViewingKeyMessage.Builder` | `clearNk()` `bytes nk = 2;` |
    | `GrpcAPI.ViewingKeyMessage.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.ViewingKeyMessage.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getAk()` `bytes ak = 1;` |
    | `GrpcAPI.ViewingKeyMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getNk()` `bytes nk = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.ViewingKeyMessage.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.ViewingKeyMessage.Builder` | `mergeFrom(GrpcAPI.ViewingKeyMessage other)` |
    | `GrpcAPI.ViewingKeyMessage.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.ViewingKeyMessage.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.ViewingKeyMessage.Builder` | `setAk(com.google.protobuf.ByteString value)` `bytes ak = 1;` |
    | `GrpcAPI.ViewingKeyMessage.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.ViewingKeyMessage.Builder` | `setNk(com.google.protobuf.ByteString value)` `bytes nk = 2;` |
    | `GrpcAPI.ViewingKeyMessage.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.ViewingKeyMessage.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ViewingKeyMessage.Builder>`
    - #### clear

      ```
      public GrpcAPI.ViewingKeyMessage.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ViewingKeyMessage.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ViewingKeyMessage.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.ViewingKeyMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.ViewingKeyMessage build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.ViewingKeyMessage buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.ViewingKeyMessage.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ViewingKeyMessage.Builder>`
    - #### setField

      ```
      public GrpcAPI.ViewingKeyMessage.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                        java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ViewingKeyMessage.Builder>`
    - #### clearField

      ```
      public GrpcAPI.ViewingKeyMessage.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ViewingKeyMessage.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.ViewingKeyMessage.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ViewingKeyMessage.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.ViewingKeyMessage.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                int index,
                                                                java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ViewingKeyMessage.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.ViewingKeyMessage.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ViewingKeyMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.ViewingKeyMessage.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.ViewingKeyMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.ViewingKeyMessage.Builder mergeFrom(GrpcAPI.ViewingKeyMessage other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ViewingKeyMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.ViewingKeyMessage.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.ViewingKeyMessage.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getAk

      ```
      public com.google.protobuf.ByteString getAk()
      ```

      `bytes ak = 1;`

      Specified by:
      :   `getAk` in interface `GrpcAPI.ViewingKeyMessageOrBuilder`

      Returns:
      :   The ak.
    - #### setAk

      ```
      public GrpcAPI.ViewingKeyMessage.Builder setAk(com.google.protobuf.ByteString value)
      ```

      `bytes ak = 1;`

      Parameters:
      :   `value` - The ak to set.

      Returns:
      :   This builder for chaining.
    - #### clearAk

      ```
      public GrpcAPI.ViewingKeyMessage.Builder clearAk()
      ```

      `bytes ak = 1;`

      Returns:
      :   This builder for chaining.
    - #### getNk

      ```
      public com.google.protobuf.ByteString getNk()
      ```

      `bytes nk = 2;`

      Specified by:
      :   `getNk` in interface `GrpcAPI.ViewingKeyMessageOrBuilder`

      Returns:
      :   The nk.
    - #### setNk

      ```
      public GrpcAPI.ViewingKeyMessage.Builder setNk(com.google.protobuf.ByteString value)
      ```

      `bytes nk = 2;`

      Parameters:
      :   `value` - The nk to set.

      Returns:
      :   This builder for chaining.
    - #### clearNk

      ```
      public GrpcAPI.ViewingKeyMessage.Builder clearNk()
      ```

      `bytes nk = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.ViewingKeyMessage.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ViewingKeyMessage.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.ViewingKeyMessage.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ViewingKeyMessage.Builder>`