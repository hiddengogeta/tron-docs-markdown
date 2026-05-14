

org.tron.trident.api

## Class GrpcAPI.PaymentAddressMessage.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.PaymentAddressMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.PaymentAddressMessage.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.PaymentAddressMessage.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.PaymentAddressMessageOrBuilder](../../../../org/tron/trident/api/GrpcAPI.PaymentAddressMessageOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.PaymentAddressMessage](../../../../org/tron/trident/api/GrpcAPI.PaymentAddressMessage.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.PaymentAddressMessage.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaymentAddressMessage.Builder>
  implements GrpcAPI.PaymentAddressMessageOrBuilder
  ```

  Protobuf type `protocol.PaymentAddressMessage`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.PaymentAddressMessage.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.PaymentAddressMessage` | `build()` |
    | `GrpcAPI.PaymentAddressMessage` | `buildPartial()` |
    | `GrpcAPI.PaymentAddressMessage.Builder` | `clear()` |
    | `GrpcAPI.PaymentAddressMessage.Builder` | `clearD()` `.protocol.DiversifierMessage d = 1;` |
    | `GrpcAPI.PaymentAddressMessage.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.PaymentAddressMessage.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.PaymentAddressMessage.Builder` | `clearPaymentAddress()` `string payment_address = 3;` |
    | `GrpcAPI.PaymentAddressMessage.Builder` | `clearPkD()` `bytes pkD = 2;` |
    | `GrpcAPI.PaymentAddressMessage.Builder` | `clone()` |
    | `GrpcAPI.DiversifierMessage` | `getD()` `.protocol.DiversifierMessage d = 1;` |
    | `GrpcAPI.DiversifierMessage.Builder` | `getDBuilder()` `.protocol.DiversifierMessage d = 1;` |
    | `GrpcAPI.PaymentAddressMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `GrpcAPI.DiversifierMessageOrBuilder` | `getDOrBuilder()` `.protocol.DiversifierMessage d = 1;` |
    | `java.lang.String` | `getPaymentAddress()` `string payment_address = 3;` |
    | `com.google.protobuf.ByteString` | `getPaymentAddressBytes()` `string payment_address = 3;` |
    | `com.google.protobuf.ByteString` | `getPkD()` `bytes pkD = 2;` |
    | `boolean` | `hasD()` `.protocol.DiversifierMessage d = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.PaymentAddressMessage.Builder` | `mergeD(GrpcAPI.DiversifierMessage value)` `.protocol.DiversifierMessage d = 1;` |
    | `GrpcAPI.PaymentAddressMessage.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.PaymentAddressMessage.Builder` | `mergeFrom(GrpcAPI.PaymentAddressMessage other)` |
    | `GrpcAPI.PaymentAddressMessage.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.PaymentAddressMessage.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.PaymentAddressMessage.Builder` | `setD(GrpcAPI.DiversifierMessage.Builder builderForValue)` `.protocol.DiversifierMessage d = 1;` |
    | `GrpcAPI.PaymentAddressMessage.Builder` | `setD(GrpcAPI.DiversifierMessage value)` `.protocol.DiversifierMessage d = 1;` |
    | `GrpcAPI.PaymentAddressMessage.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.PaymentAddressMessage.Builder` | `setPaymentAddress(java.lang.String value)` `string payment_address = 3;` |
    | `GrpcAPI.PaymentAddressMessage.Builder` | `setPaymentAddressBytes(com.google.protobuf.ByteString value)` `string payment_address = 3;` |
    | `GrpcAPI.PaymentAddressMessage.Builder` | `setPkD(com.google.protobuf.ByteString value)` `bytes pkD = 2;` |
    | `GrpcAPI.PaymentAddressMessage.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.PaymentAddressMessage.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaymentAddressMessage.Builder>`
    - #### clear

      ```
      public GrpcAPI.PaymentAddressMessage.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaymentAddressMessage.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaymentAddressMessage.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.PaymentAddressMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.PaymentAddressMessage build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.PaymentAddressMessage buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.PaymentAddressMessage.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaymentAddressMessage.Builder>`
    - #### setField

      ```
      public GrpcAPI.PaymentAddressMessage.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                            java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaymentAddressMessage.Builder>`
    - #### clearField

      ```
      public GrpcAPI.PaymentAddressMessage.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaymentAddressMessage.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.PaymentAddressMessage.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaymentAddressMessage.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.PaymentAddressMessage.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                    int index,
                                                                    java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaymentAddressMessage.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.PaymentAddressMessage.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                    java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaymentAddressMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.PaymentAddressMessage.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.PaymentAddressMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.PaymentAddressMessage.Builder mergeFrom(GrpcAPI.PaymentAddressMessage other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaymentAddressMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.PaymentAddressMessage.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                             com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                      throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.PaymentAddressMessage.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### hasD

      ```
      public boolean hasD()
      ```

      `.protocol.DiversifierMessage d = 1;`

      Specified by:
      :   `hasD` in interface `GrpcAPI.PaymentAddressMessageOrBuilder`

      Returns:
      :   Whether the d field is set.
    - #### getD

      ```
      public GrpcAPI.DiversifierMessage getD()
      ```

      `.protocol.DiversifierMessage d = 1;`

      Specified by:
      :   `getD` in interface `GrpcAPI.PaymentAddressMessageOrBuilder`

      Returns:
      :   The d.
    - #### setD

      ```
      public GrpcAPI.PaymentAddressMessage.Builder setD(GrpcAPI.DiversifierMessage value)
      ```

      `.protocol.DiversifierMessage d = 1;`
    - #### setD

      ```
      public GrpcAPI.PaymentAddressMessage.Builder setD(GrpcAPI.DiversifierMessage.Builder builderForValue)
      ```

      `.protocol.DiversifierMessage d = 1;`
    - #### mergeD

      ```
      public GrpcAPI.PaymentAddressMessage.Builder mergeD(GrpcAPI.DiversifierMessage value)
      ```

      `.protocol.DiversifierMessage d = 1;`
    - #### clearD

      ```
      public GrpcAPI.PaymentAddressMessage.Builder clearD()
      ```

      `.protocol.DiversifierMessage d = 1;`
    - #### getDBuilder

      ```
      public GrpcAPI.DiversifierMessage.Builder getDBuilder()
      ```

      `.protocol.DiversifierMessage d = 1;`
    - #### getDOrBuilder

      ```
      public GrpcAPI.DiversifierMessageOrBuilder getDOrBuilder()
      ```

      `.protocol.DiversifierMessage d = 1;`

      Specified by:
      :   `getDOrBuilder` in interface `GrpcAPI.PaymentAddressMessageOrBuilder`
    - #### getPkD

      ```
      public com.google.protobuf.ByteString getPkD()
      ```

      `bytes pkD = 2;`

      Specified by:
      :   `getPkD` in interface `GrpcAPI.PaymentAddressMessageOrBuilder`

      Returns:
      :   The pkD.
    - #### setPkD

      ```
      public GrpcAPI.PaymentAddressMessage.Builder setPkD(com.google.protobuf.ByteString value)
      ```

      `bytes pkD = 2;`

      Parameters:
      :   `value` - The pkD to set.

      Returns:
      :   This builder for chaining.
    - #### clearPkD

      ```
      public GrpcAPI.PaymentAddressMessage.Builder clearPkD()
      ```

      `bytes pkD = 2;`

      Returns:
      :   This builder for chaining.
    - #### getPaymentAddress

      ```
      public java.lang.String getPaymentAddress()
      ```

      `string payment_address = 3;`

      Specified by:
      :   `getPaymentAddress` in interface `GrpcAPI.PaymentAddressMessageOrBuilder`

      Returns:
      :   The paymentAddress.
    - #### getPaymentAddressBytes

      ```
      public com.google.protobuf.ByteString getPaymentAddressBytes()
      ```

      `string payment_address = 3;`

      Specified by:
      :   `getPaymentAddressBytes` in interface `GrpcAPI.PaymentAddressMessageOrBuilder`

      Returns:
      :   The bytes for paymentAddress.
    - #### setPaymentAddress

      ```
      public GrpcAPI.PaymentAddressMessage.Builder setPaymentAddress(java.lang.String value)
      ```

      `string payment_address = 3;`

      Parameters:
      :   `value` - The paymentAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearPaymentAddress

      ```
      public GrpcAPI.PaymentAddressMessage.Builder clearPaymentAddress()
      ```

      `string payment_address = 3;`

      Returns:
      :   This builder for chaining.
    - #### setPaymentAddressBytes

      ```
      public GrpcAPI.PaymentAddressMessage.Builder setPaymentAddressBytes(com.google.protobuf.ByteString value)
      ```

      `string payment_address = 3;`

      Parameters:
      :   `value` - The bytes for paymentAddress to set.

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.PaymentAddressMessage.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaymentAddressMessage.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.PaymentAddressMessage.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PaymentAddressMessage.Builder>`