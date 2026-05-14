

org.tron.trident.proto

## Class Response.EasyTransferResponse.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.EasyTransferResponse.Builder](../../../../org/tron/trident/proto/Response.EasyTransferResponse.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.EasyTransferResponse.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.EasyTransferResponseOrBuilder](../../../../org/tron/trident/proto/Response.EasyTransferResponseOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.EasyTransferResponse](../../../../org/tron/trident/proto/Response.EasyTransferResponse.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.EasyTransferResponse.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.EasyTransferResponse.Builder>
  implements Response.EasyTransferResponseOrBuilder
  ```

  Protobuf type `protocol.EasyTransferResponse`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.EasyTransferResponse.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.EasyTransferResponse` | `build()` |
    | `Response.EasyTransferResponse` | `buildPartial()` |
    | `Response.EasyTransferResponse.Builder` | `clear()` |
    | `Response.EasyTransferResponse.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.EasyTransferResponse.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.EasyTransferResponse.Builder` | `clearResult()` `.protocol.TransactionReturn result = 2;` |
    | `Response.EasyTransferResponse.Builder` | `clearTransaction()` `.protocol.Transaction transaction = 1;` |
    | `Response.EasyTransferResponse.Builder` | `clearTxid()` transaction id = sha256(transaction.raw\_data) |
    | `Response.EasyTransferResponse.Builder` | `clone()` |
    | `Response.EasyTransferResponse` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Response.TransactionReturn` | `getResult()` `.protocol.TransactionReturn result = 2;` |
    | `Response.TransactionReturn.Builder` | `getResultBuilder()` `.protocol.TransactionReturn result = 2;` |
    | `Response.TransactionReturnOrBuilder` | `getResultOrBuilder()` `.protocol.TransactionReturn result = 2;` |
    | `Chain.Transaction` | `getTransaction()` `.protocol.Transaction transaction = 1;` |
    | `Chain.Transaction.Builder` | `getTransactionBuilder()` `.protocol.Transaction transaction = 1;` |
    | `Chain.TransactionOrBuilder` | `getTransactionOrBuilder()` `.protocol.Transaction transaction = 1;` |
    | `com.google.protobuf.ByteString` | `getTxid()` transaction id = sha256(transaction.raw\_data) |
    | `boolean` | `hasResult()` `.protocol.TransactionReturn result = 2;` |
    | `boolean` | `hasTransaction()` `.protocol.Transaction transaction = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.EasyTransferResponse.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.EasyTransferResponse.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.EasyTransferResponse.Builder` | `mergeFrom(Response.EasyTransferResponse other)` |
    | `Response.EasyTransferResponse.Builder` | `mergeResult(Response.TransactionReturn value)` `.protocol.TransactionReturn result = 2;` |
    | `Response.EasyTransferResponse.Builder` | `mergeTransaction(Chain.Transaction value)` `.protocol.Transaction transaction = 1;` |
    | `Response.EasyTransferResponse.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.EasyTransferResponse.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.EasyTransferResponse.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.EasyTransferResponse.Builder` | `setResult(Response.TransactionReturn.Builder builderForValue)` `.protocol.TransactionReturn result = 2;` |
    | `Response.EasyTransferResponse.Builder` | `setResult(Response.TransactionReturn value)` `.protocol.TransactionReturn result = 2;` |
    | `Response.EasyTransferResponse.Builder` | `setTransaction(Chain.Transaction.Builder builderForValue)` `.protocol.Transaction transaction = 1;` |
    | `Response.EasyTransferResponse.Builder` | `setTransaction(Chain.Transaction value)` `.protocol.Transaction transaction = 1;` |
    | `Response.EasyTransferResponse.Builder` | `setTxid(com.google.protobuf.ByteString value)` transaction id = sha256(transaction.raw\_data) |
    | `Response.EasyTransferResponse.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EasyTransferResponse.Builder>`
    - #### clear

      ```
      public Response.EasyTransferResponse.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EasyTransferResponse.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EasyTransferResponse.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.EasyTransferResponse getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.EasyTransferResponse build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.EasyTransferResponse buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.EasyTransferResponse.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EasyTransferResponse.Builder>`
    - #### setField

      ```
      public Response.EasyTransferResponse.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                            java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EasyTransferResponse.Builder>`
    - #### clearField

      ```
      public Response.EasyTransferResponse.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EasyTransferResponse.Builder>`
    - #### clearOneof

      ```
      public Response.EasyTransferResponse.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EasyTransferResponse.Builder>`
    - #### setRepeatedField

      ```
      public Response.EasyTransferResponse.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                    int index,
                                                                    java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EasyTransferResponse.Builder>`
    - #### addRepeatedField

      ```
      public Response.EasyTransferResponse.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                    java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EasyTransferResponse.Builder>`
    - #### mergeFrom

      ```
      public Response.EasyTransferResponse.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.EasyTransferResponse.Builder>`
    - #### mergeFrom

      ```
      public Response.EasyTransferResponse.Builder mergeFrom(Response.EasyTransferResponse other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EasyTransferResponse.Builder>`
    - #### mergeFrom

      ```
      public Response.EasyTransferResponse.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                             com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                      throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.EasyTransferResponse.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### hasTransaction

      ```
      public boolean hasTransaction()
      ```

      `.protocol.Transaction transaction = 1;`

      Specified by:
      :   `hasTransaction` in interface `Response.EasyTransferResponseOrBuilder`

      Returns:
      :   Whether the transaction field is set.
    - #### getTransaction

      ```
      public Chain.Transaction getTransaction()
      ```

      `.protocol.Transaction transaction = 1;`

      Specified by:
      :   `getTransaction` in interface `Response.EasyTransferResponseOrBuilder`

      Returns:
      :   The transaction.
    - #### setTransaction

      ```
      public Response.EasyTransferResponse.Builder setTransaction(Chain.Transaction value)
      ```

      `.protocol.Transaction transaction = 1;`
    - #### setTransaction

      ```
      public Response.EasyTransferResponse.Builder setTransaction(Chain.Transaction.Builder builderForValue)
      ```

      `.protocol.Transaction transaction = 1;`
    - #### mergeTransaction

      ```
      public Response.EasyTransferResponse.Builder mergeTransaction(Chain.Transaction value)
      ```

      `.protocol.Transaction transaction = 1;`
    - #### clearTransaction

      ```
      public Response.EasyTransferResponse.Builder clearTransaction()
      ```

      `.protocol.Transaction transaction = 1;`
    - #### getTransactionBuilder

      ```
      public Chain.Transaction.Builder getTransactionBuilder()
      ```

      `.protocol.Transaction transaction = 1;`
    - #### getTransactionOrBuilder

      ```
      public Chain.TransactionOrBuilder getTransactionOrBuilder()
      ```

      `.protocol.Transaction transaction = 1;`

      Specified by:
      :   `getTransactionOrBuilder` in interface `Response.EasyTransferResponseOrBuilder`
    - #### hasResult

      ```
      public boolean hasResult()
      ```

      `.protocol.TransactionReturn result = 2;`

      Specified by:
      :   `hasResult` in interface `Response.EasyTransferResponseOrBuilder`

      Returns:
      :   Whether the result field is set.
    - #### getResult

      ```
      public Response.TransactionReturn getResult()
      ```

      `.protocol.TransactionReturn result = 2;`

      Specified by:
      :   `getResult` in interface `Response.EasyTransferResponseOrBuilder`

      Returns:
      :   The result.
    - #### setResult

      ```
      public Response.EasyTransferResponse.Builder setResult(Response.TransactionReturn value)
      ```

      `.protocol.TransactionReturn result = 2;`
    - #### setResult

      ```
      public Response.EasyTransferResponse.Builder setResult(Response.TransactionReturn.Builder builderForValue)
      ```

      `.protocol.TransactionReturn result = 2;`
    - #### mergeResult

      ```
      public Response.EasyTransferResponse.Builder mergeResult(Response.TransactionReturn value)
      ```

      `.protocol.TransactionReturn result = 2;`
    - #### clearResult

      ```
      public Response.EasyTransferResponse.Builder clearResult()
      ```

      `.protocol.TransactionReturn result = 2;`
    - #### getResultBuilder

      ```
      public Response.TransactionReturn.Builder getResultBuilder()
      ```

      `.protocol.TransactionReturn result = 2;`
    - #### getResultOrBuilder

      ```
      public Response.TransactionReturnOrBuilder getResultOrBuilder()
      ```

      `.protocol.TransactionReturn result = 2;`

      Specified by:
      :   `getResultOrBuilder` in interface `Response.EasyTransferResponseOrBuilder`
    - #### getTxid

      ```
      public com.google.protobuf.ByteString getTxid()
      ```

      ```
       transaction id = sha256(transaction.raw_data)
      ```

      `bytes txid = 3;`

      Specified by:
      :   `getTxid` in interface `Response.EasyTransferResponseOrBuilder`

      Returns:
      :   The txid.
    - #### setTxid

      ```
      public Response.EasyTransferResponse.Builder setTxid(com.google.protobuf.ByteString value)
      ```

      ```
       transaction id = sha256(transaction.raw_data)
      ```

      `bytes txid = 3;`

      Parameters:
      :   `value` - The txid to set.

      Returns:
      :   This builder for chaining.
    - #### clearTxid

      ```
      public Response.EasyTransferResponse.Builder clearTxid()
      ```

      ```
       transaction id = sha256(transaction.raw_data)
      ```

      `bytes txid = 3;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.EasyTransferResponse.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EasyTransferResponse.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.EasyTransferResponse.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EasyTransferResponse.Builder>`