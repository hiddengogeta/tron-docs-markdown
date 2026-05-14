

org.tron.trident.proto

## Interface Response.ResourceReceiptOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.ResourceReceipt](../../../../org/tron/trident/proto/Response.ResourceReceipt.html "class in org.tron.trident.proto"), [Response.ResourceReceipt.Builder](../../../../org/tron/trident/proto/Response.ResourceReceipt.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.ResourceReceiptOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getEnergyFee()` `int64 energy_fee = 2;` |
    | `long` | `getEnergyPenaltyTotal()` `int64 energy_penalty_total = 8;` |
    | `long` | `getEnergyUsage()` `int64 energy_usage = 1;` |
    | `long` | `getEnergyUsageTotal()` `int64 energy_usage_total = 4;` |
    | `long` | `getNetFee()` `int64 net_fee = 6;` |
    | `long` | `getNetUsage()` `int64 net_usage = 5;` |
    | `long` | `getOriginEnergyUsage()` `int64 origin_energy_usage = 3;` |
    | `Chain.Transaction.Result.contractResult` | `getResult()` `.protocol.Transaction.Result.contractResult result = 7;` |
    | `int` | `getResultValue()` `.protocol.Transaction.Result.contractResult result = 7;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getEnergyUsage

      ```
      long getEnergyUsage()
      ```

      `int64 energy_usage = 1;`

      Returns:
      :   The energyUsage.
    - #### getEnergyFee

      ```
      long getEnergyFee()
      ```

      `int64 energy_fee = 2;`

      Returns:
      :   The energyFee.
    - #### getOriginEnergyUsage

      ```
      long getOriginEnergyUsage()
      ```

      `int64 origin_energy_usage = 3;`

      Returns:
      :   The originEnergyUsage.
    - #### getEnergyUsageTotal

      ```
      long getEnergyUsageTotal()
      ```

      `int64 energy_usage_total = 4;`

      Returns:
      :   The energyUsageTotal.
    - #### getNetUsage

      ```
      long getNetUsage()
      ```

      `int64 net_usage = 5;`

      Returns:
      :   The netUsage.
    - #### getNetFee

      ```
      long getNetFee()
      ```

      `int64 net_fee = 6;`

      Returns:
      :   The netFee.
    - #### getResultValue

      ```
      int getResultValue()
      ```

      `.protocol.Transaction.Result.contractResult result = 7;`

      Returns:
      :   The enum numeric value on the wire for result.
    - #### getResult

      ```
      Chain.Transaction.Result.contractResult getResult()
      ```

      `.protocol.Transaction.Result.contractResult result = 7;`

      Returns:
      :   The result.
    - #### getEnergyPenaltyTotal

      ```
      long getEnergyPenaltyTotal()
      ```

      `int64 energy_penalty_total = 8;`

      Returns:
      :   The energyPenaltyTotal.