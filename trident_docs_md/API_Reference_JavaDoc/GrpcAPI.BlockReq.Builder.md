

org.tron.trident.api

## Class GrpcAPI.BlockReq.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.BlockReq.Builder](../../../../org/tron/trident/api/GrpcAPI.BlockReq.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.BlockReq.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.BlockReqOrBuilder](../../../../org/tron/trident/api/GrpcAPI.BlockReqOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.BlockReq](../../../../org/tron/trident/api/GrpcAPI.BlockReq.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.BlockReq.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockReq.Builder>
  implements GrpcAPI.BlockReqOrBuilder
  ```

  Protobuf type `protocol.BlockReq`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.BlockReq.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.BlockReq` | `build()` |
    | `GrpcAPI.BlockReq` | `buildPartial()` |
    | `GrpcAPI.BlockReq.Builder` | `clear()` |
    | `GrpcAPI.BlockReq.Builder` | `clearDetail()` `bool detail = 2;` |
    | `GrpcAPI.BlockReq.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.BlockReq.Builder` | `clearIdOrNum()` `string id_or_num = 1;` |
    | `GrpcAPI.BlockReq.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.BlockReq.Builder` | `clone()` |
    | `GrpcAPI.BlockReq` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `boolean` | `getDetail()` `bool detail = 2;` |
    | `java.lang.String` | `getIdOrNum()` `string id_or_num = 1;` |
    | `com.google.protobuf.ByteString` | `getIdOrNumBytes()` `string id_or_num = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.BlockReq.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.BlockReq.Builder` | `mergeFrom(GrpcAPI.BlockReq other)` |
    | `GrpcAPI.BlockReq.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.BlockReq.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.BlockReq.Builder` | `setDetail(boolean value)` `bool detail = 2;` |
    | `GrpcAPI.BlockReq.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.BlockReq.Builder` | `setIdOrNum(java.lang.String value)` `string id_or_num = 1;` |
    | `GrpcAPI.BlockReq.Builder` | `setIdOrNumBytes(com.google.protobuf.ByteString value)` `string id_or_num = 1;` |
    | `GrpcAPI.BlockReq.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.BlockReq.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockReq.Builder>`
    - #### clear

      ```
      public GrpcAPI.BlockReq.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockReq.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockReq.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.BlockReq getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.BlockReq build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.BlockReq buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.BlockReq.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockReq.Builder>`
    - #### setField

      ```
      public GrpcAPI.BlockReq.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                               java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockReq.Builder>`
    - #### clearField

      ```
      public GrpcAPI.BlockReq.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockReq.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.BlockReq.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockReq.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.BlockReq.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       int index,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockReq.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.BlockReq.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockReq.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.BlockReq.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.BlockReq.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.BlockReq.Builder mergeFrom(GrpcAPI.BlockReq other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockReq.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.BlockReq.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.BlockReq.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getIdOrNum

      ```
      public java.lang.String getIdOrNum()
      ```

      `string id_or_num = 1;`

      Specified by:
      :   `getIdOrNum` in interface `GrpcAPI.BlockReqOrBuilder`

      Returns:
      :   The idOrNum.
    - #### getIdOrNumBytes

      ```
      public com.google.protobuf.ByteString getIdOrNumBytes()
      ```

      `string id_or_num = 1;`

      Specified by:
      :   `getIdOrNumBytes` in interface `GrpcAPI.BlockReqOrBuilder`

      Returns:
      :   The bytes for idOrNum.
    - #### setIdOrNum

      ```
      public GrpcAPI.BlockReq.Builder setIdOrNum(java.lang.String value)
      ```

      `string id_or_num = 1;`

      Parameters:
      :   `value` - The idOrNum to set.

      Returns:
      :   This builder for chaining.
    - #### clearIdOrNum

      ```
      public GrpcAPI.BlockReq.Builder clearIdOrNum()
      ```

      `string id_or_num = 1;`

      Returns:
      :   This builder for chaining.
    - #### setIdOrNumBytes

      ```
      public GrpcAPI.BlockReq.Builder setIdOrNumBytes(com.google.protobuf.ByteString value)
      ```

      `string id_or_num = 1;`

      Parameters:
      :   `value` - The bytes for idOrNum to set.

      Returns:
      :   This builder for chaining.
    - #### getDetail

      ```
      public boolean getDetail()
      ```

      `bool detail = 2;`

      Specified by:
      :   `getDetail` in interface `GrpcAPI.BlockReqOrBuilder`

      Returns:
      :   The detail.
    - #### setDetail

      ```
      public GrpcAPI.BlockReq.Builder setDetail(boolean value)
      ```

      `bool detail = 2;`

      Parameters:
      :   `value` - The detail to set.

      Returns:
      :   This builder for chaining.
    - #### clearDetail

      ```
      public GrpcAPI.BlockReq.Builder clearDetail()
      ```

      `bool detail = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.BlockReq.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockReq.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.BlockReq.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.BlockReq.Builder>`