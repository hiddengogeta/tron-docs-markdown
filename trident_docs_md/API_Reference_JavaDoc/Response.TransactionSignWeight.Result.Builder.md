

org.tron.trident.proto

## Class Response.TransactionSignWeight.Result.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.TransactionSignWeight.Result.Builder](../../../../org/tron/trident/proto/Response.TransactionSignWeight.Result.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.TransactionSignWeight.Result.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.TransactionSignWeight.ResultOrBuilder](../../../../org/tron/trident/proto/Response.TransactionSignWeight.ResultOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.TransactionSignWeight.Result](../../../../org/tron/trident/proto/Response.TransactionSignWeight.Result.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.TransactionSignWeight.Result.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Result.Builder>
  implements Response.TransactionSignWeight.ResultOrBuilder
  ```

  Protobuf type `protocol.TransactionSignWeight.Result`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.TransactionSignWeight.Result.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionSignWeight.Result` | `build()` |
    | `Response.TransactionSignWeight.Result` | `buildPartial()` |
    | `Response.TransactionSignWeight.Result.Builder` | `clear()` |
    | `Response.TransactionSignWeight.Result.Builder` | `clearCode()` `.protocol.TransactionSignWeight.Result.response_code code = 1;` |
    | `Response.TransactionSignWeight.Result.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.TransactionSignWeight.Result.Builder` | `clearMessage()` `string message = 2;` |
    | `Response.TransactionSignWeight.Result.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.TransactionSignWeight.Result.Builder` | `clone()` |
    | `Response.TransactionSignWeight.Result.response_code` | `getCode()` `.protocol.TransactionSignWeight.Result.response_code code = 1;` |
    | `int` | `getCodeValue()` `.protocol.TransactionSignWeight.Result.response_code code = 1;` |
    | `Response.TransactionSignWeight.Result` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `java.lang.String` | `getMessage()` `string message = 2;` |
    | `com.google.protobuf.ByteString` | `getMessageBytes()` `string message = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.TransactionSignWeight.Result.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.TransactionSignWeight.Result.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.TransactionSignWeight.Result.Builder` | `mergeFrom(Response.TransactionSignWeight.Result other)` |
    | `Response.TransactionSignWeight.Result.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.TransactionSignWeight.Result.Builder` | `setCode(Response.TransactionSignWeight.Result.response_code value)` `.protocol.TransactionSignWeight.Result.response_code code = 1;` |
    | `Response.TransactionSignWeight.Result.Builder` | `setCodeValue(int value)` `.protocol.TransactionSignWeight.Result.response_code code = 1;` |
    | `Response.TransactionSignWeight.Result.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionSignWeight.Result.Builder` | `setMessage(java.lang.String value)` `string message = 2;` |
    | `Response.TransactionSignWeight.Result.Builder` | `setMessageBytes(com.google.protobuf.ByteString value)` `string message = 2;` |
    | `Response.TransactionSignWeight.Result.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.TransactionSignWeight.Result.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Result.Builder>`
    - #### clear

      ```
      public Response.TransactionSignWeight.Result.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Result.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Result.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.TransactionSignWeight.Result getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.TransactionSignWeight.Result build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.TransactionSignWeight.Result buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.TransactionSignWeight.Result.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Result.Builder>`
    - #### setField

      ```
      public Response.TransactionSignWeight.Result.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                    java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Result.Builder>`
    - #### clearField

      ```
      public Response.TransactionSignWeight.Result.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Result.Builder>`
    - #### clearOneof

      ```
      public Response.TransactionSignWeight.Result.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Result.Builder>`
    - #### setRepeatedField

      ```
      public Response.TransactionSignWeight.Result.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                            int index,
                                                                            java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Result.Builder>`
    - #### addRepeatedField

      ```
      public Response.TransactionSignWeight.Result.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                            java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Result.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionSignWeight.Result.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionSignWeight.Result.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionSignWeight.Result.Builder mergeFrom(Response.TransactionSignWeight.Result other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Result.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionSignWeight.Result.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                     com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                              throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionSignWeight.Result.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getCodeValue

      ```
      public int getCodeValue()
      ```

      `.protocol.TransactionSignWeight.Result.response_code code = 1;`

      Specified by:
      :   `getCodeValue` in interface `Response.TransactionSignWeight.ResultOrBuilder`

      Returns:
      :   The enum numeric value on the wire for code.
    - #### setCodeValue

      ```
      public Response.TransactionSignWeight.Result.Builder setCodeValue(int value)
      ```

      `.protocol.TransactionSignWeight.Result.response_code code = 1;`

      Parameters:
      :   `value` - The enum numeric value on the wire for code to set.

      Returns:
      :   This builder for chaining.
    - #### getCode

      ```
      public Response.TransactionSignWeight.Result.response_code getCode()
      ```

      `.protocol.TransactionSignWeight.Result.response_code code = 1;`

      Specified by:
      :   `getCode` in interface `Response.TransactionSignWeight.ResultOrBuilder`

      Returns:
      :   The code.
    - #### setCode

      ```
      public Response.TransactionSignWeight.Result.Builder setCode(Response.TransactionSignWeight.Result.response_code value)
      ```

      `.protocol.TransactionSignWeight.Result.response_code code = 1;`

      Parameters:
      :   `value` - The code to set.

      Returns:
      :   This builder for chaining.
    - #### clearCode

      ```
      public Response.TransactionSignWeight.Result.Builder clearCode()
      ```

      `.protocol.TransactionSignWeight.Result.response_code code = 1;`

      Returns:
      :   This builder for chaining.
    - #### getMessage

      ```
      public java.lang.String getMessage()
      ```

      `string message = 2;`

      Specified by:
      :   `getMessage` in interface `Response.TransactionSignWeight.ResultOrBuilder`

      Returns:
      :   The message.
    - #### getMessageBytes

      ```
      public com.google.protobuf.ByteString getMessageBytes()
      ```

      `string message = 2;`

      Specified by:
      :   `getMessageBytes` in interface `Response.TransactionSignWeight.ResultOrBuilder`

      Returns:
      :   The bytes for message.
    - #### setMessage

      ```
      public Response.TransactionSignWeight.Result.Builder setMessage(java.lang.String value)
      ```

      `string message = 2;`

      Parameters:
      :   `value` - The message to set.

      Returns:
      :   This builder for chaining.
    - #### clearMessage

      ```
      public Response.TransactionSignWeight.Result.Builder clearMessage()
      ```

      `string message = 2;`

      Returns:
      :   This builder for chaining.
    - #### setMessageBytes

      ```
      public Response.TransactionSignWeight.Result.Builder setMessageBytes(com.google.protobuf.ByteString value)
      ```

      `string message = 2;`

      Parameters:
      :   `value` - The bytes for message to set.

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.TransactionSignWeight.Result.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Result.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.TransactionSignWeight.Result.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Result.Builder>`