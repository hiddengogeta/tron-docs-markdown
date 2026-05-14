

org.tron.trident.proto

## Class Contract.AccountUpdateContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.AccountUpdateContract.Builder](../../../../org/tron/trident/proto/Contract.AccountUpdateContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.AccountUpdateContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.AccountUpdateContractOrBuilder](../../../../org/tron/trident/proto/Contract.AccountUpdateContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.AccountUpdateContract](../../../../org/tron/trident/proto/Contract.AccountUpdateContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.AccountUpdateContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountUpdateContract.Builder>
  implements Contract.AccountUpdateContractOrBuilder
  ```

  ```
   Update account name. Account name is not unique now.
  ```

  Protobuf type `protocol.AccountUpdateContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.AccountUpdateContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.AccountUpdateContract` | `build()` |
    | `Contract.AccountUpdateContract` | `buildPartial()` |
    | `Contract.AccountUpdateContract.Builder` | `clear()` |
    | `Contract.AccountUpdateContract.Builder` | `clearAccountName()` `bytes account_name = 1;` |
    | `Contract.AccountUpdateContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.AccountUpdateContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.AccountUpdateContract.Builder` | `clearOwnerAddress()` `bytes owner_address = 2;` |
    | `Contract.AccountUpdateContract.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getAccountName()` `bytes account_name = 1;` |
    | `Contract.AccountUpdateContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.AccountUpdateContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.AccountUpdateContract.Builder` | `mergeFrom(Contract.AccountUpdateContract other)` |
    | `Contract.AccountUpdateContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.AccountUpdateContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.AccountUpdateContract.Builder` | `setAccountName(com.google.protobuf.ByteString value)` `bytes account_name = 1;` |
    | `Contract.AccountUpdateContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.AccountUpdateContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 2;` |
    | `Contract.AccountUpdateContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.AccountUpdateContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountUpdateContract.Builder>`
    - #### clear

      ```
      public Contract.AccountUpdateContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountUpdateContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountUpdateContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.AccountUpdateContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.AccountUpdateContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.AccountUpdateContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.AccountUpdateContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountUpdateContract.Builder>`
    - #### setField

      ```
      public Contract.AccountUpdateContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                             java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountUpdateContract.Builder>`
    - #### clearField

      ```
      public Contract.AccountUpdateContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountUpdateContract.Builder>`
    - #### clearOneof

      ```
      public Contract.AccountUpdateContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountUpdateContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.AccountUpdateContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     int index,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountUpdateContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.AccountUpdateContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountUpdateContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.AccountUpdateContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.AccountUpdateContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.AccountUpdateContract.Builder mergeFrom(Contract.AccountUpdateContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountUpdateContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.AccountUpdateContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.AccountUpdateContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getAccountName

      ```
      public com.google.protobuf.ByteString getAccountName()
      ```

      `bytes account_name = 1;`

      Specified by:
      :   `getAccountName` in interface `Contract.AccountUpdateContractOrBuilder`

      Returns:
      :   The accountName.
    - #### setAccountName

      ```
      public Contract.AccountUpdateContract.Builder setAccountName(com.google.protobuf.ByteString value)
      ```

      `bytes account_name = 1;`

      Parameters:
      :   `value` - The accountName to set.

      Returns:
      :   This builder for chaining.
    - #### clearAccountName

      ```
      public Contract.AccountUpdateContract.Builder clearAccountName()
      ```

      `bytes account_name = 1;`

      Returns:
      :   This builder for chaining.
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 2;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.AccountUpdateContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.AccountUpdateContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 2;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.AccountUpdateContract.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.AccountUpdateContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountUpdateContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.AccountUpdateContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountUpdateContract.Builder>`