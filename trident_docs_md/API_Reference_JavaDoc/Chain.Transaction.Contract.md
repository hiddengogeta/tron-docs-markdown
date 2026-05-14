

org.tron.trident.proto

## Class Chain.Transaction.Contract

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Chain.Transaction.Contract

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Chain.Transaction.ContractOrBuilder](../../../../org/tron/trident/proto/Chain.Transaction.ContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Chain.Transaction](../../../../org/tron/trident/proto/Chain.Transaction.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Chain.Transaction.Contract
  extends com.google.protobuf.GeneratedMessageV3
  implements Chain.Transaction.ContractOrBuilder
  ```

  Protobuf type `protocol.Transaction.Contract`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Chain.Transaction.Contract)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Chain.Transaction.Contract.Builder` Protobuf type `protocol.Transaction.Contract` |
    | `static class` | `Chain.Transaction.Contract.ContractType` Protobuf enum `protocol.Transaction.Contract.ContractType` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `CONTRACTNAME_FIELD_NUMBER` |
    | `static int` | `PARAMETER_FIELD_NUMBER` |
    | `static int` | `PERMISSION_ID_FIELD_NUMBER` |
    | `static int` | `PROVIDER_FIELD_NUMBER` |
    | `static int` | `TYPE_FIELD_NUMBER` |

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
    | `com.google.protobuf.ByteString` | `getContractName()` `bytes ContractName = 4;` |
    | `static Chain.Transaction.Contract` | `getDefaultInstance()` |
    | `Chain.Transaction.Contract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Any` | `getParameter()` `.google.protobuf.Any parameter = 2;` |
    | `com.google.protobuf.AnyOrBuilder` | `getParameterOrBuilder()` `.google.protobuf.Any parameter = 2;` |
    | `com.google.protobuf.Parser<Chain.Transaction.Contract>` | `getParserForType()` |
    | `int` | `getPermissionId()` `int32 Permission_id = 5;` |
    | `com.google.protobuf.ByteString` | `getProvider()` `bytes provider = 3;` |
    | `int` | `getSerializedSize()` |
    | `Chain.Transaction.Contract.ContractType` | `getType()` `.protocol.Transaction.Contract.ContractType type = 1;` |
    | `int` | `getTypeValue()` `.protocol.Transaction.Contract.ContractType type = 1;` |
    | `int` | `hashCode()` |
    | `boolean` | `hasParameter()` `.google.protobuf.Any parameter = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Chain.Transaction.Contract.Builder` | `newBuilder()` |
    | `static Chain.Transaction.Contract.Builder` | `newBuilder(Chain.Transaction.Contract prototype)` |
    | `Chain.Transaction.Contract.Builder` | `newBuilderForType()` |
    | `protected Chain.Transaction.Contract.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Chain.Transaction.Contract` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Chain.Transaction.Contract` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.Transaction.Contract` | `parseFrom(byte[] data)` |
    | `static Chain.Transaction.Contract` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.Transaction.Contract` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Chain.Transaction.Contract` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.Transaction.Contract` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Chain.Transaction.Contract` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.Transaction.Contract` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Chain.Transaction.Contract` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Chain.Transaction.Contract` | `parseFrom(java.io.InputStream input)` |
    | `static Chain.Transaction.Contract` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Chain.Transaction.Contract>` | `parser()` |
    | `Chain.Transaction.Contract.Builder` | `toBuilder()` |
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

    - #### TYPE\_FIELD\_NUMBER

      ```
      public static final int TYPE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.TYPE_FIELD_NUMBER)
    - #### PARAMETER\_FIELD\_NUMBER

      ```
      public static final int PARAMETER_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.PARAMETER_FIELD_NUMBER)
    - #### PROVIDER\_FIELD\_NUMBER

      ```
      public static final int PROVIDER_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.PROVIDER_FIELD_NUMBER)
    - #### CONTRACTNAME\_FIELD\_NUMBER

      ```
      public static final int CONTRACTNAME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.CONTRACTNAME_FIELD_NUMBER)
    - #### PERMISSION\_ID\_FIELD\_NUMBER

      ```
      public static final int PERMISSION_ID_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Contract.PERMISSION_ID_FIELD_NUMBER)
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
    - #### getTypeValue

      ```
      public int getTypeValue()
      ```

      `.protocol.Transaction.Contract.ContractType type = 1;`

      Specified by:
      :   `getTypeValue` in interface `Chain.Transaction.ContractOrBuilder`

      Returns:
      :   The enum numeric value on the wire for type.
    - #### getType

      ```
      public Chain.Transaction.Contract.ContractType getType()
      ```

      `.protocol.Transaction.Contract.ContractType type = 1;`

      Specified by:
      :   `getType` in interface `Chain.Transaction.ContractOrBuilder`

      Returns:
      :   The type.
    - #### hasParameter

      ```
      public boolean hasParameter()
      ```

      `.google.protobuf.Any parameter = 2;`

      Specified by:
      :   `hasParameter` in interface `Chain.Transaction.ContractOrBuilder`

      Returns:
      :   Whether the parameter field is set.
    - #### getParameter

      ```
      public com.google.protobuf.Any getParameter()
      ```

      `.google.protobuf.Any parameter = 2;`

      Specified by:
      :   `getParameter` in interface `Chain.Transaction.ContractOrBuilder`

      Returns:
      :   The parameter.
    - #### getParameterOrBuilder

      ```
      public com.google.protobuf.AnyOrBuilder getParameterOrBuilder()
      ```

      `.google.protobuf.Any parameter = 2;`

      Specified by:
      :   `getParameterOrBuilder` in interface `Chain.Transaction.ContractOrBuilder`
    - #### getProvider

      ```
      public com.google.protobuf.ByteString getProvider()
      ```

      `bytes provider = 3;`

      Specified by:
      :   `getProvider` in interface `Chain.Transaction.ContractOrBuilder`

      Returns:
      :   The provider.
    - #### getContractName

      ```
      public com.google.protobuf.ByteString getContractName()
      ```

      `bytes ContractName = 4;`

      Specified by:
      :   `getContractName` in interface `Chain.Transaction.ContractOrBuilder`

      Returns:
      :   The contractName.
    - #### getPermissionId

      ```
      public int getPermissionId()
      ```

      `int32 Permission_id = 5;`

      Specified by:
      :   `getPermissionId` in interface `Chain.Transaction.ContractOrBuilder`

      Returns:
      :   The permissionId.
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
      public static Chain.Transaction.Contract parseFrom(java.nio.ByteBuffer data)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction.Contract parseFrom(java.nio.ByteBuffer data,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction.Contract parseFrom(com.google.protobuf.ByteString data)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction.Contract parseFrom(com.google.protobuf.ByteString data,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction.Contract parseFrom(byte[] data)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction.Contract parseFrom(byte[] data,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Chain.Transaction.Contract parseFrom(java.io.InputStream input)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Chain.Transaction.Contract parseFrom(java.io.InputStream input,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Chain.Transaction.Contract parseDelimitedFrom(java.io.InputStream input)
                                                           throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Chain.Transaction.Contract parseDelimitedFrom(java.io.InputStream input,
                                                                  com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                           throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Chain.Transaction.Contract parseFrom(com.google.protobuf.CodedInputStream input)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Chain.Transaction.Contract parseFrom(com.google.protobuf.CodedInputStream input,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Chain.Transaction.Contract.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Chain.Transaction.Contract.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Chain.Transaction.Contract.Builder newBuilder(Chain.Transaction.Contract prototype)
      ```
    - #### toBuilder

      ```
      public Chain.Transaction.Contract.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Chain.Transaction.Contract.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Chain.Transaction.Contract getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Chain.Transaction.Contract> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Chain.Transaction.Contract> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Chain.Transaction.Contract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`