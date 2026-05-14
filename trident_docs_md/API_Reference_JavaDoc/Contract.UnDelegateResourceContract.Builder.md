

org.tron.trident.proto

## Class Contract.UnDelegateResourceContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.UnDelegateResourceContract.Builder](../../../../org/tron/trident/proto/Contract.UnDelegateResourceContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.UnDelegateResourceContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.UnDelegateResourceContractOrBuilder](../../../../org/tron/trident/proto/Contract.UnDelegateResourceContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.UnDelegateResourceContract](../../../../org/tron/trident/proto/Contract.UnDelegateResourceContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.UnDelegateResourceContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnDelegateResourceContract.Builder>
  implements Contract.UnDelegateResourceContractOrBuilder
  ```

  Protobuf type `protocol.UnDelegateResourceContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.UnDelegateResourceContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.UnDelegateResourceContract` | `build()` |
    | `Contract.UnDelegateResourceContract` | `buildPartial()` |
    | `Contract.UnDelegateResourceContract.Builder` | `clear()` |
    | `Contract.UnDelegateResourceContract.Builder` | `clearBalance()` `int64 balance = 3;` |
    | `Contract.UnDelegateResourceContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.UnDelegateResourceContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.UnDelegateResourceContract.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `Contract.UnDelegateResourceContract.Builder` | `clearReceiverAddress()` `bytes receiver_address = 4;` |
    | `Contract.UnDelegateResourceContract.Builder` | `clearResource()` `.protocol.ResourceCode resource = 2;` |
    | `Contract.UnDelegateResourceContract.Builder` | `clone()` |
    | `long` | `getBalance()` `int64 balance = 3;` |
    | `Contract.UnDelegateResourceContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `com.google.protobuf.ByteString` | `getReceiverAddress()` `bytes receiver_address = 4;` |
    | `Common.ResourceCode` | `getResource()` `.protocol.ResourceCode resource = 2;` |
    | `int` | `getResourceValue()` `.protocol.ResourceCode resource = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.UnDelegateResourceContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.UnDelegateResourceContract.Builder` | `mergeFrom(Contract.UnDelegateResourceContract other)` |
    | `Contract.UnDelegateResourceContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.UnDelegateResourceContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.UnDelegateResourceContract.Builder` | `setBalance(long value)` `int64 balance = 3;` |
    | `Contract.UnDelegateResourceContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.UnDelegateResourceContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `Contract.UnDelegateResourceContract.Builder` | `setReceiverAddress(com.google.protobuf.ByteString value)` `bytes receiver_address = 4;` |
    | `Contract.UnDelegateResourceContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.UnDelegateResourceContract.Builder` | `setResource(Common.ResourceCode value)` `.protocol.ResourceCode resource = 2;` |
    | `Contract.UnDelegateResourceContract.Builder` | `setResourceValue(int value)` `.protocol.ResourceCode resource = 2;` |
    | `Contract.UnDelegateResourceContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnDelegateResourceContract.Builder>`
    - #### clear

      ```
      public Contract.UnDelegateResourceContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnDelegateResourceContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnDelegateResourceContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.UnDelegateResourceContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.UnDelegateResourceContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.UnDelegateResourceContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.UnDelegateResourceContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnDelegateResourceContract.Builder>`
    - #### setField

      ```
      public Contract.UnDelegateResourceContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                  java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnDelegateResourceContract.Builder>`
    - #### clearField

      ```
      public Contract.UnDelegateResourceContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnDelegateResourceContract.Builder>`
    - #### clearOneof

      ```
      public Contract.UnDelegateResourceContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnDelegateResourceContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.UnDelegateResourceContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                          int index,
                                                                          java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnDelegateResourceContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.UnDelegateResourceContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                          java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnDelegateResourceContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.UnDelegateResourceContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.UnDelegateResourceContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.UnDelegateResourceContract.Builder mergeFrom(Contract.UnDelegateResourceContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnDelegateResourceContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.UnDelegateResourceContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                   com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                            throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.UnDelegateResourceContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.UnDelegateResourceContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.UnDelegateResourceContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.UnDelegateResourceContract.Builder clearOwnerAddress()
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
      :   `getResourceValue` in interface `Contract.UnDelegateResourceContractOrBuilder`

      Returns:
      :   The enum numeric value on the wire for resource.
    - #### setResourceValue

      ```
      public Contract.UnDelegateResourceContract.Builder setResourceValue(int value)
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
      :   `getResource` in interface `Contract.UnDelegateResourceContractOrBuilder`

      Returns:
      :   The resource.
    - #### setResource

      ```
      public Contract.UnDelegateResourceContract.Builder setResource(Common.ResourceCode value)
      ```

      `.protocol.ResourceCode resource = 2;`

      Parameters:
      :   `value` - The resource to set.

      Returns:
      :   This builder for chaining.
    - #### clearResource

      ```
      public Contract.UnDelegateResourceContract.Builder clearResource()
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
      :   `getBalance` in interface `Contract.UnDelegateResourceContractOrBuilder`

      Returns:
      :   The balance.
    - #### setBalance

      ```
      public Contract.UnDelegateResourceContract.Builder setBalance(long value)
      ```

      `int64 balance = 3;`

      Parameters:
      :   `value` - The balance to set.

      Returns:
      :   This builder for chaining.
    - #### clearBalance

      ```
      public Contract.UnDelegateResourceContract.Builder clearBalance()
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
      :   `getReceiverAddress` in interface `Contract.UnDelegateResourceContractOrBuilder`

      Returns:
      :   The receiverAddress.
    - #### setReceiverAddress

      ```
      public Contract.UnDelegateResourceContract.Builder setReceiverAddress(com.google.protobuf.ByteString value)
      ```

      `bytes receiver_address = 4;`

      Parameters:
      :   `value` - The receiverAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearReceiverAddress

      ```
      public Contract.UnDelegateResourceContract.Builder clearReceiverAddress()
      ```

      `bytes receiver_address = 4;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.UnDelegateResourceContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnDelegateResourceContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.UnDelegateResourceContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnDelegateResourceContract.Builder>`