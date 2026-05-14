

org.tron.trident.proto

## Class Response.NodeList.Node.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.NodeList.Node.Builder](../../../../org/tron/trident/proto/Response.NodeList.Node.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.NodeList.Node.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.NodeList.NodeOrBuilder](../../../../org/tron/trident/proto/Response.NodeList.NodeOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.NodeList.Node](../../../../org/tron/trident/proto/Response.NodeList.Node.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.NodeList.Node.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Builder>
  implements Response.NodeList.NodeOrBuilder
  ```

  ```
   Gossip node
  ```

  Protobuf type `protocol.NodeList.Node`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.NodeList.Node.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.NodeList.Node` | `build()` |
    | `Response.NodeList.Node` | `buildPartial()` |
    | `Response.NodeList.Node.Builder` | `clear()` |
    | `Response.NodeList.Node.Builder` | `clearAddress()` `.protocol.NodeList.Node.Address address = 1;` |
    | `Response.NodeList.Node.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.NodeList.Node.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.NodeList.Node.Builder` | `clone()` |
    | `Response.NodeList.Node.Address` | `getAddress()` `.protocol.NodeList.Node.Address address = 1;` |
    | `Response.NodeList.Node.Address.Builder` | `getAddressBuilder()` `.protocol.NodeList.Node.Address address = 1;` |
    | `Response.NodeList.Node.AddressOrBuilder` | `getAddressOrBuilder()` `.protocol.NodeList.Node.Address address = 1;` |
    | `Response.NodeList.Node` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `boolean` | `hasAddress()` `.protocol.NodeList.Node.Address address = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.NodeList.Node.Builder` | `mergeAddress(Response.NodeList.Node.Address value)` `.protocol.NodeList.Node.Address address = 1;` |
    | `Response.NodeList.Node.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.NodeList.Node.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.NodeList.Node.Builder` | `mergeFrom(Response.NodeList.Node other)` |
    | `Response.NodeList.Node.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.NodeList.Node.Builder` | `setAddress(Response.NodeList.Node.Address.Builder builderForValue)` `.protocol.NodeList.Node.Address address = 1;` |
    | `Response.NodeList.Node.Builder` | `setAddress(Response.NodeList.Node.Address value)` `.protocol.NodeList.Node.Address address = 1;` |
    | `Response.NodeList.Node.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.NodeList.Node.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.NodeList.Node.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Builder>`
    - #### clear

      ```
      public Response.NodeList.Node.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.NodeList.Node getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.NodeList.Node build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.NodeList.Node buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.NodeList.Node.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Builder>`
    - #### setField

      ```
      public Response.NodeList.Node.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                     java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Builder>`
    - #### clearField

      ```
      public Response.NodeList.Node.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Builder>`
    - #### clearOneof

      ```
      public Response.NodeList.Node.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Builder>`
    - #### setRepeatedField

      ```
      public Response.NodeList.Node.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                             int index,
                                                             java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Builder>`
    - #### addRepeatedField

      ```
      public Response.NodeList.Node.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                             java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeList.Node.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.NodeList.Node.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeList.Node.Builder mergeFrom(Response.NodeList.Node other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeList.Node.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                               throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.NodeList.Node.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### hasAddress

      ```
      public boolean hasAddress()
      ```

      `.protocol.NodeList.Node.Address address = 1;`

      Specified by:
      :   `hasAddress` in interface `Response.NodeList.NodeOrBuilder`

      Returns:
      :   Whether the address field is set.
    - #### getAddress

      ```
      public Response.NodeList.Node.Address getAddress()
      ```

      `.protocol.NodeList.Node.Address address = 1;`

      Specified by:
      :   `getAddress` in interface `Response.NodeList.NodeOrBuilder`

      Returns:
      :   The address.
    - #### setAddress

      ```
      public Response.NodeList.Node.Builder setAddress(Response.NodeList.Node.Address value)
      ```

      `.protocol.NodeList.Node.Address address = 1;`
    - #### setAddress

      ```
      public Response.NodeList.Node.Builder setAddress(Response.NodeList.Node.Address.Builder builderForValue)
      ```

      `.protocol.NodeList.Node.Address address = 1;`
    - #### mergeAddress

      ```
      public Response.NodeList.Node.Builder mergeAddress(Response.NodeList.Node.Address value)
      ```

      `.protocol.NodeList.Node.Address address = 1;`
    - #### clearAddress

      ```
      public Response.NodeList.Node.Builder clearAddress()
      ```

      `.protocol.NodeList.Node.Address address = 1;`
    - #### getAddressBuilder

      ```
      public Response.NodeList.Node.Address.Builder getAddressBuilder()
      ```

      `.protocol.NodeList.Node.Address address = 1;`
    - #### getAddressOrBuilder

      ```
      public Response.NodeList.Node.AddressOrBuilder getAddressOrBuilder()
      ```

      `.protocol.NodeList.Node.Address address = 1;`

      Specified by:
      :   `getAddressOrBuilder` in interface `Response.NodeList.NodeOrBuilder`
    - #### setUnknownFields

      ```
      public final Response.NodeList.Node.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.NodeList.Node.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Builder>`