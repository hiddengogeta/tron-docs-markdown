

org.tron.trident.proto

## Class Chain.Transaction.Contract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Chain.Transaction.Contract.Builder](../../../../org/tron/trident/proto/Chain.Transaction.Contract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Chain.Transaction.Contract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Chain.Transaction.ContractOrBuilder](../../../../org/tron/trident/proto/Chain.Transaction.ContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Chain.Transaction.Contract](../../../../org/tron/trident/proto/Chain.Transaction.Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Chain.Transaction.Contract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Contract.Builder>
  implements Chain.Transaction.ContractOrBuilder
  ```

  Protobuf type `protocol.Transaction.Contract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Chain.Transaction.Contract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Chain.Transaction.Contract` | `build()` |
    | `Chain.Transaction.Contract` | `buildPartial()` |
    | `Chain.Transaction.Contract.Builder` | `clear()` |
    | `Chain.Transaction.Contract.Builder` | `clearContractName()` `bytes ContractName = 4;` |
    | `Chain.Transaction.Contract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Chain.Transaction.Contract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Chain.Transaction.Contract.Builder` | `clearParameter()` `.google.protobuf.Any parameter = 2;` |
    | `Chain.Transaction.Contract.Builder` | `clearPermissionId()` `int32 Permission_id = 5;` |
    | `Chain.Transaction.Contract.Builder` | `clearProvider()` `bytes provider = 3;` |
    | `Chain.Transaction.Contract.Builder` | `clearType()` `.protocol.Transaction.Contract.ContractType type = 1;` |
    | `Chain.Transaction.Contract.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getContractName()` `bytes ContractName = 4;` |
    | `Chain.Transaction.Contract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.Any` | `getParameter()` `.google.protobuf.Any parameter = 2;` |
    | `com.google.protobuf.Any.Builder` | `getParameterBuilder()` `.google.protobuf.Any parameter = 2;` |
    | `com.google.protobuf.AnyOrBuilder` | `getParameterOrBuilder()` `.google.protobuf.Any parameter = 2;` |
    | `int` | `getPermissionId()` `int32 Permission_id = 5;` |
    | `com.google.protobuf.ByteString` | `getProvider()` `bytes provider = 3;` |
    | `Chain.Transaction.Contract.ContractType` | `getType()` `.protocol.Transaction.Contract.ContractType type = 1;` |
    | `int` | `getTypeValue()` `.protocol.Transaction.Contract.ContractType type = 1;` |
    | `boolean` | `hasParameter()` `.google.protobuf.Any parameter = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Chain.Transaction.Contract.Builder` | `mergeFrom(Chain.Transaction.Contract other)` |
    | `Chain.Transaction.Contract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Chain.Transaction.Contract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Chain.Transaction.Contract.Builder` | `mergeParameter(com.google.protobuf.Any value)` `.google.protobuf.Any parameter = 2;` |
    | `Chain.Transaction.Contract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Chain.Transaction.Contract.Builder` | `setContractName(com.google.protobuf.ByteString value)` `bytes ContractName = 4;` |
    | `Chain.Transaction.Contract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Chain.Transaction.Contract.Builder` | `setParameter(com.google.protobuf.Any.Builder builderForValue)` `.google.protobuf.Any parameter = 2;` |
    | `Chain.Transaction.Contract.Builder` | `setParameter(com.google.protobuf.Any value)` `.google.protobuf.Any parameter = 2;` |
    | `Chain.Transaction.Contract.Builder` | `setPermissionId(int value)` `int32 Permission_id = 5;` |
    | `Chain.Transaction.Contract.Builder` | `setProvider(com.google.protobuf.ByteString value)` `bytes provider = 3;` |
    | `Chain.Transaction.Contract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Chain.Transaction.Contract.Builder` | `setType(Chain.Transaction.Contract.ContractType value)` `.protocol.Transaction.Contract.ContractType type = 1;` |
    | `Chain.Transaction.Contract.Builder` | `setTypeValue(int value)` `.protocol.Transaction.Contract.ContractType type = 1;` |
    | `Chain.Transaction.Contract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Contract.Builder>`
    - #### clear

      ```
      public Chain.Transaction.Contract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Contract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Contract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Chain.Transaction.Contract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Chain.Transaction.Contract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Chain.Transaction.Contract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Chain.Transaction.Contract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Contract.Builder>`
    - #### setField

      ```
      public Chain.Transaction.Contract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                         java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Contract.Builder>`
    - #### clearField

      ```
      public Chain.Transaction.Contract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Contract.Builder>`
    - #### clearOneof

      ```
      public Chain.Transaction.Contract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Contract.Builder>`
    - #### setRepeatedField

      ```
      public Chain.Transaction.Contract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                 int index,
                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Contract.Builder>`
    - #### addRepeatedField

      ```
      public Chain.Transaction.Contract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Contract.Builder>`
    - #### mergeFrom

      ```
      public Chain.Transaction.Contract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Chain.Transaction.Contract.Builder>`
    - #### mergeFrom

      ```
      public Chain.Transaction.Contract.Builder mergeFrom(Chain.Transaction.Contract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Contract.Builder>`
    - #### mergeFrom

      ```
      public Chain.Transaction.Contract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Chain.Transaction.Contract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getTypeValue

      ```
      public int getTypeValue()
      ```

      `.protocol.Transaction.Contract.ContractType type = 1;`

      Specified by:
      :   `getTypeValue` in interface `Chain.Transaction.ContractOrBuilder`

      Returns:
      :   The enum numeric value on the wire for type.
    - #### setTypeValue

      ```
      public Chain.Transaction.Contract.Builder setTypeValue(int value)
      ```

      `.protocol.Transaction.Contract.ContractType type = 1;`

      Parameters:
      :   `value` - The enum numeric value on the wire for type to set.

      Returns:
      :   This builder for chaining.
    - #### getType

      ```
      public Chain.Transaction.Contract.ContractType getType()
      ```

      `.protocol.Transaction.Contract.ContractType type = 1;`

      Specified by:
      :   `getType` in interface `Chain.Transaction.ContractOrBuilder`

      Returns:
      :   The type.
    - #### setType

      ```
      public Chain.Transaction.Contract.Builder setType(Chain.Transaction.Contract.ContractType value)
      ```

      `.protocol.Transaction.Contract.ContractType type = 1;`

      Parameters:
      :   `value` - The type to set.

      Returns:
      :   This builder for chaining.
    - #### clearType

      ```
      public Chain.Transaction.Contract.Builder clearType()
      ```

      `.protocol.Transaction.Contract.ContractType type = 1;`

      Returns:
      :   This builder for chaining.
    - #### hasParameter

      ```
      public boolean hasParameter()
      ```

      `.google.protobuf.Any parameter = 2;`

      Specified by:
      :   `hasParameter` in interface `Chain.Transaction.ContractOrBuilder`

      Returns:
      :   Whether the parameter field is set.
    - #### getParameter

      ```
      public com.google.protobuf.Any getParameter()
      ```

      `.google.protobuf.Any parameter = 2;`

      Specified by:
      :   `getParameter` in interface `Chain.Transaction.ContractOrBuilder`

      Returns:
      :   The parameter.
    - #### setParameter

      ```
      public Chain.Transaction.Contract.Builder setParameter(com.google.protobuf.Any value)
      ```

      `.google.protobuf.Any parameter = 2;`
    - #### setParameter

      ```
      public Chain.Transaction.Contract.Builder setParameter(com.google.protobuf.Any.Builder builderForValue)
      ```

      `.google.protobuf.Any parameter = 2;`
    - #### mergeParameter

      ```
      public Chain.Transaction.Contract.Builder mergeParameter(com.google.protobuf.Any value)
      ```

      `.google.protobuf.Any parameter = 2;`
    - #### clearParameter

      ```
      public Chain.Transaction.Contract.Builder clearParameter()
      ```

      `.google.protobuf.Any parameter = 2;`
    - #### getParameterBuilder

      ```
      public com.google.protobuf.Any.Builder getParameterBuilder()
      ```

      `.google.protobuf.Any parameter = 2;`
    - #### getParameterOrBuilder

      ```
      public com.google.protobuf.AnyOrBuilder getParameterOrBuilder()
      ```

      `.google.protobuf.Any parameter = 2;`

      Specified by:
      :   `getParameterOrBuilder` in interface `Chain.Transaction.ContractOrBuilder`
    - #### getProvider

      ```
      public com.google.protobuf.ByteString getProvider()
      ```

      `bytes provider = 3;`

      Specified by:
      :   `getProvider` in interface `Chain.Transaction.ContractOrBuilder`

      Returns:
      :   The provider.
    - #### setProvider

      ```
      public Chain.Transaction.Contract.Builder setProvider(com.google.protobuf.ByteString value)
      ```

      `bytes provider = 3;`

      Parameters:
      :   `value` - The provider to set.

      Returns:
      :   This builder for chaining.
    - #### clearProvider

      ```
      public Chain.Transaction.Contract.Builder clearProvider()
      ```

      `bytes provider = 3;`

      Returns:
      :   This builder for chaining.
    - #### getContractName

      ```
      public com.google.protobuf.ByteString getContractName()
      ```

      `bytes ContractName = 4;`

      Specified by:
      :   `getContractName` in interface `Chain.Transaction.ContractOrBuilder`

      Returns:
      :   The contractName.
    - #### setContractName

      ```
      public Chain.Transaction.Contract.Builder setContractName(com.google.protobuf.ByteString value)
      ```

      `bytes ContractName = 4;`

      Parameters:
      :   `value` - The contractName to set.

      Returns:
      :   This builder for chaining.
    - #### clearContractName

      ```
      public Chain.Transaction.Contract.Builder clearContractName()
      ```

      `bytes ContractName = 4;`

      Returns:
      :   This builder for chaining.
    - #### getPermissionId

      ```
      public int getPermissionId()
      ```

      `int32 Permission_id = 5;`

      Specified by:
      :   `getPermissionId` in interface `Chain.Transaction.ContractOrBuilder`

      Returns:
      :   The permissionId.
    - #### setPermissionId

      ```
      public Chain.Transaction.Contract.Builder setPermissionId(int value)
      ```

      `int32 Permission_id = 5;`

      Parameters:
      :   `value` - The permissionId to set.

      Returns:
      :   This builder for chaining.
    - #### clearPermissionId

      ```
      public Chain.Transaction.Contract.Builder clearPermissionId()
      ```

      `int32 Permission_id = 5;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Chain.Transaction.Contract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Contract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Chain.Transaction.Contract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Contract.Builder>`