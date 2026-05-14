

org.tron.trident.api

## Class GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.IncomingViewingKeyDiversifierMessageOrBuilder](../../../../org/tron/trident/api/GrpcAPI.IncomingViewingKeyDiversifierMessageOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.IncomingViewingKeyDiversifierMessage](../../../../org/tron/trident/api/GrpcAPI.IncomingViewingKeyDiversifierMessage.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder>
  implements GrpcAPI.IncomingViewingKeyDiversifierMessageOrBuilder
  ```

  ```
   What's the fucking API design
  ```

  Protobuf type `protocol.IncomingViewingKeyDiversifierMessage`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.IncomingViewingKeyDiversifierMessage` | `build()` |
    | `GrpcAPI.IncomingViewingKeyDiversifierMessage` | `buildPartial()` |
    | `GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder` | `clear()` |
    | `GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder` | `clearD()` `.protocol.DiversifierMessage d = 2;` |
    | `GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder` | `clearIvk()` `.protocol.IncomingViewingKeyMessage ivk = 1;` |
    | `GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder` | `clone()` |
    | `GrpcAPI.DiversifierMessage` | `getD()` `.protocol.DiversifierMessage d = 2;` |
    | `GrpcAPI.DiversifierMessage.Builder` | `getDBuilder()` `.protocol.DiversifierMessage d = 2;` |
    | `GrpcAPI.IncomingViewingKeyDiversifierMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `GrpcAPI.DiversifierMessageOrBuilder` | `getDOrBuilder()` `.protocol.DiversifierMessage d = 2;` |
    | `GrpcAPI.IncomingViewingKeyMessage` | `getIvk()` `.protocol.IncomingViewingKeyMessage ivk = 1;` |
    | `GrpcAPI.IncomingViewingKeyMessage.Builder` | `getIvkBuilder()` `.protocol.IncomingViewingKeyMessage ivk = 1;` |
    | `GrpcAPI.IncomingViewingKeyMessageOrBuilder` | `getIvkOrBuilder()` `.protocol.IncomingViewingKeyMessage ivk = 1;` |
    | `boolean` | `hasD()` `.protocol.DiversifierMessage d = 2;` |
    | `boolean` | `hasIvk()` `.protocol.IncomingViewingKeyMessage ivk = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder` | `mergeD(GrpcAPI.DiversifierMessage value)` `.protocol.DiversifierMessage d = 2;` |
    | `GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder` | `mergeFrom(GrpcAPI.IncomingViewingKeyDiversifierMessage other)` |
    | `GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder` | `mergeIvk(GrpcAPI.IncomingViewingKeyMessage value)` `.protocol.IncomingViewingKeyMessage ivk = 1;` |
    | `GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder` | `setD(GrpcAPI.DiversifierMessage.Builder builderForValue)` `.protocol.DiversifierMessage d = 2;` |
    | `GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder` | `setD(GrpcAPI.DiversifierMessage value)` `.protocol.DiversifierMessage d = 2;` |
    | `GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder` | `setIvk(GrpcAPI.IncomingViewingKeyMessage.Builder builderForValue)` `.protocol.IncomingViewingKeyMessage ivk = 1;` |
    | `GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder` | `setIvk(GrpcAPI.IncomingViewingKeyMessage value)` `.protocol.IncomingViewingKeyMessage ivk = 1;` |
    | `GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder>`
    - #### clear

      ```
      public GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.IncomingViewingKeyDiversifierMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.IncomingViewingKeyDiversifierMessage build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.IncomingViewingKeyDiversifierMessage buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder>`
    - #### setField

      ```
      public GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                           java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder>`
    - #### clearField

      ```
      public GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                   int index,
                                                                                   java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                   java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder mergeFrom(GrpcAPI.IncomingViewingKeyDiversifierMessage other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                     throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### hasIvk

      ```
      public boolean hasIvk()
      ```

      `.protocol.IncomingViewingKeyMessage ivk = 1;`

      Specified by:
      :   `hasIvk` in interface `GrpcAPI.IncomingViewingKeyDiversifierMessageOrBuilder`

      Returns:
      :   Whether the ivk field is set.
    - #### getIvk

      ```
      public GrpcAPI.IncomingViewingKeyMessage getIvk()
      ```

      `.protocol.IncomingViewingKeyMessage ivk = 1;`

      Specified by:
      :   `getIvk` in interface `GrpcAPI.IncomingViewingKeyDiversifierMessageOrBuilder`

      Returns:
      :   The ivk.
    - #### setIvk

      ```
      public GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder setIvk(GrpcAPI.IncomingViewingKeyMessage value)
      ```

      `.protocol.IncomingViewingKeyMessage ivk = 1;`
    - #### setIvk

      ```
      public GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder setIvk(GrpcAPI.IncomingViewingKeyMessage.Builder builderForValue)
      ```

      `.protocol.IncomingViewingKeyMessage ivk = 1;`
    - #### mergeIvk

      ```
      public GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder mergeIvk(GrpcAPI.IncomingViewingKeyMessage value)
      ```

      `.protocol.IncomingViewingKeyMessage ivk = 1;`
    - #### clearIvk

      ```
      public GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder clearIvk()
      ```

      `.protocol.IncomingViewingKeyMessage ivk = 1;`
    - #### getIvkBuilder

      ```
      public GrpcAPI.IncomingViewingKeyMessage.Builder getIvkBuilder()
      ```

      `.protocol.IncomingViewingKeyMessage ivk = 1;`
    - #### getIvkOrBuilder

      ```
      public GrpcAPI.IncomingViewingKeyMessageOrBuilder getIvkOrBuilder()
      ```

      `.protocol.IncomingViewingKeyMessage ivk = 1;`

      Specified by:
      :   `getIvkOrBuilder` in interface `GrpcAPI.IncomingViewingKeyDiversifierMessageOrBuilder`
    - #### hasD

      ```
      public boolean hasD()
      ```

      `.protocol.DiversifierMessage d = 2;`

      Specified by:
      :   `hasD` in interface `GrpcAPI.IncomingViewingKeyDiversifierMessageOrBuilder`

      Returns:
      :   Whether the d field is set.
    - #### getD

      ```
      public GrpcAPI.DiversifierMessage getD()
      ```

      `.protocol.DiversifierMessage d = 2;`

      Specified by:
      :   `getD` in interface `GrpcAPI.IncomingViewingKeyDiversifierMessageOrBuilder`

      Returns:
      :   The d.
    - #### setD

      ```
      public GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder setD(GrpcAPI.DiversifierMessage value)
      ```

      `.protocol.DiversifierMessage d = 2;`
    - #### setD

      ```
      public GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder setD(GrpcAPI.DiversifierMessage.Builder builderForValue)
      ```

      `.protocol.DiversifierMessage d = 2;`
    - #### mergeD

      ```
      public GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder mergeD(GrpcAPI.DiversifierMessage value)
      ```

      `.protocol.DiversifierMessage d = 2;`
    - #### clearD

      ```
      public GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder clearD()
      ```

      `.protocol.DiversifierMessage d = 2;`
    - #### getDBuilder

      ```
      public GrpcAPI.DiversifierMessage.Builder getDBuilder()
      ```

      `.protocol.DiversifierMessage d = 2;`
    - #### getDOrBuilder

      ```
      public GrpcAPI.DiversifierMessageOrBuilder getDOrBuilder()
      ```

      `.protocol.DiversifierMessage d = 2;`

      Specified by:
      :   `getDOrBuilder` in interface `GrpcAPI.IncomingViewingKeyDiversifierMessageOrBuilder`
    - #### setUnknownFields

      ```
      public final GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder>`