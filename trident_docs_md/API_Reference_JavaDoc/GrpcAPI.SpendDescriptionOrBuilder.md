

org.tron.trident.api

## Interface GrpcAPI.SpendDescriptionOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.SpendDescription](../../../../org/tron/trident/api/GrpcAPI.SpendDescription.html "class in org.tron.trident.api"), [GrpcAPI.SpendDescription.Builder](../../../../org/tron/trident/api/GrpcAPI.SpendDescription.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.SpendDescriptionOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getAnchor()` merkle root |
    | `com.google.protobuf.ByteString` | `getNullifier()` used for check double spend |
    | `com.google.protobuf.ByteString` | `getRk()` used for check spend authority signature |
    | `com.google.protobuf.ByteString` | `getSpendAuthoritySignature()` `bytes spend_authority_signature = 6;` |
    | `com.google.protobuf.ByteString` | `getValueCommitment()` `bytes value_commitment = 1;` |
    | `com.google.protobuf.ByteString` | `getZkproof()` `bytes zkproof = 5;` |

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
    - #### getAnchor

      ```
      com.google.protobuf.ByteString getAnchor()
      ```

      ```
       merkle root
      ```

      `bytes anchor = 2;`

      Returns:
      :   The anchor.
    - #### getNullifier

      ```
      com.google.protobuf.ByteString getNullifier()
      ```

      ```
       used for check double spend
      ```

      `bytes nullifier = 3;`

      Returns:
      :   The nullifier.
    - #### getRk

      ```
      com.google.protobuf.ByteString getRk()
      ```

      ```
       used for check spend authority signature
      ```

      `bytes rk = 4;`

      Returns:
      :   The rk.
    - #### getZkproof

      ```
      com.google.protobuf.ByteString getZkproof()
      ```

      `bytes zkproof = 5;`

      Returns:
      :   The zkproof.
    - #### getSpendAuthoritySignature

      ```
      com.google.protobuf.ByteString getSpendAuthoritySignature()
      ```

      `bytes spend_authority_signature = 6;`

      Returns:
      :   The spendAuthoritySignature.