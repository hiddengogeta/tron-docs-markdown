

org.tron.trident.proto

## Class Contract.UnfreezeBalanceContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.UnfreezeBalanceContract.Builder](../../../../org/tron/trident/proto/Contract.UnfreezeBalanceContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.UnfreezeBalanceContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.UnfreezeBalanceContractOrBuilder](../../../../org/tron/trident/proto/Contract.UnfreezeBalanceContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.UnfreezeBalanceContract](../../../../org/tron/trident/proto/Contract.UnfreezeBalanceContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.UnfreezeBalanceContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceContract.Builder>
  implements Contract.UnfreezeBalanceContractOrBuilder
  ```

  Protobuf type `protocol.UnfreezeBalanceContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.UnfreezeBalanceContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.UnfreezeBalanceContract` | `build()` |
    | `Contract.UnfreezeBalanceContract` | `buildPartial()` |
    | `Contract.UnfreezeBalanceContract.Builder` | `clear()` |
    | `Contract.UnfreezeBalanceContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.UnfreezeBalanceContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.UnfreezeBalanceContract.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `Contract.UnfreezeBalanceContract.Builder` | `clearReceiverAddress()` `bytes receiver_address = 15;` |
    | `Contract.UnfreezeBalanceContract.Builder` | `clearResource()` `.protocol.ResourceCode resource = 10;` |
    | `Contract.UnfreezeBalanceContract.Builder` | `clone()` |
    | `Contract.UnfreezeBalanceContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `com.google.protobuf.ByteString` | `getReceiverAddress()` `bytes receiver_address = 15;` |
    | `Common.ResourceCode` | `getResource()` `.protocol.ResourceCode resource = 10;` |
    | `int` | `getResourceValue()` `.protocol.ResourceCode resource = 10;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.UnfreezeBalanceContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.UnfreezeBalanceContract.Builder` | `mergeFrom(Contract.UnfreezeBalanceContract other)` |
    | `Contract.UnfreezeBalanceContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.UnfreezeBalanceContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.UnfreezeBalanceContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.UnfreezeBalanceContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `Contract.UnfreezeBalanceContract.Builder` | `setReceiverAddress(com.google.protobuf.ByteString value)` `bytes receiver_address = 15;` |
    | `Contract.UnfreezeBalanceContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.UnfreezeBalanceContract.Builder` | `setResource(Common.ResourceCode value)` `.protocol.ResourceCode resource = 10;` |
    | `Contract.UnfreezeBalanceContract.Builder` | `setResourceValue(int value)` `.protocol.ResourceCode resource = 10;` |
    | `Contract.UnfreezeBalanceContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceContract.Builder>`
    - #### clear

      ```
      public Contract.UnfreezeBalanceContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.UnfreezeBalanceContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.UnfreezeBalanceContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.UnfreezeBalanceContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.UnfreezeBalanceContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceContract.Builder>`
    - #### setField

      ```
      public Contract.UnfreezeBalanceContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceContract.Builder>`
    - #### clearField

      ```
      public Contract.UnfreezeBalanceContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceContract.Builder>`
    - #### clearOneof

      ```
      public Contract.UnfreezeBalanceContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.UnfreezeBalanceContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                       int index,
                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.UnfreezeBalanceContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.UnfreezeBalanceContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.UnfreezeBalanceContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.UnfreezeBalanceContract.Builder mergeFrom(Contract.UnfreezeBalanceContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.UnfreezeBalanceContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.UnfreezeBalanceContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.UnfreezeBalanceContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.UnfreezeBalanceContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.UnfreezeBalanceContract.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getResourceValue

      ```
      public int getResourceValue()
      ```

      `.protocol.ResourceCode resource = 10;`

      Specified by:
      :   `getResourceValue` in interface `Contract.UnfreezeBalanceContractOrBuilder`

      Returns:
      :   The enum numeric value on the wire for resource.
    - #### setResourceValue

      ```
      public Contract.UnfreezeBalanceContract.Builder setResourceValue(int value)
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
      :   `getResource` in interface `Contract.UnfreezeBalanceContractOrBuilder`

      Returns:
      :   The resource.
    - #### setResource

      ```
      public Contract.UnfreezeBalanceContract.Builder setResource(Common.ResourceCode value)
      ```

      `.protocol.ResourceCode resource = 10;`

      Parameters:
      :   `value` - The resource to set.

      Returns:
      :   This builder for chaining.
    - #### clearResource

      ```
      public Contract.UnfreezeBalanceContract.Builder clearResource()
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
      :   `getReceiverAddress` in interface `Contract.UnfreezeBalanceContractOrBuilder`

      Returns:
      :   The receiverAddress.
    - #### setReceiverAddress

      ```
      public Contract.UnfreezeBalanceContract.Builder setReceiverAddress(com.google.protobuf.ByteString value)
      ```

      `bytes receiver_address = 15;`

      Parameters:
      :   `value` - The receiverAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearReceiverAddress

      ```
      public Contract.UnfreezeBalanceContract.Builder clearReceiverAddress()
      ```

      `bytes receiver_address = 15;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.UnfreezeBalanceContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.UnfreezeBalanceContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceContract.Builder>`