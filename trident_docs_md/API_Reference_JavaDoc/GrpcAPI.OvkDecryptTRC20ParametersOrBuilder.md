

org.tron.trident.api

## Interface GrpcAPI.OvkDecryptTRC20ParametersOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.OvkDecryptTRC20Parameters](../../../../org/tron/trident/api/GrpcAPI.OvkDecryptTRC20Parameters.html "class in org.tron.trident.api"), [GrpcAPI.OvkDecryptTRC20Parameters.Builder](../../../../org/tron/trident/api/GrpcAPI.OvkDecryptTRC20Parameters.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.OvkDecryptTRC20ParametersOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getEndBlockIndex()` `int64 end_block_index = 2;` |
    | `java.lang.String` | `getEvents(int index)` `repeated string events = 5;` |
    | `com.google.protobuf.ByteString` | `getEventsBytes(int index)` `repeated string events = 5;` |
    | `int` | `getEventsCount()` `repeated string events = 5;` |
    | `java.util.List<java.lang.String>` | `getEventsList()` `repeated string events = 5;` |
    | `com.google.protobuf.ByteString` | `getOvk()` `bytes ovk = 3;` |
    | `com.google.protobuf.ByteString` | `getShieldedTRC20ContractAddress()` `bytes shielded_TRC20_contract_address = 4;` |
    | `long` | `getStartBlockIndex()` `int64 start_block_index = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getStartBlockIndex

      ```
      long getStartBlockIndex()
      ```

      `int64 start_block_index = 1;`

      Returns:
      :   The startBlockIndex.
    - #### getEndBlockIndex

      ```
      long getEndBlockIndex()
      ```

      `int64 end_block_index = 2;`

      Returns:
      :   The endBlockIndex.
    - #### getOvk

      ```
      com.google.protobuf.ByteString getOvk()
      ```

      `bytes ovk = 3;`

      Returns:
      :   The ovk.
    - #### getShieldedTRC20ContractAddress

      ```
      com.google.protobuf.ByteString getShieldedTRC20ContractAddress()
      ```

      `bytes shielded_TRC20_contract_address = 4;`

      Returns:
      :   The shieldedTRC20ContractAddress.
    - #### getEventsList

      ```
      java.util.List<java.lang.String> getEventsList()
      ```

      `repeated string events = 5;`

      Returns:
      :   A list containing the events.
    - #### getEventsCount

      ```
      int getEventsCount()
      ```

      `repeated string events = 5;`

      Returns:
      :   The count of events.
    - #### getEvents

      ```
      java.lang.String getEvents(int index)
      ```

      `repeated string events = 5;`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The events at the given index.
    - #### getEventsBytes

      ```
      com.google.protobuf.ByteString getEventsBytes(int index)
      ```

      `repeated string events = 5;`

      Parameters:
      :   `index` - The index of the value to return.

      Returns:
      :   The bytes of the events at the given index.