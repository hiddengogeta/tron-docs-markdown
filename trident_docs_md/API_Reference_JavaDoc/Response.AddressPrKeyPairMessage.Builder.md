

org.tron.trident.proto

## Class Response.AddressPrKeyPairMessage.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.AddressPrKeyPairMessage.Builder](../../../../org/tron/trident/proto/Response.AddressPrKeyPairMessage.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.AddressPrKeyPairMessage.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.AddressPrKeyPairMessageOrBuilder](../../../../org/tron/trident/proto/Response.AddressPrKeyPairMessageOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.AddressPrKeyPairMessage](../../../../org/tron/trident/proto/Response.AddressPrKeyPairMessage.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.AddressPrKeyPairMessage.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.AddressPrKeyPairMessage.Builder>
  implements Response.AddressPrKeyPairMessageOrBuilder
  ```

  Protobuf type `protocol.AddressPrKeyPairMessage`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.AddressPrKeyPairMessage.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.AddressPrKeyPairMessage` | `build()` |
    | `Response.AddressPrKeyPairMessage` | `buildPartial()` |
    | `Response.AddressPrKeyPairMessage.Builder` | `clear()` |
    | `Response.AddressPrKeyPairMessage.Builder` | `clearAddress()` `string address = 1;` |
    | `Response.AddressPrKeyPairMessage.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.AddressPrKeyPairMessage.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.AddressPrKeyPairMessage.Builder` | `clearPrivateKey()` `string privateKey = 2;` |
    | `Response.AddressPrKeyPairMessage.Builder` | `clone()` |
    | `java.lang.String` | `getAddress()` `string address = 1;` |
    | `com.google.protobuf.ByteString` | `getAddressBytes()` `string address = 1;` |
    | `Response.AddressPrKeyPairMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `java.lang.String` | `getPrivateKey()` `string privateKey = 2;` |
    | `com.google.protobuf.ByteString` | `getPrivateKeyBytes()` `string privateKey = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.AddressPrKeyPairMessage.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.AddressPrKeyPairMessage.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.AddressPrKeyPairMessage.Builder` | `mergeFrom(Response.AddressPrKeyPairMessage other)` |
    | `Response.AddressPrKeyPairMessage.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.AddressPrKeyPairMessage.Builder` | `setAddress(java.lang.String value)` `string address = 1;` |
    | `Response.AddressPrKeyPairMessage.Builder` | `setAddressBytes(com.google.protobuf.ByteString value)` `string address = 1;` |
    | `Response.AddressPrKeyPairMessage.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.AddressPrKeyPairMessage.Builder` | `setPrivateKey(java.lang.String value)` `string privateKey = 2;` |
    | `Response.AddressPrKeyPairMessage.Builder` | `setPrivateKeyBytes(com.google.protobuf.ByteString value)` `string privateKey = 2;` |
    | `Response.AddressPrKeyPairMessage.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.AddressPrKeyPairMessage.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AddressPrKeyPairMessage.Builder>`
    - #### clear

      ```
      public Response.AddressPrKeyPairMessage.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AddressPrKeyPairMessage.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AddressPrKeyPairMessage.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.AddressPrKeyPairMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.AddressPrKeyPairMessage build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.AddressPrKeyPairMessage buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.AddressPrKeyPairMessage.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AddressPrKeyPairMessage.Builder>`
    - #### setField

      ```
      public Response.AddressPrKeyPairMessage.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AddressPrKeyPairMessage.Builder>`
    - #### clearField

      ```
      public Response.AddressPrKeyPairMessage.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AddressPrKeyPairMessage.Builder>`
    - #### clearOneof

      ```
      public Response.AddressPrKeyPairMessage.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AddressPrKeyPairMessage.Builder>`
    - #### setRepeatedField

      ```
      public Response.AddressPrKeyPairMessage.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                       int index,
                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AddressPrKeyPairMessage.Builder>`
    - #### addRepeatedField

      ```
      public Response.AddressPrKeyPairMessage.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AddressPrKeyPairMessage.Builder>`
    - #### mergeFrom

      ```
      public Response.AddressPrKeyPairMessage.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.AddressPrKeyPairMessage.Builder>`
    - #### mergeFrom

      ```
      public Response.AddressPrKeyPairMessage.Builder mergeFrom(Response.AddressPrKeyPairMessage other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AddressPrKeyPairMessage.Builder>`
    - #### mergeFrom

      ```
      public Response.AddressPrKeyPairMessage.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                         throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.AddressPrKeyPairMessage.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getAddress

      ```
      public java.lang.String getAddress()
      ```

      `string address = 1;`

      Specified by:
      :   `getAddress` in interface `Response.AddressPrKeyPairMessageOrBuilder`

      Returns:
      :   The address.
    - #### getAddressBytes

      ```
      public com.google.protobuf.ByteString getAddressBytes()
      ```

      `string address = 1;`

      Specified by:
      :   `getAddressBytes` in interface `Response.AddressPrKeyPairMessageOrBuilder`

      Returns:
      :   The bytes for address.
    - #### setAddress

      ```
      public Response.AddressPrKeyPairMessage.Builder setAddress(java.lang.String value)
      ```

      `string address = 1;`

      Parameters:
      :   `value` - The address to set.

      Returns:
      :   This builder for chaining.
    - #### clearAddress

      ```
      public Response.AddressPrKeyPairMessage.Builder clearAddress()
      ```

      `string address = 1;`

      Returns:
      :   This builder for chaining.
    - #### setAddressBytes

      ```
      public Response.AddressPrKeyPairMessage.Builder setAddressBytes(com.google.protobuf.ByteString value)
      ```

      `string address = 1;`

      Parameters:
      :   `value` - The bytes for address to set.

      Returns:
      :   This builder for chaining.
    - #### getPrivateKey

      ```
      public java.lang.String getPrivateKey()
      ```

      `string privateKey = 2;`

      Specified by:
      :   `getPrivateKey` in interface `Response.AddressPrKeyPairMessageOrBuilder`

      Returns:
      :   The privateKey.
    - #### getPrivateKeyBytes

      ```
      public com.google.protobuf.ByteString getPrivateKeyBytes()
      ```

      `string privateKey = 2;`

      Specified by:
      :   `getPrivateKeyBytes` in interface `Response.AddressPrKeyPairMessageOrBuilder`

      Returns:
      :   The bytes for privateKey.
    - #### setPrivateKey

      ```
      public Response.AddressPrKeyPairMessage.Builder setPrivateKey(java.lang.String value)
      ```

      `string privateKey = 2;`

      Parameters:
      :   `value` - The privateKey to set.

      Returns:
      :   This builder for chaining.
    - #### clearPrivateKey

      ```
      public Response.AddressPrKeyPairMessage.Builder clearPrivateKey()
      ```

      `string privateKey = 2;`

      Returns:
      :   This builder for chaining.
    - #### setPrivateKeyBytes

      ```
      public Response.AddressPrKeyPairMessage.Builder setPrivateKeyBytes(com.google.protobuf.ByteString value)
      ```

      `string privateKey = 2;`

      Parameters:
      :   `value` - The bytes for privateKey to set.

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.AddressPrKeyPairMessage.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AddressPrKeyPairMessage.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.AddressPrKeyPairMessage.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AddressPrKeyPairMessage.Builder>`