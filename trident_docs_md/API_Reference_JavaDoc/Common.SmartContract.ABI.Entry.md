

org.tron.trident.proto

## Class Common.SmartContract.ABI.Entry

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Common.SmartContract.ABI.Entry

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Common.SmartContract.ABI.EntryOrBuilder](../../../../org/tron/trident/proto/Common.SmartContract.ABI.EntryOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Common.SmartContract.ABI](../../../../org/tron/trident/proto/Common.SmartContract.ABI.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Common.SmartContract.ABI.Entry
  extends com.google.protobuf.GeneratedMessageV3
  implements Common.SmartContract.ABI.EntryOrBuilder
  ```

  Protobuf type `protocol.SmartContract.ABI.Entry`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Common.SmartContract.ABI.Entry)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Common.SmartContract.ABI.Entry.Builder` Protobuf type `protocol.SmartContract.ABI.Entry` |
    | `static class` | `Common.SmartContract.ABI.Entry.EntryType` Protobuf enum `protocol.SmartContract.ABI.Entry.EntryType` |
    | `static class` | `Common.SmartContract.ABI.Entry.Param` Protobuf type `protocol.SmartContract.ABI.Entry.Param` |
    | `static interface` | `Common.SmartContract.ABI.Entry.ParamOrBuilder` |
    | `static class` | `Common.SmartContract.ABI.Entry.StateMutabilityType` Protobuf enum `protocol.SmartContract.ABI.Entry.StateMutabilityType` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `ANONYMOUS_FIELD_NUMBER` |
    | `static int` | `CONSTANT_FIELD_NUMBER` |
    | `static int` | `INPUTS_FIELD_NUMBER` |
    | `static int` | `NAME_FIELD_NUMBER` |
    | `static int` | `OUTPUTS_FIELD_NUMBER` |
    | `static int` | `PAYABLE_FIELD_NUMBER` |
    | `static int` | `STATEMUTABILITY_FIELD_NUMBER` |
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
    | `boolean` | `getAnonymous()` `bool anonymous = 1;` |
    | `boolean` | `getConstant()` `bool constant = 2;` |
    | `static Common.SmartContract.ABI.Entry` | `getDefaultInstance()` |
    | `Common.SmartContract.ABI.Entry` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `Common.SmartContract.ABI.Entry.Param` | `getInputs(int index)` `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;` |
    | `int` | `getInputsCount()` `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;` |
    | `java.util.List<Common.SmartContract.ABI.Entry.Param>` | `getInputsList()` `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;` |
    | `Common.SmartContract.ABI.Entry.ParamOrBuilder` | `getInputsOrBuilder(int index)` `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;` |
    | `java.util.List<? extends Common.SmartContract.ABI.Entry.ParamOrBuilder>` | `getInputsOrBuilderList()` `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;` |
    | `java.lang.String` | `getName()` `string name = 3;` |
    | `com.google.protobuf.ByteString` | `getNameBytes()` `string name = 3;` |
    | `Common.SmartContract.ABI.Entry.Param` | `getOutputs(int index)` `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;` |
    | `int` | `getOutputsCount()` `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;` |
    | `java.util.List<Common.SmartContract.ABI.Entry.Param>` | `getOutputsList()` `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;` |
    | `Common.SmartContract.ABI.Entry.ParamOrBuilder` | `getOutputsOrBuilder(int index)` `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;` |
    | `java.util.List<? extends Common.SmartContract.ABI.Entry.ParamOrBuilder>` | `getOutputsOrBuilderList()` `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;` |
    | `com.google.protobuf.Parser<Common.SmartContract.ABI.Entry>` | `getParserForType()` |
    | `boolean` | `getPayable()` `bool payable = 7;` |
    | `int` | `getSerializedSize()` |
    | `Common.SmartContract.ABI.Entry.StateMutabilityType` | `getStateMutability()` `.protocol.SmartContract.ABI.Entry.StateMutabilityType stateMutability = 8;` |
    | `int` | `getStateMutabilityValue()` `.protocol.SmartContract.ABI.Entry.StateMutabilityType stateMutability = 8;` |
    | `Common.SmartContract.ABI.Entry.EntryType` | `getType()` `.protocol.SmartContract.ABI.Entry.EntryType type = 6;` |
    | `int` | `getTypeValue()` `.protocol.SmartContract.ABI.Entry.EntryType type = 6;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Common.SmartContract.ABI.Entry.Builder` | `newBuilder()` |
    | `static Common.SmartContract.ABI.Entry.Builder` | `newBuilder(Common.SmartContract.ABI.Entry prototype)` |
    | `Common.SmartContract.ABI.Entry.Builder` | `newBuilderForType()` |
    | `protected Common.SmartContract.ABI.Entry.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Common.SmartContract.ABI.Entry` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Common.SmartContract.ABI.Entry` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.SmartContract.ABI.Entry` | `parseFrom(byte[] data)` |
    | `static Common.SmartContract.ABI.Entry` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.SmartContract.ABI.Entry` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Common.SmartContract.ABI.Entry` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.SmartContract.ABI.Entry` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Common.SmartContract.ABI.Entry` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.SmartContract.ABI.Entry` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Common.SmartContract.ABI.Entry` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Common.SmartContract.ABI.Entry` | `parseFrom(java.io.InputStream input)` |
    | `static Common.SmartContract.ABI.Entry` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Common.SmartContract.ABI.Entry>` | `parser()` |
    | `Common.SmartContract.ABI.Entry.Builder` | `toBuilder()` |
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

    - #### ANONYMOUS\_FIELD\_NUMBER

      ```
      public static final int ANONYMOUS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ABI.Entry.ANONYMOUS_FIELD_NUMBER)
    - #### CONSTANT\_FIELD\_NUMBER

      ```
      public static final int CONSTANT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ABI.Entry.CONSTANT_FIELD_NUMBER)
    - #### NAME\_FIELD\_NUMBER

      ```
      public static final int NAME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ABI.Entry.NAME_FIELD_NUMBER)
    - #### INPUTS\_FIELD\_NUMBER

      ```
      public static final int INPUTS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ABI.Entry.INPUTS_FIELD_NUMBER)
    - #### OUTPUTS\_FIELD\_NUMBER

      ```
      public static final int OUTPUTS_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ABI.Entry.OUTPUTS_FIELD_NUMBER)
    - #### TYPE\_FIELD\_NUMBER

      ```
      public static final int TYPE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ABI.Entry.TYPE_FIELD_NUMBER)
    - #### PAYABLE\_FIELD\_NUMBER

      ```
      public static final int PAYABLE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ABI.Entry.PAYABLE_FIELD_NUMBER)
    - #### STATEMUTABILITY\_FIELD\_NUMBER

      ```
      public static final int STATEMUTABILITY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ABI.Entry.STATEMUTABILITY_FIELD_NUMBER)
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
    - #### getAnonymous

      ```
      public boolean getAnonymous()
      ```

      `bool anonymous = 1;`

      Specified by:
      :   `getAnonymous` in interface `Common.SmartContract.ABI.EntryOrBuilder`

      Returns:
      :   The anonymous.
    - #### getConstant

      ```
      public boolean getConstant()
      ```

      `bool constant = 2;`

      Specified by:
      :   `getConstant` in interface `Common.SmartContract.ABI.EntryOrBuilder`

      Returns:
      :   The constant.
    - #### getName

      ```
      public java.lang.String getName()
      ```

      `string name = 3;`

      Specified by:
      :   `getName` in interface `Common.SmartContract.ABI.EntryOrBuilder`

      Returns:
      :   The name.
    - #### getNameBytes

      ```
      public com.google.protobuf.ByteString getNameBytes()
      ```

      `string name = 3;`

      Specified by:
      :   `getNameBytes` in interface `Common.SmartContract.ABI.EntryOrBuilder`

      Returns:
      :   The bytes for name.
    - #### getInputsList

      ```
      public java.util.List<Common.SmartContract.ABI.Entry.Param> getInputsList()
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`

      Specified by:
      :   `getInputsList` in interface `Common.SmartContract.ABI.EntryOrBuilder`
    - #### getInputsOrBuilderList

      ```
      public java.util.List<? extends Common.SmartContract.ABI.Entry.ParamOrBuilder> getInputsOrBuilderList()
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`

      Specified by:
      :   `getInputsOrBuilderList` in interface `Common.SmartContract.ABI.EntryOrBuilder`
    - #### getInputsCount

      ```
      public int getInputsCount()
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`

      Specified by:
      :   `getInputsCount` in interface `Common.SmartContract.ABI.EntryOrBuilder`
    - #### getInputs

      ```
      public Common.SmartContract.ABI.Entry.Param getInputs(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`

      Specified by:
      :   `getInputs` in interface `Common.SmartContract.ABI.EntryOrBuilder`
    - #### getInputsOrBuilder

      ```
      public Common.SmartContract.ABI.Entry.ParamOrBuilder getInputsOrBuilder(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`

      Specified by:
      :   `getInputsOrBuilder` in interface `Common.SmartContract.ABI.EntryOrBuilder`
    - #### getOutputsList

      ```
      public java.util.List<Common.SmartContract.ABI.Entry.Param> getOutputsList()
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`

      Specified by:
      :   `getOutputsList` in interface `Common.SmartContract.ABI.EntryOrBuilder`
    - #### getOutputsOrBuilderList

      ```
      public java.util.List<? extends Common.SmartContract.ABI.Entry.ParamOrBuilder> getOutputsOrBuilderList()
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`

      Specified by:
      :   `getOutputsOrBuilderList` in interface `Common.SmartContract.ABI.EntryOrBuilder`
    - #### getOutputsCount

      ```
      public int getOutputsCount()
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`

      Specified by:
      :   `getOutputsCount` in interface `Common.SmartContract.ABI.EntryOrBuilder`
    - #### getOutputs

      ```
      public Common.SmartContract.ABI.Entry.Param getOutputs(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`

      Specified by:
      :   `getOutputs` in interface `Common.SmartContract.ABI.EntryOrBuilder`
    - #### getOutputsOrBuilder

      ```
      public Common.SmartContract.ABI.Entry.ParamOrBuilder getOutputsOrBuilder(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`

      Specified by:
      :   `getOutputsOrBuilder` in interface `Common.SmartContract.ABI.EntryOrBuilder`
    - #### getTypeValue

      ```
      public int getTypeValue()
      ```

      `.protocol.SmartContract.ABI.Entry.EntryType type = 6;`

      Specified by:
      :   `getTypeValue` in interface `Common.SmartContract.ABI.EntryOrBuilder`

      Returns:
      :   The enum numeric value on the wire for type.
    - #### getType

      ```
      public Common.SmartContract.ABI.Entry.EntryType getType()
      ```

      `.protocol.SmartContract.ABI.Entry.EntryType type = 6;`

      Specified by:
      :   `getType` in interface `Common.SmartContract.ABI.EntryOrBuilder`

      Returns:
      :   The type.
    - #### getPayable

      ```
      public boolean getPayable()
      ```

      `bool payable = 7;`

      Specified by:
      :   `getPayable` in interface `Common.SmartContract.ABI.EntryOrBuilder`

      Returns:
      :   The payable.
    - #### getStateMutabilityValue

      ```
      public int getStateMutabilityValue()
      ```

      `.protocol.SmartContract.ABI.Entry.StateMutabilityType stateMutability = 8;`

      Specified by:
      :   `getStateMutabilityValue` in interface `Common.SmartContract.ABI.EntryOrBuilder`

      Returns:
      :   The enum numeric value on the wire for stateMutability.
    - #### getStateMutability

      ```
      public Common.SmartContract.ABI.Entry.StateMutabilityType getStateMutability()
      ```

      `.protocol.SmartContract.ABI.Entry.StateMutabilityType stateMutability = 8;`

      Specified by:
      :   `getStateMutability` in interface `Common.SmartContract.ABI.EntryOrBuilder`

      Returns:
      :   The stateMutability.
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
      public static Common.SmartContract.ABI.Entry parseFrom(java.nio.ByteBuffer data)
                                                      throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.SmartContract.ABI.Entry parseFrom(java.nio.ByteBuffer data,
                                                             com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                      throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.SmartContract.ABI.Entry parseFrom(com.google.protobuf.ByteString data)
                                                      throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.SmartContract.ABI.Entry parseFrom(com.google.protobuf.ByteString data,
                                                             com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                      throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.SmartContract.ABI.Entry parseFrom(byte[] data)
                                                      throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.SmartContract.ABI.Entry parseFrom(byte[] data,
                                                             com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                      throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Common.SmartContract.ABI.Entry parseFrom(java.io.InputStream input)
                                                      throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Common.SmartContract.ABI.Entry parseFrom(java.io.InputStream input,
                                                             com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                      throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Common.SmartContract.ABI.Entry parseDelimitedFrom(java.io.InputStream input)
                                                               throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Common.SmartContract.ABI.Entry parseDelimitedFrom(java.io.InputStream input,
                                                                      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                               throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Common.SmartContract.ABI.Entry parseFrom(com.google.protobuf.CodedInputStream input)
                                                      throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Common.SmartContract.ABI.Entry parseFrom(com.google.protobuf.CodedInputStream input,
                                                             com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                      throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Common.SmartContract.ABI.Entry.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Common.SmartContract.ABI.Entry.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Common.SmartContract.ABI.Entry.Builder newBuilder(Common.SmartContract.ABI.Entry prototype)
      ```
    - #### toBuilder

      ```
      public Common.SmartContract.ABI.Entry.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Common.SmartContract.ABI.Entry.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Common.SmartContract.ABI.Entry getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Common.SmartContract.ABI.Entry> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Common.SmartContract.ABI.Entry> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Common.SmartContract.ABI.Entry getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`