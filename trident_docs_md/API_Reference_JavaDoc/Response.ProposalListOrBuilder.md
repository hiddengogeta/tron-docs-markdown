

org.tron.trident.proto

## Interface Response.ProposalListOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.ProposalList](../../../../org/tron/trident/proto/Response.ProposalList.html "class in org.tron.trident.proto"), [Response.ProposalList.Builder](../../../../org/tron/trident/proto/Response.ProposalList.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.ProposalListOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Response.Proposal` | `getProposals(int index)` `repeated .protocol.Proposal proposals = 1;` |
    | `int` | `getProposalsCount()` `repeated .protocol.Proposal proposals = 1;` |
    | `java.util.List<Response.Proposal>` | `getProposalsList()` `repeated .protocol.Proposal proposals = 1;` |
    | `Response.ProposalOrBuilder` | `getProposalsOrBuilder(int index)` `repeated .protocol.Proposal proposals = 1;` |
    | `java.util.List<? extends Response.ProposalOrBuilder>` | `getProposalsOrBuilderList()` `repeated .protocol.Proposal proposals = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getProposalsList

      ```
      java.util.List<Response.Proposal> getProposalsList()
      ```

      `repeated .protocol.Proposal proposals = 1;`
    - #### getProposals

      ```
      Response.Proposal getProposals(int index)
      ```

      `repeated .protocol.Proposal proposals = 1;`
    - #### getProposalsCount

      ```
      int getProposalsCount()
      ```

      `repeated .protocol.Proposal proposals = 1;`
    - #### getProposalsOrBuilderList

      ```
      java.util.List<? extends Response.ProposalOrBuilder> getProposalsOrBuilderList()
      ```

      `repeated .protocol.Proposal proposals = 1;`
    - #### getProposalsOrBuilder

      ```
      Response.ProposalOrBuilder getProposalsOrBuilder(int index)
      ```

      `repeated .protocol.Proposal proposals = 1;`