

org.tron.trident.proto

## Class Contract.AssetIssueContract.FrozenSupply.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.AssetIssueContract.FrozenSupply.Builder](../../../../org/tron/trident/proto/Contract.AssetIssueContract.FrozenSupply.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.AssetIssueContract.FrozenSupply.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.AssetIssueContract.FrozenSupplyOrBuilder](../../../../org/tron/trident/proto/Contract.AssetIssueContract.FrozenSupplyOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.AssetIssueContract.FrozenSupply](../../../../org/tron/trident/proto/Contract.AssetIssueContract.FrozenSupply.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.AssetIssueContract.FrozenSupply.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.FrozenSupply.Builder>
  implements Contract.AssetIssueContract.FrozenSupplyOrBuilder
  ```

  Protobuf type `protocol.AssetIssueContract.FrozenSupply`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.AssetIssueContract.FrozenSupply.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.AssetIssueContract.FrozenSupply` | `build()` |
    | `Contract.AssetIssueContract.FrozenSupply` | `buildPartial()` |
    | `Contract.AssetIssueContract.FrozenSupply.Builder` | `clear()` |
    | `Contract.AssetIssueContract.FrozenSupply.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.AssetIssueContract.FrozenSupply.Builder` | `clearFrozenAmount()` `int64 frozen_amount = 1;` |
    | `Contract.AssetIssueContract.FrozenSupply.Builder` | `clearFrozenDays()` `int64 frozen_days = 2;` |
    | `Contract.AssetIssueContract.FrozenSupply.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.AssetIssueContract.FrozenSupply.Builder` | `clone()` |
    | `Contract.AssetIssueContract.FrozenSupply` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getFrozenAmount()` `int64 frozen_amount = 1;` |
    | `long` | `getFrozenDays()` `int64 frozen_days = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.AssetIssueContract.FrozenSupply.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.AssetIssueContract.FrozenSupply.Builder` | `mergeFrom(Contract.AssetIssueContract.FrozenSupply other)` |
    | `Contract.AssetIssueContract.FrozenSupply.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.AssetIssueContract.FrozenSupply.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.AssetIssueContract.FrozenSupply.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.AssetIssueContract.FrozenSupply.Builder` | `setFrozenAmount(long value)` `int64 frozen_amount = 1;` |
    | `Contract.AssetIssueContract.FrozenSupply.Builder` | `setFrozenDays(long value)` `int64 frozen_days = 2;` |
    | `Contract.AssetIssueContract.FrozenSupply.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.AssetIssueContract.FrozenSupply.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.FrozenSupply.Builder>`
    - #### clear

      ```
      public Contract.AssetIssueContract.FrozenSupply.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.FrozenSupply.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.FrozenSupply.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.AssetIssueContract.FrozenSupply getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.AssetIssueContract.FrozenSupply build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.AssetIssueContract.FrozenSupply buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.AssetIssueContract.FrozenSupply.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.FrozenSupply.Builder>`
    - #### setField

      ```
      public Contract.AssetIssueContract.FrozenSupply.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.FrozenSupply.Builder>`
    - #### clearField

      ```
      public Contract.AssetIssueContract.FrozenSupply.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.FrozenSupply.Builder>`
    - #### clearOneof

      ```
      public Contract.AssetIssueContract.FrozenSupply.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.FrozenSupply.Builder>`
    - #### setRepeatedField

      ```
      public Contract.AssetIssueContract.FrozenSupply.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                               int index,
                                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.FrozenSupply.Builder>`
    - #### addRepeatedField

      ```
      public Contract.AssetIssueContract.FrozenSupply.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                               java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.FrozenSupply.Builder>`
    - #### mergeFrom

      ```
      public Contract.AssetIssueContract.FrozenSupply.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.AssetIssueContract.FrozenSupply.Builder>`
    - #### mergeFrom

      ```
      public Contract.AssetIssueContract.FrozenSupply.Builder mergeFrom(Contract.AssetIssueContract.FrozenSupply other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.FrozenSupply.Builder>`
    - #### mergeFrom

      ```
      public Contract.AssetIssueContract.FrozenSupply.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                 throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.AssetIssueContract.FrozenSupply.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getFrozenAmount

      ```
      public long getFrozenAmount()
      ```

      `int64 frozen_amount = 1;`

      Specified by:
      :   `getFrozenAmount` in interface `Contract.AssetIssueContract.FrozenSupplyOrBuilder`

      Returns:
      :   The frozenAmount.
    - #### setFrozenAmount

      ```
      public Contract.AssetIssueContract.FrozenSupply.Builder setFrozenAmount(long value)
      ```

      `int64 frozen_amount = 1;`

      Parameters:
      :   `value` - The frozenAmount to set.

      Returns:
      :   This builder for chaining.
    - #### clearFrozenAmount

      ```
      public Contract.AssetIssueContract.FrozenSupply.Builder clearFrozenAmount()
      ```

      `int64 frozen_amount = 1;`

      Returns:
      :   This builder for chaining.
    - #### getFrozenDays

      ```
      public long getFrozenDays()
      ```

      `int64 frozen_days = 2;`

      Specified by:
      :   `getFrozenDays` in interface `Contract.AssetIssueContract.FrozenSupplyOrBuilder`

      Returns:
      :   The frozenDays.
    - #### setFrozenDays

      ```
      public Contract.AssetIssueContract.FrozenSupply.Builder setFrozenDays(long value)
      ```

      `int64 frozen_days = 2;`

      Parameters:
      :   `value` - The frozenDays to set.

      Returns:
      :   This builder for chaining.
    - #### clearFrozenDays

      ```
      public Contract.AssetIssueContract.FrozenSupply.Builder clearFrozenDays()
      ```

      `int64 frozen_days = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Contract.AssetIssueContract.FrozenSupply.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.FrozenSupply.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.AssetIssueContract.FrozenSupply.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AssetIssueContract.FrozenSupply.Builder>`