

org.tron.trident.api

## Class GrpcAPI.EasyTransferAssetByPrivateMessage.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.EasyTransferAssetByPrivateMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.EasyTransferAssetByPrivateMessage.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.EasyTransferAssetByPrivateMessage.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.EasyTransferAssetByPrivateMessageOrBuilder](../../../../org/tron/trident/api/GrpcAPI.EasyTransferAssetByPrivateMessageOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.EasyTransferAssetByPrivateMessage](../../../../org/tron/trident/api/GrpcAPI.EasyTransferAssetByPrivateMessage.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.EasyTransferAssetByPrivateMessage.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferAssetByPrivateMessage.Builder>
  implements GrpcAPI.EasyTransferAssetByPrivateMessageOrBuilder
  ```

  Protobuf type `protocol.EasyTransferAssetByPrivateMessage`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage` | `build()` |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage` | `buildPartial()` |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage.Builder` | `clear()` |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage.Builder` | `clearAmount()` `int64 amount = 4;` |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage.Builder` | `clearAssetId()` `string assetId = 3;` |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage.Builder` | `clearPrivateKey()` `bytes privateKey = 1;` |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage.Builder` | `clearToAddress()` `bytes toAddress = 2;` |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage.Builder` | `clone()` |
    | `long` | `getAmount()` `int64 amount = 4;` |
    | `java.lang.String` | `getAssetId()` `string assetId = 3;` |
    | `com.google.protobuf.ByteString` | `getAssetIdBytes()` `string assetId = 3;` |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getPrivateKey()` `bytes privateKey = 1;` |
    | `com.google.protobuf.ByteString` | `getToAddress()` `bytes toAddress = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage.Builder` | `mergeFrom(GrpcAPI.EasyTransferAssetByPrivateMessage other)` |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage.Builder` | `setAmount(long value)` `int64 amount = 4;` |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage.Builder` | `setAssetId(java.lang.String value)` `string assetId = 3;` |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage.Builder` | `setAssetIdBytes(com.google.protobuf.ByteString value)` `string assetId = 3;` |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage.Builder` | `setPrivateKey(com.google.protobuf.ByteString value)` `bytes privateKey = 1;` |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage.Builder` | `setToAddress(com.google.protobuf.ByteString value)` `bytes toAddress = 2;` |
    | `GrpcAPI.EasyTransferAssetByPrivateMessage.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferAssetByPrivateMessage.Builder>`
    - #### clear

      ```
      public GrpcAPI.EasyTransferAssetByPrivateMessage.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferAssetByPrivateMessage.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferAssetByPrivateMessage.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.EasyTransferAssetByPrivateMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.EasyTransferAssetByPrivateMessage build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.EasyTransferAssetByPrivateMessage buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.EasyTransferAssetByPrivateMessage.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferAssetByPrivateMessage.Builder>`
    - #### setField

      ```
      public GrpcAPI.EasyTransferAssetByPrivateMessage.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                        java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferAssetByPrivateMessage.Builder>`
    - #### clearField

      ```
      public GrpcAPI.EasyTransferAssetByPrivateMessage.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferAssetByPrivateMessage.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.EasyTransferAssetByPrivateMessage.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferAssetByPrivateMessage.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.EasyTransferAssetByPrivateMessage.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                int index,
                                                                                java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferAssetByPrivateMessage.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.EasyTransferAssetByPrivateMessage.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferAssetByPrivateMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.EasyTransferAssetByPrivateMessage.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.EasyTransferAssetByPrivateMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.EasyTransferAssetByPrivateMessage.Builder mergeFrom(GrpcAPI.EasyTransferAssetByPrivateMessage other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferAssetByPrivateMessage.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.EasyTransferAssetByPrivateMessage.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                  throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.EasyTransferAssetByPrivateMessage.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getPrivateKey

      ```
      public com.google.protobuf.ByteString getPrivateKey()
      ```

      `bytes privateKey = 1;`

      Specified by:
      :   `getPrivateKey` in interface `GrpcAPI.EasyTransferAssetByPrivateMessageOrBuilder`

      Returns:
      :   The privateKey.
    - #### setPrivateKey

      ```
      public GrpcAPI.EasyTransferAssetByPrivateMessage.Builder setPrivateKey(com.google.protobuf.ByteString value)
      ```

      `bytes privateKey = 1;`

      Parameters:
      :   `value` - The privateKey to set.

      Returns:
      :   This builder for chaining.
    - #### clearPrivateKey

      ```
      public GrpcAPI.EasyTransferAssetByPrivateMessage.Builder clearPrivateKey()
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
      :   `getToAddress` in interface `GrpcAPI.EasyTransferAssetByPrivateMessageOrBuilder`

      Returns:
      :   The toAddress.
    - #### setToAddress

      ```
      public GrpcAPI.EasyTransferAssetByPrivateMessage.Builder setToAddress(com.google.protobuf.ByteString value)
      ```

      `bytes toAddress = 2;`

      Parameters:
      :   `value` - The toAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearToAddress

      ```
      public GrpcAPI.EasyTransferAssetByPrivateMessage.Builder clearToAddress()
      ```

      `bytes toAddress = 2;`

      Returns:
      :   This builder for chaining.
    - #### getAssetId

      ```
      public java.lang.String getAssetId()
      ```

      `string assetId = 3;`

      Specified by:
      :   `getAssetId` in interface `GrpcAPI.EasyTransferAssetByPrivateMessageOrBuilder`

      Returns:
      :   The assetId.
    - #### getAssetIdBytes

      ```
      public com.google.protobuf.ByteString getAssetIdBytes()
      ```

      `string assetId = 3;`

      Specified by:
      :   `getAssetIdBytes` in interface `GrpcAPI.EasyTransferAssetByPrivateMessageOrBuilder`

      Returns:
      :   The bytes for assetId.
    - #### setAssetId

      ```
      public GrpcAPI.EasyTransferAssetByPrivateMessage.Builder setAssetId(java.lang.String value)
      ```

      `string assetId = 3;`

      Parameters:
      :   `value` - The assetId to set.

      Returns:
      :   This builder for chaining.
    - #### clearAssetId

      ```
      public GrpcAPI.EasyTransferAssetByPrivateMessage.Builder clearAssetId()
      ```

      `string assetId = 3;`

      Returns:
      :   This builder for chaining.
    - #### setAssetIdBytes

      ```
      public GrpcAPI.EasyTransferAssetByPrivateMessage.Builder setAssetIdBytes(com.google.protobuf.ByteString value)
      ```

      `string assetId = 3;`

      Parameters:
      :   `value` - The bytes for assetId to set.

      Returns:
      :   This builder for chaining.
    - #### getAmount

      ```
      public long getAmount()
      ```

      `int64 amount = 4;`

      Specified by:
      :   `getAmount` in interface `GrpcAPI.EasyTransferAssetByPrivateMessageOrBuilder`

      Returns:
      :   The amount.
    - #### setAmount

      ```
      public GrpcAPI.EasyTransferAssetByPrivateMessage.Builder setAmount(long value)
      ```

      `int64 amount = 4;`

      Parameters:
      :   `value` - The amount to set.

      Returns:
      :   This builder for chaining.
    - #### clearAmount

      ```
      public GrpcAPI.EasyTransferAssetByPrivateMessage.Builder clearAmount()
      ```

      `int64 amount = 4;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.EasyTransferAssetByPrivateMessage.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferAssetByPrivateMessage.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.EasyTransferAssetByPrivateMessage.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.EasyTransferAssetByPrivateMessage.Builder>`