

org.tron.trident.proto

## Interface Contract.AccountCreateContractOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Contract.AccountCreateContract](../../../../org/tron/trident/proto/Contract.AccountCreateContract.html "class in org.tron.trident.proto"), [Contract.AccountCreateContract.Builder](../../../../org/tron/trident/proto/Contract.AccountCreateContract.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Contract.AccountCreateContractOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getAccountAddress()` `bytes account_address = 2;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `Common.AccountType` | `getType()` `.protocol.AccountType type = 3;` |
    | `int` | `getTypeValue()` `.protocol.AccountType type = 3;` |

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
    - #### getAccountAddress

      ```
      com.google.protobuf.ByteString getAccountAddress()
      ```

      `bytes account_address = 2;`

      Returns:
      :   The accountAddress.
    - #### getTypeValue

      ```
      int getTypeValue()
      ```

      `.protocol.AccountType type = 3;`

      Returns:
      :   The enum numeric value on the wire for type.
    - #### getType

      ```
      Common.AccountType getType()
      ```

      `.protocol.AccountType type = 3;`

      Returns:
      :   The type.