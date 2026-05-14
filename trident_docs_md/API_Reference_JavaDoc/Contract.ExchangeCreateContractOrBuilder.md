

org.tron.trident.proto

## Interface Contract.ExchangeCreateContractOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Contract.ExchangeCreateContract](../../../../org/tron/trident/proto/Contract.ExchangeCreateContract.html "class in org.tron.trident.proto"), [Contract.ExchangeCreateContract.Builder](../../../../org/tron/trident/proto/Contract.ExchangeCreateContract.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Contract.ExchangeCreateContractOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getFirstTokenBalance()` `int64 first_token_balance = 3;` |
    | `com.google.protobuf.ByteString` | `getFirstTokenId()` `bytes first_token_id = 2;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `long` | `getSecondTokenBalance()` `int64 second_token_balance = 5;` |
    | `com.google.protobuf.ByteString` | `getSecondTokenId()` `bytes second_token_id = 4;` |

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
    - #### getFirstTokenId

      ```
      com.google.protobuf.ByteString getFirstTokenId()
      ```

      `bytes first_token_id = 2;`

      Returns:
      :   The firstTokenId.
    - #### getFirstTokenBalance

      ```
      long getFirstTokenBalance()
      ```

      `int64 first_token_balance = 3;`

      Returns:
      :   The firstTokenBalance.
    - #### getSecondTokenId

      ```
      com.google.protobuf.ByteString getSecondTokenId()
      ```

      `bytes second_token_id = 4;`

      Returns:
      :   The secondTokenId.
    - #### getSecondTokenBalance

      ```
      long getSecondTokenBalance()
      ```

      `int64 second_token_balance = 5;`

      Returns:
      :   The secondTokenBalance.