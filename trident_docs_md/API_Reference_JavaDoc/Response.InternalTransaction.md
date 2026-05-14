

org.tron.trident.proto

## Class Response.InternalTransaction

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.InternalTransaction

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.InternalTransactionOrBuilder](../../../../org/tron/trident/proto/Response.InternalTransactionOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.InternalTransaction
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.InternalTransactionOrBuilder
  ```

  Protobuf type `protocol.InternalTransaction`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.InternalTransaction)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.InternalTransaction.Builder` Protobuf type `protocol.InternalTransaction` |
    | `static class` | `Response.InternalTransaction.CallValueInfo` Protobuf type `protocol.InternalTransaction.CallValueInfo` |
    | `static interface` | `Response.InternalTransaction.CallValueInfoOrBuilder` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `CALLER_ADDRESS_FIELD_NUMBER` |
    | `static int` | `CALLVALUEINFO_FIELD_NUMBER` |
    | `static int` | `EXTRA_FIELD_NUMBER` |
    | `static int` | `HASH_FIELD_NUMBER` |
    | `static int` | `NOTE_FIELD_NUMBER` |
    | `static int` | `REJECTED_FIELD_NUMBER` |
    | `static int` | `TRANSFERTO_ADDRESS_FIELD_NUMBER` |

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
    | `com.google.protobuf.ByteString` | `getCallerAddress()` the one send trx (TBD: or token) via function |
    | `Response.InternalTransaction.CallValueInfo` | `getCallValueInfo(int index)` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `int` | `getCallValueInfoCount()` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `java.util.List<Response.InternalTransaction.CallValueInfo>` | `getCallValueInfoList()` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `Response.InternalTransaction.CallValueInfoOrBuilder` | `getCallValueInfoOrBuilder(int index)` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `java.util.List<? extends Response.InternalTransaction.CallValueInfoOrBuilder>` | `getCallValueInfoOrBuilderList()` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `static Response.InternalTransaction` | `getDefaultInstance()` |
    | `Response.InternalTransaction` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `java.lang.String` | `getExtra()` `string extra = 7;` |
    | `com.google.protobuf.ByteString` | `getExtraBytes()` `string extra = 7;` |
    | `com.google.protobuf.ByteString` | `getHash()` internalTransaction identity, the root InternalTransaction hash should equals to root transaction id. |
    | `com.google.protobuf.ByteString` | `getNote()` `bytes note = 5;` |
    | `com.google.protobuf.Parser<Response.InternalTransaction>` | `getParserForType()` |
    | `boolean` | `getRejected()` `bool rejected = 6;` |
    | `int` | `getSerializedSize()` |
    | `com.google.protobuf.ByteString` | `getTransferToAddress()` the one recieve trx (TBD: or token) via function |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Response.InternalTransaction.Builder` | `newBuilder()` |
    | `static Response.InternalTransaction.Builder` | `newBuilder(Response.InternalTransaction prototype)` |
    | `Response.InternalTransaction.Builder` | `newBuilderForType()` |
    | `protected Response.InternalTransaction.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.InternalTransaction` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.InternalTransaction` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.InternalTransaction` | `parseFrom(byte[] data)` |
    | `static Response.InternalTransaction` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.InternalTransaction` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.InternalTransaction` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.InternalTransaction` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.InternalTransaction` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.InternalTransaction` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.InternalTransaction` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.InternalTransaction` | `parseFrom(java.io.InputStream input)` |
    | `static Response.InternalTransaction` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.InternalTransaction>` | `parser()` |
    | `Response.InternalTransaction.Builder` | `toBuilder()` |
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

    - #### HASH\_FIELD\_NUMBER

      ```
      public static final int HASH_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.InternalTransaction.HASH_FIELD_NUMBER)
    - #### CALLER\_ADDRESS\_FIELD\_NUMBER

      ```
      public static final int CALLER_ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.InternalTransaction.CALLER_ADDRESS_FIELD_NUMBER)
    - #### TRANSFERTO\_ADDRESS\_FIELD\_NUMBER

      ```
      public static final int TRANSFERTO_ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.InternalTransaction.TRANSFERTO_ADDRESS_FIELD_NUMBER)
    - #### CALLVALUEINFO\_FIELD\_NUMBER

      ```
      public static final int CALLVALUEINFO_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.InternalTransaction.CALLVALUEINFO_FIELD_NUMBER)
    - #### NOTE\_FIELD\_NUMBER

      ```
      public static final int NOTE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.InternalTransaction.NOTE_FIELD_NUMBER)
    - #### REJECTED\_FIELD\_NUMBER

      ```
      public static final int REJECTED_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.InternalTransaction.REJECTED_FIELD_NUMBER)
    - #### EXTRA\_FIELD\_NUMBER

      ```
      public static final int EXTRA_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.InternalTransaction.EXTRA_FIELD_NUMBER)
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
    - #### getHash

      ```
      public com.google.protobuf.ByteString getHash()
      ```

      ```
       internalTransaction identity, the root InternalTransaction hash
       should equals to root transaction id.
      ```

      `bytes hash = 1;`

      Specified by:
      :   `getHash` in interface `Response.InternalTransactionOrBuilder`

      Returns:
      :   The hash.
    - #### getCallerAddress

      ```
      public com.google.protobuf.ByteString getCallerAddress()
      ```

      ```
       the one send trx (TBD: or token) via function
      ```

      `bytes caller_address = 2;`

      Specified by:
      :   `getCallerAddress` in interface `Response.InternalTransactionOrBuilder`

      Returns:
      :   The callerAddress.
    - #### getTransferToAddress

      ```
      public com.google.protobuf.ByteString getTransferToAddress()
      ```

      ```
       the one recieve trx (TBD: or token) via function
      ```

      `bytes transferTo_address = 3;`

      Specified by:
      :   `getTransferToAddress` in interface `Response.InternalTransactionOrBuilder`

      Returns:
      :   The transferToAddress.
    - #### getCallValueInfoList

      ```
      public java.util.List<Response.InternalTransaction.CallValueInfo> getCallValueInfoList()
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`

      Specified by:
      :   `getCallValueInfoList` in interface `Response.InternalTransactionOrBuilder`
    - #### getCallValueInfoOrBuilderList

      ```
      public java.util.List<? extends Response.InternalTransaction.CallValueInfoOrBuilder> getCallValueInfoOrBuilderList()
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`

      Specified by:
      :   `getCallValueInfoOrBuilderList` in interface `Response.InternalTransactionOrBuilder`
    - #### getCallValueInfoCount

      ```
      public int getCallValueInfoCount()
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`

      Specified by:
      :   `getCallValueInfoCount` in interface `Response.InternalTransactionOrBuilder`
    - #### getCallValueInfo

      ```
      public Response.InternalTransaction.CallValueInfo getCallValueInfo(int index)
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`

      Specified by:
      :   `getCallValueInfo` in interface `Response.InternalTransactionOrBuilder`
    - #### getCallValueInfoOrBuilder

      ```
      public Response.InternalTransaction.CallValueInfoOrBuilder getCallValueInfoOrBuilder(int index)
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`

      Specified by:
      :   `getCallValueInfoOrBuilder` in interface `Response.InternalTransactionOrBuilder`
    - #### getNote

      ```
      public com.google.protobuf.ByteString getNote()
      ```

      `bytes note = 5;`

      Specified by:
      :   `getNote` in interface `Response.InternalTransactionOrBuilder`

      Returns:
      :   The note.
    - #### getRejected

      ```
      public boolean getRejected()
      ```

      `bool rejected = 6;`

      Specified by:
      :   `getRejected` in interface `Response.InternalTransactionOrBuilder`

      Returns:
      :   The rejected.
    - #### getExtra

      ```
      public java.lang.String getExtra()
      ```

      `string extra = 7;`

      Specified by:
      :   `getExtra` in interface `Response.InternalTransactionOrBuilder`

      Returns:
      :   The extra.
    - #### getExtraBytes

      ```
      public com.google.protobuf.ByteString getExtraBytes()
      ```

      `string extra = 7;`

      Specified by:
      :   `getExtraBytes` in interface `Response.InternalTransactionOrBuilder`

      Returns:
      :   The bytes for extra.
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
      public static Response.InternalTransaction parseFrom(java.nio.ByteBuffer data)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.InternalTransaction parseFrom(java.nio.ByteBuffer data,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.InternalTransaction parseFrom(com.google.protobuf.ByteString data)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.InternalTransaction parseFrom(com.google.protobuf.ByteString data,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.InternalTransaction parseFrom(byte[] data)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.InternalTransaction parseFrom(byte[] data,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.InternalTransaction parseFrom(java.io.InputStream input)
                                                    throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.InternalTransaction parseFrom(java.io.InputStream input,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.InternalTransaction parseDelimitedFrom(java.io.InputStream input)
                                                             throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.InternalTransaction parseDelimitedFrom(java.io.InputStream input,
                                                                    com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                             throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.InternalTransaction parseFrom(com.google.protobuf.CodedInputStream input)
                                                    throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.InternalTransaction parseFrom(com.google.protobuf.CodedInputStream input,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.InternalTransaction.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.InternalTransaction.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.InternalTransaction.Builder newBuilder(Response.InternalTransaction prototype)
      ```
    - #### toBuilder

      ```
      public Response.InternalTransaction.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.InternalTransaction.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.InternalTransaction getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.InternalTransaction> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.InternalTransaction> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.InternalTransaction getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`