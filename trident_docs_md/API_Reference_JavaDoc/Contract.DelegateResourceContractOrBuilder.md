

org.tron.trident.proto

## Interface Contract.DelegateResourceContractOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Contract.DelegateResourceContract](../../../../org/tron/trident/proto/Contract.DelegateResourceContract.html "class in org.tron.trident.proto"), [Contract.DelegateResourceContract.Builder](../../../../org/tron/trident/proto/Contract.DelegateResourceContract.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Contract.DelegateResourceContractOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getBalance()` `int64 balance = 3;` |
    | `boolean` | `getLock()` `bool lock = 5;` |
    | `long` | `getLockPeriod()` `int64 lock_period = 6;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `com.google.protobuf.ByteString` | `getReceiverAddress()` `bytes receiver_address = 4;` |
    | `Common.ResourceCode` | `getResource()` `.protocol.ResourceCode resource = 2;` |
    | `int` | `getResourceValue()` `.protocol.ResourceCode resource = 2;` |

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
    - #### getResourceValue

      ```
      int getResourceValue()
      ```

      `.protocol.ResourceCode resource = 2;`

      Returns:
      :   The enum numeric value on the wire for resource.
    - #### getResource

      ```
      Common.ResourceCode getResource()
      ```

      `.protocol.ResourceCode resource = 2;`

      Returns:
      :   The resource.
    - #### getBalance

      ```
      long getBalance()
      ```

      `int64 balance = 3;`

      Returns:
      :   The balance.
    - #### getReceiverAddress

      ```
      com.google.protobuf.ByteString getReceiverAddress()
      ```

      `bytes receiver_address = 4;`

      Returns:
      :   The receiverAddress.
    - #### getLock

      ```
      boolean getLock()
      ```

      `bool lock = 5;`

      Returns:
      :   The lock.
    - #### getLockPeriod

      ```
      long getLockPeriod()
      ```

      `int64 lock_period = 6;`

      Returns:
      :   The lockPeriod.