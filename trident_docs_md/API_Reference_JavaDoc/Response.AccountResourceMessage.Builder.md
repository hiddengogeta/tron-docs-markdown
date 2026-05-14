

org.tron.trident.proto

## Class Response.AccountResourceMessage.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.AccountResourceMessage.Builder](../../../../org/tron/trident/proto/Response.AccountResourceMessage.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.AccountResourceMessage.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.AccountResourceMessageOrBuilder](../../../../org/tron/trident/proto/Response.AccountResourceMessageOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.AccountResourceMessage](../../../../org/tron/trident/proto/Response.AccountResourceMessage.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.AccountResourceMessage.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountResourceMessage.Builder>
  implements Response.AccountResourceMessageOrBuilder
  ```

  Protobuf type `protocol.AccountResourceMessage`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `Response.AccountResourceMessage.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.AccountResourceMessage` | `build()` |
    | `Response.AccountResourceMessage` | `buildPartial()` |
    | `Response.AccountResourceMessage.Builder` | `clear()` |
    | `Response.AccountResourceMessage.Builder` | `clearAssetNetLimit()` |
    | `Response.AccountResourceMessage.Builder` | `clearAssetNetUsed()` |
    | `Response.AccountResourceMessage.Builder` | `clearEnergyLimit()` `int64 EnergyLimit = 14;` |
    | `Response.AccountResourceMessage.Builder` | `clearEnergyUsed()` `int64 EnergyUsed = 13;` |
    | `Response.AccountResourceMessage.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.AccountResourceMessage.Builder` | `clearFreeNetLimit()` `int64 freeNetLimit = 2;` |
    | `Response.AccountResourceMessage.Builder` | `clearFreeNetUsed()` `int64 freeNetUsed = 1;` |
    | `Response.AccountResourceMessage.Builder` | `clearNetLimit()` `int64 NetLimit = 4;` |
    | `Response.AccountResourceMessage.Builder` | `clearNetUsed()` `int64 NetUsed = 3;` |
    | `Response.AccountResourceMessage.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.AccountResourceMessage.Builder` | `clearStorageLimit()` `int64 storageLimit = 22;` |
    | `Response.AccountResourceMessage.Builder` | `clearStorageUsed()` `int64 storageUsed = 21;` |
    | `Response.AccountResourceMessage.Builder` | `clearTotalEnergyLimit()` `int64 TotalEnergyLimit = 15;` |
    | `Response.AccountResourceMessage.Builder` | `clearTotalEnergyWeight()` `int64 TotalEnergyWeight = 16;` |
    | `Response.AccountResourceMessage.Builder` | `clearTotalNetLimit()` `int64 TotalNetLimit = 7;` |
    | `Response.AccountResourceMessage.Builder` | `clearTotalNetWeight()` `int64 TotalNetWeight = 8;` |
    | `Response.AccountResourceMessage.Builder` | `clearTotalTronPowerWeight()` `int64 TotalTronPowerWeight = 9;` |
    | `Response.AccountResourceMessage.Builder` | `clearTronPowerLimit()` `int64 tronPowerLimit = 11;` |
    | `Response.AccountResourceMessage.Builder` | `clearTronPowerUsed()` `int64 tronPowerUsed = 10;` |
    | `Response.AccountResourceMessage.Builder` | `clone()` |
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
    | `Response.AccountResourceMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getEnergyLimit()` `int64 EnergyLimit = 14;` |
    | `long` | `getEnergyUsed()` `int64 EnergyUsed = 13;` |
    | `long` | `getFreeNetLimit()` `int64 freeNetLimit = 2;` |
    | `long` | `getFreeNetUsed()` `int64 freeNetUsed = 1;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getMutableAssetNetLimit()` Deprecated. |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getMutableAssetNetUsed()` Deprecated. |
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
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMapFieldReflection(int number)` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMutableMapFieldReflection(int number)` |
    | `boolean` | `isInitialized()` |
    | `Response.AccountResourceMessage.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.AccountResourceMessage.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.AccountResourceMessage.Builder` | `mergeFrom(Response.AccountResourceMessage other)` |
    | `Response.AccountResourceMessage.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.AccountResourceMessage.Builder` | `putAllAssetNetLimit(java.util.Map<java.lang.String,java.lang.Long> values)` `map<string, int64> assetNetLimit = 6;` |
    | `Response.AccountResourceMessage.Builder` | `putAllAssetNetUsed(java.util.Map<java.lang.String,java.lang.Long> values)` `map<string, int64> assetNetUsed = 5;` |
    | `Response.AccountResourceMessage.Builder` | `putAssetNetLimit(java.lang.String key, long value)` `map<string, int64> assetNetLimit = 6;` |
    | `Response.AccountResourceMessage.Builder` | `putAssetNetUsed(java.lang.String key, long value)` `map<string, int64> assetNetUsed = 5;` |
    | `Response.AccountResourceMessage.Builder` | `removeAssetNetLimit(java.lang.String key)` `map<string, int64> assetNetLimit = 6;` |
    | `Response.AccountResourceMessage.Builder` | `removeAssetNetUsed(java.lang.String key)` `map<string, int64> assetNetUsed = 5;` |
    | `Response.AccountResourceMessage.Builder` | `setEnergyLimit(long value)` `int64 EnergyLimit = 14;` |
    | `Response.AccountResourceMessage.Builder` | `setEnergyUsed(long value)` `int64 EnergyUsed = 13;` |
    | `Response.AccountResourceMessage.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.AccountResourceMessage.Builder` | `setFreeNetLimit(long value)` `int64 freeNetLimit = 2;` |
    | `Response.AccountResourceMessage.Builder` | `setFreeNetUsed(long value)` `int64 freeNetUsed = 1;` |
    | `Response.AccountResourceMessage.Builder` | `setNetLimit(long value)` `int64 NetLimit = 4;` |
    | `Response.AccountResourceMessage.Builder` | `setNetUsed(long value)` `int64 NetUsed = 3;` |
    | `Response.AccountResourceMessage.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.AccountResourceMessage.Builder` | `setStorageLimit(long value)` `int64 storageLimit = 22;` |
    | `Response.AccountResourceMessage.Builder` | `setStorageUsed(long value)` `int64 storageUsed = 21;` |
    | `Response.AccountResourceMessage.Builder` | `setTotalEnergyLimit(long value)` `int64 TotalEnergyLimit = 15;` |
    | `Response.AccountResourceMessage.Builder` | `setTotalEnergyWeight(long value)` `int64 TotalEnergyWeight = 16;` |
    | `Response.AccountResourceMessage.Builder` | `setTotalNetLimit(long value)` `int64 TotalNetLimit = 7;` |
    | `Response.AccountResourceMessage.Builder` | `setTotalNetWeight(long value)` `int64 TotalNetWeight = 8;` |
    | `Response.AccountResourceMessage.Builder` | `setTotalTronPowerWeight(long value)` `int64 TotalTronPowerWeight = 9;` |
    | `Response.AccountResourceMessage.Builder` | `setTronPowerLimit(long value)` `int64 tronPowerLimit = 11;` |
    | `Response.AccountResourceMessage.Builder` | `setTronPowerUsed(long value)` `int64 tronPowerUsed = 10;` |
    | `Response.AccountResourceMessage.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

    - ### Methods inherited from class com.google.protobuf.GeneratedMessageV3.Builder

      `getAllFields, getField, getFieldBuilder, getOneofFieldDescriptor, getParentForChildren, getRepeatedField, getRepeatedFieldBuilder, getRepeatedFieldCount, getUnknownFields, getUnknownFieldSetBuilder, hasField, hasOneof, internalGetMapField, internalGetMutableMapField, isClean, markClean, mergeUnknownLengthDelimitedField, mergeUnknownVarintField, newBuilderForField, onBuilt, onChanged, parseUnknownField, setUnknownFieldSetBuilder, setUnknownFieldsProto3`
    - ### Methods inherited from class com.google.protobuf.AbstractMessage.Builder

      `findInitializationErrors, getInitializationErrorString, internalMergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, newUninitializedMessageException, toString`
    - ### Methods inherited from class com.google.protobuf.AbstractMessageLite.Builder

      `addAll, addAll, mergeDelimitedFrom, mergeDelimitedFrom, newUninitializedMessageException`
    - ### Methods inherited from class java.lang.Object

      `equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`
    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.Message.Builder

      `mergeDelimitedFrom, mergeDelimitedFrom`

* + ### Method Detail

    - #### getDescriptor

      ```
      public static final com.google.protobuf.Descriptors.Descriptor getDescriptor()
      ```
    - #### internalGetMapFieldReflection

      ```
      protected com.google.protobuf.MapFieldReflectionAccessor internalGetMapFieldReflection(int number)
      ```

      Overrides:
      :   `internalGetMapFieldReflection` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountResourceMessage.Builder>`
    - #### internalGetMutableMapFieldReflection

      ```
      protected com.google.protobuf.MapFieldReflectionAccessor internalGetMutableMapFieldReflection(int number)
      ```

      Overrides:
      :   `internalGetMutableMapFieldReflection` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountResourceMessage.Builder>`
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountResourceMessage.Builder>`
    - #### clear

      ```
      public Response.AccountResourceMessage.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountResourceMessage.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountResourceMessage.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.AccountResourceMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.AccountResourceMessage build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.AccountResourceMessage buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.AccountResourceMessage.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountResourceMessage.Builder>`
    - #### setField

      ```
      public Response.AccountResourceMessage.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                              java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountResourceMessage.Builder>`
    - #### clearField

      ```
      public Response.AccountResourceMessage.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountResourceMessage.Builder>`
    - #### clearOneof

      ```
      public Response.AccountResourceMessage.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountResourceMessage.Builder>`
    - #### setRepeatedField

      ```
      public Response.AccountResourceMessage.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                      int index,
                                                                      java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountResourceMessage.Builder>`
    - #### addRepeatedField

      ```
      public Response.AccountResourceMessage.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                      java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountResourceMessage.Builder>`
    - #### mergeFrom

      ```
      public Response.AccountResourceMessage.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.AccountResourceMessage.Builder>`
    - #### mergeFrom

      ```
      public Response.AccountResourceMessage.Builder mergeFrom(Response.AccountResourceMessage other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountResourceMessage.Builder>`
    - #### mergeFrom

      ```
      public Response.AccountResourceMessage.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.AccountResourceMessage.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getFreeNetUsed

      ```
      public long getFreeNetUsed()
      ```

      `int64 freeNetUsed = 1;`

      Specified by:
      :   `getFreeNetUsed` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The freeNetUsed.
    - #### setFreeNetUsed

      ```
      public Response.AccountResourceMessage.Builder setFreeNetUsed(long value)
      ```

      `int64 freeNetUsed = 1;`

      Parameters:
      :   `value` - The freeNetUsed to set.

      Returns:
      :   This builder for chaining.
    - #### clearFreeNetUsed

      ```
      public Response.AccountResourceMessage.Builder clearFreeNetUsed()
      ```

      `int64 freeNetUsed = 1;`

      Returns:
      :   This builder for chaining.
    - #### getFreeNetLimit

      ```
      public long getFreeNetLimit()
      ```

      `int64 freeNetLimit = 2;`

      Specified by:
      :   `getFreeNetLimit` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The freeNetLimit.
    - #### setFreeNetLimit

      ```
      public Response.AccountResourceMessage.Builder setFreeNetLimit(long value)
      ```

      `int64 freeNetLimit = 2;`

      Parameters:
      :   `value` - The freeNetLimit to set.

      Returns:
      :   This builder for chaining.
    - #### clearFreeNetLimit

      ```
      public Response.AccountResourceMessage.Builder clearFreeNetLimit()
      ```

      `int64 freeNetLimit = 2;`

      Returns:
      :   This builder for chaining.
    - #### getNetUsed

      ```
      public long getNetUsed()
      ```

      `int64 NetUsed = 3;`

      Specified by:
      :   `getNetUsed` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The netUsed.
    - #### setNetUsed

      ```
      public Response.AccountResourceMessage.Builder setNetUsed(long value)
      ```

      `int64 NetUsed = 3;`

      Parameters:
      :   `value` - The netUsed to set.

      Returns:
      :   This builder for chaining.
    - #### clearNetUsed

      ```
      public Response.AccountResourceMessage.Builder clearNetUsed()
      ```

      `int64 NetUsed = 3;`

      Returns:
      :   This builder for chaining.
    - #### getNetLimit

      ```
      public long getNetLimit()
      ```

      `int64 NetLimit = 4;`

      Specified by:
      :   `getNetLimit` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The netLimit.
    - #### setNetLimit

      ```
      public Response.AccountResourceMessage.Builder setNetLimit(long value)
      ```

      `int64 NetLimit = 4;`

      Parameters:
      :   `value` - The netLimit to set.

      Returns:
      :   This builder for chaining.
    - #### clearNetLimit

      ```
      public Response.AccountResourceMessage.Builder clearNetLimit()
      ```

      `int64 NetLimit = 4;`

      Returns:
      :   This builder for chaining.
    - #### getAssetNetUsedCount

      ```
      public int getAssetNetUsedCount()
      ```

      Description copied from interface: `Response.AccountResourceMessageOrBuilder`

      `map<string, int64> assetNetUsed = 5;`

      Specified by:
      :   `getAssetNetUsedCount` in interface `Response.AccountResourceMessageOrBuilder`
    - #### containsAssetNetUsed

      ```
      public boolean containsAssetNetUsed(java.lang.String key)
      ```

      `map<string, int64> assetNetUsed = 5;`

      Specified by:
      :   `containsAssetNetUsed` in interface `Response.AccountResourceMessageOrBuilder`
    - #### getAssetNetUsed

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getAssetNetUsed()
      ```

      Deprecated.

      Use [`getAssetNetUsedMap()`](../../../../org/tron/trident/proto/Response.AccountResourceMessage.Builder.html#getAssetNetUsedMap--) instead.

      Specified by:
      :   `getAssetNetUsed` in interface `Response.AccountResourceMessageOrBuilder`
    - #### getAssetNetUsedMap

      ```
      public java.util.Map<java.lang.String,java.lang.Long> getAssetNetUsedMap()
      ```

      `map<string, int64> assetNetUsed = 5;`

      Specified by:
      :   `getAssetNetUsedMap` in interface `Response.AccountResourceMessageOrBuilder`
    - #### getAssetNetUsedOrDefault

      ```
      public long getAssetNetUsedOrDefault(java.lang.String key,
                                           long defaultValue)
      ```

      `map<string, int64> assetNetUsed = 5;`

      Specified by:
      :   `getAssetNetUsedOrDefault` in interface `Response.AccountResourceMessageOrBuilder`
    - #### getAssetNetUsedOrThrow

      ```
      public long getAssetNetUsedOrThrow(java.lang.String key)
      ```

      `map<string, int64> assetNetUsed = 5;`

      Specified by:
      :   `getAssetNetUsedOrThrow` in interface `Response.AccountResourceMessageOrBuilder`
    - #### clearAssetNetUsed

      ```
      public Response.AccountResourceMessage.Builder clearAssetNetUsed()
      ```
    - #### removeAssetNetUsed

      ```
      public Response.AccountResourceMessage.Builder removeAssetNetUsed(java.lang.String key)
      ```

      `map<string, int64> assetNetUsed = 5;`
    - #### getMutableAssetNetUsed

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getMutableAssetNetUsed()
      ```

      Deprecated.

      Use alternate mutation accessors instead.
    - #### putAssetNetUsed

      ```
      public Response.AccountResourceMessage.Builder putAssetNetUsed(java.lang.String key,
                                                                     long value)
      ```

      `map<string, int64> assetNetUsed = 5;`
    - #### putAllAssetNetUsed

      ```
      public Response.AccountResourceMessage.Builder putAllAssetNetUsed(java.util.Map<java.lang.String,java.lang.Long> values)
      ```

      `map<string, int64> assetNetUsed = 5;`
    - #### getAssetNetLimitCount

      ```
      public int getAssetNetLimitCount()
      ```

      Description copied from interface: `Response.AccountResourceMessageOrBuilder`

      `map<string, int64> assetNetLimit = 6;`

      Specified by:
      :   `getAssetNetLimitCount` in interface `Response.AccountResourceMessageOrBuilder`
    - #### containsAssetNetLimit

      ```
      public boolean containsAssetNetLimit(java.lang.String key)
      ```

      `map<string, int64> assetNetLimit = 6;`

      Specified by:
      :   `containsAssetNetLimit` in interface `Response.AccountResourceMessageOrBuilder`
    - #### getAssetNetLimit

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getAssetNetLimit()
      ```

      Deprecated.

      Use [`getAssetNetLimitMap()`](../../../../org/tron/trident/proto/Response.AccountResourceMessage.Builder.html#getAssetNetLimitMap--) instead.

      Specified by:
      :   `getAssetNetLimit` in interface `Response.AccountResourceMessageOrBuilder`
    - #### getAssetNetLimitMap

      ```
      public java.util.Map<java.lang.String,java.lang.Long> getAssetNetLimitMap()
      ```

      `map<string, int64> assetNetLimit = 6;`

      Specified by:
      :   `getAssetNetLimitMap` in interface `Response.AccountResourceMessageOrBuilder`
    - #### getAssetNetLimitOrDefault

      ```
      public long getAssetNetLimitOrDefault(java.lang.String key,
                                            long defaultValue)
      ```

      `map<string, int64> assetNetLimit = 6;`

      Specified by:
      :   `getAssetNetLimitOrDefault` in interface `Response.AccountResourceMessageOrBuilder`
    - #### getAssetNetLimitOrThrow

      ```
      public long getAssetNetLimitOrThrow(java.lang.String key)
      ```

      `map<string, int64> assetNetLimit = 6;`

      Specified by:
      :   `getAssetNetLimitOrThrow` in interface `Response.AccountResourceMessageOrBuilder`
    - #### clearAssetNetLimit

      ```
      public Response.AccountResourceMessage.Builder clearAssetNetLimit()
      ```
    - #### removeAssetNetLimit

      ```
      public Response.AccountResourceMessage.Builder removeAssetNetLimit(java.lang.String key)
      ```

      `map<string, int64> assetNetLimit = 6;`
    - #### getMutableAssetNetLimit

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getMutableAssetNetLimit()
      ```

      Deprecated.

      Use alternate mutation accessors instead.
    - #### putAssetNetLimit

      ```
      public Response.AccountResourceMessage.Builder putAssetNetLimit(java.lang.String key,
                                                                      long value)
      ```

      `map<string, int64> assetNetLimit = 6;`
    - #### putAllAssetNetLimit

      ```
      public Response.AccountResourceMessage.Builder putAllAssetNetLimit(java.util.Map<java.lang.String,java.lang.Long> values)
      ```

      `map<string, int64> assetNetLimit = 6;`
    - #### getTotalNetLimit

      ```
      public long getTotalNetLimit()
      ```

      `int64 TotalNetLimit = 7;`

      Specified by:
      :   `getTotalNetLimit` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The totalNetLimit.
    - #### setTotalNetLimit

      ```
      public Response.AccountResourceMessage.Builder setTotalNetLimit(long value)
      ```

      `int64 TotalNetLimit = 7;`

      Parameters:
      :   `value` - The totalNetLimit to set.

      Returns:
      :   This builder for chaining.
    - #### clearTotalNetLimit

      ```
      public Response.AccountResourceMessage.Builder clearTotalNetLimit()
      ```

      `int64 TotalNetLimit = 7;`

      Returns:
      :   This builder for chaining.
    - #### getTotalNetWeight

      ```
      public long getTotalNetWeight()
      ```

      `int64 TotalNetWeight = 8;`

      Specified by:
      :   `getTotalNetWeight` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The totalNetWeight.
    - #### setTotalNetWeight

      ```
      public Response.AccountResourceMessage.Builder setTotalNetWeight(long value)
      ```

      `int64 TotalNetWeight = 8;`

      Parameters:
      :   `value` - The totalNetWeight to set.

      Returns:
      :   This builder for chaining.
    - #### clearTotalNetWeight

      ```
      public Response.AccountResourceMessage.Builder clearTotalNetWeight()
      ```

      `int64 TotalNetWeight = 8;`

      Returns:
      :   This builder for chaining.
    - #### getTotalTronPowerWeight

      ```
      public long getTotalTronPowerWeight()
      ```

      `int64 TotalTronPowerWeight = 9;`

      Specified by:
      :   `getTotalTronPowerWeight` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The totalTronPowerWeight.
    - #### setTotalTronPowerWeight

      ```
      public Response.AccountResourceMessage.Builder setTotalTronPowerWeight(long value)
      ```

      `int64 TotalTronPowerWeight = 9;`

      Parameters:
      :   `value` - The totalTronPowerWeight to set.

      Returns:
      :   This builder for chaining.
    - #### clearTotalTronPowerWeight

      ```
      public Response.AccountResourceMessage.Builder clearTotalTronPowerWeight()
      ```

      `int64 TotalTronPowerWeight = 9;`

      Returns:
      :   This builder for chaining.
    - #### getTronPowerUsed

      ```
      public long getTronPowerUsed()
      ```

      `int64 tronPowerUsed = 10;`

      Specified by:
      :   `getTronPowerUsed` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The tronPowerUsed.
    - #### setTronPowerUsed

      ```
      public Response.AccountResourceMessage.Builder setTronPowerUsed(long value)
      ```

      `int64 tronPowerUsed = 10;`

      Parameters:
      :   `value` - The tronPowerUsed to set.

      Returns:
      :   This builder for chaining.
    - #### clearTronPowerUsed

      ```
      public Response.AccountResourceMessage.Builder clearTronPowerUsed()
      ```

      `int64 tronPowerUsed = 10;`

      Returns:
      :   This builder for chaining.
    - #### getTronPowerLimit

      ```
      public long getTronPowerLimit()
      ```

      `int64 tronPowerLimit = 11;`

      Specified by:
      :   `getTronPowerLimit` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The tronPowerLimit.
    - #### setTronPowerLimit

      ```
      public Response.AccountResourceMessage.Builder setTronPowerLimit(long value)
      ```

      `int64 tronPowerLimit = 11;`

      Parameters:
      :   `value` - The tronPowerLimit to set.

      Returns:
      :   This builder for chaining.
    - #### clearTronPowerLimit

      ```
      public Response.AccountResourceMessage.Builder clearTronPowerLimit()
      ```

      `int64 tronPowerLimit = 11;`

      Returns:
      :   This builder for chaining.
    - #### getEnergyUsed

      ```
      public long getEnergyUsed()
      ```

      `int64 EnergyUsed = 13;`

      Specified by:
      :   `getEnergyUsed` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The energyUsed.
    - #### setEnergyUsed

      ```
      public Response.AccountResourceMessage.Builder setEnergyUsed(long value)
      ```

      `int64 EnergyUsed = 13;`

      Parameters:
      :   `value` - The energyUsed to set.

      Returns:
      :   This builder for chaining.
    - #### clearEnergyUsed

      ```
      public Response.AccountResourceMessage.Builder clearEnergyUsed()
      ```

      `int64 EnergyUsed = 13;`

      Returns:
      :   This builder for chaining.
    - #### getEnergyLimit

      ```
      public long getEnergyLimit()
      ```

      `int64 EnergyLimit = 14;`

      Specified by:
      :   `getEnergyLimit` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The energyLimit.
    - #### setEnergyLimit

      ```
      public Response.AccountResourceMessage.Builder setEnergyLimit(long value)
      ```

      `int64 EnergyLimit = 14;`

      Parameters:
      :   `value` - The energyLimit to set.

      Returns:
      :   This builder for chaining.
    - #### clearEnergyLimit

      ```
      public Response.AccountResourceMessage.Builder clearEnergyLimit()
      ```

      `int64 EnergyLimit = 14;`

      Returns:
      :   This builder for chaining.
    - #### getTotalEnergyLimit

      ```
      public long getTotalEnergyLimit()
      ```

      `int64 TotalEnergyLimit = 15;`

      Specified by:
      :   `getTotalEnergyLimit` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The totalEnergyLimit.
    - #### setTotalEnergyLimit

      ```
      public Response.AccountResourceMessage.Builder setTotalEnergyLimit(long value)
      ```

      `int64 TotalEnergyLimit = 15;`

      Parameters:
      :   `value` - The totalEnergyLimit to set.

      Returns:
      :   This builder for chaining.
    - #### clearTotalEnergyLimit

      ```
      public Response.AccountResourceMessage.Builder clearTotalEnergyLimit()
      ```

      `int64 TotalEnergyLimit = 15;`

      Returns:
      :   This builder for chaining.
    - #### getTotalEnergyWeight

      ```
      public long getTotalEnergyWeight()
      ```

      `int64 TotalEnergyWeight = 16;`

      Specified by:
      :   `getTotalEnergyWeight` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The totalEnergyWeight.
    - #### setTotalEnergyWeight

      ```
      public Response.AccountResourceMessage.Builder setTotalEnergyWeight(long value)
      ```

      `int64 TotalEnergyWeight = 16;`

      Parameters:
      :   `value` - The totalEnergyWeight to set.

      Returns:
      :   This builder for chaining.
    - #### clearTotalEnergyWeight

      ```
      public Response.AccountResourceMessage.Builder clearTotalEnergyWeight()
      ```

      `int64 TotalEnergyWeight = 16;`

      Returns:
      :   This builder for chaining.
    - #### getStorageUsed

      ```
      public long getStorageUsed()
      ```

      `int64 storageUsed = 21;`

      Specified by:
      :   `getStorageUsed` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The storageUsed.
    - #### setStorageUsed

      ```
      public Response.AccountResourceMessage.Builder setStorageUsed(long value)
      ```

      `int64 storageUsed = 21;`

      Parameters:
      :   `value` - The storageUsed to set.

      Returns:
      :   This builder for chaining.
    - #### clearStorageUsed

      ```
      public Response.AccountResourceMessage.Builder clearStorageUsed()
      ```

      `int64 storageUsed = 21;`

      Returns:
      :   This builder for chaining.
    - #### getStorageLimit

      ```
      public long getStorageLimit()
      ```

      `int64 storageLimit = 22;`

      Specified by:
      :   `getStorageLimit` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The storageLimit.
    - #### setStorageLimit

      ```
      public Response.AccountResourceMessage.Builder setStorageLimit(long value)
      ```

      `int64 storageLimit = 22;`

      Parameters:
      :   `value` - The storageLimit to set.

      Returns:
      :   This builder for chaining.
    - #### clearStorageLimit

      ```
      public Response.AccountResourceMessage.Builder clearStorageLimit()
      ```

      `int64 storageLimit = 22;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.AccountResourceMessage.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountResourceMessage.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.AccountResourceMessage.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountResourceMessage.Builder>`