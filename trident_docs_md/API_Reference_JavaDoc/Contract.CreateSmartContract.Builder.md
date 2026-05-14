

org.tron.trident.proto

## Class Contract.CreateSmartContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.CreateSmartContract.Builder](../../../../org/tron/trident/proto/Contract.CreateSmartContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.CreateSmartContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.CreateSmartContractOrBuilder](../../../../org/tron/trident/proto/Contract.CreateSmartContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.CreateSmartContract](../../../../org/tron/trident/proto/Contract.CreateSmartContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.CreateSmartContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.CreateSmartContract.Builder>
  implements Contract.CreateSmartContractOrBuilder
  ```

  Protobuf type `protocol.CreateSmartContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.CreateSmartContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.CreateSmartContract` | `build()` |
    | `Contract.CreateSmartContract` | `buildPartial()` |
    | `Contract.CreateSmartContract.Builder` | `clear()` |
    | `Contract.CreateSmartContract.Builder` | `clearCallTokenValue()` `int64 call_token_value = 3;` |
    | `Contract.CreateSmartContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.CreateSmartContract.Builder` | `clearNewContract()` `.protocol.SmartContract new_contract = 2;` |
    | `Contract.CreateSmartContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.CreateSmartContract.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `Contract.CreateSmartContract.Builder` | `clearTokenId()` `int64 token_id = 4;` |
    | `Contract.CreateSmartContract.Builder` | `clone()` |
    | `long` | `getCallTokenValue()` `int64 call_token_value = 3;` |
    | `Contract.CreateSmartContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Common.SmartContract` | `getNewContract()` `.protocol.SmartContract new_contract = 2;` |
    | `Common.SmartContract.Builder` | `getNewContractBuilder()` `.protocol.SmartContract new_contract = 2;` |
    | `Common.SmartContractOrBuilder` | `getNewContractOrBuilder()` `.protocol.SmartContract new_contract = 2;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `long` | `getTokenId()` `int64 token_id = 4;` |
    | `boolean` | `hasNewContract()` `.protocol.SmartContract new_contract = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.CreateSmartContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.CreateSmartContract.Builder` | `mergeFrom(Contract.CreateSmartContract other)` |
    | `Contract.CreateSmartContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.CreateSmartContract.Builder` | `mergeNewContract(Common.SmartContract value)` `.protocol.SmartContract new_contract = 2;` |
    | `Contract.CreateSmartContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.CreateSmartContract.Builder` | `setCallTokenValue(long value)` `int64 call_token_value = 3;` |
    | `Contract.CreateSmartContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.CreateSmartContract.Builder` | `setNewContract(Common.SmartContract.Builder builderForValue)` `.protocol.SmartContract new_contract = 2;` |
    | `Contract.CreateSmartContract.Builder` | `setNewContract(Common.SmartContract value)` `.protocol.SmartContract new_contract = 2;` |
    | `Contract.CreateSmartContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `Contract.CreateSmartContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.CreateSmartContract.Builder` | `setTokenId(long value)` `int64 token_id = 4;` |
    | `Contract.CreateSmartContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.CreateSmartContract.Builder>`
    - #### clear

      ```
      public Contract.CreateSmartContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.CreateSmartContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.CreateSmartContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.CreateSmartContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.CreateSmartContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.CreateSmartContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.CreateSmartContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.CreateSmartContract.Builder>`
    - #### setField

      ```
      public Contract.CreateSmartContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                           java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.CreateSmartContract.Builder>`
    - #### clearField

      ```
      public Contract.CreateSmartContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.CreateSmartContract.Builder>`
    - #### clearOneof

      ```
      public Contract.CreateSmartContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.CreateSmartContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.CreateSmartContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                   int index,
                                                                   java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.CreateSmartContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.CreateSmartContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                   java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.CreateSmartContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.CreateSmartContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.CreateSmartContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.CreateSmartContract.Builder mergeFrom(Contract.CreateSmartContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.CreateSmartContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.CreateSmartContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.CreateSmartContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.CreateSmartContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.CreateSmartContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.CreateSmartContract.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### hasNewContract

      ```
      public boolean hasNewContract()
      ```

      `.protocol.SmartContract new_contract = 2;`

      Specified by:
      :   `hasNewContract` in interface `Contract.CreateSmartContractOrBuilder`

      Returns:
      :   Whether the newContract field is set.
    - #### getNewContract

      ```
      public Common.SmartContract getNewContract()
      ```

      `.protocol.SmartContract new_contract = 2;`

      Specified by:
      :   `getNewContract` in interface `Contract.CreateSmartContractOrBuilder`

      Returns:
      :   The newContract.
    - #### setNewContract

      ```
      public Contract.CreateSmartContract.Builder setNewContract(Common.SmartContract value)
      ```

      `.protocol.SmartContract new_contract = 2;`
    - #### setNewContract

      ```
      public Contract.CreateSmartContract.Builder setNewContract(Common.SmartContract.Builder builderForValue)
      ```

      `.protocol.SmartContract new_contract = 2;`
    - #### mergeNewContract

      ```
      public Contract.CreateSmartContract.Builder mergeNewContract(Common.SmartContract value)
      ```

      `.protocol.SmartContract new_contract = 2;`
    - #### clearNewContract

      ```
      public Contract.CreateSmartContract.Builder clearNewContract()
      ```

      `.protocol.SmartContract new_contract = 2;`
    - #### getNewContractBuilder

      ```
      public Common.SmartContract.Builder getNewContractBuilder()
      ```

      `.protocol.SmartContract new_contract = 2;`
    - #### getNewContractOrBuilder

      ```
      public Common.SmartContractOrBuilder getNewContractOrBuilder()
      ```

      `.protocol.SmartContract new_contract = 2;`

      Specified by:
      :   `getNewContractOrBuilder` in interface `Contract.CreateSmartContractOrBuilder`
    - #### getCallTokenValue

      ```
      public long getCallTokenValue()
      ```

      `int64 call_token_value = 3;`

      Specified by:
      :   `getCallTokenValue` in interface `Contract.CreateSmartContractOrBuilder`

      Returns:
      :   The callTokenValue.
    - #### setCallTokenValue

      ```
      public Contract.CreateSmartContract.Builder setCallTokenValue(long value)
      ```

      `int64 call_token_value = 3;`

      Parameters:
      :   `value` - The callTokenValue to set.

      Returns:
      :   This builder for chaining.
    - #### clearCallTokenValue

      ```
      public Contract.CreateSmartContract.Builder clearCallTokenValue()
      ```

      `int64 call_token_value = 3;`

      Returns:
      :   This builder for chaining.
    - #### getTokenId

      ```
      public long getTokenId()
      ```

      `int64 token_id = 4;`

      Specified by:
      :   `getTokenId` in interface `Contract.CreateSmartContractOrBuilder`

      Returns:
      :   The tokenId.
    - #### setTokenId

      ```
      public Contract.CreateSmartContract.Builder setTokenId(long value)
      ```

      `int64 token_id = 4;`

      Parameters:
      :   `value` - The tokenId to set.

      Returns:
      :   This builder for chaining.
    - #### clearTokenId

      ```
      public Contract.CreateSmartContract.Builder clearTokenId()
      ```

      `int64 token_id = 4;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.CreateSmartContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.CreateSmartContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.CreateSmartContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.CreateSmartContract.Builder>`