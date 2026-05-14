

org.tron.trident.proto

## Class Contract.ExchangeCreateContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.ExchangeCreateContract.Builder](../../../../org/tron/trident/proto/Contract.ExchangeCreateContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.ExchangeCreateContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.ExchangeCreateContractOrBuilder](../../../../org/tron/trident/proto/Contract.ExchangeCreateContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.ExchangeCreateContract](../../../../org/tron/trident/proto/Contract.ExchangeCreateContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.ExchangeCreateContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeCreateContract.Builder>
  implements Contract.ExchangeCreateContractOrBuilder
  ```

  Protobuf type `protocol.ExchangeCreateContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.ExchangeCreateContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.ExchangeCreateContract` | `build()` |
    | `Contract.ExchangeCreateContract` | `buildPartial()` |
    | `Contract.ExchangeCreateContract.Builder` | `clear()` |
    | `Contract.ExchangeCreateContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.ExchangeCreateContract.Builder` | `clearFirstTokenBalance()` `int64 first_token_balance = 3;` |
    | `Contract.ExchangeCreateContract.Builder` | `clearFirstTokenId()` `bytes first_token_id = 2;` |
    | `Contract.ExchangeCreateContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.ExchangeCreateContract.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `Contract.ExchangeCreateContract.Builder` | `clearSecondTokenBalance()` `int64 second_token_balance = 5;` |
    | `Contract.ExchangeCreateContract.Builder` | `clearSecondTokenId()` `bytes second_token_id = 4;` |
    | `Contract.ExchangeCreateContract.Builder` | `clone()` |
    | `Contract.ExchangeCreateContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getFirstTokenBalance()` `int64 first_token_balance = 3;` |
    | `com.google.protobuf.ByteString` | `getFirstTokenId()` `bytes first_token_id = 2;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `long` | `getSecondTokenBalance()` `int64 second_token_balance = 5;` |
    | `com.google.protobuf.ByteString` | `getSecondTokenId()` `bytes second_token_id = 4;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.ExchangeCreateContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.ExchangeCreateContract.Builder` | `mergeFrom(Contract.ExchangeCreateContract other)` |
    | `Contract.ExchangeCreateContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.ExchangeCreateContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.ExchangeCreateContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.ExchangeCreateContract.Builder` | `setFirstTokenBalance(long value)` `int64 first_token_balance = 3;` |
    | `Contract.ExchangeCreateContract.Builder` | `setFirstTokenId(com.google.protobuf.ByteString value)` `bytes first_token_id = 2;` |
    | `Contract.ExchangeCreateContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `Contract.ExchangeCreateContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.ExchangeCreateContract.Builder` | `setSecondTokenBalance(long value)` `int64 second_token_balance = 5;` |
    | `Contract.ExchangeCreateContract.Builder` | `setSecondTokenId(com.google.protobuf.ByteString value)` `bytes second_token_id = 4;` |
    | `Contract.ExchangeCreateContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeCreateContract.Builder>`
    - #### clear

      ```
      public Contract.ExchangeCreateContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeCreateContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeCreateContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.ExchangeCreateContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.ExchangeCreateContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.ExchangeCreateContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.ExchangeCreateContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeCreateContract.Builder>`
    - #### setField

      ```
      public Contract.ExchangeCreateContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                              java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeCreateContract.Builder>`
    - #### clearField

      ```
      public Contract.ExchangeCreateContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeCreateContract.Builder>`
    - #### clearOneof

      ```
      public Contract.ExchangeCreateContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeCreateContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.ExchangeCreateContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                      int index,
                                                                      java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeCreateContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.ExchangeCreateContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                      java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeCreateContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.ExchangeCreateContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.ExchangeCreateContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.ExchangeCreateContract.Builder mergeFrom(Contract.ExchangeCreateContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeCreateContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.ExchangeCreateContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.ExchangeCreateContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.ExchangeCreateContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.ExchangeCreateContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.ExchangeCreateContract.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getFirstTokenId

      ```
      public com.google.protobuf.ByteString getFirstTokenId()
      ```

      `bytes first_token_id = 2;`

      Specified by:
      :   `getFirstTokenId` in interface `Contract.ExchangeCreateContractOrBuilder`

      Returns:
      :   The firstTokenId.
    - #### setFirstTokenId

      ```
      public Contract.ExchangeCreateContract.Builder setFirstTokenId(com.google.protobuf.ByteString value)
      ```

      `bytes first_token_id = 2;`

      Parameters:
      :   `value` - The firstTokenId to set.

      Returns:
      :   This builder for chaining.
    - #### clearFirstTokenId

      ```
      public Contract.ExchangeCreateContract.Builder clearFirstTokenId()
      ```

      `bytes first_token_id = 2;`

      Returns:
      :   This builder for chaining.
    - #### getFirstTokenBalance

      ```
      public long getFirstTokenBalance()
      ```

      `int64 first_token_balance = 3;`

      Specified by:
      :   `getFirstTokenBalance` in interface `Contract.ExchangeCreateContractOrBuilder`

      Returns:
      :   The firstTokenBalance.
    - #### setFirstTokenBalance

      ```
      public Contract.ExchangeCreateContract.Builder setFirstTokenBalance(long value)
      ```

      `int64 first_token_balance = 3;`

      Parameters:
      :   `value` - The firstTokenBalance to set.

      Returns:
      :   This builder for chaining.
    - #### clearFirstTokenBalance

      ```
      public Contract.ExchangeCreateContract.Builder clearFirstTokenBalance()
      ```

      `int64 first_token_balance = 3;`

      Returns:
      :   This builder for chaining.
    - #### getSecondTokenId

      ```
      public com.google.protobuf.ByteString getSecondTokenId()
      ```

      `bytes second_token_id = 4;`

      Specified by:
      :   `getSecondTokenId` in interface `Contract.ExchangeCreateContractOrBuilder`

      Returns:
      :   The secondTokenId.
    - #### setSecondTokenId

      ```
      public Contract.ExchangeCreateContract.Builder setSecondTokenId(com.google.protobuf.ByteString value)
      ```

      `bytes second_token_id = 4;`

      Parameters:
      :   `value` - The secondTokenId to set.

      Returns:
      :   This builder for chaining.
    - #### clearSecondTokenId

      ```
      public Contract.ExchangeCreateContract.Builder clearSecondTokenId()
      ```

      `bytes second_token_id = 4;`

      Returns:
      :   This builder for chaining.
    - #### getSecondTokenBalance

      ```
      public long getSecondTokenBalance()
      ```

      `int64 second_token_balance = 5;`

      Specified by:
      :   `getSecondTokenBalance` in interface `Contract.ExchangeCreateContractOrBuilder`

      Returns:
      :   The secondTokenBalance.
    - #### setSecondTokenBalance

      ```
      public Contract.ExchangeCreateContract.Builder setSecondTokenBalance(long value)
      ```

      `int64 second_token_balance = 5;`

      Parameters:
      :   `value` - The secondTokenBalance to set.

      Returns:
      :   This builder for chaining.
    - #### clearSecondTokenBalance

      ```
      public Contract.ExchangeCreateContract.Builder clearSecondTokenBalance()
      ```

      `int64 second_token_balance = 5;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.ExchangeCreateContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeCreateContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.ExchangeCreateContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ExchangeCreateContract.Builder>`