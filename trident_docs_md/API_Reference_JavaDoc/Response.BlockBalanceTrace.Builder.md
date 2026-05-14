

org.tron.trident.proto

## Class Response.BlockBalanceTrace.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.BlockBalanceTrace.Builder](../../../../org/tron/trident/proto/Response.BlockBalanceTrace.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.BlockBalanceTrace.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.BlockBalanceTraceOrBuilder](../../../../org/tron/trident/proto/Response.BlockBalanceTraceOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.BlockBalanceTrace](../../../../org/tron/trident/proto/Response.BlockBalanceTrace.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.BlockBalanceTrace.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockBalanceTrace.Builder>
  implements Response.BlockBalanceTraceOrBuilder
  ```

  Protobuf type `protocol.BlockBalanceTrace`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.BlockBalanceTrace.Builder` | `addAllTransactionBalanceTrace(java.lang.Iterable<? extends Response.TransactionBalanceTrace> values)` BlockIdentifier parent\_block\_identifier = 4; |
    | `Response.BlockBalanceTrace.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.BlockBalanceTrace.Builder` | `addTransactionBalanceTrace(int index, Response.TransactionBalanceTrace.Builder builderForValue)` BlockIdentifier parent\_block\_identifier = 4; |
    | `Response.BlockBalanceTrace.Builder` | `addTransactionBalanceTrace(int index, Response.TransactionBalanceTrace value)` BlockIdentifier parent\_block\_identifier = 4; |
    | `Response.BlockBalanceTrace.Builder` | `addTransactionBalanceTrace(Response.TransactionBalanceTrace.Builder builderForValue)` BlockIdentifier parent\_block\_identifier = 4; |
    | `Response.BlockBalanceTrace.Builder` | `addTransactionBalanceTrace(Response.TransactionBalanceTrace value)` BlockIdentifier parent\_block\_identifier = 4; |
    | `Response.TransactionBalanceTrace.Builder` | `addTransactionBalanceTraceBuilder()` BlockIdentifier parent\_block\_identifier = 4; |
    | `Response.TransactionBalanceTrace.Builder` | `addTransactionBalanceTraceBuilder(int index)` BlockIdentifier parent\_block\_identifier = 4; |
    | `Response.BlockBalanceTrace` | `build()` |
    | `Response.BlockBalanceTrace` | `buildPartial()` |
    | `Response.BlockBalanceTrace.Builder` | `clear()` |
    | `Response.BlockBalanceTrace.Builder` | `clearBlockIdentifier()` `.protocol.BlockIdentifier block_identifier = 1;` |
    | `Response.BlockBalanceTrace.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.BlockBalanceTrace.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.BlockBalanceTrace.Builder` | `clearTimestamp()` `int64 timestamp = 2;` |
    | `Response.BlockBalanceTrace.Builder` | `clearTransactionBalanceTrace()` BlockIdentifier parent\_block\_identifier = 4; |
    | `Response.BlockBalanceTrace.Builder` | `clone()` |
    | `Response.BlockIdentifier` | `getBlockIdentifier()` `.protocol.BlockIdentifier block_identifier = 1;` |
    | `Response.BlockIdentifier.Builder` | `getBlockIdentifierBuilder()` `.protocol.BlockIdentifier block_identifier = 1;` |
    | `Response.BlockIdentifierOrBuilder` | `getBlockIdentifierOrBuilder()` `.protocol.BlockIdentifier block_identifier = 1;` |
    | `Response.BlockBalanceTrace` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getTimestamp()` `int64 timestamp = 2;` |
    | `Response.TransactionBalanceTrace` | `getTransactionBalanceTrace(int index)` BlockIdentifier parent\_block\_identifier = 4; |
    | `Response.TransactionBalanceTrace.Builder` | `getTransactionBalanceTraceBuilder(int index)` BlockIdentifier parent\_block\_identifier = 4; |
    | `java.util.List<Response.TransactionBalanceTrace.Builder>` | `getTransactionBalanceTraceBuilderList()` BlockIdentifier parent\_block\_identifier = 4; |
    | `int` | `getTransactionBalanceTraceCount()` BlockIdentifier parent\_block\_identifier = 4; |
    | `java.util.List<Response.TransactionBalanceTrace>` | `getTransactionBalanceTraceList()` BlockIdentifier parent\_block\_identifier = 4; |
    | `Response.TransactionBalanceTraceOrBuilder` | `getTransactionBalanceTraceOrBuilder(int index)` BlockIdentifier parent\_block\_identifier = 4; |
    | `java.util.List<? extends Response.TransactionBalanceTraceOrBuilder>` | `getTransactionBalanceTraceOrBuilderList()` BlockIdentifier parent\_block\_identifier = 4; |
    | `boolean` | `hasBlockIdentifier()` `.protocol.BlockIdentifier block_identifier = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.BlockBalanceTrace.Builder` | `mergeBlockIdentifier(Response.BlockIdentifier value)` `.protocol.BlockIdentifier block_identifier = 1;` |
    | `Response.BlockBalanceTrace.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.BlockBalanceTrace.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.BlockBalanceTrace.Builder` | `mergeFrom(Response.BlockBalanceTrace other)` |
    | `Response.BlockBalanceTrace.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.BlockBalanceTrace.Builder` | `removeTransactionBalanceTrace(int index)` BlockIdentifier parent\_block\_identifier = 4; |
    | `Response.BlockBalanceTrace.Builder` | `setBlockIdentifier(Response.BlockIdentifier.Builder builderForValue)` `.protocol.BlockIdentifier block_identifier = 1;` |
    | `Response.BlockBalanceTrace.Builder` | `setBlockIdentifier(Response.BlockIdentifier value)` `.protocol.BlockIdentifier block_identifier = 1;` |
    | `Response.BlockBalanceTrace.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.BlockBalanceTrace.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.BlockBalanceTrace.Builder` | `setTimestamp(long value)` `int64 timestamp = 2;` |
    | `Response.BlockBalanceTrace.Builder` | `setTransactionBalanceTrace(int index, Response.TransactionBalanceTrace.Builder builderForValue)` BlockIdentifier parent\_block\_identifier = 4; |
    | `Response.BlockBalanceTrace.Builder` | `setTransactionBalanceTrace(int index, Response.TransactionBalanceTrace value)` BlockIdentifier parent\_block\_identifier = 4; |
    | `Response.BlockBalanceTrace.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockBalanceTrace.Builder>`
    - #### clear

      ```
      public Response.BlockBalanceTrace.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockBalanceTrace.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockBalanceTrace.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.BlockBalanceTrace getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.BlockBalanceTrace build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.BlockBalanceTrace buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.BlockBalanceTrace.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockBalanceTrace.Builder>`
    - #### setField

      ```
      public Response.BlockBalanceTrace.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                         java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockBalanceTrace.Builder>`
    - #### clearField

      ```
      public Response.BlockBalanceTrace.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockBalanceTrace.Builder>`
    - #### clearOneof

      ```
      public Response.BlockBalanceTrace.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockBalanceTrace.Builder>`
    - #### setRepeatedField

      ```
      public Response.BlockBalanceTrace.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                 int index,
                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockBalanceTrace.Builder>`
    - #### addRepeatedField

      ```
      public Response.BlockBalanceTrace.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockBalanceTrace.Builder>`
    - #### mergeFrom

      ```
      public Response.BlockBalanceTrace.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.BlockBalanceTrace.Builder>`
    - #### mergeFrom

      ```
      public Response.BlockBalanceTrace.Builder mergeFrom(Response.BlockBalanceTrace other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockBalanceTrace.Builder>`
    - #### mergeFrom

      ```
      public Response.BlockBalanceTrace.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.BlockBalanceTrace.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### hasBlockIdentifier

      ```
      public boolean hasBlockIdentifier()
      ```

      `.protocol.BlockIdentifier block_identifier = 1;`

      Specified by:
      :   `hasBlockIdentifier` in interface `Response.BlockBalanceTraceOrBuilder`

      Returns:
      :   Whether the blockIdentifier field is set.
    - #### getBlockIdentifier

      ```
      public Response.BlockIdentifier getBlockIdentifier()
      ```

      `.protocol.BlockIdentifier block_identifier = 1;`

      Specified by:
      :   `getBlockIdentifier` in interface `Response.BlockBalanceTraceOrBuilder`

      Returns:
      :   The blockIdentifier.
    - #### setBlockIdentifier

      ```
      public Response.BlockBalanceTrace.Builder setBlockIdentifier(Response.BlockIdentifier value)
      ```

      `.protocol.BlockIdentifier block_identifier = 1;`
    - #### setBlockIdentifier

      ```
      public Response.BlockBalanceTrace.Builder setBlockIdentifier(Response.BlockIdentifier.Builder builderForValue)
      ```

      `.protocol.BlockIdentifier block_identifier = 1;`
    - #### mergeBlockIdentifier

      ```
      public Response.BlockBalanceTrace.Builder mergeBlockIdentifier(Response.BlockIdentifier value)
      ```

      `.protocol.BlockIdentifier block_identifier = 1;`
    - #### clearBlockIdentifier

      ```
      public Response.BlockBalanceTrace.Builder clearBlockIdentifier()
      ```

      `.protocol.BlockIdentifier block_identifier = 1;`
    - #### getBlockIdentifierBuilder

      ```
      public Response.BlockIdentifier.Builder getBlockIdentifierBuilder()
      ```

      `.protocol.BlockIdentifier block_identifier = 1;`
    - #### getBlockIdentifierOrBuilder

      ```
      public Response.BlockIdentifierOrBuilder getBlockIdentifierOrBuilder()
      ```

      `.protocol.BlockIdentifier block_identifier = 1;`

      Specified by:
      :   `getBlockIdentifierOrBuilder` in interface `Response.BlockBalanceTraceOrBuilder`
    - #### getTimestamp

      ```
      public long getTimestamp()
      ```

      `int64 timestamp = 2;`

      Specified by:
      :   `getTimestamp` in interface `Response.BlockBalanceTraceOrBuilder`

      Returns:
      :   The timestamp.
    - #### setTimestamp

      ```
      public Response.BlockBalanceTrace.Builder setTimestamp(long value)
      ```

      `int64 timestamp = 2;`

      Parameters:
      :   `value` - The timestamp to set.

      Returns:
      :   This builder for chaining.
    - #### clearTimestamp

      ```
      public Response.BlockBalanceTrace.Builder clearTimestamp()
      ```

      `int64 timestamp = 2;`

      Returns:
      :   This builder for chaining.
    - #### getTransactionBalanceTraceList

      ```
      public java.util.List<Response.TransactionBalanceTrace> getTransactionBalanceTraceList()
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`

      Specified by:
      :   `getTransactionBalanceTraceList` in interface `Response.BlockBalanceTraceOrBuilder`
    - #### getTransactionBalanceTraceCount

      ```
      public int getTransactionBalanceTraceCount()
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`

      Specified by:
      :   `getTransactionBalanceTraceCount` in interface `Response.BlockBalanceTraceOrBuilder`
    - #### getTransactionBalanceTrace

      ```
      public Response.TransactionBalanceTrace getTransactionBalanceTrace(int index)
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`

      Specified by:
      :   `getTransactionBalanceTrace` in interface `Response.BlockBalanceTraceOrBuilder`
    - #### setTransactionBalanceTrace

      ```
      public Response.BlockBalanceTrace.Builder setTransactionBalanceTrace(int index,
                                                                           Response.TransactionBalanceTrace value)
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`
    - #### setTransactionBalanceTrace

      ```
      public Response.BlockBalanceTrace.Builder setTransactionBalanceTrace(int index,
                                                                           Response.TransactionBalanceTrace.Builder builderForValue)
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`
    - #### addTransactionBalanceTrace

      ```
      public Response.BlockBalanceTrace.Builder addTransactionBalanceTrace(Response.TransactionBalanceTrace value)
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`
    - #### addTransactionBalanceTrace

      ```
      public Response.BlockBalanceTrace.Builder addTransactionBalanceTrace(int index,
                                                                           Response.TransactionBalanceTrace value)
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`
    - #### addTransactionBalanceTrace

      ```
      public Response.BlockBalanceTrace.Builder addTransactionBalanceTrace(Response.TransactionBalanceTrace.Builder builderForValue)
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`
    - #### addTransactionBalanceTrace

      ```
      public Response.BlockBalanceTrace.Builder addTransactionBalanceTrace(int index,
                                                                           Response.TransactionBalanceTrace.Builder builderForValue)
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`
    - #### addAllTransactionBalanceTrace

      ```
      public Response.BlockBalanceTrace.Builder addAllTransactionBalanceTrace(java.lang.Iterable<? extends Response.TransactionBalanceTrace> values)
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`
    - #### clearTransactionBalanceTrace

      ```
      public Response.BlockBalanceTrace.Builder clearTransactionBalanceTrace()
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`
    - #### removeTransactionBalanceTrace

      ```
      public Response.BlockBalanceTrace.Builder removeTransactionBalanceTrace(int index)
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`
    - #### getTransactionBalanceTraceBuilder

      ```
      public Response.TransactionBalanceTrace.Builder getTransactionBalanceTraceBuilder(int index)
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`
    - #### getTransactionBalanceTraceOrBuilder

      ```
      public Response.TransactionBalanceTraceOrBuilder getTransactionBalanceTraceOrBuilder(int index)
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`

      Specified by:
      :   `getTransactionBalanceTraceOrBuilder` in interface `Response.BlockBalanceTraceOrBuilder`
    - #### getTransactionBalanceTraceOrBuilderList

      ```
      public java.util.List<? extends Response.TransactionBalanceTraceOrBuilder> getTransactionBalanceTraceOrBuilderList()
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`

      Specified by:
      :   `getTransactionBalanceTraceOrBuilderList` in interface `Response.BlockBalanceTraceOrBuilder`
    - #### addTransactionBalanceTraceBuilder

      ```
      public Response.TransactionBalanceTrace.Builder addTransactionBalanceTraceBuilder()
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`
    - #### addTransactionBalanceTraceBuilder

      ```
      public Response.TransactionBalanceTrace.Builder addTransactionBalanceTraceBuilder(int index)
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`
    - #### getTransactionBalanceTraceBuilderList

      ```
      public java.util.List<Response.TransactionBalanceTrace.Builder> getTransactionBalanceTraceBuilderList()
      ```

      ```
        BlockIdentifier parent_block_identifier = 4;
      ```

      `repeated .protocol.TransactionBalanceTrace transaction_balance_trace = 3;`
    - #### setUnknownFields

      ```
      public final Response.BlockBalanceTrace.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockBalanceTrace.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.BlockBalanceTrace.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.BlockBalanceTrace.Builder>`