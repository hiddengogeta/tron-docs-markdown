

org.tron.trident.proto

## Class Contract.AccountCreateContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.AccountCreateContract.Builder](../../../../org/tron/trident/proto/Contract.AccountCreateContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.AccountCreateContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.AccountCreateContractOrBuilder](../../../../org/tron/trident/proto/Contract.AccountCreateContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.AccountCreateContract](../../../../org/tron/trident/proto/Contract.AccountCreateContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.AccountCreateContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountCreateContract.Builder>
  implements Contract.AccountCreateContractOrBuilder
  ```

  Protobuf type `protocol.AccountCreateContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.AccountCreateContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.AccountCreateContract` | `build()` |
    | `Contract.AccountCreateContract` | `buildPartial()` |
    | `Contract.AccountCreateContract.Builder` | `clear()` |
    | `Contract.AccountCreateContract.Builder` | `clearAccountAddress()` `bytes account_address = 2;` |
    | `Contract.AccountCreateContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.AccountCreateContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.AccountCreateContract.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `Contract.AccountCreateContract.Builder` | `clearType()` `.protocol.AccountType type = 3;` |
    | `Contract.AccountCreateContract.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getAccountAddress()` `bytes account_address = 2;` |
    | `Contract.AccountCreateContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `Common.AccountType` | `getType()` `.protocol.AccountType type = 3;` |
    | `int` | `getTypeValue()` `.protocol.AccountType type = 3;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.AccountCreateContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.AccountCreateContract.Builder` | `mergeFrom(Contract.AccountCreateContract other)` |
    | `Contract.AccountCreateContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.AccountCreateContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.AccountCreateContract.Builder` | `setAccountAddress(com.google.protobuf.ByteString value)` `bytes account_address = 2;` |
    | `Contract.AccountCreateContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.AccountCreateContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `Contract.AccountCreateContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.AccountCreateContract.Builder` | `setType(Common.AccountType value)` `.protocol.AccountType type = 3;` |
    | `Contract.AccountCreateContract.Builder` | `setTypeValue(int value)` `.protocol.AccountType type = 3;` |
    | `Contract.AccountCreateContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountCreateContract.Builder>`
    - #### clear

      ```
      public Contract.AccountCreateContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountCreateContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountCreateContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.AccountCreateContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.AccountCreateContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.AccountCreateContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.AccountCreateContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountCreateContract.Builder>`
    - #### setField

      ```
      public Contract.AccountCreateContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                             java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountCreateContract.Builder>`
    - #### clearField

      ```
      public Contract.AccountCreateContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountCreateContract.Builder>`
    - #### clearOneof

      ```
      public Contract.AccountCreateContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountCreateContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.AccountCreateContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     int index,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountCreateContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.AccountCreateContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountCreateContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.AccountCreateContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.AccountCreateContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.AccountCreateContract.Builder mergeFrom(Contract.AccountCreateContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountCreateContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.AccountCreateContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.AccountCreateContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.AccountCreateContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.AccountCreateContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.AccountCreateContract.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getAccountAddress

      ```
      public com.google.protobuf.ByteString getAccountAddress()
      ```

      `bytes account_address = 2;`

      Specified by:
      :   `getAccountAddress` in interface `Contract.AccountCreateContractOrBuilder`

      Returns:
      :   The accountAddress.
    - #### setAccountAddress

      ```
      public Contract.AccountCreateContract.Builder setAccountAddress(com.google.protobuf.ByteString value)
      ```

      `bytes account_address = 2;`

      Parameters:
      :   `value` - The accountAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearAccountAddress

      ```
      public Contract.AccountCreateContract.Builder clearAccountAddress()
      ```

      `bytes account_address = 2;`

      Returns:
      :   This builder for chaining.
    - #### getTypeValue

      ```
      public int getTypeValue()
      ```

      `.protocol.AccountType type = 3;`

      Specified by:
      :   `getTypeValue` in interface `Contract.AccountCreateContractOrBuilder`

      Returns:
      :   The enum numeric value on the wire for type.
    - #### setTypeValue

      ```
      public Contract.AccountCreateContract.Builder setTypeValue(int value)
      ```

      `.protocol.AccountType type = 3;`

      Parameters:
      :   `value` - The enum numeric value on the wire for type to set.

      Returns:
      :   This builder for chaining.
    - #### getType

      ```
      public Common.AccountType getType()
      ```

      `.protocol.AccountType type = 3;`

      Specified by:
      :   `getType` in interface `Contract.AccountCreateContractOrBuilder`

      Returns:
      :   The type.
    - #### setType

      ```
      public Contract.AccountCreateContract.Builder setType(Common.AccountType value)
      ```

      `.protocol.AccountType type = 3;`

      Parameters:
      :   `value` - The type to set.

      Returns:
      :   This builder for chaining.
    - #### clearType

      ```
      public Contract.AccountCreateContract.Builder clearType()
      ```

      `.protocol.AccountType type = 3;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.AccountCreateContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountCreateContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.AccountCreateContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountCreateContract.Builder>`