

org.tron.trident.proto

## Class Contract.SetAccountIdContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.SetAccountIdContract.Builder](../../../../org/tron/trident/proto/Contract.SetAccountIdContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.SetAccountIdContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.SetAccountIdContractOrBuilder](../../../../org/tron/trident/proto/Contract.SetAccountIdContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.SetAccountIdContract](../../../../org/tron/trident/proto/Contract.SetAccountIdContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.SetAccountIdContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.SetAccountIdContract.Builder>
  implements Contract.SetAccountIdContractOrBuilder
  ```

  ```
   Set account id if the account has no id. Account id is unique and case
   insensitive.
  ```

  Protobuf type `protocol.SetAccountIdContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.SetAccountIdContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.SetAccountIdContract` | `build()` |
    | `Contract.SetAccountIdContract` | `buildPartial()` |
    | `Contract.SetAccountIdContract.Builder` | `clear()` |
    | `Contract.SetAccountIdContract.Builder` | `clearAccountId()` `bytes account_id = 1;` |
    | `Contract.SetAccountIdContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.SetAccountIdContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.SetAccountIdContract.Builder` | `clearOwnerAddress()` `bytes owner_address = 2;` |
    | `Contract.SetAccountIdContract.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getAccountId()` `bytes account_id = 1;` |
    | `Contract.SetAccountIdContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.SetAccountIdContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.SetAccountIdContract.Builder` | `mergeFrom(Contract.SetAccountIdContract other)` |
    | `Contract.SetAccountIdContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.SetAccountIdContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.SetAccountIdContract.Builder` | `setAccountId(com.google.protobuf.ByteString value)` `bytes account_id = 1;` |
    | `Contract.SetAccountIdContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.SetAccountIdContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 2;` |
    | `Contract.SetAccountIdContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.SetAccountIdContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.SetAccountIdContract.Builder>`
    - #### clear

      ```
      public Contract.SetAccountIdContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.SetAccountIdContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.SetAccountIdContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.SetAccountIdContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.SetAccountIdContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.SetAccountIdContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.SetAccountIdContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.SetAccountIdContract.Builder>`
    - #### setField

      ```
      public Contract.SetAccountIdContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                            java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.SetAccountIdContract.Builder>`
    - #### clearField

      ```
      public Contract.SetAccountIdContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.SetAccountIdContract.Builder>`
    - #### clearOneof

      ```
      public Contract.SetAccountIdContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.SetAccountIdContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.SetAccountIdContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                    int index,
                                                                    java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.SetAccountIdContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.SetAccountIdContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                    java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.SetAccountIdContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.SetAccountIdContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.SetAccountIdContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.SetAccountIdContract.Builder mergeFrom(Contract.SetAccountIdContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.SetAccountIdContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.SetAccountIdContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                             com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                      throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.SetAccountIdContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getAccountId

      ```
      public com.google.protobuf.ByteString getAccountId()
      ```

      `bytes account_id = 1;`

      Specified by:
      :   `getAccountId` in interface `Contract.SetAccountIdContractOrBuilder`

      Returns:
      :   The accountId.
    - #### setAccountId

      ```
      public Contract.SetAccountIdContract.Builder setAccountId(com.google.protobuf.ByteString value)
      ```

      `bytes account_id = 1;`

      Parameters:
      :   `value` - The accountId to set.

      Returns:
      :   This builder for chaining.
    - #### clearAccountId

      ```
      public Contract.SetAccountIdContract.Builder clearAccountId()
      ```

      `bytes account_id = 1;`

      Returns:
      :   This builder for chaining.
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 2;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.SetAccountIdContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.SetAccountIdContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 2;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.SetAccountIdContract.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.SetAccountIdContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.SetAccountIdContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.SetAccountIdContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.SetAccountIdContract.Builder>`