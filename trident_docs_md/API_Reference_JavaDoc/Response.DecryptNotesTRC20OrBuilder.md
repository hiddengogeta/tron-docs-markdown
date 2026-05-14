

org.tron.trident.proto

## Interface Response.DecryptNotesTRC20OrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.DecryptNotesTRC20](../../../../org/tron/trident/proto/Response.DecryptNotesTRC20.html "class in org.tron.trident.proto"), [Response.DecryptNotesTRC20.Builder](../../../../org/tron/trident/proto/Response.DecryptNotesTRC20.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.DecryptNotesTRC20OrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Response.DecryptNotesTRC20.NoteTx` | `getNoteTxs(int index)` `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;` |
    | `int` | `getNoteTxsCount()` `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;` |
    | `java.util.List<Response.DecryptNotesTRC20.NoteTx>` | `getNoteTxsList()` `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;` |
    | `Response.DecryptNotesTRC20.NoteTxOrBuilder` | `getNoteTxsOrBuilder(int index)` `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;` |
    | `java.util.List<? extends Response.DecryptNotesTRC20.NoteTxOrBuilder>` | `getNoteTxsOrBuilderList()` `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getNoteTxsList

      ```
      java.util.List<Response.DecryptNotesTRC20.NoteTx> getNoteTxsList()
      ```

      `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;`
    - #### getNoteTxs

      ```
      Response.DecryptNotesTRC20.NoteTx getNoteTxs(int index)
      ```

      `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;`
    - #### getNoteTxsCount

      ```
      int getNoteTxsCount()
      ```

      `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;`
    - #### getNoteTxsOrBuilderList

      ```
      java.util.List<? extends Response.DecryptNotesTRC20.NoteTxOrBuilder> getNoteTxsOrBuilderList()
      ```

      `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;`
    - #### getNoteTxsOrBuilder

      ```
      Response.DecryptNotesTRC20.NoteTxOrBuilder getNoteTxsOrBuilder(int index)
      ```

      `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;`