

org.tron.trident.proto

## Interface Response.ProposalOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.Proposal](../../../../org/tron/trident/proto/Response.Proposal.html "class in org.tron.trident.proto"), [Response.Proposal.Builder](../../../../org/tron/trident/proto/Response.Proposal.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.ProposalOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `boolean` | `containsParameters(long key)` `map<int64, int64> parameters = 3;` |
    | `com.google.protobuf.ByteString` | `getApprovals(int index)` `repeated bytes approvals = 6;` |
    | `int` | `getApprovalsCount()` `repeated bytes approvals = 6;` |
    | `java.util.List<com.google.protobuf.ByteString>` | `getApprovalsList()` `repeated bytes approvals = 6;` |
    | `long` | `getCreateTime()` `int64 create_time = 5;` |
    | `long` | `getExpirationTime()` `int64 expiration_time = 4;` |
    | `java.util.Map<java.lang.Long,java.lang.Long>` | `getParameters()` Deprecated. |
    | `int` | `getParametersCount()` `map<int64, int64> parameters = 3;` |
    | `java.util.Map<java.lang.Long,java.lang.Long>` | `getParametersMap()` `map<int64, int64> parameters = 3;` |
    | `long` | `getParametersOrDefault(long key, long defaultValue)` `map<int64, int64> parameters = 3;` |
    | `long` | `getParametersOrThrow(long key)` `map<int64, int64> parameters = 3;` |
    | `long` | `getProposalId()` `int64 proposal_id = 1;` |
    | `com.google.protobuf.ByteString` | `getProposerAddress()` `bytes proposer_address = 2;` |
    | `Response.Proposal.State` | `getState()` `.protocol.Proposal.State state = 7;` |
    | `int` | `getStateValue()` `.protocol.Proposal.State state = 7;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getProposalId

      ```
      long getProposalId()
      ```

      `int64 proposal_id = 1;`

      Returns:
      :   The proposalId.
    - #### getProposerAddress

      ```
      com.google.protobuf.ByteString getProposerAddress()
      ```

      `bytes proposer_address = 2;`

      Returns:
      :   The proposerAddress.
    - #### getParametersCount

      ```
      int getParametersCount()
      ```

      `map<int64, int64> parameters = 3;`
    - #### containsParameters

      ```
      boolean containsParameters(long key)
      ```

      `map<int64, int64> parameters = 3;`
    - #### getParameters

      ```
      @Deprecated
      java.util.Map<java.lang.Long,java.lang.Long> getParameters()
      ```

      Deprecated.

      Use [`getParametersMap()`](../../../../org/tron/trident/proto/Response.ProposalOrBuilder.html#getParametersMap--) instead.
    - #### getParametersMap

      ```
      java.util.Map<java.lang.Long,java.lang.Long> getParametersMap()
      ```

      `map<int64, int64> parameters = 3;`
    - #### getParametersOrDefault

      ```
      long getParametersOrDefault(long key,
                                  long defaultValue)
      ```

      `map<int64, int64> parameters = 3;`
    - #### getParametersOrThrow

      ```
      long getParametersOrThrow(long key)
      ```

      `map<int64, int64> parameters = 3;`
    - #### getExpirationTime

      ```
      long getExpirationTime()
      ```

      `int64 expiration_time = 4;`

      Returns:
      :   The expirationTime.
    - #### getCreateTime

      ```
      long getCreateTime()
      ```

      `int64 create_time = 5;`

      Returns:
      :   The createTime.
    - #### getApprovalsList

      ```
      java.util.List<com.google.protobuf.ByteString> getApprovalsList()
      ```

      `repeated bytes approvals = 6;`

      Returns:
      :   A list containing the approvals.
    - #### getApprovalsCount

      ```
      int getApprovalsCount()
      ```

      `repeated bytes approvals = 6;`

      Returns:
      :   The count of approvals.
    - #### getApprovals

      ```
      com.google.protobuf.ByteString getApprovals(int index)
      ```

      `repeated bytes approvals = 6;`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The approvals at the given index.
    - #### getStateValue

      ```
      int getStateValue()
      ```

      `.protocol.Proposal.State state = 7;`

      Returns:
      :   The enum numeric value on the wire for state.
    - #### getState

      ```
      Response.Proposal.State getState()
      ```

      `.protocol.Proposal.State state = 7;`

      Returns:
      :   The state.