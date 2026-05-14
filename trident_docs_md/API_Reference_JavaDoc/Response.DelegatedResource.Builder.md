

org.tron.trident.proto

## Class Response.DelegatedResource.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.DelegatedResource.Builder](../../../../org/tron/trident/proto/Response.DelegatedResource.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.DelegatedResource.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.DelegatedResourceOrBuilder](../../../../org/tron/trident/proto/Response.DelegatedResourceOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.DelegatedResource](../../../../org/tron/trident/proto/Response.DelegatedResource.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.DelegatedResource.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResource.Builder>
  implements Response.DelegatedResourceOrBuilder
  ```

  Protobuf type `protocol.DelegatedResource`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.DelegatedResource.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.DelegatedResource` | `build()` |
    | `Response.DelegatedResource` | `buildPartial()` |
    | `Response.DelegatedResource.Builder` | `clear()` |
    | `Response.DelegatedResource.Builder` | `clearExpireTimeForBandwidth()` `int64 expire_time_for_bandwidth = 5;` |
    | `Response.DelegatedResource.Builder` | `clearExpireTimeForEnergy()` `int64 expire_time_for_energy = 6;` |
    | `Response.DelegatedResource.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.DelegatedResource.Builder` | `clearFrom()` `bytes from = 1;` |
    | `Response.DelegatedResource.Builder` | `clearFrozenBalanceForBandwidth()` `int64 frozen_balance_for_bandwidth = 3;` |
    | `Response.DelegatedResource.Builder` | `clearFrozenBalanceForEnergy()` `int64 frozen_balance_for_energy = 4;` |
    | `Response.DelegatedResource.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.DelegatedResource.Builder` | `clearTo()` `bytes to = 2;` |
    | `Response.DelegatedResource.Builder` | `clone()` |
    | `Response.DelegatedResource` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getExpireTimeForBandwidth()` `int64 expire_time_for_bandwidth = 5;` |
    | `long` | `getExpireTimeForEnergy()` `int64 expire_time_for_energy = 6;` |
    | `com.google.protobuf.ByteString` | `getFrom()` `bytes from = 1;` |
    | `long` | `getFrozenBalanceForBandwidth()` `int64 frozen_balance_for_bandwidth = 3;` |
    | `long` | `getFrozenBalanceForEnergy()` `int64 frozen_balance_for_energy = 4;` |
    | `com.google.protobuf.ByteString` | `getTo()` `bytes to = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.DelegatedResource.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.DelegatedResource.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.DelegatedResource.Builder` | `mergeFrom(Response.DelegatedResource other)` |
    | `Response.DelegatedResource.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.DelegatedResource.Builder` | `setExpireTimeForBandwidth(long value)` `int64 expire_time_for_bandwidth = 5;` |
    | `Response.DelegatedResource.Builder` | `setExpireTimeForEnergy(long value)` `int64 expire_time_for_energy = 6;` |
    | `Response.DelegatedResource.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.DelegatedResource.Builder` | `setFrom(com.google.protobuf.ByteString value)` `bytes from = 1;` |
    | `Response.DelegatedResource.Builder` | `setFrozenBalanceForBandwidth(long value)` `int64 frozen_balance_for_bandwidth = 3;` |
    | `Response.DelegatedResource.Builder` | `setFrozenBalanceForEnergy(long value)` `int64 frozen_balance_for_energy = 4;` |
    | `Response.DelegatedResource.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.DelegatedResource.Builder` | `setTo(com.google.protobuf.ByteString value)` `bytes to = 2;` |
    | `Response.DelegatedResource.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

    - ### Methods inherited from class com.google.protobuf.GeneratedMessageV3.Builder

      `getAllFields, getField, getFieldBuilder, getOneofFieldDescriptor, getParentForChildren, getRepeatedField, getRepeatedFieldBuilder, getRepeatedFieldCount, getUnknownFields, getUnknownFieldSetBuilder, hasField, hasOneof, internalGetMapField, internalGetMapFieldReflection, internalGetMutableMapField, internalGetMutableMapFieldReflection, isClean, markClean, mergeUnknownLengthDelimitedField, mergeUnknownVarintField, newBuilderForField, onBuilt, onChanged, parseUnknownField, setUnknownFieldSetBuilder, setUnknownFieldsProto3`
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
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResource.Builder>`
    - #### clear

      ```
      public Response.DelegatedResource.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResource.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResource.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.DelegatedResource getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.DelegatedResource build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.DelegatedResource buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.DelegatedResource.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResource.Builder>`
    - #### setField

      ```
      public Response.DelegatedResource.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                         java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResource.Builder>`
    - #### clearField

      ```
      public Response.DelegatedResource.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResource.Builder>`
    - #### clearOneof

      ```
      public Response.DelegatedResource.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResource.Builder>`
    - #### setRepeatedField

      ```
      public Response.DelegatedResource.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                 int index,
                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResource.Builder>`
    - #### addRepeatedField

      ```
      public Response.DelegatedResource.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResource.Builder>`
    - #### mergeFrom

      ```
      public Response.DelegatedResource.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.DelegatedResource.Builder>`
    - #### mergeFrom

      ```
      public Response.DelegatedResource.Builder mergeFrom(Response.DelegatedResource other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResource.Builder>`
    - #### mergeFrom

      ```
      public Response.DelegatedResource.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.DelegatedResource.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getFrom

      ```
      public com.google.protobuf.ByteString getFrom()
      ```

      `bytes from = 1;`

      Specified by:
      :   `getFrom` in interface `Response.DelegatedResourceOrBuilder`

      Returns:
      :   The from.
    - #### setFrom

      ```
      public Response.DelegatedResource.Builder setFrom(com.google.protobuf.ByteString value)
      ```

      `bytes from = 1;`

      Parameters:
      :   `value` - The from to set.

      Returns:
      :   This builder for chaining.
    - #### clearFrom

      ```
      public Response.DelegatedResource.Builder clearFrom()
      ```

      `bytes from = 1;`

      Returns:
      :   This builder for chaining.
    - #### getTo

      ```
      public com.google.protobuf.ByteString getTo()
      ```

      `bytes to = 2;`

      Specified by:
      :   `getTo` in interface `Response.DelegatedResourceOrBuilder`

      Returns:
      :   The to.
    - #### setTo

      ```
      public Response.DelegatedResource.Builder setTo(com.google.protobuf.ByteString value)
      ```

      `bytes to = 2;`

      Parameters:
      :   `value` - The to to set.

      Returns:
      :   This builder for chaining.
    - #### clearTo

      ```
      public Response.DelegatedResource.Builder clearTo()
      ```

      `bytes to = 2;`

      Returns:
      :   This builder for chaining.
    - #### getFrozenBalanceForBandwidth

      ```
      public long getFrozenBalanceForBandwidth()
      ```

      `int64 frozen_balance_for_bandwidth = 3;`

      Specified by:
      :   `getFrozenBalanceForBandwidth` in interface `Response.DelegatedResourceOrBuilder`

      Returns:
      :   The frozenBalanceForBandwidth.
    - #### setFrozenBalanceForBandwidth

      ```
      public Response.DelegatedResource.Builder setFrozenBalanceForBandwidth(long value)
      ```

      `int64 frozen_balance_for_bandwidth = 3;`

      Parameters:
      :   `value` - The frozenBalanceForBandwidth to set.

      Returns:
      :   This builder for chaining.
    - #### clearFrozenBalanceForBandwidth

      ```
      public Response.DelegatedResource.Builder clearFrozenBalanceForBandwidth()
      ```

      `int64 frozen_balance_for_bandwidth = 3;`

      Returns:
      :   This builder for chaining.
    - #### getFrozenBalanceForEnergy

      ```
      public long getFrozenBalanceForEnergy()
      ```

      `int64 frozen_balance_for_energy = 4;`

      Specified by:
      :   `getFrozenBalanceForEnergy` in interface `Response.DelegatedResourceOrBuilder`

      Returns:
      :   The frozenBalanceForEnergy.
    - #### setFrozenBalanceForEnergy

      ```
      public Response.DelegatedResource.Builder setFrozenBalanceForEnergy(long value)
      ```

      `int64 frozen_balance_for_energy = 4;`

      Parameters:
      :   `value` - The frozenBalanceForEnergy to set.

      Returns:
      :   This builder for chaining.
    - #### clearFrozenBalanceForEnergy

      ```
      public Response.DelegatedResource.Builder clearFrozenBalanceForEnergy()
      ```

      `int64 frozen_balance_for_energy = 4;`

      Returns:
      :   This builder for chaining.
    - #### getExpireTimeForBandwidth

      ```
      public long getExpireTimeForBandwidth()
      ```

      `int64 expire_time_for_bandwidth = 5;`

      Specified by:
      :   `getExpireTimeForBandwidth` in interface `Response.DelegatedResourceOrBuilder`

      Returns:
      :   The expireTimeForBandwidth.
    - #### setExpireTimeForBandwidth

      ```
      public Response.DelegatedResource.Builder setExpireTimeForBandwidth(long value)
      ```

      `int64 expire_time_for_bandwidth = 5;`

      Parameters:
      :   `value` - The expireTimeForBandwidth to set.

      Returns:
      :   This builder for chaining.
    - #### clearExpireTimeForBandwidth

      ```
      public Response.DelegatedResource.Builder clearExpireTimeForBandwidth()
      ```

      `int64 expire_time_for_bandwidth = 5;`

      Returns:
      :   This builder for chaining.
    - #### getExpireTimeForEnergy

      ```
      public long getExpireTimeForEnergy()
      ```

      `int64 expire_time_for_energy = 6;`

      Specified by:
      :   `getExpireTimeForEnergy` in interface `Response.DelegatedResourceOrBuilder`

      Returns:
      :   The expireTimeForEnergy.
    - #### setExpireTimeForEnergy

      ```
      public Response.DelegatedResource.Builder setExpireTimeForEnergy(long value)
      ```

      `int64 expire_time_for_energy = 6;`

      Parameters:
      :   `value` - The expireTimeForEnergy to set.

      Returns:
      :   This builder for chaining.
    - #### clearExpireTimeForEnergy

      ```
      public Response.DelegatedResource.Builder clearExpireTimeForEnergy()
      ```

      `int64 expire_time_for_energy = 6;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.DelegatedResource.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResource.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.DelegatedResource.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResource.Builder>`