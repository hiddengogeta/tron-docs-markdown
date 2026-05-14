

org.tron.trident.proto

## Class Response.Account.AccountResource

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.Account.AccountResource

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.Account.AccountResourceOrBuilder](../../../../org/tron/trident/proto/Response.Account.AccountResourceOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.Account](../../../../org/tron/trident/proto/Response.Account.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.Account.AccountResource
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.Account.AccountResourceOrBuilder
  ```

  Protobuf type `protocol.Account.AccountResource`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.Account.AccountResource)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.Account.AccountResource.Builder` Protobuf type `protocol.Account.AccountResource` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `ACQUIRED_DELEGATED_FROZEN_BALANCE_FOR_ENERGY_FIELD_NUMBER` |
    | `static int` | `ACQUIRED_DELEGATED_FROZENV2_BALANCE_FOR_ENERGY_FIELD_NUMBER` |
    | `static int` | `DELEGATED_FROZEN_BALANCE_FOR_ENERGY_FIELD_NUMBER` |
    | `static int` | `DELEGATED_FROZENV2_BALANCE_FOR_ENERGY_FIELD_NUMBER` |
    | `static int` | `ENERGY_USAGE_FIELD_NUMBER` |
    | `static int` | `ENERGY_WINDOW_OPTIMIZED_FIELD_NUMBER` |
    | `static int` | `ENERGY_WINDOW_SIZE_FIELD_NUMBER` |
    | `static int` | `FROZEN_BALANCE_FOR_ENERGY_FIELD_NUMBER` |
    | `static int` | `LATEST_CONSUME_TIME_FOR_ENERGY_FIELD_NUMBER` |
    | `static int` | `LATEST_EXCHANGE_STORAGE_TIME_FIELD_NUMBER` |
    | `static int` | `STORAGE_LIMIT_FIELD_NUMBER` |
    | `static int` | `STORAGE_USAGE_FIELD_NUMBER` |

    - ### Fields inherited from class com.google.protobuf.GeneratedMessageV3

      `alwaysUseFieldBuilders, unknownFields`
    - ### Fields inherited from class com.google.protobuf.AbstractMessage

      `memoizedSize`
    - ### Fields inherited from class com.google.protobuf.AbstractMessageLite

      `memoizedHashCode`
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `boolean` | `equals(java.lang.Object obj)` |
    | `long` | `getAcquiredDelegatedFrozenBalanceForEnergy()` Frozen balance provided by other accounts to this account |
    | `long` | `getAcquiredDelegatedFrozenV2BalanceForEnergy()` `int64 acquired_delegated_frozenV2_balance_for_energy = 11;` |
    | `static Response.Account.AccountResource` | `getDefaultInstance()` |
    | `Response.Account.AccountResource` | `getDefaultInstanceForType()` |
    | `long` | `getDelegatedFrozenBalanceForEnergy()` Frozen balances provided to other accounts |
    | `long` | `getDelegatedFrozenV2BalanceForEnergy()` `int64 delegated_frozenV2_balance_for_energy = 10;` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `long` | `getEnergyUsage()` energy resource, get from frozen |
    | `boolean` | `getEnergyWindowOptimized()` `bool energy_window_optimized = 12;` |
    | `long` | `getEnergyWindowSize()` `int64 energy_window_size = 9;` |
    | `Response.Account.Frozen` | `getFrozenBalanceForEnergy()` the frozen balance for energy |
    | `Response.Account.FrozenOrBuilder` | `getFrozenBalanceForEnergyOrBuilder()` the frozen balance for energy |
    | `long` | `getLatestConsumeTimeForEnergy()` `int64 latest_consume_time_for_energy = 3;` |
    | `long` | `getLatestExchangeStorageTime()` `int64 latest_exchange_storage_time = 8;` |
    | `com.google.protobuf.Parser<Response.Account.AccountResource>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `long` | `getStorageLimit()` storage resource, get from market |
    | `long` | `getStorageUsage()` `int64 storage_usage = 7;` |
    | `boolean` | `hasFrozenBalanceForEnergy()` the frozen balance for energy |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Response.Account.AccountResource.Builder` | `newBuilder()` |
    | `static Response.Account.AccountResource.Builder` | `newBuilder(Response.Account.AccountResource prototype)` |
    | `Response.Account.AccountResource.Builder` | `newBuilderForType()` |
    | `protected Response.Account.AccountResource.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.Account.AccountResource` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.Account.AccountResource` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Account.AccountResource` | `parseFrom(byte[] data)` |
    | `static Response.Account.AccountResource` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Account.AccountResource` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.Account.AccountResource` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Account.AccountResource` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.Account.AccountResource` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Account.AccountResource` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.Account.AccountResource` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.Account.AccountResource` | `parseFrom(java.io.InputStream input)` |
    | `static Response.Account.AccountResource` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.Account.AccountResource>` | `parser()` |
    | `Response.Account.AccountResource.Builder` | `toBuilder()` |
    | `void` | `writeTo(com.google.protobuf.CodedOutputStream output)` |

    - ### Methods inherited from class com.google.protobuf.GeneratedMessageV3

      `canUseUnsafe, computeStringSize, computeStringSizeNoTag, emptyBooleanList, emptyDoubleList, emptyFloatList, emptyIntList, emptyList, emptyLongList, getAllFields, getDescriptorForType, getField, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof, internalGetMapField, internalGetMapFieldReflection, isStringEmpty, makeExtensionsImmutable, makeMutableCopy, makeMutableCopy, mergeFromAndMakeImmutableInternal, mutableCopy, mutableCopy, mutableCopy, mutableCopy, mutableCopy, newBooleanList, newBuilderForType, newDoubleList, newFloatList, newIntList, newLongList, parseDelimitedWithIOException, parseDelimitedWithIOException, parseUnknownField, parseUnknownFieldProto3, parseWithIOException, parseWithIOException, parseWithIOException, parseWithIOException, serializeBooleanMapTo, serializeIntegerMapTo, serializeLongMapTo, serializeStringMapTo, writeReplace, writeString, writeStringNoTag`
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

    - #### ENERGY\_USAGE\_FIELD\_NUMBER

      ```
      public static final int ENERGY_USAGE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.AccountResource.ENERGY_USAGE_FIELD_NUMBER)
    - #### FROZEN\_BALANCE\_FOR\_ENERGY\_FIELD\_NUMBER

      ```
      public static final int FROZEN_BALANCE_FOR_ENERGY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.AccountResource.FROZEN_BALANCE_FOR_ENERGY_FIELD_NUMBER)
    - #### LATEST\_CONSUME\_TIME\_FOR\_ENERGY\_FIELD\_NUMBER

      ```
      public static final int LATEST_CONSUME_TIME_FOR_ENERGY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.AccountResource.LATEST_CONSUME_TIME_FOR_ENERGY_FIELD_NUMBER)
    - #### ACQUIRED\_DELEGATED\_FROZEN\_BALANCE\_FOR\_ENERGY\_FIELD\_NUMBER

      ```
      public static final int ACQUIRED_DELEGATED_FROZEN_BALANCE_FOR_ENERGY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.AccountResource.ACQUIRED_DELEGATED_FROZEN_BALANCE_FOR_ENERGY_FIELD_NUMBER)
    - #### DELEGATED\_FROZEN\_BALANCE\_FOR\_ENERGY\_FIELD\_NUMBER

      ```
      public static final int DELEGATED_FROZEN_BALANCE_FOR_ENERGY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.AccountResource.DELEGATED_FROZEN_BALANCE_FOR_ENERGY_FIELD_NUMBER)
    - #### STORAGE\_LIMIT\_FIELD\_NUMBER

      ```
      public static final int STORAGE_LIMIT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.AccountResource.STORAGE_LIMIT_FIELD_NUMBER)
    - #### STORAGE\_USAGE\_FIELD\_NUMBER

      ```
      public static final int STORAGE_USAGE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.AccountResource.STORAGE_USAGE_FIELD_NUMBER)
    - #### LATEST\_EXCHANGE\_STORAGE\_TIME\_FIELD\_NUMBER

      ```
      public static final int LATEST_EXCHANGE_STORAGE_TIME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.AccountResource.LATEST_EXCHANGE_STORAGE_TIME_FIELD_NUMBER)
    - #### ENERGY\_WINDOW\_SIZE\_FIELD\_NUMBER

      ```
      public static final int ENERGY_WINDOW_SIZE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.AccountResource.ENERGY_WINDOW_SIZE_FIELD_NUMBER)
    - #### DELEGATED\_FROZENV2\_BALANCE\_FOR\_ENERGY\_FIELD\_NUMBER

      ```
      public static final int DELEGATED_FROZENV2_BALANCE_FOR_ENERGY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.AccountResource.DELEGATED_FROZENV2_BALANCE_FOR_ENERGY_FIELD_NUMBER)
    - #### ACQUIRED\_DELEGATED\_FROZENV2\_BALANCE\_FOR\_ENERGY\_FIELD\_NUMBER

      ```
      public static final int ACQUIRED_DELEGATED_FROZENV2_BALANCE_FOR_ENERGY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.AccountResource.ACQUIRED_DELEGATED_FROZENV2_BALANCE_FOR_ENERGY_FIELD_NUMBER)
    - #### ENERGY\_WINDOW\_OPTIMIZED\_FIELD\_NUMBER

      ```
      public static final int ENERGY_WINDOW_OPTIMIZED_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Account.AccountResource.ENERGY_WINDOW_OPTIMIZED_FIELD_NUMBER)
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
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getEnergyUsage

      ```
      public long getEnergyUsage()
      ```

      ```
       energy resource, get from frozen
      ```

      `int64 energy_usage = 1;`

      Specified by:
      :   `getEnergyUsage` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The energyUsage.
    - #### hasFrozenBalanceForEnergy

      ```
      public boolean hasFrozenBalanceForEnergy()
      ```

      ```
       the frozen balance for energy
      ```

      `.protocol.Account.Frozen frozen_balance_for_energy = 2;`

      Specified by:
      :   `hasFrozenBalanceForEnergy` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   Whether the frozenBalanceForEnergy field is set.
    - #### getFrozenBalanceForEnergy

      ```
      public Response.Account.Frozen getFrozenBalanceForEnergy()
      ```

      ```
       the frozen balance for energy
      ```

      `.protocol.Account.Frozen frozen_balance_for_energy = 2;`

      Specified by:
      :   `getFrozenBalanceForEnergy` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The frozenBalanceForEnergy.
    - #### getFrozenBalanceForEnergyOrBuilder

      ```
      public Response.Account.FrozenOrBuilder getFrozenBalanceForEnergyOrBuilder()
      ```

      ```
       the frozen balance for energy
      ```

      `.protocol.Account.Frozen frozen_balance_for_energy = 2;`

      Specified by:
      :   `getFrozenBalanceForEnergyOrBuilder` in interface `Response.Account.AccountResourceOrBuilder`
    - #### getLatestConsumeTimeForEnergy

      ```
      public long getLatestConsumeTimeForEnergy()
      ```

      `int64 latest_consume_time_for_energy = 3;`

      Specified by:
      :   `getLatestConsumeTimeForEnergy` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The latestConsumeTimeForEnergy.
    - #### getAcquiredDelegatedFrozenBalanceForEnergy

      ```
      public long getAcquiredDelegatedFrozenBalanceForEnergy()
      ```

      ```
       Frozen balance provided by other accounts to this account
      ```

      `int64 acquired_delegated_frozen_balance_for_energy = 4;`

      Specified by:
      :   `getAcquiredDelegatedFrozenBalanceForEnergy` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The acquiredDelegatedFrozenBalanceForEnergy.
    - #### getDelegatedFrozenBalanceForEnergy

      ```
      public long getDelegatedFrozenBalanceForEnergy()
      ```

      ```
       Frozen balances provided to other accounts
      ```

      `int64 delegated_frozen_balance_for_energy = 5;`

      Specified by:
      :   `getDelegatedFrozenBalanceForEnergy` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The delegatedFrozenBalanceForEnergy.
    - #### getStorageLimit

      ```
      public long getStorageLimit()
      ```

      ```
       storage resource, get from market
      ```

      `int64 storage_limit = 6;`

      Specified by:
      :   `getStorageLimit` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The storageLimit.
    - #### getStorageUsage

      ```
      public long getStorageUsage()
      ```

      `int64 storage_usage = 7;`

      Specified by:
      :   `getStorageUsage` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The storageUsage.
    - #### getLatestExchangeStorageTime

      ```
      public long getLatestExchangeStorageTime()
      ```

      `int64 latest_exchange_storage_time = 8;`

      Specified by:
      :   `getLatestExchangeStorageTime` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The latestExchangeStorageTime.
    - #### getEnergyWindowSize

      ```
      public long getEnergyWindowSize()
      ```

      `int64 energy_window_size = 9;`

      Specified by:
      :   `getEnergyWindowSize` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The energyWindowSize.
    - #### getDelegatedFrozenV2BalanceForEnergy

      ```
      public long getDelegatedFrozenV2BalanceForEnergy()
      ```

      `int64 delegated_frozenV2_balance_for_energy = 10;`

      Specified by:
      :   `getDelegatedFrozenV2BalanceForEnergy` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The delegatedFrozenV2BalanceForEnergy.
    - #### getAcquiredDelegatedFrozenV2BalanceForEnergy

      ```
      public long getAcquiredDelegatedFrozenV2BalanceForEnergy()
      ```

      `int64 acquired_delegated_frozenV2_balance_for_energy = 11;`

      Specified by:
      :   `getAcquiredDelegatedFrozenV2BalanceForEnergy` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The acquiredDelegatedFrozenV2BalanceForEnergy.
    - #### getEnergyWindowOptimized

      ```
      public boolean getEnergyWindowOptimized()
      ```

      `bool energy_window_optimized = 12;`

      Specified by:
      :   `getEnergyWindowOptimized` in interface `Response.Account.AccountResourceOrBuilder`

      Returns:
      :   The energyWindowOptimized.
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
      public static Response.Account.AccountResource parseFrom(java.nio.ByteBuffer data)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Account.AccountResource parseFrom(java.nio.ByteBuffer data,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Account.AccountResource parseFrom(com.google.protobuf.ByteString data)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Account.AccountResource parseFrom(com.google.protobuf.ByteString data,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Account.AccountResource parseFrom(byte[] data)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Account.AccountResource parseFrom(byte[] data,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.Account.AccountResource parseFrom(java.io.InputStream input)
                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.Account.AccountResource parseFrom(java.io.InputStream input,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.Account.AccountResource parseDelimitedFrom(java.io.InputStream input)
                                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.Account.AccountResource parseDelimitedFrom(java.io.InputStream input,
                                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.Account.AccountResource parseFrom(com.google.protobuf.CodedInputStream input)
                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.Account.AccountResource parseFrom(com.google.protobuf.CodedInputStream input,
                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.Account.AccountResource.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.Account.AccountResource.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.Account.AccountResource.Builder newBuilder(Response.Account.AccountResource prototype)
      ```
    - #### toBuilder

      ```
      public Response.Account.AccountResource.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.Account.AccountResource.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.Account.AccountResource getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.Account.AccountResource> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.Account.AccountResource> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.Account.AccountResource getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`