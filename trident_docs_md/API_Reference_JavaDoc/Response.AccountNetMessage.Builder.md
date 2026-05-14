

org.tron.trident.proto

## Class Response.AccountNetMessage.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.AccountNetMessage.Builder](../../../../org/tron/trident/proto/Response.AccountNetMessage.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.AccountNetMessage.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.AccountNetMessageOrBuilder](../../../../org/tron/trident/proto/Response.AccountNetMessageOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.AccountNetMessage](../../../../org/tron/trident/proto/Response.AccountNetMessage.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.AccountNetMessage.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountNetMessage.Builder>
  implements Response.AccountNetMessageOrBuilder
  ```

  ```
   deprecated
  ```

  Protobuf type `protocol.AccountNetMessage`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `Response.AccountNetMessage.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.AccountNetMessage` | `build()` |
    | `Response.AccountNetMessage` | `buildPartial()` |
    | `Response.AccountNetMessage.Builder` | `clear()` |
    | `Response.AccountNetMessage.Builder` | `clearAssetNetLimit()` |
    | `Response.AccountNetMessage.Builder` | `clearAssetNetUsed()` |
    | `Response.AccountNetMessage.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.AccountNetMessage.Builder` | `clearFreeNetLimit()` `int64 freeNetLimit = 2;` |
    | `Response.AccountNetMessage.Builder` | `clearFreeNetUsed()` `int64 freeNetUsed = 1;` |
    | `Response.AccountNetMessage.Builder` | `clearNetLimit()` `int64 NetLimit = 4;` |
    | `Response.AccountNetMessage.Builder` | `clearNetUsed()` `int64 NetUsed = 3;` |
    | `Response.AccountNetMessage.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.AccountNetMessage.Builder` | `clearTotalNetLimit()` `int64 TotalNetLimit = 7;` |
    | `Response.AccountNetMessage.Builder` | `clearTotalNetWeight()` `int64 TotalNetWeight = 8;` |
    | `Response.AccountNetMessage.Builder` | `clone()` |
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
    | `Response.AccountNetMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getFreeNetLimit()` `int64 freeNetLimit = 2;` |
    | `long` | `getFreeNetUsed()` `int64 freeNetUsed = 1;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getMutableAssetNetLimit()` Deprecated. |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getMutableAssetNetUsed()` Deprecated. |
    | `long` | `getNetLimit()` `int64 NetLimit = 4;` |
    | `long` | `getNetUsed()` `int64 NetUsed = 3;` |
    | `long` | `getTotalNetLimit()` `int64 TotalNetLimit = 7;` |
    | `long` | `getTotalNetWeight()` `int64 TotalNetWeight = 8;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMapFieldReflection(int number)` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMutableMapFieldReflection(int number)` |
    | `boolean` | `isInitialized()` |
    | `Response.AccountNetMessage.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.AccountNetMessage.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.AccountNetMessage.Builder` | `mergeFrom(Response.AccountNetMessage other)` |
    | `Response.AccountNetMessage.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.AccountNetMessage.Builder` | `putAllAssetNetLimit(java.util.Map<java.lang.String,java.lang.Long> values)` `map<string, int64> assetNetLimit = 6;` |
    | `Response.AccountNetMessage.Builder` | `putAllAssetNetUsed(java.util.Map<java.lang.String,java.lang.Long> values)` `map<string, int64> assetNetUsed = 5;` |
    | `Response.AccountNetMessage.Builder` | `putAssetNetLimit(java.lang.String key, long value)` `map<string, int64> assetNetLimit = 6;` |
    | `Response.AccountNetMessage.Builder` | `putAssetNetUsed(java.lang.String key, long value)` `map<string, int64> assetNetUsed = 5;` |
    | `Response.AccountNetMessage.Builder` | `removeAssetNetLimit(java.lang.String key)` `map<string, int64> assetNetLimit = 6;` |
    | `Response.AccountNetMessage.Builder` | `removeAssetNetUsed(java.lang.String key)` `map<string, int64> assetNetUsed = 5;` |
    | `Response.AccountNetMessage.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.AccountNetMessage.Builder` | `setFreeNetLimit(long value)` `int64 freeNetLimit = 2;` |
    | `Response.AccountNetMessage.Builder` | `setFreeNetUsed(long value)` `int64 freeNetUsed = 1;` |
    | `Response.AccountNetMessage.Builder` | `setNetLimit(long value)` `int64 NetLimit = 4;` |
    | `Response.AccountNetMessage.Builder` | `setNetUsed(long value)` `int64 NetUsed = 3;` |
    | `Response.AccountNetMessage.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.AccountNetMessage.Builder` | `setTotalNetLimit(long value)` `int64 TotalNetLimit = 7;` |
    | `Response.AccountNetMessage.Builder` | `setTotalNetWeight(long value)` `int64 TotalNetWeight = 8;` |
    | `Response.AccountNetMessage.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetMapFieldReflection` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountNetMessage.Builder>`
    - #### internalGetMutableMapFieldReflection

      ```
      protected com.google.protobuf.MapFieldReflectionAccessor internalGetMutableMapFieldReflection(int number)
      ```

      Overrides:
      :   `internalGetMutableMapFieldReflection` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountNetMessage.Builder>`
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountNetMessage.Builder>`
    - #### clear

      ```
      public Response.AccountNetMessage.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountNetMessage.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountNetMessage.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.AccountNetMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.AccountNetMessage build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.AccountNetMessage buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.AccountNetMessage.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountNetMessage.Builder>`
    - #### setField

      ```
      public Response.AccountNetMessage.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                         java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountNetMessage.Builder>`
    - #### clearField

      ```
      public Response.AccountNetMessage.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountNetMessage.Builder>`
    - #### clearOneof

      ```
      public Response.AccountNetMessage.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountNetMessage.Builder>`
    - #### setRepeatedField

      ```
      public Response.AccountNetMessage.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                 int index,
                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountNetMessage.Builder>`
    - #### addRepeatedField

      ```
      public Response.AccountNetMessage.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountNetMessage.Builder>`
    - #### mergeFrom

      ```
      public Response.AccountNetMessage.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.AccountNetMessage.Builder>`
    - #### mergeFrom

      ```
      public Response.AccountNetMessage.Builder mergeFrom(Response.AccountNetMessage other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountNetMessage.Builder>`
    - #### mergeFrom

      ```
      public Response.AccountNetMessage.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.AccountNetMessage.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getFreeNetUsed

      ```
      public long getFreeNetUsed()
      ```

      `int64 freeNetUsed = 1;`

      Specified by:
      :   `getFreeNetUsed` in interface `Response.AccountNetMessageOrBuilder`

      Returns:
      :   The freeNetUsed.
    - #### setFreeNetUsed

      ```
      public Response.AccountNetMessage.Builder setFreeNetUsed(long value)
      ```

      `int64 freeNetUsed = 1;`

      Parameters:
      :   `value` - The freeNetUsed to set.

      Returns:
      :   This builder for chaining.
    - #### clearFreeNetUsed

      ```
      public Response.AccountNetMessage.Builder clearFreeNetUsed()
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
      :   `getFreeNetLimit` in interface `Response.AccountNetMessageOrBuilder`

      Returns:
      :   The freeNetLimit.
    - #### setFreeNetLimit

      ```
      public Response.AccountNetMessage.Builder setFreeNetLimit(long value)
      ```

      `int64 freeNetLimit = 2;`

      Parameters:
      :   `value` - The freeNetLimit to set.

      Returns:
      :   This builder for chaining.
    - #### clearFreeNetLimit

      ```
      public Response.AccountNetMessage.Builder clearFreeNetLimit()
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
      :   `getNetUsed` in interface `Response.AccountNetMessageOrBuilder`

      Returns:
      :   The netUsed.
    - #### setNetUsed

      ```
      public Response.AccountNetMessage.Builder setNetUsed(long value)
      ```

      `int64 NetUsed = 3;`

      Parameters:
      :   `value` - The netUsed to set.

      Returns:
      :   This builder for chaining.
    - #### clearNetUsed

      ```
      public Response.AccountNetMessage.Builder clearNetUsed()
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
      :   `getNetLimit` in interface `Response.AccountNetMessageOrBuilder`

      Returns:
      :   The netLimit.
    - #### setNetLimit

      ```
      public Response.AccountNetMessage.Builder setNetLimit(long value)
      ```

      `int64 NetLimit = 4;`

      Parameters:
      :   `value` - The netLimit to set.

      Returns:
      :   This builder for chaining.
    - #### clearNetLimit

      ```
      public Response.AccountNetMessage.Builder clearNetLimit()
      ```

      `int64 NetLimit = 4;`

      Returns:
      :   This builder for chaining.
    - #### getAssetNetUsedCount

      ```
      public int getAssetNetUsedCount()
      ```

      Description copied from interface: `Response.AccountNetMessageOrBuilder`

      `map<string, int64> assetNetUsed = 5;`

      Specified by:
      :   `getAssetNetUsedCount` in interface `Response.AccountNetMessageOrBuilder`
    - #### containsAssetNetUsed

      ```
      public boolean containsAssetNetUsed(java.lang.String key)
      ```

      `map<string, int64> assetNetUsed = 5;`

      Specified by:
      :   `containsAssetNetUsed` in interface `Response.AccountNetMessageOrBuilder`
    - #### getAssetNetUsed

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getAssetNetUsed()
      ```

      Deprecated.

      Use [`getAssetNetUsedMap()`](../../../../org/tron/trident/proto/Response.AccountNetMessage.Builder.html#getAssetNetUsedMap--) instead.

      Specified by:
      :   `getAssetNetUsed` in interface `Response.AccountNetMessageOrBuilder`
    - #### getAssetNetUsedMap

      ```
      public java.util.Map<java.lang.String,java.lang.Long> getAssetNetUsedMap()
      ```

      `map<string, int64> assetNetUsed = 5;`

      Specified by:
      :   `getAssetNetUsedMap` in interface `Response.AccountNetMessageOrBuilder`
    - #### getAssetNetUsedOrDefault

      ```
      public long getAssetNetUsedOrDefault(java.lang.String key,
                                           long defaultValue)
      ```

      `map<string, int64> assetNetUsed = 5;`

      Specified by:
      :   `getAssetNetUsedOrDefault` in interface `Response.AccountNetMessageOrBuilder`
    - #### getAssetNetUsedOrThrow

      ```
      public long getAssetNetUsedOrThrow(java.lang.String key)
      ```

      `map<string, int64> assetNetUsed = 5;`

      Specified by:
      :   `getAssetNetUsedOrThrow` in interface `Response.AccountNetMessageOrBuilder`
    - #### clearAssetNetUsed

      ```
      public Response.AccountNetMessage.Builder clearAssetNetUsed()
      ```
    - #### removeAssetNetUsed

      ```
      public Response.AccountNetMessage.Builder removeAssetNetUsed(java.lang.String key)
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
      public Response.AccountNetMessage.Builder putAssetNetUsed(java.lang.String key,
                                                                long value)
      ```

      `map<string, int64> assetNetUsed = 5;`
    - #### putAllAssetNetUsed

      ```
      public Response.AccountNetMessage.Builder putAllAssetNetUsed(java.util.Map<java.lang.String,java.lang.Long> values)
      ```

      `map<string, int64> assetNetUsed = 5;`
    - #### getAssetNetLimitCount

      ```
      public int getAssetNetLimitCount()
      ```

      Description copied from interface: `Response.AccountNetMessageOrBuilder`

      `map<string, int64> assetNetLimit = 6;`

      Specified by:
      :   `getAssetNetLimitCount` in interface `Response.AccountNetMessageOrBuilder`
    - #### containsAssetNetLimit

      ```
      public boolean containsAssetNetLimit(java.lang.String key)
      ```

      `map<string, int64> assetNetLimit = 6;`

      Specified by:
      :   `containsAssetNetLimit` in interface `Response.AccountNetMessageOrBuilder`
    - #### getAssetNetLimit

      ```
      @Deprecated
      public java.util.Map<java.lang.String,java.lang.Long> getAssetNetLimit()
      ```

      Deprecated.

      Use [`getAssetNetLimitMap()`](../../../../org/tron/trident/proto/Response.AccountNetMessage.Builder.html#getAssetNetLimitMap--) instead.

      Specified by:
      :   `getAssetNetLimit` in interface `Response.AccountNetMessageOrBuilder`
    - #### getAssetNetLimitMap

      ```
      public java.util.Map<java.lang.String,java.lang.Long> getAssetNetLimitMap()
      ```

      `map<string, int64> assetNetLimit = 6;`

      Specified by:
      :   `getAssetNetLimitMap` in interface `Response.AccountNetMessageOrBuilder`
    - #### getAssetNetLimitOrDefault

      ```
      public long getAssetNetLimitOrDefault(java.lang.String key,
                                            long defaultValue)
      ```

      `map<string, int64> assetNetLimit = 6;`

      Specified by:
      :   `getAssetNetLimitOrDefault` in interface `Response.AccountNetMessageOrBuilder`
    - #### getAssetNetLimitOrThrow

      ```
      public long getAssetNetLimitOrThrow(java.lang.String key)
      ```

      `map<string, int64> assetNetLimit = 6;`

      Specified by:
      :   `getAssetNetLimitOrThrow` in interface `Response.AccountNetMessageOrBuilder`
    - #### clearAssetNetLimit

      ```
      public Response.AccountNetMessage.Builder clearAssetNetLimit()
      ```
    - #### removeAssetNetLimit

      ```
      public Response.AccountNetMessage.Builder removeAssetNetLimit(java.lang.String key)
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
      public Response.AccountNetMessage.Builder putAssetNetLimit(java.lang.String key,
                                                                 long value)
      ```

      `map<string, int64> assetNetLimit = 6;`
    - #### putAllAssetNetLimit

      ```
      public Response.AccountNetMessage.Builder putAllAssetNetLimit(java.util.Map<java.lang.String,java.lang.Long> values)
      ```

      `map<string, int64> assetNetLimit = 6;`
    - #### getTotalNetLimit

      ```
      public long getTotalNetLimit()
      ```

      `int64 TotalNetLimit = 7;`

      Specified by:
      :   `getTotalNetLimit` in interface `Response.AccountNetMessageOrBuilder`

      Returns:
      :   The totalNetLimit.
    - #### setTotalNetLimit

      ```
      public Response.AccountNetMessage.Builder setTotalNetLimit(long value)
      ```

      `int64 TotalNetLimit = 7;`

      Parameters:
      :   `value` - The totalNetLimit to set.

      Returns:
      :   This builder for chaining.
    - #### clearTotalNetLimit

      ```
      public Response.AccountNetMessage.Builder clearTotalNetLimit()
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
      :   `getTotalNetWeight` in interface `Response.AccountNetMessageOrBuilder`

      Returns:
      :   The totalNetWeight.
    - #### setTotalNetWeight

      ```
      public Response.AccountNetMessage.Builder setTotalNetWeight(long value)
      ```

      `int64 TotalNetWeight = 8;`

      Parameters:
      :   `value` - The totalNetWeight to set.

      Returns:
      :   This builder for chaining.
    - #### clearTotalNetWeight

      ```
      public Response.AccountNetMessage.Builder clearTotalNetWeight()
      ```

      `int64 TotalNetWeight = 8;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.AccountNetMessage.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountNetMessage.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.AccountNetMessage.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AccountNetMessage.Builder>`