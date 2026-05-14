

org.tron.trident.proto

## Interface Common.SmartContract.ABIOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Common.SmartContract.ABI](../../../../org/tron/trident/proto/Common.SmartContract.ABI.html "class in org.tron.trident.proto"), [Common.SmartContract.ABI.Builder](../../../../org/tron/trident/proto/Common.SmartContract.ABI.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Common.SmartContract](../../../../org/tron/trident/proto/Common.SmartContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Common.SmartContract.ABIOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Common.SmartContract.ABI.Entry` | `getEntrys(int index)` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `int` | `getEntrysCount()` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `java.util.List<Common.SmartContract.ABI.Entry>` | `getEntrysList()` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `Common.SmartContract.ABI.EntryOrBuilder` | `getEntrysOrBuilder(int index)` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `java.util.List<? extends Common.SmartContract.ABI.EntryOrBuilder>` | `getEntrysOrBuilderList()` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getEntrysList

      ```
      java.util.List<Common.SmartContract.ABI.Entry> getEntrysList()
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`
    - #### getEntrys

      ```
      Common.SmartContract.ABI.Entry getEntrys(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`
    - #### getEntrysCount

      ```
      int getEntrysCount()
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`
    - #### getEntrysOrBuilderList

      ```
      java.util.List<? extends Common.SmartContract.ABI.EntryOrBuilder> getEntrysOrBuilderList()
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`
    - #### getEntrysOrBuilder

      ```
      Common.SmartContract.ABI.EntryOrBuilder getEntrysOrBuilder(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`