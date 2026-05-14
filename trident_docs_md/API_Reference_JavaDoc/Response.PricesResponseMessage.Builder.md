

org.tron.trident.proto

## Class Response.PricesResponseMessage.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.PricesResponseMessage.Builder](../../../../org/tron/trident/proto/Response.PricesResponseMessage.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.PricesResponseMessage.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.PricesResponseMessageOrBuilder](../../../../org/tron/trident/proto/Response.PricesResponseMessageOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.PricesResponseMessage](../../../../org/tron/trident/proto/Response.PricesResponseMessage.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.PricesResponseMessage.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.PricesResponseMessage.Builder>
  implements Response.PricesResponseMessageOrBuilder
  ```

  Protobuf type `protocol.PricesResponseMessage`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.PricesResponseMessage.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.PricesResponseMessage` | `build()` |
    | `Response.PricesResponseMessage` | `buildPartial()` |
    | `Response.PricesResponseMessage.Builder` | `clear()` |
    | `Response.PricesResponseMessage.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.PricesResponseMessage.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.PricesResponseMessage.Builder` | `clearPrices()` `string prices = 1;` |
    | `Response.PricesResponseMessage.Builder` | `clone()` |
    | `Response.PricesResponseMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `java.lang.String` | `getPrices()` `string prices = 1;` |
    | `com.google.protobuf.ByteString` | `getPricesBytes()` `string prices = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.PricesResponseMessage.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.PricesResponseMessage.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.PricesResponseMessage.Builder` | `mergeFrom(Response.PricesResponseMessage other)` |
    | `Response.PricesResponseMessage.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.PricesResponseMessage.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.PricesResponseMessage.Builder` | `setPrices(java.lang.String value)` `string prices = 1;` |
    | `Response.PricesResponseMessage.Builder` | `setPricesBytes(com.google.protobuf.ByteString value)` `string prices = 1;` |
    | `Response.PricesResponseMessage.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.PricesResponseMessage.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.PricesResponseMessage.Builder>`
    - #### clear

      ```
      public Response.PricesResponseMessage.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.PricesResponseMessage.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.PricesResponseMessage.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.PricesResponseMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.PricesResponseMessage build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.PricesResponseMessage buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.PricesResponseMessage.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.PricesResponseMessage.Builder>`
    - #### setField

      ```
      public Response.PricesResponseMessage.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                             java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.PricesResponseMessage.Builder>`
    - #### clearField

      ```
      public Response.PricesResponseMessage.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.PricesResponseMessage.Builder>`
    - #### clearOneof

      ```
      public Response.PricesResponseMessage.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.PricesResponseMessage.Builder>`
    - #### setRepeatedField

      ```
      public Response.PricesResponseMessage.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     int index,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.PricesResponseMessage.Builder>`
    - #### addRepeatedField

      ```
      public Response.PricesResponseMessage.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.PricesResponseMessage.Builder>`
    - #### mergeFrom

      ```
      public Response.PricesResponseMessage.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.PricesResponseMessage.Builder>`
    - #### mergeFrom

      ```
      public Response.PricesResponseMessage.Builder mergeFrom(Response.PricesResponseMessage other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.PricesResponseMessage.Builder>`
    - #### mergeFrom

      ```
      public Response.PricesResponseMessage.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.PricesResponseMessage.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getPrices

      ```
      public java.lang.String getPrices()
      ```

      `string prices = 1;`

      Specified by:
      :   `getPrices` in interface `Response.PricesResponseMessageOrBuilder`

      Returns:
      :   The prices.
    - #### getPricesBytes

      ```
      public com.google.protobuf.ByteString getPricesBytes()
      ```

      `string prices = 1;`

      Specified by:
      :   `getPricesBytes` in interface `Response.PricesResponseMessageOrBuilder`

      Returns:
      :   The bytes for prices.
    - #### setPrices

      ```
      public Response.PricesResponseMessage.Builder setPrices(java.lang.String value)
      ```

      `string prices = 1;`

      Parameters:
      :   `value` - The prices to set.

      Returns:
      :   This builder for chaining.
    - #### clearPrices

      ```
      public Response.PricesResponseMessage.Builder clearPrices()
      ```

      `string prices = 1;`

      Returns:
      :   This builder for chaining.
    - #### setPricesBytes

      ```
      public Response.PricesResponseMessage.Builder setPricesBytes(com.google.protobuf.ByteString value)
      ```

      `string prices = 1;`

      Parameters:
      :   `value` - The bytes for prices to set.

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.PricesResponseMessage.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.PricesResponseMessage.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.PricesResponseMessage.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.PricesResponseMessage.Builder>`