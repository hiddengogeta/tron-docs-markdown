

org.tron.trident.api

## Interface GrpcAPI.ReceiveDescriptionOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.ReceiveDescription](../../../../org/tron/trident/api/GrpcAPI.ReceiveDescription.html "class in org.tron.trident.api"), [GrpcAPI.ReceiveDescription.Builder](../../../../org/tron/trident/api/GrpcAPI.ReceiveDescription.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.ReceiveDescriptionOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getCEnc()` Encryption for incoming, decrypt it with ivk |
    | `com.google.protobuf.ByteString` | `getCOut()` Encryption for audit, decrypt it with ovk |
    | `com.google.protobuf.ByteString` | `getEpk()` for Encryption |
    | `com.google.protobuf.ByteString` | `getNoteCommitment()` `bytes note_commitment = 2;` |
    | `com.google.protobuf.ByteString` | `getValueCommitment()` `bytes value_commitment = 1;` |
    | `com.google.protobuf.ByteString` | `getZkproof()` `bytes zkproof = 6;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getValueCommitment

      ```
      com.google.protobuf.ByteString getValueCommitment()
      ```

      `bytes value_commitment = 1;`

      Returns:
      :   The valueCommitment.
    - #### getNoteCommitment

      ```
      com.google.protobuf.ByteString getNoteCommitment()
      ```

      `bytes note_commitment = 2;`

      Returns:
      :   The noteCommitment.
    - #### getEpk

      ```
      com.google.protobuf.ByteString getEpk()
      ```

      ```
       for Encryption
      ```

      `bytes epk = 3;`

      Returns:
      :   The epk.
    - #### getCEnc

      ```
      com.google.protobuf.ByteString getCEnc()
      ```

      ```
       Encryption for incoming, decrypt it with ivk
      ```

      `bytes c_enc = 4;`

      Returns:
      :   The cEnc.
    - #### getCOut

      ```
      com.google.protobuf.ByteString getCOut()
      ```

      ```
       Encryption for audit, decrypt it with ovk
      ```

      `bytes c_out = 5;`

      Returns:
      :   The cOut.
    - #### getZkproof

      ```
      com.google.protobuf.ByteString getZkproof()
      ```

      `bytes zkproof = 6;`

      Returns:
      :   The zkproof.