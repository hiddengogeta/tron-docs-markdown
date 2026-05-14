

org.tron.trident.proto

## Class Response.Witness

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.Witness

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.WitnessOrBuilder](../../../../org/tron/trident/proto/Response.WitnessOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.Witness
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.WitnessOrBuilder
  ```

  ```
   Witness
  ```

  Protobuf type `protocol.Witness`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.Witness)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.Witness.Builder` Witness |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `ADDRESS_FIELD_NUMBER` |
    | `static int` | `ISJOBS_FIELD_NUMBER` |
    | `static int` | `LATESTBLOCKNUM_FIELD_NUMBER` |
    | `static int` | `LATESTSLOTNUM_FIELD_NUMBER` |
    | `static int` | `PUBKEY_FIELD_NUMBER` |
    | `static int` | `TOTALMISSED_FIELD_NUMBER` |
    | `static int` | `TOTALPRODUCED_FIELD_NUMBER` |
    | `static int` | `URL_FIELD_NUMBER` |
    | `static int` | `VOTECOUNT_FIELD_NUMBER` |

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
    | `com.google.protobuf.ByteString` | `getAddress()` `bytes address = 1;` |
    | `static Response.Witness` | `getDefaultInstance()` |
    | `Response.Witness` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `boolean` | `getIsJobs()` `bool isJobs = 9;` |
    | `long` | `getLatestBlockNum()` `int64 latestBlockNum = 7;` |
    | `long` | `getLatestSlotNum()` `int64 latestSlotNum = 8;` |
    | `com.google.protobuf.Parser<Response.Witness>` | `getParserForType()` |
    | `com.google.protobuf.ByteString` | `getPubKey()` `bytes pubKey = 3;` |
    | `int` | `getSerializedSize()` |
    | `long` | `getTotalMissed()` `int64 totalMissed = 6;` |
    | `long` | `getTotalProduced()` `int64 totalProduced = 5;` |
    | `java.lang.String` | `getUrl()` `string url = 4;` |
    | `com.google.protobuf.ByteString` | `getUrlBytes()` `string url = 4;` |
    | `long` | `getVoteCount()` `int64 voteCount = 2;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Response.Witness.Builder` | `newBuilder()` |
    | `static Response.Witness.Builder` | `newBuilder(Response.Witness prototype)` |
    | `Response.Witness.Builder` | `newBuilderForType()` |
    | `protected Response.Witness.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.Witness` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.Witness` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Witness` | `parseFrom(byte[] data)` |
    | `static Response.Witness` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Witness` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.Witness` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Witness` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.Witness` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Witness` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.Witness` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Witness` | `parseFrom(java.io.InputStream input)` |
    | `static Response.Witness` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.Witness>` | `parser()` |
    | `Response.Witness.Builder` | `toBuilder()` |
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

    - #### ADDRESS\_FIELD\_NUMBER

      ```
      public static final int ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Witness.ADDRESS_FIELD_NUMBER)
    - #### VOTECOUNT\_FIELD\_NUMBER

      ```
      public static final int VOTECOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Witness.VOTECOUNT_FIELD_NUMBER)
    - #### PUBKEY\_FIELD\_NUMBER

      ```
      public static final int PUBKEY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Witness.PUBKEY_FIELD_NUMBER)
    - #### URL\_FIELD\_NUMBER

      ```
      public static final int URL_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Witness.URL_FIELD_NUMBER)
    - #### TOTALPRODUCED\_FIELD\_NUMBER

      ```
      public static final int TOTALPRODUCED_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Witness.TOTALPRODUCED_FIELD_NUMBER)
    - #### TOTALMISSED\_FIELD\_NUMBER

      ```
      public static final int TOTALMISSED_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Witness.TOTALMISSED_FIELD_NUMBER)
    - #### LATESTBLOCKNUM\_FIELD\_NUMBER

      ```
      public static final int LATESTBLOCKNUM_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Witness.LATESTBLOCKNUM_FIELD_NUMBER)
    - #### LATESTSLOTNUM\_FIELD\_NUMBER

      ```
      public static final int LATESTSLOTNUM_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Witness.LATESTSLOTNUM_FIELD_NUMBER)
    - #### ISJOBS\_FIELD\_NUMBER

      ```
      public static final int ISJOBS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Witness.ISJOBS_FIELD_NUMBER)
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
    - #### getAddress

      ```
      public com.google.protobuf.ByteString getAddress()
      ```

      `bytes address = 1;`

      Specified by:
      :   `getAddress` in interface `Response.WitnessOrBuilder`

      Returns:
      :   The address.
    - #### getVoteCount

      ```
      public long getVoteCount()
      ```

      `int64 voteCount = 2;`

      Specified by:
      :   `getVoteCount` in interface `Response.WitnessOrBuilder`

      Returns:
      :   The voteCount.
    - #### getPubKey

      ```
      public com.google.protobuf.ByteString getPubKey()
      ```

      `bytes pubKey = 3;`

      Specified by:
      :   `getPubKey` in interface `Response.WitnessOrBuilder`

      Returns:
      :   The pubKey.
    - #### getUrl

      ```
      public java.lang.String getUrl()
      ```

      `string url = 4;`

      Specified by:
      :   `getUrl` in interface `Response.WitnessOrBuilder`

      Returns:
      :   The url.
    - #### getUrlBytes

      ```
      public com.google.protobuf.ByteString getUrlBytes()
      ```

      `string url = 4;`

      Specified by:
      :   `getUrlBytes` in interface `Response.WitnessOrBuilder`

      Returns:
      :   The bytes for url.
    - #### getTotalProduced

      ```
      public long getTotalProduced()
      ```

      `int64 totalProduced = 5;`

      Specified by:
      :   `getTotalProduced` in interface `Response.WitnessOrBuilder`

      Returns:
      :   The totalProduced.
    - #### getTotalMissed

      ```
      public long getTotalMissed()
      ```

      `int64 totalMissed = 6;`

      Specified by:
      :   `getTotalMissed` in interface `Response.WitnessOrBuilder`

      Returns:
      :   The totalMissed.
    - #### getLatestBlockNum

      ```
      public long getLatestBlockNum()
      ```

      `int64 latestBlockNum = 7;`

      Specified by:
      :   `getLatestBlockNum` in interface `Response.WitnessOrBuilder`

      Returns:
      :   The latestBlockNum.
    - #### getLatestSlotNum

      ```
      public long getLatestSlotNum()
      ```

      `int64 latestSlotNum = 8;`

      Specified by:
      :   `getLatestSlotNum` in interface `Response.WitnessOrBuilder`

      Returns:
      :   The latestSlotNum.
    - #### getIsJobs

      ```
      public boolean getIsJobs()
      ```

      `bool isJobs = 9;`

      Specified by:
      :   `getIsJobs` in interface `Response.WitnessOrBuilder`

      Returns:
      :   The isJobs.
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
      public static Response.Witness parseFrom(java.nio.ByteBuffer data)
                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Witness parseFrom(java.nio.ByteBuffer data,
                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Witness parseFrom(com.google.protobuf.ByteString data)
                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Witness parseFrom(com.google.protobuf.ByteString data,
                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Witness parseFrom(byte[] data)
                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Witness parseFrom(byte[] data,
                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Witness parseFrom(java.io.InputStream input)
                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.Witness parseFrom(java.io.InputStream input,
                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.Witness parseDelimitedFrom(java.io.InputStream input)
                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.Witness parseDelimitedFrom(java.io.InputStream input,
                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.Witness parseFrom(com.google.protobuf.CodedInputStream input)
                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.Witness parseFrom(com.google.protobuf.CodedInputStream input,
                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.Witness.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.Witness.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.Witness.Builder newBuilder(Response.Witness prototype)
      ```
    - #### toBuilder

      ```
      public Response.Witness.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.Witness.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.Witness getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.Witness> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.Witness> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.Witness getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`