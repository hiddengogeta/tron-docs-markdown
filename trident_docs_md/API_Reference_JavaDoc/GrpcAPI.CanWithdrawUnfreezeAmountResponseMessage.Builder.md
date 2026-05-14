

org.tron.trident.api

## Class GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.CanWithdrawUnfreezeAmountResponseMessageOrBuilder](../../../../org/tron/trident/api/GrpcAPI.CanWithdrawUnfreezeAmountResponseMessageOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage](../../../../org/tron/trident/api/GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder>
  implements GrpcAPI.CanWithdrawUnfreezeAmountResponseMessageOrBuilder
  ```

  Protobuf type `protocol.CanWithdrawUnfreezeAmountResponseMessage`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage` | `build()` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage` | `buildPartial()` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder` | `clear()` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder` | `clearAmount()` `int64 amount = 1;` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder` | `clone()` |
    | `long` | `getAmount()` `int64 amount = 1;` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder` | `mergeFrom(GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage other)` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder` | `setAmount(long value)` `int64 amount = 1;` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder>`
    - #### clear

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder>`
    - #### setField

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder>`
    - #### clearField

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                       int index,
                                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder mergeFrom(GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                         throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getAmount

      ```
      public long getAmount()
      ```

      `int64 amount = 1;`

      Specified by:
      :   `getAmount` in interface `GrpcAPI.CanWithdrawUnfreezeAmountResponseMessageOrBuilder`

      Returns:
      :   The amount.
    - #### setAmount

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder setAmount(long value)
      ```

      `int64 amount = 1;`

      Parameters:
      :   `value` - The amount to set.

      Returns:
      :   This builder for chaining.
    - #### clearAmount

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder clearAmount()
      ```

      `int64 amount = 1;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountResponseMessage.Builder>`