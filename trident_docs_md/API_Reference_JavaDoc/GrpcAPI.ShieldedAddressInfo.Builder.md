

org.tron.trident.api

## Class GrpcAPI.ShieldedAddressInfo.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.ShieldedAddressInfo.Builder](../../../../org/tron/trident/api/GrpcAPI.ShieldedAddressInfo.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.ShieldedAddressInfo.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.ShieldedAddressInfoOrBuilder](../../../../org/tron/trident/api/GrpcAPI.ShieldedAddressInfoOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.ShieldedAddressInfo](../../../../org/tron/trident/api/GrpcAPI.ShieldedAddressInfo.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.ShieldedAddressInfo.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedAddressInfo.Builder>
  implements GrpcAPI.ShieldedAddressInfoOrBuilder
  ```

  Protobuf type `protocol.ShieldedAddressInfo`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.ShieldedAddressInfo` | `build()` |
    | `GrpcAPI.ShieldedAddressInfo` | `buildPartial()` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `clear()` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `clearAk()` `bytes ak = 5;` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `clearAsk()` `bytes ask = 2;` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `clearD()` `bytes d = 8;` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `clearIvk()` `bytes ivk = 7;` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `clearNk()` `bytes nk = 6;` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `clearNsk()` `bytes nsk = 3;` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `clearOvk()` `bytes ovk = 4;` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `clearPaymentAddress()` `string payment_address = 10;` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `clearPkD()` `bytes pkD = 9;` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `clearSk()` `bytes sk = 1;` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getAk()` `bytes ak = 5;` |
    | `com.google.protobuf.ByteString` | `getAsk()` `bytes ask = 2;` |
    | `com.google.protobuf.ByteString` | `getD()` `bytes d = 8;` |
    | `GrpcAPI.ShieldedAddressInfo` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getIvk()` `bytes ivk = 7;` |
    | `com.google.protobuf.ByteString` | `getNk()` `bytes nk = 6;` |
    | `com.google.protobuf.ByteString` | `getNsk()` `bytes nsk = 3;` |
    | `com.google.protobuf.ByteString` | `getOvk()` `bytes ovk = 4;` |
    | `java.lang.String` | `getPaymentAddress()` `string payment_address = 10;` |
    | `com.google.protobuf.ByteString` | `getPaymentAddressBytes()` `string payment_address = 10;` |
    | `com.google.protobuf.ByteString` | `getPkD()` `bytes pkD = 9;` |
    | `com.google.protobuf.ByteString` | `getSk()` `bytes sk = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `mergeFrom(GrpcAPI.ShieldedAddressInfo other)` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `setAk(com.google.protobuf.ByteString value)` `bytes ak = 5;` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `setAsk(com.google.protobuf.ByteString value)` `bytes ask = 2;` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `setD(com.google.protobuf.ByteString value)` `bytes d = 8;` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `setIvk(com.google.protobuf.ByteString value)` `bytes ivk = 7;` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `setNk(com.google.protobuf.ByteString value)` `bytes nk = 6;` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `setNsk(com.google.protobuf.ByteString value)` `bytes nsk = 3;` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `setOvk(com.google.protobuf.ByteString value)` `bytes ovk = 4;` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `setPaymentAddress(java.lang.String value)` `string payment_address = 10;` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `setPaymentAddressBytes(com.google.protobuf.ByteString value)` `string payment_address = 10;` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `setPkD(com.google.protobuf.ByteString value)` `bytes pkD = 9;` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `setSk(com.google.protobuf.ByteString value)` `bytes sk = 1;` |
    | `GrpcAPI.ShieldedAddressInfo.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedAddressInfo.Builder>`
    - #### clear

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedAddressInfo.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedAddressInfo.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.ShieldedAddressInfo getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.ShieldedAddressInfo build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.ShieldedAddressInfo buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedAddressInfo.Builder>`
    - #### setField

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                          java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedAddressInfo.Builder>`
    - #### clearField

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedAddressInfo.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedAddressInfo.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                  int index,
                                                                  java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedAddressInfo.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                  java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedAddressInfo.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.ShieldedAddressInfo.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder mergeFrom(GrpcAPI.ShieldedAddressInfo other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedAddressInfo.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.ShieldedAddressInfo.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getSk

      ```
      public com.google.protobuf.ByteString getSk()
      ```

      `bytes sk = 1;`

      Specified by:
      :   `getSk` in interface `GrpcAPI.ShieldedAddressInfoOrBuilder`

      Returns:
      :   The sk.
    - #### setSk

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder setSk(com.google.protobuf.ByteString value)
      ```

      `bytes sk = 1;`

      Parameters:
      :   `value` - The sk to set.

      Returns:
      :   This builder for chaining.
    - #### clearSk

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder clearSk()
      ```

      `bytes sk = 1;`

      Returns:
      :   This builder for chaining.
    - #### getAsk

      ```
      public com.google.protobuf.ByteString getAsk()
      ```

      `bytes ask = 2;`

      Specified by:
      :   `getAsk` in interface `GrpcAPI.ShieldedAddressInfoOrBuilder`

      Returns:
      :   The ask.
    - #### setAsk

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder setAsk(com.google.protobuf.ByteString value)
      ```

      `bytes ask = 2;`

      Parameters:
      :   `value` - The ask to set.

      Returns:
      :   This builder for chaining.
    - #### clearAsk

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder clearAsk()
      ```

      `bytes ask = 2;`

      Returns:
      :   This builder for chaining.
    - #### getNsk

      ```
      public com.google.protobuf.ByteString getNsk()
      ```

      `bytes nsk = 3;`

      Specified by:
      :   `getNsk` in interface `GrpcAPI.ShieldedAddressInfoOrBuilder`

      Returns:
      :   The nsk.
    - #### setNsk

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder setNsk(com.google.protobuf.ByteString value)
      ```

      `bytes nsk = 3;`

      Parameters:
      :   `value` - The nsk to set.

      Returns:
      :   This builder for chaining.
    - #### clearNsk

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder clearNsk()
      ```

      `bytes nsk = 3;`

      Returns:
      :   This builder for chaining.
    - #### getOvk

      ```
      public com.google.protobuf.ByteString getOvk()
      ```

      `bytes ovk = 4;`

      Specified by:
      :   `getOvk` in interface `GrpcAPI.ShieldedAddressInfoOrBuilder`

      Returns:
      :   The ovk.
    - #### setOvk

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder setOvk(com.google.protobuf.ByteString value)
      ```

      `bytes ovk = 4;`

      Parameters:
      :   `value` - The ovk to set.

      Returns:
      :   This builder for chaining.
    - #### clearOvk

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder clearOvk()
      ```

      `bytes ovk = 4;`

      Returns:
      :   This builder for chaining.
    - #### getAk

      ```
      public com.google.protobuf.ByteString getAk()
      ```

      `bytes ak = 5;`

      Specified by:
      :   `getAk` in interface `GrpcAPI.ShieldedAddressInfoOrBuilder`

      Returns:
      :   The ak.
    - #### setAk

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder setAk(com.google.protobuf.ByteString value)
      ```

      `bytes ak = 5;`

      Parameters:
      :   `value` - The ak to set.

      Returns:
      :   This builder for chaining.
    - #### clearAk

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder clearAk()
      ```

      `bytes ak = 5;`

      Returns:
      :   This builder for chaining.
    - #### getNk

      ```
      public com.google.protobuf.ByteString getNk()
      ```

      `bytes nk = 6;`

      Specified by:
      :   `getNk` in interface `GrpcAPI.ShieldedAddressInfoOrBuilder`

      Returns:
      :   The nk.
    - #### setNk

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder setNk(com.google.protobuf.ByteString value)
      ```

      `bytes nk = 6;`

      Parameters:
      :   `value` - The nk to set.

      Returns:
      :   This builder for chaining.
    - #### clearNk

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder clearNk()
      ```

      `bytes nk = 6;`

      Returns:
      :   This builder for chaining.
    - #### getIvk

      ```
      public com.google.protobuf.ByteString getIvk()
      ```

      `bytes ivk = 7;`

      Specified by:
      :   `getIvk` in interface `GrpcAPI.ShieldedAddressInfoOrBuilder`

      Returns:
      :   The ivk.
    - #### setIvk

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder setIvk(com.google.protobuf.ByteString value)
      ```

      `bytes ivk = 7;`

      Parameters:
      :   `value` - The ivk to set.

      Returns:
      :   This builder for chaining.
    - #### clearIvk

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder clearIvk()
      ```

      `bytes ivk = 7;`

      Returns:
      :   This builder for chaining.
    - #### getD

      ```
      public com.google.protobuf.ByteString getD()
      ```

      `bytes d = 8;`

      Specified by:
      :   `getD` in interface `GrpcAPI.ShieldedAddressInfoOrBuilder`

      Returns:
      :   The d.
    - #### setD

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder setD(com.google.protobuf.ByteString value)
      ```

      `bytes d = 8;`

      Parameters:
      :   `value` - The d to set.

      Returns:
      :   This builder for chaining.
    - #### clearD

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder clearD()
      ```

      `bytes d = 8;`

      Returns:
      :   This builder for chaining.
    - #### getPkD

      ```
      public com.google.protobuf.ByteString getPkD()
      ```

      `bytes pkD = 9;`

      Specified by:
      :   `getPkD` in interface `GrpcAPI.ShieldedAddressInfoOrBuilder`

      Returns:
      :   The pkD.
    - #### setPkD

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder setPkD(com.google.protobuf.ByteString value)
      ```

      `bytes pkD = 9;`

      Parameters:
      :   `value` - The pkD to set.

      Returns:
      :   This builder for chaining.
    - #### clearPkD

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder clearPkD()
      ```

      `bytes pkD = 9;`

      Returns:
      :   This builder for chaining.
    - #### getPaymentAddress

      ```
      public java.lang.String getPaymentAddress()
      ```

      `string payment_address = 10;`

      Specified by:
      :   `getPaymentAddress` in interface `GrpcAPI.ShieldedAddressInfoOrBuilder`

      Returns:
      :   The paymentAddress.
    - #### getPaymentAddressBytes

      ```
      public com.google.protobuf.ByteString getPaymentAddressBytes()
      ```

      `string payment_address = 10;`

      Specified by:
      :   `getPaymentAddressBytes` in interface `GrpcAPI.ShieldedAddressInfoOrBuilder`

      Returns:
      :   The bytes for paymentAddress.
    - #### setPaymentAddress

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder setPaymentAddress(java.lang.String value)
      ```

      `string payment_address = 10;`

      Parameters:
      :   `value` - The paymentAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearPaymentAddress

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder clearPaymentAddress()
      ```

      `string payment_address = 10;`

      Returns:
      :   This builder for chaining.
    - #### setPaymentAddressBytes

      ```
      public GrpcAPI.ShieldedAddressInfo.Builder setPaymentAddressBytes(com.google.protobuf.ByteString value)
      ```

      `string payment_address = 10;`

      Parameters:
      :   `value` - The bytes for paymentAddress to set.

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.ShieldedAddressInfo.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedAddressInfo.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.ShieldedAddressInfo.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedAddressInfo.Builder>`