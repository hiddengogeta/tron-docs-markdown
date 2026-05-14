

org.tron.trident.proto

## Interface Contract.VoteWitnessContract.VoteOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Contract.VoteWitnessContract.Vote](../../../../org/tron/trident/proto/Contract.VoteWitnessContract.Vote.html "class in org.tron.trident.proto"), [Contract.VoteWitnessContract.Vote.Builder](../../../../org/tron/trident/proto/Contract.VoteWitnessContract.Vote.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.VoteWitnessContract](../../../../org/tron/trident/proto/Contract.VoteWitnessContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Contract.VoteWitnessContract.VoteOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getVoteAddress()` `bytes vote_address = 1;` |
    | `long` | `getVoteCount()` `int64 vote_count = 2;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getVoteAddress

      ```
      com.google.protobuf.ByteString getVoteAddress()
      ```

      `bytes vote_address = 1;`

      Returns:
      :   The voteAddress.
    - #### getVoteCount

      ```
      long getVoteCount()
      ```

      `int64 vote_count = 2;`

      Returns:
      :   The voteCount.