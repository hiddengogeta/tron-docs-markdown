

org.tron.trident.proto

## Interface Response.ExchangeOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.Exchange](../../../../org/tron/trident/proto/Response.Exchange.html "class in org.tron.trident.proto"), [Response.Exchange.Builder](../../../../org/tron/trident/proto/Response.Exchange.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.ExchangeOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getCreateTime()` `int64 create_time = 3;` |
    | `com.google.protobuf.ByteString` | `getCreatorAddress()` `bytes creator_address = 2;` |
    | `long` | `getExchangeId()` `int64 exchange_id = 1;` |
    | `long` | `getFirstTokenBalance()` `int64 first_token_balance = 7;` |
    | `com.google.protobuf.ByteString` | `getFirstTokenId()` `bytes first_token_id = 6;` |
    | `long` | `getSecondTokenBalance()` `int64 second_token_balance = 9;` |
    | `com.google.protobuf.ByteString` | `getSecondTokenId()` `bytes second_token_id = 8;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getExchangeId

      ```
      long getExchangeId()
      ```

      `int64 exchange_id = 1;`

      Returns:
      :   The exchangeId.
    - #### getCreatorAddress

      ```
      com.google.protobuf.ByteString getCreatorAddress()
      ```

      `bytes creator_address = 2;`

      Returns:
      :   The creatorAddress.
    - #### getCreateTime

      ```
      long getCreateTime()
      ```

      `int64 create_time = 3;`

      Returns:
      :   The createTime.
    - #### getFirstTokenId

      ```
      com.google.protobuf.ByteString getFirstTokenId()
      ```

      `bytes first_token_id = 6;`

      Returns:
      :   The firstTokenId.
    - #### getFirstTokenBalance

      ```
      long getFirstTokenBalance()
      ```

      `int64 first_token_balance = 7;`

      Returns:
      :   The firstTokenBalance.
    - #### getSecondTokenId

      ```
      com.google.protobuf.ByteString getSecondTokenId()
      ```

      `bytes second_token_id = 8;`

      Returns:
      :   The secondTokenId.
    - #### getSecondTokenBalance

      ```
      long getSecondTokenBalance()
      ```

      `int64 second_token_balance = 9;`

      Returns:
      :   The secondTokenBalance.