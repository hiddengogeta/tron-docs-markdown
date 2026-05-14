

org.tron.trident.api

## Class GrpcAPI.ShieldedTRC20Parameters

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.api.GrpcAPI.ShieldedTRC20Parameters

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [GrpcAPI.ShieldedTRC20ParametersOrBuilder](../../../../org/tron/trident/api/GrpcAPI.ShieldedTRC20ParametersOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.ShieldedTRC20Parameters
  extends com.google.protobuf.GeneratedMessageV3
  implements GrpcAPI.ShieldedTRC20ParametersOrBuilder
  ```

  Protobuf type `protocol.ShieldedTRC20Parameters`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.api.GrpcAPI.ShieldedTRC20Parameters)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `GrpcAPI.ShieldedTRC20Parameters.Builder` Protobuf type `protocol.ShieldedTRC20Parameters` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `BINDING_SIGNATURE_FIELD_NUMBER` |
    | `static int` | `MESSAGE_HASH_FIELD_NUMBER` |
    | `static int` | `PARAMETER_TYPE_FIELD_NUMBER` |
    | `static int` | `RECEIVE_DESCRIPTION_FIELD_NUMBER` |
    | `static int` | `SPEND_DESCRIPTION_FIELD_NUMBER` |
    | `static int` | `TRIGGER_CONTRACT_INPUT_FIELD_NUMBER` |

    - ### Fields inherited from class com.google.protobuf.GeneratedMessageV3

      `alwaysUseFieldBuilders, unknownFields`
    - ### Fields inherited from class com.google.protobuf.AbstractMessage

      `memoizedSize`
    - ### Fields inherited from class com.google.protobuf.AbstractMessageLite

      `memoizedHashCode`
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `boolean` | `equals(java.lang.Object obj)` |
    | `com.google.protobuf.ByteString` | `getBindingSignature()` `bytes binding_signature = 3;` |
    | `static GrpcAPI.ShieldedTRC20Parameters` | `getDefaultInstance()` |
    | `GrpcAPI.ShieldedTRC20Parameters` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.ByteString` | `getMessageHash()` `bytes message_hash = 4;` |
    | `java.lang.String` | `getParameterType()` `string parameter_type = 6;` |
    | `com.google.protobuf.ByteString` | `getParameterTypeBytes()` `string parameter_type = 6;` |
    | `com.google.protobuf.Parser<GrpcAPI.ShieldedTRC20Parameters>` | `getParserForType()` |
    | `GrpcAPI.ReceiveDescription` | `getReceiveDescription(int index)` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `int` | `getReceiveDescriptionCount()` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `java.util.List<GrpcAPI.ReceiveDescription>` | `getReceiveDescriptionList()` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `GrpcAPI.ReceiveDescriptionOrBuilder` | `getReceiveDescriptionOrBuilder(int index)` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `java.util.List<? extends GrpcAPI.ReceiveDescriptionOrBuilder>` | `getReceiveDescriptionOrBuilderList()` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `int` | `getSerializedSize()` |
    | `GrpcAPI.SpendDescription` | `getSpendDescription(int index)` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `int` | `getSpendDescriptionCount()` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `java.util.List<GrpcAPI.SpendDescription>` | `getSpendDescriptionList()` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `GrpcAPI.SpendDescriptionOrBuilder` | `getSpendDescriptionOrBuilder(int index)` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `java.util.List<? extends GrpcAPI.SpendDescriptionOrBuilder>` | `getSpendDescriptionOrBuilderList()` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `java.lang.String` | `getTriggerContractInput()` `string trigger_contract_input = 5;` |
    | `com.google.protobuf.ByteString` | `getTriggerContractInputBytes()` `string trigger_contract_input = 5;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static GrpcAPI.ShieldedTRC20Parameters.Builder` | `newBuilder()` |
    | `static GrpcAPI.ShieldedTRC20Parameters.Builder` | `newBuilder(GrpcAPI.ShieldedTRC20Parameters prototype)` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `newBuilderForType()` |
    | `protected GrpcAPI.ShieldedTRC20Parameters.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static GrpcAPI.ShieldedTRC20Parameters` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static GrpcAPI.ShieldedTRC20Parameters` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.ShieldedTRC20Parameters` | `parseFrom(byte[] data)` |
    | `static GrpcAPI.ShieldedTRC20Parameters` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.ShieldedTRC20Parameters` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static GrpcAPI.ShieldedTRC20Parameters` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.ShieldedTRC20Parameters` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static GrpcAPI.ShieldedTRC20Parameters` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.ShieldedTRC20Parameters` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static GrpcAPI.ShieldedTRC20Parameters` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.ShieldedTRC20Parameters` | `parseFrom(java.io.InputStream input)` |
    | `static GrpcAPI.ShieldedTRC20Parameters` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<GrpcAPI.ShieldedTRC20Parameters>` | `parser()` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `toBuilder()` |
    | `void` | `writeTo(com.google.protobuf.CodedOutputStream output)` |

    - ### Methods inherited from class com.google.protobuf.GeneratedMessageV3

      `canUseUnsafe, computeStringSize, computeStringSizeNoTag, emptyBooleanList, emptyDoubleList, emptyFloatList, emptyIntList, emptyList, emptyLongList, getAllFields, getDescriptorForType, getField, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof, internalGetMapField, internalGetMapFieldReflection, isStringEmpty, makeExtensionsImmutable, makeMutableCopy, makeMutableCopy, mergeFromAndMakeImmutableInternal, mutableCopy, mutableCopy, mutableCopy, mutableCopy, mutableCopy, newBooleanList, newBuilderForType, newDoubleList, newFloatList, newIntList, newLongList, parseDelimitedWithIOException, parseDelimitedWithIOException, parseUnknownField, parseUnknownFieldProto3, parseWithIOException, parseWithIOException, parseWithIOException, parseWithIOException, serializeBooleanMapTo, serializeIntegerMapTo, serializeLongMapTo, serializeStringMapTo, writeReplace, writeString, writeStringNoTag`
    - ### Methods inherited from class com.google.protobuf.AbstractMessage

      `findInitializationErrors, getInitializationErrorString, hashBoolean, hashEnum, hashEnumList, hashFields, hashLong, toString`
    - ### Methods inherited from class com.google.protobuf.AbstractMessageLite

      `addAll, addAll, checkByteStringIsUtf8, toByteArray, toByteString, writeDelimitedTo, writeTo`
    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, wait, wait, wait`
    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLite

      `toByteArray, toByteString, writeDelimitedTo, writeTo`

* + ### Field Detail

    - #### SPEND\_DESCRIPTION\_FIELD\_NUMBER

      ```
      public static final int SPEND_DESCRIPTION_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ShieldedTRC20Parameters.SPEND_DESCRIPTION_FIELD_NUMBER)
    - #### RECEIVE\_DESCRIPTION\_FIELD\_NUMBER

      ```
      public static final int RECEIVE_DESCRIPTION_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ShieldedTRC20Parameters.RECEIVE_DESCRIPTION_FIELD_NUMBER)
    - #### BINDING\_SIGNATURE\_FIELD\_NUMBER

      ```
      public static final int BINDING_SIGNATURE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ShieldedTRC20Parameters.BINDING_SIGNATURE_FIELD_NUMBER)
    - #### MESSAGE\_HASH\_FIELD\_NUMBER

      ```
      public static final int MESSAGE_HASH_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ShieldedTRC20Parameters.MESSAGE_HASH_FIELD_NUMBER)
    - #### TRIGGER\_CONTRACT\_INPUT\_FIELD\_NUMBER

      ```
      public static final int TRIGGER_CONTRACT_INPUT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ShieldedTRC20Parameters.TRIGGER_CONTRACT_INPUT_FIELD_NUMBER)
    - #### PARAMETER\_TYPE\_FIELD\_NUMBER

      ```
      public static final int PARAMETER_TYPE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ShieldedTRC20Parameters.PARAMETER_TYPE_FIELD_NUMBER)
  + ### Method Detail

    - #### newInstance

      ```
      protected java.lang.Object newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)
      ```

      Overrides:
      :   `newInstance` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDescriptor

      ```
      public static final com.google.protobuf.Descriptors.Descriptor getDescriptor()
      ```
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getSpendDescriptionList

      ```
      public java.util.List<GrpcAPI.SpendDescription> getSpendDescriptionList()
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`

      Specified by:
      :   `getSpendDescriptionList` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`
    - #### getSpendDescriptionOrBuilderList

      ```
      public java.util.List<? extends GrpcAPI.SpendDescriptionOrBuilder> getSpendDescriptionOrBuilderList()
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`

      Specified by:
      :   `getSpendDescriptionOrBuilderList` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`
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
    - #### getSpendDescriptionOrBuilder

      ```
      public GrpcAPI.SpendDescriptionOrBuilder getSpendDescriptionOrBuilder(int index)
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`

      Specified by:
      :   `getSpendDescriptionOrBuilder` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`
    - #### getReceiveDescriptionList

      ```
      public java.util.List<GrpcAPI.ReceiveDescription> getReceiveDescriptionList()
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`

      Specified by:
      :   `getReceiveDescriptionList` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`
    - #### getReceiveDescriptionOrBuilderList

      ```
      public java.util.List<? extends GrpcAPI.ReceiveDescriptionOrBuilder> getReceiveDescriptionOrBuilderList()
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`

      Specified by:
      :   `getReceiveDescriptionOrBuilderList` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`
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
    - #### getReceiveDescriptionOrBuilder

      ```
      public GrpcAPI.ReceiveDescriptionOrBuilder getReceiveDescriptionOrBuilder(int index)
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`

      Specified by:
      :   `getReceiveDescriptionOrBuilder` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`
    - #### getBindingSignature

      ```
      public com.google.protobuf.ByteString getBindingSignature()
      ```

      `bytes binding_signature = 3;`

      Specified by:
      :   `getBindingSignature` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The bindingSignature.
    - #### getMessageHash

      ```
      public com.google.protobuf.ByteString getMessageHash()
      ```

      `bytes message_hash = 4;`

      Specified by:
      :   `getMessageHash` in interface `GrpcAPI.ShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The messageHash.
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
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3`
    - #### writeTo

      ```
      public void writeTo(com.google.protobuf.CodedOutputStream output)
                   throws java.io.IOException
      ```

      Specified by:
      :   `writeTo` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `writeTo` in class `com.google.protobuf.GeneratedMessageV3`

      Throws:
      :   `java.io.IOException`
    - #### getSerializedSize

      ```
      public int getSerializedSize()
      ```

      Specified by:
      :   `getSerializedSize` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getSerializedSize` in class `com.google.protobuf.GeneratedMessageV3`
    - #### equals

      ```
      public boolean equals(java.lang.Object obj)
      ```

      Specified by:
      :   `equals` in interface `com.google.protobuf.Message`

      Overrides:
      :   `equals` in class `com.google.protobuf.AbstractMessage`
    - #### hashCode

      ```
      public int hashCode()
      ```

      Specified by:
      :   `hashCode` in interface `com.google.protobuf.Message`

      Overrides:
      :   `hashCode` in class `com.google.protobuf.AbstractMessage`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedTRC20Parameters parseFrom(java.nio.ByteBuffer data)
                                                       throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedTRC20Parameters parseFrom(java.nio.ByteBuffer data,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedTRC20Parameters parseFrom(com.google.protobuf.ByteString data)
                                                       throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedTRC20Parameters parseFrom(com.google.protobuf.ByteString data,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedTRC20Parameters parseFrom(byte[] data)
                                                       throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedTRC20Parameters parseFrom(byte[] data,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedTRC20Parameters parseFrom(java.io.InputStream input)
                                                       throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedTRC20Parameters parseFrom(java.io.InputStream input,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static GrpcAPI.ShieldedTRC20Parameters parseDelimitedFrom(java.io.InputStream input)
                                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static GrpcAPI.ShieldedTRC20Parameters parseDelimitedFrom(java.io.InputStream input,
                                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedTRC20Parameters parseFrom(com.google.protobuf.CodedInputStream input)
                                                       throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedTRC20Parameters parseFrom(com.google.protobuf.CodedInputStream input,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static GrpcAPI.ShieldedTRC20Parameters.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static GrpcAPI.ShieldedTRC20Parameters.Builder newBuilder(GrpcAPI.ShieldedTRC20Parameters prototype)
      ```
    - #### toBuilder

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected GrpcAPI.ShieldedTRC20Parameters.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static GrpcAPI.ShieldedTRC20Parameters getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<GrpcAPI.ShieldedTRC20Parameters> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<GrpcAPI.ShieldedTRC20Parameters> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.ShieldedTRC20Parameters getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`