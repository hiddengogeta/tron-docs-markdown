

org.tron.trident.proto

## Class Common.Note.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Common.Note.Builder](../../../../org/tron/trident/proto/Common.Note.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Common.Note.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Common.NoteOrBuilder](../../../../org/tron/trident/proto/Common.NoteOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Common.Note](../../../../org/tron/trident/proto/Common.Note.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Common.Note.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Common.Note.Builder>
  implements Common.NoteOrBuilder
  ```

  Protobuf type `protocol.Note`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Common.Note.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Common.Note` | `build()` |
    | `Common.Note` | `buildPartial()` |
    | `Common.Note.Builder` | `clear()` |
    | `Common.Note.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Common.Note.Builder` | `clearMemo()` `bytes memo = 4;` |
    | `Common.Note.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Common.Note.Builder` | `clearPaymentAddress()` `string payment_address = 2;` |
    | `Common.Note.Builder` | `clearRcm()` random 32 |
    | `Common.Note.Builder` | `clearValue()` `int64 value = 1;` |
    | `Common.Note.Builder` | `clone()` |
    | `Common.Note` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getMemo()` `bytes memo = 4;` |
    | `java.lang.String` | `getPaymentAddress()` `string payment_address = 2;` |
    | `com.google.protobuf.ByteString` | `getPaymentAddressBytes()` `string payment_address = 2;` |
    | `com.google.protobuf.ByteString` | `getRcm()` random 32 |
    | `long` | `getValue()` `int64 value = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Common.Note.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Common.Note.Builder` | `mergeFrom(Common.Note other)` |
    | `Common.Note.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Common.Note.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Common.Note.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Common.Note.Builder` | `setMemo(com.google.protobuf.ByteString value)` `bytes memo = 4;` |
    | `Common.Note.Builder` | `setPaymentAddress(java.lang.String value)` `string payment_address = 2;` |
    | `Common.Note.Builder` | `setPaymentAddressBytes(com.google.protobuf.ByteString value)` `string payment_address = 2;` |
    | `Common.Note.Builder` | `setRcm(com.google.protobuf.ByteString value)` random 32 |
    | `Common.Note.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Common.Note.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Common.Note.Builder` | `setValue(long value)` `int64 value = 1;` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Note.Builder>`
    - #### clear

      ```
      public Common.Note.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Note.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Note.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Common.Note getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Common.Note build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Common.Note buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Common.Note.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Note.Builder>`
    - #### setField

      ```
      public Common.Note.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                          java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Note.Builder>`
    - #### clearField

      ```
      public Common.Note.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Note.Builder>`
    - #### clearOneof

      ```
      public Common.Note.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Note.Builder>`
    - #### setRepeatedField

      ```
      public Common.Note.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                  int index,
                                                  java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Note.Builder>`
    - #### addRepeatedField

      ```
      public Common.Note.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                  java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Note.Builder>`
    - #### mergeFrom

      ```
      public Common.Note.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Common.Note.Builder>`
    - #### mergeFrom

      ```
      public Common.Note.Builder mergeFrom(Common.Note other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Note.Builder>`
    - #### mergeFrom

      ```
      public Common.Note.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                    throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Common.Note.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getValue

      ```
      public long getValue()
      ```

      `int64 value = 1;`

      Specified by:
      :   `getValue` in interface `Common.NoteOrBuilder`

      Returns:
      :   The value.
    - #### setValue

      ```
      public Common.Note.Builder setValue(long value)
      ```

      `int64 value = 1;`

      Parameters:
      :   `value` - The value to set.

      Returns:
      :   This builder for chaining.
    - #### clearValue

      ```
      public Common.Note.Builder clearValue()
      ```

      `int64 value = 1;`

      Returns:
      :   This builder for chaining.
    - #### getPaymentAddress

      ```
      public java.lang.String getPaymentAddress()
      ```

      `string payment_address = 2;`

      Specified by:
      :   `getPaymentAddress` in interface `Common.NoteOrBuilder`

      Returns:
      :   The paymentAddress.
    - #### getPaymentAddressBytes

      ```
      public com.google.protobuf.ByteString getPaymentAddressBytes()
      ```

      `string payment_address = 2;`

      Specified by:
      :   `getPaymentAddressBytes` in interface `Common.NoteOrBuilder`

      Returns:
      :   The bytes for paymentAddress.
    - #### setPaymentAddress

      ```
      public Common.Note.Builder setPaymentAddress(java.lang.String value)
      ```

      `string payment_address = 2;`

      Parameters:
      :   `value` - The paymentAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearPaymentAddress

      ```
      public Common.Note.Builder clearPaymentAddress()
      ```

      `string payment_address = 2;`

      Returns:
      :   This builder for chaining.
    - #### setPaymentAddressBytes

      ```
      public Common.Note.Builder setPaymentAddressBytes(com.google.protobuf.ByteString value)
      ```

      `string payment_address = 2;`

      Parameters:
      :   `value` - The bytes for paymentAddress to set.

      Returns:
      :   This builder for chaining.
    - #### getRcm

      ```
      public com.google.protobuf.ByteString getRcm()
      ```

      ```
       random 32
      ```

      `bytes rcm = 3;`

      Specified by:
      :   `getRcm` in interface `Common.NoteOrBuilder`

      Returns:
      :   The rcm.
    - #### setRcm

      ```
      public Common.Note.Builder setRcm(com.google.protobuf.ByteString value)
      ```

      ```
       random 32
      ```

      `bytes rcm = 3;`

      Parameters:
      :   `value` - The rcm to set.

      Returns:
      :   This builder for chaining.
    - #### clearRcm

      ```
      public Common.Note.Builder clearRcm()
      ```

      ```
       random 32
      ```

      `bytes rcm = 3;`

      Returns:
      :   This builder for chaining.
    - #### getMemo

      ```
      public com.google.protobuf.ByteString getMemo()
      ```

      `bytes memo = 4;`

      Specified by:
      :   `getMemo` in interface `Common.NoteOrBuilder`

      Returns:
      :   The memo.
    - #### setMemo

      ```
      public Common.Note.Builder setMemo(com.google.protobuf.ByteString value)
      ```

      `bytes memo = 4;`

      Parameters:
      :   `value` - The memo to set.

      Returns:
      :   This builder for chaining.
    - #### clearMemo

      ```
      public Common.Note.Builder clearMemo()
      ```

      `bytes memo = 4;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Common.Note.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Note.Builder>`
    - #### mergeUnknownFields

      ```
      public final Common.Note.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Note.Builder>`