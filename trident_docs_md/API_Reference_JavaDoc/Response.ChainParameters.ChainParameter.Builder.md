

org.tron.trident.proto

## Class Response.ChainParameters.ChainParameter.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.ChainParameters.ChainParameter.Builder](../../../../org/tron/trident/proto/Response.ChainParameters.ChainParameter.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.ChainParameters.ChainParameter.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.ChainParameters.ChainParameterOrBuilder](../../../../org/tron/trident/proto/Response.ChainParameters.ChainParameterOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.ChainParameters.ChainParameter](../../../../org/tron/trident/proto/Response.ChainParameters.ChainParameter.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.ChainParameters.ChainParameter.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.ChainParameter.Builder>
  implements Response.ChainParameters.ChainParameterOrBuilder
  ```

  Protobuf type `protocol.ChainParameters.ChainParameter`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.ChainParameters.ChainParameter.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.ChainParameters.ChainParameter` | `build()` |
    | `Response.ChainParameters.ChainParameter` | `buildPartial()` |
    | `Response.ChainParameters.ChainParameter.Builder` | `clear()` |
    | `Response.ChainParameters.ChainParameter.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.ChainParameters.ChainParameter.Builder` | `clearKey()` `string key = 1;` |
    | `Response.ChainParameters.ChainParameter.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.ChainParameters.ChainParameter.Builder` | `clearValue()` `int64 value = 2;` |
    | `Response.ChainParameters.ChainParameter.Builder` | `clone()` |
    | `Response.ChainParameters.ChainParameter` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `java.lang.String` | `getKey()` `string key = 1;` |
    | `com.google.protobuf.ByteString` | `getKeyBytes()` `string key = 1;` |
    | `long` | `getValue()` `int64 value = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.ChainParameters.ChainParameter.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.ChainParameters.ChainParameter.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.ChainParameters.ChainParameter.Builder` | `mergeFrom(Response.ChainParameters.ChainParameter other)` |
    | `Response.ChainParameters.ChainParameter.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.ChainParameters.ChainParameter.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.ChainParameters.ChainParameter.Builder` | `setKey(java.lang.String value)` `string key = 1;` |
    | `Response.ChainParameters.ChainParameter.Builder` | `setKeyBytes(com.google.protobuf.ByteString value)` `string key = 1;` |
    | `Response.ChainParameters.ChainParameter.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.ChainParameters.ChainParameter.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.ChainParameters.ChainParameter.Builder` | `setValue(long value)` `int64 value = 2;` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.ChainParameter.Builder>`
    - #### clear

      ```
      public Response.ChainParameters.ChainParameter.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.ChainParameter.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.ChainParameter.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.ChainParameters.ChainParameter getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.ChainParameters.ChainParameter build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.ChainParameters.ChainParameter buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.ChainParameters.ChainParameter.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.ChainParameter.Builder>`
    - #### setField

      ```
      public Response.ChainParameters.ChainParameter.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                      java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.ChainParameter.Builder>`
    - #### clearField

      ```
      public Response.ChainParameters.ChainParameter.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.ChainParameter.Builder>`
    - #### clearOneof

      ```
      public Response.ChainParameters.ChainParameter.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.ChainParameter.Builder>`
    - #### setRepeatedField

      ```
      public Response.ChainParameters.ChainParameter.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                              int index,
                                                                              java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.ChainParameter.Builder>`
    - #### addRepeatedField

      ```
      public Response.ChainParameters.ChainParameter.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                              java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.ChainParameter.Builder>`
    - #### mergeFrom

      ```
      public Response.ChainParameters.ChainParameter.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.ChainParameters.ChainParameter.Builder>`
    - #### mergeFrom

      ```
      public Response.ChainParameters.ChainParameter.Builder mergeFrom(Response.ChainParameters.ChainParameter other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.ChainParameter.Builder>`
    - #### mergeFrom

      ```
      public Response.ChainParameters.ChainParameter.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.ChainParameters.ChainParameter.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getKey

      ```
      public java.lang.String getKey()
      ```

      `string key = 1;`

      Specified by:
      :   `getKey` in interface `Response.ChainParameters.ChainParameterOrBuilder`

      Returns:
      :   The key.
    - #### getKeyBytes

      ```
      public com.google.protobuf.ByteString getKeyBytes()
      ```

      `string key = 1;`

      Specified by:
      :   `getKeyBytes` in interface `Response.ChainParameters.ChainParameterOrBuilder`

      Returns:
      :   The bytes for key.
    - #### setKey

      ```
      public Response.ChainParameters.ChainParameter.Builder setKey(java.lang.String value)
      ```

      `string key = 1;`

      Parameters:
      :   `value` - The key to set.

      Returns:
      :   This builder for chaining.
    - #### clearKey

      ```
      public Response.ChainParameters.ChainParameter.Builder clearKey()
      ```

      `string key = 1;`

      Returns:
      :   This builder for chaining.
    - #### setKeyBytes

      ```
      public Response.ChainParameters.ChainParameter.Builder setKeyBytes(com.google.protobuf.ByteString value)
      ```

      `string key = 1;`

      Parameters:
      :   `value` - The bytes for key to set.

      Returns:
      :   This builder for chaining.
    - #### getValue

      ```
      public long getValue()
      ```

      `int64 value = 2;`

      Specified by:
      :   `getValue` in interface `Response.ChainParameters.ChainParameterOrBuilder`

      Returns:
      :   The value.
    - #### setValue

      ```
      public Response.ChainParameters.ChainParameter.Builder setValue(long value)
      ```

      `int64 value = 2;`

      Parameters:
      :   `value` - The value to set.

      Returns:
      :   This builder for chaining.
    - #### clearValue

      ```
      public Response.ChainParameters.ChainParameter.Builder clearValue()
      ```

      `int64 value = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.ChainParameters.ChainParameter.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.ChainParameter.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.ChainParameters.ChainParameter.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.ChainParameter.Builder>`