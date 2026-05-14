

org.tron.trident.proto

## Class Response.TransactionApprovedList.Result.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.TransactionApprovedList.Result.Builder](../../../../org/tron/trident/proto/Response.TransactionApprovedList.Result.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.TransactionApprovedList.Result.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.TransactionApprovedList.ResultOrBuilder](../../../../org/tron/trident/proto/Response.TransactionApprovedList.ResultOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.TransactionApprovedList.Result](../../../../org/tron/trident/proto/Response.TransactionApprovedList.Result.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.TransactionApprovedList.Result.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Result.Builder>
  implements Response.TransactionApprovedList.ResultOrBuilder
  ```

  Protobuf type `protocol.TransactionApprovedList.Result`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.TransactionApprovedList.Result.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionApprovedList.Result` | `build()` |
    | `Response.TransactionApprovedList.Result` | `buildPartial()` |
    | `Response.TransactionApprovedList.Result.Builder` | `clear()` |
    | `Response.TransactionApprovedList.Result.Builder` | `clearCode()` `.protocol.TransactionApprovedList.Result.response_code code = 1;` |
    | `Response.TransactionApprovedList.Result.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.TransactionApprovedList.Result.Builder` | `clearMessage()` `string message = 2;` |
    | `Response.TransactionApprovedList.Result.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.TransactionApprovedList.Result.Builder` | `clone()` |
    | `Response.TransactionApprovedList.Result.response_code` | `getCode()` `.protocol.TransactionApprovedList.Result.response_code code = 1;` |
    | `int` | `getCodeValue()` `.protocol.TransactionApprovedList.Result.response_code code = 1;` |
    | `Response.TransactionApprovedList.Result` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `java.lang.String` | `getMessage()` `string message = 2;` |
    | `com.google.protobuf.ByteString` | `getMessageBytes()` `string message = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.TransactionApprovedList.Result.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.TransactionApprovedList.Result.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.TransactionApprovedList.Result.Builder` | `mergeFrom(Response.TransactionApprovedList.Result other)` |
    | `Response.TransactionApprovedList.Result.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.TransactionApprovedList.Result.Builder` | `setCode(Response.TransactionApprovedList.Result.response_code value)` `.protocol.TransactionApprovedList.Result.response_code code = 1;` |
    | `Response.TransactionApprovedList.Result.Builder` | `setCodeValue(int value)` `.protocol.TransactionApprovedList.Result.response_code code = 1;` |
    | `Response.TransactionApprovedList.Result.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionApprovedList.Result.Builder` | `setMessage(java.lang.String value)` `string message = 2;` |
    | `Response.TransactionApprovedList.Result.Builder` | `setMessageBytes(com.google.protobuf.ByteString value)` `string message = 2;` |
    | `Response.TransactionApprovedList.Result.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.TransactionApprovedList.Result.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Result.Builder>`
    - #### clear

      ```
      public Response.TransactionApprovedList.Result.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Result.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Result.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.TransactionApprovedList.Result getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.TransactionApprovedList.Result build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.TransactionApprovedList.Result buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.TransactionApprovedList.Result.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Result.Builder>`
    - #### setField

      ```
      public Response.TransactionApprovedList.Result.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                      java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Result.Builder>`
    - #### clearField

      ```
      public Response.TransactionApprovedList.Result.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Result.Builder>`
    - #### clearOneof

      ```
      public Response.TransactionApprovedList.Result.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Result.Builder>`
    - #### setRepeatedField

      ```
      public Response.TransactionApprovedList.Result.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                              int index,
                                                                              java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Result.Builder>`
    - #### addRepeatedField

      ```
      public Response.TransactionApprovedList.Result.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                              java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Result.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionApprovedList.Result.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionApprovedList.Result.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionApprovedList.Result.Builder mergeFrom(Response.TransactionApprovedList.Result other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Result.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionApprovedList.Result.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionApprovedList.Result.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getCodeValue

      ```
      public int getCodeValue()
      ```

      `.protocol.TransactionApprovedList.Result.response_code code = 1;`

      Specified by:
      :   `getCodeValue` in interface `Response.TransactionApprovedList.ResultOrBuilder`

      Returns:
      :   The enum numeric value on the wire for code.
    - #### setCodeValue

      ```
      public Response.TransactionApprovedList.Result.Builder setCodeValue(int value)
      ```

      `.protocol.TransactionApprovedList.Result.response_code code = 1;`

      Parameters:
      :   `value` - The enum numeric value on the wire for code to set.

      Returns:
      :   This builder for chaining.
    - #### getCode

      ```
      public Response.TransactionApprovedList.Result.response_code getCode()
      ```

      `.protocol.TransactionApprovedList.Result.response_code code = 1;`

      Specified by:
      :   `getCode` in interface `Response.TransactionApprovedList.ResultOrBuilder`

      Returns:
      :   The code.
    - #### setCode

      ```
      public Response.TransactionApprovedList.Result.Builder setCode(Response.TransactionApprovedList.Result.response_code value)
      ```

      `.protocol.TransactionApprovedList.Result.response_code code = 1;`

      Parameters:
      :   `value` - The code to set.

      Returns:
      :   This builder for chaining.
    - #### clearCode

      ```
      public Response.TransactionApprovedList.Result.Builder clearCode()
      ```

      `.protocol.TransactionApprovedList.Result.response_code code = 1;`

      Returns:
      :   This builder for chaining.
    - #### getMessage

      ```
      public java.lang.String getMessage()
      ```

      `string message = 2;`

      Specified by:
      :   `getMessage` in interface `Response.TransactionApprovedList.ResultOrBuilder`

      Returns:
      :   The message.
    - #### getMessageBytes

      ```
      public com.google.protobuf.ByteString getMessageBytes()
      ```

      `string message = 2;`

      Specified by:
      :   `getMessageBytes` in interface `Response.TransactionApprovedList.ResultOrBuilder`

      Returns:
      :   The bytes for message.
    - #### setMessage

      ```
      public Response.TransactionApprovedList.Result.Builder setMessage(java.lang.String value)
      ```

      `string message = 2;`

      Parameters:
      :   `value` - The message to set.

      Returns:
      :   This builder for chaining.
    - #### clearMessage

      ```
      public Response.TransactionApprovedList.Result.Builder clearMessage()
      ```

      `string message = 2;`

      Returns:
      :   This builder for chaining.
    - #### setMessageBytes

      ```
      public Response.TransactionApprovedList.Result.Builder setMessageBytes(com.google.protobuf.ByteString value)
      ```

      `string message = 2;`

      Parameters:
      :   `value` - The bytes for message to set.

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.TransactionApprovedList.Result.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Result.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.TransactionApprovedList.Result.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Result.Builder>`