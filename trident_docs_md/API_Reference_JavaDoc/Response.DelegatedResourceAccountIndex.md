

org.tron.trident.proto

## Class Response.DelegatedResourceAccountIndex

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.DelegatedResourceAccountIndex

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.DelegatedResourceAccountIndexOrBuilder](../../../../org/tron/trident/proto/Response.DelegatedResourceAccountIndexOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.DelegatedResourceAccountIndex
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.DelegatedResourceAccountIndexOrBuilder
  ```

  Protobuf type `protocol.DelegatedResourceAccountIndex`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.DelegatedResourceAccountIndex)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.DelegatedResourceAccountIndex.Builder` Protobuf type `protocol.DelegatedResourceAccountIndex` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `ACCOUNT_FIELD_NUMBER` |
    | `static int` | `FROMACCOUNTS_FIELD_NUMBER` |
    | `static int` | `TIMESTAMP_FIELD_NUMBER` |
    | `static int` | `TOACCOUNTS_FIELD_NUMBER` |

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
    | `com.google.protobuf.ByteString` | `getAccount()` `bytes account = 1;` |
    | `static Response.DelegatedResourceAccountIndex` | `getDefaultInstance()` |
    | `Response.DelegatedResourceAccountIndex` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.ByteString` | `getFromAccounts(int index)` `repeated bytes fromAccounts = 2;` |
    | `int` | `getFromAccountsCount()` `repeated bytes fromAccounts = 2;` |
    | `java.util.List<com.google.protobuf.ByteString>` | `getFromAccountsList()` `repeated bytes fromAccounts = 2;` |
    | `com.google.protobuf.Parser<Response.DelegatedResourceAccountIndex>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `long` | `getTimestamp()` `int64 timestamp = 4;` |
    | `com.google.protobuf.ByteString` | `getToAccounts(int index)` `repeated bytes toAccounts = 3;` |
    | `int` | `getToAccountsCount()` `repeated bytes toAccounts = 3;` |
    | `java.util.List<com.google.protobuf.ByteString>` | `getToAccountsList()` `repeated bytes toAccounts = 3;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Response.DelegatedResourceAccountIndex.Builder` | `newBuilder()` |
    | `static Response.DelegatedResourceAccountIndex.Builder` | `newBuilder(Response.DelegatedResourceAccountIndex prototype)` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `newBuilderForType()` |
    | `protected Response.DelegatedResourceAccountIndex.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.DelegatedResourceAccountIndex` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.DelegatedResourceAccountIndex` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.DelegatedResourceAccountIndex` | `parseFrom(byte[] data)` |
    | `static Response.DelegatedResourceAccountIndex` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.DelegatedResourceAccountIndex` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.DelegatedResourceAccountIndex` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.DelegatedResourceAccountIndex` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.DelegatedResourceAccountIndex` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.DelegatedResourceAccountIndex` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.DelegatedResourceAccountIndex` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.DelegatedResourceAccountIndex` | `parseFrom(java.io.InputStream input)` |
    | `static Response.DelegatedResourceAccountIndex` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.DelegatedResourceAccountIndex>` | `parser()` |
    | `Response.DelegatedResourceAccountIndex.Builder` | `toBuilder()` |
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

    - #### ACCOUNT\_FIELD\_NUMBER

      ```
      public static final int ACCOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.DelegatedResourceAccountIndex.ACCOUNT_FIELD_NUMBER)
    - #### FROMACCOUNTS\_FIELD\_NUMBER

      ```
      public static final int FROMACCOUNTS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.DelegatedResourceAccountIndex.FROMACCOUNTS_FIELD_NUMBER)
    - #### TOACCOUNTS\_FIELD\_NUMBER

      ```
      public static final int TOACCOUNTS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.DelegatedResourceAccountIndex.TOACCOUNTS_FIELD_NUMBER)
    - #### TIMESTAMP\_FIELD\_NUMBER

      ```
      public static final int TIMESTAMP_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.DelegatedResourceAccountIndex.TIMESTAMP_FIELD_NUMBER)
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
    - #### getAccount

      ```
      public com.google.protobuf.ByteString getAccount()
      ```

      `bytes account = 1;`

      Specified by:
      :   `getAccount` in interface `Response.DelegatedResourceAccountIndexOrBuilder`

      Returns:
      :   The account.
    - #### getFromAccountsList

      ```
      public java.util.List<com.google.protobuf.ByteString> getFromAccountsList()
      ```

      `repeated bytes fromAccounts = 2;`

      Specified by:
      :   `getFromAccountsList` in interface `Response.DelegatedResourceAccountIndexOrBuilder`

      Returns:
      :   A list containing the fromAccounts.
    - #### getFromAccountsCount

      ```
      public int getFromAccountsCount()
      ```

      `repeated bytes fromAccounts = 2;`

      Specified by:
      :   `getFromAccountsCount` in interface `Response.DelegatedResourceAccountIndexOrBuilder`

      Returns:
      :   The count of fromAccounts.
    - #### getFromAccounts

      ```
      public com.google.protobuf.ByteString getFromAccounts(int index)
      ```

      `repeated bytes fromAccounts = 2;`

      Specified by:
      :   `getFromAccounts` in interface `Response.DelegatedResourceAccountIndexOrBuilder`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The fromAccounts at the given index.
    - #### getToAccountsList

      ```
      public java.util.List<com.google.protobuf.ByteString> getToAccountsList()
      ```

      `repeated bytes toAccounts = 3;`

      Specified by:
      :   `getToAccountsList` in interface `Response.DelegatedResourceAccountIndexOrBuilder`

      Returns:
      :   A list containing the toAccounts.
    - #### getToAccountsCount

      ```
      public int getToAccountsCount()
      ```

      `repeated bytes toAccounts = 3;`

      Specified by:
      :   `getToAccountsCount` in interface `Response.DelegatedResourceAccountIndexOrBuilder`

      Returns:
      :   The count of toAccounts.
    - #### getToAccounts

      ```
      public com.google.protobuf.ByteString getToAccounts(int index)
      ```

      `repeated bytes toAccounts = 3;`

      Specified by:
      :   `getToAccounts` in interface `Response.DelegatedResourceAccountIndexOrBuilder`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The toAccounts at the given index.
    - #### getTimestamp

      ```
      public long getTimestamp()
      ```

      `int64 timestamp = 4;`

      Specified by:
      :   `getTimestamp` in interface `Response.DelegatedResourceAccountIndexOrBuilder`

      Returns:
      :   The timestamp.
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
      public static Response.DelegatedResourceAccountIndex parseFrom(java.nio.ByteBuffer data)
                                                              throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DelegatedResourceAccountIndex parseFrom(java.nio.ByteBuffer data,
                                                                     com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                              throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DelegatedResourceAccountIndex parseFrom(com.google.protobuf.ByteString data)
                                                              throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DelegatedResourceAccountIndex parseFrom(com.google.protobuf.ByteString data,
                                                                     com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                              throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DelegatedResourceAccountIndex parseFrom(byte[] data)
                                                              throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DelegatedResourceAccountIndex parseFrom(byte[] data,
                                                                     com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                              throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DelegatedResourceAccountIndex parseFrom(java.io.InputStream input)
                                                              throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.DelegatedResourceAccountIndex parseFrom(java.io.InputStream input,
                                                                     com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                              throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.DelegatedResourceAccountIndex parseDelimitedFrom(java.io.InputStream input)
                                                                       throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.DelegatedResourceAccountIndex parseDelimitedFrom(java.io.InputStream input,
                                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                       throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.DelegatedResourceAccountIndex parseFrom(com.google.protobuf.CodedInputStream input)
                                                              throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.DelegatedResourceAccountIndex parseFrom(com.google.protobuf.CodedInputStream input,
                                                                     com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                              throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.DelegatedResourceAccountIndex.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.DelegatedResourceAccountIndex.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.DelegatedResourceAccountIndex.Builder newBuilder(Response.DelegatedResourceAccountIndex prototype)
      ```
    - #### toBuilder

      ```
      public Response.DelegatedResourceAccountIndex.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.DelegatedResourceAccountIndex.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.DelegatedResourceAccountIndex getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.DelegatedResourceAccountIndex> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.DelegatedResourceAccountIndex> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.DelegatedResourceAccountIndex getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`