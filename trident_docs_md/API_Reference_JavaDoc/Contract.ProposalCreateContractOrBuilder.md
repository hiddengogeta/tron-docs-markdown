

org.tron.trident.proto

## Interface Contract.ProposalCreateContractOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Contract.ProposalCreateContract](../../../../org/tron/trident/proto/Contract.ProposalCreateContract.html "class in org.tron.trident.proto"), [Contract.ProposalCreateContract.Builder](../../../../org/tron/trident/proto/Contract.ProposalCreateContract.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Contract.ProposalCreateContractOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `boolean` | `containsParameters(long key)` `map<int64, int64> parameters = 2;` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `java.util.Map<java.lang.Long,java.lang.Long>` | `getParameters()` Deprecated. |
    | `int` | `getParametersCount()` `map<int64, int64> parameters = 2;` |
    | `java.util.Map<java.lang.Long,java.lang.Long>` | `getParametersMap()` `map<int64, int64> parameters = 2;` |
    | `long` | `getParametersOrDefault(long key, long defaultValue)` `map<int64, int64> parameters = 2;` |
    | `long` | `getParametersOrThrow(long key)` `map<int64, int64> parameters = 2;` |

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
    - #### getParametersCount

      ```
      int getParametersCount()
      ```

      `map<int64, int64> parameters = 2;`
    - #### containsParameters

      ```
      boolean containsParameters(long key)
      ```

      `map<int64, int64> parameters = 2;`
    - #### getParameters

      ```
      @Deprecated
      java.util.Map<java.lang.Long,java.lang.Long> getParameters()
      ```

      Deprecated.

      Use [`getParametersMap()`](../../../../org/tron/trident/proto/Contract.ProposalCreateContractOrBuilder.html#getParametersMap--) instead.
    - #### getParametersMap

      ```
      java.util.Map<java.lang.Long,java.lang.Long> getParametersMap()
      ```

      `map<int64, int64> parameters = 2;`
    - #### getParametersOrDefault

      ```
      long getParametersOrDefault(long key,
                                  long defaultValue)
      ```

      `map<int64, int64> parameters = 2;`
    - #### getParametersOrThrow

      ```
      long getParametersOrThrow(long key)
      ```

      `map<int64, int64> parameters = 2;`