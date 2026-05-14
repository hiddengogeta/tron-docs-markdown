

org.tron.trident.proto

## Interface Contract.ProposalApproveContractOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Contract.ProposalApproveContract](../../../../org/tron/trident/proto/Contract.ProposalApproveContract.html "class in org.tron.trident.proto"), [Contract.ProposalApproveContract.Builder](../../../../org/tron/trident/proto/Contract.ProposalApproveContract.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Contract.ProposalApproveContractOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `boolean` | `getIsAddApproval()` add or remove approval |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `long` | `getProposalId()` `int64 proposal_id = 2;` |

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
    - #### getProposalId

      ```
      long getProposalId()
      ```

      `int64 proposal_id = 2;`

      Returns:
      :   The proposalId.
    - #### getIsAddApproval

      ```
      boolean getIsAddApproval()
      ```

      ```
       add or remove approval
      ```

      `bool is_add_approval = 3;`

      Returns:
      :   The isAddApproval.