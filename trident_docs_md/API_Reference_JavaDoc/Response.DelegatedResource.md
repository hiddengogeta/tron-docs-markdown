

org.tron.trident.proto

## Class Response.DelegatedResource

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.DelegatedResource

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.DelegatedResourceOrBuilder](../../../../org/tron/trident/proto/Response.DelegatedResourceOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.DelegatedResource
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.DelegatedResourceOrBuilder
  ```

  Protobuf type `protocol.DelegatedResource`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.DelegatedResource)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.DelegatedResource.Builder` Protobuf type `protocol.DelegatedResource` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `EXPIRE_TIME_FOR_BANDWIDTH_FIELD_NUMBER` |
    | `static int` | `EXPIRE_TIME_FOR_ENERGY_FIELD_NUMBER` |
    | `static int` | `FROM_FIELD_NUMBER` |
    | `static int` | `FROZEN_BALANCE_FOR_BANDWIDTH_FIELD_NUMBER` |
    | `static int` | `FROZEN_BALANCE_FOR_ENERGY_FIELD_NUMBER` |
    | `static int` | `TO_FIELD_NUMBER` |

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
    | `static Response.DelegatedResource` | `getDefaultInstance()` |
    | `Response.DelegatedResource` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `long` | `getExpireTimeForBandwidth()` `int64 expire_time_for_bandwidth = 5;` |
    | `long` | `getExpireTimeForEnergy()` `int64 expire_time_for_energy = 6;` |
    | `com.google.protobuf.ByteString` | `getFrom()` `bytes from = 1;` |
    | `long` | `getFrozenBalanceForBandwidth()` `int64 frozen_balance_for_bandwidth = 3;` |
    | `long` | `getFrozenBalanceForEnergy()` `int64 frozen_balance_for_energy = 4;` |
    | `com.google.protobuf.Parser<Response.DelegatedResource>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `com.google.protobuf.ByteString` | `getTo()` `bytes to = 2;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Response.DelegatedResource.Builder` | `newBuilder()` |
    | `static Response.DelegatedResource.Builder` | `newBuilder(Response.DelegatedResource prototype)` |
    | `Response.DelegatedResource.Builder` | `newBuilderForType()` |
    | `protected Response.DelegatedResource.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.DelegatedResource` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.DelegatedResource` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.DelegatedResource` | `parseFrom(byte[] data)` |
    | `static Response.DelegatedResource` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.DelegatedResource` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.DelegatedResource` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.DelegatedResource` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.DelegatedResource` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.DelegatedResource` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.DelegatedResource` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.DelegatedResource` | `parseFrom(java.io.InputStream input)` |
    | `static Response.DelegatedResource` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.DelegatedResource>` | `parser()` |
    | `Response.DelegatedResource.Builder` | `toBuilder()` |
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

    - #### FROM\_FIELD\_NUMBER

      ```
      public static final int FROM_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.DelegatedResource.FROM_FIELD_NUMBER)
    - #### TO\_FIELD\_NUMBER

      ```
      public static final int TO_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.DelegatedResource.TO_FIELD_NUMBER)
    - #### FROZEN\_BALANCE\_FOR\_BANDWIDTH\_FIELD\_NUMBER

      ```
      public static final int FROZEN_BALANCE_FOR_BANDWIDTH_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.DelegatedResource.FROZEN_BALANCE_FOR_BANDWIDTH_FIELD_NUMBER)
    - #### FROZEN\_BALANCE\_FOR\_ENERGY\_FIELD\_NUMBER

      ```
      public static final int FROZEN_BALANCE_FOR_ENERGY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.DelegatedResource.FROZEN_BALANCE_FOR_ENERGY_FIELD_NUMBER)
    - #### EXPIRE\_TIME\_FOR\_BANDWIDTH\_FIELD\_NUMBER

      ```
      public static final int EXPIRE_TIME_FOR_BANDWIDTH_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.DelegatedResource.EXPIRE_TIME_FOR_BANDWIDTH_FIELD_NUMBER)
    - #### EXPIRE\_TIME\_FOR\_ENERGY\_FIELD\_NUMBER

      ```
      public static final int EXPIRE_TIME_FOR_ENERGY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.DelegatedResource.EXPIRE_TIME_FOR_ENERGY_FIELD_NUMBER)
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
    - #### getFrom

      ```
      public com.google.protobuf.ByteString getFrom()
      ```

      `bytes from = 1;`

      Specified by:
      :   `getFrom` in interface `Response.DelegatedResourceOrBuilder`

      Returns:
      :   The from.
    - #### getTo

      ```
      public com.google.protobuf.ByteString getTo()
      ```

      `bytes to = 2;`

      Specified by:
      :   `getTo` in interface `Response.DelegatedResourceOrBuilder`

      Returns:
      :   The to.
    - #### getFrozenBalanceForBandwidth

      ```
      public long getFrozenBalanceForBandwidth()
      ```

      `int64 frozen_balance_for_bandwidth = 3;`

      Specified by:
      :   `getFrozenBalanceForBandwidth` in interface `Response.DelegatedResourceOrBuilder`

      Returns:
      :   The frozenBalanceForBandwidth.
    - #### getFrozenBalanceForEnergy

      ```
      public long getFrozenBalanceForEnergy()
      ```

      `int64 frozen_balance_for_energy = 4;`

      Specified by:
      :   `getFrozenBalanceForEnergy` in interface `Response.DelegatedResourceOrBuilder`

      Returns:
      :   The frozenBalanceForEnergy.
    - #### getExpireTimeForBandwidth

      ```
      public long getExpireTimeForBandwidth()
      ```

      `int64 expire_time_for_bandwidth = 5;`

      Specified by:
      :   `getExpireTimeForBandwidth` in interface `Response.DelegatedResourceOrBuilder`

      Returns:
      :   The expireTimeForBandwidth.
    - #### getExpireTimeForEnergy

      ```
      public long getExpireTimeForEnergy()
      ```

      `int64 expire_time_for_energy = 6;`

      Specified by:
      :   `getExpireTimeForEnergy` in interface `Response.DelegatedResourceOrBuilder`

      Returns:
      :   The expireTimeForEnergy.
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
      public static Response.DelegatedResource parseFrom(java.nio.ByteBuffer data)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DelegatedResource parseFrom(java.nio.ByteBuffer data,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DelegatedResource parseFrom(com.google.protobuf.ByteString data)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DelegatedResource parseFrom(com.google.protobuf.ByteString data,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DelegatedResource parseFrom(byte[] data)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DelegatedResource parseFrom(byte[] data,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DelegatedResource parseFrom(java.io.InputStream input)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.DelegatedResource parseFrom(java.io.InputStream input,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.DelegatedResource parseDelimitedFrom(java.io.InputStream input)
                                                           throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.DelegatedResource parseDelimitedFrom(java.io.InputStream input,
                                                                  com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                           throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.DelegatedResource parseFrom(com.google.protobuf.CodedInputStream input)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.DelegatedResource parseFrom(com.google.protobuf.CodedInputStream input,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.DelegatedResource.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.DelegatedResource.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.DelegatedResource.Builder newBuilder(Response.DelegatedResource prototype)
      ```
    - #### toBuilder

      ```
      public Response.DelegatedResource.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.DelegatedResource.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.DelegatedResource getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.DelegatedResource> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.DelegatedResource> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.DelegatedResource getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`