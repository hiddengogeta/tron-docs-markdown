

org.tron.trident.proto

## Interface Contract.FreezeBalanceV2ContractOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Contract.FreezeBalanceV2Contract](../../../../org/tron/trident/proto/Contract.FreezeBalanceV2Contract.html "class in org.tron.trident.proto"), [Contract.FreezeBalanceV2Contract.Builder](../../../../org/tron/trident/proto/Contract.FreezeBalanceV2Contract.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Contract.FreezeBalanceV2ContractOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getFrozenBalance()` `int64 frozen_balance = 2;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `Common.ResourceCode` | `getResource()` `.protocol.ResourceCode resource = 3;` |
    | `int` | `getResourceValue()` `.protocol.ResourceCode resource = 3;` |

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
    - #### getFrozenBalance

      ```
      long getFrozenBalance()
      ```

      `int64 frozen_balance = 2;`

      Returns:
      :   The frozenBalance.
    - #### getResourceValue

      ```
      int getResourceValue()
      ```

      `.protocol.ResourceCode resource = 3;`

      Returns:
      :   The enum numeric value on the wire for resource.
    - #### getResource

      ```
      Common.ResourceCode getResource()
      ```

      `.protocol.ResourceCode resource = 3;`

      Returns:
      :   The resource.