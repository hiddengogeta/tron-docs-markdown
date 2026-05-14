

org.tron.trident.api

## Class GrpcAPI.EasyTransferByPrivateMessage.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.EasyTransferByPrivateMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.EasyTransferByPrivateMessage.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.EasyTransferByPrivateMessage.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.EasyTransferByPrivateMessageOrBuilder](../../../../org/tron/trident/api/GrpcAPI.EasyTransferByPrivateMessageOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.EasyTransferByPrivateMessage](../../../../org/tron/trident/api/GrpcAPI.EasyTransferByPrivateMessage.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.EasyTransferByPrivateMessage.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferByPrivateMessage.Builder>
  implements GrpcAPI.EasyTransferByPrivateMessageOrBuilder
  ```

  Protobuf type `protocol.EasyTransferByPrivateMessage`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.EasyTransferByPrivateMessage.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.EasyTransferByPrivateMessage` | `build()` |
    | `GrpcAPI.EasyTransferByPrivateMessage` | `buildPartial()` |
    | `GrpcAPI.EasyTransferByPrivateMessage.Builder` | `clear()` |
    | `GrpcAPI.EasyTransferByPrivateMessage.Builder` | `clearAmount()` `int64 amount = 3;` |
    | `GrpcAPI.EasyTransferByPrivateMessage.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.EasyTransferByPrivateMessage.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.EasyTransferByPrivateMessage.Builder` | `clearPrivateKey()` `bytes privateKey = 1;` |
    | `GrpcAPI.EasyTransferByPrivateMessage.Builder` | `clearToAddress()` `bytes toAddress = 2;` |
    | `GrpcAPI.EasyTransferByPrivateMessage.Builder` | `clone()` |
    | `long` | `getAmount()` `int64 amount = 3;` |
    | `GrpcAPI.EasyTransferByPrivateMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getPrivateKey()` `bytes privateKey = 1;` |
    | `com.google.protobuf.ByteString` | `getToAddress()` `bytes toAddress = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.EasyTransferByPrivateMessage.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.EasyTransferByPrivateMessage.Builder` | `mergeFrom(GrpcAPI.EasyTransferByPrivateMessage other)` |
    | `GrpcAPI.EasyTransferByPrivateMessage.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.EasyTransferByPrivateMessage.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.EasyTransferByPrivateMessage.Builder` | `setAmount(long value)` `int64 amount = 3;` |
    | `GrpcAPI.EasyTransferByPrivateMessage.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.EasyTransferByPrivateMessage.Builder` | `setPrivateKey(com.google.protobuf.ByteString value)` `bytes privateKey = 1;` |
    | `GrpcAPI.EasyTransferByPrivateMessage.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.EasyTransferByPrivateMessage.Builder` | `setToAddress(com.google.protobuf.ByteString value)` `bytes toAddress = 2;` |
    | `GrpcAPI.EasyTransferByPrivateMessage.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferByPrivateMessage.Builder>`
    - #### clear

      ```
      public GrpcAPI.EasyTransferByPrivateMessage.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferByPrivateMessage.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferByPrivateMessage.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.EasyTransferByPrivateMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.EasyTransferByPrivateMessage build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.EasyTransferByPrivateMessage buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.EasyTransferByPrivateMessage.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferByPrivateMessage.Builder>`
    - #### setField

      ```
      public GrpcAPI.EasyTransferByPrivateMessage.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                   java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferByPrivateMessage.Builder>`
    - #### clearField

      ```
      public GrpcAPI.EasyTransferByPrivateMessage.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferByPrivateMessage.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.EasyTransferByPrivateMessage.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferByPrivateMessage.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.EasyTransferByPrivateMessage.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                           int index,
                                                                           java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferByPrivateMessage.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.EasyTransferByPrivateMessage.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                           java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferByPrivateMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.EasyTransferByPrivateMessage.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.EasyTransferByPrivateMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.EasyTransferByPrivateMessage.Builder mergeFrom(GrpcAPI.EasyTransferByPrivateMessage other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferByPrivateMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.EasyTransferByPrivateMessage.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                    com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                             throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.EasyTransferByPrivateMessage.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getPrivateKey

      ```
      public com.google.protobuf.ByteString getPrivateKey()
      ```

      `bytes privateKey = 1;`

      Specified by:
      :   `getPrivateKey` in interface `GrpcAPI.EasyTransferByPrivateMessageOrBuilder`

      Returns:
      :   The privateKey.
    - #### setPrivateKey

      ```
      public GrpcAPI.EasyTransferByPrivateMessage.Builder setPrivateKey(com.google.protobuf.ByteString value)
      ```

      `bytes privateKey = 1;`

      Parameters:
      :   `value` - The privateKey to set.

      Returns:
      :   This builder for chaining.
    - #### clearPrivateKey

      ```
      public GrpcAPI.EasyTransferByPrivateMessage.Builder clearPrivateKey()
      ```

      `bytes privateKey = 1;`

      Returns:
      :   This builder for chaining.
    - #### getToAddress

      ```
      public com.google.protobuf.ByteString getToAddress()
      ```

      `bytes toAddress = 2;`

      Specified by:
      :   `getToAddress` in interface `GrpcAPI.EasyTransferByPrivateMessageOrBuilder`

      Returns:
      :   The toAddress.
    - #### setToAddress

      ```
      public GrpcAPI.EasyTransferByPrivateMessage.Builder setToAddress(com.google.protobuf.ByteString value)
      ```

      `bytes toAddress = 2;`

      Parameters:
      :   `value` - The toAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearToAddress

      ```
      public GrpcAPI.EasyTransferByPrivateMessage.Builder clearToAddress()
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
      :   `getAmount` in interface `GrpcAPI.EasyTransferByPrivateMessageOrBuilder`

      Returns:
      :   The amount.
    - #### setAmount

      ```
      public GrpcAPI.EasyTransferByPrivateMessage.Builder setAmount(long value)
      ```

      `int64 amount = 3;`

      Parameters:
      :   `value` - The amount to set.

      Returns:
      :   This builder for chaining.
    - #### clearAmount

      ```
      public GrpcAPI.EasyTransferByPrivateMessage.Builder clearAmount()
      ```

      `int64 amount = 3;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.EasyTransferByPrivateMessage.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferByPrivateMessage.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.EasyTransferByPrivateMessage.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferByPrivateMessage.Builder>`