

org.tron.trident.api

## Class GrpcAPI.PrivateShieldedTRC20Parameters

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.api.GrpcAPI.PrivateShieldedTRC20Parameters

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder](../../../../org/tron/trident/api/GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.PrivateShieldedTRC20Parameters
  extends com.google.protobuf.GeneratedMessageV3
  implements GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder
  ```

  Protobuf type `protocol.PrivateShieldedTRC20Parameters`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.api.GrpcAPI.PrivateShieldedTRC20Parameters)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` Protobuf type `protocol.PrivateShieldedTRC20Parameters` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `ASK_FIELD_NUMBER` |
    | `static int` | `FROM_AMOUNT_FIELD_NUMBER` |
    | `static int` | `NSK_FIELD_NUMBER` |
    | `static int` | `OVK_FIELD_NUMBER` |
    | `static int` | `SHIELDED_RECEIVES_FIELD_NUMBER` |
    | `static int` | `SHIELDED_SPENDS_FIELD_NUMBER` |
    | `static int` | `SHIELDED_TRC20_CONTRACT_ADDRESS_FIELD_NUMBER` |
    | `static int` | `TO_AMOUNT_FIELD_NUMBER` |
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
    | `com.google.protobuf.ByteString` | `getAsk()` `bytes ask = 1;` |
    | `static GrpcAPI.PrivateShieldedTRC20Parameters` | `getDefaultInstance()` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `java.lang.String` | `getFromAmount()` `string from_amount = 4;` |
    | `com.google.protobuf.ByteString` | `getFromAmountBytes()` `string from_amount = 4;` |
    | `com.google.protobuf.ByteString` | `getNsk()` `bytes nsk = 2;` |
    | `com.google.protobuf.ByteString` | `getOvk()` `bytes ovk = 3;` |
    | `com.google.protobuf.Parser<GrpcAPI.PrivateShieldedTRC20Parameters>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `GrpcAPI.ReceiveNote` | `getShieldedReceives(int index)` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `int` | `getShieldedReceivesCount()` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `java.util.List<GrpcAPI.ReceiveNote>` | `getShieldedReceivesList()` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `GrpcAPI.ReceiveNoteOrBuilder` | `getShieldedReceivesOrBuilder(int index)` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `java.util.List<? extends GrpcAPI.ReceiveNoteOrBuilder>` | `getShieldedReceivesOrBuilderList()` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `GrpcAPI.SpendNoteTRC20` | `getShieldedSpends(int index)` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `int` | `getShieldedSpendsCount()` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `java.util.List<GrpcAPI.SpendNoteTRC20>` | `getShieldedSpendsList()` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `GrpcAPI.SpendNoteTRC20OrBuilder` | `getShieldedSpendsOrBuilder(int index)` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `java.util.List<? extends GrpcAPI.SpendNoteTRC20OrBuilder>` | `getShieldedSpendsOrBuilderList()` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `com.google.protobuf.ByteString` | `getShieldedTRC20ContractAddress()` `bytes shielded_TRC20_contract_address = 9;` |
    | `java.lang.String` | `getToAmount()` `string to_amount = 8;` |
    | `com.google.protobuf.ByteString` | `getToAmountBytes()` `string to_amount = 8;` |
    | `com.google.protobuf.ByteString` | `getTransparentToAddress()` `bytes transparent_to_address = 7;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `newBuilder()` |
    | `static GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `newBuilder(GrpcAPI.PrivateShieldedTRC20Parameters prototype)` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `newBuilderForType()` |
    | `protected GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static GrpcAPI.PrivateShieldedTRC20Parameters` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static GrpcAPI.PrivateShieldedTRC20Parameters` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.PrivateShieldedTRC20Parameters` | `parseFrom(byte[] data)` |
    | `static GrpcAPI.PrivateShieldedTRC20Parameters` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.PrivateShieldedTRC20Parameters` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static GrpcAPI.PrivateShieldedTRC20Parameters` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.PrivateShieldedTRC20Parameters` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static GrpcAPI.PrivateShieldedTRC20Parameters` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.PrivateShieldedTRC20Parameters` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static GrpcAPI.PrivateShieldedTRC20Parameters` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.PrivateShieldedTRC20Parameters` | `parseFrom(java.io.InputStream input)` |
    | `static GrpcAPI.PrivateShieldedTRC20Parameters` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<GrpcAPI.PrivateShieldedTRC20Parameters>` | `parser()` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `toBuilder()` |
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

    - #### ASK\_FIELD\_NUMBER

      ```
      public static final int ASK_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.PrivateShieldedTRC20Parameters.ASK_FIELD_NUMBER)
    - #### NSK\_FIELD\_NUMBER

      ```
      public static final int NSK_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.PrivateShieldedTRC20Parameters.NSK_FIELD_NUMBER)
    - #### OVK\_FIELD\_NUMBER

      ```
      public static final int OVK_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.PrivateShieldedTRC20Parameters.OVK_FIELD_NUMBER)
    - #### FROM\_AMOUNT\_FIELD\_NUMBER

      ```
      public static final int FROM_AMOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.PrivateShieldedTRC20Parameters.FROM_AMOUNT_FIELD_NUMBER)
    - #### SHIELDED\_SPENDS\_FIELD\_NUMBER

      ```
      public static final int SHIELDED_SPENDS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.PrivateShieldedTRC20Parameters.SHIELDED_SPENDS_FIELD_NUMBER)
    - #### SHIELDED\_RECEIVES\_FIELD\_NUMBER

      ```
      public static final int SHIELDED_RECEIVES_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.PrivateShieldedTRC20Parameters.SHIELDED_RECEIVES_FIELD_NUMBER)
    - #### TRANSPARENT\_TO\_ADDRESS\_FIELD\_NUMBER

      ```
      public static final int TRANSPARENT_TO_ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.PrivateShieldedTRC20Parameters.TRANSPARENT_TO_ADDRESS_FIELD_NUMBER)
    - #### TO\_AMOUNT\_FIELD\_NUMBER

      ```
      public static final int TO_AMOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.PrivateShieldedTRC20Parameters.TO_AMOUNT_FIELD_NUMBER)
    - #### SHIELDED\_TRC20\_CONTRACT\_ADDRESS\_FIELD\_NUMBER

      ```
      public static final int SHIELDED_TRC20_CONTRACT_ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.PrivateShieldedTRC20Parameters.SHIELDED_TRC20_CONTRACT_ADDRESS_FIELD_NUMBER)
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
    - #### getAsk

      ```
      public com.google.protobuf.ByteString getAsk()
      ```

      `bytes ask = 1;`

      Specified by:
      :   `getAsk` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The ask.
    - #### getNsk

      ```
      public com.google.protobuf.ByteString getNsk()
      ```

      `bytes nsk = 2;`

      Specified by:
      :   `getNsk` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The nsk.
    - #### getOvk

      ```
      public com.google.protobuf.ByteString getOvk()
      ```

      `bytes ovk = 3;`

      Specified by:
      :   `getOvk` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The ovk.
    - #### getFromAmount

      ```
      public java.lang.String getFromAmount()
      ```

      `string from_amount = 4;`

      Specified by:
      :   `getFromAmount` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The fromAmount.
    - #### getFromAmountBytes

      ```
      public com.google.protobuf.ByteString getFromAmountBytes()
      ```

      `string from_amount = 4;`

      Specified by:
      :   `getFromAmountBytes` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The bytes for fromAmount.
    - #### getShieldedSpendsList

      ```
      public java.util.List<GrpcAPI.SpendNoteTRC20> getShieldedSpendsList()
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`

      Specified by:
      :   `getShieldedSpendsList` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`
    - #### getShieldedSpendsOrBuilderList

      ```
      public java.util.List<? extends GrpcAPI.SpendNoteTRC20OrBuilder> getShieldedSpendsOrBuilderList()
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`

      Specified by:
      :   `getShieldedSpendsOrBuilderList` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`
    - #### getShieldedSpendsCount

      ```
      public int getShieldedSpendsCount()
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`

      Specified by:
      :   `getShieldedSpendsCount` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`
    - #### getShieldedSpends

      ```
      public GrpcAPI.SpendNoteTRC20 getShieldedSpends(int index)
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`

      Specified by:
      :   `getShieldedSpends` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`
    - #### getShieldedSpendsOrBuilder

      ```
      public GrpcAPI.SpendNoteTRC20OrBuilder getShieldedSpendsOrBuilder(int index)
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`

      Specified by:
      :   `getShieldedSpendsOrBuilder` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`
    - #### getShieldedReceivesList

      ```
      public java.util.List<GrpcAPI.ReceiveNote> getShieldedReceivesList()
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`

      Specified by:
      :   `getShieldedReceivesList` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`
    - #### getShieldedReceivesOrBuilderList

      ```
      public java.util.List<? extends GrpcAPI.ReceiveNoteOrBuilder> getShieldedReceivesOrBuilderList()
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`

      Specified by:
      :   `getShieldedReceivesOrBuilderList` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`
    - #### getShieldedReceivesCount

      ```
      public int getShieldedReceivesCount()
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`

      Specified by:
      :   `getShieldedReceivesCount` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`
    - #### getShieldedReceives

      ```
      public GrpcAPI.ReceiveNote getShieldedReceives(int index)
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`

      Specified by:
      :   `getShieldedReceives` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`
    - #### getShieldedReceivesOrBuilder

      ```
      public GrpcAPI.ReceiveNoteOrBuilder getShieldedReceivesOrBuilder(int index)
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`

      Specified by:
      :   `getShieldedReceivesOrBuilder` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`
    - #### getTransparentToAddress

      ```
      public com.google.protobuf.ByteString getTransparentToAddress()
      ```

      `bytes transparent_to_address = 7;`

      Specified by:
      :   `getTransparentToAddress` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The transparentToAddress.
    - #### getToAmount

      ```
      public java.lang.String getToAmount()
      ```

      `string to_amount = 8;`

      Specified by:
      :   `getToAmount` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The toAmount.
    - #### getToAmountBytes

      ```
      public com.google.protobuf.ByteString getToAmountBytes()
      ```

      `string to_amount = 8;`

      Specified by:
      :   `getToAmountBytes` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The bytes for toAmount.
    - #### getShieldedTRC20ContractAddress

      ```
      public com.google.protobuf.ByteString getShieldedTRC20ContractAddress()
      ```

      `bytes shielded_TRC20_contract_address = 9;`

      Specified by:
      :   `getShieldedTRC20ContractAddress` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The shieldedTRC20ContractAddress.
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
      public static GrpcAPI.PrivateShieldedTRC20Parameters parseFrom(java.nio.ByteBuffer data)
                                                              throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.PrivateShieldedTRC20Parameters parseFrom(java.nio.ByteBuffer data,
                                                                     com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                              throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.PrivateShieldedTRC20Parameters parseFrom(com.google.protobuf.ByteString data)
                                                              throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.PrivateShieldedTRC20Parameters parseFrom(com.google.protobuf.ByteString data,
                                                                     com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                              throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.PrivateShieldedTRC20Parameters parseFrom(byte[] data)
                                                              throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.PrivateShieldedTRC20Parameters parseFrom(byte[] data,
                                                                     com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                              throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.PrivateShieldedTRC20Parameters parseFrom(java.io.InputStream input)
                                                              throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.PrivateShieldedTRC20Parameters parseFrom(java.io.InputStream input,
                                                                     com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                              throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static GrpcAPI.PrivateShieldedTRC20Parameters parseDelimitedFrom(java.io.InputStream input)
                                                                       throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static GrpcAPI.PrivateShieldedTRC20Parameters parseDelimitedFrom(java.io.InputStream input,
                                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                       throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.PrivateShieldedTRC20Parameters parseFrom(com.google.protobuf.CodedInputStream input)
                                                              throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.PrivateShieldedTRC20Parameters parseFrom(com.google.protobuf.CodedInputStream input,
                                                                     com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                              throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static GrpcAPI.PrivateShieldedTRC20Parameters.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static GrpcAPI.PrivateShieldedTRC20Parameters.Builder newBuilder(GrpcAPI.PrivateShieldedTRC20Parameters prototype)
      ```
    - #### toBuilder

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected GrpcAPI.PrivateShieldedTRC20Parameters.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static GrpcAPI.PrivateShieldedTRC20Parameters getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<GrpcAPI.PrivateShieldedTRC20Parameters> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<GrpcAPI.PrivateShieldedTRC20Parameters> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`