

org.tron.trident.proto

## Class Common.SmartContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Common.SmartContract.Builder](../../../../org/tron/trident/proto/Common.SmartContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Common.SmartContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Common.SmartContractOrBuilder](../../../../org/tron/trident/proto/Common.SmartContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Common.SmartContract](../../../../org/tron/trident/proto/Common.SmartContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Common.SmartContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.Builder>
  implements Common.SmartContractOrBuilder
  ```

  Protobuf type `protocol.SmartContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Common.SmartContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Common.SmartContract` | `build()` |
    | `Common.SmartContract` | `buildPartial()` |
    | `Common.SmartContract.Builder` | `clear()` |
    | `Common.SmartContract.Builder` | `clearAbi()` `.protocol.SmartContract.ABI abi = 3;` |
    | `Common.SmartContract.Builder` | `clearBytecode()` `bytes bytecode = 4;` |
    | `Common.SmartContract.Builder` | `clearCallValue()` `int64 call_value = 5;` |
    | `Common.SmartContract.Builder` | `clearCodeHash()` `bytes code_hash = 9;` |
    | `Common.SmartContract.Builder` | `clearConsumeUserResourcePercent()` `int64 consume_user_resource_percent = 6;` |
    | `Common.SmartContract.Builder` | `clearContractAddress()` `bytes contract_address = 2;` |
    | `Common.SmartContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Common.SmartContract.Builder` | `clearName()` `string name = 7;` |
    | `Common.SmartContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Common.SmartContract.Builder` | `clearOriginAddress()` `bytes origin_address = 1;` |
    | `Common.SmartContract.Builder` | `clearOriginEnergyLimit()` `int64 origin_energy_limit = 8;` |
    | `Common.SmartContract.Builder` | `clearTrxHash()` `bytes trx_hash = 10;` |
    | `Common.SmartContract.Builder` | `clearVersion()` `int32 version = 11;` |
    | `Common.SmartContract.Builder` | `clone()` |
    | `Common.SmartContract.ABI` | `getAbi()` `.protocol.SmartContract.ABI abi = 3;` |
    | `Common.SmartContract.ABI.Builder` | `getAbiBuilder()` `.protocol.SmartContract.ABI abi = 3;` |
    | `Common.SmartContract.ABIOrBuilder` | `getAbiOrBuilder()` `.protocol.SmartContract.ABI abi = 3;` |
    | `com.google.protobuf.ByteString` | `getBytecode()` `bytes bytecode = 4;` |
    | `long` | `getCallValue()` `int64 call_value = 5;` |
    | `com.google.protobuf.ByteString` | `getCodeHash()` `bytes code_hash = 9;` |
    | `long` | `getConsumeUserResourcePercent()` `int64 consume_user_resource_percent = 6;` |
    | `com.google.protobuf.ByteString` | `getContractAddress()` `bytes contract_address = 2;` |
    | `Common.SmartContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `java.lang.String` | `getName()` `string name = 7;` |
    | `com.google.protobuf.ByteString` | `getNameBytes()` `string name = 7;` |
    | `com.google.protobuf.ByteString` | `getOriginAddress()` `bytes origin_address = 1;` |
    | `long` | `getOriginEnergyLimit()` `int64 origin_energy_limit = 8;` |
    | `com.google.protobuf.ByteString` | `getTrxHash()` `bytes trx_hash = 10;` |
    | `int` | `getVersion()` `int32 version = 11;` |
    | `boolean` | `hasAbi()` `.protocol.SmartContract.ABI abi = 3;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Common.SmartContract.Builder` | `mergeAbi(Common.SmartContract.ABI value)` `.protocol.SmartContract.ABI abi = 3;` |
    | `Common.SmartContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Common.SmartContract.Builder` | `mergeFrom(Common.SmartContract other)` |
    | `Common.SmartContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Common.SmartContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Common.SmartContract.Builder` | `setAbi(Common.SmartContract.ABI.Builder builderForValue)` `.protocol.SmartContract.ABI abi = 3;` |
    | `Common.SmartContract.Builder` | `setAbi(Common.SmartContract.ABI value)` `.protocol.SmartContract.ABI abi = 3;` |
    | `Common.SmartContract.Builder` | `setBytecode(com.google.protobuf.ByteString value)` `bytes bytecode = 4;` |
    | `Common.SmartContract.Builder` | `setCallValue(long value)` `int64 call_value = 5;` |
    | `Common.SmartContract.Builder` | `setCodeHash(com.google.protobuf.ByteString value)` `bytes code_hash = 9;` |
    | `Common.SmartContract.Builder` | `setConsumeUserResourcePercent(long value)` `int64 consume_user_resource_percent = 6;` |
    | `Common.SmartContract.Builder` | `setContractAddress(com.google.protobuf.ByteString value)` `bytes contract_address = 2;` |
    | `Common.SmartContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Common.SmartContract.Builder` | `setName(java.lang.String value)` `string name = 7;` |
    | `Common.SmartContract.Builder` | `setNameBytes(com.google.protobuf.ByteString value)` `string name = 7;` |
    | `Common.SmartContract.Builder` | `setOriginAddress(com.google.protobuf.ByteString value)` `bytes origin_address = 1;` |
    | `Common.SmartContract.Builder` | `setOriginEnergyLimit(long value)` `int64 origin_energy_limit = 8;` |
    | `Common.SmartContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Common.SmartContract.Builder` | `setTrxHash(com.google.protobuf.ByteString value)` `bytes trx_hash = 10;` |
    | `Common.SmartContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Common.SmartContract.Builder` | `setVersion(int value)` `int32 version = 11;` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.Builder>`
    - #### clear

      ```
      public Common.SmartContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Common.SmartContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Common.SmartContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Common.SmartContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Common.SmartContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.Builder>`
    - #### setField

      ```
      public Common.SmartContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                   java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.Builder>`
    - #### clearField

      ```
      public Common.SmartContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.Builder>`
    - #### clearOneof

      ```
      public Common.SmartContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.Builder>`
    - #### setRepeatedField

      ```
      public Common.SmartContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                           int index,
                                                           java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.Builder>`
    - #### addRepeatedField

      ```
      public Common.SmartContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                           java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.Builder>`
    - #### mergeFrom

      ```
      public Common.SmartContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Common.SmartContract.Builder>`
    - #### mergeFrom

      ```
      public Common.SmartContract.Builder mergeFrom(Common.SmartContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.Builder>`
    - #### mergeFrom

      ```
      public Common.SmartContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                    com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                             throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Common.SmartContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOriginAddress

      ```
      public com.google.protobuf.ByteString getOriginAddress()
      ```

      `bytes origin_address = 1;`

      Specified by:
      :   `getOriginAddress` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The originAddress.
    - #### setOriginAddress

      ```
      public Common.SmartContract.Builder setOriginAddress(com.google.protobuf.ByteString value)
      ```

      `bytes origin_address = 1;`

      Parameters:
      :   `value` - The originAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOriginAddress

      ```
      public Common.SmartContract.Builder clearOriginAddress()
      ```

      `bytes origin_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getContractAddress

      ```
      public com.google.protobuf.ByteString getContractAddress()
      ```

      `bytes contract_address = 2;`

      Specified by:
      :   `getContractAddress` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The contractAddress.
    - #### setContractAddress

      ```
      public Common.SmartContract.Builder setContractAddress(com.google.protobuf.ByteString value)
      ```

      `bytes contract_address = 2;`

      Parameters:
      :   `value` - The contractAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearContractAddress

      ```
      public Common.SmartContract.Builder clearContractAddress()
      ```

      `bytes contract_address = 2;`

      Returns:
      :   This builder for chaining.
    - #### hasAbi

      ```
      public boolean hasAbi()
      ```

      `.protocol.SmartContract.ABI abi = 3;`

      Specified by:
      :   `hasAbi` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   Whether the abi field is set.
    - #### getAbi

      ```
      public Common.SmartContract.ABI getAbi()
      ```

      `.protocol.SmartContract.ABI abi = 3;`

      Specified by:
      :   `getAbi` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The abi.
    - #### setAbi

      ```
      public Common.SmartContract.Builder setAbi(Common.SmartContract.ABI value)
      ```

      `.protocol.SmartContract.ABI abi = 3;`
    - #### setAbi

      ```
      public Common.SmartContract.Builder setAbi(Common.SmartContract.ABI.Builder builderForValue)
      ```

      `.protocol.SmartContract.ABI abi = 3;`
    - #### mergeAbi

      ```
      public Common.SmartContract.Builder mergeAbi(Common.SmartContract.ABI value)
      ```

      `.protocol.SmartContract.ABI abi = 3;`
    - #### clearAbi

      ```
      public Common.SmartContract.Builder clearAbi()
      ```

      `.protocol.SmartContract.ABI abi = 3;`
    - #### getAbiBuilder

      ```
      public Common.SmartContract.ABI.Builder getAbiBuilder()
      ```

      `.protocol.SmartContract.ABI abi = 3;`
    - #### getAbiOrBuilder

      ```
      public Common.SmartContract.ABIOrBuilder getAbiOrBuilder()
      ```

      `.protocol.SmartContract.ABI abi = 3;`

      Specified by:
      :   `getAbiOrBuilder` in interface `Common.SmartContractOrBuilder`
    - #### getBytecode

      ```
      public com.google.protobuf.ByteString getBytecode()
      ```

      `bytes bytecode = 4;`

      Specified by:
      :   `getBytecode` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The bytecode.
    - #### setBytecode

      ```
      public Common.SmartContract.Builder setBytecode(com.google.protobuf.ByteString value)
      ```

      `bytes bytecode = 4;`

      Parameters:
      :   `value` - The bytecode to set.

      Returns:
      :   This builder for chaining.
    - #### clearBytecode

      ```
      public Common.SmartContract.Builder clearBytecode()
      ```

      `bytes bytecode = 4;`

      Returns:
      :   This builder for chaining.
    - #### getCallValue

      ```
      public long getCallValue()
      ```

      `int64 call_value = 5;`

      Specified by:
      :   `getCallValue` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The callValue.
    - #### setCallValue

      ```
      public Common.SmartContract.Builder setCallValue(long value)
      ```

      `int64 call_value = 5;`

      Parameters:
      :   `value` - The callValue to set.

      Returns:
      :   This builder for chaining.
    - #### clearCallValue

      ```
      public Common.SmartContract.Builder clearCallValue()
      ```

      `int64 call_value = 5;`

      Returns:
      :   This builder for chaining.
    - #### getConsumeUserResourcePercent

      ```
      public long getConsumeUserResourcePercent()
      ```

      `int64 consume_user_resource_percent = 6;`

      Specified by:
      :   `getConsumeUserResourcePercent` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The consumeUserResourcePercent.
    - #### setConsumeUserResourcePercent

      ```
      public Common.SmartContract.Builder setConsumeUserResourcePercent(long value)
      ```

      `int64 consume_user_resource_percent = 6;`

      Parameters:
      :   `value` - The consumeUserResourcePercent to set.

      Returns:
      :   This builder for chaining.
    - #### clearConsumeUserResourcePercent

      ```
      public Common.SmartContract.Builder clearConsumeUserResourcePercent()
      ```

      `int64 consume_user_resource_percent = 6;`

      Returns:
      :   This builder for chaining.
    - #### getName

      ```
      public java.lang.String getName()
      ```

      `string name = 7;`

      Specified by:
      :   `getName` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The name.
    - #### getNameBytes

      ```
      public com.google.protobuf.ByteString getNameBytes()
      ```

      `string name = 7;`

      Specified by:
      :   `getNameBytes` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The bytes for name.
    - #### setName

      ```
      public Common.SmartContract.Builder setName(java.lang.String value)
      ```

      `string name = 7;`

      Parameters:
      :   `value` - The name to set.

      Returns:
      :   This builder for chaining.
    - #### clearName

      ```
      public Common.SmartContract.Builder clearName()
      ```

      `string name = 7;`

      Returns:
      :   This builder for chaining.
    - #### setNameBytes

      ```
      public Common.SmartContract.Builder setNameBytes(com.google.protobuf.ByteString value)
      ```

      `string name = 7;`

      Parameters:
      :   `value` - The bytes for name to set.

      Returns:
      :   This builder for chaining.
    - #### getOriginEnergyLimit

      ```
      public long getOriginEnergyLimit()
      ```

      `int64 origin_energy_limit = 8;`

      Specified by:
      :   `getOriginEnergyLimit` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The originEnergyLimit.
    - #### setOriginEnergyLimit

      ```
      public Common.SmartContract.Builder setOriginEnergyLimit(long value)
      ```

      `int64 origin_energy_limit = 8;`

      Parameters:
      :   `value` - The originEnergyLimit to set.

      Returns:
      :   This builder for chaining.
    - #### clearOriginEnergyLimit

      ```
      public Common.SmartContract.Builder clearOriginEnergyLimit()
      ```

      `int64 origin_energy_limit = 8;`

      Returns:
      :   This builder for chaining.
    - #### getCodeHash

      ```
      public com.google.protobuf.ByteString getCodeHash()
      ```

      `bytes code_hash = 9;`

      Specified by:
      :   `getCodeHash` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The codeHash.
    - #### setCodeHash

      ```
      public Common.SmartContract.Builder setCodeHash(com.google.protobuf.ByteString value)
      ```

      `bytes code_hash = 9;`

      Parameters:
      :   `value` - The codeHash to set.

      Returns:
      :   This builder for chaining.
    - #### clearCodeHash

      ```
      public Common.SmartContract.Builder clearCodeHash()
      ```

      `bytes code_hash = 9;`

      Returns:
      :   This builder for chaining.
    - #### getTrxHash

      ```
      public com.google.protobuf.ByteString getTrxHash()
      ```

      `bytes trx_hash = 10;`

      Specified by:
      :   `getTrxHash` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The trxHash.
    - #### setTrxHash

      ```
      public Common.SmartContract.Builder setTrxHash(com.google.protobuf.ByteString value)
      ```

      `bytes trx_hash = 10;`

      Parameters:
      :   `value` - The trxHash to set.

      Returns:
      :   This builder for chaining.
    - #### clearTrxHash

      ```
      public Common.SmartContract.Builder clearTrxHash()
      ```

      `bytes trx_hash = 10;`

      Returns:
      :   This builder for chaining.
    - #### getVersion

      ```
      public int getVersion()
      ```

      `int32 version = 11;`

      Specified by:
      :   `getVersion` in interface `Common.SmartContractOrBuilder`

      Returns:
      :   The version.
    - #### setVersion

      ```
      public Common.SmartContract.Builder setVersion(int value)
      ```

      `int32 version = 11;`

      Parameters:
      :   `value` - The version to set.

      Returns:
      :   This builder for chaining.
    - #### clearVersion

      ```
      public Common.SmartContract.Builder clearVersion()
      ```

      `int32 version = 11;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Common.SmartContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Common.SmartContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.Builder>`