

org.tron.trident.proto

## Class Response.BlockListExtention.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.BlockListExtention.Builder](../../../../org/tron/trident/proto/Response.BlockListExtention.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.BlockListExtention.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.BlockListExtentionOrBuilder](../../../../org/tron/trident/proto/Response.BlockListExtentionOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.BlockListExtention](../../../../org/tron/trident/proto/Response.BlockListExtention.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.BlockListExtention.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockListExtention.Builder>
  implements Response.BlockListExtentionOrBuilder
  ```

  Protobuf type `protocol.BlockListExtention`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.BlockListExtention.Builder` | `addAllBlock(java.lang.Iterable<? extends Response.BlockExtention> values)` `repeated .protocol.BlockExtention block = 1;` |
    | `Response.BlockListExtention.Builder` | `addBlock(int index, Response.BlockExtention.Builder builderForValue)` `repeated .protocol.BlockExtention block = 1;` |
    | `Response.BlockListExtention.Builder` | `addBlock(int index, Response.BlockExtention value)` `repeated .protocol.BlockExtention block = 1;` |
    | `Response.BlockListExtention.Builder` | `addBlock(Response.BlockExtention.Builder builderForValue)` `repeated .protocol.BlockExtention block = 1;` |
    | `Response.BlockListExtention.Builder` | `addBlock(Response.BlockExtention value)` `repeated .protocol.BlockExtention block = 1;` |
    | `Response.BlockExtention.Builder` | `addBlockBuilder()` `repeated .protocol.BlockExtention block = 1;` |
    | `Response.BlockExtention.Builder` | `addBlockBuilder(int index)` `repeated .protocol.BlockExtention block = 1;` |
    | `Response.BlockListExtention.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.BlockListExtention` | `build()` |
    | `Response.BlockListExtention` | `buildPartial()` |
    | `Response.BlockListExtention.Builder` | `clear()` |
    | `Response.BlockListExtention.Builder` | `clearBlock()` `repeated .protocol.BlockExtention block = 1;` |
    | `Response.BlockListExtention.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.BlockListExtention.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.BlockListExtention.Builder` | `clone()` |
    | `Response.BlockExtention` | `getBlock(int index)` `repeated .protocol.BlockExtention block = 1;` |
    | `Response.BlockExtention.Builder` | `getBlockBuilder(int index)` `repeated .protocol.BlockExtention block = 1;` |
    | `java.util.List<Response.BlockExtention.Builder>` | `getBlockBuilderList()` `repeated .protocol.BlockExtention block = 1;` |
    | `int` | `getBlockCount()` `repeated .protocol.BlockExtention block = 1;` |
    | `java.util.List<Response.BlockExtention>` | `getBlockList()` `repeated .protocol.BlockExtention block = 1;` |
    | `Response.BlockExtentionOrBuilder` | `getBlockOrBuilder(int index)` `repeated .protocol.BlockExtention block = 1;` |
    | `java.util.List<? extends Response.BlockExtentionOrBuilder>` | `getBlockOrBuilderList()` `repeated .protocol.BlockExtention block = 1;` |
    | `Response.BlockListExtention` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.BlockListExtention.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.BlockListExtention.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.BlockListExtention.Builder` | `mergeFrom(Response.BlockListExtention other)` |
    | `Response.BlockListExtention.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.BlockListExtention.Builder` | `removeBlock(int index)` `repeated .protocol.BlockExtention block = 1;` |
    | `Response.BlockListExtention.Builder` | `setBlock(int index, Response.BlockExtention.Builder builderForValue)` `repeated .protocol.BlockExtention block = 1;` |
    | `Response.BlockListExtention.Builder` | `setBlock(int index, Response.BlockExtention value)` `repeated .protocol.BlockExtention block = 1;` |
    | `Response.BlockListExtention.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.BlockListExtention.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.BlockListExtention.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockListExtention.Builder>`
    - #### clear

      ```
      public Response.BlockListExtention.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockListExtention.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockListExtention.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.BlockListExtention getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.BlockListExtention build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.BlockListExtention buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.BlockListExtention.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockListExtention.Builder>`
    - #### setField

      ```
      public Response.BlockListExtention.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                          java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockListExtention.Builder>`
    - #### clearField

      ```
      public Response.BlockListExtention.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockListExtention.Builder>`
    - #### clearOneof

      ```
      public Response.BlockListExtention.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockListExtention.Builder>`
    - #### setRepeatedField

      ```
      public Response.BlockListExtention.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                  int index,
                                                                  java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockListExtention.Builder>`
    - #### addRepeatedField

      ```
      public Response.BlockListExtention.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                  java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockListExtention.Builder>`
    - #### mergeFrom

      ```
      public Response.BlockListExtention.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.BlockListExtention.Builder>`
    - #### mergeFrom

      ```
      public Response.BlockListExtention.Builder mergeFrom(Response.BlockListExtention other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockListExtention.Builder>`
    - #### mergeFrom

      ```
      public Response.BlockListExtention.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                    throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.BlockListExtention.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getBlockList

      ```
      public java.util.List<Response.BlockExtention> getBlockList()
      ```

      `repeated .protocol.BlockExtention block = 1;`

      Specified by:
      :   `getBlockList` in interface `Response.BlockListExtentionOrBuilder`
    - #### getBlockCount

      ```
      public int getBlockCount()
      ```

      `repeated .protocol.BlockExtention block = 1;`

      Specified by:
      :   `getBlockCount` in interface `Response.BlockListExtentionOrBuilder`
    - #### getBlock

      ```
      public Response.BlockExtention getBlock(int index)
      ```

      `repeated .protocol.BlockExtention block = 1;`

      Specified by:
      :   `getBlock` in interface `Response.BlockListExtentionOrBuilder`
    - #### setBlock

      ```
      public Response.BlockListExtention.Builder setBlock(int index,
                                                          Response.BlockExtention value)
      ```

      `repeated .protocol.BlockExtention block = 1;`
    - #### setBlock

      ```
      public Response.BlockListExtention.Builder setBlock(int index,
                                                          Response.BlockExtention.Builder builderForValue)
      ```

      `repeated .protocol.BlockExtention block = 1;`
    - #### addBlock

      ```
      public Response.BlockListExtention.Builder addBlock(Response.BlockExtention value)
      ```

      `repeated .protocol.BlockExtention block = 1;`
    - #### addBlock

      ```
      public Response.BlockListExtention.Builder addBlock(int index,
                                                          Response.BlockExtention value)
      ```

      `repeated .protocol.BlockExtention block = 1;`
    - #### addBlock

      ```
      public Response.BlockListExtention.Builder addBlock(Response.BlockExtention.Builder builderForValue)
      ```

      `repeated .protocol.BlockExtention block = 1;`
    - #### addBlock

      ```
      public Response.BlockListExtention.Builder addBlock(int index,
                                                          Response.BlockExtention.Builder builderForValue)
      ```

      `repeated .protocol.BlockExtention block = 1;`
    - #### addAllBlock

      ```
      public Response.BlockListExtention.Builder addAllBlock(java.lang.Iterable<? extends Response.BlockExtention> values)
      ```

      `repeated .protocol.BlockExtention block = 1;`
    - #### clearBlock

      ```
      public Response.BlockListExtention.Builder clearBlock()
      ```

      `repeated .protocol.BlockExtention block = 1;`
    - #### removeBlock

      ```
      public Response.BlockListExtention.Builder removeBlock(int index)
      ```

      `repeated .protocol.BlockExtention block = 1;`
    - #### getBlockBuilder

      ```
      public Response.BlockExtention.Builder getBlockBuilder(int index)
      ```

      `repeated .protocol.BlockExtention block = 1;`
    - #### getBlockOrBuilder

      ```
      public Response.BlockExtentionOrBuilder getBlockOrBuilder(int index)
      ```

      `repeated .protocol.BlockExtention block = 1;`

      Specified by:
      :   `getBlockOrBuilder` in interface `Response.BlockListExtentionOrBuilder`
    - #### getBlockOrBuilderList

      ```
      public java.util.List<? extends Response.BlockExtentionOrBuilder> getBlockOrBuilderList()
      ```

      `repeated .protocol.BlockExtention block = 1;`

      Specified by:
      :   `getBlockOrBuilderList` in interface `Response.BlockListExtentionOrBuilder`
    - #### addBlockBuilder

      ```
      public Response.BlockExtention.Builder addBlockBuilder()
      ```

      `repeated .protocol.BlockExtention block = 1;`
    - #### addBlockBuilder

      ```
      public Response.BlockExtention.Builder addBlockBuilder(int index)
      ```

      `repeated .protocol.BlockExtention block = 1;`
    - #### getBlockBuilderList

      ```
      public java.util.List<Response.BlockExtention.Builder> getBlockBuilderList()
      ```

      `repeated .protocol.BlockExtention block = 1;`
    - #### setUnknownFields

      ```
      public final Response.BlockListExtention.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockListExtention.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.BlockListExtention.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockListExtention.Builder>`