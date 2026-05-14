

org.tron.trident.proto

## Interface Contract.UnfreezeBalanceContractOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Contract.UnfreezeBalanceContract](../../../../org/tron/trident/proto/Contract.UnfreezeBalanceContract.html "class in org.tron.trident.proto"), [Contract.UnfreezeBalanceContract.Builder](../../../../org/tron/trident/proto/Contract.UnfreezeBalanceContract.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Contract.UnfreezeBalanceContractOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `com.google.protobuf.ByteString` | `getReceiverAddress()` `bytes receiver_address = 15;` |
    | `Common.ResourceCode` | `getResource()` `.protocol.ResourceCode resource = 10;` |
    | `int` | `getResourceValue()` `.protocol.ResourceCode resource = 10;` |

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

      `.protocol.ResourceCode resource = 10;`

      Returns:
      :   The enum numeric value on the wire for resource.
    - #### getResource

      ```
      Common.ResourceCode getResource()
      ```

      `.protocol.ResourceCode resource = 10;`

      Returns:
      :   The resource.
    - #### getReceiverAddress

      ```
      com.google.protobuf.ByteString getReceiverAddress()
      ```

      `bytes receiver_address = 15;`

      Returns:
      :   The receiverAddress.