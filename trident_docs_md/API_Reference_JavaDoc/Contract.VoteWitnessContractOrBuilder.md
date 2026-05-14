

org.tron.trident.proto

## Interface Contract.VoteWitnessContractOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Contract.VoteWitnessContract](../../../../org/tron/trident/proto/Contract.VoteWitnessContract.html "class in org.tron.trident.proto"), [Contract.VoteWitnessContract.Builder](../../../../org/tron/trident/proto/Contract.VoteWitnessContract.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Contract.VoteWitnessContractOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `boolean` | `getSupport()` `bool support = 3;` |
    | `Contract.VoteWitnessContract.Vote` | `getVotes(int index)` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `int` | `getVotesCount()` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `java.util.List<Contract.VoteWitnessContract.Vote>` | `getVotesList()` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `Contract.VoteWitnessContract.VoteOrBuilder` | `getVotesOrBuilder(int index)` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |
    | `java.util.List<? extends Contract.VoteWitnessContract.VoteOrBuilder>` | `getVotesOrBuilderList()` `repeated .protocol.VoteWitnessContract.Vote votes = 2;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getOwnerAddress

      ```
      com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   The ownerAddress.
    - #### getVotesList

      ```
      java.util.List<Contract.VoteWitnessContract.Vote> getVotesList()
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`
    - #### getVotes

      ```
      Contract.VoteWitnessContract.Vote getVotes(int index)
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`
    - #### getVotesCount

      ```
      int getVotesCount()
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`
    - #### getVotesOrBuilderList

      ```
      java.util.List<? extends Contract.VoteWitnessContract.VoteOrBuilder> getVotesOrBuilderList()
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`
    - #### getVotesOrBuilder

      ```
      Contract.VoteWitnessContract.VoteOrBuilder getVotesOrBuilder(int index)
      ```

      `repeated .protocol.VoteWitnessContract.Vote votes = 2;`
    - #### getSupport

      ```
      boolean getSupport()
      ```

      `bool support = 3;`

      Returns:
      :   The support.