

org.tron.trident.api

## Class GrpcAPI.EasyTransferMessage.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.EasyTransferMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.EasyTransferMessage.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.EasyTransferMessage.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.EasyTransferMessageOrBuilder](../../../../org/tron/trident/api/GrpcAPI.EasyTransferMessageOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.EasyTransferMessage](../../../../org/tron/trident/api/GrpcAPI.EasyTransferMessage.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.EasyTransferMessage.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferMessage.Builder>
  implements GrpcAPI.EasyTransferMessageOrBuilder
  ```

  Protobuf type `protocol.EasyTransferMessage`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.EasyTransferMessage.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.EasyTransferMessage` | `build()` |
    | `GrpcAPI.EasyTransferMessage` | `buildPartial()` |
    | `GrpcAPI.EasyTransferMessage.Builder` | `clear()` |
    | `GrpcAPI.EasyTransferMessage.Builder` | `clearAmount()` `int64 amount = 3;` |
    | `GrpcAPI.EasyTransferMessage.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.EasyTransferMessage.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.EasyTransferMessage.Builder` | `clearPassPhrase()` `bytes passPhrase = 1;` |
    | `GrpcAPI.EasyTransferMessage.Builder` | `clearToAddress()` `bytes toAddress = 2;` |
    | `GrpcAPI.EasyTransferMessage.Builder` | `clone()` |
    | `long` | `getAmount()` `int64 amount = 3;` |
    | `GrpcAPI.EasyTransferMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getPassPhrase()` `bytes passPhrase = 1;` |
    | `com.google.protobuf.ByteString` | `getToAddress()` `bytes toAddress = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.EasyTransferMessage.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.EasyTransferMessage.Builder` | `mergeFrom(GrpcAPI.EasyTransferMessage other)` |
    | `GrpcAPI.EasyTransferMessage.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.EasyTransferMessage.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.EasyTransferMessage.Builder` | `setAmount(long value)` `int64 amount = 3;` |
    | `GrpcAPI.EasyTransferMessage.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.EasyTransferMessage.Builder` | `setPassPhrase(com.google.protobuf.ByteString value)` `bytes passPhrase = 1;` |
    | `GrpcAPI.EasyTransferMessage.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.EasyTransferMessage.Builder` | `setToAddress(com.google.protobuf.ByteString value)` `bytes toAddress = 2;` |
    | `GrpcAPI.EasyTransferMessage.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferMessage.Builder>`
    - #### clear

      ```
      public GrpcAPI.EasyTransferMessage.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferMessage.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferMessage.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.EasyTransferMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.EasyTransferMessage build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.EasyTransferMessage buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.EasyTransferMessage.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferMessage.Builder>`
    - #### setField

      ```
      public GrpcAPI.EasyTransferMessage.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                          java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferMessage.Builder>`
    - #### clearField

      ```
      public GrpcAPI.EasyTransferMessage.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferMessage.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.EasyTransferMessage.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferMessage.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.EasyTransferMessage.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                  int index,
                                                                  java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferMessage.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.EasyTransferMessage.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                  java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.EasyTransferMessage.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.EasyTransferMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.EasyTransferMessage.Builder mergeFrom(GrpcAPI.EasyTransferMessage other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.EasyTransferMessage.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.EasyTransferMessage.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getPassPhrase

      ```
      public com.google.protobuf.ByteString getPassPhrase()
      ```

      `bytes passPhrase = 1;`

      Specified by:
      :   `getPassPhrase` in interface `GrpcAPI.EasyTransferMessageOrBuilder`

      Returns:
      :   The passPhrase.
    - #### setPassPhrase

      ```
      public GrpcAPI.EasyTransferMessage.Builder setPassPhrase(com.google.protobuf.ByteString value)
      ```

      `bytes passPhrase = 1;`

      Parameters:
      :   `value` - The passPhrase to set.

      Returns:
      :   This builder for chaining.
    - #### clearPassPhrase

      ```
      public GrpcAPI.EasyTransferMessage.Builder clearPassPhrase()
      ```

      `bytes passPhrase = 1;`

      Returns:
      :   This builder for chaining.
    - #### getToAddress

      ```
      public com.google.protobuf.ByteString getToAddress()
      ```

      `bytes toAddress = 2;`

      Specified by:
      :   `getToAddress` in interface `GrpcAPI.EasyTransferMessageOrBuilder`

      Returns:
      :   The toAddress.
    - #### setToAddress

      ```
      public GrpcAPI.EasyTransferMessage.Builder setToAddress(com.google.protobuf.ByteString value)
      ```

      `bytes toAddress = 2;`

      Parameters:
      :   `value` - The toAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearToAddress

      ```
      public GrpcAPI.EasyTransferMessage.Builder clearToAddress()
      ```

      `bytes toAddress = 2;`

      Returns:
      :   This builder for chaining.
    - #### getAmount

      ```
      public long getAmount()
      ```

      `int64 amount = 3;`

      Specified by:
      :   `getAmount` in interface `GrpcAPI.EasyTransferMessageOrBuilder`

      Returns:
      :   The amount.
    - #### setAmount

      ```
      public GrpcAPI.EasyTransferMessage.Builder setAmount(long value)
      ```

      `int64 amount = 3;`

      Parameters:
      :   `value` - The amount to set.

      Returns:
      :   This builder for chaining.
    - #### clearAmount

      ```
      public GrpcAPI.EasyTransferMessage.Builder clearAmount()
      ```

      `int64 amount = 3;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.EasyTransferMessage.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferMessage.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.EasyTransferMessage.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferMessage.Builder>`