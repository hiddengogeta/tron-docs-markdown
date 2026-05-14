

org.tron.trident.proto

## Interface Common.SmartContract.ABI.EntryOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Common.SmartContract.ABI.Entry](../../../../org/tron/trident/proto/Common.SmartContract.ABI.Entry.html "class in org.tron.trident.proto"), [Common.SmartContract.ABI.Entry.Builder](../../../../org/tron/trident/proto/Common.SmartContract.ABI.Entry.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Common.SmartContract.ABI](../../../../org/tron/trident/proto/Common.SmartContract.ABI.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Common.SmartContract.ABI.EntryOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `boolean` | `getAnonymous()` `bool anonymous = 1;` |
    | `boolean` | `getConstant()` `bool constant = 2;` |
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
    | `boolean` | `getPayable()` `bool payable = 7;` |
    | `Common.SmartContract.ABI.Entry.StateMutabilityType` | `getStateMutability()` `.protocol.SmartContract.ABI.Entry.StateMutabilityType stateMutability = 8;` |
    | `int` | `getStateMutabilityValue()` `.protocol.SmartContract.ABI.Entry.StateMutabilityType stateMutability = 8;` |
    | `Common.SmartContract.ABI.Entry.EntryType` | `getType()` `.protocol.SmartContract.ABI.Entry.EntryType type = 6;` |
    | `int` | `getTypeValue()` `.protocol.SmartContract.ABI.Entry.EntryType type = 6;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getAnonymous

      ```
      boolean getAnonymous()
      ```

      `bool anonymous = 1;`

      Returns:
      :   The anonymous.
    - #### getConstant

      ```
      boolean getConstant()
      ```

      `bool constant = 2;`

      Returns:
      :   The constant.
    - #### getName

      ```
      java.lang.String getName()
      ```

      `string name = 3;`

      Returns:
      :   The name.
    - #### getNameBytes

      ```
      com.google.protobuf.ByteString getNameBytes()
      ```

      `string name = 3;`

      Returns:
      :   The bytes for name.
    - #### getInputsList

      ```
      java.util.List<Common.SmartContract.ABI.Entry.Param> getInputsList()
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`
    - #### getInputs

      ```
      Common.SmartContract.ABI.Entry.Param getInputs(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`
    - #### getInputsCount

      ```
      int getInputsCount()
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`
    - #### getInputsOrBuilderList

      ```
      java.util.List<? extends Common.SmartContract.ABI.Entry.ParamOrBuilder> getInputsOrBuilderList()
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`
    - #### getInputsOrBuilder

      ```
      Common.SmartContract.ABI.Entry.ParamOrBuilder getInputsOrBuilder(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param inputs = 4;`
    - #### getOutputsList

      ```
      java.util.List<Common.SmartContract.ABI.Entry.Param> getOutputsList()
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`
    - #### getOutputs

      ```
      Common.SmartContract.ABI.Entry.Param getOutputs(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`
    - #### getOutputsCount

      ```
      int getOutputsCount()
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`
    - #### getOutputsOrBuilderList

      ```
      java.util.List<? extends Common.SmartContract.ABI.Entry.ParamOrBuilder> getOutputsOrBuilderList()
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`
    - #### getOutputsOrBuilder

      ```
      Common.SmartContract.ABI.Entry.ParamOrBuilder getOutputsOrBuilder(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry.Param outputs = 5;`
    - #### getTypeValue

      ```
      int getTypeValue()
      ```

      `.protocol.SmartContract.ABI.Entry.EntryType type = 6;`

      Returns:
      :   The enum numeric value on the wire for type.
    - #### getType

      ```
      Common.SmartContract.ABI.Entry.EntryType getType()
      ```

      `.protocol.SmartContract.ABI.Entry.EntryType type = 6;`

      Returns:
      :   The type.
    - #### getPayable

      ```
      boolean getPayable()
      ```

      `bool payable = 7;`

      Returns:
      :   The payable.
    - #### getStateMutabilityValue

      ```
      int getStateMutabilityValue()
      ```

      `.protocol.SmartContract.ABI.Entry.StateMutabilityType stateMutability = 8;`

      Returns:
      :   The enum numeric value on the wire for stateMutability.
    - #### getStateMutability

      ```
      Common.SmartContract.ABI.Entry.StateMutabilityType getStateMutability()
      ```

      `.protocol.SmartContract.ABI.Entry.StateMutabilityType stateMutability = 8;`

      Returns:
      :   The stateMutability.