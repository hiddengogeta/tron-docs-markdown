

org.tron.trident.proto

## Interface Response.Account.FrozenOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.Account.Frozen](../../../../org/tron/trident/proto/Response.Account.Frozen.html "class in org.tron.trident.proto"), [Response.Account.Frozen.Builder](../../../../org/tron/trident/proto/Response.Account.Frozen.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response.Account](../../../../org/tron/trident/proto/Response.Account.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.Account.FrozenOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getExpireTime()` the expire time |
    | `long` | `getFrozenBalance()` the frozen trx balance |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getFrozenBalance

      ```
      long getFrozenBalance()
      ```

      ```
       the frozen trx balance
      ```

      `int64 frozen_balance = 1;`

      Returns:
      :   The frozenBalance.
    - #### getExpireTime

      ```
      long getExpireTime()
      ```

      ```
       the expire time
      ```

      `int64 expire_time = 2;`

      Returns:
      :   The expireTime.