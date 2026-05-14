

org.tron.trident.proto

## Class Response.TransactionBalanceTrace.Operation.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.TransactionBalanceTrace.Operation.Builder](../../../../org/tron/trident/proto/Response.TransactionBalanceTrace.Operation.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.TransactionBalanceTrace.Operation.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.TransactionBalanceTrace.OperationOrBuilder](../../../../org/tron/trident/proto/Response.TransactionBalanceTrace.OperationOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.TransactionBalanceTrace.Operation](../../../../org/tron/trident/proto/Response.TransactionBalanceTrace.Operation.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.TransactionBalanceTrace.Operation.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Operation.Builder>
  implements Response.TransactionBalanceTrace.OperationOrBuilder
  ```

  Protobuf type `protocol.TransactionBalanceTrace.Operation`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.TransactionBalanceTrace.Operation.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionBalanceTrace.Operation` | `build()` |
    | `Response.TransactionBalanceTrace.Operation` | `buildPartial()` |
    | `Response.TransactionBalanceTrace.Operation.Builder` | `clear()` |
    | `Response.TransactionBalanceTrace.Operation.Builder` | `clearAddress()` `bytes address = 2;` |
    | `Response.TransactionBalanceTrace.Operation.Builder` | `clearAmount()` `int64 amount = 3;` |
    | `Response.TransactionBalanceTrace.Operation.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.TransactionBalanceTrace.Operation.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.TransactionBalanceTrace.Operation.Builder` | `clearOperationIdentifier()` `int64 operation_identifier = 1;` |
    | `Response.TransactionBalanceTrace.Operation.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getAddress()` `bytes address = 2;` |
    | `long` | `getAmount()` `int64 amount = 3;` |
    | `Response.TransactionBalanceTrace.Operation` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getOperationIdentifier()` `int64 operation_identifier = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.TransactionBalanceTrace.Operation.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.TransactionBalanceTrace.Operation.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.TransactionBalanceTrace.Operation.Builder` | `mergeFrom(Response.TransactionBalanceTrace.Operation other)` |
    | `Response.TransactionBalanceTrace.Operation.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.TransactionBalanceTrace.Operation.Builder` | `setAddress(com.google.protobuf.ByteString value)` `bytes address = 2;` |
    | `Response.TransactionBalanceTrace.Operation.Builder` | `setAmount(long value)` `int64 amount = 3;` |
    | `Response.TransactionBalanceTrace.Operation.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionBalanceTrace.Operation.Builder` | `setOperationIdentifier(long value)` `int64 operation_identifier = 1;` |
    | `Response.TransactionBalanceTrace.Operation.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.TransactionBalanceTrace.Operation.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Operation.Builder>`
    - #### clear

      ```
      public Response.TransactionBalanceTrace.Operation.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Operation.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Operation.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.TransactionBalanceTrace.Operation getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.TransactionBalanceTrace.Operation build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.TransactionBalanceTrace.Operation buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.TransactionBalanceTrace.Operation.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Operation.Builder>`
    - #### setField

      ```
      public Response.TransactionBalanceTrace.Operation.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                         java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Operation.Builder>`
    - #### clearField

      ```
      public Response.TransactionBalanceTrace.Operation.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Operation.Builder>`
    - #### clearOneof

      ```
      public Response.TransactionBalanceTrace.Operation.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Operation.Builder>`
    - #### setRepeatedField

      ```
      public Response.TransactionBalanceTrace.Operation.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                 int index,
                                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Operation.Builder>`
    - #### addRepeatedField

      ```
      public Response.TransactionBalanceTrace.Operation.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Operation.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionBalanceTrace.Operation.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionBalanceTrace.Operation.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionBalanceTrace.Operation.Builder mergeFrom(Response.TransactionBalanceTrace.Operation other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Operation.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionBalanceTrace.Operation.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                   throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionBalanceTrace.Operation.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOperationIdentifier

      ```
      public long getOperationIdentifier()
      ```

      `int64 operation_identifier = 1;`

      Specified by:
      :   `getOperationIdentifier` in interface `Response.TransactionBalanceTrace.OperationOrBuilder`

      Returns:
      :   The operationIdentifier.
    - #### setOperationIdentifier

      ```
      public Response.TransactionBalanceTrace.Operation.Builder setOperationIdentifier(long value)
      ```

      `int64 operation_identifier = 1;`

      Parameters:
      :   `value` - The operationIdentifier to set.

      Returns:
      :   This builder for chaining.
    - #### clearOperationIdentifier

      ```
      public Response.TransactionBalanceTrace.Operation.Builder clearOperationIdentifier()
      ```

      `int64 operation_identifier = 1;`

      Returns:
      :   This builder for chaining.
    - #### getAddress

      ```
      public com.google.protobuf.ByteString getAddress()
      ```

      `bytes address = 2;`

      Specified by:
      :   `getAddress` in interface `Response.TransactionBalanceTrace.OperationOrBuilder`

      Returns:
      :   The address.
    - #### setAddress

      ```
      public Response.TransactionBalanceTrace.Operation.Builder setAddress(com.google.protobuf.ByteString value)
      ```

      `bytes address = 2;`

      Parameters:
      :   `value` - The address to set.

      Returns:
      :   This builder for chaining.
    - #### clearAddress

      ```
      public Response.TransactionBalanceTrace.Operation.Builder clearAddress()
      ```

      `bytes address = 2;`

      Returns:
      :   This builder for chaining.
    - #### getAmount

      ```
      public long getAmount()
      ```

      `int64 amount = 3;`

      Specified by:
      :   `getAmount` in interface `Response.TransactionBalanceTrace.OperationOrBuilder`

      Returns:
      :   The amount.
    - #### setAmount

      ```
      public Response.TransactionBalanceTrace.Operation.Builder setAmount(long value)
      ```

      `int64 amount = 3;`

      Parameters:
      :   `value` - The amount to set.

      Returns:
      :   This builder for chaining.
    - #### clearAmount

      ```
      public Response.TransactionBalanceTrace.Operation.Builder clearAmount()
      ```

      `int64 amount = 3;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.TransactionBalanceTrace.Operation.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Operation.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.TransactionBalanceTrace.Operation.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionBalanceTrace.Operation.Builder>`