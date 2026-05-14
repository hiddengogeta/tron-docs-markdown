

org.tron.trident.proto

## Class Response.ResourceReceipt.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.ResourceReceipt.Builder](../../../../org/tron/trident/proto/Response.ResourceReceipt.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.ResourceReceipt.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.ResourceReceiptOrBuilder](../../../../org/tron/trident/proto/Response.ResourceReceiptOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.ResourceReceipt](../../../../org/tron/trident/proto/Response.ResourceReceipt.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.ResourceReceipt.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.ResourceReceipt.Builder>
  implements Response.ResourceReceiptOrBuilder
  ```

  Protobuf type `protocol.ResourceReceipt`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.ResourceReceipt.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.ResourceReceipt` | `build()` |
    | `Response.ResourceReceipt` | `buildPartial()` |
    | `Response.ResourceReceipt.Builder` | `clear()` |
    | `Response.ResourceReceipt.Builder` | `clearEnergyFee()` `int64 energy_fee = 2;` |
    | `Response.ResourceReceipt.Builder` | `clearEnergyPenaltyTotal()` `int64 energy_penalty_total = 8;` |
    | `Response.ResourceReceipt.Builder` | `clearEnergyUsage()` `int64 energy_usage = 1;` |
    | `Response.ResourceReceipt.Builder` | `clearEnergyUsageTotal()` `int64 energy_usage_total = 4;` |
    | `Response.ResourceReceipt.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.ResourceReceipt.Builder` | `clearNetFee()` `int64 net_fee = 6;` |
    | `Response.ResourceReceipt.Builder` | `clearNetUsage()` `int64 net_usage = 5;` |
    | `Response.ResourceReceipt.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.ResourceReceipt.Builder` | `clearOriginEnergyUsage()` `int64 origin_energy_usage = 3;` |
    | `Response.ResourceReceipt.Builder` | `clearResult()` `.protocol.Transaction.Result.contractResult result = 7;` |
    | `Response.ResourceReceipt.Builder` | `clone()` |
    | `Response.ResourceReceipt` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getEnergyFee()` `int64 energy_fee = 2;` |
    | `long` | `getEnergyPenaltyTotal()` `int64 energy_penalty_total = 8;` |
    | `long` | `getEnergyUsage()` `int64 energy_usage = 1;` |
    | `long` | `getEnergyUsageTotal()` `int64 energy_usage_total = 4;` |
    | `long` | `getNetFee()` `int64 net_fee = 6;` |
    | `long` | `getNetUsage()` `int64 net_usage = 5;` |
    | `long` | `getOriginEnergyUsage()` `int64 origin_energy_usage = 3;` |
    | `Chain.Transaction.Result.contractResult` | `getResult()` `.protocol.Transaction.Result.contractResult result = 7;` |
    | `int` | `getResultValue()` `.protocol.Transaction.Result.contractResult result = 7;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.ResourceReceipt.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.ResourceReceipt.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.ResourceReceipt.Builder` | `mergeFrom(Response.ResourceReceipt other)` |
    | `Response.ResourceReceipt.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.ResourceReceipt.Builder` | `setEnergyFee(long value)` `int64 energy_fee = 2;` |
    | `Response.ResourceReceipt.Builder` | `setEnergyPenaltyTotal(long value)` `int64 energy_penalty_total = 8;` |
    | `Response.ResourceReceipt.Builder` | `setEnergyUsage(long value)` `int64 energy_usage = 1;` |
    | `Response.ResourceReceipt.Builder` | `setEnergyUsageTotal(long value)` `int64 energy_usage_total = 4;` |
    | `Response.ResourceReceipt.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.ResourceReceipt.Builder` | `setNetFee(long value)` `int64 net_fee = 6;` |
    | `Response.ResourceReceipt.Builder` | `setNetUsage(long value)` `int64 net_usage = 5;` |
    | `Response.ResourceReceipt.Builder` | `setOriginEnergyUsage(long value)` `int64 origin_energy_usage = 3;` |
    | `Response.ResourceReceipt.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.ResourceReceipt.Builder` | `setResult(Chain.Transaction.Result.contractResult value)` `.protocol.Transaction.Result.contractResult result = 7;` |
    | `Response.ResourceReceipt.Builder` | `setResultValue(int value)` `.protocol.Transaction.Result.contractResult result = 7;` |
    | `Response.ResourceReceipt.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ResourceReceipt.Builder>`
    - #### clear

      ```
      public Response.ResourceReceipt.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ResourceReceipt.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ResourceReceipt.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.ResourceReceipt getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.ResourceReceipt build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.ResourceReceipt buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.ResourceReceipt.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ResourceReceipt.Builder>`
    - #### setField

      ```
      public Response.ResourceReceipt.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ResourceReceipt.Builder>`
    - #### clearField

      ```
      public Response.ResourceReceipt.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ResourceReceipt.Builder>`
    - #### clearOneof

      ```
      public Response.ResourceReceipt.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ResourceReceipt.Builder>`
    - #### setRepeatedField

      ```
      public Response.ResourceReceipt.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               int index,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ResourceReceipt.Builder>`
    - #### addRepeatedField

      ```
      public Response.ResourceReceipt.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ResourceReceipt.Builder>`
    - #### mergeFrom

      ```
      public Response.ResourceReceipt.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.ResourceReceipt.Builder>`
    - #### mergeFrom

      ```
      public Response.ResourceReceipt.Builder mergeFrom(Response.ResourceReceipt other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ResourceReceipt.Builder>`
    - #### mergeFrom

      ```
      public Response.ResourceReceipt.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                 throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.ResourceReceipt.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getEnergyUsage

      ```
      public long getEnergyUsage()
      ```

      `int64 energy_usage = 1;`

      Specified by:
      :   `getEnergyUsage` in interface `Response.ResourceReceiptOrBuilder`

      Returns:
      :   The energyUsage.
    - #### setEnergyUsage

      ```
      public Response.ResourceReceipt.Builder setEnergyUsage(long value)
      ```

      `int64 energy_usage = 1;`

      Parameters:
      :   `value` - The energyUsage to set.

      Returns:
      :   This builder for chaining.
    - #### clearEnergyUsage

      ```
      public Response.ResourceReceipt.Builder clearEnergyUsage()
      ```

      `int64 energy_usage = 1;`

      Returns:
      :   This builder for chaining.
    - #### getEnergyFee

      ```
      public long getEnergyFee()
      ```

      `int64 energy_fee = 2;`

      Specified by:
      :   `getEnergyFee` in interface `Response.ResourceReceiptOrBuilder`

      Returns:
      :   The energyFee.
    - #### setEnergyFee

      ```
      public Response.ResourceReceipt.Builder setEnergyFee(long value)
      ```

      `int64 energy_fee = 2;`

      Parameters:
      :   `value` - The energyFee to set.

      Returns:
      :   This builder for chaining.
    - #### clearEnergyFee

      ```
      public Response.ResourceReceipt.Builder clearEnergyFee()
      ```

      `int64 energy_fee = 2;`

      Returns:
      :   This builder for chaining.
    - #### getOriginEnergyUsage

      ```
      public long getOriginEnergyUsage()
      ```

      `int64 origin_energy_usage = 3;`

      Specified by:
      :   `getOriginEnergyUsage` in interface `Response.ResourceReceiptOrBuilder`

      Returns:
      :   The originEnergyUsage.
    - #### setOriginEnergyUsage

      ```
      public Response.ResourceReceipt.Builder setOriginEnergyUsage(long value)
      ```

      `int64 origin_energy_usage = 3;`

      Parameters:
      :   `value` - The originEnergyUsage to set.

      Returns:
      :   This builder for chaining.
    - #### clearOriginEnergyUsage

      ```
      public Response.ResourceReceipt.Builder clearOriginEnergyUsage()
      ```

      `int64 origin_energy_usage = 3;`

      Returns:
      :   This builder for chaining.
    - #### getEnergyUsageTotal

      ```
      public long getEnergyUsageTotal()
      ```

      `int64 energy_usage_total = 4;`

      Specified by:
      :   `getEnergyUsageTotal` in interface `Response.ResourceReceiptOrBuilder`

      Returns:
      :   The energyUsageTotal.
    - #### setEnergyUsageTotal

      ```
      public Response.ResourceReceipt.Builder setEnergyUsageTotal(long value)
      ```

      `int64 energy_usage_total = 4;`

      Parameters:
      :   `value` - The energyUsageTotal to set.

      Returns:
      :   This builder for chaining.
    - #### clearEnergyUsageTotal

      ```
      public Response.ResourceReceipt.Builder clearEnergyUsageTotal()
      ```

      `int64 energy_usage_total = 4;`

      Returns:
      :   This builder for chaining.
    - #### getNetUsage

      ```
      public long getNetUsage()
      ```

      `int64 net_usage = 5;`

      Specified by:
      :   `getNetUsage` in interface `Response.ResourceReceiptOrBuilder`

      Returns:
      :   The netUsage.
    - #### setNetUsage

      ```
      public Response.ResourceReceipt.Builder setNetUsage(long value)
      ```

      `int64 net_usage = 5;`

      Parameters:
      :   `value` - The netUsage to set.

      Returns:
      :   This builder for chaining.
    - #### clearNetUsage

      ```
      public Response.ResourceReceipt.Builder clearNetUsage()
      ```

      `int64 net_usage = 5;`

      Returns:
      :   This builder for chaining.
    - #### getNetFee

      ```
      public long getNetFee()
      ```

      `int64 net_fee = 6;`

      Specified by:
      :   `getNetFee` in interface `Response.ResourceReceiptOrBuilder`

      Returns:
      :   The netFee.
    - #### setNetFee

      ```
      public Response.ResourceReceipt.Builder setNetFee(long value)
      ```

      `int64 net_fee = 6;`

      Parameters:
      :   `value` - The netFee to set.

      Returns:
      :   This builder for chaining.
    - #### clearNetFee

      ```
      public Response.ResourceReceipt.Builder clearNetFee()
      ```

      `int64 net_fee = 6;`

      Returns:
      :   This builder for chaining.
    - #### getResultValue

      ```
      public int getResultValue()
      ```

      `.protocol.Transaction.Result.contractResult result = 7;`

      Specified by:
      :   `getResultValue` in interface `Response.ResourceReceiptOrBuilder`

      Returns:
      :   The enum numeric value on the wire for result.
    - #### setResultValue

      ```
      public Response.ResourceReceipt.Builder setResultValue(int value)
      ```

      `.protocol.Transaction.Result.contractResult result = 7;`

      Parameters:
      :   `value` - The enum numeric value on the wire for result to set.

      Returns:
      :   This builder for chaining.
    - #### getResult

      ```
      public Chain.Transaction.Result.contractResult getResult()
      ```

      `.protocol.Transaction.Result.contractResult result = 7;`

      Specified by:
      :   `getResult` in interface `Response.ResourceReceiptOrBuilder`

      Returns:
      :   The result.
    - #### setResult

      ```
      public Response.ResourceReceipt.Builder setResult(Chain.Transaction.Result.contractResult value)
      ```

      `.protocol.Transaction.Result.contractResult result = 7;`

      Parameters:
      :   `value` - The result to set.

      Returns:
      :   This builder for chaining.
    - #### clearResult

      ```
      public Response.ResourceReceipt.Builder clearResult()
      ```

      `.protocol.Transaction.Result.contractResult result = 7;`

      Returns:
      :   This builder for chaining.
    - #### getEnergyPenaltyTotal

      ```
      public long getEnergyPenaltyTotal()
      ```

      `int64 energy_penalty_total = 8;`

      Specified by:
      :   `getEnergyPenaltyTotal` in interface `Response.ResourceReceiptOrBuilder`

      Returns:
      :   The energyPenaltyTotal.
    - #### setEnergyPenaltyTotal

      ```
      public Response.ResourceReceipt.Builder setEnergyPenaltyTotal(long value)
      ```

      `int64 energy_penalty_total = 8;`

      Parameters:
      :   `value` - The energyPenaltyTotal to set.

      Returns:
      :   This builder for chaining.
    - #### clearEnergyPenaltyTotal

      ```
      public Response.ResourceReceipt.Builder clearEnergyPenaltyTotal()
      ```

      `int64 energy_penalty_total = 8;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.ResourceReceipt.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ResourceReceipt.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.ResourceReceipt.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ResourceReceipt.Builder>`