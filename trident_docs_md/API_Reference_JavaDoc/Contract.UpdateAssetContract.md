

org.tron.trident.proto

## Class Contract.UpdateAssetContract

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Contract.UpdateAssetContract

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Contract.UpdateAssetContractOrBuilder](../../../../org/tron/trident/proto/Contract.UpdateAssetContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.UpdateAssetContract
  extends com.google.protobuf.GeneratedMessageV3
  implements Contract.UpdateAssetContractOrBuilder
  ```

  Protobuf type `protocol.UpdateAssetContract`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Contract.UpdateAssetContract)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Contract.UpdateAssetContract.Builder` Protobuf type `protocol.UpdateAssetContract` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `DESCRIPTION_FIELD_NUMBER` |
    | `static int` | `NEW_LIMIT_FIELD_NUMBER` |
    | `static int` | `NEW_PUBLIC_LIMIT_FIELD_NUMBER` |
    | `static int` | `OWNER_ADDRESS_FIELD_NUMBER` |
    | `static int` | `URL_FIELD_NUMBER` |

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
    | `static Contract.UpdateAssetContract` | `getDefaultInstance()` |
    | `Contract.UpdateAssetContract` | `getDefaultInstanceForType()` |
    | `com.google.protobuf.ByteString` | `getDescription()` `bytes description = 2;` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `long` | `getNewLimit()` `int64 new_limit = 4;` |
    | `long` | `getNewPublicLimit()` `int64 new_public_limit = 5;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `com.google.protobuf.Parser<Contract.UpdateAssetContract>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `com.google.protobuf.ByteString` | `getUrl()` `bytes url = 3;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Contract.UpdateAssetContract.Builder` | `newBuilder()` |
    | `static Contract.UpdateAssetContract.Builder` | `newBuilder(Contract.UpdateAssetContract prototype)` |
    | `Contract.UpdateAssetContract.Builder` | `newBuilderForType()` |
    | `protected Contract.UpdateAssetContract.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Contract.UpdateAssetContract` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Contract.UpdateAssetContract` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.UpdateAssetContract` | `parseFrom(byte[] data)` |
    | `static Contract.UpdateAssetContract` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.UpdateAssetContract` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Contract.UpdateAssetContract` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.UpdateAssetContract` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Contract.UpdateAssetContract` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.UpdateAssetContract` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Contract.UpdateAssetContract` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Contract.UpdateAssetContract` | `parseFrom(java.io.InputStream input)` |
    | `static Contract.UpdateAssetContract` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Contract.UpdateAssetContract>` | `parser()` |
    | `Contract.UpdateAssetContract.Builder` | `toBuilder()` |
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

    - #### OWNER\_ADDRESS\_FIELD\_NUMBER

      ```
      public static final int OWNER_ADDRESS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.UpdateAssetContract.OWNER_ADDRESS_FIELD_NUMBER)
    - #### DESCRIPTION\_FIELD\_NUMBER

      ```
      public static final int DESCRIPTION_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.UpdateAssetContract.DESCRIPTION_FIELD_NUMBER)
    - #### URL\_FIELD\_NUMBER

      ```
      public static final int URL_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.UpdateAssetContract.URL_FIELD_NUMBER)
    - #### NEW\_LIMIT\_FIELD\_NUMBER

      ```
      public static final int NEW_LIMIT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.UpdateAssetContract.NEW_LIMIT_FIELD_NUMBER)
    - #### NEW\_PUBLIC\_LIMIT\_FIELD\_NUMBER

      ```
      public static final int NEW_PUBLIC_LIMIT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Contract.UpdateAssetContract.NEW_PUBLIC_LIMIT_FIELD_NUMBER)
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
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.UpdateAssetContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### getDescription

      ```
      public com.google.protobuf.ByteString getDescription()
      ```

      `bytes description = 2;`

      Specified by:
      :   `getDescription` in interface `Contract.UpdateAssetContractOrBuilder`

      Returns:
      :   The description.
    - #### getUrl

      ```
      public com.google.protobuf.ByteString getUrl()
      ```

      `bytes url = 3;`

      Specified by:
      :   `getUrl` in interface `Contract.UpdateAssetContractOrBuilder`

      Returns:
      :   The url.
    - #### getNewLimit

      ```
      public long getNewLimit()
      ```

      `int64 new_limit = 4;`

      Specified by:
      :   `getNewLimit` in interface `Contract.UpdateAssetContractOrBuilder`

      Returns:
      :   The newLimit.
    - #### getNewPublicLimit

      ```
      public long getNewPublicLimit()
      ```

      `int64 new_public_limit = 5;`

      Specified by:
      :   `getNewPublicLimit` in interface `Contract.UpdateAssetContractOrBuilder`

      Returns:
      :   The newPublicLimit.
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
      public static Contract.UpdateAssetContract parseFrom(java.nio.ByteBuffer data)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.UpdateAssetContract parseFrom(java.nio.ByteBuffer data,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.UpdateAssetContract parseFrom(com.google.protobuf.ByteString data)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.UpdateAssetContract parseFrom(com.google.protobuf.ByteString data,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.UpdateAssetContract parseFrom(byte[] data)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.UpdateAssetContract parseFrom(byte[] data,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Contract.UpdateAssetContract parseFrom(java.io.InputStream input)
                                                    throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.UpdateAssetContract parseFrom(java.io.InputStream input,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Contract.UpdateAssetContract parseDelimitedFrom(java.io.InputStream input)
                                                             throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Contract.UpdateAssetContract parseDelimitedFrom(java.io.InputStream input,
                                                                    com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                             throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.UpdateAssetContract parseFrom(com.google.protobuf.CodedInputStream input)
                                                    throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Contract.UpdateAssetContract parseFrom(com.google.protobuf.CodedInputStream input,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Contract.UpdateAssetContract.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Contract.UpdateAssetContract.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Contract.UpdateAssetContract.Builder newBuilder(Contract.UpdateAssetContract prototype)
      ```
    - #### toBuilder

      ```
      public Contract.UpdateAssetContract.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Contract.UpdateAssetContract.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Contract.UpdateAssetContract getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Contract.UpdateAssetContract> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Contract.UpdateAssetContract> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Contract.UpdateAssetContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`