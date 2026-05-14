

org.tron.trident.proto

## Class Response.AccountResourceMessage

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.AccountResourceMessage

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.AccountResourceMessageOrBuilder](../../../../org/tron/trident/proto/Response.AccountResourceMessageOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.AccountResourceMessage
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.AccountResourceMessageOrBuilder
  ```

  Protobuf type `protocol.AccountResourceMessage`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.AccountResourceMessage)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.AccountResourceMessage.Builder` Protobuf type `protocol.AccountResourceMessage` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `ASSETNETLIMIT_FIELD_NUMBER` |
    | `static int` | `ASSETNETUSED_FIELD_NUMBER` |
    | `static int` | `ENERGYLIMIT_FIELD_NUMBER` |
    | `static int` | `ENERGYUSED_FIELD_NUMBER` |
    | `static int` | `FREENETLIMIT_FIELD_NUMBER` |
    | `static int` | `FREENETUSED_FIELD_NUMBER` |
    | `static int` | `NETLIMIT_FIELD_NUMBER` |
    | `static int` | `NETUSED_FIELD_NUMBER` |
    | `static int` | `STORAGELIMIT_FIELD_NUMBER` |
    | `static int` | `STORAGEUSED_FIELD_NUMBER` |
    | `static int` | `TOTALENERGYLIMIT_FIELD_NUMBER` |
    | `static int` | `TOTALENERGYWEIGHT_FIELD_NUMBER` |
    | `static int` | `TOTALNETLIMIT_FIELD_NUMBER` |
    | `static int` | `TOTALNETWEIGHT_FIELD_NUMBER` |
    | `static int` | `TOTALTRONPOWERWEIGHT_FIELD_NUMBER` |
    | `static int` | `TRONPOWERLIMIT_FIELD_NUMBER` |
    | `static int` | `TRONPOWERUSED_FIELD_NUMBER` |

    - ### Fields inherited from class com.google.protobuf.GeneratedMessageV3

      `alwaysUseFieldBuilders, unknownFields`
    - ### Fields inherited from class com.google.protobuf.AbstractMessage

      `memoizedSize`
    - ### Fields inherited from class com.google.protobuf.AbstractMessageLite

      `memoizedHashCode`
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `boolean` | `containsAssetNetLimit(java.lang.String key)` `map<string, int64> assetNetLimit = 6;` |
    | `boolean` | `containsAssetNetUsed(java.lang.String key)` `map<string, int64> assetNetUsed = 5;` |
    | `boolean` | `equals(java.lang.Object obj)` |
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
    | `static Response.AccountResourceMessage` | `getDefaultInstance()` |
    | `Response.AccountResourceMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `long` | `getEnergyLimit()` `int64 EnergyLimit = 14;` |
    | `long` | `getEnergyUsed()` `int64 EnergyUsed = 13;` |
    | `long` | `getFreeNetLimit()` `int64 freeNetLimit = 2;` |
    | `long` | `getFreeNetUsed()` `int64 freeNetUsed = 1;` |
    | `long` | `getNetLimit()` `int64 NetLimit = 4;` |
    | `long` | `getNetUsed()` `int64 NetUsed = 3;` |
    | `com.google.protobuf.Parser<Response.AccountResourceMessage>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `long` | `getStorageLimit()` `int64 storageLimit = 22;` |
    | `long` | `getStorageUsed()` `int64 storageUsed = 21;` |
    | `long` | `getTotalEnergyLimit()` `int64 TotalEnergyLimit = 15;` |
    | `long` | `getTotalEnergyWeight()` `int64 TotalEnergyWeight = 16;` |
    | `long` | `getTotalNetLimit()` `int64 TotalNetLimit = 7;` |
    | `long` | `getTotalNetWeight()` `int64 TotalNetWeight = 8;` |
    | `long` | `getTotalTronPowerWeight()` `int64 TotalTronPowerWeight = 9;` |
    | `long` | `getTronPowerLimit()` `int64 tronPowerLimit = 11;` |
    | `long` | `getTronPowerUsed()` `int64 tronPowerUsed = 10;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `protected com.google.protobuf.MapFieldReflectionAccessor` | `internalGetMapFieldReflection(int number)` |
    | `boolean` | `isInitialized()` |
    | `static Response.AccountResourceMessage.Builder` | `newBuilder()` |
    | `static Response.AccountResourceMessage.Builder` | `newBuilder(Response.AccountResourceMessage prototype)` |
    | `Response.AccountResourceMessage.Builder` | `newBuilderForType()` |
    | `protected Response.AccountResourceMessage.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.AccountResourceMessage` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.AccountResourceMessage` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.AccountResourceMessage` | `parseFrom(byte[] data)` |
    | `static Response.AccountResourceMessage` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.AccountResourceMessage` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.AccountResourceMessage` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.AccountResourceMessage` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.AccountResourceMessage` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.AccountResourceMessage` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.AccountResourceMessage` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.AccountResourceMessage` | `parseFrom(java.io.InputStream input)` |
    | `static Response.AccountResourceMessage` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.AccountResourceMessage>` | `parser()` |
    | `Response.AccountResourceMessage.Builder` | `toBuilder()` |
    | `void` | `writeTo(com.google.protobuf.CodedOutputStream output)` |

    - ### Methods inherited from class com.google.protobuf.GeneratedMessageV3

      `canUseUnsafe, computeStringSize, computeStringSizeNoTag, emptyBooleanList, emptyDoubleList, emptyFloatList, emptyIntList, emptyList, emptyLongList, getAllFields, getDescriptorForType, getField, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof, internalGetMapField, isStringEmpty, makeExtensionsImmutable, makeMutableCopy, makeMutableCopy, mergeFromAndMakeImmutableInternal, mutableCopy, mutableCopy, mutableCopy, mutableCopy, mutableCopy, newBooleanList, newBuilderForType, newDoubleList, newFloatList, newIntList, newLongList, parseDelimitedWithIOException, parseDelimitedWithIOException, parseUnknownField, parseUnknownFieldProto3, parseWithIOException, parseWithIOException, parseWithIOException, parseWithIOException, serializeBooleanMapTo, serializeIntegerMapTo, serializeLongMapTo, serializeStringMapTo, writeReplace, writeString, writeStringNoTag`
    - ### Methods inherited from class com.google.protobuf.AbstractMessage

      `findInitializationErrors, getInitializationErrorString, hashBoolean, hashEnum, hashEnumList, hashFields, hashLong, toString`
    - ### Methods inherited from class com.google.protobuf.AbstractMessageLite

      `addAll, addAll, checkByteStringIsUtf8, toByteArray, toByteString, writeDelimitedTo, writeTo`
    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, wait, wait, wait`
    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLite

      `toByteArray, toByteString, writeDelimitedTo, writeTo`

* + ### Field Detail

    - #### FREENETUSED\_FIELD\_NUMBER

      ```
      public static final int FREENETUSED_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountResourceMessage.FREENETUSED_FIELD_NUMBER)
    - #### FREENETLIMIT\_FIELD\_NUMBER

      ```
      public static final int FREENETLIMIT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountResourceMessage.FREENETLIMIT_FIELD_NUMBER)
    - #### NETUSED\_FIELD\_NUMBER

      ```
      public static final int NETUSED_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountResourceMessage.NETUSED_FIELD_NUMBER)
    - #### NETLIMIT\_FIELD\_NUMBER

      ```
      public static final int NETLIMIT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountResourceMessage.NETLIMIT_FIELD_NUMBER)
    - #### ASSETNETUSED\_FIELD\_NUMBER

      ```
      public static final int ASSETNETUSED_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountResourceMessage.ASSETNETUSED_FIELD_NUMBER)
    - #### ASSETNETLIMIT\_FIELD\_NUMBER

      ```
      public static final int ASSETNETLIMIT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountResourceMessage.ASSETNETLIMIT_FIELD_NUMBER)
    - #### TOTALNETLIMIT\_FIELD\_NUMBER

      ```
      public static final int TOTALNETLIMIT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountResourceMessage.TOTALNETLIMIT_FIELD_NUMBER)
    - #### TOTALNETWEIGHT\_FIELD\_NUMBER

      ```
      public static final int TOTALNETWEIGHT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountResourceMessage.TOTALNETWEIGHT_FIELD_NUMBER)
    - #### TOTALTRONPOWERWEIGHT\_FIELD\_NUMBER

      ```
      public static final int TOTALTRONPOWERWEIGHT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountResourceMessage.TOTALTRONPOWERWEIGHT_FIELD_NUMBER)
    - #### TRONPOWERUSED\_FIELD\_NUMBER

      ```
      public static final int TRONPOWERUSED_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountResourceMessage.TRONPOWERUSED_FIELD_NUMBER)
    - #### TRONPOWERLIMIT\_FIELD\_NUMBER

      ```
      public static final int TRONPOWERLIMIT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountResourceMessage.TRONPOWERLIMIT_FIELD_NUMBER)
    - #### ENERGYUSED\_FIELD\_NUMBER

      ```
      public static final int ENERGYUSED_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountResourceMessage.ENERGYUSED_FIELD_NUMBER)
    - #### ENERGYLIMIT\_FIELD\_NUMBER

      ```
      public static final int ENERGYLIMIT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountResourceMessage.ENERGYLIMIT_FIELD_NUMBER)
    - #### TOTALENERGYLIMIT\_FIELD\_NUMBER

      ```
      public static final int TOTALENERGYLIMIT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountResourceMessage.TOTALENERGYLIMIT_FIELD_NUMBER)
    - #### TOTALENERGYWEIGHT\_FIELD\_NUMBER

      ```
      public static final int TOTALENERGYWEIGHT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountResourceMessage.TOTALENERGYWEIGHT_FIELD_NUMBER)
    - #### STORAGEUSED\_FIELD\_NUMBER

      ```
      public static final int STORAGEUSED_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountResourceMessage.STORAGEUSED_FIELD_NUMBER)
    - #### STORAGELIMIT\_FIELD\_NUMBER

      ```
      public static final int STORAGELIMIT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.AccountResourceMessage.STORAGELIMIT_FIELD_NUMBER)
  + ### Method Detail

    - #### newInstance

      ```
      protected java.lang.Object newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)
      ```

      Overrides:
      :   `newInstance` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDescriptor

      ```
      public static final com.google.protobuf.Descriptors.Descriptor getDescriptor()
      ```
    - #### internalGetMapFieldReflection

      ```
      protected com.google.protobuf.MapFieldReflectionAccessor internalGetMapFieldReflection(int number)
      ```

      Overrides:
      :   `internalGetMapFieldReflection` in class `com.google.protobuf.GeneratedMessageV3`
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getFreeNetUsed

      ```
      public long getFreeNetUsed()
      ```

      `int64 freeNetUsed = 1;`

      Specified by:
      :   `getFreeNetUsed` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The freeNetUsed.
    - #### getFreeNetLimit

      ```
      public long getFreeNetLimit()
      ```

      `int64 freeNetLimit = 2;`

      Specified by:
      :   `getFreeNetLimit` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The freeNetLimit.
    - #### getNetUsed

      ```
      public long getNetUsed()
      ```

      `int64 NetUsed = 3;`

      Specified by:
      :   `getNetUsed` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The netUsed.
    - #### getNetLimit

      ```
      public long getNetLimit()
      ```

      `int64 NetLimit = 4;`

      Specified by:
      :   `getNetLimit` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The netLimit.
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

      Use [`getAssetNetUsedMap()`](../../../../org/tron/trident/proto/Response.AccountResourceMessage.html#getAssetNetUsedMap--) instead.

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

      Use [`getAssetNetLimitMap()`](../../../../org/tron/trident/proto/Response.AccountResourceMessage.html#getAssetNetLimitMap--) instead.

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
    - #### getTotalNetLimit

      ```
      public long getTotalNetLimit()
      ```

      `int64 TotalNetLimit = 7;`

      Specified by:
      :   `getTotalNetLimit` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The totalNetLimit.
    - #### getTotalNetWeight

      ```
      public long getTotalNetWeight()
      ```

      `int64 TotalNetWeight = 8;`

      Specified by:
      :   `getTotalNetWeight` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The totalNetWeight.
    - #### getTotalTronPowerWeight

      ```
      public long getTotalTronPowerWeight()
      ```

      `int64 TotalTronPowerWeight = 9;`

      Specified by:
      :   `getTotalTronPowerWeight` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The totalTronPowerWeight.
    - #### getTronPowerUsed

      ```
      public long getTronPowerUsed()
      ```

      `int64 tronPowerUsed = 10;`

      Specified by:
      :   `getTronPowerUsed` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The tronPowerUsed.
    - #### getTronPowerLimit

      ```
      public long getTronPowerLimit()
      ```

      `int64 tronPowerLimit = 11;`

      Specified by:
      :   `getTronPowerLimit` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The tronPowerLimit.
    - #### getEnergyUsed

      ```
      public long getEnergyUsed()
      ```

      `int64 EnergyUsed = 13;`

      Specified by:
      :   `getEnergyUsed` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The energyUsed.
    - #### getEnergyLimit

      ```
      public long getEnergyLimit()
      ```

      `int64 EnergyLimit = 14;`

      Specified by:
      :   `getEnergyLimit` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The energyLimit.
    - #### getTotalEnergyLimit

      ```
      public long getTotalEnergyLimit()
      ```

      `int64 TotalEnergyLimit = 15;`

      Specified by:
      :   `getTotalEnergyLimit` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The totalEnergyLimit.
    - #### getTotalEnergyWeight

      ```
      public long getTotalEnergyWeight()
      ```

      `int64 TotalEnergyWeight = 16;`

      Specified by:
      :   `getTotalEnergyWeight` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The totalEnergyWeight.
    - #### getStorageUsed

      ```
      public long getStorageUsed()
      ```

      `int64 storageUsed = 21;`

      Specified by:
      :   `getStorageUsed` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The storageUsed.
    - #### getStorageLimit

      ```
      public long getStorageLimit()
      ```

      `int64 storageLimit = 22;`

      Specified by:
      :   `getStorageLimit` in interface `Response.AccountResourceMessageOrBuilder`

      Returns:
      :   The storageLimit.
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3`
    - #### writeTo

      ```
      public void writeTo(com.google.protobuf.CodedOutputStream output)
                   throws java.io.IOException
      ```

      Specified by:
      :   `writeTo` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `writeTo` in class `com.google.protobuf.GeneratedMessageV3`

      Throws:
      :   `java.io.IOException`
    - #### getSerializedSize

      ```
      public int getSerializedSize()
      ```

      Specified by:
      :   `getSerializedSize` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getSerializedSize` in class `com.google.protobuf.GeneratedMessageV3`
    - #### equals

      ```
      public boolean equals(java.lang.Object obj)
      ```

      Specified by:
      :   `equals` in interface `com.google.protobuf.Message`

      Overrides:
      :   `equals` in class `com.google.protobuf.AbstractMessage`
    - #### hashCode

      ```
      public int hashCode()
      ```

      Specified by:
      :   `hashCode` in interface `com.google.protobuf.Message`

      Overrides:
      :   `hashCode` in class `com.google.protobuf.AbstractMessage`
    - #### parseFrom

      ```
      public static Response.AccountResourceMessage parseFrom(java.nio.ByteBuffer data)
                                                       throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.AccountResourceMessage parseFrom(java.nio.ByteBuffer data,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.AccountResourceMessage parseFrom(com.google.protobuf.ByteString data)
                                                       throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.AccountResourceMessage parseFrom(com.google.protobuf.ByteString data,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.AccountResourceMessage parseFrom(byte[] data)
                                                       throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.AccountResourceMessage parseFrom(byte[] data,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.AccountResourceMessage parseFrom(java.io.InputStream input)
                                                       throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.AccountResourceMessage parseFrom(java.io.InputStream input,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.AccountResourceMessage parseDelimitedFrom(java.io.InputStream input)
                                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.AccountResourceMessage parseDelimitedFrom(java.io.InputStream input,
                                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.AccountResourceMessage parseFrom(com.google.protobuf.CodedInputStream input)
                                                       throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.AccountResourceMessage parseFrom(com.google.protobuf.CodedInputStream input,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.AccountResourceMessage.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.AccountResourceMessage.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.AccountResourceMessage.Builder newBuilder(Response.AccountResourceMessage prototype)
      ```
    - #### toBuilder

      ```
      public Response.AccountResourceMessage.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.AccountResourceMessage.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.AccountResourceMessage getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.AccountResourceMessage> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.AccountResourceMessage> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.AccountResourceMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`