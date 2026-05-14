

org.tron.trident.api

## Class GrpcAPI.IvkDecryptTRC20Parameters

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.api.GrpcAPI.IvkDecryptTRC20Parameters

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [GrpcAPI.IvkDecryptTRC20ParametersOrBuilder](../../../../org/tron/trident/api/GrpcAPI.IvkDecryptTRC20ParametersOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.IvkDecryptTRC20Parameters
  extends com.google.protobuf.GeneratedMessageV3
  implements GrpcAPI.IvkDecryptTRC20ParametersOrBuilder
  ```

  Protobuf type `protocol.IvkDecryptTRC20Parameters`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.api.GrpcAPI.IvkDecryptTRC20Parameters)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` Protobuf type `protocol.IvkDecryptTRC20Parameters` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `AK_FIELD_NUMBER` |
    | `static int` | `END_BLOCK_INDEX_FIELD_NUMBER` |
    | `static int` | `EVENTS_FIELD_NUMBER` |
    | `static int` | `IVK_FIELD_NUMBER` |
    | `static int` | `NK_FIELD_NUMBER` |
    | `static int` | `SHIELDED_TRC20_CONTRACT_ADDRESS_FIELD_NUMBER` |
    | `static int` | `START_BLOCK_INDEX_FIELD_NUMBER` |

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
    | `static GrpcAPI.IvkDecryptTRC20Parameters` | `getDefaultInstance()` |
    | `GrpcAPI.IvkDecryptTRC20Parameters` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `long` | `getEndBlockIndex()` `int64 end_block_index = 2;` |
    | `java.lang.String` | `getEvents(int index)` `repeated string events = 7;` |
    | `com.google.protobuf.ByteString` | `getEventsBytes(int index)` `repeated string events = 7;` |
    | `int` | `getEventsCount()` `repeated string events = 7;` |
    | `com.google.protobuf.ProtocolStringList` | `getEventsList()` `repeated string events = 7;` |
    | `com.google.protobuf.ByteString` | `getIvk()` `bytes ivk = 4;` |
    | `com.google.protobuf.ByteString` | `getNk()` `bytes nk = 6;` |
    | `com.google.protobuf.Parser<GrpcAPI.IvkDecryptTRC20Parameters>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `com.google.protobuf.ByteString` | `getShieldedTRC20ContractAddress()` `bytes shielded_TRC20_contract_address = 3;` |
    | `long` | `getStartBlockIndex()` `int64 start_block_index = 1;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `newBuilder()` |
    | `static GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `newBuilder(GrpcAPI.IvkDecryptTRC20Parameters prototype)` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `newBuilderForType()` |
    | `protected GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static GrpcAPI.IvkDecryptTRC20Parameters` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static GrpcAPI.IvkDecryptTRC20Parameters` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.IvkDecryptTRC20Parameters` | `parseFrom(byte[] data)` |
    | `static GrpcAPI.IvkDecryptTRC20Parameters` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.IvkDecryptTRC20Parameters` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static GrpcAPI.IvkDecryptTRC20Parameters` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.IvkDecryptTRC20Parameters` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static GrpcAPI.IvkDecryptTRC20Parameters` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.IvkDecryptTRC20Parameters` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static GrpcAPI.IvkDecryptTRC20Parameters` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static GrpcAPI.IvkDecryptTRC20Parameters` | `parseFrom(java.io.InputStream input)` |
    | `static GrpcAPI.IvkDecryptTRC20Parameters` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<GrpcAPI.IvkDecryptTRC20Parameters>` | `parser()` |
    | `GrpcAPI.IvkDecryptTRC20Parameters.Builder` | `toBuilder()` |
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

    - #### START\_BLOCK\_INDEX\_FIELD\_NUMBER

      ```
      public static final int START_BLOCK_INDEX_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.IvkDecryptTRC20Parameters.START_BLOCK_INDEX_FIELD_NUMBER)
    - #### END\_BLOCK\_INDEX\_FIELD\_NUMBER

      ```
      public static final int END_BLOCK_INDEX_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.IvkDecryptTRC20Parameters.END_BLOCK_INDEX_FIELD_NUMBER)
    - #### SHIELDED\_TRC20\_CONTRACT\_ADDRESS\_FIELD\_NUMBER

      ```
      public static final int SHIELDED_TRC20_CONTRACT_ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.IvkDecryptTRC20Parameters.SHIELDED_TRC20_CONTRACT_ADDRESS_FIELD_NUMBER)
    - #### IVK\_FIELD\_NUMBER

      ```
      public static final int IVK_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.IvkDecryptTRC20Parameters.IVK_FIELD_NUMBER)
    - #### AK\_FIELD\_NUMBER

      ```
      public static final int AK_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.IvkDecryptTRC20Parameters.AK_FIELD_NUMBER)
    - #### NK\_FIELD\_NUMBER

      ```
      public static final int NK_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.IvkDecryptTRC20Parameters.NK_FIELD_NUMBER)
    - #### EVENTS\_FIELD\_NUMBER

      ```
      public static final int EVENTS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.api.GrpcAPI.IvkDecryptTRC20Parameters.EVENTS_FIELD_NUMBER)
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
    - #### getStartBlockIndex

      ```
      public long getStartBlockIndex()
      ```

      `int64 start_block_index = 1;`

      Specified by:
      :   `getStartBlockIndex` in interface `GrpcAPI.IvkDecryptTRC20ParametersOrBuilder`

      Returns:
      :   The startBlockIndex.
    - #### getEndBlockIndex

      ```
      public long getEndBlockIndex()
      ```

      `int64 end_block_index = 2;`

      Specified by:
      :   `getEndBlockIndex` in interface `GrpcAPI.IvkDecryptTRC20ParametersOrBuilder`

      Returns:
      :   The endBlockIndex.
    - #### getShieldedTRC20ContractAddress

      ```
      public com.google.protobuf.ByteString getShieldedTRC20ContractAddress()
      ```

      `bytes shielded_TRC20_contract_address = 3;`

      Specified by:
      :   `getShieldedTRC20ContractAddress` in interface `GrpcAPI.IvkDecryptTRC20ParametersOrBuilder`

      Returns:
      :   The shieldedTRC20ContractAddress.
    - #### getIvk

      ```
      public com.google.protobuf.ByteString getIvk()
      ```

      `bytes ivk = 4;`

      Specified by:
      :   `getIvk` in interface `GrpcAPI.IvkDecryptTRC20ParametersOrBuilder`

      Returns:
      :   The ivk.
    - #### getAk

      ```
      public com.google.protobuf.ByteString getAk()
      ```

      `bytes ak = 5;`

      Specified by:
      :   `getAk` in interface `GrpcAPI.IvkDecryptTRC20ParametersOrBuilder`

      Returns:
      :   The ak.
    - #### getNk

      ```
      public com.google.protobuf.ByteString getNk()
      ```

      `bytes nk = 6;`

      Specified by:
      :   `getNk` in interface `GrpcAPI.IvkDecryptTRC20ParametersOrBuilder`

      Returns:
      :   The nk.
    - #### getEventsList

      ```
      public com.google.protobuf.ProtocolStringList getEventsList()
      ```

      `repeated string events = 7;`

      Specified by:
      :   `getEventsList` in interface `GrpcAPI.IvkDecryptTRC20ParametersOrBuilder`

      Returns:
      :   A list containing the events.
    - #### getEventsCount

      ```
      public int getEventsCount()
      ```

      `repeated string events = 7;`

      Specified by:
      :   `getEventsCount` in interface `GrpcAPI.IvkDecryptTRC20ParametersOrBuilder`

      Returns:
      :   The count of events.
    - #### getEvents

      ```
      public java.lang.String getEvents(int index)
      ```

      `repeated string events = 7;`

      Specified by:
      :   `getEvents` in interface `GrpcAPI.IvkDecryptTRC20ParametersOrBuilder`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The events at the given index.
    - #### getEventsBytes

      ```
      public com.google.protobuf.ByteString getEventsBytes(int index)
      ```

      `repeated string events = 7;`

      Specified by:
      :   `getEventsBytes` in interface `GrpcAPI.IvkDecryptTRC20ParametersOrBuilder`

      Parameters:
      :   `index` - The index of the value to return.

      Returns:
      :   The bytes of the events at the given index.
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
      public static GrpcAPI.IvkDecryptTRC20Parameters parseFrom(java.nio.ByteBuffer data)
                                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.IvkDecryptTRC20Parameters parseFrom(java.nio.ByteBuffer data,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.IvkDecryptTRC20Parameters parseFrom(com.google.protobuf.ByteString data)
                                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.IvkDecryptTRC20Parameters parseFrom(com.google.protobuf.ByteString data,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.IvkDecryptTRC20Parameters parseFrom(byte[] data)
                                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.IvkDecryptTRC20Parameters parseFrom(byte[] data,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static GrpcAPI.IvkDecryptTRC20Parameters parseFrom(java.io.InputStream input)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.IvkDecryptTRC20Parameters parseFrom(java.io.InputStream input,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static GrpcAPI.IvkDecryptTRC20Parameters parseDelimitedFrom(java.io.InputStream input)
                                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static GrpcAPI.IvkDecryptTRC20Parameters parseDelimitedFrom(java.io.InputStream input,
                                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.IvkDecryptTRC20Parameters parseFrom(com.google.protobuf.CodedInputStream input)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static GrpcAPI.IvkDecryptTRC20Parameters parseFrom(com.google.protobuf.CodedInputStream input,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static GrpcAPI.IvkDecryptTRC20Parameters.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static GrpcAPI.IvkDecryptTRC20Parameters.Builder newBuilder(GrpcAPI.IvkDecryptTRC20Parameters prototype)
      ```
    - #### toBuilder

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected GrpcAPI.IvkDecryptTRC20Parameters.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static GrpcAPI.IvkDecryptTRC20Parameters getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<GrpcAPI.IvkDecryptTRC20Parameters> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<GrpcAPI.IvkDecryptTRC20Parameters> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.IvkDecryptTRC20Parameters getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`