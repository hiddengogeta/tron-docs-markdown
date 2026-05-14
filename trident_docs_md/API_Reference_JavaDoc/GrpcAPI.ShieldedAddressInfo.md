

org.tron.trident.api

## Class GrpcAPI.ShieldedAddressInfo

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.api.GrpcAPI.ShieldedAddressInfo

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [GrpcAPI.ShieldedAddressInfoOrBuilder](../../../../org/tron/trident/api/GrpcAPI.ShieldedAddressInfoOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.ShieldedAddressInfo
  extends com.google.protobuf.GeneratedMessageV3
  implements GrpcAPI.ShieldedAddressInfoOrBuilder
  ```

  Protobuf type `protocol.ShieldedAddressInfo`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.api.GrpcAPI.ShieldedAddressInfo)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `GrpcAPI.ShieldedAddressInfo.Builder` Protobuf type `protocol.ShieldedAddressInfo` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `AK_FIELD_NUMBER` |
    | `static int` | `ASK_FIELD_NUMBER` |
    | `static int` | `D_FIELD_NUMBER` |
    | `static int` | `IVK_FIELD_NUMBER` |
    | `static int` | `NK_FIELD_NUMBER` |
    | `static int` | `NSK_FIELD_NUMBER` |
    | `static int` | `OVK_FIELD_NUMBER` |
    | `static int` | `PAYMENT_ADDRESS_FIELD_NUMBER` |
    | `static int` | `PKD_FIELD_NUMBER` |
    | `static int` | `SK_FIELD_NUMBER` |

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
    | `com.google.protobuf.ByteString` | `getAk()` `bytes ak = 5;` |
    | `com.google.protobuf.ByteString` | `getAsk()` `bytes ask = 2;` |
    | `com.google.protobuf.ByteString` | `getD()` `bytes d = 8;` |
    | `static GrpcAPI.ShieldedAddressInfo` | `getDefaultInstance()` |
    | `GrpcAPI.ShieldedAddressInfo` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.ByteString` | `getIvk()` `bytes ivk = 7;` |
    | `com.google.protobuf.ByteString` | `getNk()` `bytes nk = 6;` |
    | `com.google.protobuf.ByteString` | `getNsk()` `bytes nsk = 3;` |
    | `com.google.protobuf.ByteString` | `getOvk()` `bytes ovk = 4;` |
    | `com.google.protobuf.Parser<GrpcAPI.ShieldedAddressInfo>` | `getParserForType()` |
    | `java.lang.String` | `getPaymentAddress()` `string payment_address = 10;` |
    | `com.google.protobuf.ByteString` | `getPaymentAddressBytes()` `string payment_address = 10;` |
    | `com.google.protobuf.ByteString` | `getPkD()` `bytes pkD = 9;` |
    | `int` | `getSerializedSize()` |
    | `com.google.protobuf.ByteString` | `getSk()` `bytes sk = 1;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static GrpcAPI.ShieldedAddressInfo.Builder` | `newBuilder()` |
    | `static GrpcAPI.ShieldedAddressInfo.Builder` | `newBuilder(GrpcAPI.ShieldedAddressInfo prototype)` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `newBuilderForType()` |
    | `protected GrpcAPI.ShieldedAddressInfo.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static GrpcAPI.ShieldedAddressInfo` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static GrpcAPI.ShieldedAddressInfo` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.ShieldedAddressInfo` | `parseFrom(byte[] data)` |
    | `static GrpcAPI.ShieldedAddressInfo` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.ShieldedAddressInfo` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static GrpcAPI.ShieldedAddressInfo` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.ShieldedAddressInfo` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static GrpcAPI.ShieldedAddressInfo` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.ShieldedAddressInfo` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static GrpcAPI.ShieldedAddressInfo` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.ShieldedAddressInfo` | `parseFrom(java.io.InputStream input)` |
    | `static GrpcAPI.ShieldedAddressInfo` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<GrpcAPI.ShieldedAddressInfo>` | `parser()` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `toBuilder()` |
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

    - #### SK\_FIELD\_NUMBER

      ```
      public static final int SK_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ShieldedAddressInfo.SK_FIELD_NUMBER)
    - #### ASK\_FIELD\_NUMBER

      ```
      public static final int ASK_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ShieldedAddressInfo.ASK_FIELD_NUMBER)
    - #### NSK\_FIELD\_NUMBER

      ```
      public static final int NSK_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ShieldedAddressInfo.NSK_FIELD_NUMBER)
    - #### OVK\_FIELD\_NUMBER

      ```
      public static final int OVK_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ShieldedAddressInfo.OVK_FIELD_NUMBER)
    - #### AK\_FIELD\_NUMBER

      ```
      public static final int AK_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ShieldedAddressInfo.AK_FIELD_NUMBER)
    - #### NK\_FIELD\_NUMBER

      ```
      public static final int NK_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ShieldedAddressInfo.NK_FIELD_NUMBER)
    - #### IVK\_FIELD\_NUMBER

      ```
      public static final int IVK_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ShieldedAddressInfo.IVK_FIELD_NUMBER)
    - #### D\_FIELD\_NUMBER

      ```
      public static final int D_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ShieldedAddressInfo.D_FIELD_NUMBER)
    - #### PKD\_FIELD\_NUMBER

      ```
      public static final int PKD_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ShieldedAddressInfo.PKD_FIELD_NUMBER)
    - #### PAYMENT\_ADDRESS\_FIELD\_NUMBER

      ```
      public static final int PAYMENT_ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ShieldedAddressInfo.PAYMENT_ADDRESS_FIELD_NUMBER)
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
    - #### getSk

      ```
      public com.google.protobuf.ByteString getSk()
      ```

      `bytes sk = 1;`

      Specified by:
      :   `getSk` in interface `GrpcAPI.ShieldedAddressInfoOrBuilder`

      Returns:
      :   The sk.
    - #### getAsk

      ```
      public com.google.protobuf.ByteString getAsk()
      ```

      `bytes ask = 2;`

      Specified by:
      :   `getAsk` in interface `GrpcAPI.ShieldedAddressInfoOrBuilder`

      Returns:
      :   The ask.
    - #### getNsk

      ```
      public com.google.protobuf.ByteString getNsk()
      ```

      `bytes nsk = 3;`

      Specified by:
      :   `getNsk` in interface `GrpcAPI.ShieldedAddressInfoOrBuilder`

      Returns:
      :   The nsk.
    - #### getOvk

      ```
      public com.google.protobuf.ByteString getOvk()
      ```

      `bytes ovk = 4;`

      Specified by:
      :   `getOvk` in interface `GrpcAPI.ShieldedAddressInfoOrBuilder`

      Returns:
      :   The ovk.
    - #### getAk

      ```
      public com.google.protobuf.ByteString getAk()
      ```

      `bytes ak = 5;`

      Specified by:
      :   `getAk` in interface `GrpcAPI.ShieldedAddressInfoOrBuilder`

      Returns:
      :   The ak.
    - #### getNk

      ```
      public com.google.protobuf.ByteString getNk()
      ```

      `bytes nk = 6;`

      Specified by:
      :   `getNk` in interface `GrpcAPI.ShieldedAddressInfoOrBuilder`

      Returns:
      :   The nk.
    - #### getIvk

      ```
      public com.google.protobuf.ByteString getIvk()
      ```

      `bytes ivk = 7;`

      Specified by:
      :   `getIvk` in interface `GrpcAPI.ShieldedAddressInfoOrBuilder`

      Returns:
      :   The ivk.
    - #### getD

      ```
      public com.google.protobuf.ByteString getD()
      ```

      `bytes d = 8;`

      Specified by:
      :   `getD` in interface `GrpcAPI.ShieldedAddressInfoOrBuilder`

      Returns:
      :   The d.
    - #### getPkD

      ```
      public com.google.protobuf.ByteString getPkD()
      ```

      `bytes pkD = 9;`

      Specified by:
      :   `getPkD` in interface `GrpcAPI.ShieldedAddressInfoOrBuilder`

      Returns:
      :   The pkD.
    - #### getPaymentAddress

      ```
      public java.lang.String getPaymentAddress()
      ```

      `string payment_address = 10;`

      Specified by:
      :   `getPaymentAddress` in interface `GrpcAPI.ShieldedAddressInfoOrBuilder`

      Returns:
      :   The paymentAddress.
    - #### getPaymentAddressBytes

      ```
      public com.google.protobuf.ByteString getPaymentAddressBytes()
      ```

      `string payment_address = 10;`

      Specified by:
      :   `getPaymentAddressBytes` in interface `GrpcAPI.ShieldedAddressInfoOrBuilder`

      Returns:
      :   The bytes for paymentAddress.
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
      public static GrpcAPI.ShieldedAddressInfo parseFrom(java.nio.ByteBuffer data)
                                                   throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedAddressInfo parseFrom(java.nio.ByteBuffer data,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedAddressInfo parseFrom(com.google.protobuf.ByteString data)
                                                   throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedAddressInfo parseFrom(com.google.protobuf.ByteString data,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedAddressInfo parseFrom(byte[] data)
                                                   throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedAddressInfo parseFrom(byte[] data,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedAddressInfo parseFrom(java.io.InputStream input)
                                                   throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedAddressInfo parseFrom(java.io.InputStream input,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static GrpcAPI.ShieldedAddressInfo parseDelimitedFrom(java.io.InputStream input)
                                                            throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static GrpcAPI.ShieldedAddressInfo parseDelimitedFrom(java.io.InputStream input,
                                                                   com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                            throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedAddressInfo parseFrom(com.google.protobuf.CodedInputStream input)
                                                   throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.ShieldedAddressInfo parseFrom(com.google.protobuf.CodedInputStream input,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static GrpcAPI.ShieldedAddressInfo.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static GrpcAPI.ShieldedAddressInfo.Builder newBuilder(GrpcAPI.ShieldedAddressInfo prototype)
      ```
    - #### toBuilder

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected GrpcAPI.ShieldedAddressInfo.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static GrpcAPI.ShieldedAddressInfo getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<GrpcAPI.ShieldedAddressInfo> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<GrpcAPI.ShieldedAddressInfo> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.ShieldedAddressInfo getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`