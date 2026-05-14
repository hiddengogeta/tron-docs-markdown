

org.tron.trident.proto

## Class Response.BlockList.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.BlockList.Builder](../../../../org/tron/trident/proto/Response.BlockList.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.BlockList.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.BlockListOrBuilder](../../../../org/tron/trident/proto/Response.BlockListOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.BlockList](../../../../org/tron/trident/proto/Response.BlockList.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.BlockList.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockList.Builder>
  implements Response.BlockListOrBuilder
  ```

  Protobuf type `protocol.BlockList`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.BlockList.Builder` | `addAllBlock(java.lang.Iterable<? extends Chain.Block> values)` `repeated .protocol.Block block = 1;` |
    | `Response.BlockList.Builder` | `addBlock(Chain.Block.Builder builderForValue)` `repeated .protocol.Block block = 1;` |
    | `Response.BlockList.Builder` | `addBlock(Chain.Block value)` `repeated .protocol.Block block = 1;` |
    | `Response.BlockList.Builder` | `addBlock(int index, Chain.Block.Builder builderForValue)` `repeated .protocol.Block block = 1;` |
    | `Response.BlockList.Builder` | `addBlock(int index, Chain.Block value)` `repeated .protocol.Block block = 1;` |
    | `Chain.Block.Builder` | `addBlockBuilder()` `repeated .protocol.Block block = 1;` |
    | `Chain.Block.Builder` | `addBlockBuilder(int index)` `repeated .protocol.Block block = 1;` |
    | `Response.BlockList.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.BlockList` | `build()` |
    | `Response.BlockList` | `buildPartial()` |
    | `Response.BlockList.Builder` | `clear()` |
    | `Response.BlockList.Builder` | `clearBlock()` `repeated .protocol.Block block = 1;` |
    | `Response.BlockList.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.BlockList.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.BlockList.Builder` | `clone()` |
    | `Chain.Block` | `getBlock(int index)` `repeated .protocol.Block block = 1;` |
    | `Chain.Block.Builder` | `getBlockBuilder(int index)` `repeated .protocol.Block block = 1;` |
    | `java.util.List<Chain.Block.Builder>` | `getBlockBuilderList()` `repeated .protocol.Block block = 1;` |
    | `int` | `getBlockCount()` `repeated .protocol.Block block = 1;` |
    | `java.util.List<Chain.Block>` | `getBlockList()` `repeated .protocol.Block block = 1;` |
    | `Chain.BlockOrBuilder` | `getBlockOrBuilder(int index)` `repeated .protocol.Block block = 1;` |
    | `java.util.List<? extends Chain.BlockOrBuilder>` | `getBlockOrBuilderList()` `repeated .protocol.Block block = 1;` |
    | `Response.BlockList` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.BlockList.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.BlockList.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.BlockList.Builder` | `mergeFrom(Response.BlockList other)` |
    | `Response.BlockList.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.BlockList.Builder` | `removeBlock(int index)` `repeated .protocol.Block block = 1;` |
    | `Response.BlockList.Builder` | `setBlock(int index, Chain.Block.Builder builderForValue)` `repeated .protocol.Block block = 1;` |
    | `Response.BlockList.Builder` | `setBlock(int index, Chain.Block value)` `repeated .protocol.Block block = 1;` |
    | `Response.BlockList.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.BlockList.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.BlockList.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockList.Builder>`
    - #### clear

      ```
      public Response.BlockList.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockList.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockList.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.BlockList getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.BlockList build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.BlockList buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.BlockList.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockList.Builder>`
    - #### setField

      ```
      public Response.BlockList.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                 java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockList.Builder>`
    - #### clearField

      ```
      public Response.BlockList.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockList.Builder>`
    - #### clearOneof

      ```
      public Response.BlockList.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockList.Builder>`
    - #### setRepeatedField

      ```
      public Response.BlockList.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                         int index,
                                                         java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockList.Builder>`
    - #### addRepeatedField

      ```
      public Response.BlockList.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                         java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockList.Builder>`
    - #### mergeFrom

      ```
      public Response.BlockList.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.BlockList.Builder>`
    - #### mergeFrom

      ```
      public Response.BlockList.Builder mergeFrom(Response.BlockList other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockList.Builder>`
    - #### mergeFrom

      ```
      public Response.BlockList.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                  com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                           throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.BlockList.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getBlockList

      ```
      public java.util.List<Chain.Block> getBlockList()
      ```

      `repeated .protocol.Block block = 1;`

      Specified by:
      :   `getBlockList` in interface `Response.BlockListOrBuilder`
    - #### getBlockCount

      ```
      public int getBlockCount()
      ```

      `repeated .protocol.Block block = 1;`

      Specified by:
      :   `getBlockCount` in interface `Response.BlockListOrBuilder`
    - #### getBlock

      ```
      public Chain.Block getBlock(int index)
      ```

      `repeated .protocol.Block block = 1;`

      Specified by:
      :   `getBlock` in interface `Response.BlockListOrBuilder`
    - #### setBlock

      ```
      public Response.BlockList.Builder setBlock(int index,
                                                 Chain.Block value)
      ```

      `repeated .protocol.Block block = 1;`
    - #### setBlock

      ```
      public Response.BlockList.Builder setBlock(int index,
                                                 Chain.Block.Builder builderForValue)
      ```

      `repeated .protocol.Block block = 1;`
    - #### addBlock

      ```
      public Response.BlockList.Builder addBlock(Chain.Block value)
      ```

      `repeated .protocol.Block block = 1;`
    - #### addBlock

      ```
      public Response.BlockList.Builder addBlock(int index,
                                                 Chain.Block value)
      ```

      `repeated .protocol.Block block = 1;`
    - #### addBlock

      ```
      public Response.BlockList.Builder addBlock(Chain.Block.Builder builderForValue)
      ```

      `repeated .protocol.Block block = 1;`
    - #### addBlock

      ```
      public Response.BlockList.Builder addBlock(int index,
                                                 Chain.Block.Builder builderForValue)
      ```

      `repeated .protocol.Block block = 1;`
    - #### addAllBlock

      ```
      public Response.BlockList.Builder addAllBlock(java.lang.Iterable<? extends Chain.Block> values)
      ```

      `repeated .protocol.Block block = 1;`
    - #### clearBlock

      ```
      public Response.BlockList.Builder clearBlock()
      ```

      `repeated .protocol.Block block = 1;`
    - #### removeBlock

      ```
      public Response.BlockList.Builder removeBlock(int index)
      ```

      `repeated .protocol.Block block = 1;`
    - #### getBlockBuilder

      ```
      public Chain.Block.Builder getBlockBuilder(int index)
      ```

      `repeated .protocol.Block block = 1;`
    - #### getBlockOrBuilder

      ```
      public Chain.BlockOrBuilder getBlockOrBuilder(int index)
      ```

      `repeated .protocol.Block block = 1;`

      Specified by:
      :   `getBlockOrBuilder` in interface `Response.BlockListOrBuilder`
    - #### getBlockOrBuilderList

      ```
      public java.util.List<? extends Chain.BlockOrBuilder> getBlockOrBuilderList()
      ```

      `repeated .protocol.Block block = 1;`

      Specified by:
      :   `getBlockOrBuilderList` in interface `Response.BlockListOrBuilder`
    - #### addBlockBuilder

      ```
      public Chain.Block.Builder addBlockBuilder()
      ```

      `repeated .protocol.Block block = 1;`
    - #### addBlockBuilder

      ```
      public Chain.Block.Builder addBlockBuilder(int index)
      ```

      `repeated .protocol.Block block = 1;`
    - #### getBlockBuilderList

      ```
      public java.util.List<Chain.Block.Builder> getBlockBuilderList()
      ```

      `repeated .protocol.Block block = 1;`
    - #### setUnknownFields

      ```
      public final Response.BlockList.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockList.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.BlockList.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockList.Builder>`