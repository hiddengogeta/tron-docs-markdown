

org.tron.trident.proto

## Class Contract.MarketSellAssetContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.MarketSellAssetContract.Builder](../../../../org/tron/trident/proto/Contract.MarketSellAssetContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.MarketSellAssetContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.MarketSellAssetContractOrBuilder](../../../../org/tron/trident/proto/Contract.MarketSellAssetContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.MarketSellAssetContract](../../../../org/tron/trident/proto/Contract.MarketSellAssetContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.MarketSellAssetContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketSellAssetContract.Builder>
  implements Contract.MarketSellAssetContractOrBuilder
  ```

  Protobuf type `protocol.MarketSellAssetContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.MarketSellAssetContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.MarketSellAssetContract` | `build()` |
    | `Contract.MarketSellAssetContract` | `buildPartial()` |
    | `Contract.MarketSellAssetContract.Builder` | `clear()` |
    | `Contract.MarketSellAssetContract.Builder` | `clearBuyTokenId()` `bytes buy_token_id = 4;` |
    | `Contract.MarketSellAssetContract.Builder` | `clearBuyTokenQuantity()` min to receive |
    | `Contract.MarketSellAssetContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.MarketSellAssetContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.MarketSellAssetContract.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `Contract.MarketSellAssetContract.Builder` | `clearSellTokenId()` `bytes sell_token_id = 2;` |
    | `Contract.MarketSellAssetContract.Builder` | `clearSellTokenQuantity()` `int64 sell_token_quantity = 3;` |
    | `Contract.MarketSellAssetContract.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getBuyTokenId()` `bytes buy_token_id = 4;` |
    | `long` | `getBuyTokenQuantity()` min to receive |
    | `Contract.MarketSellAssetContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `com.google.protobuf.ByteString` | `getSellTokenId()` `bytes sell_token_id = 2;` |
    | `long` | `getSellTokenQuantity()` `int64 sell_token_quantity = 3;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.MarketSellAssetContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.MarketSellAssetContract.Builder` | `mergeFrom(Contract.MarketSellAssetContract other)` |
    | `Contract.MarketSellAssetContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.MarketSellAssetContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.MarketSellAssetContract.Builder` | `setBuyTokenId(com.google.protobuf.ByteString value)` `bytes buy_token_id = 4;` |
    | `Contract.MarketSellAssetContract.Builder` | `setBuyTokenQuantity(long value)` min to receive |
    | `Contract.MarketSellAssetContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.MarketSellAssetContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `Contract.MarketSellAssetContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.MarketSellAssetContract.Builder` | `setSellTokenId(com.google.protobuf.ByteString value)` `bytes sell_token_id = 2;` |
    | `Contract.MarketSellAssetContract.Builder` | `setSellTokenQuantity(long value)` `int64 sell_token_quantity = 3;` |
    | `Contract.MarketSellAssetContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketSellAssetContract.Builder>`
    - #### clear

      ```
      public Contract.MarketSellAssetContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketSellAssetContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketSellAssetContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.MarketSellAssetContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.MarketSellAssetContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.MarketSellAssetContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.MarketSellAssetContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketSellAssetContract.Builder>`
    - #### setField

      ```
      public Contract.MarketSellAssetContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketSellAssetContract.Builder>`
    - #### clearField

      ```
      public Contract.MarketSellAssetContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketSellAssetContract.Builder>`
    - #### clearOneof

      ```
      public Contract.MarketSellAssetContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketSellAssetContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.MarketSellAssetContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                       int index,
                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketSellAssetContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.MarketSellAssetContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketSellAssetContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.MarketSellAssetContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.MarketSellAssetContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.MarketSellAssetContract.Builder mergeFrom(Contract.MarketSellAssetContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketSellAssetContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.MarketSellAssetContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.MarketSellAssetContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.MarketSellAssetContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.MarketSellAssetContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.MarketSellAssetContract.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getSellTokenId

      ```
      public com.google.protobuf.ByteString getSellTokenId()
      ```

      `bytes sell_token_id = 2;`

      Specified by:
      :   `getSellTokenId` in interface `Contract.MarketSellAssetContractOrBuilder`

      Returns:
      :   The sellTokenId.
    - #### setSellTokenId

      ```
      public Contract.MarketSellAssetContract.Builder setSellTokenId(com.google.protobuf.ByteString value)
      ```

      `bytes sell_token_id = 2;`

      Parameters:
      :   `value` - The sellTokenId to set.

      Returns:
      :   This builder for chaining.
    - #### clearSellTokenId

      ```
      public Contract.MarketSellAssetContract.Builder clearSellTokenId()
      ```

      `bytes sell_token_id = 2;`

      Returns:
      :   This builder for chaining.
    - #### getSellTokenQuantity

      ```
      public long getSellTokenQuantity()
      ```

      `int64 sell_token_quantity = 3;`

      Specified by:
      :   `getSellTokenQuantity` in interface `Contract.MarketSellAssetContractOrBuilder`

      Returns:
      :   The sellTokenQuantity.
    - #### setSellTokenQuantity

      ```
      public Contract.MarketSellAssetContract.Builder setSellTokenQuantity(long value)
      ```

      `int64 sell_token_quantity = 3;`

      Parameters:
      :   `value` - The sellTokenQuantity to set.

      Returns:
      :   This builder for chaining.
    - #### clearSellTokenQuantity

      ```
      public Contract.MarketSellAssetContract.Builder clearSellTokenQuantity()
      ```

      `int64 sell_token_quantity = 3;`

      Returns:
      :   This builder for chaining.
    - #### getBuyTokenId

      ```
      public com.google.protobuf.ByteString getBuyTokenId()
      ```

      `bytes buy_token_id = 4;`

      Specified by:
      :   `getBuyTokenId` in interface `Contract.MarketSellAssetContractOrBuilder`

      Returns:
      :   The buyTokenId.
    - #### setBuyTokenId

      ```
      public Contract.MarketSellAssetContract.Builder setBuyTokenId(com.google.protobuf.ByteString value)
      ```

      `bytes buy_token_id = 4;`

      Parameters:
      :   `value` - The buyTokenId to set.

      Returns:
      :   This builder for chaining.
    - #### clearBuyTokenId

      ```
      public Contract.MarketSellAssetContract.Builder clearBuyTokenId()
      ```

      `bytes buy_token_id = 4;`

      Returns:
      :   This builder for chaining.
    - #### getBuyTokenQuantity

      ```
      public long getBuyTokenQuantity()
      ```

      ```
       min to receive
      ```

      `int64 buy_token_quantity = 5;`

      Specified by:
      :   `getBuyTokenQuantity` in interface `Contract.MarketSellAssetContractOrBuilder`

      Returns:
      :   The buyTokenQuantity.
    - #### setBuyTokenQuantity

      ```
      public Contract.MarketSellAssetContract.Builder setBuyTokenQuantity(long value)
      ```

      ```
       min to receive
      ```

      `int64 buy_token_quantity = 5;`

      Parameters:
      :   `value` - The buyTokenQuantity to set.

      Returns:
      :   This builder for chaining.
    - #### clearBuyTokenQuantity

      ```
      public Contract.MarketSellAssetContract.Builder clearBuyTokenQuantity()
      ```

      ```
       min to receive
      ```

      `int64 buy_token_quantity = 5;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.MarketSellAssetContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketSellAssetContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.MarketSellAssetContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketSellAssetContract.Builder>`