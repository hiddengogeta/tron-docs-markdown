

org.tron.trident.proto

## Class Contract.MarketCancelOrderContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.MarketCancelOrderContract.Builder](../../../../org/tron/trident/proto/Contract.MarketCancelOrderContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.MarketCancelOrderContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.MarketCancelOrderContractOrBuilder](../../../../org/tron/trident/proto/Contract.MarketCancelOrderContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.MarketCancelOrderContract](../../../../org/tron/trident/proto/Contract.MarketCancelOrderContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.MarketCancelOrderContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketCancelOrderContract.Builder>
  implements Contract.MarketCancelOrderContractOrBuilder
  ```

  Protobuf type `protocol.MarketCancelOrderContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.MarketCancelOrderContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.MarketCancelOrderContract` | `build()` |
    | `Contract.MarketCancelOrderContract` | `buildPartial()` |
    | `Contract.MarketCancelOrderContract.Builder` | `clear()` |
    | `Contract.MarketCancelOrderContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.MarketCancelOrderContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.MarketCancelOrderContract.Builder` | `clearOrderId()` `bytes order_id = 2;` |
    | `Contract.MarketCancelOrderContract.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `Contract.MarketCancelOrderContract.Builder` | `clone()` |
    | `Contract.MarketCancelOrderContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getOrderId()` `bytes order_id = 2;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.MarketCancelOrderContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.MarketCancelOrderContract.Builder` | `mergeFrom(Contract.MarketCancelOrderContract other)` |
    | `Contract.MarketCancelOrderContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.MarketCancelOrderContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.MarketCancelOrderContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.MarketCancelOrderContract.Builder` | `setOrderId(com.google.protobuf.ByteString value)` `bytes order_id = 2;` |
    | `Contract.MarketCancelOrderContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `Contract.MarketCancelOrderContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.MarketCancelOrderContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketCancelOrderContract.Builder>`
    - #### clear

      ```
      public Contract.MarketCancelOrderContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketCancelOrderContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketCancelOrderContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.MarketCancelOrderContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.MarketCancelOrderContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.MarketCancelOrderContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.MarketCancelOrderContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketCancelOrderContract.Builder>`
    - #### setField

      ```
      public Contract.MarketCancelOrderContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketCancelOrderContract.Builder>`
    - #### clearField

      ```
      public Contract.MarketCancelOrderContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketCancelOrderContract.Builder>`
    - #### clearOneof

      ```
      public Contract.MarketCancelOrderContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketCancelOrderContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.MarketCancelOrderContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                         int index,
                                                                         java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketCancelOrderContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.MarketCancelOrderContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                         java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketCancelOrderContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.MarketCancelOrderContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.MarketCancelOrderContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.MarketCancelOrderContract.Builder mergeFrom(Contract.MarketCancelOrderContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketCancelOrderContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.MarketCancelOrderContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                  com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                           throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.MarketCancelOrderContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.MarketCancelOrderContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.MarketCancelOrderContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.MarketCancelOrderContract.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getOrderId

      ```
      public com.google.protobuf.ByteString getOrderId()
      ```

      `bytes order_id = 2;`

      Specified by:
      :   `getOrderId` in interface `Contract.MarketCancelOrderContractOrBuilder`

      Returns:
      :   The orderId.
    - #### setOrderId

      ```
      public Contract.MarketCancelOrderContract.Builder setOrderId(com.google.protobuf.ByteString value)
      ```

      `bytes order_id = 2;`

      Parameters:
      :   `value` - The orderId to set.

      Returns:
      :   This builder for chaining.
    - #### clearOrderId

      ```
      public Contract.MarketCancelOrderContract.Builder clearOrderId()
      ```

      `bytes order_id = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.MarketCancelOrderContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketCancelOrderContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.MarketCancelOrderContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.MarketCancelOrderContract.Builder>`