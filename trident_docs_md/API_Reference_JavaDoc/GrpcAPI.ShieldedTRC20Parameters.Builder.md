

org.tron.trident.api

## Class GrpcAPI.ShieldedTRC20Parameters.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.ShieldedTRC20Parameters.Builder](../../../../org/tron/trident/api/GrpcAPI.ShieldedTRC20Parameters.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.ShieldedTRC20Parameters.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.ShieldedTRC20ParametersOrBuilder](../../../../org/tron/trident/api/GrpcAPI.ShieldedTRC20ParametersOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.ShieldedTRC20Parameters](../../../../org/tron/trident/api/GrpcAPI.ShieldedTRC20Parameters.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.ShieldedTRC20Parameters.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20Parameters.Builder>
  implements GrpcAPI.ShieldedTRC20ParametersOrBuilder
  ```

  Protobuf type `protocol.ShieldedTRC20Parameters`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `addAllReceiveDescription(java.lang.Iterable<? extends GrpcAPI.ReceiveDescription> values)` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `addAllSpendDescription(java.lang.Iterable<? extends GrpcAPI.SpendDescription> values)` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `addReceiveDescription(GrpcAPI.ReceiveDescription.Builder builderForValue)` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `addReceiveDescription(GrpcAPI.ReceiveDescription value)` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `addReceiveDescription(int index, GrpcAPI.ReceiveDescription.Builder builderForValue)` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `addReceiveDescription(int index, GrpcAPI.ReceiveDescription value)` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `GrpcAPI.ReceiveDescription.Builder` | `addReceiveDescriptionBuilder()` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `GrpcAPI.ReceiveDescription.Builder` | `addReceiveDescriptionBuilder(int index)` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `addSpendDescription(GrpcAPI.SpendDescription.Builder builderForValue)` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `addSpendDescription(GrpcAPI.SpendDescription value)` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `addSpendDescription(int index, GrpcAPI.SpendDescription.Builder builderForValue)` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `addSpendDescription(int index, GrpcAPI.SpendDescription value)` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `GrpcAPI.SpendDescription.Builder` | `addSpendDescriptionBuilder()` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `GrpcAPI.SpendDescription.Builder` | `addSpendDescriptionBuilder(int index)` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `GrpcAPI.ShieldedTRC20Parameters` | `build()` |
    | `GrpcAPI.ShieldedTRC20Parameters` | `buildPartial()` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `clear()` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `clearBindingSignature()` `bytes binding_signature = 3;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `clearMessageHash()` `bytes message_hash = 4;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `clearParameterType()` `string parameter_type = 6;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `clearReceiveDescription()` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `clearSpendDescription()` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `clearTriggerContractInput()` `string trigger_contract_input = 5;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getBindingSignature()` `bytes binding_signature = 3;` |
    | `GrpcAPI.ShieldedTRC20Parameters` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getMessageHash()` `bytes message_hash = 4;` |
    | `java.lang.String` | `getParameterType()` `string parameter_type = 6;` |
    | `com.google.protobuf.ByteString` | `getParameterTypeBytes()` `string parameter_type = 6;` |
    | `GrpcAPI.ReceiveDescription` | `getReceiveDescription(int index)` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `GrpcAPI.ReceiveDescription.Builder` | `getReceiveDescriptionBuilder(int index)` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `java.util.List<GrpcAPI.ReceiveDescription.Builder>` | `getReceiveDescriptionBuilderList()` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `int` | `getReceiveDescriptionCount()` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `java.util.List<GrpcAPI.ReceiveDescription>` | `getReceiveDescriptionList()` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `GrpcAPI.ReceiveDescriptionOrBuilder` | `getReceiveDescriptionOrBuilder(int index)` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `java.util.List<? extends GrpcAPI.ReceiveDescriptionOrBuilder>` | `getReceiveDescriptionOrBuilderList()` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `GrpcAPI.SpendDescription` | `getSpendDescription(int index)` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `GrpcAPI.SpendDescription.Builder` | `getSpendDescriptionBuilder(int index)` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `java.util.List<GrpcAPI.SpendDescription.Builder>` | `getSpendDescriptionBuilderList()` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `int` | `getSpendDescriptionCount()` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `java.util.List<GrpcAPI.SpendDescription>` | `getSpendDescriptionList()` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `GrpcAPI.SpendDescriptionOrBuilder` | `getSpendDescriptionOrBuilder(int index)` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `java.util.List<? extends GrpcAPI.SpendDescriptionOrBuilder>` | `getSpendDescriptionOrBuilderList()` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `java.lang.String` | `getTriggerContractInput()` `string trigger_contract_input = 5;` |
    | `com.google.protobuf.ByteString` | `getTriggerContractInputBytes()` `string trigger_contract_input = 5;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `mergeFrom(GrpcAPI.ShieldedTRC20Parameters other)` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `removeReceiveDescription(int index)` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `removeSpendDescription(int index)` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `setBindingSignature(com.google.protobuf.ByteString value)` `bytes binding_signature = 3;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `setMessageHash(com.google.protobuf.ByteString value)` `bytes message_hash = 4;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `setParameterType(java.lang.String value)` `string parameter_type = 6;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `setParameterTypeBytes(com.google.protobuf.ByteString value)` `string parameter_type = 6;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `setReceiveDescription(int index, GrpcAPI.ReceiveDescription.Builder builderForValue)` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `setReceiveDescription(int index, GrpcAPI.ReceiveDescription value)` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `setSpendDescription(int index, GrpcAPI.SpendDescription.Builder builderForValue)` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `setSpendDescription(int index, GrpcAPI.SpendDescription value)` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `setTriggerContractInput(java.lang.String value)` `string trigger_contract_input = 5;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `setTriggerContractInputBytes(com.google.protobuf.ByteString value)` `string trigger_contract_input = 5;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20Parameters.Builder>`
    - #### clear

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20Parameters.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20Parameters.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.ShieldedTRC20Parameters getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.ShieldedTRC20Parameters build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.ShieldedTRC20Parameters buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20Parameters.Builder>`
    - #### setField

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                              java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20Parameters.Builder>`
    - #### clearField

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20Parameters.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20Parameters.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                      int index,
                                                                      java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20Parameters.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                      java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20Parameters.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.ShieldedTRC20Parameters.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder mergeFrom(GrpcAPI.ShieldedTRC20Parameters other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20Parameters.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.ShieldedTRC20Parameters.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getSpendDescriptionList

      ```
      public java.util.List<GrpcAPI.SpendDescription> getSpendDescriptionList()
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`

      Specified by:
      :   `getSpendDescriptionList` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`
    - #### getSpendDescriptionCount

      ```
      public int getSpendDescriptionCount()
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`

      Specified by:
      :   `getSpendDescriptionCount` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`
    - #### getSpendDescription

      ```
      public GrpcAPI.SpendDescription getSpendDescription(int index)
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`

      Specified by:
      :   `getSpendDescription` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`
    - #### setSpendDescription

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder setSpendDescription(int index,
                                                                         GrpcAPI.SpendDescription value)
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`
    - #### setSpendDescription

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder setSpendDescription(int index,
                                                                         GrpcAPI.SpendDescription.Builder builderForValue)
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`
    - #### addSpendDescription

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder addSpendDescription(GrpcAPI.SpendDescription value)
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`
    - #### addSpendDescription

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder addSpendDescription(int index,
                                                                         GrpcAPI.SpendDescription value)
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`
    - #### addSpendDescription

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder addSpendDescription(GrpcAPI.SpendDescription.Builder builderForValue)
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`
    - #### addSpendDescription

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder addSpendDescription(int index,
                                                                         GrpcAPI.SpendDescription.Builder builderForValue)
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`
    - #### addAllSpendDescription

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder addAllSpendDescription(java.lang.Iterable<? extends GrpcAPI.SpendDescription> values)
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`
    - #### clearSpendDescription

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder clearSpendDescription()
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`
    - #### removeSpendDescription

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder removeSpendDescription(int index)
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`
    - #### getSpendDescriptionBuilder

      ```
      public GrpcAPI.SpendDescription.Builder getSpendDescriptionBuilder(int index)
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`
    - #### getSpendDescriptionOrBuilder

      ```
      public GrpcAPI.SpendDescriptionOrBuilder getSpendDescriptionOrBuilder(int index)
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`

      Specified by:
      :   `getSpendDescriptionOrBuilder` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`
    - #### getSpendDescriptionOrBuilderList

      ```
      public java.util.List<? extends GrpcAPI.SpendDescriptionOrBuilder> getSpendDescriptionOrBuilderList()
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`

      Specified by:
      :   `getSpendDescriptionOrBuilderList` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`
    - #### addSpendDescriptionBuilder

      ```
      public GrpcAPI.SpendDescription.Builder addSpendDescriptionBuilder()
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`
    - #### addSpendDescriptionBuilder

      ```
      public GrpcAPI.SpendDescription.Builder addSpendDescriptionBuilder(int index)
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`
    - #### getSpendDescriptionBuilderList

      ```
      public java.util.List<GrpcAPI.SpendDescription.Builder> getSpendDescriptionBuilderList()
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`
    - #### getReceiveDescriptionList

      ```
      public java.util.List<GrpcAPI.ReceiveDescription> getReceiveDescriptionList()
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`

      Specified by:
      :   `getReceiveDescriptionList` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`
    - #### getReceiveDescriptionCount

      ```
      public int getReceiveDescriptionCount()
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`

      Specified by:
      :   `getReceiveDescriptionCount` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`
    - #### getReceiveDescription

      ```
      public GrpcAPI.ReceiveDescription getReceiveDescription(int index)
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`

      Specified by:
      :   `getReceiveDescription` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`
    - #### setReceiveDescription

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder setReceiveDescription(int index,
                                                                           GrpcAPI.ReceiveDescription value)
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`
    - #### setReceiveDescription

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder setReceiveDescription(int index,
                                                                           GrpcAPI.ReceiveDescription.Builder builderForValue)
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`
    - #### addReceiveDescription

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder addReceiveDescription(GrpcAPI.ReceiveDescription value)
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`
    - #### addReceiveDescription

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder addReceiveDescription(int index,
                                                                           GrpcAPI.ReceiveDescription value)
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`
    - #### addReceiveDescription

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder addReceiveDescription(GrpcAPI.ReceiveDescription.Builder builderForValue)
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`
    - #### addReceiveDescription

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder addReceiveDescription(int index,
                                                                           GrpcAPI.ReceiveDescription.Builder builderForValue)
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`
    - #### addAllReceiveDescription

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder addAllReceiveDescription(java.lang.Iterable<? extends GrpcAPI.ReceiveDescription> values)
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`
    - #### clearReceiveDescription

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder clearReceiveDescription()
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`
    - #### removeReceiveDescription

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder removeReceiveDescription(int index)
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`
    - #### getReceiveDescriptionBuilder

      ```
      public GrpcAPI.ReceiveDescription.Builder getReceiveDescriptionBuilder(int index)
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`
    - #### getReceiveDescriptionOrBuilder

      ```
      public GrpcAPI.ReceiveDescriptionOrBuilder getReceiveDescriptionOrBuilder(int index)
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`

      Specified by:
      :   `getReceiveDescriptionOrBuilder` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`
    - #### getReceiveDescriptionOrBuilderList

      ```
      public java.util.List<? extends GrpcAPI.ReceiveDescriptionOrBuilder> getReceiveDescriptionOrBuilderList()
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`

      Specified by:
      :   `getReceiveDescriptionOrBuilderList` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`
    - #### addReceiveDescriptionBuilder

      ```
      public GrpcAPI.ReceiveDescription.Builder addReceiveDescriptionBuilder()
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`
    - #### addReceiveDescriptionBuilder

      ```
      public GrpcAPI.ReceiveDescription.Builder addReceiveDescriptionBuilder(int index)
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`
    - #### getReceiveDescriptionBuilderList

      ```
      public java.util.List<GrpcAPI.ReceiveDescription.Builder> getReceiveDescriptionBuilderList()
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`
    - #### getBindingSignature

      ```
      public com.google.protobuf.ByteString getBindingSignature()
      ```

      `bytes binding_signature = 3;`

      Specified by:
      :   `getBindingSignature` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The bindingSignature.
    - #### setBindingSignature

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder setBindingSignature(com.google.protobuf.ByteString value)
      ```

      `bytes binding_signature = 3;`

      Parameters:
      :   `value` - The bindingSignature to set.

      Returns:
      :   This builder for chaining.
    - #### clearBindingSignature

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder clearBindingSignature()
      ```

      `bytes binding_signature = 3;`

      Returns:
      :   This builder for chaining.
    - #### getMessageHash

      ```
      public com.google.protobuf.ByteString getMessageHash()
      ```

      `bytes message_hash = 4;`

      Specified by:
      :   `getMessageHash` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The messageHash.
    - #### setMessageHash

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder setMessageHash(com.google.protobuf.ByteString value)
      ```

      `bytes message_hash = 4;`

      Parameters:
      :   `value` - The messageHash to set.

      Returns:
      :   This builder for chaining.
    - #### clearMessageHash

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder clearMessageHash()
      ```

      `bytes message_hash = 4;`

      Returns:
      :   This builder for chaining.
    - #### getTriggerContractInput

      ```
      public java.lang.String getTriggerContractInput()
      ```

      `string trigger_contract_input = 5;`

      Specified by:
      :   `getTriggerContractInput` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The triggerContractInput.
    - #### getTriggerContractInputBytes

      ```
      public com.google.protobuf.ByteString getTriggerContractInputBytes()
      ```

      `string trigger_contract_input = 5;`

      Specified by:
      :   `getTriggerContractInputBytes` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The bytes for triggerContractInput.
    - #### setTriggerContractInput

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder setTriggerContractInput(java.lang.String value)
      ```

      `string trigger_contract_input = 5;`

      Parameters:
      :   `value` - The triggerContractInput to set.

      Returns:
      :   This builder for chaining.
    - #### clearTriggerContractInput

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder clearTriggerContractInput()
      ```

      `string trigger_contract_input = 5;`

      Returns:
      :   This builder for chaining.
    - #### setTriggerContractInputBytes

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder setTriggerContractInputBytes(com.google.protobuf.ByteString value)
      ```

      `string trigger_contract_input = 5;`

      Parameters:
      :   `value` - The bytes for triggerContractInput to set.

      Returns:
      :   This builder for chaining.
    - #### getParameterType

      ```
      public java.lang.String getParameterType()
      ```

      `string parameter_type = 6;`

      Specified by:
      :   `getParameterType` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The parameterType.
    - #### getParameterTypeBytes

      ```
      public com.google.protobuf.ByteString getParameterTypeBytes()
      ```

      `string parameter_type = 6;`

      Specified by:
      :   `getParameterTypeBytes` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The bytes for parameterType.
    - #### setParameterType

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder setParameterType(java.lang.String value)
      ```

      `string parameter_type = 6;`

      Parameters:
      :   `value` - The parameterType to set.

      Returns:
      :   This builder for chaining.
    - #### clearParameterType

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder clearParameterType()
      ```

      `string parameter_type = 6;`

      Returns:
      :   This builder for chaining.
    - #### setParameterTypeBytes

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder setParameterTypeBytes(com.google.protobuf.ByteString value)
      ```

      `string parameter_type = 6;`

      Parameters:
      :   `value` - The bytes for parameterType to set.

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.ShieldedTRC20Parameters.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20Parameters.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.ShieldedTRC20Parameters.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20Parameters.Builder>`