

org.tron.trident.proto

## Class Response.TransactionBalanceTrace.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.TransactionBalanceTrace.Builder](../../../../org/tron/trident/proto/Response.TransactionBalanceTrace.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.TransactionBalanceTrace.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.TransactionBalanceTraceOrBuilder](../../../../org/tron/trident/proto/Response.TransactionBalanceTraceOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.TransactionBalanceTrace](../../../../org/tron/trident/proto/Response.TransactionBalanceTrace.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.TransactionBalanceTrace.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Builder>
  implements Response.TransactionBalanceTraceOrBuilder
  ```

  Protobuf type `protocol.TransactionBalanceTrace`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.TransactionBalanceTrace.Builder` | `addAllOperation(java.lang.Iterable<? extends Response.TransactionBalanceTrace.Operation> values)` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `Response.TransactionBalanceTrace.Builder` | `addOperation(int index, Response.TransactionBalanceTrace.Operation.Builder builderForValue)` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `Response.TransactionBalanceTrace.Builder` | `addOperation(int index, Response.TransactionBalanceTrace.Operation value)` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `Response.TransactionBalanceTrace.Builder` | `addOperation(Response.TransactionBalanceTrace.Operation.Builder builderForValue)` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `Response.TransactionBalanceTrace.Builder` | `addOperation(Response.TransactionBalanceTrace.Operation value)` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `Response.TransactionBalanceTrace.Operation.Builder` | `addOperationBuilder()` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `Response.TransactionBalanceTrace.Operation.Builder` | `addOperationBuilder(int index)` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `Response.TransactionBalanceTrace.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionBalanceTrace` | `build()` |
    | `Response.TransactionBalanceTrace` | `buildPartial()` |
    | `Response.TransactionBalanceTrace.Builder` | `clear()` |
    | `Response.TransactionBalanceTrace.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.TransactionBalanceTrace.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.TransactionBalanceTrace.Builder` | `clearOperation()` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `Response.TransactionBalanceTrace.Builder` | `clearStatus()` `string status = 4;` |
    | `Response.TransactionBalanceTrace.Builder` | `clearTransactionIdentifier()` `bytes transaction_identifier = 1;` |
    | `Response.TransactionBalanceTrace.Builder` | `clearType()` `string type = 3;` |
    | `Response.TransactionBalanceTrace.Builder` | `clone()` |
    | `Response.TransactionBalanceTrace` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Response.TransactionBalanceTrace.Operation` | `getOperation(int index)` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `Response.TransactionBalanceTrace.Operation.Builder` | `getOperationBuilder(int index)` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `java.util.List<Response.TransactionBalanceTrace.Operation.Builder>` | `getOperationBuilderList()` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `int` | `getOperationCount()` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `java.util.List<Response.TransactionBalanceTrace.Operation>` | `getOperationList()` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `Response.TransactionBalanceTrace.OperationOrBuilder` | `getOperationOrBuilder(int index)` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `java.util.List<? extends Response.TransactionBalanceTrace.OperationOrBuilder>` | `getOperationOrBuilderList()` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `java.lang.String` | `getStatus()` `string status = 4;` |
    | `com.google.protobuf.ByteString` | `getStatusBytes()` `string status = 4;` |
    | `com.google.protobuf.ByteString` | `getTransactionIdentifier()` `bytes transaction_identifier = 1;` |
    | `java.lang.String` | `getType()` `string type = 3;` |
    | `com.google.protobuf.ByteString` | `getTypeBytes()` `string type = 3;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.TransactionBalanceTrace.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.TransactionBalanceTrace.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.TransactionBalanceTrace.Builder` | `mergeFrom(Response.TransactionBalanceTrace other)` |
    | `Response.TransactionBalanceTrace.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.TransactionBalanceTrace.Builder` | `removeOperation(int index)` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `Response.TransactionBalanceTrace.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionBalanceTrace.Builder` | `setOperation(int index, Response.TransactionBalanceTrace.Operation.Builder builderForValue)` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `Response.TransactionBalanceTrace.Builder` | `setOperation(int index, Response.TransactionBalanceTrace.Operation value)` `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;` |
    | `Response.TransactionBalanceTrace.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.TransactionBalanceTrace.Builder` | `setStatus(java.lang.String value)` `string status = 4;` |
    | `Response.TransactionBalanceTrace.Builder` | `setStatusBytes(com.google.protobuf.ByteString value)` `string status = 4;` |
    | `Response.TransactionBalanceTrace.Builder` | `setTransactionIdentifier(com.google.protobuf.ByteString value)` `bytes transaction_identifier = 1;` |
    | `Response.TransactionBalanceTrace.Builder` | `setType(java.lang.String value)` `string type = 3;` |
    | `Response.TransactionBalanceTrace.Builder` | `setTypeBytes(com.google.protobuf.ByteString value)` `string type = 3;` |
    | `Response.TransactionBalanceTrace.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Builder>`
    - #### clear

      ```
      public Response.TransactionBalanceTrace.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.TransactionBalanceTrace getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.TransactionBalanceTrace build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.TransactionBalanceTrace buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.TransactionBalanceTrace.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Builder>`
    - #### setField

      ```
      public Response.TransactionBalanceTrace.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Builder>`
    - #### clearField

      ```
      public Response.TransactionBalanceTrace.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Builder>`
    - #### clearOneof

      ```
      public Response.TransactionBalanceTrace.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Builder>`
    - #### setRepeatedField

      ```
      public Response.TransactionBalanceTrace.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                       int index,
                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Builder>`
    - #### addRepeatedField

      ```
      public Response.TransactionBalanceTrace.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionBalanceTrace.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionBalanceTrace.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionBalanceTrace.Builder mergeFrom(Response.TransactionBalanceTrace other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionBalanceTrace.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionBalanceTrace.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getTransactionIdentifier

      ```
      public com.google.protobuf.ByteString getTransactionIdentifier()
      ```

      `bytes transaction_identifier = 1;`

      Specified by:
      :   `getTransactionIdentifier` in interface `Response.TransactionBalanceTraceOrBuilder`

      Returns:
      :   The transactionIdentifier.
    - #### setTransactionIdentifier

      ```
      public Response.TransactionBalanceTrace.Builder setTransactionIdentifier(com.google.protobuf.ByteString value)
      ```

      `bytes transaction_identifier = 1;`

      Parameters:
      :   `value` - The transactionIdentifier to set.

      Returns:
      :   This builder for chaining.
    - #### clearTransactionIdentifier

      ```
      public Response.TransactionBalanceTrace.Builder clearTransactionIdentifier()
      ```

      `bytes transaction_identifier = 1;`

      Returns:
      :   This builder for chaining.
    - #### getOperationList

      ```
      public java.util.List<Response.TransactionBalanceTrace.Operation> getOperationList()
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`

      Specified by:
      :   `getOperationList` in interface `Response.TransactionBalanceTraceOrBuilder`
    - #### getOperationCount

      ```
      public int getOperationCount()
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`

      Specified by:
      :   `getOperationCount` in interface `Response.TransactionBalanceTraceOrBuilder`
    - #### getOperation

      ```
      public Response.TransactionBalanceTrace.Operation getOperation(int index)
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`

      Specified by:
      :   `getOperation` in interface `Response.TransactionBalanceTraceOrBuilder`
    - #### setOperation

      ```
      public Response.TransactionBalanceTrace.Builder setOperation(int index,
                                                                   Response.TransactionBalanceTrace.Operation value)
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`
    - #### setOperation

      ```
      public Response.TransactionBalanceTrace.Builder setOperation(int index,
                                                                   Response.TransactionBalanceTrace.Operation.Builder builderForValue)
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`
    - #### addOperation

      ```
      public Response.TransactionBalanceTrace.Builder addOperation(Response.TransactionBalanceTrace.Operation value)
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`
    - #### addOperation

      ```
      public Response.TransactionBalanceTrace.Builder addOperation(int index,
                                                                   Response.TransactionBalanceTrace.Operation value)
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`
    - #### addOperation

      ```
      public Response.TransactionBalanceTrace.Builder addOperation(Response.TransactionBalanceTrace.Operation.Builder builderForValue)
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`
    - #### addOperation

      ```
      public Response.TransactionBalanceTrace.Builder addOperation(int index,
                                                                   Response.TransactionBalanceTrace.Operation.Builder builderForValue)
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`
    - #### addAllOperation

      ```
      public Response.TransactionBalanceTrace.Builder addAllOperation(java.lang.Iterable<? extends Response.TransactionBalanceTrace.Operation> values)
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`
    - #### clearOperation

      ```
      public Response.TransactionBalanceTrace.Builder clearOperation()
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`
    - #### removeOperation

      ```
      public Response.TransactionBalanceTrace.Builder removeOperation(int index)
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`
    - #### getOperationBuilder

      ```
      public Response.TransactionBalanceTrace.Operation.Builder getOperationBuilder(int index)
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`
    - #### getOperationOrBuilder

      ```
      public Response.TransactionBalanceTrace.OperationOrBuilder getOperationOrBuilder(int index)
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`

      Specified by:
      :   `getOperationOrBuilder` in interface `Response.TransactionBalanceTraceOrBuilder`
    - #### getOperationOrBuilderList

      ```
      public java.util.List<? extends Response.TransactionBalanceTrace.OperationOrBuilder> getOperationOrBuilderList()
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`

      Specified by:
      :   `getOperationOrBuilderList` in interface `Response.TransactionBalanceTraceOrBuilder`
    - #### addOperationBuilder

      ```
      public Response.TransactionBalanceTrace.Operation.Builder addOperationBuilder()
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`
    - #### addOperationBuilder

      ```
      public Response.TransactionBalanceTrace.Operation.Builder addOperationBuilder(int index)
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`
    - #### getOperationBuilderList

      ```
      public java.util.List<Response.TransactionBalanceTrace.Operation.Builder> getOperationBuilderList()
      ```

      `repeated .protocol.TransactionBalanceTrace.Operation operation = 2;`
    - #### getType

      ```
      public java.lang.String getType()
      ```

      `string type = 3;`

      Specified by:
      :   `getType` in interface `Response.TransactionBalanceTraceOrBuilder`

      Returns:
      :   The type.
    - #### getTypeBytes

      ```
      public com.google.protobuf.ByteString getTypeBytes()
      ```

      `string type = 3;`

      Specified by:
      :   `getTypeBytes` in interface `Response.TransactionBalanceTraceOrBuilder`

      Returns:
      :   The bytes for type.
    - #### setType

      ```
      public Response.TransactionBalanceTrace.Builder setType(java.lang.String value)
      ```

      `string type = 3;`

      Parameters:
      :   `value` - The type to set.

      Returns:
      :   This builder for chaining.
    - #### clearType

      ```
      public Response.TransactionBalanceTrace.Builder clearType()
      ```

      `string type = 3;`

      Returns:
      :   This builder for chaining.
    - #### setTypeBytes

      ```
      public Response.TransactionBalanceTrace.Builder setTypeBytes(com.google.protobuf.ByteString value)
      ```

      `string type = 3;`

      Parameters:
      :   `value` - The bytes for type to set.

      Returns:
      :   This builder for chaining.
    - #### getStatus

      ```
      public java.lang.String getStatus()
      ```

      `string status = 4;`

      Specified by:
      :   `getStatus` in interface `Response.TransactionBalanceTraceOrBuilder`

      Returns:
      :   The status.
    - #### getStatusBytes

      ```
      public com.google.protobuf.ByteString getStatusBytes()
      ```

      `string status = 4;`

      Specified by:
      :   `getStatusBytes` in interface `Response.TransactionBalanceTraceOrBuilder`

      Returns:
      :   The bytes for status.
    - #### setStatus

      ```
      public Response.TransactionBalanceTrace.Builder setStatus(java.lang.String value)
      ```

      `string status = 4;`

      Parameters:
      :   `value` - The status to set.

      Returns:
      :   This builder for chaining.
    - #### clearStatus

      ```
      public Response.TransactionBalanceTrace.Builder clearStatus()
      ```

      `string status = 4;`

      Returns:
      :   This builder for chaining.
    - #### setStatusBytes

      ```
      public Response.TransactionBalanceTrace.Builder setStatusBytes(com.google.protobuf.ByteString value)
      ```

      `string status = 4;`

      Parameters:
      :   `value` - The bytes for status to set.

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.TransactionBalanceTrace.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.TransactionBalanceTrace.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Builder>`