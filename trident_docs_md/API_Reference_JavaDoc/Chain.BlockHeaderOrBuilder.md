

org.tron.trident.proto

## Interface Chain.BlockHeaderOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Chain.BlockHeader](../../../../org/tron/trident/proto/Chain.BlockHeader.html "class in org.tron.trident.proto"), [Chain.BlockHeader.Builder](../../../../org/tron/trident/proto/Chain.BlockHeader.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Chain](../../../../org/tron/trident/proto/Chain.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Chain.BlockHeaderOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Chain.BlockHeader.raw` | `getRawData()` `.protocol.BlockHeader.raw raw_data = 1;` |
    | `Chain.BlockHeader.rawOrBuilder` | `getRawDataOrBuilder()` `.protocol.BlockHeader.raw raw_data = 1;` |
    | `com.google.protobuf.ByteString` | `getWitnessSignature()` `bytes witness_signature = 2;` |
    | `boolean` | `hasRawData()` `.protocol.BlockHeader.raw raw_data = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### hasRawData

      ```
      boolean hasRawData()
      ```

      `.protocol.BlockHeader.raw raw_data = 1;`

      Returns:
      :   Whether the rawData field is set.
    - #### getRawData

      ```
      Chain.BlockHeader.raw getRawData()
      ```

      `.protocol.BlockHeader.raw raw_data = 1;`

      Returns:
      :   The rawData.
    - #### getRawDataOrBuilder

      ```
      Chain.BlockHeader.rawOrBuilder getRawDataOrBuilder()
      ```

      `.protocol.BlockHeader.raw raw_data = 1;`
    - #### getWitnessSignature

      ```
      com.google.protobuf.ByteString getWitnessSignature()
      ```

      `bytes witness_signature = 2;`

      Returns:
      :   The witnessSignature.