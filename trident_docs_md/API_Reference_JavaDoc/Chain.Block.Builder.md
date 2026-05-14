

org.tron.trident.proto

## Class Chain.Block.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Chain.Block.Builder](../../../../org/tron/trident/proto/Chain.Block.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Chain.Block.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Chain.BlockOrBuilder](../../../../org/tron/trident/proto/Chain.BlockOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Chain.Block](../../../../org/tron/trident/proto/Chain.Block.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Chain.Block.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Chain.Block.Builder>
  implements Chain.BlockOrBuilder
  ```

  ```
   block
  ```

  Protobuf type `protocol.Block`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Chain.Block.Builder` | `addAllTransactions(java.lang.Iterable<? extends Chain.Transaction> values)` `repeated .protocol.Transaction transactions = 1;` |
    | `Chain.Block.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Chain.Block.Builder` | `addTransactions(Chain.Transaction.Builder builderForValue)` `repeated .protocol.Transaction transactions = 1;` |
    | `Chain.Block.Builder` | `addTransactions(Chain.Transaction value)` `repeated .protocol.Transaction transactions = 1;` |
    | `Chain.Block.Builder` | `addTransactions(int index, Chain.Transaction.Builder builderForValue)` `repeated .protocol.Transaction transactions = 1;` |
    | `Chain.Block.Builder` | `addTransactions(int index, Chain.Transaction value)` `repeated .protocol.Transaction transactions = 1;` |
    | `Chain.Transaction.Builder` | `addTransactionsBuilder()` `repeated .protocol.Transaction transactions = 1;` |
    | `Chain.Transaction.Builder` | `addTransactionsBuilder(int index)` `repeated .protocol.Transaction transactions = 1;` |
    | `Chain.Block` | `build()` |
    | `Chain.Block` | `buildPartial()` |
    | `Chain.Block.Builder` | `clear()` |
    | `Chain.Block.Builder` | `clearBlockHeader()` `.protocol.BlockHeader block_header = 2;` |
    | `Chain.Block.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Chain.Block.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Chain.Block.Builder` | `clearTransactions()` `repeated .protocol.Transaction transactions = 1;` |
    | `Chain.Block.Builder` | `clone()` |
    | `Chain.BlockHeader` | `getBlockHeader()` `.protocol.BlockHeader block_header = 2;` |
    | `Chain.BlockHeader.Builder` | `getBlockHeaderBuilder()` `.protocol.BlockHeader block_header = 2;` |
    | `Chain.BlockHeaderOrBuilder` | `getBlockHeaderOrBuilder()` `.protocol.BlockHeader block_header = 2;` |
    | `Chain.Block` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Chain.Transaction` | `getTransactions(int index)` `repeated .protocol.Transaction transactions = 1;` |
    | `Chain.Transaction.Builder` | `getTransactionsBuilder(int index)` `repeated .protocol.Transaction transactions = 1;` |
    | `java.util.List<Chain.Transaction.Builder>` | `getTransactionsBuilderList()` `repeated .protocol.Transaction transactions = 1;` |
    | `int` | `getTransactionsCount()` `repeated .protocol.Transaction transactions = 1;` |
    | `java.util.List<Chain.Transaction>` | `getTransactionsList()` `repeated .protocol.Transaction transactions = 1;` |
    | `Chain.TransactionOrBuilder` | `getTransactionsOrBuilder(int index)` `repeated .protocol.Transaction transactions = 1;` |
    | `java.util.List<? extends Chain.TransactionOrBuilder>` | `getTransactionsOrBuilderList()` `repeated .protocol.Transaction transactions = 1;` |
    | `boolean` | `hasBlockHeader()` `.protocol.BlockHeader block_header = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Chain.Block.Builder` | `mergeBlockHeader(Chain.BlockHeader value)` `.protocol.BlockHeader block_header = 2;` |
    | `Chain.Block.Builder` | `mergeFrom(Chain.Block other)` |
    | `Chain.Block.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Chain.Block.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Chain.Block.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Chain.Block.Builder` | `removeTransactions(int index)` `repeated .protocol.Transaction transactions = 1;` |
    | `Chain.Block.Builder` | `setBlockHeader(Chain.BlockHeader.Builder builderForValue)` `.protocol.BlockHeader block_header = 2;` |
    | `Chain.Block.Builder` | `setBlockHeader(Chain.BlockHeader value)` `.protocol.BlockHeader block_header = 2;` |
    | `Chain.Block.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Chain.Block.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Chain.Block.Builder` | `setTransactions(int index, Chain.Transaction.Builder builderForValue)` `repeated .protocol.Transaction transactions = 1;` |
    | `Chain.Block.Builder` | `setTransactions(int index, Chain.Transaction value)` `repeated .protocol.Transaction transactions = 1;` |
    | `Chain.Block.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Block.Builder>`
    - #### clear

      ```
      public Chain.Block.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Block.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Block.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Chain.Block getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Chain.Block build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Chain.Block buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Chain.Block.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Block.Builder>`
    - #### setField

      ```
      public Chain.Block.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                          java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Block.Builder>`
    - #### clearField

      ```
      public Chain.Block.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Block.Builder>`
    - #### clearOneof

      ```
      public Chain.Block.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Block.Builder>`
    - #### setRepeatedField

      ```
      public Chain.Block.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                  int index,
                                                  java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Block.Builder>`
    - #### addRepeatedField

      ```
      public Chain.Block.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                  java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Block.Builder>`
    - #### mergeFrom

      ```
      public Chain.Block.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Chain.Block.Builder>`
    - #### mergeFrom

      ```
      public Chain.Block.Builder mergeFrom(Chain.Block other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Block.Builder>`
    - #### mergeFrom

      ```
      public Chain.Block.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                    throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Chain.Block.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getTransactionsList

      ```
      public java.util.List<Chain.Transaction> getTransactionsList()
      ```

      `repeated .protocol.Transaction transactions = 1;`

      Specified by:
      :   `getTransactionsList` in interface `Chain.BlockOrBuilder`
    - #### getTransactionsCount

      ```
      public int getTransactionsCount()
      ```

      `repeated .protocol.Transaction transactions = 1;`

      Specified by:
      :   `getTransactionsCount` in interface `Chain.BlockOrBuilder`
    - #### getTransactions

      ```
      public Chain.Transaction getTransactions(int index)
      ```

      `repeated .protocol.Transaction transactions = 1;`

      Specified by:
      :   `getTransactions` in interface `Chain.BlockOrBuilder`
    - #### setTransactions

      ```
      public Chain.Block.Builder setTransactions(int index,
                                                 Chain.Transaction value)
      ```

      `repeated .protocol.Transaction transactions = 1;`
    - #### setTransactions

      ```
      public Chain.Block.Builder setTransactions(int index,
                                                 Chain.Transaction.Builder builderForValue)
      ```

      `repeated .protocol.Transaction transactions = 1;`
    - #### addTransactions

      ```
      public Chain.Block.Builder addTransactions(Chain.Transaction value)
      ```

      `repeated .protocol.Transaction transactions = 1;`
    - #### addTransactions

      ```
      public Chain.Block.Builder addTransactions(int index,
                                                 Chain.Transaction value)
      ```

      `repeated .protocol.Transaction transactions = 1;`
    - #### addTransactions

      ```
      public Chain.Block.Builder addTransactions(Chain.Transaction.Builder builderForValue)
      ```

      `repeated .protocol.Transaction transactions = 1;`
    - #### addTransactions

      ```
      public Chain.Block.Builder addTransactions(int index,
                                                 Chain.Transaction.Builder builderForValue)
      ```

      `repeated .protocol.Transaction transactions = 1;`
    - #### addAllTransactions

      ```
      public Chain.Block.Builder addAllTransactions(java.lang.Iterable<? extends Chain.Transaction> values)
      ```

      `repeated .protocol.Transaction transactions = 1;`
    - #### clearTransactions

      ```
      public Chain.Block.Builder clearTransactions()
      ```

      `repeated .protocol.Transaction transactions = 1;`
    - #### removeTransactions

      ```
      public Chain.Block.Builder removeTransactions(int index)
      ```

      `repeated .protocol.Transaction transactions = 1;`
    - #### getTransactionsBuilder

      ```
      public Chain.Transaction.Builder getTransactionsBuilder(int index)
      ```

      `repeated .protocol.Transaction transactions = 1;`
    - #### getTransactionsOrBuilder

      ```
      public Chain.TransactionOrBuilder getTransactionsOrBuilder(int index)
      ```

      `repeated .protocol.Transaction transactions = 1;`

      Specified by:
      :   `getTransactionsOrBuilder` in interface `Chain.BlockOrBuilder`
    - #### getTransactionsOrBuilderList

      ```
      public java.util.List<? extends Chain.TransactionOrBuilder> getTransactionsOrBuilderList()
      ```

      `repeated .protocol.Transaction transactions = 1;`

      Specified by:
      :   `getTransactionsOrBuilderList` in interface `Chain.BlockOrBuilder`
    - #### addTransactionsBuilder

      ```
      public Chain.Transaction.Builder addTransactionsBuilder()
      ```

      `repeated .protocol.Transaction transactions = 1;`
    - #### addTransactionsBuilder

      ```
      public Chain.Transaction.Builder addTransactionsBuilder(int index)
      ```

      `repeated .protocol.Transaction transactions = 1;`
    - #### getTransactionsBuilderList

      ```
      public java.util.List<Chain.Transaction.Builder> getTransactionsBuilderList()
      ```

      `repeated .protocol.Transaction transactions = 1;`
    - #### hasBlockHeader

      ```
      public boolean hasBlockHeader()
      ```

      `.protocol.BlockHeader block_header = 2;`

      Specified by:
      :   `hasBlockHeader` in interface `Chain.BlockOrBuilder`

      Returns:
      :   Whether the blockHeader field is set.
    - #### getBlockHeader

      ```
      public Chain.BlockHeader getBlockHeader()
      ```

      `.protocol.BlockHeader block_header = 2;`

      Specified by:
      :   `getBlockHeader` in interface `Chain.BlockOrBuilder`

      Returns:
      :   The blockHeader.
    - #### setBlockHeader

      ```
      public Chain.Block.Builder setBlockHeader(Chain.BlockHeader value)
      ```

      `.protocol.BlockHeader block_header = 2;`
    - #### setBlockHeader

      ```
      public Chain.Block.Builder setBlockHeader(Chain.BlockHeader.Builder builderForValue)
      ```

      `.protocol.BlockHeader block_header = 2;`
    - #### mergeBlockHeader

      ```
      public Chain.Block.Builder mergeBlockHeader(Chain.BlockHeader value)
      ```

      `.protocol.BlockHeader block_header = 2;`
    - #### clearBlockHeader

      ```
      public Chain.Block.Builder clearBlockHeader()
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
      :   `getBlockHeaderOrBuilder` in interface `Chain.BlockOrBuilder`
    - #### setUnknownFields

      ```
      public final Chain.Block.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Block.Builder>`
    - #### mergeUnknownFields

      ```
      public final Chain.Block.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Block.Builder>`