

org.tron.trident.proto

## Interface Response.AccountResourceMessageOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.AccountResourceMessage](../../../../org/tron/trident/proto/Response.AccountResourceMessage.html "class in org.tron.trident.proto"), [Response.AccountResourceMessage.Builder](../../../../org/tron/trident/proto/Response.AccountResourceMessage.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.AccountResourceMessageOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `boolean` | `containsAssetNetLimit(java.lang.String key)` `map<string, int64> assetNetLimit = 6;` |
    | `boolean` | `containsAssetNetUsed(java.lang.String key)` `map<string, int64> assetNetUsed = 5;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getAssetNetLimit()` Deprecated. |
    | `int` | `getAssetNetLimitCount()` `map<string, int64> assetNetLimit = 6;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getAssetNetLimitMap()` `map<string, int64> assetNetLimit = 6;` |
    | `long` | `getAssetNetLimitOrDefault(java.lang.String key, long defaultValue)` `map<string, int64> assetNetLimit = 6;` |
    | `long` | `getAssetNetLimitOrThrow(java.lang.String key)` `map<string, int64> assetNetLimit = 6;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getAssetNetUsed()` Deprecated. |
    | `int` | `getAssetNetUsedCount()` `map<string, int64> assetNetUsed = 5;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getAssetNetUsedMap()` `map<string, int64> assetNetUsed = 5;` |
    | `long` | `getAssetNetUsedOrDefault(java.lang.String key, long defaultValue)` `map<string, int64> assetNetUsed = 5;` |
    | `long` | `getAssetNetUsedOrThrow(java.lang.String key)` `map<string, int64> assetNetUsed = 5;` |
    | `long` | `getEnergyLimit()` `int64 EnergyLimit = 14;` |
    | `long` | `getEnergyUsed()` `int64 EnergyUsed = 13;` |
    | `long` | `getFreeNetLimit()` `int64 freeNetLimit = 2;` |
    | `long` | `getFreeNetUsed()` `int64 freeNetUsed = 1;` |
    | `long` | `getNetLimit()` `int64 NetLimit = 4;` |
    | `long` | `getNetUsed()` `int64 NetUsed = 3;` |
    | `long` | `getStorageLimit()` `int64 storageLimit = 22;` |
    | `long` | `getStorageUsed()` `int64 storageUsed = 21;` |
    | `long` | `getTotalEnergyLimit()` `int64 TotalEnergyLimit = 15;` |
    | `long` | `getTotalEnergyWeight()` `int64 TotalEnergyWeight = 16;` |
    | `long` | `getTotalNetLimit()` `int64 TotalNetLimit = 7;` |
    | `long` | `getTotalNetWeight()` `int64 TotalNetWeight = 8;` |
    | `long` | `getTotalTronPowerWeight()` `int64 TotalTronPowerWeight = 9;` |
    | `long` | `getTronPowerLimit()` `int64 tronPowerLimit = 11;` |
    | `long` | `getTronPowerUsed()` `int64 tronPowerUsed = 10;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getFreeNetUsed

      ```
      long getFreeNetUsed()
      ```

      `int64 freeNetUsed = 1;`

      Returns:
      :   The freeNetUsed.
    - #### getFreeNetLimit

      ```
      long getFreeNetLimit()
      ```

      `int64 freeNetLimit = 2;`

      Returns:
      :   The freeNetLimit.
    - #### getNetUsed

      ```
      long getNetUsed()
      ```

      `int64 NetUsed = 3;`

      Returns:
      :   The netUsed.
    - #### getNetLimit

      ```
      long getNetLimit()
      ```

      `int64 NetLimit = 4;`

      Returns:
      :   The netLimit.
    - #### getAssetNetUsedCount

      ```
      int getAssetNetUsedCount()
      ```

      `map<string, int64> assetNetUsed = 5;`
    - #### containsAssetNetUsed

      ```
      boolean containsAssetNetUsed(java.lang.String key)
      ```

      `map<string, int64> assetNetUsed = 5;`
    - #### getAssetNetUsed

      ```
      @Deprecated
      java.util.Map<java.lang.String,java.lang.Long> getAssetNetUsed()
      ```

      Deprecated.

      Use [`getAssetNetUsedMap()`](../../../../org/tron/trident/proto/Response.AccountResourceMessageOrBuilder.html#getAssetNetUsedMap--) instead.
    - #### getAssetNetUsedMap

      ```
      java.util.Map<java.lang.String,java.lang.Long> getAssetNetUsedMap()
      ```

      `map<string, int64> assetNetUsed = 5;`
    - #### getAssetNetUsedOrDefault

      ```
      long getAssetNetUsedOrDefault(java.lang.String key,
                                    long defaultValue)
      ```

      `map<string, int64> assetNetUsed = 5;`
    - #### getAssetNetUsedOrThrow

      ```
      long getAssetNetUsedOrThrow(java.lang.String key)
      ```

      `map<string, int64> assetNetUsed = 5;`
    - #### getAssetNetLimitCount

      ```
      int getAssetNetLimitCount()
      ```

      `map<string, int64> assetNetLimit = 6;`
    - #### containsAssetNetLimit

      ```
      boolean containsAssetNetLimit(java.lang.String key)
      ```

      `map<string, int64> assetNetLimit = 6;`
    - #### getAssetNetLimit

      ```
      @Deprecated
      java.util.Map<java.lang.String,java.lang.Long> getAssetNetLimit()
      ```

      Deprecated.

      Use [`getAssetNetLimitMap()`](../../../../org/tron/trident/proto/Response.AccountResourceMessageOrBuilder.html#getAssetNetLimitMap--) instead.
    - #### getAssetNetLimitMap

      ```
      java.util.Map<java.lang.String,java.lang.Long> getAssetNetLimitMap()
      ```

      `map<string, int64> assetNetLimit = 6;`
    - #### getAssetNetLimitOrDefault

      ```
      long getAssetNetLimitOrDefault(java.lang.String key,
                                     long defaultValue)
      ```

      `map<string, int64> assetNetLimit = 6;`
    - #### getAssetNetLimitOrThrow

      ```
      long getAssetNetLimitOrThrow(java.lang.String key)
      ```

      `map<string, int64> assetNetLimit = 6;`
    - #### getTotalNetLimit

      ```
      long getTotalNetLimit()
      ```

      `int64 TotalNetLimit = 7;`

      Returns:
      :   The totalNetLimit.
    - #### getTotalNetWeight

      ```
      long getTotalNetWeight()
      ```

      `int64 TotalNetWeight = 8;`

      Returns:
      :   The totalNetWeight.
    - #### getTotalTronPowerWeight

      ```
      long getTotalTronPowerWeight()
      ```

      `int64 TotalTronPowerWeight = 9;`

      Returns:
      :   The totalTronPowerWeight.
    - #### getTronPowerUsed

      ```
      long getTronPowerUsed()
      ```

      `int64 tronPowerUsed = 10;`

      Returns:
      :   The tronPowerUsed.
    - #### getTronPowerLimit

      ```
      long getTronPowerLimit()
      ```

      `int64 tronPowerLimit = 11;`

      Returns:
      :   The tronPowerLimit.
    - #### getEnergyUsed

      ```
      long getEnergyUsed()
      ```

      `int64 EnergyUsed = 13;`

      Returns:
      :   The energyUsed.
    - #### getEnergyLimit

      ```
      long getEnergyLimit()
      ```

      `int64 EnergyLimit = 14;`

      Returns:
      :   The energyLimit.
    - #### getTotalEnergyLimit

      ```
      long getTotalEnergyLimit()
      ```

      `int64 TotalEnergyLimit = 15;`

      Returns:
      :   The totalEnergyLimit.
    - #### getTotalEnergyWeight

      ```
      long getTotalEnergyWeight()
      ```

      `int64 TotalEnergyWeight = 16;`

      Returns:
      :   The totalEnergyWeight.
    - #### getStorageUsed

      ```
      long getStorageUsed()
      ```

      `int64 storageUsed = 21;`

      Returns:
      :   The storageUsed.
    - #### getStorageLimit

      ```
      long getStorageLimit()
      ```

      `int64 storageLimit = 22;`

      Returns:
      :   The storageLimit.