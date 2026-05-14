

org.tron.trident.proto

## Interface Response.DelegatedResourceOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.DelegatedResource](../../../../org/tron/trident/proto/Response.DelegatedResource.html "class in org.tron.trident.proto"), [Response.DelegatedResource.Builder](../../../../org/tron/trident/proto/Response.DelegatedResource.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.DelegatedResourceOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getExpireTimeForBandwidth()` `int64 expire_time_for_bandwidth = 5;` |
    | `long` | `getExpireTimeForEnergy()` `int64 expire_time_for_energy = 6;` |
    | `com.google.protobuf.ByteString` | `getFrom()` `bytes from = 1;` |
    | `long` | `getFrozenBalanceForBandwidth()` `int64 frozen_balance_for_bandwidth = 3;` |
    | `long` | `getFrozenBalanceForEnergy()` `int64 frozen_balance_for_energy = 4;` |
    | `com.google.protobuf.ByteString` | `getTo()` `bytes to = 2;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getFrom

      ```
      com.google.protobuf.ByteString getFrom()
      ```

      `bytes from = 1;`

      Returns:
      :   The from.
    - #### getTo

      ```
      com.google.protobuf.ByteString getTo()
      ```

      `bytes to = 2;`

      Returns:
      :   The to.
    - #### getFrozenBalanceForBandwidth

      ```
      long getFrozenBalanceForBandwidth()
      ```

      `int64 frozen_balance_for_bandwidth = 3;`

      Returns:
      :   The frozenBalanceForBandwidth.
    - #### getFrozenBalanceForEnergy

      ```
      long getFrozenBalanceForEnergy()
      ```

      `int64 frozen_balance_for_energy = 4;`

      Returns:
      :   The frozenBalanceForEnergy.
    - #### getExpireTimeForBandwidth

      ```
      long getExpireTimeForBandwidth()
      ```

      `int64 expire_time_for_bandwidth = 5;`

      Returns:
      :   The expireTimeForBandwidth.
    - #### getExpireTimeForEnergy

      ```
      long getExpireTimeForEnergy()
      ```

      `int64 expire_time_for_energy = 6;`

      Returns:
      :   The expireTimeForEnergy.