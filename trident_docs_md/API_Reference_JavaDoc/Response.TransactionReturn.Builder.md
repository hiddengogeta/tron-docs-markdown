

org.tron.trident.proto

## Class Response.TransactionReturn.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.TransactionReturn.Builder](../../../../org/tron/trident/proto/Response.TransactionReturn.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.TransactionReturn.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.TransactionReturnOrBuilder](../../../../org/tron/trident/proto/Response.TransactionReturnOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.TransactionReturn](../../../../org/tron/trident/proto/Response.TransactionReturn.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.TransactionReturn.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionReturn.Builder>
  implements Response.TransactionReturnOrBuilder
  ```

  Protobuf type `protocol.TransactionReturn`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.TransactionReturn.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionReturn` | `build()` |
    | `Response.TransactionReturn` | `buildPartial()` |
    | `Response.TransactionReturn.Builder` | `clear()` |
    | `Response.TransactionReturn.Builder` | `clearCode()` `.protocol.TransactionReturn.response_code code = 2;` |
    | `Response.TransactionReturn.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.TransactionReturn.Builder` | `clearMessage()` `bytes message = 3;` |
    | `Response.TransactionReturn.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.TransactionReturn.Builder` | `clearResult()` `bool result = 1;` |
    | `Response.TransactionReturn.Builder` | `clone()` |
    | `Response.TransactionReturn.response_code` | `getCode()` `.protocol.TransactionReturn.response_code code = 2;` |
    | `int` | `getCodeValue()` `.protocol.TransactionReturn.response_code code = 2;` |
    | `Response.TransactionReturn` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getMessage()` `bytes message = 3;` |
    | `boolean` | `getResult()` `bool result = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.TransactionReturn.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.TransactionReturn.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.TransactionReturn.Builder` | `mergeFrom(Response.TransactionReturn other)` |
    | `Response.TransactionReturn.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.TransactionReturn.Builder` | `setCode(Response.TransactionReturn.response_code value)` `.protocol.TransactionReturn.response_code code = 2;` |
    | `Response.TransactionReturn.Builder` | `setCodeValue(int value)` `.protocol.TransactionReturn.response_code code = 2;` |
    | `Response.TransactionReturn.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionReturn.Builder` | `setMessage(com.google.protobuf.ByteString value)` `bytes message = 3;` |
    | `Response.TransactionReturn.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.TransactionReturn.Builder` | `setResult(boolean value)` `bool result = 1;` |
    | `Response.TransactionReturn.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionReturn.Builder>`
    - #### clear

      ```
      public Response.TransactionReturn.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionReturn.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionReturn.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.TransactionReturn getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.TransactionReturn build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.TransactionReturn buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.TransactionReturn.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionReturn.Builder>`
    - #### setField

      ```
      public Response.TransactionReturn.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                         java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionReturn.Builder>`
    - #### clearField

      ```
      public Response.TransactionReturn.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionReturn.Builder>`
    - #### clearOneof

      ```
      public Response.TransactionReturn.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionReturn.Builder>`
    - #### setRepeatedField

      ```
      public Response.TransactionReturn.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                 int index,
                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionReturn.Builder>`
    - #### addRepeatedField

      ```
      public Response.TransactionReturn.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionReturn.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionReturn.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionReturn.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionReturn.Builder mergeFrom(Response.TransactionReturn other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionReturn.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionReturn.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionReturn.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getResult

      ```
      public boolean getResult()
      ```

      `bool result = 1;`

      Specified by:
      :   `getResult` in interface `Response.TransactionReturnOrBuilder`

      Returns:
      :   The result.
    - #### setResult

      ```
      public Response.TransactionReturn.Builder setResult(boolean value)
      ```

      `bool result = 1;`

      Parameters:
      :   `value` - The result to set.

      Returns:
      :   This builder for chaining.
    - #### clearResult

      ```
      public Response.TransactionReturn.Builder clearResult()
      ```

      `bool result = 1;`

      Returns:
      :   This builder for chaining.
    - #### getCodeValue

      ```
      public int getCodeValue()
      ```

      `.protocol.TransactionReturn.response_code code = 2;`

      Specified by:
      :   `getCodeValue` in interface `Response.TransactionReturnOrBuilder`

      Returns:
      :   The enum numeric value on the wire for code.
    - #### setCodeValue

      ```
      public Response.TransactionReturn.Builder setCodeValue(int value)
      ```

      `.protocol.TransactionReturn.response_code code = 2;`

      Parameters:
      :   `value` - The enum numeric value on the wire for code to set.

      Returns:
      :   This builder for chaining.
    - #### getCode

      ```
      public Response.TransactionReturn.response_code getCode()
      ```

      `.protocol.TransactionReturn.response_code code = 2;`

      Specified by:
      :   `getCode` in interface `Response.TransactionReturnOrBuilder`

      Returns:
      :   The code.
    - #### setCode

      ```
      public Response.TransactionReturn.Builder setCode(Response.TransactionReturn.response_code value)
      ```

      `.protocol.TransactionReturn.response_code code = 2;`

      Parameters:
      :   `value` - The code to set.

      Returns:
      :   This builder for chaining.
    - #### clearCode

      ```
      public Response.TransactionReturn.Builder clearCode()
      ```

      `.protocol.TransactionReturn.response_code code = 2;`

      Returns:
      :   This builder for chaining.
    - #### getMessage

      ```
      public com.google.protobuf.ByteString getMessage()
      ```

      `bytes message = 3;`

      Specified by:
      :   `getMessage` in interface `Response.TransactionReturnOrBuilder`

      Returns:
      :   The message.
    - #### setMessage

      ```
      public Response.TransactionReturn.Builder setMessage(com.google.protobuf.ByteString value)
      ```

      `bytes message = 3;`

      Parameters:
      :   `value` - The message to set.

      Returns:
      :   This builder for chaining.
    - #### clearMessage

      ```
      public Response.TransactionReturn.Builder clearMessage()
      ```

      `bytes message = 3;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.TransactionReturn.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionReturn.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.TransactionReturn.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionReturn.Builder>`