

org.tron.trident.proto

## Class Response.TransactionSignWeight.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.TransactionSignWeight.Builder](../../../../org/tron/trident/proto/Response.TransactionSignWeight.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.TransactionSignWeight.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.TransactionSignWeightOrBuilder](../../../../org/tron/trident/proto/Response.TransactionSignWeightOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.TransactionSignWeight](../../../../org/tron/trident/proto/Response.TransactionSignWeight.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.TransactionSignWeight.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Builder>
  implements Response.TransactionSignWeightOrBuilder
  ```

  Protobuf type `protocol.TransactionSignWeight`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.TransactionSignWeight.Builder` | `addAllApprovedList(java.lang.Iterable<? extends com.google.protobuf.ByteString> values)` `repeated bytes approved_list = 2;` |
    | `Response.TransactionSignWeight.Builder` | `addApprovedList(com.google.protobuf.ByteString value)` `repeated bytes approved_list = 2;` |
    | `Response.TransactionSignWeight.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionSignWeight` | `build()` |
    | `Response.TransactionSignWeight` | `buildPartial()` |
    | `Response.TransactionSignWeight.Builder` | `clear()` |
    | `Response.TransactionSignWeight.Builder` | `clearApprovedList()` `repeated bytes approved_list = 2;` |
    | `Response.TransactionSignWeight.Builder` | `clearCurrentWeight()` `int64 current_weight = 3;` |
    | `Response.TransactionSignWeight.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.TransactionSignWeight.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.TransactionSignWeight.Builder` | `clearPermission()` `.protocol.Permission permission = 1;` |
    | `Response.TransactionSignWeight.Builder` | `clearResult()` `.protocol.TransactionSignWeight.Result result = 4;` |
    | `Response.TransactionSignWeight.Builder` | `clearTransaction()` `.protocol.TransactionExtention transaction = 5;` |
    | `Response.TransactionSignWeight.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getApprovedList(int index)` `repeated bytes approved_list = 2;` |
    | `int` | `getApprovedListCount()` `repeated bytes approved_list = 2;` |
    | `java.util.List<com.google.protobuf.ByteString>` | `getApprovedListList()` `repeated bytes approved_list = 2;` |
    | `long` | `getCurrentWeight()` `int64 current_weight = 3;` |
    | `Response.TransactionSignWeight` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Common.Permission` | `getPermission()` `.protocol.Permission permission = 1;` |
    | `Common.Permission.Builder` | `getPermissionBuilder()` `.protocol.Permission permission = 1;` |
    | `Common.PermissionOrBuilder` | `getPermissionOrBuilder()` `.protocol.Permission permission = 1;` |
    | `Response.TransactionSignWeight.Result` | `getResult()` `.protocol.TransactionSignWeight.Result result = 4;` |
    | `Response.TransactionSignWeight.Result.Builder` | `getResultBuilder()` `.protocol.TransactionSignWeight.Result result = 4;` |
    | `Response.TransactionSignWeight.ResultOrBuilder` | `getResultOrBuilder()` `.protocol.TransactionSignWeight.Result result = 4;` |
    | `Response.TransactionExtention` | `getTransaction()` `.protocol.TransactionExtention transaction = 5;` |
    | `Response.TransactionExtention.Builder` | `getTransactionBuilder()` `.protocol.TransactionExtention transaction = 5;` |
    | `Response.TransactionExtentionOrBuilder` | `getTransactionOrBuilder()` `.protocol.TransactionExtention transaction = 5;` |
    | `boolean` | `hasPermission()` `.protocol.Permission permission = 1;` |
    | `boolean` | `hasResult()` `.protocol.TransactionSignWeight.Result result = 4;` |
    | `boolean` | `hasTransaction()` `.protocol.TransactionExtention transaction = 5;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.TransactionSignWeight.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.TransactionSignWeight.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.TransactionSignWeight.Builder` | `mergeFrom(Response.TransactionSignWeight other)` |
    | `Response.TransactionSignWeight.Builder` | `mergePermission(Common.Permission value)` `.protocol.Permission permission = 1;` |
    | `Response.TransactionSignWeight.Builder` | `mergeResult(Response.TransactionSignWeight.Result value)` `.protocol.TransactionSignWeight.Result result = 4;` |
    | `Response.TransactionSignWeight.Builder` | `mergeTransaction(Response.TransactionExtention value)` `.protocol.TransactionExtention transaction = 5;` |
    | `Response.TransactionSignWeight.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.TransactionSignWeight.Builder` | `setApprovedList(int index, com.google.protobuf.ByteString value)` `repeated bytes approved_list = 2;` |
    | `Response.TransactionSignWeight.Builder` | `setCurrentWeight(long value)` `int64 current_weight = 3;` |
    | `Response.TransactionSignWeight.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionSignWeight.Builder` | `setPermission(Common.Permission.Builder builderForValue)` `.protocol.Permission permission = 1;` |
    | `Response.TransactionSignWeight.Builder` | `setPermission(Common.Permission value)` `.protocol.Permission permission = 1;` |
    | `Response.TransactionSignWeight.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.TransactionSignWeight.Builder` | `setResult(Response.TransactionSignWeight.Result.Builder builderForValue)` `.protocol.TransactionSignWeight.Result result = 4;` |
    | `Response.TransactionSignWeight.Builder` | `setResult(Response.TransactionSignWeight.Result value)` `.protocol.TransactionSignWeight.Result result = 4;` |
    | `Response.TransactionSignWeight.Builder` | `setTransaction(Response.TransactionExtention.Builder builderForValue)` `.protocol.TransactionExtention transaction = 5;` |
    | `Response.TransactionSignWeight.Builder` | `setTransaction(Response.TransactionExtention value)` `.protocol.TransactionExtention transaction = 5;` |
    | `Response.TransactionSignWeight.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Builder>`
    - #### clear

      ```
      public Response.TransactionSignWeight.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.TransactionSignWeight getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.TransactionSignWeight build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.TransactionSignWeight buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.TransactionSignWeight.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Builder>`
    - #### setField

      ```
      public Response.TransactionSignWeight.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                             java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Builder>`
    - #### clearField

      ```
      public Response.TransactionSignWeight.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Builder>`
    - #### clearOneof

      ```
      public Response.TransactionSignWeight.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Builder>`
    - #### setRepeatedField

      ```
      public Response.TransactionSignWeight.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     int index,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Builder>`
    - #### addRepeatedField

      ```
      public Response.TransactionSignWeight.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionSignWeight.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionSignWeight.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionSignWeight.Builder mergeFrom(Response.TransactionSignWeight other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionSignWeight.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionSignWeight.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### hasPermission

      ```
      public boolean hasPermission()
      ```

      `.protocol.Permission permission = 1;`

      Specified by:
      :   `hasPermission` in interface `Response.TransactionSignWeightOrBuilder`

      Returns:
      :   Whether the permission field is set.
    - #### getPermission

      ```
      public Common.Permission getPermission()
      ```

      `.protocol.Permission permission = 1;`

      Specified by:
      :   `getPermission` in interface `Response.TransactionSignWeightOrBuilder`

      Returns:
      :   The permission.
    - #### setPermission

      ```
      public Response.TransactionSignWeight.Builder setPermission(Common.Permission value)
      ```

      `.protocol.Permission permission = 1;`
    - #### setPermission

      ```
      public Response.TransactionSignWeight.Builder setPermission(Common.Permission.Builder builderForValue)
      ```

      `.protocol.Permission permission = 1;`
    - #### mergePermission

      ```
      public Response.TransactionSignWeight.Builder mergePermission(Common.Permission value)
      ```

      `.protocol.Permission permission = 1;`
    - #### clearPermission

      ```
      public Response.TransactionSignWeight.Builder clearPermission()
      ```

      `.protocol.Permission permission = 1;`
    - #### getPermissionBuilder

      ```
      public Common.Permission.Builder getPermissionBuilder()
      ```

      `.protocol.Permission permission = 1;`
    - #### getPermissionOrBuilder

      ```
      public Common.PermissionOrBuilder getPermissionOrBuilder()
      ```

      `.protocol.Permission permission = 1;`

      Specified by:
      :   `getPermissionOrBuilder` in interface `Response.TransactionSignWeightOrBuilder`
    - #### getApprovedListList

      ```
      public java.util.List<com.google.protobuf.ByteString> getApprovedListList()
      ```

      `repeated bytes approved_list = 2;`

      Specified by:
      :   `getApprovedListList` in interface `Response.TransactionSignWeightOrBuilder`

      Returns:
      :   A list containing the approvedList.
    - #### getApprovedListCount

      ```
      public int getApprovedListCount()
      ```

      `repeated bytes approved_list = 2;`

      Specified by:
      :   `getApprovedListCount` in interface `Response.TransactionSignWeightOrBuilder`

      Returns:
      :   The count of approvedList.
    - #### getApprovedList

      ```
      public com.google.protobuf.ByteString getApprovedList(int index)
      ```

      `repeated bytes approved_list = 2;`

      Specified by:
      :   `getApprovedList` in interface `Response.TransactionSignWeightOrBuilder`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The approvedList at the given index.
    - #### setApprovedList

      ```
      public Response.TransactionSignWeight.Builder setApprovedList(int index,
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
      public Response.TransactionSignWeight.Builder addApprovedList(com.google.protobuf.ByteString value)
      ```

      `repeated bytes approved_list = 2;`

      Parameters:
      :   `value` - The approvedList to add.

      Returns:
      :   This builder for chaining.
    - #### addAllApprovedList

      ```
      public Response.TransactionSignWeight.Builder addAllApprovedList(java.lang.Iterable<? extends com.google.protobuf.ByteString> values)
      ```

      `repeated bytes approved_list = 2;`

      Parameters:
      :   `values` - The approvedList to add.

      Returns:
      :   This builder for chaining.
    - #### clearApprovedList

      ```
      public Response.TransactionSignWeight.Builder clearApprovedList()
      ```

      `repeated bytes approved_list = 2;`

      Returns:
      :   This builder for chaining.
    - #### getCurrentWeight

      ```
      public long getCurrentWeight()
      ```

      `int64 current_weight = 3;`

      Specified by:
      :   `getCurrentWeight` in interface `Response.TransactionSignWeightOrBuilder`

      Returns:
      :   The currentWeight.
    - #### setCurrentWeight

      ```
      public Response.TransactionSignWeight.Builder setCurrentWeight(long value)
      ```

      `int64 current_weight = 3;`

      Parameters:
      :   `value` - The currentWeight to set.

      Returns:
      :   This builder for chaining.
    - #### clearCurrentWeight

      ```
      public Response.TransactionSignWeight.Builder clearCurrentWeight()
      ```

      `int64 current_weight = 3;`

      Returns:
      :   This builder for chaining.
    - #### hasResult

      ```
      public boolean hasResult()
      ```

      `.protocol.TransactionSignWeight.Result result = 4;`

      Specified by:
      :   `hasResult` in interface `Response.TransactionSignWeightOrBuilder`

      Returns:
      :   Whether the result field is set.
    - #### getResult

      ```
      public Response.TransactionSignWeight.Result getResult()
      ```

      `.protocol.TransactionSignWeight.Result result = 4;`

      Specified by:
      :   `getResult` in interface `Response.TransactionSignWeightOrBuilder`

      Returns:
      :   The result.
    - #### setResult

      ```
      public Response.TransactionSignWeight.Builder setResult(Response.TransactionSignWeight.Result value)
      ```

      `.protocol.TransactionSignWeight.Result result = 4;`
    - #### setResult

      ```
      public Response.TransactionSignWeight.Builder setResult(Response.TransactionSignWeight.Result.Builder builderForValue)
      ```

      `.protocol.TransactionSignWeight.Result result = 4;`
    - #### mergeResult

      ```
      public Response.TransactionSignWeight.Builder mergeResult(Response.TransactionSignWeight.Result value)
      ```

      `.protocol.TransactionSignWeight.Result result = 4;`
    - #### clearResult

      ```
      public Response.TransactionSignWeight.Builder clearResult()
      ```

      `.protocol.TransactionSignWeight.Result result = 4;`
    - #### getResultBuilder

      ```
      public Response.TransactionSignWeight.Result.Builder getResultBuilder()
      ```

      `.protocol.TransactionSignWeight.Result result = 4;`
    - #### getResultOrBuilder

      ```
      public Response.TransactionSignWeight.ResultOrBuilder getResultOrBuilder()
      ```

      `.protocol.TransactionSignWeight.Result result = 4;`

      Specified by:
      :   `getResultOrBuilder` in interface `Response.TransactionSignWeightOrBuilder`
    - #### hasTransaction

      ```
      public boolean hasTransaction()
      ```

      `.protocol.TransactionExtention transaction = 5;`

      Specified by:
      :   `hasTransaction` in interface `Response.TransactionSignWeightOrBuilder`

      Returns:
      :   Whether the transaction field is set.
    - #### getTransaction

      ```
      public Response.TransactionExtention getTransaction()
      ```

      `.protocol.TransactionExtention transaction = 5;`

      Specified by:
      :   `getTransaction` in interface `Response.TransactionSignWeightOrBuilder`

      Returns:
      :   The transaction.
    - #### setTransaction

      ```
      public Response.TransactionSignWeight.Builder setTransaction(Response.TransactionExtention value)
      ```

      `.protocol.TransactionExtention transaction = 5;`
    - #### setTransaction

      ```
      public Response.TransactionSignWeight.Builder setTransaction(Response.TransactionExtention.Builder builderForValue)
      ```

      `.protocol.TransactionExtention transaction = 5;`
    - #### mergeTransaction

      ```
      public Response.TransactionSignWeight.Builder mergeTransaction(Response.TransactionExtention value)
      ```

      `.protocol.TransactionExtention transaction = 5;`
    - #### clearTransaction

      ```
      public Response.TransactionSignWeight.Builder clearTransaction()
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
      :   `getTransactionOrBuilder` in interface `Response.TransactionSignWeightOrBuilder`
    - #### setUnknownFields

      ```
      public final Response.TransactionSignWeight.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.TransactionSignWeight.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionSignWeight.Builder>`