

org.tron.trident.api

## Interface GrpcAPI.NfTRC20ParametersOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.NfTRC20Parameters](../../../../org/tron/trident/api/GrpcAPI.NfTRC20Parameters.html "class in org.tron.trident.api"), [GrpcAPI.NfTRC20Parameters.Builder](../../../../org/tron/trident/api/GrpcAPI.NfTRC20Parameters.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.NfTRC20ParametersOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getAk()` `bytes ak = 2;` |
    | `com.google.protobuf.ByteString` | `getNk()` `bytes nk = 3;` |
    | `Common.Note` | `getNote()` `.protocol.Note note = 1;` |
    | `Common.NoteOrBuilder` | `getNoteOrBuilder()` `.protocol.Note note = 1;` |
    | `long` | `getPosition()` `int64 position = 4;` |
    | `com.google.protobuf.ByteString` | `getShieldedTRC20ContractAddress()` `bytes shielded_TRC20_contract_address = 5;` |
    | `boolean` | `hasNote()` `.protocol.Note note = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### hasNote

      ```
      boolean hasNote()
      ```

      `.protocol.Note note = 1;`

      Returns:
      :   Whether the note field is set.
    - #### getNote

      ```
      Common.Note getNote()
      ```

      `.protocol.Note note = 1;`

      Returns:
      :   The note.
    - #### getNoteOrBuilder

      ```
      Common.NoteOrBuilder getNoteOrBuilder()
      ```

      `.protocol.Note note = 1;`
    - #### getAk

      ```
      com.google.protobuf.ByteString getAk()
      ```

      `bytes ak = 2;`

      Returns:
      :   The ak.
    - #### getNk

      ```
      com.google.protobuf.ByteString getNk()
      ```

      `bytes nk = 3;`

      Returns:
      :   The nk.
    - #### getPosition

      ```
      long getPosition()
      ```

      `int64 position = 4;`

      Returns:
      :   The position.
    - #### getShieldedTRC20ContractAddress

      ```
      com.google.protobuf.ByteString getShieldedTRC20ContractAddress()
      ```

      `bytes shielded_TRC20_contract_address = 5;`

      Returns:
      :   The shieldedTRC20ContractAddress.