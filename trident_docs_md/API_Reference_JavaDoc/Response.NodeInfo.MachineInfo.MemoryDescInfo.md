

org.tron.trident.proto

## Class Response.NodeInfo.MachineInfo.MemoryDescInfo

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.NodeInfo.MachineInfo.MemoryDescInfo

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder](../../../../org/tron/trident/proto/Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.NodeInfo.MachineInfo](../../../../org/tron/trident/proto/Response.NodeInfo.MachineInfo.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.NodeInfo.MachineInfo.MemoryDescInfo
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder
  ```

  Protobuf type `protocol.NodeInfo.MachineInfo.MemoryDescInfo`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.MemoryDescInfo)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` Protobuf type `protocol.NodeInfo.MachineInfo.MemoryDescInfo` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `INITSIZE_FIELD_NUMBER` |
    | `static int` | `MAXSIZE_FIELD_NUMBER` |
    | `static int` | `NAME_FIELD_NUMBER` |
    | `static int` | `USERATE_FIELD_NUMBER` |
    | `static int` | `USESIZE_FIELD_NUMBER` |

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
    | `static Response.NodeInfo.MachineInfo.MemoryDescInfo` | `getDefaultInstance()` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `long` | `getInitSize()` `int64 initSize = 2;` |
    | `long` | `getMaxSize()` `int64 maxSize = 4;` |
    | `java.lang.String` | `getName()` `string name = 1;` |
    | `com.google.protobuf.ByteString` | `getNameBytes()` `string name = 1;` |
    | `com.google.protobuf.Parser<Response.NodeInfo.MachineInfo.MemoryDescInfo>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `double` | `getUseRate()` `double useRate = 5;` |
    | `long` | `getUseSize()` `int64 useSize = 3;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `newBuilder()` |
    | `static Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `newBuilder(Response.NodeInfo.MachineInfo.MemoryDescInfo prototype)` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `newBuilderForType()` |
    | `protected Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.NodeInfo.MachineInfo.MemoryDescInfo` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.NodeInfo.MachineInfo.MemoryDescInfo` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.MachineInfo.MemoryDescInfo` | `parseFrom(byte[] data)` |
    | `static Response.NodeInfo.MachineInfo.MemoryDescInfo` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.MachineInfo.MemoryDescInfo` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.NodeInfo.MachineInfo.MemoryDescInfo` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.MachineInfo.MemoryDescInfo` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.NodeInfo.MachineInfo.MemoryDescInfo` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.MachineInfo.MemoryDescInfo` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.NodeInfo.MachineInfo.MemoryDescInfo` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.MachineInfo.MemoryDescInfo` | `parseFrom(java.io.InputStream input)` |
    | `static Response.NodeInfo.MachineInfo.MemoryDescInfo` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.NodeInfo.MachineInfo.MemoryDescInfo>` | `parser()` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `toBuilder()` |
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

    - #### NAME\_FIELD\_NUMBER

      ```
      public static final int NAME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.MemoryDescInfo.NAME_FIELD_NUMBER)
    - #### INITSIZE\_FIELD\_NUMBER

      ```
      public static final int INITSIZE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.MemoryDescInfo.INITSIZE_FIELD_NUMBER)
    - #### USESIZE\_FIELD\_NUMBER

      ```
      public static final int USESIZE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.MemoryDescInfo.USESIZE_FIELD_NUMBER)
    - #### MAXSIZE\_FIELD\_NUMBER

      ```
      public static final int MAXSIZE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.MemoryDescInfo.MAXSIZE_FIELD_NUMBER)
    - #### USERATE\_FIELD\_NUMBER

      ```
      public static final int USERATE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.MemoryDescInfo.USERATE_FIELD_NUMBER)
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
    - #### getName

      ```
      public java.lang.String getName()
      ```

      `string name = 1;`

      Specified by:
      :   `getName` in interface `Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder`

      Returns:
      :   The name.
    - #### getNameBytes

      ```
      public com.google.protobuf.ByteString getNameBytes()
      ```

      `string name = 1;`

      Specified by:
      :   `getNameBytes` in interface `Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder`

      Returns:
      :   The bytes for name.
    - #### getInitSize

      ```
      public long getInitSize()
      ```

      `int64 initSize = 2;`

      Specified by:
      :   `getInitSize` in interface `Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder`

      Returns:
      :   The initSize.
    - #### getUseSize

      ```
      public long getUseSize()
      ```

      `int64 useSize = 3;`

      Specified by:
      :   `getUseSize` in interface `Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder`

      Returns:
      :   The useSize.
    - #### getMaxSize

      ```
      public long getMaxSize()
      ```

      `int64 maxSize = 4;`

      Specified by:
      :   `getMaxSize` in interface `Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder`

      Returns:
      :   The maxSize.
    - #### getUseRate

      ```
      public double getUseRate()
      ```

      `double useRate = 5;`

      Specified by:
      :   `getUseRate` in interface `Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder`

      Returns:
      :   The useRate.
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
      public static Response.NodeInfo.MachineInfo.MemoryDescInfo parseFrom(java.nio.ByteBuffer data)
                                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo.MemoryDescInfo parseFrom(java.nio.ByteBuffer data,
                                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo.MemoryDescInfo parseFrom(com.google.protobuf.ByteString data)
                                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo.MemoryDescInfo parseFrom(com.google.protobuf.ByteString data,
                                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo.MemoryDescInfo parseFrom(byte[] data)
                                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo.MemoryDescInfo parseFrom(byte[] data,
                                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo.MemoryDescInfo parseFrom(java.io.InputStream input)
                                                                    throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo.MemoryDescInfo parseFrom(java.io.InputStream input,
                                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                    throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.NodeInfo.MachineInfo.MemoryDescInfo parseDelimitedFrom(java.io.InputStream input)
                                                                             throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.NodeInfo.MachineInfo.MemoryDescInfo parseDelimitedFrom(java.io.InputStream input,
                                                                                    com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                             throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo.MemoryDescInfo parseFrom(com.google.protobuf.CodedInputStream input)
                                                                    throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo.MemoryDescInfo parseFrom(com.google.protobuf.CodedInputStream input,
                                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                    throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder newBuilder(Response.NodeInfo.MachineInfo.MemoryDescInfo prototype)
      ```
    - #### toBuilder

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.NodeInfo.MachineInfo.MemoryDescInfo getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.NodeInfo.MachineInfo.MemoryDescInfo> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.NodeInfo.MachineInfo.MemoryDescInfo> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`