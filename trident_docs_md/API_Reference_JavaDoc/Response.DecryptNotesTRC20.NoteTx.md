

org.tron.trident.proto

## Class Response.DecryptNotesTRC20.NoteTx

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.DecryptNotesTRC20.NoteTx

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.DecryptNotesTRC20.NoteTxOrBuilder](../../../../org/tron/trident/proto/Response.DecryptNotesTRC20.NoteTxOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.DecryptNotesTRC20](../../../../org/tron/trident/proto/Response.DecryptNotesTRC20.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.DecryptNotesTRC20.NoteTx
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.DecryptNotesTRC20.NoteTxOrBuilder
  ```

  Protobuf type `protocol.DecryptNotesTRC20.NoteTx`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.DecryptNotesTRC20.NoteTx)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.DecryptNotesTRC20.NoteTx.Builder` Protobuf type `protocol.DecryptNotesTRC20.NoteTx` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `INDEX_FIELD_NUMBER` |
    | `static int` | `IS_SPENT_FIELD_NUMBER` |
    | `static int` | `NOTE_FIELD_NUMBER` |
    | `static int` | `POSITION_FIELD_NUMBER` |
    | `static int` | `TO_AMOUNT_FIELD_NUMBER` |
    | `static int` | `TRANSPARENT_TO_ADDRESS_FIELD_NUMBER` |
    | `static int` | `TXID_FIELD_NUMBER` |

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
    | `static Response.DecryptNotesTRC20.NoteTx` | `getDefaultInstance()` |
    | `Response.DecryptNotesTRC20.NoteTx` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `int` | `getIndex()` the index of note in txid |
    | `boolean` | `getIsSpent()` `bool is_spent = 3;` |
    | `Common.Note` | `getNote()` `.protocol.Note note = 1;` |
    | `Common.NoteOrBuilder` | `getNoteOrBuilder()` `.protocol.Note note = 1;` |
    | `com.google.protobuf.Parser<Response.DecryptNotesTRC20.NoteTx>` | `getParserForType()` |
    | `long` | `getPosition()` `int64 position = 2;` |
    | `int` | `getSerializedSize()` |
    | `java.lang.String` | `getToAmount()` `string to_amount = 6;` |
    | `com.google.protobuf.ByteString` | `getToAmountBytes()` `string to_amount = 6;` |
    | `com.google.protobuf.ByteString` | `getTransparentToAddress()` `bytes transparent_to_address = 7;` |
    | `com.google.protobuf.ByteString` | `getTxid()` `bytes txid = 4;` |
    | `int` | `hashCode()` |
    | `boolean` | `hasNote()` `.protocol.Note note = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Response.DecryptNotesTRC20.NoteTx.Builder` | `newBuilder()` |
    | `static Response.DecryptNotesTRC20.NoteTx.Builder` | `newBuilder(Response.DecryptNotesTRC20.NoteTx prototype)` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `newBuilderForType()` |
    | `protected Response.DecryptNotesTRC20.NoteTx.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.DecryptNotesTRC20.NoteTx` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.DecryptNotesTRC20.NoteTx` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.DecryptNotesTRC20.NoteTx` | `parseFrom(byte[] data)` |
    | `static Response.DecryptNotesTRC20.NoteTx` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.DecryptNotesTRC20.NoteTx` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.DecryptNotesTRC20.NoteTx` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.DecryptNotesTRC20.NoteTx` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.DecryptNotesTRC20.NoteTx` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.DecryptNotesTRC20.NoteTx` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.DecryptNotesTRC20.NoteTx` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.DecryptNotesTRC20.NoteTx` | `parseFrom(java.io.InputStream input)` |
    | `static Response.DecryptNotesTRC20.NoteTx` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.DecryptNotesTRC20.NoteTx>` | `parser()` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `toBuilder()` |
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
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.DecryptNotesTRC20.NoteTx.NOTE_FIELD_NUMBER)
    - #### POSITION\_FIELD\_NUMBER

      ```
      public static final int POSITION_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.DecryptNotesTRC20.NoteTx.POSITION_FIELD_NUMBER)
    - #### IS\_SPENT\_FIELD\_NUMBER

      ```
      public static final int IS_SPENT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.DecryptNotesTRC20.NoteTx.IS_SPENT_FIELD_NUMBER)
    - #### TXID\_FIELD\_NUMBER

      ```
      public static final int TXID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.DecryptNotesTRC20.NoteTx.TXID_FIELD_NUMBER)
    - #### INDEX\_FIELD\_NUMBER

      ```
      public static final int INDEX_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.DecryptNotesTRC20.NoteTx.INDEX_FIELD_NUMBER)
    - #### TO\_AMOUNT\_FIELD\_NUMBER

      ```
      public static final int TO_AMOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.DecryptNotesTRC20.NoteTx.TO_AMOUNT_FIELD_NUMBER)
    - #### TRANSPARENT\_TO\_ADDRESS\_FIELD\_NUMBER

      ```
      public static final int TRANSPARENT_TO_ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.DecryptNotesTRC20.NoteTx.TRANSPARENT_TO_ADDRESS_FIELD_NUMBER)
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
      :   `hasNote` in interface `Response.DecryptNotesTRC20.NoteTxOrBuilder`

      Returns:
      :   Whether the note field is set.
    - #### getNote

      ```
      public Common.Note getNote()
      ```

      `.protocol.Note note = 1;`

      Specified by:
      :   `getNote` in interface `Response.DecryptNotesTRC20.NoteTxOrBuilder`

      Returns:
      :   The note.
    - #### getNoteOrBuilder

      ```
      public Common.NoteOrBuilder getNoteOrBuilder()
      ```

      `.protocol.Note note = 1;`

      Specified by:
      :   `getNoteOrBuilder` in interface `Response.DecryptNotesTRC20.NoteTxOrBuilder`
    - #### getPosition

      ```
      public long getPosition()
      ```

      `int64 position = 2;`

      Specified by:
      :   `getPosition` in interface `Response.DecryptNotesTRC20.NoteTxOrBuilder`

      Returns:
      :   The position.
    - #### getIsSpent

      ```
      public boolean getIsSpent()
      ```

      `bool is_spent = 3;`

      Specified by:
      :   `getIsSpent` in interface `Response.DecryptNotesTRC20.NoteTxOrBuilder`

      Returns:
      :   The isSpent.
    - #### getTxid

      ```
      public com.google.protobuf.ByteString getTxid()
      ```

      `bytes txid = 4;`

      Specified by:
      :   `getTxid` in interface `Response.DecryptNotesTRC20.NoteTxOrBuilder`

      Returns:
      :   The txid.
    - #### getIndex

      ```
      public int getIndex()
      ```

      ```
       the index of note in txid
      ```

      `int32 index = 5;`

      Specified by:
      :   `getIndex` in interface `Response.DecryptNotesTRC20.NoteTxOrBuilder`

      Returns:
      :   The index.
    - #### getToAmount

      ```
      public java.lang.String getToAmount()
      ```

      `string to_amount = 6;`

      Specified by:
      :   `getToAmount` in interface `Response.DecryptNotesTRC20.NoteTxOrBuilder`

      Returns:
      :   The toAmount.
    - #### getToAmountBytes

      ```
      public com.google.protobuf.ByteString getToAmountBytes()
      ```

      `string to_amount = 6;`

      Specified by:
      :   `getToAmountBytes` in interface `Response.DecryptNotesTRC20.NoteTxOrBuilder`

      Returns:
      :   The bytes for toAmount.
    - #### getTransparentToAddress

      ```
      public com.google.protobuf.ByteString getTransparentToAddress()
      ```

      `bytes transparent_to_address = 7;`

      Specified by:
      :   `getTransparentToAddress` in interface `Response.DecryptNotesTRC20.NoteTxOrBuilder`

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
      public static Response.DecryptNotesTRC20.NoteTx parseFrom(java.nio.ByteBuffer data)
                                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DecryptNotesTRC20.NoteTx parseFrom(java.nio.ByteBuffer data,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DecryptNotesTRC20.NoteTx parseFrom(com.google.protobuf.ByteString data)
                                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DecryptNotesTRC20.NoteTx parseFrom(com.google.protobuf.ByteString data,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DecryptNotesTRC20.NoteTx parseFrom(byte[] data)
                                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DecryptNotesTRC20.NoteTx parseFrom(byte[] data,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DecryptNotesTRC20.NoteTx parseFrom(java.io.InputStream input)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.DecryptNotesTRC20.NoteTx parseFrom(java.io.InputStream input,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.DecryptNotesTRC20.NoteTx parseDelimitedFrom(java.io.InputStream input)
                                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.DecryptNotesTRC20.NoteTx parseDelimitedFrom(java.io.InputStream input,
                                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.DecryptNotesTRC20.NoteTx parseFrom(com.google.protobuf.CodedInputStream input)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.DecryptNotesTRC20.NoteTx parseFrom(com.google.protobuf.CodedInputStream input,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.DecryptNotesTRC20.NoteTx.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.DecryptNotesTRC20.NoteTx.Builder newBuilder(Response.DecryptNotesTRC20.NoteTx prototype)
      ```
    - #### toBuilder

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.DecryptNotesTRC20.NoteTx.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.DecryptNotesTRC20.NoteTx getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.DecryptNotesTRC20.NoteTx> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.DecryptNotesTRC20.NoteTx> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.DecryptNotesTRC20.NoteTx getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`