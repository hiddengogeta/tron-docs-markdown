

org.tron.trident.api

## Class GrpcAPI.ShieldedTRC20TriggerContractParameters

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.api.GrpcAPI.ShieldedTRC20TriggerContractParameters

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder](../../../../org/tron/trident/api/GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.ShieldedTRC20TriggerContractParameters
  extends com.google.protobuf.GeneratedMessageV3
  implements GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder
  ```

  Protobuf type `protocol.ShieldedTRC20TriggerContractParameters`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.api.GrpcAPI.ShieldedTRC20TriggerContractParameters)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` Protobuf type `protocol.ShieldedTRC20TriggerContractParameters` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `AMOUNT_FIELD_NUMBER` |
    | `static int` | `SHIELDED_TRC20_PARAMETERS_FIELD_NUMBER` |
    | `static int` | `SPEND_AUTHORITY_SIGNATURE_FIELD_NUMBER` |
    | `static int` | `TRANSPARENT_TO_ADDRESS_FIELD_NUMBER` |

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
    | `java.lang.String` | `getAmount()` `string amount = 3;` |
    | `com.google.protobuf.ByteString` | `getAmountBytes()` `string amount = 3;` |
    | `static GrpcAPI.ShieldedTRC20TriggerContractParameters` | `getDefaultInstance()` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Parser<GrpcAPI.ShieldedTRC20TriggerContractParameters>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `GrpcAPI.ShieldedTRC20Parameters` | `getShieldedTRC20Parameters()` `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;` |
    | `GrpcAPI.ShieldedTRC20ParametersOrBuilder` | `getShieldedTRC20ParametersOrBuilder()` `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;` |
    | `GrpcAPI.BytesMessage` | `getSpendAuthoritySignature(int index)` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `int` | `getSpendAuthoritySignatureCount()` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `java.util.List<GrpcAPI.BytesMessage>` | `getSpendAuthoritySignatureList()` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `GrpcAPI.BytesMessageOrBuilder` | `getSpendAuthoritySignatureOrBuilder(int index)` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `java.util.List<? extends GrpcAPI.BytesMessageOrBuilder>` | `getSpendAuthoritySignatureOrBuilderList()` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `com.google.protobuf.ByteString` | `getTransparentToAddress()` `bytes transparent_to_address = 4;` |
    | `int` | `hashCode()` |
    | `boolean` | `hasShieldedTRC20Parameters()` `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `newBuilder()` |
    | `static GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `newBuilder(GrpcAPI.ShieldedTRC20TriggerContractParameters prototype)` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `newBuilderForType()` |
    | `protected GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static GrpcAPI.ShieldedTRC20TriggerContractParameters` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static GrpcAPI.ShieldedTRC20TriggerContractParameters` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.ShieldedTRC20TriggerContractParameters` | `parseFrom(byte[] data)` |
    | `static GrpcAPI.ShieldedTRC20TriggerContractParameters` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.ShieldedTRC20TriggerContractParameters` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static GrpcAPI.ShieldedTRC20TriggerContractParameters` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.ShieldedTRC20TriggerContractParameters` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static GrpcAPI.ShieldedTRC20TriggerContractParameters` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.ShieldedTRC20TriggerContractParameters` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static GrpcAPI.ShieldedTRC20TriggerContractParameters` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.ShieldedTRC20TriggerContractParameters` | `parseFrom(java.io.InputStream input)` |
    | `static GrpcAPI.ShieldedTRC20TriggerContractParameters` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<GrpcAPI.ShieldedTRC20TriggerContractParameters>` | `parser()` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `toBuilder()` |
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

    - #### SHIELDED\_TRC20\_PARAMETERS\_FIELD\_NUMBER

      ```
      public static final int SHIELDED_TRC20_PARAMETERS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ShieldedTRC20TriggerContractParameters.SHIELDED_TRC20_PARAMETERS_FIELD_NUMBER)
    - #### SPEND\_AUTHORITY\_SIGNATURE\_FIELD\_NUMBER

      ```
      public static final int SPEND_AUTHORITY_SIGNATURE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ShieldedTRC20TriggerContractParameters.SPEND_AUTHORITY_SIGNATURE_FIELD_NUMBER)
    - #### AMOUNT\_FIELD\_NUMBER

      ```
      public static final int AMOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ShieldedTRC20TriggerContractParameters.AMOUNT_FIELD_NUMBER)
    - #### TRANSPARENT\_TO\_ADDRESS\_FIELD\_NUMBER

      ```
      public static final int TRANSPARENT_TO_ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ShieldedTRC20TriggerContractParameters.TRANSPARENT_TO_ADDRESS_FIELD_NUMBER)
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
    - #### hasShieldedTRC20Parameters

      ```
      public boolean hasShieldedTRC20Parameters()
      ```

      `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;`

      Specified by:
      :   `hasShieldedTRC20Parameters` in interface `GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder`

      Returns:
      :   Whether the shieldedTRC20Parameters field is set.
    - #### getShieldedTRC20Parameters

      ```
      public GrpcAPI.ShieldedTRC20Parameters getShieldedTRC20Parameters()
      ```

      `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;`

      Specified by:
      :   `getShieldedTRC20Parameters` in interface `GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder`

      Returns:
      :   The shieldedTRC20Parameters.
    - #### getShieldedTRC20ParametersOrBuilder

      ```
      public GrpcAPI.ShieldedTRC20ParametersOrBuilder getShieldedTRC20ParametersOrBuilder()
      ```

      `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;`

      Specified by:
      :   `getShieldedTRC20ParametersOrBuilder` in interface `GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder`
    - #### getSpendAuthoritySignatureList

      ```
      public java.util.List<GrpcAPI.BytesMessage> getSpendAuthoritySignatureList()
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`

      Specified by:
      :   `getSpendAuthoritySignatureList` in interface `GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder`
    - #### getSpendAuthoritySignatureOrBuilderList

      ```
      public java.util.List<? extends GrpcAPI.BytesMessageOrBuilder> getSpendAuthoritySignatureOrBuilderList()
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`

      Specified by:
      :   `getSpendAuthoritySignatureOrBuilderList` in interface `GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder`
    - #### getSpendAuthoritySignatureCount

      ```
      public int getSpendAuthoritySignatureCount()
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`

      Specified by:
      :   `getSpendAuthoritySignatureCount` in interface `GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder`
    - #### getSpendAuthoritySignature

      ```
      public GrpcAPI.BytesMessage getSpendAuthoritySignature(int index)
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`

      Specified by:
      :   `getSpendAuthoritySignature` in interface `GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder`
    - #### getSpendAuthoritySignatureOrBuilder

      ```
      public GrpcAPI.BytesMessageOrBuilder getSpendAuthoritySignatureOrBuilder(int index)
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`

      Specified by:
      :   `getSpendAuthoritySignatureOrBuilder` in interface `GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder`
    - #### getAmount

      ```
      public java.lang.String getAmount()
      ```

      `string amount = 3;`

      Specified by:
      :   `getAmount` in interface `GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder`

      Returns:
      :   The amount.
    - #### getAmountBytes

      ```
      public com.google.protobuf.ByteString getAmountBytes()
      ```

      `string amount = 3;`

      Specified by:
      :   `getAmountBytes` in interface `GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder`

      Returns:
      :   The bytes for amount.
    - #### getTransparentToAddress

      ```
      public com.google.protobuf.ByteString getTransparentToAddress()
      ```

      `bytes transparent_to_address = 4;`

      Specified by:
      :   `getTransparentToAddress` in interface `GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder`

      Returns:
      :   The transparentToAddress.
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
      public static GrpcAPI.ShieldedTRC20TriggerContractParameters parseFrom(java.nio.ByteBuffer data)
                                                                      throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedTRC20TriggerContractParameters parseFrom(java.nio.ByteBuffer data,
                                                                             com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                      throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedTRC20TriggerContractParameters parseFrom(com.google.protobuf.ByteString data)
                                                                      throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedTRC20TriggerContractParameters parseFrom(com.google.protobuf.ByteString data,
                                                                             com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                      throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedTRC20TriggerContractParameters parseFrom(byte[] data)
                                                                      throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedTRC20TriggerContractParameters parseFrom(byte[] data,
                                                                             com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                      throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedTRC20TriggerContractParameters parseFrom(java.io.InputStream input)
                                                                      throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedTRC20TriggerContractParameters parseFrom(java.io.InputStream input,
                                                                             com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                      throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static GrpcAPI.ShieldedTRC20TriggerContractParameters parseDelimitedFrom(java.io.InputStream input)
                                                                               throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static GrpcAPI.ShieldedTRC20TriggerContractParameters parseDelimitedFrom(java.io.InputStream input,
                                                                                      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                               throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedTRC20TriggerContractParameters parseFrom(com.google.protobuf.CodedInputStream input)
                                                                      throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedTRC20TriggerContractParameters parseFrom(com.google.protobuf.CodedInputStream input,
                                                                             com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                      throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder newBuilder(GrpcAPI.ShieldedTRC20TriggerContractParameters prototype)
      ```
    - #### toBuilder

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static GrpcAPI.ShieldedTRC20TriggerContractParameters getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<GrpcAPI.ShieldedTRC20TriggerContractParameters> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<GrpcAPI.ShieldedTRC20TriggerContractParameters> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`