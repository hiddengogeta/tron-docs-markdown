

org.tron.trident.proto

## Interface Contract.AssetIssueContract.FrozenSupplyOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Contract.AssetIssueContract.FrozenSupply](../../../../org/tron/trident/proto/Contract.AssetIssueContract.FrozenSupply.html "class in org.tron.trident.proto"), [Contract.AssetIssueContract.FrozenSupply.Builder](../../../../org/tron/trident/proto/Contract.AssetIssueContract.FrozenSupply.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.AssetIssueContract](../../../../org/tron/trident/proto/Contract.AssetIssueContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Contract.AssetIssueContract.FrozenSupplyOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getFrozenAmount()` `int64 frozen_amount = 1;` |
    | `long` | `getFrozenDays()` `int64 frozen_days = 2;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getFrozenAmount

      ```
      long getFrozenAmount()
      ```

      `int64 frozen_amount = 1;`

      Returns:
      :   The frozenAmount.
    - #### getFrozenDays

      ```
      long getFrozenDays()
      ```

      `int64 frozen_days = 2;`

      Returns:
      :   The frozenDays.