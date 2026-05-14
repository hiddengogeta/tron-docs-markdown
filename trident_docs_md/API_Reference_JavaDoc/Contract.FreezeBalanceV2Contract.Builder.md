

org.tron.trident.proto

## Class Contract.FreezeBalanceV2Contract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.FreezeBalanceV2Contract.Builder](../../../../org/tron/trident/proto/Contract.FreezeBalanceV2Contract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.FreezeBalanceV2Contract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.FreezeBalanceV2ContractOrBuilder](../../../../org/tron/trident/proto/Contract.FreezeBalanceV2ContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.FreezeBalanceV2Contract](../../../../org/tron/trident/proto/Contract.FreezeBalanceV2Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.FreezeBalanceV2Contract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceV2Contract.Builder>
  implements Contract.FreezeBalanceV2ContractOrBuilder
  ```

  ```
  stake 2.0
  ```

  Protobuf type `protocol.FreezeBalanceV2Contract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.FreezeBalanceV2Contract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.FreezeBalanceV2Contract` | `build()` |
    | `Contract.FreezeBalanceV2Contract` | `buildPartial()` |
    | `Contract.FreezeBalanceV2Contract.Builder` | `clear()` |
    | `Contract.FreezeBalanceV2Contract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.FreezeBalanceV2Contract.Builder` | `clearFrozenBalance()` `int64 frozen_balance = 2;` |
    | `Contract.FreezeBalanceV2Contract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.FreezeBalanceV2Contract.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `Contract.FreezeBalanceV2Contract.Builder` | `clearResource()` `.protocol.ResourceCode resource = 3;` |
    | `Contract.FreezeBalanceV2Contract.Builder` | `clone()` |
    | `Contract.FreezeBalanceV2Contract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getFrozenBalance()` `int64 frozen_balance = 2;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `Common.ResourceCode` | `getResource()` `.protocol.ResourceCode resource = 3;` |
    | `int` | `getResourceValue()` `.protocol.ResourceCode resource = 3;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.FreezeBalanceV2Contract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.FreezeBalanceV2Contract.Builder` | `mergeFrom(Contract.FreezeBalanceV2Contract other)` |
    | `Contract.FreezeBalanceV2Contract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.FreezeBalanceV2Contract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.FreezeBalanceV2Contract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.FreezeBalanceV2Contract.Builder` | `setFrozenBalance(long value)` `int64 frozen_balance = 2;` |
    | `Contract.FreezeBalanceV2Contract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `Contract.FreezeBalanceV2Contract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.FreezeBalanceV2Contract.Builder` | `setResource(Common.ResourceCode value)` `.protocol.ResourceCode resource = 3;` |
    | `Contract.FreezeBalanceV2Contract.Builder` | `setResourceValue(int value)` `.protocol.ResourceCode resource = 3;` |
    | `Contract.FreezeBalanceV2Contract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceV2Contract.Builder>`
    - #### clear

      ```
      public Contract.FreezeBalanceV2Contract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceV2Contract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceV2Contract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.FreezeBalanceV2Contract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.FreezeBalanceV2Contract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.FreezeBalanceV2Contract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.FreezeBalanceV2Contract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceV2Contract.Builder>`
    - #### setField

      ```
      public Contract.FreezeBalanceV2Contract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceV2Contract.Builder>`
    - #### clearField

      ```
      public Contract.FreezeBalanceV2Contract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceV2Contract.Builder>`
    - #### clearOneof

      ```
      public Contract.FreezeBalanceV2Contract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceV2Contract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.FreezeBalanceV2Contract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                       int index,
                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceV2Contract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.FreezeBalanceV2Contract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceV2Contract.Builder>`
    - #### mergeFrom

      ```
      public Contract.FreezeBalanceV2Contract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.FreezeBalanceV2Contract.Builder>`
    - #### mergeFrom

      ```
      public Contract.FreezeBalanceV2Contract.Builder mergeFrom(Contract.FreezeBalanceV2Contract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceV2Contract.Builder>`
    - #### mergeFrom

      ```
      public Contract.FreezeBalanceV2Contract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.FreezeBalanceV2Contract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.FreezeBalanceV2ContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.FreezeBalanceV2Contract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.FreezeBalanceV2Contract.Builder clearOwnerAddress()
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
      :   `getFrozenBalance` in interface `Contract.FreezeBalanceV2ContractOrBuilder`

      Returns:
      :   The frozenBalance.
    - #### setFrozenBalance

      ```
      public Contract.FreezeBalanceV2Contract.Builder setFrozenBalance(long value)
      ```

      `int64 frozen_balance = 2;`

      Parameters:
      :   `value` - The frozenBalance to set.

      Returns:
      :   This builder for chaining.
    - #### clearFrozenBalance

      ```
      public Contract.FreezeBalanceV2Contract.Builder clearFrozenBalance()
      ```

      `int64 frozen_balance = 2;`

      Returns:
      :   This builder for chaining.
    - #### getResourceValue

      ```
      public int getResourceValue()
      ```

      `.protocol.ResourceCode resource = 3;`

      Specified by:
      :   `getResourceValue` in interface `Contract.FreezeBalanceV2ContractOrBuilder`

      Returns:
      :   The enum numeric value on the wire for resource.
    - #### setResourceValue

      ```
      public Contract.FreezeBalanceV2Contract.Builder setResourceValue(int value)
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
      :   `getResource` in interface `Contract.FreezeBalanceV2ContractOrBuilder`

      Returns:
      :   The resource.
    - #### setResource

      ```
      public Contract.FreezeBalanceV2Contract.Builder setResource(Common.ResourceCode value)
      ```

      `.protocol.ResourceCode resource = 3;`

      Parameters:
      :   `value` - The resource to set.

      Returns:
      :   This builder for chaining.
    - #### clearResource

      ```
      public Contract.FreezeBalanceV2Contract.Builder clearResource()
      ```

      `.protocol.ResourceCode resource = 3;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.FreezeBalanceV2Contract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceV2Contract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.FreezeBalanceV2Contract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.FreezeBalanceV2Contract.Builder>`