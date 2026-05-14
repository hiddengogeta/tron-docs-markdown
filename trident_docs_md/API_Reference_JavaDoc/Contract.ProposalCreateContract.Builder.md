

org.tron.trident.proto

## Class Contract.ProposalCreateContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.ProposalCreateContract.Builder](../../../../org/tron/trident/proto/Contract.ProposalCreateContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.ProposalCreateContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.ProposalCreateContractOrBuilder](../../../../org/tron/trident/proto/Contract.ProposalCreateContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.ProposalCreateContract](../../../../org/tron/trident/proto/Contract.ProposalCreateContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.ProposalCreateContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalCreateContract.Builder>
  implements Contract.ProposalCreateContractOrBuilder
  ```

  Protobuf type `protocol.ProposalCreateContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `Contract.ProposalCreateContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.ProposalCreateContract` | `build()` |
    | `Contract.ProposalCreateContract` | `buildPartial()` |
    | `Contract.ProposalCreateContract.Builder` | `clear()` |
    | `Contract.ProposalCreateContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.ProposalCreateContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.ProposalCreateContract.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `Contract.ProposalCreateContract.Builder` | `clearParameters()` |
    | `Contract.ProposalCreateContract.Builder` | `clone()` |
    | `boolean` | `containsParameters(long key)` `map<int64, int64> parameters = 2;` |
    | `Contract.ProposalCreateContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `java.util.Map<java.lang.Long,java.lang.Long>` | `getMutableParameters()` Deprecated. |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `java.util.Map<java.lang.Long,java.lang.Long>` | `getParameters()` Deprecated. |
    | `int` | `getParametersCount()` `map<int64, int64> parameters = 2;` |
    | `java.util.Map<java.lang.Long,java.lang.Long>` | `getParametersMap()` `map<int64, int64> parameters = 2;` |
    | `long` | `getParametersOrDefault(long key, long defaultValue)` `map<int64, int64> parameters = 2;` |
    | `long` | `getParametersOrThrow(long key)` `map<int64, int64> parameters = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMapFieldReflection(int number)` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMutableMapFieldReflection(int number)` |
    | `boolean` | `isInitialized()` |
    | `Contract.ProposalCreateContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.ProposalCreateContract.Builder` | `mergeFrom(Contract.ProposalCreateContract other)` |
    | `Contract.ProposalCreateContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.ProposalCreateContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.ProposalCreateContract.Builder` | `putAllParameters(java.util.Map<java.lang.Long,java.lang.Long> values)` `map<int64, int64> parameters = 2;` |
    | `Contract.ProposalCreateContract.Builder` | `putParameters(long key, long value)` `map<int64, int64> parameters = 2;` |
    | `Contract.ProposalCreateContract.Builder` | `removeParameters(long key)` `map<int64, int64> parameters = 2;` |
    | `Contract.ProposalCreateContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.ProposalCreateContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `Contract.ProposalCreateContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.ProposalCreateContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

    - ### Methods inherited from class com.google.protobuf.GeneratedMessageV3.Builder

      `getAllFields, getField, getFieldBuilder, getOneofFieldDescriptor, getParentForChildren, getRepeatedField, getRepeatedFieldBuilder, getRepeatedFieldCount, getUnknownFields, getUnknownFieldSetBuilder, hasField, hasOneof, internalGetMapField, internalGetMutableMapField, isClean, markClean, mergeUnknownLengthDelimitedField, mergeUnknownVarintField, newBuilderForField, onBuilt, onChanged, parseUnknownField, setUnknownFieldSetBuilder, setUnknownFieldsProto3`
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
    - #### internalGetMapFieldReflection

      ```
      protected com.google.protobuf.MapFieldReflectionAccessor internalGetMapFieldReflection(int number)
      ```

      Overrides:
      :   `internalGetMapFieldReflection` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalCreateContract.Builder>`
    - #### internalGetMutableMapFieldReflection

      ```
      protected com.google.protobuf.MapFieldReflectionAccessor internalGetMutableMapFieldReflection(int number)
      ```

      Overrides:
      :   `internalGetMutableMapFieldReflection` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalCreateContract.Builder>`
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalCreateContract.Builder>`
    - #### clear

      ```
      public Contract.ProposalCreateContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalCreateContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalCreateContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.ProposalCreateContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.ProposalCreateContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.ProposalCreateContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.ProposalCreateContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalCreateContract.Builder>`
    - #### setField

      ```
      public Contract.ProposalCreateContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                              java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalCreateContract.Builder>`
    - #### clearField

      ```
      public Contract.ProposalCreateContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalCreateContract.Builder>`
    - #### clearOneof

      ```
      public Contract.ProposalCreateContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalCreateContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.ProposalCreateContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                      int index,
                                                                      java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalCreateContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.ProposalCreateContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                      java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalCreateContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.ProposalCreateContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.ProposalCreateContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.ProposalCreateContract.Builder mergeFrom(Contract.ProposalCreateContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalCreateContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.ProposalCreateContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.ProposalCreateContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.ProposalCreateContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.ProposalCreateContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.ProposalCreateContract.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getParametersCount

      ```
      public int getParametersCount()
      ```

      Description copied from interface: `Contract.ProposalCreateContractOrBuilder`

      `map<int64, int64> parameters = 2;`

      Specified by:
      :   `getParametersCount` in interface `Contract.ProposalCreateContractOrBuilder`
    - #### containsParameters

      ```
      public boolean containsParameters(long key)
      ```

      `map<int64, int64> parameters = 2;`

      Specified by:
      :   `containsParameters` in interface `Contract.ProposalCreateContractOrBuilder`
    - #### getParameters

      ```
      @Deprecated
      public java.util.Map<java.lang.Long,java.lang.Long> getParameters()
      ```

      Deprecated.

      Use [`getParametersMap()`](../../../../org/tron/trident/proto/Contract.ProposalCreateContract.Builder.html#getParametersMap--) instead.

      Specified by:
      :   `getParameters` in interface `Contract.ProposalCreateContractOrBuilder`
    - #### getParametersMap

      ```
      public java.util.Map<java.lang.Long,java.lang.Long> getParametersMap()
      ```

      `map<int64, int64> parameters = 2;`

      Specified by:
      :   `getParametersMap` in interface `Contract.ProposalCreateContractOrBuilder`
    - #### getParametersOrDefault

      ```
      public long getParametersOrDefault(long key,
                                         long defaultValue)
      ```

      `map<int64, int64> parameters = 2;`

      Specified by:
      :   `getParametersOrDefault` in interface `Contract.ProposalCreateContractOrBuilder`
    - #### getParametersOrThrow

      ```
      public long getParametersOrThrow(long key)
      ```

      `map<int64, int64> parameters = 2;`

      Specified by:
      :   `getParametersOrThrow` in interface `Contract.ProposalCreateContractOrBuilder`
    - #### clearParameters

      ```
      public Contract.ProposalCreateContract.Builder clearParameters()
      ```
    - #### removeParameters

      ```
      public Contract.ProposalCreateContract.Builder removeParameters(long key)
      ```

      `map<int64, int64> parameters = 2;`
    - #### getMutableParameters

      ```
      @Deprecated
      public java.util.Map<java.lang.Long,java.lang.Long> getMutableParameters()
      ```

      Deprecated.

      Use alternate mutation accessors instead.
    - #### putParameters

      ```
      public Contract.ProposalCreateContract.Builder putParameters(long key,
                                                                   long value)
      ```

      `map<int64, int64> parameters = 2;`
    - #### putAllParameters

      ```
      public Contract.ProposalCreateContract.Builder putAllParameters(java.util.Map<java.lang.Long,java.lang.Long> values)
      ```

      `map<int64, int64> parameters = 2;`
    - #### setUnknownFields

      ```
      public final Contract.ProposalCreateContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalCreateContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.ProposalCreateContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.ProposalCreateContract.Builder>`