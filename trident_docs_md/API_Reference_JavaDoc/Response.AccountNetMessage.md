

org.tron.trident.proto

## Class Response.AccountNetMessage

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.AccountNetMessage

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.AccountNetMessageOrBuilder](../../../../org/tron/trident/proto/Response.AccountNetMessageOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.AccountNetMessage
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.AccountNetMessageOrBuilder
  ```

  ```
   deprecated
  ```

  Protobuf type `protocol.AccountNetMessage`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.AccountNetMessage)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.AccountNetMessage.Builder` deprecated |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `ASSETNETLIMIT_FIELD_NUMBER` |
    | `static int` | `ASSETNETUSED_FIELD_NUMBER` |
    | `static int` | `FREENETLIMIT_FIELD_NUMBER` |
    | `static int` | `FREENETUSED_FIELD_NUMBER` |
    | `static int` | `NETLIMIT_FIELD_NUMBER` |
    | `static int` | `NETUSED_FIELD_NUMBER` |
    | `static int` | `TOTALNETLIMIT_FIELD_NUMBER` |
    | `static int` | `TOTALNETWEIGHT_FIELD_NUMBER` |

    - ### Fields inherited from class com.google.protobuf.GeneratedMessageV3

      `alwaysUseFieldBuilders, unknownFields`
    - ### Fields inherited from class com.google.protobuf.AbstractMessage

      `memoizedSize`
    - ### Fields inherited from class com.google.protobuf.AbstractMessageLite

      `memoizedHashCode`
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `boolean` | `containsAssetNetLimit(java.lang.String key)` `map<string, int64> assetNetLimit = 6;` |
    | `boolean` | `containsAssetNetUsed(java.lang.String key)` `map<string, int64> assetNetUsed = 5;` |
    | `boolean` | `equals(java.lang.Object obj)` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getAssetNetLimit()` Deprecated. |
    | `int` | `getAssetNetLimitCount()` `map<string, int64> assetNetLimit = 6;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getAssetNetLimitMap()` `map<string, int64> assetNetLimit = 6;` |
    | `long` | `getAssetNetLimitOrDefault(java.lang.String key, long defaultValue)` `map<string, int64> assetNetLimit = 6;` |
    | `long` | `getAssetNetLimitOrThrow(java.lang.String key)` `map<string, int64> assetNetLimit = 6;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getAssetNetUsed()` Deprecated. |
    | `int` | `getAssetNetUsedCount()` `map<string, int64> assetNetUsed = 5;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getAssetNetUsedMap()` `map<string, int64> assetNetUsed = 5;` |
    | `long` | `getAssetNetUsedOrDefault(java.lang.String key, long defaultValue)` `map<string, int64> assetNetUsed = 5;` |
    | `long` | `getAssetNetUsedOrThrow(java.lang.String key)` `map<string, int64> assetNetUsed = 5;` |
    | `static Response.AccountNetMessage` | `getDefaultInstance()` |
    | `Response.AccountNetMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `long` | `getFreeNetLimit()` `int64 freeNetLimit = 2;` |
    | `long` | `getFreeNetUsed()` `int64 freeNetUsed = 1;` |
    | `long` | `getNetLimit()` `int64 NetLimit = 4;` |
    | `long` | `getNetUsed()` `int64 NetUsed = 3;` |
    | `com.google.protobuf.Parser<Response.AccountNetMessage>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `long` | `getTotalNetLimit()` `int64 TotalNetLimit = 7;` |
    | `long` | `getTotalNetWeight()` `int64 TotalNetWeight = 8;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMapFieldReflection(int number)` |
    | `boolean` | `isInitialized()` |
    | `static Response.AccountNetMessage.Builder` | `newBuilder()` |
    | `static Response.AccountNetMessage.Builder` | `newBuilder(Response.AccountNetMessage prototype)` |
    | `Response.AccountNetMessage.Builder` | `newBuilderForType()` |
    | `protected Response.AccountNetMessage.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.AccountNetMessage` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.AccountNetMessage` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.AccountNetMessage` | `parseFrom(byte[] data)` |
    | `static Response.AccountNetMessage` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.AccountNetMessage` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.AccountNetMessage` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.AccountNetMessage` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.AccountNetMessage` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.AccountNetMessage` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.AccountNetMessage` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.AccountNetMessage` | `parseFrom(java.io.InputStream input)` |
    | `static Response.AccountNetMessage` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.AccountNetMessage>` | `parser()` |
    | `Response.AccountNetMessage.Builder` | `toBuilder()` |
    | `void` | `writeTo(com.google.protobuf.CodedOutputStream output)` |

    - ### Methods inherited from class com.google.protobuf.GeneratedMessageV3

      `canUseUnsafe, computeStringSize, computeStringSizeNoTag, emptyBooleanList, emptyDoubleList, emptyFloatList, emptyIntList, emptyList, emptyLongList, getAllFields, getDescriptorForType, getField, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof, internalGetMapField, isStringEmpty, makeExtensionsImmutable, makeMutableCopy, makeMutableCopy, mergeFromAndMakeImmutableInternal, mutableCopy, mutableCopy, mutableCopy, mutableCopy, mutableCopy, newBooleanList, newBuilderForType, newDoubleList, newFloatList, newIntList, newLongList, parseDelimitedWithIOException, parseDelimitedWithIOException, parseUnknownField, parseUnknownFieldProto3, parseWithIOException, parseWithIOException, parseWithIOException, parseWithIOException, serializeBooleanMapTo, serializeIntegerMapTo, serializeLongMapTo, serializeStringMapTo, writeReplace, writeString, writeStringNoTag`
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

    - #### FREENETUSED\_FIELD\_NUMBER

      ```
      public static final int FREENETUSED_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountNetMessage.FREENETUSED_FIELD_NUMBER)
    - #### FREENETLIMIT\_FIELD\_NUMBER

      ```
      public static final int FREENETLIMIT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountNetMessage.FREENETLIMIT_FIELD_NUMBER)
    - #### NETUSED\_FIELD\_NUMBER

      ```
      public static final int NETUSED_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountNetMessage.NETUSED_FIELD_NUMBER)
    - #### NETLIMIT\_FIELD\_NUMBER

      ```
      public static final int NETLIMIT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountNetMessage.NETLIMIT_FIELD_NUMBER)
    - #### ASSETNETUSED\_FIELD\_NUMBER

      ```
      public static final int ASSETNETUSED_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountNetMessage.ASSETNETUSED_FIELD_NUMBER)
    - #### ASSETNETLIMIT\_FIELD\_NUMBER

      ```
      public static final int ASSETNETLIMIT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountNetMessage.ASSETNETLIMIT_FIELD_NUMBER)
    - #### TOTALNETLIMIT\_FIELD\_NUMBER

      ```
      public static final int TOTALNETLIMIT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountNetMessage.TOTALNETLIMIT_FIELD_NUMBER)
    - #### TOTALNETWEIGHT\_FIELD\_NUMBER

      ```
      public static final int TOTALNETWEIGHT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountNetMessage.TOTALNETWEIGHT_FIELD_NUMBER)
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
    - #### internalGetMapFieldReflection

      ```
      protected com.google.protobuf.MapFieldReflectionAccessor internalGetMapFieldReflection(int number)
      ```

      Overrides:
      :   `internalGetMapFieldReflection` in class `com.google.protobuf.GeneratedMessageV3`
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getFreeNetUsed

      ```
      public long getFreeNetUsed()
      ```

      `int64 freeNetUsed = 1;`

      Specified by:
      :   `getFreeNetUsed` in interface `Response.AccountNetMessageOrBuilder`

      Returns:
      :   The freeNetUsed.
    - #### getFreeNetLimit

      ```
      public long getFreeNetLimit()
      ```

      `int64 freeNetLimit = 2;`

      Specified by:
      :   `getFreeNetLimit` in interface `Response.AccountNetMessageOrBuilder`

      Returns:
      :   The freeNetLimit.
    - #### getNetUsed

      ```
      public long getNetUsed()
      ```

      `int64 NetUsed = 3;`

      Specified by:
      :   `getNetUsed` in interface `Response.AccountNetMessageOrBuilder`

      Returns:
      :   The netUsed.
    - #### getNetLimit

      ```
      public long getNetLimit()
      ```

      `int64 NetLimit = 4;`

      Specified by:
      :   `getNetLimit` in interface `Response.AccountNetMessageOrBuilder`

      Returns:
      :   The netLimit.
    - #### getAssetNetUsedCount

      ```
      public int getAssetNetUsedCount()
      ```

      Description copied from interface: `Response.AccountNetMessageOrBuilder`

      `map<string, int64> assetNetUsed = 5;`

      Specified by:
      :   `getAssetNetUsedCount` in interface `Response.AccountNetMessageOrBuilder`
    - #### containsAssetNetUsed

      ```
      public boolean containsAssetNetUsed(java.lang.String key)
      ```

      `map<string, int64> assetNetUsed = 5;`

      Specified by:
      :   `containsAssetNetUsed` in interface `Response.AccountNetMessageOrBuilder`
    - #### getAssetNetUsed

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getAssetNetUsed()
      ```

      Deprecated.

      Use [`getAssetNetUsedMap()`](../../../../org/tron/trident/proto/Response.AccountNetMessage.html#getAssetNetUsedMap--) instead.

      Specified by:
      :   `getAssetNetUsed` in interface `Response.AccountNetMessageOrBuilder`
    - #### getAssetNetUsedMap

      ```
      public java.util.Map<java.lang.String,java.lang.Long> getAssetNetUsedMap()
      ```

      `map<string, int64> assetNetUsed = 5;`

      Specified by:
      :   `getAssetNetUsedMap` in interface `Response.AccountNetMessageOrBuilder`
    - #### getAssetNetUsedOrDefault

      ```
      public long getAssetNetUsedOrDefault(java.lang.String key,
                                           long defaultValue)
      ```

      `map<string, int64> assetNetUsed = 5;`

      Specified by:
      :   `getAssetNetUsedOrDefault` in interface `Response.AccountNetMessageOrBuilder`
    - #### getAssetNetUsedOrThrow

      ```
      public long getAssetNetUsedOrThrow(java.lang.String key)
      ```

      `map<string, int64> assetNetUsed = 5;`

      Specified by:
      :   `getAssetNetUsedOrThrow` in interface `Response.AccountNetMessageOrBuilder`
    - #### getAssetNetLimitCount

      ```
      public int getAssetNetLimitCount()
      ```

      Description copied from interface: `Response.AccountNetMessageOrBuilder`

      `map<string, int64> assetNetLimit = 6;`

      Specified by:
      :   `getAssetNetLimitCount` in interface `Response.AccountNetMessageOrBuilder`
    - #### containsAssetNetLimit

      ```
      public boolean containsAssetNetLimit(java.lang.String key)
      ```

      `map<string, int64> assetNetLimit = 6;`

      Specified by:
      :   `containsAssetNetLimit` in interface `Response.AccountNetMessageOrBuilder`
    - #### getAssetNetLimit

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getAssetNetLimit()
      ```

      Deprecated.

      Use [`getAssetNetLimitMap()`](../../../../org/tron/trident/proto/Response.AccountNetMessage.html#getAssetNetLimitMap--) instead.

      Specified by:
      :   `getAssetNetLimit` in interface `Response.AccountNetMessageOrBuilder`
    - #### getAssetNetLimitMap

      ```
      public java.util.Map<java.lang.String,java.lang.Long> getAssetNetLimitMap()
      ```

      `map<string, int64> assetNetLimit = 6;`

      Specified by:
      :   `getAssetNetLimitMap` in interface `Response.AccountNetMessageOrBuilder`
    - #### getAssetNetLimitOrDefault

      ```
      public long getAssetNetLimitOrDefault(java.lang.String key,
                                            long defaultValue)
      ```

      `map<string, int64> assetNetLimit = 6;`

      Specified by:
      :   `getAssetNetLimitOrDefault` in interface `Response.AccountNetMessageOrBuilder`
    - #### getAssetNetLimitOrThrow

      ```
      public long getAssetNetLimitOrThrow(java.lang.String key)
      ```

      `map<string, int64> assetNetLimit = 6;`

      Specified by:
      :   `getAssetNetLimitOrThrow` in interface `Response.AccountNetMessageOrBuilder`
    - #### getTotalNetLimit

      ```
      public long getTotalNetLimit()
      ```

      `int64 TotalNetLimit = 7;`

      Specified by:
      :   `getTotalNetLimit` in interface `Response.AccountNetMessageOrBuilder`

      Returns:
      :   The totalNetLimit.
    - #### getTotalNetWeight

      ```
      public long getTotalNetWeight()
      ```

      `int64 TotalNetWeight = 8;`

      Specified by:
      :   `getTotalNetWeight` in interface `Response.AccountNetMessageOrBuilder`

      Returns:
      :   The totalNetWeight.
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
      public static Response.AccountNetMessage parseFrom(java.nio.ByteBuffer data)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.AccountNetMessage parseFrom(java.nio.ByteBuffer data,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.AccountNetMessage parseFrom(com.google.protobuf.ByteString data)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.AccountNetMessage parseFrom(com.google.protobuf.ByteString data,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.AccountNetMessage parseFrom(byte[] data)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.AccountNetMessage parseFrom(byte[] data,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.AccountNetMessage parseFrom(java.io.InputStream input)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.AccountNetMessage parseFrom(java.io.InputStream input,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.AccountNetMessage parseDelimitedFrom(java.io.InputStream input)
                                                           throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.AccountNetMessage parseDelimitedFrom(java.io.InputStream input,
                                                                  com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                           throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.AccountNetMessage parseFrom(com.google.protobuf.CodedInputStream input)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.AccountNetMessage parseFrom(com.google.protobuf.CodedInputStream input,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.AccountNetMessage.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.AccountNetMessage.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.AccountNetMessage.Builder newBuilder(Response.AccountNetMessage prototype)
      ```
    - #### toBuilder

      ```
      public Response.AccountNetMessage.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.AccountNetMessage.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.AccountNetMessage getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.AccountNetMessage> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.AccountNetMessage> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.AccountNetMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`