

org.tron.trident.proto

## Class Response.TransactionList.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.TransactionList.Builder](../../../../org/tron/trident/proto/Response.TransactionList.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.TransactionList.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.TransactionListOrBuilder](../../../../org/tron/trident/proto/Response.TransactionListOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.TransactionList](../../../../org/tron/trident/proto/Response.TransactionList.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.TransactionList.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionList.Builder>
  implements Response.TransactionListOrBuilder
  ```

  Protobuf type `protocol.TransactionList`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.TransactionList.Builder` | `addAllTransaction(java.lang.Iterable<? extends Chain.Transaction> values)` `repeated .protocol.Transaction transaction = 1;` |
    | `Response.TransactionList.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionList.Builder` | `addTransaction(Chain.Transaction.Builder builderForValue)` `repeated .protocol.Transaction transaction = 1;` |
    | `Response.TransactionList.Builder` | `addTransaction(Chain.Transaction value)` `repeated .protocol.Transaction transaction = 1;` |
    | `Response.TransactionList.Builder` | `addTransaction(int index, Chain.Transaction.Builder builderForValue)` `repeated .protocol.Transaction transaction = 1;` |
    | `Response.TransactionList.Builder` | `addTransaction(int index, Chain.Transaction value)` `repeated .protocol.Transaction transaction = 1;` |
    | `Chain.Transaction.Builder` | `addTransactionBuilder()` `repeated .protocol.Transaction transaction = 1;` |
    | `Chain.Transaction.Builder` | `addTransactionBuilder(int index)` `repeated .protocol.Transaction transaction = 1;` |
    | `Response.TransactionList` | `build()` |
    | `Response.TransactionList` | `buildPartial()` |
    | `Response.TransactionList.Builder` | `clear()` |
    | `Response.TransactionList.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.TransactionList.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.TransactionList.Builder` | `clearTransaction()` `repeated .protocol.Transaction transaction = 1;` |
    | `Response.TransactionList.Builder` | `clone()` |
    | `Response.TransactionList` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Chain.Transaction` | `getTransaction(int index)` `repeated .protocol.Transaction transaction = 1;` |
    | `Chain.Transaction.Builder` | `getTransactionBuilder(int index)` `repeated .protocol.Transaction transaction = 1;` |
    | `java.util.List<Chain.Transaction.Builder>` | `getTransactionBuilderList()` `repeated .protocol.Transaction transaction = 1;` |
    | `int` | `getTransactionCount()` `repeated .protocol.Transaction transaction = 1;` |
    | `java.util.List<Chain.Transaction>` | `getTransactionList()` `repeated .protocol.Transaction transaction = 1;` |
    | `Chain.TransactionOrBuilder` | `getTransactionOrBuilder(int index)` `repeated .protocol.Transaction transaction = 1;` |
    | `java.util.List<? extends Chain.TransactionOrBuilder>` | `getTransactionOrBuilderList()` `repeated .protocol.Transaction transaction = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.TransactionList.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.TransactionList.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.TransactionList.Builder` | `mergeFrom(Response.TransactionList other)` |
    | `Response.TransactionList.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.TransactionList.Builder` | `removeTransaction(int index)` `repeated .protocol.Transaction transaction = 1;` |
    | `Response.TransactionList.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionList.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.TransactionList.Builder` | `setTransaction(int index, Chain.Transaction.Builder builderForValue)` `repeated .protocol.Transaction transaction = 1;` |
    | `Response.TransactionList.Builder` | `setTransaction(int index, Chain.Transaction value)` `repeated .protocol.Transaction transaction = 1;` |
    | `Response.TransactionList.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionList.Builder>`
    - #### clear

      ```
      public Response.TransactionList.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionList.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionList.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.TransactionList getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.TransactionList build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.TransactionList buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.TransactionList.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionList.Builder>`
    - #### setField

      ```
      public Response.TransactionList.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionList.Builder>`
    - #### clearField

      ```
      public Response.TransactionList.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionList.Builder>`
    - #### clearOneof

      ```
      public Response.TransactionList.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionList.Builder>`
    - #### setRepeatedField

      ```
      public Response.TransactionList.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               int index,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionList.Builder>`
    - #### addRepeatedField

      ```
      public Response.TransactionList.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionList.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionList.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionList.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionList.Builder mergeFrom(Response.TransactionList other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionList.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionList.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                 throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionList.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getTransactionList

      ```
      public java.util.List<Chain.Transaction> getTransactionList()
      ```

      `repeated .protocol.Transaction transaction = 1;`

      Specified by:
      :   `getTransactionList` in interface `Response.TransactionListOrBuilder`
    - #### getTransactionCount

      ```
      public int getTransactionCount()
      ```

      `repeated .protocol.Transaction transaction = 1;`

      Specified by:
      :   `getTransactionCount` in interface `Response.TransactionListOrBuilder`
    - #### getTransaction

      ```
      public Chain.Transaction getTransaction(int index)
      ```

      `repeated .protocol.Transaction transaction = 1;`

      Specified by:
      :   `getTransaction` in interface `Response.TransactionListOrBuilder`
    - #### setTransaction

      ```
      public Response.TransactionList.Builder setTransaction(int index,
                                                             Chain.Transaction value)
      ```

      `repeated .protocol.Transaction transaction = 1;`
    - #### setTransaction

      ```
      public Response.TransactionList.Builder setTransaction(int index,
                                                             Chain.Transaction.Builder builderForValue)
      ```

      `repeated .protocol.Transaction transaction = 1;`
    - #### addTransaction

      ```
      public Response.TransactionList.Builder addTransaction(Chain.Transaction value)
      ```

      `repeated .protocol.Transaction transaction = 1;`
    - #### addTransaction

      ```
      public Response.TransactionList.Builder addTransaction(int index,
                                                             Chain.Transaction value)
      ```

      `repeated .protocol.Transaction transaction = 1;`
    - #### addTransaction

      ```
      public Response.TransactionList.Builder addTransaction(Chain.Transaction.Builder builderForValue)
      ```

      `repeated .protocol.Transaction transaction = 1;`
    - #### addTransaction

      ```
      public Response.TransactionList.Builder addTransaction(int index,
                                                             Chain.Transaction.Builder builderForValue)
      ```

      `repeated .protocol.Transaction transaction = 1;`
    - #### addAllTransaction

      ```
      public Response.TransactionList.Builder addAllTransaction(java.lang.Iterable<? extends Chain.Transaction> values)
      ```

      `repeated .protocol.Transaction transaction = 1;`
    - #### clearTransaction

      ```
      public Response.TransactionList.Builder clearTransaction()
      ```

      `repeated .protocol.Transaction transaction = 1;`
    - #### removeTransaction

      ```
      public Response.TransactionList.Builder removeTransaction(int index)
      ```

      `repeated .protocol.Transaction transaction = 1;`
    - #### getTransactionBuilder

      ```
      public Chain.Transaction.Builder getTransactionBuilder(int index)
      ```

      `repeated .protocol.Transaction transaction = 1;`
    - #### getTransactionOrBuilder

      ```
      public Chain.TransactionOrBuilder getTransactionOrBuilder(int index)
      ```

      `repeated .protocol.Transaction transaction = 1;`

      Specified by:
      :   `getTransactionOrBuilder` in interface `Response.TransactionListOrBuilder`
    - #### getTransactionOrBuilderList

      ```
      public java.util.List<? extends Chain.TransactionOrBuilder> getTransactionOrBuilderList()
      ```

      `repeated .protocol.Transaction transaction = 1;`

      Specified by:
      :   `getTransactionOrBuilderList` in interface `Response.TransactionListOrBuilder`
    - #### addTransactionBuilder

      ```
      public Chain.Transaction.Builder addTransactionBuilder()
      ```

      `repeated .protocol.Transaction transaction = 1;`
    - #### addTransactionBuilder

      ```
      public Chain.Transaction.Builder addTransactionBuilder(int index)
      ```

      `repeated .protocol.Transaction transaction = 1;`
    - #### getTransactionBuilderList

      ```
      public java.util.List<Chain.Transaction.Builder> getTransactionBuilderList()
      ```

      `repeated .protocol.Transaction transaction = 1;`
    - #### setUnknownFields

      ```
      public final Response.TransactionList.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionList.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.TransactionList.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionList.Builder>`