

org.tron.trident.proto

## Interface Contract.VoteAssetContractOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Contract.VoteAssetContract](../../../../org/tron/trident/proto/Contract.VoteAssetContract.html "class in org.tron.trident.proto"), [Contract.VoteAssetContract.Builder](../../../../org/tron/trident/proto/Contract.VoteAssetContract.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Contract.VoteAssetContractOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `int` | `getCount()` `int32 count = 5;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `boolean` | `getSupport()` `bool support = 3;` |
    | `com.google.protobuf.ByteString` | `getVoteAddress(int index)` `repeated bytes vote_address = 2;` |
    | `int` | `getVoteAddressCount()` `repeated bytes vote_address = 2;` |
    | `java.util.List<com.google.protobuf.ByteString>` | `getVoteAddressList()` `repeated bytes vote_address = 2;` |

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
    - #### getVoteAddressList

      ```
      java.util.List<com.google.protobuf.ByteString> getVoteAddressList()
      ```

      `repeated bytes vote_address = 2;`

      Returns:
      :   A list containing the voteAddress.
    - #### getVoteAddressCount

      ```
      int getVoteAddressCount()
      ```

      `repeated bytes vote_address = 2;`

      Returns:
      :   The count of voteAddress.
    - #### getVoteAddress

      ```
      com.google.protobuf.ByteString getVoteAddress(int index)
      ```

      `repeated bytes vote_address = 2;`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The voteAddress at the given index.
    - #### getSupport

      ```
      boolean getSupport()
      ```

      `bool support = 3;`

      Returns:
      :   The support.
    - #### getCount

      ```
      int getCount()
      ```

      `int32 count = 5;`

      Returns:
      :   The count.