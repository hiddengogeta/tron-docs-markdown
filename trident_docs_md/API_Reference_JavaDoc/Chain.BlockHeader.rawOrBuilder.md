

org.tron.trident.proto

## Interface Chain.BlockHeader.rawOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Chain.BlockHeader.raw](../../../../org/tron/trident/proto/Chain.BlockHeader.raw.html "class in org.tron.trident.proto"), [Chain.BlockHeader.raw.Builder](../../../../org/tron/trident/proto/Chain.BlockHeader.raw.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Chain.BlockHeader](../../../../org/tron/trident/proto/Chain.BlockHeader.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Chain.BlockHeader.rawOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getAccountStateRoot()` `bytes accountStateRoot = 11;` |
    | `long` | `getNumber()` bytes nonce = 5; bytes difficulty = 6; |
    | `com.google.protobuf.ByteString` | `getParentHash()` `bytes parentHash = 3;` |
    | `long` | `getTimestamp()` `int64 timestamp = 1;` |
    | `com.google.protobuf.ByteString` | `getTxTrieRoot()` `bytes txTrieRoot = 2;` |
    | `int` | `getVersion()` `int32 version = 10;` |
    | `com.google.protobuf.ByteString` | `getWitnessAddress()` `bytes witness_address = 9;` |
    | `long` | `getWitnessId()` `int64 witness_id = 8;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getTimestamp

      ```
      long getTimestamp()
      ```

      `int64 timestamp = 1;`

      Returns:
      :   The timestamp.
    - #### getTxTrieRoot

      ```
      com.google.protobuf.ByteString getTxTrieRoot()
      ```

      `bytes txTrieRoot = 2;`

      Returns:
      :   The txTrieRoot.
    - #### getParentHash

      ```
      com.google.protobuf.ByteString getParentHash()
      ```

      `bytes parentHash = 3;`

      Returns:
      :   The parentHash.
    - #### getNumber

      ```
      long getNumber()
      ```

      ```
       bytes nonce = 5;
       bytes difficulty = 6;
      ```

      `int64 number = 7;`

      Returns:
      :   The number.
    - #### getWitnessId

      ```
      long getWitnessId()
      ```

      `int64 witness_id = 8;`

      Returns:
      :   The witnessId.
    - #### getWitnessAddress

      ```
      com.google.protobuf.ByteString getWitnessAddress()
      ```

      `bytes witness_address = 9;`

      Returns:
      :   The witnessAddress.
    - #### getVersion

      ```
      int getVersion()
      ```

      `int32 version = 10;`

      Returns:
      :   The version.
    - #### getAccountStateRoot

      ```
      com.google.protobuf.ByteString getAccountStateRoot()
      ```

      `bytes accountStateRoot = 11;`

      Returns:
      :   The accountStateRoot.