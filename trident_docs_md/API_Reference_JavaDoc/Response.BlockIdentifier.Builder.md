

org.tron.trident.proto

## Class Response.BlockIdentifier.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.BlockIdentifier.Builder](../../../../org/tron/trident/proto/Response.BlockIdentifier.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.BlockIdentifier.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.BlockIdentifierOrBuilder](../../../../org/tron/trident/proto/Response.BlockIdentifierOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.BlockIdentifier](../../../../org/tron/trident/proto/Response.BlockIdentifier.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.BlockIdentifier.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockIdentifier.Builder>
  implements Response.BlockIdentifierOrBuilder
  ```

  Protobuf type `protocol.BlockIdentifier`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.BlockIdentifier.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.BlockIdentifier` | `build()` |
    | `Response.BlockIdentifier` | `buildPartial()` |
    | `Response.BlockIdentifier.Builder` | `clear()` |
    | `Response.BlockIdentifier.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.BlockIdentifier.Builder` | `clearHash()` `bytes hash = 1;` |
    | `Response.BlockIdentifier.Builder` | `clearNumber()` `int64 number = 2;` |
    | `Response.BlockIdentifier.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.BlockIdentifier.Builder` | `clone()` |
    | `Response.BlockIdentifier` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getHash()` `bytes hash = 1;` |
    | `long` | `getNumber()` `int64 number = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.BlockIdentifier.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.BlockIdentifier.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.BlockIdentifier.Builder` | `mergeFrom(Response.BlockIdentifier other)` |
    | `Response.BlockIdentifier.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.BlockIdentifier.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.BlockIdentifier.Builder` | `setHash(com.google.protobuf.ByteString value)` `bytes hash = 1;` |
    | `Response.BlockIdentifier.Builder` | `setNumber(long value)` `int64 number = 2;` |
    | `Response.BlockIdentifier.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.BlockIdentifier.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockIdentifier.Builder>`
    - #### clear

      ```
      public Response.BlockIdentifier.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockIdentifier.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockIdentifier.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.BlockIdentifier getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.BlockIdentifier build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.BlockIdentifier buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.BlockIdentifier.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockIdentifier.Builder>`
    - #### setField

      ```
      public Response.BlockIdentifier.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockIdentifier.Builder>`
    - #### clearField

      ```
      public Response.BlockIdentifier.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockIdentifier.Builder>`
    - #### clearOneof

      ```
      public Response.BlockIdentifier.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockIdentifier.Builder>`
    - #### setRepeatedField

      ```
      public Response.BlockIdentifier.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               int index,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockIdentifier.Builder>`
    - #### addRepeatedField

      ```
      public Response.BlockIdentifier.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockIdentifier.Builder>`
    - #### mergeFrom

      ```
      public Response.BlockIdentifier.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.BlockIdentifier.Builder>`
    - #### mergeFrom

      ```
      public Response.BlockIdentifier.Builder mergeFrom(Response.BlockIdentifier other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockIdentifier.Builder>`
    - #### mergeFrom

      ```
      public Response.BlockIdentifier.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                 throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.BlockIdentifier.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getHash

      ```
      public com.google.protobuf.ByteString getHash()
      ```

      `bytes hash = 1;`

      Specified by:
      :   `getHash` in interface `Response.BlockIdentifierOrBuilder`

      Returns:
      :   The hash.
    - #### setHash

      ```
      public Response.BlockIdentifier.Builder setHash(com.google.protobuf.ByteString value)
      ```

      `bytes hash = 1;`

      Parameters:
      :   `value` - The hash to set.

      Returns:
      :   This builder for chaining.
    - #### clearHash

      ```
      public Response.BlockIdentifier.Builder clearHash()
      ```

      `bytes hash = 1;`

      Returns:
      :   This builder for chaining.
    - #### getNumber

      ```
      public long getNumber()
      ```

      `int64 number = 2;`

      Specified by:
      :   `getNumber` in interface `Response.BlockIdentifierOrBuilder`

      Returns:
      :   The number.
    - #### setNumber

      ```
      public Response.BlockIdentifier.Builder setNumber(long value)
      ```

      `int64 number = 2;`

      Parameters:
      :   `value` - The number to set.

      Returns:
      :   This builder for chaining.
    - #### clearNumber

      ```
      public Response.BlockIdentifier.Builder clearNumber()
      ```

      `int64 number = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.BlockIdentifier.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockIdentifier.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.BlockIdentifier.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockIdentifier.Builder>`