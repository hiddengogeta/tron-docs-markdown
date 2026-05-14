

org.tron.trident.proto

## Class Response.SmartContractDataWrapper.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.SmartContractDataWrapper.Builder](../../../../org/tron/trident/proto/Response.SmartContractDataWrapper.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.SmartContractDataWrapper.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.SmartContractDataWrapperOrBuilder](../../../../org/tron/trident/proto/Response.SmartContractDataWrapperOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.SmartContractDataWrapper](../../../../org/tron/trident/proto/Response.SmartContractDataWrapper.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.SmartContractDataWrapper.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.SmartContractDataWrapper.Builder>
  implements Response.SmartContractDataWrapperOrBuilder
  ```

  Protobuf type `protocol.SmartContractDataWrapper`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.SmartContractDataWrapper.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.SmartContractDataWrapper` | `build()` |
    | `Response.SmartContractDataWrapper` | `buildPartial()` |
    | `Response.SmartContractDataWrapper.Builder` | `clear()` |
    | `Response.SmartContractDataWrapper.Builder` | `clearContractState()` `.protocol.ContractState contract_state = 3;` |
    | `Response.SmartContractDataWrapper.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.SmartContractDataWrapper.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.SmartContractDataWrapper.Builder` | `clearRuntimeCode()` `bytes runtime_code = 2;` |
    | `Response.SmartContractDataWrapper.Builder` | `clearSmartContract()` `.protocol.SmartContract smart_contract = 1;` |
    | `Response.SmartContractDataWrapper.Builder` | `clone()` |
    | `Contract.ContractState` | `getContractState()` `.protocol.ContractState contract_state = 3;` |
    | `Contract.ContractState.Builder` | `getContractStateBuilder()` `.protocol.ContractState contract_state = 3;` |
    | `Contract.ContractStateOrBuilder` | `getContractStateOrBuilder()` `.protocol.ContractState contract_state = 3;` |
    | `Response.SmartContractDataWrapper` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getRuntimeCode()` `bytes runtime_code = 2;` |
    | `Common.SmartContract` | `getSmartContract()` `.protocol.SmartContract smart_contract = 1;` |
    | `Common.SmartContract.Builder` | `getSmartContractBuilder()` `.protocol.SmartContract smart_contract = 1;` |
    | `Common.SmartContractOrBuilder` | `getSmartContractOrBuilder()` `.protocol.SmartContract smart_contract = 1;` |
    | `boolean` | `hasContractState()` `.protocol.ContractState contract_state = 3;` |
    | `boolean` | `hasSmartContract()` `.protocol.SmartContract smart_contract = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.SmartContractDataWrapper.Builder` | `mergeContractState(Contract.ContractState value)` `.protocol.ContractState contract_state = 3;` |
    | `Response.SmartContractDataWrapper.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.SmartContractDataWrapper.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.SmartContractDataWrapper.Builder` | `mergeFrom(Response.SmartContractDataWrapper other)` |
    | `Response.SmartContractDataWrapper.Builder` | `mergeSmartContract(Common.SmartContract value)` `.protocol.SmartContract smart_contract = 1;` |
    | `Response.SmartContractDataWrapper.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.SmartContractDataWrapper.Builder` | `setContractState(Contract.ContractState.Builder builderForValue)` `.protocol.ContractState contract_state = 3;` |
    | `Response.SmartContractDataWrapper.Builder` | `setContractState(Contract.ContractState value)` `.protocol.ContractState contract_state = 3;` |
    | `Response.SmartContractDataWrapper.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.SmartContractDataWrapper.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.SmartContractDataWrapper.Builder` | `setRuntimeCode(com.google.protobuf.ByteString value)` `bytes runtime_code = 2;` |
    | `Response.SmartContractDataWrapper.Builder` | `setSmartContract(Common.SmartContract.Builder builderForValue)` `.protocol.SmartContract smart_contract = 1;` |
    | `Response.SmartContractDataWrapper.Builder` | `setSmartContract(Common.SmartContract value)` `.protocol.SmartContract smart_contract = 1;` |
    | `Response.SmartContractDataWrapper.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.SmartContractDataWrapper.Builder>`
    - #### clear

      ```
      public Response.SmartContractDataWrapper.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.SmartContractDataWrapper.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.SmartContractDataWrapper.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.SmartContractDataWrapper getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.SmartContractDataWrapper build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.SmartContractDataWrapper buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.SmartContractDataWrapper.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.SmartContractDataWrapper.Builder>`
    - #### setField

      ```
      public Response.SmartContractDataWrapper.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.SmartContractDataWrapper.Builder>`
    - #### clearField

      ```
      public Response.SmartContractDataWrapper.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.SmartContractDataWrapper.Builder>`
    - #### clearOneof

      ```
      public Response.SmartContractDataWrapper.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.SmartContractDataWrapper.Builder>`
    - #### setRepeatedField

      ```
      public Response.SmartContractDataWrapper.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                        int index,
                                                                        java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.SmartContractDataWrapper.Builder>`
    - #### addRepeatedField

      ```
      public Response.SmartContractDataWrapper.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                        java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.SmartContractDataWrapper.Builder>`
    - #### mergeFrom

      ```
      public Response.SmartContractDataWrapper.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.SmartContractDataWrapper.Builder>`
    - #### mergeFrom

      ```
      public Response.SmartContractDataWrapper.Builder mergeFrom(Response.SmartContractDataWrapper other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.SmartContractDataWrapper.Builder>`
    - #### mergeFrom

      ```
      public Response.SmartContractDataWrapper.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                 com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                          throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.SmartContractDataWrapper.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### hasSmartContract

      ```
      public boolean hasSmartContract()
      ```

      `.protocol.SmartContract smart_contract = 1;`

      Specified by:
      :   `hasSmartContract` in interface `Response.SmartContractDataWrapperOrBuilder`

      Returns:
      :   Whether the smartContract field is set.
    - #### getSmartContract

      ```
      public Common.SmartContract getSmartContract()
      ```

      `.protocol.SmartContract smart_contract = 1;`

      Specified by:
      :   `getSmartContract` in interface `Response.SmartContractDataWrapperOrBuilder`

      Returns:
      :   The smartContract.
    - #### setSmartContract

      ```
      public Response.SmartContractDataWrapper.Builder setSmartContract(Common.SmartContract value)
      ```

      `.protocol.SmartContract smart_contract = 1;`
    - #### setSmartContract

      ```
      public Response.SmartContractDataWrapper.Builder setSmartContract(Common.SmartContract.Builder builderForValue)
      ```

      `.protocol.SmartContract smart_contract = 1;`
    - #### mergeSmartContract

      ```
      public Response.SmartContractDataWrapper.Builder mergeSmartContract(Common.SmartContract value)
      ```

      `.protocol.SmartContract smart_contract = 1;`
    - #### clearSmartContract

      ```
      public Response.SmartContractDataWrapper.Builder clearSmartContract()
      ```

      `.protocol.SmartContract smart_contract = 1;`
    - #### getSmartContractBuilder

      ```
      public Common.SmartContract.Builder getSmartContractBuilder()
      ```

      `.protocol.SmartContract smart_contract = 1;`
    - #### getSmartContractOrBuilder

      ```
      public Common.SmartContractOrBuilder getSmartContractOrBuilder()
      ```

      `.protocol.SmartContract smart_contract = 1;`

      Specified by:
      :   `getSmartContractOrBuilder` in interface `Response.SmartContractDataWrapperOrBuilder`
    - #### getRuntimeCode

      ```
      public com.google.protobuf.ByteString getRuntimeCode()
      ```

      `bytes runtime_code = 2;`

      Specified by:
      :   `getRuntimeCode` in interface `Response.SmartContractDataWrapperOrBuilder`

      Returns:
      :   The runtimeCode.
    - #### setRuntimeCode

      ```
      public Response.SmartContractDataWrapper.Builder setRuntimeCode(com.google.protobuf.ByteString value)
      ```

      `bytes runtime_code = 2;`

      Parameters:
      :   `value` - The runtimeCode to set.

      Returns:
      :   This builder for chaining.
    - #### clearRuntimeCode

      ```
      public Response.SmartContractDataWrapper.Builder clearRuntimeCode()
      ```

      `bytes runtime_code = 2;`

      Returns:
      :   This builder for chaining.
    - #### hasContractState

      ```
      public boolean hasContractState()
      ```

      `.protocol.ContractState contract_state = 3;`

      Specified by:
      :   `hasContractState` in interface `Response.SmartContractDataWrapperOrBuilder`

      Returns:
      :   Whether the contractState field is set.
    - #### getContractState

      ```
      public Contract.ContractState getContractState()
      ```

      `.protocol.ContractState contract_state = 3;`

      Specified by:
      :   `getContractState` in interface `Response.SmartContractDataWrapperOrBuilder`

      Returns:
      :   The contractState.
    - #### setContractState

      ```
      public Response.SmartContractDataWrapper.Builder setContractState(Contract.ContractState value)
      ```

      `.protocol.ContractState contract_state = 3;`
    - #### setContractState

      ```
      public Response.SmartContractDataWrapper.Builder setContractState(Contract.ContractState.Builder builderForValue)
      ```

      `.protocol.ContractState contract_state = 3;`
    - #### mergeContractState

      ```
      public Response.SmartContractDataWrapper.Builder mergeContractState(Contract.ContractState value)
      ```

      `.protocol.ContractState contract_state = 3;`
    - #### clearContractState

      ```
      public Response.SmartContractDataWrapper.Builder clearContractState()
      ```

      `.protocol.ContractState contract_state = 3;`
    - #### getContractStateBuilder

      ```
      public Contract.ContractState.Builder getContractStateBuilder()
      ```

      `.protocol.ContractState contract_state = 3;`
    - #### getContractStateOrBuilder

      ```
      public Contract.ContractStateOrBuilder getContractStateOrBuilder()
      ```

      `.protocol.ContractState contract_state = 3;`

      Specified by:
      :   `getContractStateOrBuilder` in interface `Response.SmartContractDataWrapperOrBuilder`
    - #### setUnknownFields

      ```
      public final Response.SmartContractDataWrapper.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.SmartContractDataWrapper.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.SmartContractDataWrapper.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.SmartContractDataWrapper.Builder>`