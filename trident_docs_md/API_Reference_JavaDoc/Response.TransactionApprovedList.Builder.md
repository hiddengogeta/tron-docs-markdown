

org.tron.trident.proto

## Class Response.TransactionApprovedList.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.TransactionApprovedList.Builder](../../../../org/tron/trident/proto/Response.TransactionApprovedList.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.TransactionApprovedList.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.TransactionApprovedListOrBuilder](../../../../org/tron/trident/proto/Response.TransactionApprovedListOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.TransactionApprovedList](../../../../org/tron/trident/proto/Response.TransactionApprovedList.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.TransactionApprovedList.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Builder>
  implements Response.TransactionApprovedListOrBuilder
  ```

  Protobuf type `protocol.TransactionApprovedList`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.TransactionApprovedList.Builder` | `addAllApprovedList(java.lang.Iterable<? extends com.google.protobuf.ByteString> values)` `repeated bytes approved_list = 2;` |
    | `Response.TransactionApprovedList.Builder` | `addApprovedList(com.google.protobuf.ByteString value)` `repeated bytes approved_list = 2;` |
    | `Response.TransactionApprovedList.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionApprovedList` | `build()` |
    | `Response.TransactionApprovedList` | `buildPartial()` |
    | `Response.TransactionApprovedList.Builder` | `clear()` |
    | `Response.TransactionApprovedList.Builder` | `clearApprovedList()` `repeated bytes approved_list = 2;` |
    | `Response.TransactionApprovedList.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.TransactionApprovedList.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.TransactionApprovedList.Builder` | `clearResult()` `.protocol.TransactionApprovedList.Result result = 4;` |
    | `Response.TransactionApprovedList.Builder` | `clearTransaction()` `.protocol.TransactionExtention transaction = 5;` |
    | `Response.TransactionApprovedList.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getApprovedList(int index)` `repeated bytes approved_list = 2;` |
    | `int` | `getApprovedListCount()` `repeated bytes approved_list = 2;` |
    | `java.util.List<com.google.protobuf.ByteString>` | `getApprovedListList()` `repeated bytes approved_list = 2;` |
    | `Response.TransactionApprovedList` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Response.TransactionApprovedList.Result` | `getResult()` `.protocol.TransactionApprovedList.Result result = 4;` |
    | `Response.TransactionApprovedList.Result.Builder` | `getResultBuilder()` `.protocol.TransactionApprovedList.Result result = 4;` |
    | `Response.TransactionApprovedList.ResultOrBuilder` | `getResultOrBuilder()` `.protocol.TransactionApprovedList.Result result = 4;` |
    | `Response.TransactionExtention` | `getTransaction()` `.protocol.TransactionExtention transaction = 5;` |
    | `Response.TransactionExtention.Builder` | `getTransactionBuilder()` `.protocol.TransactionExtention transaction = 5;` |
    | `Response.TransactionExtentionOrBuilder` | `getTransactionOrBuilder()` `.protocol.TransactionExtention transaction = 5;` |
    | `boolean` | `hasResult()` `.protocol.TransactionApprovedList.Result result = 4;` |
    | `boolean` | `hasTransaction()` `.protocol.TransactionExtention transaction = 5;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.TransactionApprovedList.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.TransactionApprovedList.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.TransactionApprovedList.Builder` | `mergeFrom(Response.TransactionApprovedList other)` |
    | `Response.TransactionApprovedList.Builder` | `mergeResult(Response.TransactionApprovedList.Result value)` `.protocol.TransactionApprovedList.Result result = 4;` |
    | `Response.TransactionApprovedList.Builder` | `mergeTransaction(Response.TransactionExtention value)` `.protocol.TransactionExtention transaction = 5;` |
    | `Response.TransactionApprovedList.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.TransactionApprovedList.Builder` | `setApprovedList(int index, com.google.protobuf.ByteString value)` `repeated bytes approved_list = 2;` |
    | `Response.TransactionApprovedList.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionApprovedList.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.TransactionApprovedList.Builder` | `setResult(Response.TransactionApprovedList.Result.Builder builderForValue)` `.protocol.TransactionApprovedList.Result result = 4;` |
    | `Response.TransactionApprovedList.Builder` | `setResult(Response.TransactionApprovedList.Result value)` `.protocol.TransactionApprovedList.Result result = 4;` |
    | `Response.TransactionApprovedList.Builder` | `setTransaction(Response.TransactionExtention.Builder builderForValue)` `.protocol.TransactionExtention transaction = 5;` |
    | `Response.TransactionApprovedList.Builder` | `setTransaction(Response.TransactionExtention value)` `.protocol.TransactionExtention transaction = 5;` |
    | `Response.TransactionApprovedList.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Builder>`
    - #### clear

      ```
      public Response.TransactionApprovedList.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.TransactionApprovedList getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.TransactionApprovedList build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.TransactionApprovedList buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.TransactionApprovedList.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Builder>`
    - #### setField

      ```
      public Response.TransactionApprovedList.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Builder>`
    - #### clearField

      ```
      public Response.TransactionApprovedList.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Builder>`
    - #### clearOneof

      ```
      public Response.TransactionApprovedList.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Builder>`
    - #### setRepeatedField

      ```
      public Response.TransactionApprovedList.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                       int index,
                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Builder>`
    - #### addRepeatedField

      ```
      public Response.TransactionApprovedList.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionApprovedList.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionApprovedList.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionApprovedList.Builder mergeFrom(Response.TransactionApprovedList other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionApprovedList.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionApprovedList.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getApprovedListList

      ```
      public java.util.List<com.google.protobuf.ByteString> getApprovedListList()
      ```

      `repeated bytes approved_list = 2;`

      Specified by:
      :   `getApprovedListList` in interface `Response.TransactionApprovedListOrBuilder`

      Returns:
      :   A list containing the approvedList.
    - #### getApprovedListCount

      ```
      public int getApprovedListCount()
      ```

      `repeated bytes approved_list = 2;`

      Specified by:
      :   `getApprovedListCount` in interface `Response.TransactionApprovedListOrBuilder`

      Returns:
      :   The count of approvedList.
    - #### getApprovedList

      ```
      public com.google.protobuf.ByteString getApprovedList(int index)
      ```

      `repeated bytes approved_list = 2;`

      Specified by:
      :   `getApprovedList` in interface `Response.TransactionApprovedListOrBuilder`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The approvedList at the given index.
    - #### setApprovedList

      ```
      public Response.TransactionApprovedList.Builder setApprovedList(int index,
                                                                      com.google.protobuf.ByteString value)
      ```

      `repeated bytes approved_list = 2;`

      Parameters:
      :   `index` - The index to set the value at.
      :   `value` - The approvedList to set.

      Returns:
      :   This builder for chaining.
    - #### addApprovedList

      ```
      public Response.TransactionApprovedList.Builder addApprovedList(com.google.protobuf.ByteString value)
      ```

      `repeated bytes approved_list = 2;`

      Parameters:
      :   `value` - The approvedList to add.

      Returns:
      :   This builder for chaining.
    - #### addAllApprovedList

      ```
      public Response.TransactionApprovedList.Builder addAllApprovedList(java.lang.Iterable<? extends com.google.protobuf.ByteString> values)
      ```

      `repeated bytes approved_list = 2;`

      Parameters:
      :   `values` - The approvedList to add.

      Returns:
      :   This builder for chaining.
    - #### clearApprovedList

      ```
      public Response.TransactionApprovedList.Builder clearApprovedList()
      ```

      `repeated bytes approved_list = 2;`

      Returns:
      :   This builder for chaining.
    - #### hasResult

      ```
      public boolean hasResult()
      ```

      `.protocol.TransactionApprovedList.Result result = 4;`

      Specified by:
      :   `hasResult` in interface `Response.TransactionApprovedListOrBuilder`

      Returns:
      :   Whether the result field is set.
    - #### getResult

      ```
      public Response.TransactionApprovedList.Result getResult()
      ```

      `.protocol.TransactionApprovedList.Result result = 4;`

      Specified by:
      :   `getResult` in interface `Response.TransactionApprovedListOrBuilder`

      Returns:
      :   The result.
    - #### setResult

      ```
      public Response.TransactionApprovedList.Builder setResult(Response.TransactionApprovedList.Result value)
      ```

      `.protocol.TransactionApprovedList.Result result = 4;`
    - #### setResult

      ```
      public Response.TransactionApprovedList.Builder setResult(Response.TransactionApprovedList.Result.Builder builderForValue)
      ```

      `.protocol.TransactionApprovedList.Result result = 4;`
    - #### mergeResult

      ```
      public Response.TransactionApprovedList.Builder mergeResult(Response.TransactionApprovedList.Result value)
      ```

      `.protocol.TransactionApprovedList.Result result = 4;`
    - #### clearResult

      ```
      public Response.TransactionApprovedList.Builder clearResult()
      ```

      `.protocol.TransactionApprovedList.Result result = 4;`
    - #### getResultBuilder

      ```
      public Response.TransactionApprovedList.Result.Builder getResultBuilder()
      ```

      `.protocol.TransactionApprovedList.Result result = 4;`
    - #### getResultOrBuilder

      ```
      public Response.TransactionApprovedList.ResultOrBuilder getResultOrBuilder()
      ```

      `.protocol.TransactionApprovedList.Result result = 4;`

      Specified by:
      :   `getResultOrBuilder` in interface `Response.TransactionApprovedListOrBuilder`
    - #### hasTransaction

      ```
      public boolean hasTransaction()
      ```

      `.protocol.TransactionExtention transaction = 5;`

      Specified by:
      :   `hasTransaction` in interface `Response.TransactionApprovedListOrBuilder`

      Returns:
      :   Whether the transaction field is set.
    - #### getTransaction

      ```
      public Response.TransactionExtention getTransaction()
      ```

      `.protocol.TransactionExtention transaction = 5;`

      Specified by:
      :   `getTransaction` in interface `Response.TransactionApprovedListOrBuilder`

      Returns:
      :   The transaction.
    - #### setTransaction

      ```
      public Response.TransactionApprovedList.Builder setTransaction(Response.TransactionExtention value)
      ```

      `.protocol.TransactionExtention transaction = 5;`
    - #### setTransaction

      ```
      public Response.TransactionApprovedList.Builder setTransaction(Response.TransactionExtention.Builder builderForValue)
      ```

      `.protocol.TransactionExtention transaction = 5;`
    - #### mergeTransaction

      ```
      public Response.TransactionApprovedList.Builder mergeTransaction(Response.TransactionExtention value)
      ```

      `.protocol.TransactionExtention transaction = 5;`
    - #### clearTransaction

      ```
      public Response.TransactionApprovedList.Builder clearTransaction()
      ```

      `.protocol.TransactionExtention transaction = 5;`
    - #### getTransactionBuilder

      ```
      public Response.TransactionExtention.Builder getTransactionBuilder()
      ```

      `.protocol.TransactionExtention transaction = 5;`
    - #### getTransactionOrBuilder

      ```
      public Response.TransactionExtentionOrBuilder getTransactionOrBuilder()
      ```

      `.protocol.TransactionExtention transaction = 5;`

      Specified by:
      :   `getTransactionOrBuilder` in interface `Response.TransactionApprovedListOrBuilder`
    - #### setUnknownFields

      ```
      public final Response.TransactionApprovedList.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.TransactionApprovedList.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionApprovedList.Builder>`