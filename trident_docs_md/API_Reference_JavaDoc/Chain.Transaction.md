

org.tron.trident.proto

## Class Chain.Transaction

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Chain.Transaction

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Chain.TransactionOrBuilder](../../../../org/tron/trident/proto/Chain.TransactionOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Chain](../../../../org/tron/trident/proto/Chain.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Chain.Transaction
  extends com.google.protobuf.GeneratedMessageV3
  implements Chain.TransactionOrBuilder
  ```

  Protobuf type `protocol.Transaction`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Chain.Transaction)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Chain.Transaction.Builder` Protobuf type `protocol.Transaction` |
    | `static class` | `Chain.Transaction.Contract` Protobuf type `protocol.Transaction.Contract` |
    | `static interface` | `Chain.Transaction.ContractOrBuilder` |
    | `static class` | `Chain.Transaction.raw` Protobuf type `protocol.Transaction.raw` |
    | `static interface` | `Chain.Transaction.rawOrBuilder` |
    | `static class` | `Chain.Transaction.Result` Protobuf type `protocol.Transaction.Result` |
    | `static interface` | `Chain.Transaction.ResultOrBuilder` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `RAW_DATA_FIELD_NUMBER` |
    | `static int` | `RET_FIELD_NUMBER` |
    | `static int` | `SIGNATURE_FIELD_NUMBER` |

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
    | `static Chain.Transaction` | `getDefaultInstance()` |
    | `Chain.Transaction` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Parser<Chain.Transaction>` | `getParserForType()` |
    | `Chain.Transaction.raw` | `getRawData()` `.protocol.Transaction.raw raw_data = 1;` |
    | `Chain.Transaction.rawOrBuilder` | `getRawDataOrBuilder()` `.protocol.Transaction.raw raw_data = 1;` |
    | `Chain.Transaction.Result` | `getRet(int index)` `repeated .protocol.Transaction.Result ret = 5;` |
    | `int` | `getRetCount()` `repeated .protocol.Transaction.Result ret = 5;` |
    | `java.util.List<Chain.Transaction.Result>` | `getRetList()` `repeated .protocol.Transaction.Result ret = 5;` |
    | `Chain.Transaction.ResultOrBuilder` | `getRetOrBuilder(int index)` `repeated .protocol.Transaction.Result ret = 5;` |
    | `java.util.List<? extends Chain.Transaction.ResultOrBuilder>` | `getRetOrBuilderList()` `repeated .protocol.Transaction.Result ret = 5;` |
    | `int` | `getSerializedSize()` |
    | `com.google.protobuf.ByteString` | `getSignature(int index)` only support size = 1, repeated list here for muti-sig extension |
    | `int` | `getSignatureCount()` only support size = 1, repeated list here for muti-sig extension |
    | `java.util.List<com.google.protobuf.ByteString>` | `getSignatureList()` only support size = 1, repeated list here for muti-sig extension |
    | `int` | `hashCode()` |
    | `boolean` | `hasRawData()` `.protocol.Transaction.raw raw_data = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Chain.Transaction.Builder` | `newBuilder()` |
    | `static Chain.Transaction.Builder` | `newBuilder(Chain.Transaction prototype)` |
    | `Chain.Transaction.Builder` | `newBuilderForType()` |
    | `protected Chain.Transaction.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Chain.Transaction` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Chain.Transaction` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.Transaction` | `parseFrom(byte[] data)` |
    | `static Chain.Transaction` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.Transaction` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Chain.Transaction` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.Transaction` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Chain.Transaction` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.Transaction` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Chain.Transaction` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.Transaction` | `parseFrom(java.io.InputStream input)` |
    | `static Chain.Transaction` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Chain.Transaction>` | `parser()` |
    | `Chain.Transaction.Builder` | `toBuilder()` |
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

    - #### RAW\_DATA\_FIELD\_NUMBER

      ```
      public static final int RAW_DATA_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.RAW_DATA_FIELD_NUMBER)
    - #### SIGNATURE\_FIELD\_NUMBER

      ```
      public static final int SIGNATURE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.SIGNATURE_FIELD_NUMBER)
    - #### RET\_FIELD\_NUMBER

      ```
      public static final int RET_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.RET_FIELD_NUMBER)
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
    - #### hasRawData

      ```
      public boolean hasRawData()
      ```

      `.protocol.Transaction.raw raw_data = 1;`

      Specified by:
      :   `hasRawData` in interface `Chain.TransactionOrBuilder`

      Returns:
      :   Whether the rawData field is set.
    - #### getRawData

      ```
      public Chain.Transaction.raw getRawData()
      ```

      `.protocol.Transaction.raw raw_data = 1;`

      Specified by:
      :   `getRawData` in interface `Chain.TransactionOrBuilder`

      Returns:
      :   The rawData.
    - #### getRawDataOrBuilder

      ```
      public Chain.Transaction.rawOrBuilder getRawDataOrBuilder()
      ```

      `.protocol.Transaction.raw raw_data = 1;`

      Specified by:
      :   `getRawDataOrBuilder` in interface `Chain.TransactionOrBuilder`
    - #### getSignatureList

      ```
      public java.util.List<com.google.protobuf.ByteString> getSignatureList()
      ```

      ```
       only support size = 1, repeated list here for muti-sig extension
      ```

      `repeated bytes signature = 2;`

      Specified by:
      :   `getSignatureList` in interface `Chain.TransactionOrBuilder`

      Returns:
      :   A list containing the signature.
    - #### getSignatureCount

      ```
      public int getSignatureCount()
      ```

      ```
       only support size = 1, repeated list here for muti-sig extension
      ```

      `repeated bytes signature = 2;`

      Specified by:
      :   `getSignatureCount` in interface `Chain.TransactionOrBuilder`

      Returns:
      :   The count of signature.
    - #### getSignature

      ```
      public com.google.protobuf.ByteString getSignature(int index)
      ```

      ```
       only support size = 1, repeated list here for muti-sig extension
      ```

      `repeated bytes signature = 2;`

      Specified by:
      :   `getSignature` in interface `Chain.TransactionOrBuilder`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The signature at the given index.
    - #### getRetList

      ```
      public java.util.List<Chain.Transaction.Result> getRetList()
      ```

      `repeated .protocol.Transaction.Result ret = 5;`

      Specified by:
      :   `getRetList` in interface `Chain.TransactionOrBuilder`
    - #### getRetOrBuilderList

      ```
      public java.util.List<? extends Chain.Transaction.ResultOrBuilder> getRetOrBuilderList()
      ```

      `repeated .protocol.Transaction.Result ret = 5;`

      Specified by:
      :   `getRetOrBuilderList` in interface `Chain.TransactionOrBuilder`
    - #### getRetCount

      ```
      public int getRetCount()
      ```

      `repeated .protocol.Transaction.Result ret = 5;`

      Specified by:
      :   `getRetCount` in interface `Chain.TransactionOrBuilder`
    - #### getRet

      ```
      public Chain.Transaction.Result getRet(int index)
      ```

      `repeated .protocol.Transaction.Result ret = 5;`

      Specified by:
      :   `getRet` in interface `Chain.TransactionOrBuilder`
    - #### getRetOrBuilder

      ```
      public Chain.Transaction.ResultOrBuilder getRetOrBuilder(int index)
      ```

      `repeated .protocol.Transaction.Result ret = 5;`

      Specified by:
      :   `getRetOrBuilder` in interface `Chain.TransactionOrBuilder`
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
      public static Chain.Transaction parseFrom(java.nio.ByteBuffer data)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction parseFrom(java.nio.ByteBuffer data,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction parseFrom(com.google.protobuf.ByteString data)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction parseFrom(com.google.protobuf.ByteString data,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction parseFrom(byte[] data)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction parseFrom(byte[] data,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction parseFrom(java.io.InputStream input)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Chain.Transaction parseFrom(java.io.InputStream input,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Chain.Transaction parseDelimitedFrom(java.io.InputStream input)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Chain.Transaction parseDelimitedFrom(java.io.InputStream input,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Chain.Transaction parseFrom(com.google.protobuf.CodedInputStream input)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Chain.Transaction parseFrom(com.google.protobuf.CodedInputStream input,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Chain.Transaction.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Chain.Transaction.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Chain.Transaction.Builder newBuilder(Chain.Transaction prototype)
      ```
    - #### toBuilder

      ```
      public Chain.Transaction.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Chain.Transaction.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Chain.Transaction getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Chain.Transaction> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Chain.Transaction> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Chain.Transaction getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`