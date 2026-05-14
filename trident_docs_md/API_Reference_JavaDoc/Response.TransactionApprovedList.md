

org.tron.trident.proto

## Class Response.TransactionApprovedList

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.TransactionApprovedList

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.TransactionApprovedListOrBuilder](../../../../org/tron/trident/proto/Response.TransactionApprovedListOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.TransactionApprovedList
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.TransactionApprovedListOrBuilder
  ```

  Protobuf type `protocol.TransactionApprovedList`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.TransactionApprovedList)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.TransactionApprovedList.Builder` Protobuf type `protocol.TransactionApprovedList` |
    | `static class` | `Response.TransactionApprovedList.Result` Protobuf type `protocol.TransactionApprovedList.Result` |
    | `static interface` | `Response.TransactionApprovedList.ResultOrBuilder` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `APPROVED_LIST_FIELD_NUMBER` |
    | `static int` | `RESULT_FIELD_NUMBER` |
    | `static int` | `TRANSACTION_FIELD_NUMBER` |

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
    | `com.google.protobuf.ByteString` | `getApprovedList(int index)` `repeated bytes approved_list = 2;` |
    | `int` | `getApprovedListCount()` `repeated bytes approved_list = 2;` |
    | `java.util.List<com.google.protobuf.ByteString>` | `getApprovedListList()` `repeated bytes approved_list = 2;` |
    | `static Response.TransactionApprovedList` | `getDefaultInstance()` |
    | `Response.TransactionApprovedList` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Parser<Response.TransactionApprovedList>` | `getParserForType()` |
    | `Response.TransactionApprovedList.Result` | `getResult()` `.protocol.TransactionApprovedList.Result result = 4;` |
    | `Response.TransactionApprovedList.ResultOrBuilder` | `getResultOrBuilder()` `.protocol.TransactionApprovedList.Result result = 4;` |
    | `int` | `getSerializedSize()` |
    | `Response.TransactionExtention` | `getTransaction()` `.protocol.TransactionExtention transaction = 5;` |
    | `Response.TransactionExtentionOrBuilder` | `getTransactionOrBuilder()` `.protocol.TransactionExtention transaction = 5;` |
    | `int` | `hashCode()` |
    | `boolean` | `hasResult()` `.protocol.TransactionApprovedList.Result result = 4;` |
    | `boolean` | `hasTransaction()` `.protocol.TransactionExtention transaction = 5;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Response.TransactionApprovedList.Builder` | `newBuilder()` |
    | `static Response.TransactionApprovedList.Builder` | `newBuilder(Response.TransactionApprovedList prototype)` |
    | `Response.TransactionApprovedList.Builder` | `newBuilderForType()` |
    | `protected Response.TransactionApprovedList.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.TransactionApprovedList` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.TransactionApprovedList` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.TransactionApprovedList` | `parseFrom(byte[] data)` |
    | `static Response.TransactionApprovedList` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.TransactionApprovedList` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.TransactionApprovedList` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.TransactionApprovedList` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.TransactionApprovedList` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.TransactionApprovedList` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.TransactionApprovedList` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.TransactionApprovedList` | `parseFrom(java.io.InputStream input)` |
    | `static Response.TransactionApprovedList` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.TransactionApprovedList>` | `parser()` |
    | `Response.TransactionApprovedList.Builder` | `toBuilder()` |
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

    - #### APPROVED\_LIST\_FIELD\_NUMBER

      ```
      public static final int APPROVED_LIST_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionApprovedList.APPROVED_LIST_FIELD_NUMBER)
    - #### RESULT\_FIELD\_NUMBER

      ```
      public static final int RESULT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionApprovedList.RESULT_FIELD_NUMBER)
    - #### TRANSACTION\_FIELD\_NUMBER

      ```
      public static final int TRANSACTION_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionApprovedList.TRANSACTION_FIELD_NUMBER)
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
    - #### getApprovedListList

      ```
      public java.util.List<com.google.protobuf.ByteString> getApprovedListList()
      ```

      `repeated bytes approved_list = 2;`

      Specified by:
      :   `getApprovedListList` in interface `Response.TransactionApprovedListOrBuilder`

      Returns:
      :   A list containing the approvedList.
    - #### getApprovedListCount

      ```
      public int getApprovedListCount()
      ```

      `repeated bytes approved_list = 2;`

      Specified by:
      :   `getApprovedListCount` in interface `Response.TransactionApprovedListOrBuilder`

      Returns:
      :   The count of approvedList.
    - #### getApprovedList

      ```
      public com.google.protobuf.ByteString getApprovedList(int index)
      ```

      `repeated bytes approved_list = 2;`

      Specified by:
      :   `getApprovedList` in interface `Response.TransactionApprovedListOrBuilder`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The approvedList at the given index.
    - #### hasResult

      ```
      public boolean hasResult()
      ```

      `.protocol.TransactionApprovedList.Result result = 4;`

      Specified by:
      :   `hasResult` in interface `Response.TransactionApprovedListOrBuilder`

      Returns:
      :   Whether the result field is set.
    - #### getResult

      ```
      public Response.TransactionApprovedList.Result getResult()
      ```

      `.protocol.TransactionApprovedList.Result result = 4;`

      Specified by:
      :   `getResult` in interface `Response.TransactionApprovedListOrBuilder`

      Returns:
      :   The result.
    - #### getResultOrBuilder

      ```
      public Response.TransactionApprovedList.ResultOrBuilder getResultOrBuilder()
      ```

      `.protocol.TransactionApprovedList.Result result = 4;`

      Specified by:
      :   `getResultOrBuilder` in interface `Response.TransactionApprovedListOrBuilder`
    - #### hasTransaction

      ```
      public boolean hasTransaction()
      ```

      `.protocol.TransactionExtention transaction = 5;`

      Specified by:
      :   `hasTransaction` in interface `Response.TransactionApprovedListOrBuilder`

      Returns:
      :   Whether the transaction field is set.
    - #### getTransaction

      ```
      public Response.TransactionExtention getTransaction()
      ```

      `.protocol.TransactionExtention transaction = 5;`

      Specified by:
      :   `getTransaction` in interface `Response.TransactionApprovedListOrBuilder`

      Returns:
      :   The transaction.
    - #### getTransactionOrBuilder

      ```
      public Response.TransactionExtentionOrBuilder getTransactionOrBuilder()
      ```

      `.protocol.TransactionExtention transaction = 5;`

      Specified by:
      :   `getTransactionOrBuilder` in interface `Response.TransactionApprovedListOrBuilder`
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
      public static Response.TransactionApprovedList parseFrom(java.nio.ByteBuffer data)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionApprovedList parseFrom(java.nio.ByteBuffer data,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionApprovedList parseFrom(com.google.protobuf.ByteString data)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionApprovedList parseFrom(com.google.protobuf.ByteString data,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionApprovedList parseFrom(byte[] data)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionApprovedList parseFrom(byte[] data,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.TransactionApprovedList parseFrom(java.io.InputStream input)
                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.TransactionApprovedList parseFrom(java.io.InputStream input,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.TransactionApprovedList parseDelimitedFrom(java.io.InputStream input)
                                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.TransactionApprovedList parseDelimitedFrom(java.io.InputStream input,
                                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.TransactionApprovedList parseFrom(com.google.protobuf.CodedInputStream input)
                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.TransactionApprovedList parseFrom(com.google.protobuf.CodedInputStream input,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.TransactionApprovedList.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.TransactionApprovedList.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.TransactionApprovedList.Builder newBuilder(Response.TransactionApprovedList prototype)
      ```
    - #### toBuilder

      ```
      public Response.TransactionApprovedList.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.TransactionApprovedList.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.TransactionApprovedList getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.TransactionApprovedList> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.TransactionApprovedList> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.TransactionApprovedList getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`