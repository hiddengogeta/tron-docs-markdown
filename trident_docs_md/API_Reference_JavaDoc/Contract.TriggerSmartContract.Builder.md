

org.tron.trident.proto

## Class Contract.TriggerSmartContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.TriggerSmartContract.Builder](../../../../org/tron/trident/proto/Contract.TriggerSmartContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.TriggerSmartContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.TriggerSmartContractOrBuilder](../../../../org/tron/trident/proto/Contract.TriggerSmartContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.TriggerSmartContract](../../../../org/tron/trident/proto/Contract.TriggerSmartContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.TriggerSmartContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.TriggerSmartContract.Builder>
  implements Contract.TriggerSmartContractOrBuilder
  ```

  Protobuf type `protocol.TriggerSmartContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.TriggerSmartContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.TriggerSmartContract` | `build()` |
    | `Contract.TriggerSmartContract` | `buildPartial()` |
    | `Contract.TriggerSmartContract.Builder` | `clear()` |
    | `Contract.TriggerSmartContract.Builder` | `clearCallTokenValue()` `int64 call_token_value = 5;` |
    | `Contract.TriggerSmartContract.Builder` | `clearCallValue()` `int64 call_value = 3;` |
    | `Contract.TriggerSmartContract.Builder` | `clearContractAddress()` `bytes contract_address = 2;` |
    | `Contract.TriggerSmartContract.Builder` | `clearData()` `bytes data = 4;` |
    | `Contract.TriggerSmartContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.TriggerSmartContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.TriggerSmartContract.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `Contract.TriggerSmartContract.Builder` | `clearTokenId()` `int64 token_id = 6;` |
    | `Contract.TriggerSmartContract.Builder` | `clone()` |
    | `long` | `getCallTokenValue()` `int64 call_token_value = 5;` |
    | `long` | `getCallValue()` `int64 call_value = 3;` |
    | `com.google.protobuf.ByteString` | `getContractAddress()` `bytes contract_address = 2;` |
    | `com.google.protobuf.ByteString` | `getData()` `bytes data = 4;` |
    | `Contract.TriggerSmartContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `long` | `getTokenId()` `int64 token_id = 6;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.TriggerSmartContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.TriggerSmartContract.Builder` | `mergeFrom(Contract.TriggerSmartContract other)` |
    | `Contract.TriggerSmartContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.TriggerSmartContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.TriggerSmartContract.Builder` | `setCallTokenValue(long value)` `int64 call_token_value = 5;` |
    | `Contract.TriggerSmartContract.Builder` | `setCallValue(long value)` `int64 call_value = 3;` |
    | `Contract.TriggerSmartContract.Builder` | `setContractAddress(com.google.protobuf.ByteString value)` `bytes contract_address = 2;` |
    | `Contract.TriggerSmartContract.Builder` | `setData(com.google.protobuf.ByteString value)` `bytes data = 4;` |
    | `Contract.TriggerSmartContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.TriggerSmartContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `Contract.TriggerSmartContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.TriggerSmartContract.Builder` | `setTokenId(long value)` `int64 token_id = 6;` |
    | `Contract.TriggerSmartContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TriggerSmartContract.Builder>`
    - #### clear

      ```
      public Contract.TriggerSmartContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TriggerSmartContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TriggerSmartContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.TriggerSmartContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.TriggerSmartContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.TriggerSmartContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.TriggerSmartContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TriggerSmartContract.Builder>`
    - #### setField

      ```
      public Contract.TriggerSmartContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                            java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TriggerSmartContract.Builder>`
    - #### clearField

      ```
      public Contract.TriggerSmartContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TriggerSmartContract.Builder>`
    - #### clearOneof

      ```
      public Contract.TriggerSmartContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TriggerSmartContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.TriggerSmartContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                    int index,
                                                                    java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TriggerSmartContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.TriggerSmartContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                    java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TriggerSmartContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.TriggerSmartContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.TriggerSmartContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.TriggerSmartContract.Builder mergeFrom(Contract.TriggerSmartContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TriggerSmartContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.TriggerSmartContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                             com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                      throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.TriggerSmartContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.TriggerSmartContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.TriggerSmartContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.TriggerSmartContract.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getContractAddress

      ```
      public com.google.protobuf.ByteString getContractAddress()
      ```

      `bytes contract_address = 2;`

      Specified by:
      :   `getContractAddress` in interface `Contract.TriggerSmartContractOrBuilder`

      Returns:
      :   The contractAddress.
    - #### setContractAddress

      ```
      public Contract.TriggerSmartContract.Builder setContractAddress(com.google.protobuf.ByteString value)
      ```

      `bytes contract_address = 2;`

      Parameters:
      :   `value` - The contractAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearContractAddress

      ```
      public Contract.TriggerSmartContract.Builder clearContractAddress()
      ```

      `bytes contract_address = 2;`

      Returns:
      :   This builder for chaining.
    - #### getCallValue

      ```
      public long getCallValue()
      ```

      `int64 call_value = 3;`

      Specified by:
      :   `getCallValue` in interface `Contract.TriggerSmartContractOrBuilder`

      Returns:
      :   The callValue.
    - #### setCallValue

      ```
      public Contract.TriggerSmartContract.Builder setCallValue(long value)
      ```

      `int64 call_value = 3;`

      Parameters:
      :   `value` - The callValue to set.

      Returns:
      :   This builder for chaining.
    - #### clearCallValue

      ```
      public Contract.TriggerSmartContract.Builder clearCallValue()
      ```

      `int64 call_value = 3;`

      Returns:
      :   This builder for chaining.
    - #### getData

      ```
      public com.google.protobuf.ByteString getData()
      ```

      `bytes data = 4;`

      Specified by:
      :   `getData` in interface `Contract.TriggerSmartContractOrBuilder`

      Returns:
      :   The data.
    - #### setData

      ```
      public Contract.TriggerSmartContract.Builder setData(com.google.protobuf.ByteString value)
      ```

      `bytes data = 4;`

      Parameters:
      :   `value` - The data to set.

      Returns:
      :   This builder for chaining.
    - #### clearData

      ```
      public Contract.TriggerSmartContract.Builder clearData()
      ```

      `bytes data = 4;`

      Returns:
      :   This builder for chaining.
    - #### getCallTokenValue

      ```
      public long getCallTokenValue()
      ```

      `int64 call_token_value = 5;`

      Specified by:
      :   `getCallTokenValue` in interface `Contract.TriggerSmartContractOrBuilder`

      Returns:
      :   The callTokenValue.
    - #### setCallTokenValue

      ```
      public Contract.TriggerSmartContract.Builder setCallTokenValue(long value)
      ```

      `int64 call_token_value = 5;`

      Parameters:
      :   `value` - The callTokenValue to set.

      Returns:
      :   This builder for chaining.
    - #### clearCallTokenValue

      ```
      public Contract.TriggerSmartContract.Builder clearCallTokenValue()
      ```

      `int64 call_token_value = 5;`

      Returns:
      :   This builder for chaining.
    - #### getTokenId

      ```
      public long getTokenId()
      ```

      `int64 token_id = 6;`

      Specified by:
      :   `getTokenId` in interface `Contract.TriggerSmartContractOrBuilder`

      Returns:
      :   The tokenId.
    - #### setTokenId

      ```
      public Contract.TriggerSmartContract.Builder setTokenId(long value)
      ```

      `int64 token_id = 6;`

      Parameters:
      :   `value` - The tokenId to set.

      Returns:
      :   This builder for chaining.
    - #### clearTokenId

      ```
      public Contract.TriggerSmartContract.Builder clearTokenId()
      ```

      `int64 token_id = 6;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.TriggerSmartContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TriggerSmartContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.TriggerSmartContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.TriggerSmartContract.Builder>`