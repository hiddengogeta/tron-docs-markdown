

org.tron.trident.proto

## Class Response.DelegatedResourceAccountIndex.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.DelegatedResourceAccountIndex.Builder](../../../../org/tron/trident/proto/Response.DelegatedResourceAccountIndex.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.DelegatedResourceAccountIndex.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.DelegatedResourceAccountIndexOrBuilder](../../../../org/tron/trident/proto/Response.DelegatedResourceAccountIndexOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.DelegatedResourceAccountIndex](../../../../org/tron/trident/proto/Response.DelegatedResourceAccountIndex.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.DelegatedResourceAccountIndex.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceAccountIndex.Builder>
  implements Response.DelegatedResourceAccountIndexOrBuilder
  ```

  Protobuf type `protocol.DelegatedResourceAccountIndex`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.DelegatedResourceAccountIndex.Builder` | `addAllFromAccounts(java.lang.Iterable<? extends com.google.protobuf.ByteString> values)` `repeated bytes fromAccounts = 2;` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `addAllToAccounts(java.lang.Iterable<? extends com.google.protobuf.ByteString> values)` `repeated bytes toAccounts = 3;` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `addFromAccounts(com.google.protobuf.ByteString value)` `repeated bytes fromAccounts = 2;` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `addToAccounts(com.google.protobuf.ByteString value)` `repeated bytes toAccounts = 3;` |
    | `Response.DelegatedResourceAccountIndex` | `build()` |
    | `Response.DelegatedResourceAccountIndex` | `buildPartial()` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `clear()` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `clearAccount()` `bytes account = 1;` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `clearFromAccounts()` `repeated bytes fromAccounts = 2;` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `clearTimestamp()` `int64 timestamp = 4;` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `clearToAccounts()` `repeated bytes toAccounts = 3;` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getAccount()` `bytes account = 1;` |
    | `Response.DelegatedResourceAccountIndex` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getFromAccounts(int index)` `repeated bytes fromAccounts = 2;` |
    | `int` | `getFromAccountsCount()` `repeated bytes fromAccounts = 2;` |
    | `java.util.List<com.google.protobuf.ByteString>` | `getFromAccountsList()` `repeated bytes fromAccounts = 2;` |
    | `long` | `getTimestamp()` `int64 timestamp = 4;` |
    | `com.google.protobuf.ByteString` | `getToAccounts(int index)` `repeated bytes toAccounts = 3;` |
    | `int` | `getToAccountsCount()` `repeated bytes toAccounts = 3;` |
    | `java.util.List<com.google.protobuf.ByteString>` | `getToAccountsList()` `repeated bytes toAccounts = 3;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `mergeFrom(Response.DelegatedResourceAccountIndex other)` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `setAccount(com.google.protobuf.ByteString value)` `bytes account = 1;` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `setFromAccounts(int index, com.google.protobuf.ByteString value)` `repeated bytes fromAccounts = 2;` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `setTimestamp(long value)` `int64 timestamp = 4;` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `setToAccounts(int index, com.google.protobuf.ByteString value)` `repeated bytes toAccounts = 3;` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceAccountIndex.Builder>`
    - #### clear

      ```
      public Response.DelegatedResourceAccountIndex.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceAccountIndex.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceAccountIndex.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.DelegatedResourceAccountIndex getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.DelegatedResourceAccountIndex build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.DelegatedResourceAccountIndex buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.DelegatedResourceAccountIndex.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceAccountIndex.Builder>`
    - #### setField

      ```
      public Response.DelegatedResourceAccountIndex.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceAccountIndex.Builder>`
    - #### clearField

      ```
      public Response.DelegatedResourceAccountIndex.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceAccountIndex.Builder>`
    - #### clearOneof

      ```
      public Response.DelegatedResourceAccountIndex.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceAccountIndex.Builder>`
    - #### setRepeatedField

      ```
      public Response.DelegatedResourceAccountIndex.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                             int index,
                                                                             java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceAccountIndex.Builder>`
    - #### addRepeatedField

      ```
      public Response.DelegatedResourceAccountIndex.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                             java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceAccountIndex.Builder>`
    - #### mergeFrom

      ```
      public Response.DelegatedResourceAccountIndex.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.DelegatedResourceAccountIndex.Builder>`
    - #### mergeFrom

      ```
      public Response.DelegatedResourceAccountIndex.Builder mergeFrom(Response.DelegatedResourceAccountIndex other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceAccountIndex.Builder>`
    - #### mergeFrom

      ```
      public Response.DelegatedResourceAccountIndex.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                               throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.DelegatedResourceAccountIndex.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getAccount

      ```
      public com.google.protobuf.ByteString getAccount()
      ```

      `bytes account = 1;`

      Specified by:
      :   `getAccount` in interface `Response.DelegatedResourceAccountIndexOrBuilder`

      Returns:
      :   The account.
    - #### setAccount

      ```
      public Response.DelegatedResourceAccountIndex.Builder setAccount(com.google.protobuf.ByteString value)
      ```

      `bytes account = 1;`

      Parameters:
      :   `value` - The account to set.

      Returns:
      :   This builder for chaining.
    - #### clearAccount

      ```
      public Response.DelegatedResourceAccountIndex.Builder clearAccount()
      ```

      `bytes account = 1;`

      Returns:
      :   This builder for chaining.
    - #### getFromAccountsList

      ```
      public java.util.List<com.google.protobuf.ByteString> getFromAccountsList()
      ```

      `repeated bytes fromAccounts = 2;`

      Specified by:
      :   `getFromAccountsList` in interface `Response.DelegatedResourceAccountIndexOrBuilder`

      Returns:
      :   A list containing the fromAccounts.
    - #### getFromAccountsCount

      ```
      public int getFromAccountsCount()
      ```

      `repeated bytes fromAccounts = 2;`

      Specified by:
      :   `getFromAccountsCount` in interface `Response.DelegatedResourceAccountIndexOrBuilder`

      Returns:
      :   The count of fromAccounts.
    - #### getFromAccounts

      ```
      public com.google.protobuf.ByteString getFromAccounts(int index)
      ```

      `repeated bytes fromAccounts = 2;`

      Specified by:
      :   `getFromAccounts` in interface `Response.DelegatedResourceAccountIndexOrBuilder`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The fromAccounts at the given index.
    - #### setFromAccounts

      ```
      public Response.DelegatedResourceAccountIndex.Builder setFromAccounts(int index,
                                                                            com.google.protobuf.ByteString value)
      ```

      `repeated bytes fromAccounts = 2;`

      Parameters:
      :   `index` - The index to set the value at.
      :   `value` - The fromAccounts to set.

      Returns:
      :   This builder for chaining.
    - #### addFromAccounts

      ```
      public Response.DelegatedResourceAccountIndex.Builder addFromAccounts(com.google.protobuf.ByteString value)
      ```

      `repeated bytes fromAccounts = 2;`

      Parameters:
      :   `value` - The fromAccounts to add.

      Returns:
      :   This builder for chaining.
    - #### addAllFromAccounts

      ```
      public Response.DelegatedResourceAccountIndex.Builder addAllFromAccounts(java.lang.Iterable<? extends com.google.protobuf.ByteString> values)
      ```

      `repeated bytes fromAccounts = 2;`

      Parameters:
      :   `values` - The fromAccounts to add.

      Returns:
      :   This builder for chaining.
    - #### clearFromAccounts

      ```
      public Response.DelegatedResourceAccountIndex.Builder clearFromAccounts()
      ```

      `repeated bytes fromAccounts = 2;`

      Returns:
      :   This builder for chaining.
    - #### getToAccountsList

      ```
      public java.util.List<com.google.protobuf.ByteString> getToAccountsList()
      ```

      `repeated bytes toAccounts = 3;`

      Specified by:
      :   `getToAccountsList` in interface `Response.DelegatedResourceAccountIndexOrBuilder`

      Returns:
      :   A list containing the toAccounts.
    - #### getToAccountsCount

      ```
      public int getToAccountsCount()
      ```

      `repeated bytes toAccounts = 3;`

      Specified by:
      :   `getToAccountsCount` in interface `Response.DelegatedResourceAccountIndexOrBuilder`

      Returns:
      :   The count of toAccounts.
    - #### getToAccounts

      ```
      public com.google.protobuf.ByteString getToAccounts(int index)
      ```

      `repeated bytes toAccounts = 3;`

      Specified by:
      :   `getToAccounts` in interface `Response.DelegatedResourceAccountIndexOrBuilder`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The toAccounts at the given index.
    - #### setToAccounts

      ```
      public Response.DelegatedResourceAccountIndex.Builder setToAccounts(int index,
                                                                          com.google.protobuf.ByteString value)
      ```

      `repeated bytes toAccounts = 3;`

      Parameters:
      :   `index` - The index to set the value at.
      :   `value` - The toAccounts to set.

      Returns:
      :   This builder for chaining.
    - #### addToAccounts

      ```
      public Response.DelegatedResourceAccountIndex.Builder addToAccounts(com.google.protobuf.ByteString value)
      ```

      `repeated bytes toAccounts = 3;`

      Parameters:
      :   `value` - The toAccounts to add.

      Returns:
      :   This builder for chaining.
    - #### addAllToAccounts

      ```
      public Response.DelegatedResourceAccountIndex.Builder addAllToAccounts(java.lang.Iterable<? extends com.google.protobuf.ByteString> values)
      ```

      `repeated bytes toAccounts = 3;`

      Parameters:
      :   `values` - The toAccounts to add.

      Returns:
      :   This builder for chaining.
    - #### clearToAccounts

      ```
      public Response.DelegatedResourceAccountIndex.Builder clearToAccounts()
      ```

      `repeated bytes toAccounts = 3;`

      Returns:
      :   This builder for chaining.
    - #### getTimestamp

      ```
      public long getTimestamp()
      ```

      `int64 timestamp = 4;`

      Specified by:
      :   `getTimestamp` in interface `Response.DelegatedResourceAccountIndexOrBuilder`

      Returns:
      :   The timestamp.
    - #### setTimestamp

      ```
      public Response.DelegatedResourceAccountIndex.Builder setTimestamp(long value)
      ```

      `int64 timestamp = 4;`

      Parameters:
      :   `value` - The timestamp to set.

      Returns:
      :   This builder for chaining.
    - #### clearTimestamp

      ```
      public Response.DelegatedResourceAccountIndex.Builder clearTimestamp()
      ```

      `int64 timestamp = 4;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.DelegatedResourceAccountIndex.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceAccountIndex.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.DelegatedResourceAccountIndex.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceAccountIndex.Builder>`