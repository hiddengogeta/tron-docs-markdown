

org.tron.trident.proto

## Class Contract.DelegateResourceContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.DelegateResourceContract.Builder](../../../../org/tron/trident/proto/Contract.DelegateResourceContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.DelegateResourceContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.DelegateResourceContractOrBuilder](../../../../org/tron/trident/proto/Contract.DelegateResourceContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.DelegateResourceContract](../../../../org/tron/trident/proto/Contract.DelegateResourceContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.DelegateResourceContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.DelegateResourceContract.Builder>
  implements Contract.DelegateResourceContractOrBuilder
  ```

  Protobuf type `protocol.DelegateResourceContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.DelegateResourceContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.DelegateResourceContract` | `build()` |
    | `Contract.DelegateResourceContract` | `buildPartial()` |
    | `Contract.DelegateResourceContract.Builder` | `clear()` |
    | `Contract.DelegateResourceContract.Builder` | `clearBalance()` `int64 balance = 3;` |
    | `Contract.DelegateResourceContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.DelegateResourceContract.Builder` | `clearLock()` `bool lock = 5;` |
    | `Contract.DelegateResourceContract.Builder` | `clearLockPeriod()` `int64 lock_period = 6;` |
    | `Contract.DelegateResourceContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.DelegateResourceContract.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `Contract.DelegateResourceContract.Builder` | `clearReceiverAddress()` `bytes receiver_address = 4;` |
    | `Contract.DelegateResourceContract.Builder` | `clearResource()` `.protocol.ResourceCode resource = 2;` |
    | `Contract.DelegateResourceContract.Builder` | `clone()` |
    | `long` | `getBalance()` `int64 balance = 3;` |
    | `Contract.DelegateResourceContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `boolean` | `getLock()` `bool lock = 5;` |
    | `long` | `getLockPeriod()` `int64 lock_period = 6;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `com.google.protobuf.ByteString` | `getReceiverAddress()` `bytes receiver_address = 4;` |
    | `Common.ResourceCode` | `getResource()` `.protocol.ResourceCode resource = 2;` |
    | `int` | `getResourceValue()` `.protocol.ResourceCode resource = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.DelegateResourceContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.DelegateResourceContract.Builder` | `mergeFrom(Contract.DelegateResourceContract other)` |
    | `Contract.DelegateResourceContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.DelegateResourceContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.DelegateResourceContract.Builder` | `setBalance(long value)` `int64 balance = 3;` |
    | `Contract.DelegateResourceContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.DelegateResourceContract.Builder` | `setLock(boolean value)` `bool lock = 5;` |
    | `Contract.DelegateResourceContract.Builder` | `setLockPeriod(long value)` `int64 lock_period = 6;` |
    | `Contract.DelegateResourceContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `Contract.DelegateResourceContract.Builder` | `setReceiverAddress(com.google.protobuf.ByteString value)` `bytes receiver_address = 4;` |
    | `Contract.DelegateResourceContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.DelegateResourceContract.Builder` | `setResource(Common.ResourceCode value)` `.protocol.ResourceCode resource = 2;` |
    | `Contract.DelegateResourceContract.Builder` | `setResourceValue(int value)` `.protocol.ResourceCode resource = 2;` |
    | `Contract.DelegateResourceContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.DelegateResourceContract.Builder>`
    - #### clear

      ```
      public Contract.DelegateResourceContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.DelegateResourceContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.DelegateResourceContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.DelegateResourceContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.DelegateResourceContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.DelegateResourceContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.DelegateResourceContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.DelegateResourceContract.Builder>`
    - #### setField

      ```
      public Contract.DelegateResourceContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.DelegateResourceContract.Builder>`
    - #### clearField

      ```
      public Contract.DelegateResourceContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.DelegateResourceContract.Builder>`
    - #### clearOneof

      ```
      public Contract.DelegateResourceContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.DelegateResourceContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.DelegateResourceContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                        int index,
                                                                        java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.DelegateResourceContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.DelegateResourceContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                        java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.DelegateResourceContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.DelegateResourceContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.DelegateResourceContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.DelegateResourceContract.Builder mergeFrom(Contract.DelegateResourceContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.DelegateResourceContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.DelegateResourceContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                 com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                          throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.DelegateResourceContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.DelegateResourceContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.DelegateResourceContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.DelegateResourceContract.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getResourceValue

      ```
      public int getResourceValue()
      ```

      `.protocol.ResourceCode resource = 2;`

      Specified by:
      :   `getResourceValue` in interface `Contract.DelegateResourceContractOrBuilder`

      Returns:
      :   The enum numeric value on the wire for resource.
    - #### setResourceValue

      ```
      public Contract.DelegateResourceContract.Builder setResourceValue(int value)
      ```

      `.protocol.ResourceCode resource = 2;`

      Parameters:
      :   `value` - The enum numeric value on the wire for resource to set.

      Returns:
      :   This builder for chaining.
    - #### getResource

      ```
      public Common.ResourceCode getResource()
      ```

      `.protocol.ResourceCode resource = 2;`

      Specified by:
      :   `getResource` in interface `Contract.DelegateResourceContractOrBuilder`

      Returns:
      :   The resource.
    - #### setResource

      ```
      public Contract.DelegateResourceContract.Builder setResource(Common.ResourceCode value)
      ```

      `.protocol.ResourceCode resource = 2;`

      Parameters:
      :   `value` - The resource to set.

      Returns:
      :   This builder for chaining.
    - #### clearResource

      ```
      public Contract.DelegateResourceContract.Builder clearResource()
      ```

      `.protocol.ResourceCode resource = 2;`

      Returns:
      :   This builder for chaining.
    - #### getBalance

      ```
      public long getBalance()
      ```

      `int64 balance = 3;`

      Specified by:
      :   `getBalance` in interface `Contract.DelegateResourceContractOrBuilder`

      Returns:
      :   The balance.
    - #### setBalance

      ```
      public Contract.DelegateResourceContract.Builder setBalance(long value)
      ```

      `int64 balance = 3;`

      Parameters:
      :   `value` - The balance to set.

      Returns:
      :   This builder for chaining.
    - #### clearBalance

      ```
      public Contract.DelegateResourceContract.Builder clearBalance()
      ```

      `int64 balance = 3;`

      Returns:
      :   This builder for chaining.
    - #### getReceiverAddress

      ```
      public com.google.protobuf.ByteString getReceiverAddress()
      ```

      `bytes receiver_address = 4;`

      Specified by:
      :   `getReceiverAddress` in interface `Contract.DelegateResourceContractOrBuilder`

      Returns:
      :   The receiverAddress.
    - #### setReceiverAddress

      ```
      public Contract.DelegateResourceContract.Builder setReceiverAddress(com.google.protobuf.ByteString value)
      ```

      `bytes receiver_address = 4;`

      Parameters:
      :   `value` - The receiverAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearReceiverAddress

      ```
      public Contract.DelegateResourceContract.Builder clearReceiverAddress()
      ```

      `bytes receiver_address = 4;`

      Returns:
      :   This builder for chaining.
    - #### getLock

      ```
      public boolean getLock()
      ```

      `bool lock = 5;`

      Specified by:
      :   `getLock` in interface `Contract.DelegateResourceContractOrBuilder`

      Returns:
      :   The lock.
    - #### setLock

      ```
      public Contract.DelegateResourceContract.Builder setLock(boolean value)
      ```

      `bool lock = 5;`

      Parameters:
      :   `value` - The lock to set.

      Returns:
      :   This builder for chaining.
    - #### clearLock

      ```
      public Contract.DelegateResourceContract.Builder clearLock()
      ```

      `bool lock = 5;`

      Returns:
      :   This builder for chaining.
    - #### getLockPeriod

      ```
      public long getLockPeriod()
      ```

      `int64 lock_period = 6;`

      Specified by:
      :   `getLockPeriod` in interface `Contract.DelegateResourceContractOrBuilder`

      Returns:
      :   The lockPeriod.
    - #### setLockPeriod

      ```
      public Contract.DelegateResourceContract.Builder setLockPeriod(long value)
      ```

      `int64 lock_period = 6;`

      Parameters:
      :   `value` - The lockPeriod to set.

      Returns:
      :   This builder for chaining.
    - #### clearLockPeriod

      ```
      public Contract.DelegateResourceContract.Builder clearLockPeriod()
      ```

      `int64 lock_period = 6;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.DelegateResourceContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.DelegateResourceContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.DelegateResourceContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.DelegateResourceContract.Builder>`