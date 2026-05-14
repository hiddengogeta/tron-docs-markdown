

org.tron.trident.proto

## Class Response.TransactionSign.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.TransactionSign.Builder](../../../../org/tron/trident/proto/Response.TransactionSign.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.TransactionSign.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.TransactionSignOrBuilder](../../../../org/tron/trident/proto/Response.TransactionSignOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.TransactionSign](../../../../org/tron/trident/proto/Response.TransactionSign.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.TransactionSign.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSign.Builder>
  implements Response.TransactionSignOrBuilder
  ```

  Protobuf type `protocol.TransactionSign`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.TransactionSign.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionSign` | `build()` |
    | `Response.TransactionSign` | `buildPartial()` |
    | `Response.TransactionSign.Builder` | `clear()` |
    | `Response.TransactionSign.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.TransactionSign.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.TransactionSign.Builder` | `clearPrivateKey()` `bytes privateKey = 2;` |
    | `Response.TransactionSign.Builder` | `clearTransaction()` `.protocol.Transaction transaction = 1;` |
    | `Response.TransactionSign.Builder` | `clone()` |
    | `Response.TransactionSign` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getPrivateKey()` `bytes privateKey = 2;` |
    | `Chain.Transaction` | `getTransaction()` `.protocol.Transaction transaction = 1;` |
    | `Chain.Transaction.Builder` | `getTransactionBuilder()` `.protocol.Transaction transaction = 1;` |
    | `Chain.TransactionOrBuilder` | `getTransactionOrBuilder()` `.protocol.Transaction transaction = 1;` |
    | `boolean` | `hasTransaction()` `.protocol.Transaction transaction = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.TransactionSign.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.TransactionSign.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.TransactionSign.Builder` | `mergeFrom(Response.TransactionSign other)` |
    | `Response.TransactionSign.Builder` | `mergeTransaction(Chain.Transaction value)` `.protocol.Transaction transaction = 1;` |
    | `Response.TransactionSign.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.TransactionSign.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionSign.Builder` | `setPrivateKey(com.google.protobuf.ByteString value)` `bytes privateKey = 2;` |
    | `Response.TransactionSign.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.TransactionSign.Builder` | `setTransaction(Chain.Transaction.Builder builderForValue)` `.protocol.Transaction transaction = 1;` |
    | `Response.TransactionSign.Builder` | `setTransaction(Chain.Transaction value)` `.protocol.Transaction transaction = 1;` |
    | `Response.TransactionSign.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSign.Builder>`
    - #### clear

      ```
      public Response.TransactionSign.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSign.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSign.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.TransactionSign getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.TransactionSign build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.TransactionSign buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.TransactionSign.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSign.Builder>`
    - #### setField

      ```
      public Response.TransactionSign.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSign.Builder>`
    - #### clearField

      ```
      public Response.TransactionSign.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSign.Builder>`
    - #### clearOneof

      ```
      public Response.TransactionSign.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSign.Builder>`
    - #### setRepeatedField

      ```
      public Response.TransactionSign.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               int index,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSign.Builder>`
    - #### addRepeatedField

      ```
      public Response.TransactionSign.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSign.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionSign.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionSign.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionSign.Builder mergeFrom(Response.TransactionSign other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSign.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionSign.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                 throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionSign.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### hasTransaction

      ```
      public boolean hasTransaction()
      ```

      `.protocol.Transaction transaction = 1;`

      Specified by:
      :   `hasTransaction` in interface `Response.TransactionSignOrBuilder`

      Returns:
      :   Whether the transaction field is set.
    - #### getTransaction

      ```
      public Chain.Transaction getTransaction()
      ```

      `.protocol.Transaction transaction = 1;`

      Specified by:
      :   `getTransaction` in interface `Response.TransactionSignOrBuilder`

      Returns:
      :   The transaction.
    - #### setTransaction

      ```
      public Response.TransactionSign.Builder setTransaction(Chain.Transaction value)
      ```

      `.protocol.Transaction transaction = 1;`
    - #### setTransaction

      ```
      public Response.TransactionSign.Builder setTransaction(Chain.Transaction.Builder builderForValue)
      ```

      `.protocol.Transaction transaction = 1;`
    - #### mergeTransaction

      ```
      public Response.TransactionSign.Builder mergeTransaction(Chain.Transaction value)
      ```

      `.protocol.Transaction transaction = 1;`
    - #### clearTransaction

      ```
      public Response.TransactionSign.Builder clearTransaction()
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
      :   `getTransactionOrBuilder` in interface `Response.TransactionSignOrBuilder`
    - #### getPrivateKey

      ```
      public com.google.protobuf.ByteString getPrivateKey()
      ```

      `bytes privateKey = 2;`

      Specified by:
      :   `getPrivateKey` in interface `Response.TransactionSignOrBuilder`

      Returns:
      :   The privateKey.
    - #### setPrivateKey

      ```
      public Response.TransactionSign.Builder setPrivateKey(com.google.protobuf.ByteString value)
      ```

      `bytes privateKey = 2;`

      Parameters:
      :   `value` - The privateKey to set.

      Returns:
      :   This builder for chaining.
    - #### clearPrivateKey

      ```
      public Response.TransactionSign.Builder clearPrivateKey()
      ```

      `bytes privateKey = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.TransactionSign.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSign.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.TransactionSign.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSign.Builder>`