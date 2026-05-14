

org.tron.trident.proto

## Interface Response.EstimateEnergyMessageOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.EstimateEnergyMessage](../../../../org/tron/trident/proto/Response.EstimateEnergyMessage.html "class in org.tron.trident.proto"), [Response.EstimateEnergyMessage.Builder](../../../../org/tron/trident/proto/Response.EstimateEnergyMessage.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.EstimateEnergyMessageOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getEnergyRequired()` `int64 energy_required = 2;` |
    | `Response.TransactionReturn` | `getResult()` `.protocol.TransactionReturn result = 1;` |
    | `Response.TransactionReturnOrBuilder` | `getResultOrBuilder()` `.protocol.TransactionReturn result = 1;` |
    | `boolean` | `hasResult()` `.protocol.TransactionReturn result = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### hasResult

      ```
      boolean hasResult()
      ```

      `.protocol.TransactionReturn result = 1;`

      Returns:
      :   Whether the result field is set.
    - #### getResult

      ```
      Response.TransactionReturn getResult()
      ```

      `.protocol.TransactionReturn result = 1;`

      Returns:
      :   The result.
    - #### getResultOrBuilder

      ```
      Response.TransactionReturnOrBuilder getResultOrBuilder()
      ```

      `.protocol.TransactionReturn result = 1;`
    - #### getEnergyRequired

      ```
      long getEnergyRequired()
      ```

      `int64 energy_required = 2;`

      Returns:
      :   The energyRequired.