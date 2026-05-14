

org.tron.trident.api

## Class GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.CanWithdrawUnfreezeAmountRequestMessageOrBuilder](../../../../org/tron/trident/api/GrpcAPI.CanWithdrawUnfreezeAmountRequestMessageOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage](../../../../org/tron/trident/api/GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder>
  implements GrpcAPI.CanWithdrawUnfreezeAmountRequestMessageOrBuilder
  ```

  ```
   Stake 2.0
  ```

  Protobuf type `protocol.CanWithdrawUnfreezeAmountRequestMessage`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage` | `build()` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage` | `buildPartial()` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder` | `clear()` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder` | `clearTimestamp()` `int64 timestamp = 2;` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder` | `clone()` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `long` | `getTimestamp()` `int64 timestamp = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder` | `mergeFrom(GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage other)` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder` | `setTimestamp(long value)` `int64 timestamp = 2;` |
    | `GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder>`
    - #### clear

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder>`
    - #### setField

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                              java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder>`
    - #### clearField

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                      int index,
                                                                                      java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                      java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder mergeFrom(GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                        throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `GrpcAPI.CanWithdrawUnfreezeAmountRequestMessageOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getTimestamp

      ```
      public long getTimestamp()
      ```

      `int64 timestamp = 2;`

      Specified by:
      :   `getTimestamp` in interface `GrpcAPI.CanWithdrawUnfreezeAmountRequestMessageOrBuilder`

      Returns:
      :   The timestamp.
    - #### setTimestamp

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder setTimestamp(long value)
      ```

      `int64 timestamp = 2;`

      Parameters:
      :   `value` - The timestamp to set.

      Returns:
      :   This builder for chaining.
    - #### clearTimestamp

      ```
      public GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder clearTimestamp()
      ```

      `int64 timestamp = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.CanWithdrawUnfreezeAmountRequestMessage.Builder>`