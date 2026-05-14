

org.tron.trident.api

## Class GrpcAPI.NfTRC20Parameters

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.api.GrpcAPI.NfTRC20Parameters

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [GrpcAPI.NfTRC20ParametersOrBuilder](../../../../org/tron/trident/api/GrpcAPI.NfTRC20ParametersOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.NfTRC20Parameters
  extends com.google.protobuf.GeneratedMessageV3
  implements GrpcAPI.NfTRC20ParametersOrBuilder
  ```

  Protobuf type `protocol.NfTRC20Parameters`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.api.GrpcAPI.NfTRC20Parameters)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `GrpcAPI.NfTRC20Parameters.Builder` Protobuf type `protocol.NfTRC20Parameters` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `AK_FIELD_NUMBER` |
    | `static int` | `NK_FIELD_NUMBER` |
    | `static int` | `NOTE_FIELD_NUMBER` |
    | `static int` | `POSITION_FIELD_NUMBER` |
    | `static int` | `SHIELDED_TRC20_CONTRACT_ADDRESS_FIELD_NUMBER` |

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
    | `com.google.protobuf.ByteString` | `getAk()` `bytes ak = 2;` |
    | `static GrpcAPI.NfTRC20Parameters` | `getDefaultInstance()` |
    | `GrpcAPI.NfTRC20Parameters` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.ByteString` | `getNk()` `bytes nk = 3;` |
    | `Common.Note` | `getNote()` `.protocol.Note note = 1;` |
    | `Common.NoteOrBuilder` | `getNoteOrBuilder()` `.protocol.Note note = 1;` |
    | `com.google.protobuf.Parser<GrpcAPI.NfTRC20Parameters>` | `getParserForType()` |
    | `long` | `getPosition()` `int64 position = 4;` |
    | `int` | `getSerializedSize()` |
    | `com.google.protobuf.ByteString` | `getShieldedTRC20ContractAddress()` `bytes shielded_TRC20_contract_address = 5;` |
    | `int` | `hashCode()` |
    | `boolean` | `hasNote()` `.protocol.Note note = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static GrpcAPI.NfTRC20Parameters.Builder` | `newBuilder()` |
    | `static GrpcAPI.NfTRC20Parameters.Builder` | `newBuilder(GrpcAPI.NfTRC20Parameters prototype)` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `newBuilderForType()` |
    | `protected GrpcAPI.NfTRC20Parameters.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static GrpcAPI.NfTRC20Parameters` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static GrpcAPI.NfTRC20Parameters` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.NfTRC20Parameters` | `parseFrom(byte[] data)` |
    | `static GrpcAPI.NfTRC20Parameters` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.NfTRC20Parameters` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static GrpcAPI.NfTRC20Parameters` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.NfTRC20Parameters` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static GrpcAPI.NfTRC20Parameters` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.NfTRC20Parameters` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static GrpcAPI.NfTRC20Parameters` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.NfTRC20Parameters` | `parseFrom(java.io.InputStream input)` |
    | `static GrpcAPI.NfTRC20Parameters` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<GrpcAPI.NfTRC20Parameters>` | `parser()` |
    | `GrpcAPI.NfTRC20Parameters.Builder` | `toBuilder()` |
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

    - #### NOTE\_FIELD\_NUMBER

      ```
      public static final int NOTE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.NfTRC20Parameters.NOTE_FIELD_NUMBER)
    - #### AK\_FIELD\_NUMBER

      ```
      public static final int AK_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.NfTRC20Parameters.AK_FIELD_NUMBER)
    - #### NK\_FIELD\_NUMBER

      ```
      public static final int NK_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.NfTRC20Parameters.NK_FIELD_NUMBER)
    - #### POSITION\_FIELD\_NUMBER

      ```
      public static final int POSITION_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.NfTRC20Parameters.POSITION_FIELD_NUMBER)
    - #### SHIELDED\_TRC20\_CONTRACT\_ADDRESS\_FIELD\_NUMBER

      ```
      public static final int SHIELDED_TRC20_CONTRACT_ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.NfTRC20Parameters.SHIELDED_TRC20_CONTRACT_ADDRESS_FIELD_NUMBER)
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
    - #### hasNote

      ```
      public boolean hasNote()
      ```

      `.protocol.Note note = 1;`

      Specified by:
      :   `hasNote` in interface `GrpcAPI.NfTRC20ParametersOrBuilder`

      Returns:
      :   Whether the note field is set.
    - #### getNote

      ```
      public Common.Note getNote()
      ```

      `.protocol.Note note = 1;`

      Specified by:
      :   `getNote` in interface `GrpcAPI.NfTRC20ParametersOrBuilder`

      Returns:
      :   The note.
    - #### getNoteOrBuilder

      ```
      public Common.NoteOrBuilder getNoteOrBuilder()
      ```

      `.protocol.Note note = 1;`

      Specified by:
      :   `getNoteOrBuilder` in interface `GrpcAPI.NfTRC20ParametersOrBuilder`
    - #### getAk

      ```
      public com.google.protobuf.ByteString getAk()
      ```

      `bytes ak = 2;`

      Specified by:
      :   `getAk` in interface `GrpcAPI.NfTRC20ParametersOrBuilder`

      Returns:
      :   The ak.
    - #### getNk

      ```
      public com.google.protobuf.ByteString getNk()
      ```

      `bytes nk = 3;`

      Specified by:
      :   `getNk` in interface `GrpcAPI.NfTRC20ParametersOrBuilder`

      Returns:
      :   The nk.
    - #### getPosition

      ```
      public long getPosition()
      ```

      `int64 position = 4;`

      Specified by:
      :   `getPosition` in interface `GrpcAPI.NfTRC20ParametersOrBuilder`

      Returns:
      :   The position.
    - #### getShieldedTRC20ContractAddress

      ```
      public com.google.protobuf.ByteString getShieldedTRC20ContractAddress()
      ```

      `bytes shielded_TRC20_contract_address = 5;`

      Specified by:
      :   `getShieldedTRC20ContractAddress` in interface `GrpcAPI.NfTRC20ParametersOrBuilder`

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
      public static GrpcAPI.NfTRC20Parameters parseFrom(java.nio.ByteBuffer data)
                                                 throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.NfTRC20Parameters parseFrom(java.nio.ByteBuffer data,
                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                 throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.NfTRC20Parameters parseFrom(com.google.protobuf.ByteString data)
                                                 throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.NfTRC20Parameters parseFrom(com.google.protobuf.ByteString data,
                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                 throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.NfTRC20Parameters parseFrom(byte[] data)
                                                 throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.NfTRC20Parameters parseFrom(byte[] data,
                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                 throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.NfTRC20Parameters parseFrom(java.io.InputStream input)
                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.NfTRC20Parameters parseFrom(java.io.InputStream input,
                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static GrpcAPI.NfTRC20Parameters parseDelimitedFrom(java.io.InputStream input)
                                                          throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static GrpcAPI.NfTRC20Parameters parseDelimitedFrom(java.io.InputStream input,
                                                                 com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                          throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.NfTRC20Parameters parseFrom(com.google.protobuf.CodedInputStream input)
                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.NfTRC20Parameters parseFrom(com.google.protobuf.CodedInputStream input,
                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public GrpcAPI.NfTRC20Parameters.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static GrpcAPI.NfTRC20Parameters.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static GrpcAPI.NfTRC20Parameters.Builder newBuilder(GrpcAPI.NfTRC20Parameters prototype)
      ```
    - #### toBuilder

      ```
      public GrpcAPI.NfTRC20Parameters.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected GrpcAPI.NfTRC20Parameters.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static GrpcAPI.NfTRC20Parameters getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<GrpcAPI.NfTRC20Parameters> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<GrpcAPI.NfTRC20Parameters> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.NfTRC20Parameters getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`