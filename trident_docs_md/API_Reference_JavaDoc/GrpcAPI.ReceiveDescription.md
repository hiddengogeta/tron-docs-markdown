

org.tron.trident.api

## Class GrpcAPI.ReceiveDescription

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.api.GrpcAPI.ReceiveDescription

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [GrpcAPI.ReceiveDescriptionOrBuilder](../../../../org/tron/trident/api/GrpcAPI.ReceiveDescriptionOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.ReceiveDescription
  extends com.google.protobuf.GeneratedMessageV3
  implements GrpcAPI.ReceiveDescriptionOrBuilder
  ```

  Protobuf type `protocol.ReceiveDescription`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.api.GrpcAPI.ReceiveDescription)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `GrpcAPI.ReceiveDescription.Builder` Protobuf type `protocol.ReceiveDescription` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `C_ENC_FIELD_NUMBER` |
    | `static int` | `C_OUT_FIELD_NUMBER` |
    | `static int` | `EPK_FIELD_NUMBER` |
    | `static int` | `NOTE_COMMITMENT_FIELD_NUMBER` |
    | `static int` | `VALUE_COMMITMENT_FIELD_NUMBER` |
    | `static int` | `ZKPROOF_FIELD_NUMBER` |

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
    | `com.google.protobuf.ByteString` | `getCEnc()` Encryption for incoming, decrypt it with ivk |
    | `com.google.protobuf.ByteString` | `getCOut()` Encryption for audit, decrypt it with ovk |
    | `static GrpcAPI.ReceiveDescription` | `getDefaultInstance()` |
    | `GrpcAPI.ReceiveDescription` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.ByteString` | `getEpk()` for Encryption |
    | `com.google.protobuf.ByteString` | `getNoteCommitment()` `bytes note_commitment = 2;` |
    | `com.google.protobuf.Parser<GrpcAPI.ReceiveDescription>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `com.google.protobuf.ByteString` | `getValueCommitment()` `bytes value_commitment = 1;` |
    | `com.google.protobuf.ByteString` | `getZkproof()` `bytes zkproof = 6;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static GrpcAPI.ReceiveDescription.Builder` | `newBuilder()` |
    | `static GrpcAPI.ReceiveDescription.Builder` | `newBuilder(GrpcAPI.ReceiveDescription prototype)` |
    | `GrpcAPI.ReceiveDescription.Builder` | `newBuilderForType()` |
    | `protected GrpcAPI.ReceiveDescription.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static GrpcAPI.ReceiveDescription` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static GrpcAPI.ReceiveDescription` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.ReceiveDescription` | `parseFrom(byte[] data)` |
    | `static GrpcAPI.ReceiveDescription` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.ReceiveDescription` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static GrpcAPI.ReceiveDescription` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.ReceiveDescription` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static GrpcAPI.ReceiveDescription` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.ReceiveDescription` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static GrpcAPI.ReceiveDescription` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.ReceiveDescription` | `parseFrom(java.io.InputStream input)` |
    | `static GrpcAPI.ReceiveDescription` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<GrpcAPI.ReceiveDescription>` | `parser()` |
    | `GrpcAPI.ReceiveDescription.Builder` | `toBuilder()` |
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

    - #### VALUE\_COMMITMENT\_FIELD\_NUMBER

      ```
      public static final int VALUE_COMMITMENT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ReceiveDescription.VALUE_COMMITMENT_FIELD_NUMBER)
    - #### NOTE\_COMMITMENT\_FIELD\_NUMBER

      ```
      public static final int NOTE_COMMITMENT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ReceiveDescription.NOTE_COMMITMENT_FIELD_NUMBER)
    - #### EPK\_FIELD\_NUMBER

      ```
      public static final int EPK_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ReceiveDescription.EPK_FIELD_NUMBER)
    - #### C\_ENC\_FIELD\_NUMBER

      ```
      public static final int C_ENC_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ReceiveDescription.C_ENC_FIELD_NUMBER)
    - #### C\_OUT\_FIELD\_NUMBER

      ```
      public static final int C_OUT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ReceiveDescription.C_OUT_FIELD_NUMBER)
    - #### ZKPROOF\_FIELD\_NUMBER

      ```
      public static final int ZKPROOF_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.ReceiveDescription.ZKPROOF_FIELD_NUMBER)
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
    - #### getValueCommitment

      ```
      public com.google.protobuf.ByteString getValueCommitment()
      ```

      `bytes value_commitment = 1;`

      Specified by:
      :   `getValueCommitment` in interface `GrpcAPI.ReceiveDescriptionOrBuilder`

      Returns:
      :   The valueCommitment.
    - #### getNoteCommitment

      ```
      public com.google.protobuf.ByteString getNoteCommitment()
      ```

      `bytes note_commitment = 2;`

      Specified by:
      :   `getNoteCommitment` in interface `GrpcAPI.ReceiveDescriptionOrBuilder`

      Returns:
      :   The noteCommitment.
    - #### getEpk

      ```
      public com.google.protobuf.ByteString getEpk()
      ```

      ```
       for Encryption
      ```

      `bytes epk = 3;`

      Specified by:
      :   `getEpk` in interface `GrpcAPI.ReceiveDescriptionOrBuilder`

      Returns:
      :   The epk.
    - #### getCEnc

      ```
      public com.google.protobuf.ByteString getCEnc()
      ```

      ```
       Encryption for incoming, decrypt it with ivk
      ```

      `bytes c_enc = 4;`

      Specified by:
      :   `getCEnc` in interface `GrpcAPI.ReceiveDescriptionOrBuilder`

      Returns:
      :   The cEnc.
    - #### getCOut

      ```
      public com.google.protobuf.ByteString getCOut()
      ```

      ```
       Encryption for audit, decrypt it with ovk
      ```

      `bytes c_out = 5;`

      Specified by:
      :   `getCOut` in interface `GrpcAPI.ReceiveDescriptionOrBuilder`

      Returns:
      :   The cOut.
    - #### getZkproof

      ```
      public com.google.protobuf.ByteString getZkproof()
      ```

      `bytes zkproof = 6;`

      Specified by:
      :   `getZkproof` in interface `GrpcAPI.ReceiveDescriptionOrBuilder`

      Returns:
      :   The zkproof.
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
      public static GrpcAPI.ReceiveDescription parseFrom(java.nio.ByteBuffer data)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ReceiveDescription parseFrom(java.nio.ByteBuffer data,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ReceiveDescription parseFrom(com.google.protobuf.ByteString data)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ReceiveDescription parseFrom(com.google.protobuf.ByteString data,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ReceiveDescription parseFrom(byte[] data)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ReceiveDescription parseFrom(byte[] data,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.ReceiveDescription parseFrom(java.io.InputStream input)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.ReceiveDescription parseFrom(java.io.InputStream input,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static GrpcAPI.ReceiveDescription parseDelimitedFrom(java.io.InputStream input)
                                                           throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static GrpcAPI.ReceiveDescription parseDelimitedFrom(java.io.InputStream input,
                                                                  com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                           throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.ReceiveDescription parseFrom(com.google.protobuf.CodedInputStream input)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.ReceiveDescription parseFrom(com.google.protobuf.CodedInputStream input,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public GrpcAPI.ReceiveDescription.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static GrpcAPI.ReceiveDescription.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static GrpcAPI.ReceiveDescription.Builder newBuilder(GrpcAPI.ReceiveDescription prototype)
      ```
    - #### toBuilder

      ```
      public GrpcAPI.ReceiveDescription.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected GrpcAPI.ReceiveDescription.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static GrpcAPI.ReceiveDescription getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<GrpcAPI.ReceiveDescription> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<GrpcAPI.ReceiveDescription> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.ReceiveDescription getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`