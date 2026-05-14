

org.tron.trident.proto

## Class Contract.UnfreezeBalanceV2Contract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.UnfreezeBalanceV2Contract.Builder](../../../../org/tron/trident/proto/Contract.UnfreezeBalanceV2Contract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.UnfreezeBalanceV2Contract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.UnfreezeBalanceV2ContractOrBuilder](../../../../org/tron/trident/proto/Contract.UnfreezeBalanceV2ContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.UnfreezeBalanceV2Contract](../../../../org/tron/trident/proto/Contract.UnfreezeBalanceV2Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.UnfreezeBalanceV2Contract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceV2Contract.Builder>
  implements Contract.UnfreezeBalanceV2ContractOrBuilder
  ```

  Protobuf type `protocol.UnfreezeBalanceV2Contract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.UnfreezeBalanceV2Contract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.UnfreezeBalanceV2Contract` | `build()` |
    | `Contract.UnfreezeBalanceV2Contract` | `buildPartial()` |
    | `Contract.UnfreezeBalanceV2Contract.Builder` | `clear()` |
    | `Contract.UnfreezeBalanceV2Contract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.UnfreezeBalanceV2Contract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.UnfreezeBalanceV2Contract.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `Contract.UnfreezeBalanceV2Contract.Builder` | `clearResource()` `.protocol.ResourceCode resource = 3;` |
    | `Contract.UnfreezeBalanceV2Contract.Builder` | `clearUnfreezeBalance()` `int64 unfreeze_balance = 2;` |
    | `Contract.UnfreezeBalanceV2Contract.Builder` | `clone()` |
    | `Contract.UnfreezeBalanceV2Contract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `Common.ResourceCode` | `getResource()` `.protocol.ResourceCode resource = 3;` |
    | `int` | `getResourceValue()` `.protocol.ResourceCode resource = 3;` |
    | `long` | `getUnfreezeBalance()` `int64 unfreeze_balance = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.UnfreezeBalanceV2Contract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.UnfreezeBalanceV2Contract.Builder` | `mergeFrom(Contract.UnfreezeBalanceV2Contract other)` |
    | `Contract.UnfreezeBalanceV2Contract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.UnfreezeBalanceV2Contract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.UnfreezeBalanceV2Contract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.UnfreezeBalanceV2Contract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `Contract.UnfreezeBalanceV2Contract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.UnfreezeBalanceV2Contract.Builder` | `setResource(Common.ResourceCode value)` `.protocol.ResourceCode resource = 3;` |
    | `Contract.UnfreezeBalanceV2Contract.Builder` | `setResourceValue(int value)` `.protocol.ResourceCode resource = 3;` |
    | `Contract.UnfreezeBalanceV2Contract.Builder` | `setUnfreezeBalance(long value)` `int64 unfreeze_balance = 2;` |
    | `Contract.UnfreezeBalanceV2Contract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceV2Contract.Builder>`
    - #### clear

      ```
      public Contract.UnfreezeBalanceV2Contract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceV2Contract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceV2Contract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.UnfreezeBalanceV2Contract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.UnfreezeBalanceV2Contract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.UnfreezeBalanceV2Contract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.UnfreezeBalanceV2Contract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceV2Contract.Builder>`
    - #### setField

      ```
      public Contract.UnfreezeBalanceV2Contract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceV2Contract.Builder>`
    - #### clearField

      ```
      public Contract.UnfreezeBalanceV2Contract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceV2Contract.Builder>`
    - #### clearOneof

      ```
      public Contract.UnfreezeBalanceV2Contract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceV2Contract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.UnfreezeBalanceV2Contract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                         int index,
                                                                         java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceV2Contract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.UnfreezeBalanceV2Contract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                         java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceV2Contract.Builder>`
    - #### mergeFrom

      ```
      public Contract.UnfreezeBalanceV2Contract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.UnfreezeBalanceV2Contract.Builder>`
    - #### mergeFrom

      ```
      public Contract.UnfreezeBalanceV2Contract.Builder mergeFrom(Contract.UnfreezeBalanceV2Contract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceV2Contract.Builder>`
    - #### mergeFrom

      ```
      public Contract.UnfreezeBalanceV2Contract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                  com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                           throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.UnfreezeBalanceV2Contract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.UnfreezeBalanceV2ContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.UnfreezeBalanceV2Contract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.UnfreezeBalanceV2Contract.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getUnfreezeBalance

      ```
      public long getUnfreezeBalance()
      ```

      `int64 unfreeze_balance = 2;`

      Specified by:
      :   `getUnfreezeBalance` in interface `Contract.UnfreezeBalanceV2ContractOrBuilder`

      Returns:
      :   The unfreezeBalance.
    - #### setUnfreezeBalance

      ```
      public Contract.UnfreezeBalanceV2Contract.Builder setUnfreezeBalance(long value)
      ```

      `int64 unfreeze_balance = 2;`

      Parameters:
      :   `value` - The unfreezeBalance to set.

      Returns:
      :   This builder for chaining.
    - #### clearUnfreezeBalance

      ```
      public Contract.UnfreezeBalanceV2Contract.Builder clearUnfreezeBalance()
      ```

      `int64 unfreeze_balance = 2;`

      Returns:
      :   This builder for chaining.
    - #### getResourceValue

      ```
      public int getResourceValue()
      ```

      `.protocol.ResourceCode resource = 3;`

      Specified by:
      :   `getResourceValue` in interface `Contract.UnfreezeBalanceV2ContractOrBuilder`

      Returns:
      :   The enum numeric value on the wire for resource.
    - #### setResourceValue

      ```
      public Contract.UnfreezeBalanceV2Contract.Builder setResourceValue(int value)
      ```

      `.protocol.ResourceCode resource = 3;`

      Parameters:
      :   `value` - The enum numeric value on the wire for resource to set.

      Returns:
      :   This builder for chaining.
    - #### getResource

      ```
      public Common.ResourceCode getResource()
      ```

      `.protocol.ResourceCode resource = 3;`

      Specified by:
      :   `getResource` in interface `Contract.UnfreezeBalanceV2ContractOrBuilder`

      Returns:
      :   The resource.
    - #### setResource

      ```
      public Contract.UnfreezeBalanceV2Contract.Builder setResource(Common.ResourceCode value)
      ```

      `.protocol.ResourceCode resource = 3;`

      Parameters:
      :   `value` - The resource to set.

      Returns:
      :   This builder for chaining.
    - #### clearResource

      ```
      public Contract.UnfreezeBalanceV2Contract.Builder clearResource()
      ```

      `.protocol.ResourceCode resource = 3;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.UnfreezeBalanceV2Contract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceV2Contract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.UnfreezeBalanceV2Contract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.UnfreezeBalanceV2Contract.Builder>`