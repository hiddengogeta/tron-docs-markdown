

org.tron.trident.proto

## Class Contract.FreezeBalanceContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.FreezeBalanceContract.Builder](../../../../org/tron/trident/proto/Contract.FreezeBalanceContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.FreezeBalanceContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.FreezeBalanceContractOrBuilder](../../../../org/tron/trident/proto/Contract.FreezeBalanceContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.FreezeBalanceContract](../../../../org/tron/trident/proto/Contract.FreezeBalanceContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.FreezeBalanceContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceContract.Builder>
  implements Contract.FreezeBalanceContractOrBuilder
  ```

  Protobuf type `protocol.FreezeBalanceContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.FreezeBalanceContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.FreezeBalanceContract` | `build()` |
    | `Contract.FreezeBalanceContract` | `buildPartial()` |
    | `Contract.FreezeBalanceContract.Builder` | `clear()` |
    | `Contract.FreezeBalanceContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.FreezeBalanceContract.Builder` | `clearFrozenBalance()` `int64 frozen_balance = 2;` |
    | `Contract.FreezeBalanceContract.Builder` | `clearFrozenDuration()` `int64 frozen_duration = 3;` |
    | `Contract.FreezeBalanceContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.FreezeBalanceContract.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `Contract.FreezeBalanceContract.Builder` | `clearReceiverAddress()` `bytes receiver_address = 15;` |
    | `Contract.FreezeBalanceContract.Builder` | `clearResource()` `.protocol.ResourceCode resource = 10;` |
    | `Contract.FreezeBalanceContract.Builder` | `clone()` |
    | `Contract.FreezeBalanceContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getFrozenBalance()` `int64 frozen_balance = 2;` |
    | `long` | `getFrozenDuration()` `int64 frozen_duration = 3;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `com.google.protobuf.ByteString` | `getReceiverAddress()` `bytes receiver_address = 15;` |
    | `Common.ResourceCode` | `getResource()` `.protocol.ResourceCode resource = 10;` |
    | `int` | `getResourceValue()` `.protocol.ResourceCode resource = 10;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.FreezeBalanceContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.FreezeBalanceContract.Builder` | `mergeFrom(Contract.FreezeBalanceContract other)` |
    | `Contract.FreezeBalanceContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.FreezeBalanceContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.FreezeBalanceContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.FreezeBalanceContract.Builder` | `setFrozenBalance(long value)` `int64 frozen_balance = 2;` |
    | `Contract.FreezeBalanceContract.Builder` | `setFrozenDuration(long value)` `int64 frozen_duration = 3;` |
    | `Contract.FreezeBalanceContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `Contract.FreezeBalanceContract.Builder` | `setReceiverAddress(com.google.protobuf.ByteString value)` `bytes receiver_address = 15;` |
    | `Contract.FreezeBalanceContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.FreezeBalanceContract.Builder` | `setResource(Common.ResourceCode value)` `.protocol.ResourceCode resource = 10;` |
    | `Contract.FreezeBalanceContract.Builder` | `setResourceValue(int value)` `.protocol.ResourceCode resource = 10;` |
    | `Contract.FreezeBalanceContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceContract.Builder>`
    - #### clear

      ```
      public Contract.FreezeBalanceContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.FreezeBalanceContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.FreezeBalanceContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.FreezeBalanceContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.FreezeBalanceContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceContract.Builder>`
    - #### setField

      ```
      public Contract.FreezeBalanceContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                             java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceContract.Builder>`
    - #### clearField

      ```
      public Contract.FreezeBalanceContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceContract.Builder>`
    - #### clearOneof

      ```
      public Contract.FreezeBalanceContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.FreezeBalanceContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     int index,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.FreezeBalanceContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.FreezeBalanceContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.FreezeBalanceContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.FreezeBalanceContract.Builder mergeFrom(Contract.FreezeBalanceContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.FreezeBalanceContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.FreezeBalanceContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.FreezeBalanceContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.FreezeBalanceContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.FreezeBalanceContract.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getFrozenBalance

      ```
      public long getFrozenBalance()
      ```

      `int64 frozen_balance = 2;`

      Specified by:
      :   `getFrozenBalance` in interface `Contract.FreezeBalanceContractOrBuilder`

      Returns:
      :   The frozenBalance.
    - #### setFrozenBalance

      ```
      public Contract.FreezeBalanceContract.Builder setFrozenBalance(long value)
      ```

      `int64 frozen_balance = 2;`

      Parameters:
      :   `value` - The frozenBalance to set.

      Returns:
      :   This builder for chaining.
    - #### clearFrozenBalance

      ```
      public Contract.FreezeBalanceContract.Builder clearFrozenBalance()
      ```

      `int64 frozen_balance = 2;`

      Returns:
      :   This builder for chaining.
    - #### getFrozenDuration

      ```
      public long getFrozenDuration()
      ```

      `int64 frozen_duration = 3;`

      Specified by:
      :   `getFrozenDuration` in interface `Contract.FreezeBalanceContractOrBuilder`

      Returns:
      :   The frozenDuration.
    - #### setFrozenDuration

      ```
      public Contract.FreezeBalanceContract.Builder setFrozenDuration(long value)
      ```

      `int64 frozen_duration = 3;`

      Parameters:
      :   `value` - The frozenDuration to set.

      Returns:
      :   This builder for chaining.
    - #### clearFrozenDuration

      ```
      public Contract.FreezeBalanceContract.Builder clearFrozenDuration()
      ```

      `int64 frozen_duration = 3;`

      Returns:
      :   This builder for chaining.
    - #### getResourceValue

      ```
      public int getResourceValue()
      ```

      `.protocol.ResourceCode resource = 10;`

      Specified by:
      :   `getResourceValue` in interface `Contract.FreezeBalanceContractOrBuilder`

      Returns:
      :   The enum numeric value on the wire for resource.
    - #### setResourceValue

      ```
      public Contract.FreezeBalanceContract.Builder setResourceValue(int value)
      ```

      `.protocol.ResourceCode resource = 10;`

      Parameters:
      :   `value` - The enum numeric value on the wire for resource to set.

      Returns:
      :   This builder for chaining.
    - #### getResource

      ```
      public Common.ResourceCode getResource()
      ```

      `.protocol.ResourceCode resource = 10;`

      Specified by:
      :   `getResource` in interface `Contract.FreezeBalanceContractOrBuilder`

      Returns:
      :   The resource.
    - #### setResource

      ```
      public Contract.FreezeBalanceContract.Builder setResource(Common.ResourceCode value)
      ```

      `.protocol.ResourceCode resource = 10;`

      Parameters:
      :   `value` - The resource to set.

      Returns:
      :   This builder for chaining.
    - #### clearResource

      ```
      public Contract.FreezeBalanceContract.Builder clearResource()
      ```

      `.protocol.ResourceCode resource = 10;`

      Returns:
      :   This builder for chaining.
    - #### getReceiverAddress

      ```
      public com.google.protobuf.ByteString getReceiverAddress()
      ```

      `bytes receiver_address = 15;`

      Specified by:
      :   `getReceiverAddress` in interface `Contract.FreezeBalanceContractOrBuilder`

      Returns:
      :   The receiverAddress.
    - #### setReceiverAddress

      ```
      public Contract.FreezeBalanceContract.Builder setReceiverAddress(com.google.protobuf.ByteString value)
      ```

      `bytes receiver_address = 15;`

      Parameters:
      :   `value` - The receiverAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearReceiverAddress

      ```
      public Contract.FreezeBalanceContract.Builder clearReceiverAddress()
      ```

      `bytes receiver_address = 15;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.FreezeBalanceContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.FreezeBalanceContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceContract.Builder>`