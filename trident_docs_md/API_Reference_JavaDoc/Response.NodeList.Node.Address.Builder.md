

org.tron.trident.proto

## Class Response.NodeList.Node.Address.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.NodeList.Node.Address.Builder](../../../../org/tron/trident/proto/Response.NodeList.Node.Address.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.NodeList.Node.Address.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.NodeList.Node.AddressOrBuilder](../../../../org/tron/trident/proto/Response.NodeList.Node.AddressOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.NodeList.Node.Address](../../../../org/tron/trident/proto/Response.NodeList.Node.Address.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.NodeList.Node.Address.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Address.Builder>
  implements Response.NodeList.Node.AddressOrBuilder
  ```

  ```
   Gossip node address
  ```

  Protobuf type `protocol.NodeList.Node.Address`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.NodeList.Node.Address.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.NodeList.Node.Address` | `build()` |
    | `Response.NodeList.Node.Address` | `buildPartial()` |
    | `Response.NodeList.Node.Address.Builder` | `clear()` |
    | `Response.NodeList.Node.Address.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.NodeList.Node.Address.Builder` | `clearHost()` `bytes host = 1;` |
    | `Response.NodeList.Node.Address.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.NodeList.Node.Address.Builder` | `clearPort()` `int32 port = 2;` |
    | `Response.NodeList.Node.Address.Builder` | `clone()` |
    | `Response.NodeList.Node.Address` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getHost()` `bytes host = 1;` |
    | `int` | `getPort()` `int32 port = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.NodeList.Node.Address.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.NodeList.Node.Address.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.NodeList.Node.Address.Builder` | `mergeFrom(Response.NodeList.Node.Address other)` |
    | `Response.NodeList.Node.Address.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.NodeList.Node.Address.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.NodeList.Node.Address.Builder` | `setHost(com.google.protobuf.ByteString value)` `bytes host = 1;` |
    | `Response.NodeList.Node.Address.Builder` | `setPort(int value)` `int32 port = 2;` |
    | `Response.NodeList.Node.Address.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.NodeList.Node.Address.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Address.Builder>`
    - #### clear

      ```
      public Response.NodeList.Node.Address.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Address.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Address.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.NodeList.Node.Address getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.NodeList.Node.Address build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.NodeList.Node.Address buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.NodeList.Node.Address.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Address.Builder>`
    - #### setField

      ```
      public Response.NodeList.Node.Address.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                             java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Address.Builder>`
    - #### clearField

      ```
      public Response.NodeList.Node.Address.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Address.Builder>`
    - #### clearOneof

      ```
      public Response.NodeList.Node.Address.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Address.Builder>`
    - #### setRepeatedField

      ```
      public Response.NodeList.Node.Address.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     int index,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Address.Builder>`
    - #### addRepeatedField

      ```
      public Response.NodeList.Node.Address.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Address.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeList.Node.Address.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.NodeList.Node.Address.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeList.Node.Address.Builder mergeFrom(Response.NodeList.Node.Address other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Address.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeList.Node.Address.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.NodeList.Node.Address.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getHost

      ```
      public com.google.protobuf.ByteString getHost()
      ```

      `bytes host = 1;`

      Specified by:
      :   `getHost` in interface `Response.NodeList.Node.AddressOrBuilder`

      Returns:
      :   The host.
    - #### setHost

      ```
      public Response.NodeList.Node.Address.Builder setHost(com.google.protobuf.ByteString value)
      ```

      `bytes host = 1;`

      Parameters:
      :   `value` - The host to set.

      Returns:
      :   This builder for chaining.
    - #### clearHost

      ```
      public Response.NodeList.Node.Address.Builder clearHost()
      ```

      `bytes host = 1;`

      Returns:
      :   This builder for chaining.
    - #### getPort

      ```
      public int getPort()
      ```

      `int32 port = 2;`

      Specified by:
      :   `getPort` in interface `Response.NodeList.Node.AddressOrBuilder`

      Returns:
      :   The port.
    - #### setPort

      ```
      public Response.NodeList.Node.Address.Builder setPort(int value)
      ```

      `int32 port = 2;`

      Parameters:
      :   `value` - The port to set.

      Returns:
      :   This builder for chaining.
    - #### clearPort

      ```
      public Response.NodeList.Node.Address.Builder clearPort()
      ```

      `int32 port = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.NodeList.Node.Address.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Address.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.NodeList.Node.Address.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Node.Address.Builder>`