

org.tron.trident.proto

## Class Response.DecryptNotesTRC20.NoteTx.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.DecryptNotesTRC20.NoteTx.Builder](../../../../org/tron/trident/proto/Response.DecryptNotesTRC20.NoteTx.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.DecryptNotesTRC20.NoteTx.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.DecryptNotesTRC20.NoteTxOrBuilder](../../../../org/tron/trident/proto/Response.DecryptNotesTRC20.NoteTxOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.DecryptNotesTRC20.NoteTx](../../../../org/tron/trident/proto/Response.DecryptNotesTRC20.NoteTx.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.DecryptNotesTRC20.NoteTx.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.NoteTx.Builder>
  implements Response.DecryptNotesTRC20.NoteTxOrBuilder
  ```

  Protobuf type `protocol.DecryptNotesTRC20.NoteTx`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.DecryptNotesTRC20.NoteTx` | `build()` |
    | `Response.DecryptNotesTRC20.NoteTx` | `buildPartial()` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `clear()` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `clearIndex()` the index of note in txid |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `clearIsSpent()` `bool is_spent = 3;` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `clearNote()` `.protocol.Note note = 1;` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `clearPosition()` `int64 position = 2;` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `clearToAmount()` `string to_amount = 6;` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `clearTransparentToAddress()` `bytes transparent_to_address = 7;` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `clearTxid()` `bytes txid = 4;` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `clone()` |
    | `Response.DecryptNotesTRC20.NoteTx` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `int` | `getIndex()` the index of note in txid |
    | `boolean` | `getIsSpent()` `bool is_spent = 3;` |
    | `Common.Note` | `getNote()` `.protocol.Note note = 1;` |
    | `Common.Note.Builder` | `getNoteBuilder()` `.protocol.Note note = 1;` |
    | `Common.NoteOrBuilder` | `getNoteOrBuilder()` `.protocol.Note note = 1;` |
    | `long` | `getPosition()` `int64 position = 2;` |
    | `java.lang.String` | `getToAmount()` `string to_amount = 6;` |
    | `com.google.protobuf.ByteString` | `getToAmountBytes()` `string to_amount = 6;` |
    | `com.google.protobuf.ByteString` | `getTransparentToAddress()` `bytes transparent_to_address = 7;` |
    | `com.google.protobuf.ByteString` | `getTxid()` `bytes txid = 4;` |
    | `boolean` | `hasNote()` `.protocol.Note note = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `mergeFrom(Response.DecryptNotesTRC20.NoteTx other)` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `mergeNote(Common.Note value)` `.protocol.Note note = 1;` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `setIndex(int value)` the index of note in txid |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `setIsSpent(boolean value)` `bool is_spent = 3;` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `setNote(Common.Note.Builder builderForValue)` `.protocol.Note note = 1;` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `setNote(Common.Note value)` `.protocol.Note note = 1;` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `setPosition(long value)` `int64 position = 2;` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `setToAmount(java.lang.String value)` `string to_amount = 6;` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `setToAmountBytes(com.google.protobuf.ByteString value)` `string to_amount = 6;` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `setTransparentToAddress(com.google.protobuf.ByteString value)` `bytes transparent_to_address = 7;` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `setTxid(com.google.protobuf.ByteString value)` `bytes txid = 4;` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.NoteTx.Builder>`
    - #### clear

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.NoteTx.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.NoteTx.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.DecryptNotesTRC20.NoteTx getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.DecryptNotesTRC20.NoteTx build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.DecryptNotesTRC20.NoteTx buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.NoteTx.Builder>`
    - #### setField

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.NoteTx.Builder>`
    - #### clearField

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.NoteTx.Builder>`
    - #### clearOneof

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.NoteTx.Builder>`
    - #### setRepeatedField

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                        int index,
                                                                        java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.NoteTx.Builder>`
    - #### addRepeatedField

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                        java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.NoteTx.Builder>`
    - #### mergeFrom

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.DecryptNotesTRC20.NoteTx.Builder>`
    - #### mergeFrom

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder mergeFrom(Response.DecryptNotesTRC20.NoteTx other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.NoteTx.Builder>`
    - #### mergeFrom

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                 com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                          throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.DecryptNotesTRC20.NoteTx.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### hasNote

      ```
      public boolean hasNote()
      ```

      `.protocol.Note note = 1;`

      Specified by:
      :   `hasNote` in interface `Response.DecryptNotesTRC20.NoteTxOrBuilder`

      Returns:
      :   Whether the note field is set.
    - #### getNote

      ```
      public Common.Note getNote()
      ```

      `.protocol.Note note = 1;`

      Specified by:
      :   `getNote` in interface `Response.DecryptNotesTRC20.NoteTxOrBuilder`

      Returns:
      :   The note.
    - #### setNote

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder setNote(Common.Note value)
      ```

      `.protocol.Note note = 1;`
    - #### setNote

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder setNote(Common.Note.Builder builderForValue)
      ```

      `.protocol.Note note = 1;`
    - #### mergeNote

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder mergeNote(Common.Note value)
      ```

      `.protocol.Note note = 1;`
    - #### clearNote

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder clearNote()
      ```

      `.protocol.Note note = 1;`
    - #### getNoteBuilder

      ```
      public Common.Note.Builder getNoteBuilder()
      ```

      `.protocol.Note note = 1;`
    - #### getNoteOrBuilder

      ```
      public Common.NoteOrBuilder getNoteOrBuilder()
      ```

      `.protocol.Note note = 1;`

      Specified by:
      :   `getNoteOrBuilder` in interface `Response.DecryptNotesTRC20.NoteTxOrBuilder`
    - #### getPosition

      ```
      public long getPosition()
      ```

      `int64 position = 2;`

      Specified by:
      :   `getPosition` in interface `Response.DecryptNotesTRC20.NoteTxOrBuilder`

      Returns:
      :   The position.
    - #### setPosition

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder setPosition(long value)
      ```

      `int64 position = 2;`

      Parameters:
      :   `value` - The position to set.

      Returns:
      :   This builder for chaining.
    - #### clearPosition

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder clearPosition()
      ```

      `int64 position = 2;`

      Returns:
      :   This builder for chaining.
    - #### getIsSpent

      ```
      public boolean getIsSpent()
      ```

      `bool is_spent = 3;`

      Specified by:
      :   `getIsSpent` in interface `Response.DecryptNotesTRC20.NoteTxOrBuilder`

      Returns:
      :   The isSpent.
    - #### setIsSpent

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder setIsSpent(boolean value)
      ```

      `bool is_spent = 3;`

      Parameters:
      :   `value` - The isSpent to set.

      Returns:
      :   This builder for chaining.
    - #### clearIsSpent

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder clearIsSpent()
      ```

      `bool is_spent = 3;`

      Returns:
      :   This builder for chaining.
    - #### getTxid

      ```
      public com.google.protobuf.ByteString getTxid()
      ```

      `bytes txid = 4;`

      Specified by:
      :   `getTxid` in interface `Response.DecryptNotesTRC20.NoteTxOrBuilder`

      Returns:
      :   The txid.
    - #### setTxid

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder setTxid(com.google.protobuf.ByteString value)
      ```

      `bytes txid = 4;`

      Parameters:
      :   `value` - The txid to set.

      Returns:
      :   This builder for chaining.
    - #### clearTxid

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder clearTxid()
      ```

      `bytes txid = 4;`

      Returns:
      :   This builder for chaining.
    - #### getIndex

      ```
      public int getIndex()
      ```

      ```
       the index of note in txid
      ```

      `int32 index = 5;`

      Specified by:
      :   `getIndex` in interface `Response.DecryptNotesTRC20.NoteTxOrBuilder`

      Returns:
      :   The index.
    - #### setIndex

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder setIndex(int value)
      ```

      ```
       the index of note in txid
      ```

      `int32 index = 5;`

      Parameters:
      :   `value` - The index to set.

      Returns:
      :   This builder for chaining.
    - #### clearIndex

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder clearIndex()
      ```

      ```
       the index of note in txid
      ```

      `int32 index = 5;`

      Returns:
      :   This builder for chaining.
    - #### getToAmount

      ```
      public java.lang.String getToAmount()
      ```

      `string to_amount = 6;`

      Specified by:
      :   `getToAmount` in interface `Response.DecryptNotesTRC20.NoteTxOrBuilder`

      Returns:
      :   The toAmount.
    - #### getToAmountBytes

      ```
      public com.google.protobuf.ByteString getToAmountBytes()
      ```

      `string to_amount = 6;`

      Specified by:
      :   `getToAmountBytes` in interface `Response.DecryptNotesTRC20.NoteTxOrBuilder`

      Returns:
      :   The bytes for toAmount.
    - #### setToAmount

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder setToAmount(java.lang.String value)
      ```

      `string to_amount = 6;`

      Parameters:
      :   `value` - The toAmount to set.

      Returns:
      :   This builder for chaining.
    - #### clearToAmount

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder clearToAmount()
      ```

      `string to_amount = 6;`

      Returns:
      :   This builder for chaining.
    - #### setToAmountBytes

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder setToAmountBytes(com.google.protobuf.ByteString value)
      ```

      `string to_amount = 6;`

      Parameters:
      :   `value` - The bytes for toAmount to set.

      Returns:
      :   This builder for chaining.
    - #### getTransparentToAddress

      ```
      public com.google.protobuf.ByteString getTransparentToAddress()
      ```

      `bytes transparent_to_address = 7;`

      Specified by:
      :   `getTransparentToAddress` in interface `Response.DecryptNotesTRC20.NoteTxOrBuilder`

      Returns:
      :   The transparentToAddress.
    - #### setTransparentToAddress

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder setTransparentToAddress(com.google.protobuf.ByteString value)
      ```

      `bytes transparent_to_address = 7;`

      Parameters:
      :   `value` - The transparentToAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearTransparentToAddress

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder clearTransparentToAddress()
      ```

      `bytes transparent_to_address = 7;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.DecryptNotesTRC20.NoteTx.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.NoteTx.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.DecryptNotesTRC20.NoteTx.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.NoteTx.Builder>`