

org.tron.trident.proto

## Class Common.SmartContract.ABI

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Common.SmartContract.ABI

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Common.SmartContract.ABIOrBuilder](../../../../org/tron/trident/proto/Common.SmartContract.ABIOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Common.SmartContract](../../../../org/tron/trident/proto/Common.SmartContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Common.SmartContract.ABI
  extends com.google.protobuf.GeneratedMessageV3
  implements Common.SmartContract.ABIOrBuilder
  ```

  Protobuf type `protocol.SmartContract.ABI`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Common.SmartContract.ABI)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Common.SmartContract.ABI.Builder` Protobuf type `protocol.SmartContract.ABI` |
    | `static class` | `Common.SmartContract.ABI.Entry` Protobuf type `protocol.SmartContract.ABI.Entry` |
    | `static interface` | `Common.SmartContract.ABI.EntryOrBuilder` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `ENTRYS_FIELD_NUMBER` |

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
    | `static Common.SmartContract.ABI` | `getDefaultInstance()` |
    | `Common.SmartContract.ABI` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `Common.SmartContract.ABI.Entry` | `getEntrys(int index)` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `int` | `getEntrysCount()` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `java.util.List<Common.SmartContract.ABI.Entry>` | `getEntrysList()` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `Common.SmartContract.ABI.EntryOrBuilder` | `getEntrysOrBuilder(int index)` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `java.util.List<? extends Common.SmartContract.ABI.EntryOrBuilder>` | `getEntrysOrBuilderList()` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `com.google.protobuf.Parser<Common.SmartContract.ABI>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Common.SmartContract.ABI.Builder` | `newBuilder()` |
    | `static Common.SmartContract.ABI.Builder` | `newBuilder(Common.SmartContract.ABI prototype)` |
    | `Common.SmartContract.ABI.Builder` | `newBuilderForType()` |
    | `protected Common.SmartContract.ABI.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Common.SmartContract.ABI` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Common.SmartContract.ABI` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.SmartContract.ABI` | `parseFrom(byte[] data)` |
    | `static Common.SmartContract.ABI` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.SmartContract.ABI` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Common.SmartContract.ABI` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.SmartContract.ABI` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Common.SmartContract.ABI` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.SmartContract.ABI` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Common.SmartContract.ABI` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.SmartContract.ABI` | `parseFrom(java.io.InputStream input)` |
    | `static Common.SmartContract.ABI` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Common.SmartContract.ABI>` | `parser()` |
    | `Common.SmartContract.ABI.Builder` | `toBuilder()` |
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

    - #### ENTRYS\_FIELD\_NUMBER

      ```
      public static final int ENTRYS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ABI.ENTRYS_FIELD_NUMBER)
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
    - #### getEntrysList

      ```
      public java.util.List<Common.SmartContract.ABI.Entry> getEntrysList()
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`

      Specified by:
      :   `getEntrysList` in interface `Common.SmartContract.ABIOrBuilder`
    - #### getEntrysOrBuilderList

      ```
      public java.util.List<? extends Common.SmartContract.ABI.EntryOrBuilder> getEntrysOrBuilderList()
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`

      Specified by:
      :   `getEntrysOrBuilderList` in interface `Common.SmartContract.ABIOrBuilder`
    - #### getEntrysCount

      ```
      public int getEntrysCount()
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`

      Specified by:
      :   `getEntrysCount` in interface `Common.SmartContract.ABIOrBuilder`
    - #### getEntrys

      ```
      public Common.SmartContract.ABI.Entry getEntrys(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`

      Specified by:
      :   `getEntrys` in interface `Common.SmartContract.ABIOrBuilder`
    - #### getEntrysOrBuilder

      ```
      public Common.SmartContract.ABI.EntryOrBuilder getEntrysOrBuilder(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`

      Specified by:
      :   `getEntrysOrBuilder` in interface `Common.SmartContract.ABIOrBuilder`
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
      public static Common.SmartContract.ABI parseFrom(java.nio.ByteBuffer data)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.SmartContract.ABI parseFrom(java.nio.ByteBuffer data,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.SmartContract.ABI parseFrom(com.google.protobuf.ByteString data)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.SmartContract.ABI parseFrom(com.google.protobuf.ByteString data,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.SmartContract.ABI parseFrom(byte[] data)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.SmartContract.ABI parseFrom(byte[] data,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.SmartContract.ABI parseFrom(java.io.InputStream input)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Common.SmartContract.ABI parseFrom(java.io.InputStream input,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Common.SmartContract.ABI parseDelimitedFrom(java.io.InputStream input)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Common.SmartContract.ABI parseDelimitedFrom(java.io.InputStream input,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Common.SmartContract.ABI parseFrom(com.google.protobuf.CodedInputStream input)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Common.SmartContract.ABI parseFrom(com.google.protobuf.CodedInputStream input,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Common.SmartContract.ABI.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Common.SmartContract.ABI.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Common.SmartContract.ABI.Builder newBuilder(Common.SmartContract.ABI prototype)
      ```
    - #### toBuilder

      ```
      public Common.SmartContract.ABI.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Common.SmartContract.ABI.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Common.SmartContract.ABI getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Common.SmartContract.ABI> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Common.SmartContract.ABI> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Common.SmartContract.ABI getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`