

org.tron.trident.proto

## Class Contract.ExchangeInjectContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.ExchangeInjectContract.Builder](../../../../org/tron/trident/proto/Contract.ExchangeInjectContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.ExchangeInjectContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.ExchangeInjectContractOrBuilder](../../../../org/tron/trident/proto/Contract.ExchangeInjectContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.ExchangeInjectContract](../../../../org/tron/trident/proto/Contract.ExchangeInjectContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.ExchangeInjectContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeInjectContract.Builder>
  implements Contract.ExchangeInjectContractOrBuilder
  ```

  Protobuf type `protocol.ExchangeInjectContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.ExchangeInjectContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.ExchangeInjectContract` | `build()` |
    | `Contract.ExchangeInjectContract` | `buildPartial()` |
    | `Contract.ExchangeInjectContract.Builder` | `clear()` |
    | `Contract.ExchangeInjectContract.Builder` | `clearExchangeId()` `int64 exchange_id = 2;` |
    | `Contract.ExchangeInjectContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.ExchangeInjectContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.ExchangeInjectContract.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `Contract.ExchangeInjectContract.Builder` | `clearQuant()` `int64 quant = 4;` |
    | `Contract.ExchangeInjectContract.Builder` | `clearTokenId()` `bytes token_id = 3;` |
    | `Contract.ExchangeInjectContract.Builder` | `clone()` |
    | `Contract.ExchangeInjectContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getExchangeId()` `int64 exchange_id = 2;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `long` | `getQuant()` `int64 quant = 4;` |
    | `com.google.protobuf.ByteString` | `getTokenId()` `bytes token_id = 3;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.ExchangeInjectContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.ExchangeInjectContract.Builder` | `mergeFrom(Contract.ExchangeInjectContract other)` |
    | `Contract.ExchangeInjectContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.ExchangeInjectContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.ExchangeInjectContract.Builder` | `setExchangeId(long value)` `int64 exchange_id = 2;` |
    | `Contract.ExchangeInjectContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.ExchangeInjectContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `Contract.ExchangeInjectContract.Builder` | `setQuant(long value)` `int64 quant = 4;` |
    | `Contract.ExchangeInjectContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.ExchangeInjectContract.Builder` | `setTokenId(com.google.protobuf.ByteString value)` `bytes token_id = 3;` |
    | `Contract.ExchangeInjectContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeInjectContract.Builder>`
    - #### clear

      ```
      public Contract.ExchangeInjectContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeInjectContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeInjectContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.ExchangeInjectContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.ExchangeInjectContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.ExchangeInjectContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.ExchangeInjectContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeInjectContract.Builder>`
    - #### setField

      ```
      public Contract.ExchangeInjectContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                              java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeInjectContract.Builder>`
    - #### clearField

      ```
      public Contract.ExchangeInjectContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeInjectContract.Builder>`
    - #### clearOneof

      ```
      public Contract.ExchangeInjectContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeInjectContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.ExchangeInjectContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                      int index,
                                                                      java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeInjectContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.ExchangeInjectContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                      java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeInjectContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.ExchangeInjectContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.ExchangeInjectContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.ExchangeInjectContract.Builder mergeFrom(Contract.ExchangeInjectContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeInjectContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.ExchangeInjectContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.ExchangeInjectContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.ExchangeInjectContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.ExchangeInjectContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.ExchangeInjectContract.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getExchangeId

      ```
      public long getExchangeId()
      ```

      `int64 exchange_id = 2;`

      Specified by:
      :   `getExchangeId` in interface `Contract.ExchangeInjectContractOrBuilder`

      Returns:
      :   The exchangeId.
    - #### setExchangeId

      ```
      public Contract.ExchangeInjectContract.Builder setExchangeId(long value)
      ```

      `int64 exchange_id = 2;`

      Parameters:
      :   `value` - The exchangeId to set.

      Returns:
      :   This builder for chaining.
    - #### clearExchangeId

      ```
      public Contract.ExchangeInjectContract.Builder clearExchangeId()
      ```

      `int64 exchange_id = 2;`

      Returns:
      :   This builder for chaining.
    - #### getTokenId

      ```
      public com.google.protobuf.ByteString getTokenId()
      ```

      `bytes token_id = 3;`

      Specified by:
      :   `getTokenId` in interface `Contract.ExchangeInjectContractOrBuilder`

      Returns:
      :   The tokenId.
    - #### setTokenId

      ```
      public Contract.ExchangeInjectContract.Builder setTokenId(com.google.protobuf.ByteString value)
      ```

      `bytes token_id = 3;`

      Parameters:
      :   `value` - The tokenId to set.

      Returns:
      :   This builder for chaining.
    - #### clearTokenId

      ```
      public Contract.ExchangeInjectContract.Builder clearTokenId()
      ```

      `bytes token_id = 3;`

      Returns:
      :   This builder for chaining.
    - #### getQuant

      ```
      public long getQuant()
      ```

      `int64 quant = 4;`

      Specified by:
      :   `getQuant` in interface `Contract.ExchangeInjectContractOrBuilder`

      Returns:
      :   The quant.
    - #### setQuant

      ```
      public Contract.ExchangeInjectContract.Builder setQuant(long value)
      ```

      `int64 quant = 4;`

      Parameters:
      :   `value` - The quant to set.

      Returns:
      :   This builder for chaining.
    - #### clearQuant

      ```
      public Contract.ExchangeInjectContract.Builder clearQuant()
      ```

      `int64 quant = 4;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.ExchangeInjectContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeInjectContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.ExchangeInjectContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeInjectContract.Builder>`