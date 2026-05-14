

org.tron.trident.proto

## Class Common.SmartContract.ABI.Entry.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Common.SmartContract.ABI.Entry.Builder](../../../../org/tron/trident/proto/Common.SmartContract.ABI.Entry.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Common.SmartContract.ABI.Entry.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Common.SmartContract.ABI.EntryOrBuilder](../../../../org/tron/trident/proto/Common.SmartContract.ABI.EntryOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Common.SmartContract.ABI.Entry](../../../../org/tron/trident/proto/Common.SmartContract.ABI.Entry.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Common.SmartContract.ABI.Entry.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Builder>
  implements Common.SmartContract.ABI.EntryOrBuilder
  ```

  Protobuf type `protocol.SmartContract.ABI.Entry`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Common.SmartContract.ABI.Entry.Builder` | `addAllInputs(java.lang.Iterable<? extends Common.SmartContract.ABI.Entry.Param> values)` `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `addAllOutputs(java.lang.Iterable<? extends Common.SmartContract.ABI.Entry.Param> values)` `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `addInputs(Common.SmartContract.ABI.Entry.Param.Builder builderForValue)` `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `addInputs(Common.SmartContract.ABI.Entry.Param value)` `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `addInputs(int index, Common.SmartContract.ABI.Entry.Param.Builder builderForValue)` `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `addInputs(int index, Common.SmartContract.ABI.Entry.Param value)` `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;` |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `addInputsBuilder()` `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;` |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `addInputsBuilder(int index)` `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `addOutputs(Common.SmartContract.ABI.Entry.Param.Builder builderForValue)` `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `addOutputs(Common.SmartContract.ABI.Entry.Param value)` `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `addOutputs(int index, Common.SmartContract.ABI.Entry.Param.Builder builderForValue)` `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `addOutputs(int index, Common.SmartContract.ABI.Entry.Param value)` `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;` |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `addOutputsBuilder()` `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;` |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `addOutputsBuilder(int index)` `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Common.SmartContract.ABI.Entry` | `build()` |
    | `Common.SmartContract.ABI.Entry` | `buildPartial()` |
    | `Common.SmartContract.ABI.Entry.Builder` | `clear()` |
    | `Common.SmartContract.ABI.Entry.Builder` | `clearAnonymous()` `bool anonymous = 1;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `clearConstant()` `bool constant = 2;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Common.SmartContract.ABI.Entry.Builder` | `clearInputs()` `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `clearName()` `string name = 3;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Common.SmartContract.ABI.Entry.Builder` | `clearOutputs()` `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `clearPayable()` `bool payable = 7;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `clearStateMutability()` `.protocol.SmartContract.ABI.Entry.StateMutabilityType stateMutability = 8;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `clearType()` `.protocol.SmartContract.ABI.Entry.EntryType type = 6;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `clone()` |
    | `boolean` | `getAnonymous()` `bool anonymous = 1;` |
    | `boolean` | `getConstant()` `bool constant = 2;` |
    | `Common.SmartContract.ABI.Entry` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Common.SmartContract.ABI.Entry.Param` | `getInputs(int index)` `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;` |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `getInputsBuilder(int index)` `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;` |
    | `java.util.List<Common.SmartContract.ABI.Entry.Param.Builder>` | `getInputsBuilderList()` `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;` |
    | `int` | `getInputsCount()` `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;` |
    | `java.util.List<Common.SmartContract.ABI.Entry.Param>` | `getInputsList()` `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;` |
    | `Common.SmartContract.ABI.Entry.ParamOrBuilder` | `getInputsOrBuilder(int index)` `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;` |
    | `java.util.List<? extends Common.SmartContract.ABI.Entry.ParamOrBuilder>` | `getInputsOrBuilderList()` `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;` |
    | `java.lang.String` | `getName()` `string name = 3;` |
    | `com.google.protobuf.ByteString` | `getNameBytes()` `string name = 3;` |
    | `Common.SmartContract.ABI.Entry.Param` | `getOutputs(int index)` `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;` |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `getOutputsBuilder(int index)` `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;` |
    | `java.util.List<Common.SmartContract.ABI.Entry.Param.Builder>` | `getOutputsBuilderList()` `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;` |
    | `int` | `getOutputsCount()` `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;` |
    | `java.util.List<Common.SmartContract.ABI.Entry.Param>` | `getOutputsList()` `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;` |
    | `Common.SmartContract.ABI.Entry.ParamOrBuilder` | `getOutputsOrBuilder(int index)` `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;` |
    | `java.util.List<? extends Common.SmartContract.ABI.Entry.ParamOrBuilder>` | `getOutputsOrBuilderList()` `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;` |
    | `boolean` | `getPayable()` `bool payable = 7;` |
    | `Common.SmartContract.ABI.Entry.StateMutabilityType` | `getStateMutability()` `.protocol.SmartContract.ABI.Entry.StateMutabilityType stateMutability = 8;` |
    | `int` | `getStateMutabilityValue()` `.protocol.SmartContract.ABI.Entry.StateMutabilityType stateMutability = 8;` |
    | `Common.SmartContract.ABI.Entry.EntryType` | `getType()` `.protocol.SmartContract.ABI.Entry.EntryType type = 6;` |
    | `int` | `getTypeValue()` `.protocol.SmartContract.ABI.Entry.EntryType type = 6;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Common.SmartContract.ABI.Entry.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Common.SmartContract.ABI.Entry.Builder` | `mergeFrom(Common.SmartContract.ABI.Entry other)` |
    | `Common.SmartContract.ABI.Entry.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Common.SmartContract.ABI.Entry.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Common.SmartContract.ABI.Entry.Builder` | `removeInputs(int index)` `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `removeOutputs(int index)` `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `setAnonymous(boolean value)` `bool anonymous = 1;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `setConstant(boolean value)` `bool constant = 2;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Common.SmartContract.ABI.Entry.Builder` | `setInputs(int index, Common.SmartContract.ABI.Entry.Param.Builder builderForValue)` `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `setInputs(int index, Common.SmartContract.ABI.Entry.Param value)` `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `setName(java.lang.String value)` `string name = 3;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `setNameBytes(com.google.protobuf.ByteString value)` `string name = 3;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `setOutputs(int index, Common.SmartContract.ABI.Entry.Param.Builder builderForValue)` `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `setOutputs(int index, Common.SmartContract.ABI.Entry.Param value)` `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `setPayable(boolean value)` `bool payable = 7;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Common.SmartContract.ABI.Entry.Builder` | `setStateMutability(Common.SmartContract.ABI.Entry.StateMutabilityType value)` `.protocol.SmartContract.ABI.Entry.StateMutabilityType stateMutability = 8;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `setStateMutabilityValue(int value)` `.protocol.SmartContract.ABI.Entry.StateMutabilityType stateMutability = 8;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `setType(Common.SmartContract.ABI.Entry.EntryType value)` `.protocol.SmartContract.ABI.Entry.EntryType type = 6;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `setTypeValue(int value)` `.protocol.SmartContract.ABI.Entry.EntryType type = 6;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

    - ### Methods inherited from class com.google.protobuf.GeneratedMessageV3.Builder

      `getAllFields, getField, getFieldBuilder, getOneofFieldDescriptor, getParentForChildren, getRepeatedField, getRepeatedFieldBuilder, getRepeatedFieldCount, getUnknownFields, getUnknownFieldSetBuilder, hasField, hasOneof, internalGetMapField, internalGetMapFieldReflection, internalGetMutableMapField, internalGetMutableMapFieldReflection, isClean, markClean, mergeUnknownLengthDelimitedField, mergeUnknownVarintField, newBuilderForField, onBuilt, onChanged, parseUnknownField, setUnknownFieldSetBuilder, setUnknownFieldsProto3`
    - ### Methods inherited from class com.google.protobuf.AbstractMessage.Builder

      `findInitializationErrors, getInitializationErrorString, internalMergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, newUninitializedMessageException, toString`
    - ### Methods inherited from class com.google.protobuf.AbstractMessageLite.Builder

      `addAll, addAll, mergeDelimitedFrom, mergeDelimitedFrom, newUninitializedMessageException`
    - ### Methods inherited from class java.lang.Object

      `equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`
    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.Message.Builder

      `mergeDelimitedFrom, mergeDelimitedFrom`

* + ### Method Detail

    - #### getDescriptor

      ```
      public static final com.google.protobuf.Descriptors.Descriptor getDescriptor()
      ```
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Builder>`
    - #### clear

      ```
      public Common.SmartContract.ABI.Entry.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Common.SmartContract.ABI.Entry getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Common.SmartContract.ABI.Entry build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Common.SmartContract.ABI.Entry buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Common.SmartContract.ABI.Entry.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Builder>`
    - #### setField

      ```
      public Common.SmartContract.ABI.Entry.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                             java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Builder>`
    - #### clearField

      ```
      public Common.SmartContract.ABI.Entry.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Builder>`
    - #### clearOneof

      ```
      public Common.SmartContract.ABI.Entry.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Builder>`
    - #### setRepeatedField

      ```
      public Common.SmartContract.ABI.Entry.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     int index,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Builder>`
    - #### addRepeatedField

      ```
      public Common.SmartContract.ABI.Entry.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Builder>`
    - #### mergeFrom

      ```
      public Common.SmartContract.ABI.Entry.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Common.SmartContract.ABI.Entry.Builder>`
    - #### mergeFrom

      ```
      public Common.SmartContract.ABI.Entry.Builder mergeFrom(Common.SmartContract.ABI.Entry other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Builder>`
    - #### mergeFrom

      ```
      public Common.SmartContract.ABI.Entry.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Common.SmartContract.ABI.Entry.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getAnonymous

      ```
      public boolean getAnonymous()
      ```

      `bool anonymous = 1;`

      Specified by:
      :   `getAnonymous` in interface `Common.SmartContract.ABI.EntryOrBuilder`

      Returns:
      :   The anonymous.
    - #### setAnonymous

      ```
      public Common.SmartContract.ABI.Entry.Builder setAnonymous(boolean value)
      ```

      `bool anonymous = 1;`

      Parameters:
      :   `value` - The anonymous to set.

      Returns:
      :   This builder for chaining.
    - #### clearAnonymous

      ```
      public Common.SmartContract.ABI.Entry.Builder clearAnonymous()
      ```

      `bool anonymous = 1;`

      Returns:
      :   This builder for chaining.
    - #### getConstant

      ```
      public boolean getConstant()
      ```

      `bool constant = 2;`

      Specified by:
      :   `getConstant` in interface `Common.SmartContract.ABI.EntryOrBuilder`

      Returns:
      :   The constant.
    - #### setConstant

      ```
      public Common.SmartContract.ABI.Entry.Builder setConstant(boolean value)
      ```

      `bool constant = 2;`

      Parameters:
      :   `value` - The constant to set.

      Returns:
      :   This builder for chaining.
    - #### clearConstant

      ```
      public Common.SmartContract.ABI.Entry.Builder clearConstant()
      ```

      `bool constant = 2;`

      Returns:
      :   This builder for chaining.
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
    - #### setName

      ```
      public Common.SmartContract.ABI.Entry.Builder setName(java.lang.String value)
      ```

      `string name = 3;`

      Parameters:
      :   `value` - The name to set.

      Returns:
      :   This builder for chaining.
    - #### clearName

      ```
      public Common.SmartContract.ABI.Entry.Builder clearName()
      ```

      `string name = 3;`

      Returns:
      :   This builder for chaining.
    - #### setNameBytes

      ```
      public Common.SmartContract.ABI.Entry.Builder setNameBytes(com.google.protobuf.ByteString value)
      ```

      `string name = 3;`

      Parameters:
      :   `value` - The bytes for name to set.

      Returns:
      :   This builder for chaining.
    - #### getInputsList

      ```
      public java.util.List<Common.SmartContract.ABI.Entry.Param> getInputsList()
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`

      Specified by:
      :   `getInputsList` in interface `Common.SmartContract.ABI.EntryOrBuilder`
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
    - #### setInputs

      ```
      public Common.SmartContract.ABI.Entry.Builder setInputs(int index,
                                                              Common.SmartContract.ABI.Entry.Param value)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`
    - #### setInputs

      ```
      public Common.SmartContract.ABI.Entry.Builder setInputs(int index,
                                                              Common.SmartContract.ABI.Entry.Param.Builder builderForValue)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`
    - #### addInputs

      ```
      public Common.SmartContract.ABI.Entry.Builder addInputs(Common.SmartContract.ABI.Entry.Param value)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`
    - #### addInputs

      ```
      public Common.SmartContract.ABI.Entry.Builder addInputs(int index,
                                                              Common.SmartContract.ABI.Entry.Param value)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`
    - #### addInputs

      ```
      public Common.SmartContract.ABI.Entry.Builder addInputs(Common.SmartContract.ABI.Entry.Param.Builder builderForValue)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`
    - #### addInputs

      ```
      public Common.SmartContract.ABI.Entry.Builder addInputs(int index,
                                                              Common.SmartContract.ABI.Entry.Param.Builder builderForValue)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`
    - #### addAllInputs

      ```
      public Common.SmartContract.ABI.Entry.Builder addAllInputs(java.lang.Iterable<? extends Common.SmartContract.ABI.Entry.Param> values)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`
    - #### clearInputs

      ```
      public Common.SmartContract.ABI.Entry.Builder clearInputs()
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`
    - #### removeInputs

      ```
      public Common.SmartContract.ABI.Entry.Builder removeInputs(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`
    - #### getInputsBuilder

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder getInputsBuilder(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`
    - #### getInputsOrBuilder

      ```
      public Common.SmartContract.ABI.Entry.ParamOrBuilder getInputsOrBuilder(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`

      Specified by:
      :   `getInputsOrBuilder` in interface `Common.SmartContract.ABI.EntryOrBuilder`
    - #### getInputsOrBuilderList

      ```
      public java.util.List<? extends Common.SmartContract.ABI.Entry.ParamOrBuilder> getInputsOrBuilderList()
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`

      Specified by:
      :   `getInputsOrBuilderList` in interface `Common.SmartContract.ABI.EntryOrBuilder`
    - #### addInputsBuilder

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder addInputsBuilder()
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`
    - #### addInputsBuilder

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder addInputsBuilder(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`
    - #### getInputsBuilderList

      ```
      public java.util.List<Common.SmartContract.ABI.Entry.Param.Builder> getInputsBuilderList()
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`
    - #### getOutputsList

      ```
      public java.util.List<Common.SmartContract.ABI.Entry.Param> getOutputsList()
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`

      Specified by:
      :   `getOutputsList` in interface `Common.SmartContract.ABI.EntryOrBuilder`
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
    - #### setOutputs

      ```
      public Common.SmartContract.ABI.Entry.Builder setOutputs(int index,
                                                               Common.SmartContract.ABI.Entry.Param value)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`
    - #### setOutputs

      ```
      public Common.SmartContract.ABI.Entry.Builder setOutputs(int index,
                                                               Common.SmartContract.ABI.Entry.Param.Builder builderForValue)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`
    - #### addOutputs

      ```
      public Common.SmartContract.ABI.Entry.Builder addOutputs(Common.SmartContract.ABI.Entry.Param value)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`
    - #### addOutputs

      ```
      public Common.SmartContract.ABI.Entry.Builder addOutputs(int index,
                                                               Common.SmartContract.ABI.Entry.Param value)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`
    - #### addOutputs

      ```
      public Common.SmartContract.ABI.Entry.Builder addOutputs(Common.SmartContract.ABI.Entry.Param.Builder builderForValue)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`
    - #### addOutputs

      ```
      public Common.SmartContract.ABI.Entry.Builder addOutputs(int index,
                                                               Common.SmartContract.ABI.Entry.Param.Builder builderForValue)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`
    - #### addAllOutputs

      ```
      public Common.SmartContract.ABI.Entry.Builder addAllOutputs(java.lang.Iterable<? extends Common.SmartContract.ABI.Entry.Param> values)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`
    - #### clearOutputs

      ```
      public Common.SmartContract.ABI.Entry.Builder clearOutputs()
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`
    - #### removeOutputs

      ```
      public Common.SmartContract.ABI.Entry.Builder removeOutputs(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`
    - #### getOutputsBuilder

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder getOutputsBuilder(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`
    - #### getOutputsOrBuilder

      ```
      public Common.SmartContract.ABI.Entry.ParamOrBuilder getOutputsOrBuilder(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`

      Specified by:
      :   `getOutputsOrBuilder` in interface `Common.SmartContract.ABI.EntryOrBuilder`
    - #### getOutputsOrBuilderList

      ```
      public java.util.List<? extends Common.SmartContract.ABI.Entry.ParamOrBuilder> getOutputsOrBuilderList()
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`

      Specified by:
      :   `getOutputsOrBuilderList` in interface `Common.SmartContract.ABI.EntryOrBuilder`
    - #### addOutputsBuilder

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder addOutputsBuilder()
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`
    - #### addOutputsBuilder

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder addOutputsBuilder(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`
    - #### getOutputsBuilderList

      ```
      public java.util.List<Common.SmartContract.ABI.Entry.Param.Builder> getOutputsBuilderList()
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`
    - #### getTypeValue

      ```
      public int getTypeValue()
      ```

      `.protocol.SmartContract.ABI.Entry.EntryType type = 6;`

      Specified by:
      :   `getTypeValue` in interface `Common.SmartContract.ABI.EntryOrBuilder`

      Returns:
      :   The enum numeric value on the wire for type.
    - #### setTypeValue

      ```
      public Common.SmartContract.ABI.Entry.Builder setTypeValue(int value)
      ```

      `.protocol.SmartContract.ABI.Entry.EntryType type = 6;`

      Parameters:
      :   `value` - The enum numeric value on the wire for type to set.

      Returns:
      :   This builder for chaining.
    - #### getType

      ```
      public Common.SmartContract.ABI.Entry.EntryType getType()
      ```

      `.protocol.SmartContract.ABI.Entry.EntryType type = 6;`

      Specified by:
      :   `getType` in interface `Common.SmartContract.ABI.EntryOrBuilder`

      Returns:
      :   The type.
    - #### setType

      ```
      public Common.SmartContract.ABI.Entry.Builder setType(Common.SmartContract.ABI.Entry.EntryType value)
      ```

      `.protocol.SmartContract.ABI.Entry.EntryType type = 6;`

      Parameters:
      :   `value` - The type to set.

      Returns:
      :   This builder for chaining.
    - #### clearType

      ```
      public Common.SmartContract.ABI.Entry.Builder clearType()
      ```

      `.protocol.SmartContract.ABI.Entry.EntryType type = 6;`

      Returns:
      :   This builder for chaining.
    - #### getPayable

      ```
      public boolean getPayable()
      ```

      `bool payable = 7;`

      Specified by:
      :   `getPayable` in interface `Common.SmartContract.ABI.EntryOrBuilder`

      Returns:
      :   The payable.
    - #### setPayable

      ```
      public Common.SmartContract.ABI.Entry.Builder setPayable(boolean value)
      ```

      `bool payable = 7;`

      Parameters:
      :   `value` - The payable to set.

      Returns:
      :   This builder for chaining.
    - #### clearPayable

      ```
      public Common.SmartContract.ABI.Entry.Builder clearPayable()
      ```

      `bool payable = 7;`

      Returns:
      :   This builder for chaining.
    - #### getStateMutabilityValue

      ```
      public int getStateMutabilityValue()
      ```

      `.protocol.SmartContract.ABI.Entry.StateMutabilityType stateMutability = 8;`

      Specified by:
      :   `getStateMutabilityValue` in interface `Common.SmartContract.ABI.EntryOrBuilder`

      Returns:
      :   The enum numeric value on the wire for stateMutability.
    - #### setStateMutabilityValue

      ```
      public Common.SmartContract.ABI.Entry.Builder setStateMutabilityValue(int value)
      ```

      `.protocol.SmartContract.ABI.Entry.StateMutabilityType stateMutability = 8;`

      Parameters:
      :   `value` - The enum numeric value on the wire for stateMutability to set.

      Returns:
      :   This builder for chaining.
    - #### getStateMutability

      ```
      public Common.SmartContract.ABI.Entry.StateMutabilityType getStateMutability()
      ```

      `.protocol.SmartContract.ABI.Entry.StateMutabilityType stateMutability = 8;`

      Specified by:
      :   `getStateMutability` in interface `Common.SmartContract.ABI.EntryOrBuilder`

      Returns:
      :   The stateMutability.
    - #### setStateMutability

      ```
      public Common.SmartContract.ABI.Entry.Builder setStateMutability(Common.SmartContract.ABI.Entry.StateMutabilityType value)
      ```

      `.protocol.SmartContract.ABI.Entry.StateMutabilityType stateMutability = 8;`

      Parameters:
      :   `value` - The stateMutability to set.

      Returns:
      :   This builder for chaining.
    - #### clearStateMutability

      ```
      public Common.SmartContract.ABI.Entry.Builder clearStateMutability()
      ```

      `.protocol.SmartContract.ABI.Entry.StateMutabilityType stateMutability = 8;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Common.SmartContract.ABI.Entry.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Builder>`
    - #### mergeUnknownFields

      ```
      public final Common.SmartContract.ABI.Entry.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Builder>`