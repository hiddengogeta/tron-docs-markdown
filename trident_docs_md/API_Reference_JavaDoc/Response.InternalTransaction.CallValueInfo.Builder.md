

org.tron.trident.proto

## Class Response.InternalTransaction.CallValueInfo.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.InternalTransaction.CallValueInfo.Builder](../../../../org/tron/trident/proto/Response.InternalTransaction.CallValueInfo.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.InternalTransaction.CallValueInfo.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.InternalTransaction.CallValueInfoOrBuilder](../../../../org/tron/trident/proto/Response.InternalTransaction.CallValueInfoOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.InternalTransaction.CallValueInfo](../../../../org/tron/trident/proto/Response.InternalTransaction.CallValueInfo.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.InternalTransaction.CallValueInfo.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.CallValueInfo.Builder>
  implements Response.InternalTransaction.CallValueInfoOrBuilder
  ```

  Protobuf type `protocol.InternalTransaction.CallValueInfo`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.InternalTransaction.CallValueInfo.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.InternalTransaction.CallValueInfo` | `build()` |
    | `Response.InternalTransaction.CallValueInfo` | `buildPartial()` |
    | `Response.InternalTransaction.CallValueInfo.Builder` | `clear()` |
    | `Response.InternalTransaction.CallValueInfo.Builder` | `clearCallValue()` trx (TBD: or token) value |
    | `Response.InternalTransaction.CallValueInfo.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.InternalTransaction.CallValueInfo.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.InternalTransaction.CallValueInfo.Builder` | `clearTokenId()` TBD: tokenName, trx should be empty |
    | `Response.InternalTransaction.CallValueInfo.Builder` | `clone()` |
    | `long` | `getCallValue()` trx (TBD: or token) value |
    | `Response.InternalTransaction.CallValueInfo` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `java.lang.String` | `getTokenId()` TBD: tokenName, trx should be empty |
    | `com.google.protobuf.ByteString` | `getTokenIdBytes()` TBD: tokenName, trx should be empty |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.InternalTransaction.CallValueInfo.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.InternalTransaction.CallValueInfo.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.InternalTransaction.CallValueInfo.Builder` | `mergeFrom(Response.InternalTransaction.CallValueInfo other)` |
    | `Response.InternalTransaction.CallValueInfo.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.InternalTransaction.CallValueInfo.Builder` | `setCallValue(long value)` trx (TBD: or token) value |
    | `Response.InternalTransaction.CallValueInfo.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.InternalTransaction.CallValueInfo.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.InternalTransaction.CallValueInfo.Builder` | `setTokenId(java.lang.String value)` TBD: tokenName, trx should be empty |
    | `Response.InternalTransaction.CallValueInfo.Builder` | `setTokenIdBytes(com.google.protobuf.ByteString value)` TBD: tokenName, trx should be empty |
    | `Response.InternalTransaction.CallValueInfo.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.CallValueInfo.Builder>`
    - #### clear

      ```
      public Response.InternalTransaction.CallValueInfo.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.CallValueInfo.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.CallValueInfo.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.InternalTransaction.CallValueInfo getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.InternalTransaction.CallValueInfo build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.InternalTransaction.CallValueInfo buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.InternalTransaction.CallValueInfo.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.CallValueInfo.Builder>`
    - #### setField

      ```
      public Response.InternalTransaction.CallValueInfo.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                         java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.CallValueInfo.Builder>`
    - #### clearField

      ```
      public Response.InternalTransaction.CallValueInfo.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.CallValueInfo.Builder>`
    - #### clearOneof

      ```
      public Response.InternalTransaction.CallValueInfo.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.CallValueInfo.Builder>`
    - #### setRepeatedField

      ```
      public Response.InternalTransaction.CallValueInfo.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                 int index,
                                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.CallValueInfo.Builder>`
    - #### addRepeatedField

      ```
      public Response.InternalTransaction.CallValueInfo.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.CallValueInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.InternalTransaction.CallValueInfo.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.InternalTransaction.CallValueInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.InternalTransaction.CallValueInfo.Builder mergeFrom(Response.InternalTransaction.CallValueInfo other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.CallValueInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.InternalTransaction.CallValueInfo.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                   throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.InternalTransaction.CallValueInfo.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getCallValue

      ```
      public long getCallValue()
      ```

      ```
       trx (TBD: or token) value
      ```

      `int64 callValue = 1;`

      Specified by:
      :   `getCallValue` in interface `Response.InternalTransaction.CallValueInfoOrBuilder`

      Returns:
      :   The callValue.
    - #### setCallValue

      ```
      public Response.InternalTransaction.CallValueInfo.Builder setCallValue(long value)
      ```

      ```
       trx (TBD: or token) value
      ```

      `int64 callValue = 1;`

      Parameters:
      :   `value` - The callValue to set.

      Returns:
      :   This builder for chaining.
    - #### clearCallValue

      ```
      public Response.InternalTransaction.CallValueInfo.Builder clearCallValue()
      ```

      ```
       trx (TBD: or token) value
      ```

      `int64 callValue = 1;`

      Returns:
      :   This builder for chaining.
    - #### getTokenId

      ```
      public java.lang.String getTokenId()
      ```

      ```
       TBD: tokenName, trx should be empty
      ```

      `string tokenId = 2;`

      Specified by:
      :   `getTokenId` in interface `Response.InternalTransaction.CallValueInfoOrBuilder`

      Returns:
      :   The tokenId.
    - #### getTokenIdBytes

      ```
      public com.google.protobuf.ByteString getTokenIdBytes()
      ```

      ```
       TBD: tokenName, trx should be empty
      ```

      `string tokenId = 2;`

      Specified by:
      :   `getTokenIdBytes` in interface `Response.InternalTransaction.CallValueInfoOrBuilder`

      Returns:
      :   The bytes for tokenId.
    - #### setTokenId

      ```
      public Response.InternalTransaction.CallValueInfo.Builder setTokenId(java.lang.String value)
      ```

      ```
       TBD: tokenName, trx should be empty
      ```

      `string tokenId = 2;`

      Parameters:
      :   `value` - The tokenId to set.

      Returns:
      :   This builder for chaining.
    - #### clearTokenId

      ```
      public Response.InternalTransaction.CallValueInfo.Builder clearTokenId()
      ```

      ```
       TBD: tokenName, trx should be empty
      ```

      `string tokenId = 2;`

      Returns:
      :   This builder for chaining.
    - #### setTokenIdBytes

      ```
      public Response.InternalTransaction.CallValueInfo.Builder setTokenIdBytes(com.google.protobuf.ByteString value)
      ```

      ```
       TBD: tokenName, trx should be empty
      ```

      `string tokenId = 2;`

      Parameters:
      :   `value` - The bytes for tokenId to set.

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.InternalTransaction.CallValueInfo.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.CallValueInfo.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.InternalTransaction.CallValueInfo.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.CallValueInfo.Builder>`