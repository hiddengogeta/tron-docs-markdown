

org.tron.trident.proto

## Class Response.BlockExtention.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.BlockExtention.Builder](../../../../org/tron/trident/proto/Response.BlockExtention.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.BlockExtention.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.BlockExtentionOrBuilder](../../../../org/tron/trident/proto/Response.BlockExtentionOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.BlockExtention](../../../../org/tron/trident/proto/Response.BlockExtention.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.BlockExtention.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockExtention.Builder>
  implements Response.BlockExtentionOrBuilder
  ```

  Protobuf type `protocol.BlockExtention`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.BlockExtention.Builder` | `addAllTransactions(java.lang.Iterable<? extends Response.TransactionExtention> values)` `repeated .protocol.TransactionExtention transactions = 1;` |
    | `Response.BlockExtention.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.BlockExtention.Builder` | `addTransactions(int index, Response.TransactionExtention.Builder builderForValue)` `repeated .protocol.TransactionExtention transactions = 1;` |
    | `Response.BlockExtention.Builder` | `addTransactions(int index, Response.TransactionExtention value)` `repeated .protocol.TransactionExtention transactions = 1;` |
    | `Response.BlockExtention.Builder` | `addTransactions(Response.TransactionExtention.Builder builderForValue)` `repeated .protocol.TransactionExtention transactions = 1;` |
    | `Response.BlockExtention.Builder` | `addTransactions(Response.TransactionExtention value)` `repeated .protocol.TransactionExtention transactions = 1;` |
    | `Response.TransactionExtention.Builder` | `addTransactionsBuilder()` `repeated .protocol.TransactionExtention transactions = 1;` |
    | `Response.TransactionExtention.Builder` | `addTransactionsBuilder(int index)` `repeated .protocol.TransactionExtention transactions = 1;` |
    | `Response.BlockExtention` | `build()` |
    | `Response.BlockExtention` | `buildPartial()` |
    | `Response.BlockExtention.Builder` | `clear()` |
    | `Response.BlockExtention.Builder` | `clearBlockHeader()` `.protocol.BlockHeader block_header = 2;` |
    | `Response.BlockExtention.Builder` | `clearBlockid()` `bytes blockid = 3;` |
    | `Response.BlockExtention.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.BlockExtention.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.BlockExtention.Builder` | `clearTransactions()` `repeated .protocol.TransactionExtention transactions = 1;` |
    | `Response.BlockExtention.Builder` | `clone()` |
    | `Chain.BlockHeader` | `getBlockHeader()` `.protocol.BlockHeader block_header = 2;` |
    | `Chain.BlockHeader.Builder` | `getBlockHeaderBuilder()` `.protocol.BlockHeader block_header = 2;` |
    | `Chain.BlockHeaderOrBuilder` | `getBlockHeaderOrBuilder()` `.protocol.BlockHeader block_header = 2;` |
    | `com.google.protobuf.ByteString` | `getBlockid()` `bytes blockid = 3;` |
    | `Response.BlockExtention` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Response.TransactionExtention` | `getTransactions(int index)` `repeated .protocol.TransactionExtention transactions = 1;` |
    | `Response.TransactionExtention.Builder` | `getTransactionsBuilder(int index)` `repeated .protocol.TransactionExtention transactions = 1;` |
    | `java.util.List<Response.TransactionExtention.Builder>` | `getTransactionsBuilderList()` `repeated .protocol.TransactionExtention transactions = 1;` |
    | `int` | `getTransactionsCount()` `repeated .protocol.TransactionExtention transactions = 1;` |
    | `java.util.List<Response.TransactionExtention>` | `getTransactionsList()` `repeated .protocol.TransactionExtention transactions = 1;` |
    | `Response.TransactionExtentionOrBuilder` | `getTransactionsOrBuilder(int index)` `repeated .protocol.TransactionExtention transactions = 1;` |
    | `java.util.List<? extends Response.TransactionExtentionOrBuilder>` | `getTransactionsOrBuilderList()` `repeated .protocol.TransactionExtention transactions = 1;` |
    | `boolean` | `hasBlockHeader()` `.protocol.BlockHeader block_header = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.BlockExtention.Builder` | `mergeBlockHeader(Chain.BlockHeader value)` `.protocol.BlockHeader block_header = 2;` |
    | `Response.BlockExtention.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.BlockExtention.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.BlockExtention.Builder` | `mergeFrom(Response.BlockExtention other)` |
    | `Response.BlockExtention.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.BlockExtention.Builder` | `removeTransactions(int index)` `repeated .protocol.TransactionExtention transactions = 1;` |
    | `Response.BlockExtention.Builder` | `setBlockHeader(Chain.BlockHeader.Builder builderForValue)` `.protocol.BlockHeader block_header = 2;` |
    | `Response.BlockExtention.Builder` | `setBlockHeader(Chain.BlockHeader value)` `.protocol.BlockHeader block_header = 2;` |
    | `Response.BlockExtention.Builder` | `setBlockid(com.google.protobuf.ByteString value)` `bytes blockid = 3;` |
    | `Response.BlockExtention.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.BlockExtention.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.BlockExtention.Builder` | `setTransactions(int index, Response.TransactionExtention.Builder builderForValue)` `repeated .protocol.TransactionExtention transactions = 1;` |
    | `Response.BlockExtention.Builder` | `setTransactions(int index, Response.TransactionExtention value)` `repeated .protocol.TransactionExtention transactions = 1;` |
    | `Response.BlockExtention.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockExtention.Builder>`
    - #### clear

      ```
      public Response.BlockExtention.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockExtention.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockExtention.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.BlockExtention getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.BlockExtention build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.BlockExtention buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.BlockExtention.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockExtention.Builder>`
    - #### setField

      ```
      public Response.BlockExtention.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                      java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockExtention.Builder>`
    - #### clearField

      ```
      public Response.BlockExtention.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockExtention.Builder>`
    - #### clearOneof

      ```
      public Response.BlockExtention.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockExtention.Builder>`
    - #### setRepeatedField

      ```
      public Response.BlockExtention.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                              int index,
                                                              java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockExtention.Builder>`
    - #### addRepeatedField

      ```
      public Response.BlockExtention.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                              java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockExtention.Builder>`
    - #### mergeFrom

      ```
      public Response.BlockExtention.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.BlockExtention.Builder>`
    - #### mergeFrom

      ```
      public Response.BlockExtention.Builder mergeFrom(Response.BlockExtention other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockExtention.Builder>`
    - #### mergeFrom

      ```
      public Response.BlockExtention.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.BlockExtention.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getTransactionsList

      ```
      public java.util.List<Response.TransactionExtention> getTransactionsList()
      ```

      `repeated .protocol.TransactionExtention transactions = 1;`

      Specified by:
      :   `getTransactionsList` in interface `Response.BlockExtentionOrBuilder`
    - #### getTransactionsCount

      ```
      public int getTransactionsCount()
      ```

      `repeated .protocol.TransactionExtention transactions = 1;`

      Specified by:
      :   `getTransactionsCount` in interface `Response.BlockExtentionOrBuilder`
    - #### getTransactions

      ```
      public Response.TransactionExtention getTransactions(int index)
      ```

      `repeated .protocol.TransactionExtention transactions = 1;`

      Specified by:
      :   `getTransactions` in interface `Response.BlockExtentionOrBuilder`
    - #### setTransactions

      ```
      public Response.BlockExtention.Builder setTransactions(int index,
                                                             Response.TransactionExtention value)
      ```

      `repeated .protocol.TransactionExtention transactions = 1;`
    - #### setTransactions

      ```
      public Response.BlockExtention.Builder setTransactions(int index,
                                                             Response.TransactionExtention.Builder builderForValue)
      ```

      `repeated .protocol.TransactionExtention transactions = 1;`
    - #### addTransactions

      ```
      public Response.BlockExtention.Builder addTransactions(Response.TransactionExtention value)
      ```

      `repeated .protocol.TransactionExtention transactions = 1;`
    - #### addTransactions

      ```
      public Response.BlockExtention.Builder addTransactions(int index,
                                                             Response.TransactionExtention value)
      ```

      `repeated .protocol.TransactionExtention transactions = 1;`
    - #### addTransactions

      ```
      public Response.BlockExtention.Builder addTransactions(Response.TransactionExtention.Builder builderForValue)
      ```

      `repeated .protocol.TransactionExtention transactions = 1;`
    - #### addTransactions

      ```
      public Response.BlockExtention.Builder addTransactions(int index,
                                                             Response.TransactionExtention.Builder builderForValue)
      ```

      `repeated .protocol.TransactionExtention transactions = 1;`
    - #### addAllTransactions

      ```
      public Response.BlockExtention.Builder addAllTransactions(java.lang.Iterable<? extends Response.TransactionExtention> values)
      ```

      `repeated .protocol.TransactionExtention transactions = 1;`
    - #### clearTransactions

      ```
      public Response.BlockExtention.Builder clearTransactions()
      ```

      `repeated .protocol.TransactionExtention transactions = 1;`
    - #### removeTransactions

      ```
      public Response.BlockExtention.Builder removeTransactions(int index)
      ```

      `repeated .protocol.TransactionExtention transactions = 1;`
    - #### getTransactionsBuilder

      ```
      public Response.TransactionExtention.Builder getTransactionsBuilder(int index)
      ```

      `repeated .protocol.TransactionExtention transactions = 1;`
    - #### getTransactionsOrBuilder

      ```
      public Response.TransactionExtentionOrBuilder getTransactionsOrBuilder(int index)
      ```

      `repeated .protocol.TransactionExtention transactions = 1;`

      Specified by:
      :   `getTransactionsOrBuilder` in interface `Response.BlockExtentionOrBuilder`
    - #### getTransactionsOrBuilderList

      ```
      public java.util.List<? extends Response.TransactionExtentionOrBuilder> getTransactionsOrBuilderList()
      ```

      `repeated .protocol.TransactionExtention transactions = 1;`

      Specified by:
      :   `getTransactionsOrBuilderList` in interface `Response.BlockExtentionOrBuilder`
    - #### addTransactionsBuilder

      ```
      public Response.TransactionExtention.Builder addTransactionsBuilder()
      ```

      `repeated .protocol.TransactionExtention transactions = 1;`
    - #### addTransactionsBuilder

      ```
      public Response.TransactionExtention.Builder addTransactionsBuilder(int index)
      ```

      `repeated .protocol.TransactionExtention transactions = 1;`
    - #### getTransactionsBuilderList

      ```
      public java.util.List<Response.TransactionExtention.Builder> getTransactionsBuilderList()
      ```

      `repeated .protocol.TransactionExtention transactions = 1;`
    - #### hasBlockHeader

      ```
      public boolean hasBlockHeader()
      ```

      `.protocol.BlockHeader block_header = 2;`

      Specified by:
      :   `hasBlockHeader` in interface `Response.BlockExtentionOrBuilder`

      Returns:
      :   Whether the blockHeader field is set.
    - #### getBlockHeader

      ```
      public Chain.BlockHeader getBlockHeader()
      ```

      `.protocol.BlockHeader block_header = 2;`

      Specified by:
      :   `getBlockHeader` in interface `Response.BlockExtentionOrBuilder`

      Returns:
      :   The blockHeader.
    - #### setBlockHeader

      ```
      public Response.BlockExtention.Builder setBlockHeader(Chain.BlockHeader value)
      ```

      `.protocol.BlockHeader block_header = 2;`
    - #### setBlockHeader

      ```
      public Response.BlockExtention.Builder setBlockHeader(Chain.BlockHeader.Builder builderForValue)
      ```

      `.protocol.BlockHeader block_header = 2;`
    - #### mergeBlockHeader

      ```
      public Response.BlockExtention.Builder mergeBlockHeader(Chain.BlockHeader value)
      ```

      `.protocol.BlockHeader block_header = 2;`
    - #### clearBlockHeader

      ```
      public Response.BlockExtention.Builder clearBlockHeader()
      ```

      `.protocol.BlockHeader block_header = 2;`
    - #### getBlockHeaderBuilder

      ```
      public Chain.BlockHeader.Builder getBlockHeaderBuilder()
      ```

      `.protocol.BlockHeader block_header = 2;`
    - #### getBlockHeaderOrBuilder

      ```
      public Chain.BlockHeaderOrBuilder getBlockHeaderOrBuilder()
      ```

      `.protocol.BlockHeader block_header = 2;`

      Specified by:
      :   `getBlockHeaderOrBuilder` in interface `Response.BlockExtentionOrBuilder`
    - #### getBlockid

      ```
      public com.google.protobuf.ByteString getBlockid()
      ```

      `bytes blockid = 3;`

      Specified by:
      :   `getBlockid` in interface `Response.BlockExtentionOrBuilder`

      Returns:
      :   The blockid.
    - #### setBlockid

      ```
      public Response.BlockExtention.Builder setBlockid(com.google.protobuf.ByteString value)
      ```

      `bytes blockid = 3;`

      Parameters:
      :   `value` - The blockid to set.

      Returns:
      :   This builder for chaining.
    - #### clearBlockid

      ```
      public Response.BlockExtention.Builder clearBlockid()
      ```

      `bytes blockid = 3;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.BlockExtention.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockExtention.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.BlockExtention.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockExtention.Builder>`