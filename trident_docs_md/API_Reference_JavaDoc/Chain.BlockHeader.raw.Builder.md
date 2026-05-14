

org.tron.trident.proto

## Class Chain.BlockHeader.raw.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Chain.BlockHeader.raw.Builder](../../../../org/tron/trident/proto/Chain.BlockHeader.raw.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Chain.BlockHeader.raw.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Chain.BlockHeader.rawOrBuilder](../../../../org/tron/trident/proto/Chain.BlockHeader.rawOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Chain.BlockHeader.raw](../../../../org/tron/trident/proto/Chain.BlockHeader.raw.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Chain.BlockHeader.raw.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.raw.Builder>
  implements Chain.BlockHeader.rawOrBuilder
  ```

  Protobuf type `protocol.BlockHeader.raw`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Chain.BlockHeader.raw.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Chain.BlockHeader.raw` | `build()` |
    | `Chain.BlockHeader.raw` | `buildPartial()` |
    | `Chain.BlockHeader.raw.Builder` | `clear()` |
    | `Chain.BlockHeader.raw.Builder` | `clearAccountStateRoot()` `bytes accountStateRoot = 11;` |
    | `Chain.BlockHeader.raw.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Chain.BlockHeader.raw.Builder` | `clearNumber()` bytes nonce = 5; bytes difficulty = 6; |
    | `Chain.BlockHeader.raw.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Chain.BlockHeader.raw.Builder` | `clearParentHash()` `bytes parentHash = 3;` |
    | `Chain.BlockHeader.raw.Builder` | `clearTimestamp()` `int64 timestamp = 1;` |
    | `Chain.BlockHeader.raw.Builder` | `clearTxTrieRoot()` `bytes txTrieRoot = 2;` |
    | `Chain.BlockHeader.raw.Builder` | `clearVersion()` `int32 version = 10;` |
    | `Chain.BlockHeader.raw.Builder` | `clearWitnessAddress()` `bytes witness_address = 9;` |
    | `Chain.BlockHeader.raw.Builder` | `clearWitnessId()` `int64 witness_id = 8;` |
    | `Chain.BlockHeader.raw.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getAccountStateRoot()` `bytes accountStateRoot = 11;` |
    | `Chain.BlockHeader.raw` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getNumber()` bytes nonce = 5; bytes difficulty = 6; |
    | `com.google.protobuf.ByteString` | `getParentHash()` `bytes parentHash = 3;` |
    | `long` | `getTimestamp()` `int64 timestamp = 1;` |
    | `com.google.protobuf.ByteString` | `getTxTrieRoot()` `bytes txTrieRoot = 2;` |
    | `int` | `getVersion()` `int32 version = 10;` |
    | `com.google.protobuf.ByteString` | `getWitnessAddress()` `bytes witness_address = 9;` |
    | `long` | `getWitnessId()` `int64 witness_id = 8;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Chain.BlockHeader.raw.Builder` | `mergeFrom(Chain.BlockHeader.raw other)` |
    | `Chain.BlockHeader.raw.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Chain.BlockHeader.raw.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Chain.BlockHeader.raw.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Chain.BlockHeader.raw.Builder` | `setAccountStateRoot(com.google.protobuf.ByteString value)` `bytes accountStateRoot = 11;` |
    | `Chain.BlockHeader.raw.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Chain.BlockHeader.raw.Builder` | `setNumber(long value)` bytes nonce = 5; bytes difficulty = 6; |
    | `Chain.BlockHeader.raw.Builder` | `setParentHash(com.google.protobuf.ByteString value)` `bytes parentHash = 3;` |
    | `Chain.BlockHeader.raw.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Chain.BlockHeader.raw.Builder` | `setTimestamp(long value)` `int64 timestamp = 1;` |
    | `Chain.BlockHeader.raw.Builder` | `setTxTrieRoot(com.google.protobuf.ByteString value)` `bytes txTrieRoot = 2;` |
    | `Chain.BlockHeader.raw.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Chain.BlockHeader.raw.Builder` | `setVersion(int value)` `int32 version = 10;` |
    | `Chain.BlockHeader.raw.Builder` | `setWitnessAddress(com.google.protobuf.ByteString value)` `bytes witness_address = 9;` |
    | `Chain.BlockHeader.raw.Builder` | `setWitnessId(long value)` `int64 witness_id = 8;` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.raw.Builder>`
    - #### clear

      ```
      public Chain.BlockHeader.raw.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.raw.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.raw.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Chain.BlockHeader.raw getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Chain.BlockHeader.raw build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Chain.BlockHeader.raw buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Chain.BlockHeader.raw.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.raw.Builder>`
    - #### setField

      ```
      public Chain.BlockHeader.raw.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                    java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.raw.Builder>`
    - #### clearField

      ```
      public Chain.BlockHeader.raw.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.raw.Builder>`
    - #### clearOneof

      ```
      public Chain.BlockHeader.raw.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.raw.Builder>`
    - #### setRepeatedField

      ```
      public Chain.BlockHeader.raw.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                            int index,
                                                            java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.raw.Builder>`
    - #### addRepeatedField

      ```
      public Chain.BlockHeader.raw.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                            java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.raw.Builder>`
    - #### mergeFrom

      ```
      public Chain.BlockHeader.raw.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Chain.BlockHeader.raw.Builder>`
    - #### mergeFrom

      ```
      public Chain.BlockHeader.raw.Builder mergeFrom(Chain.BlockHeader.raw other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.raw.Builder>`
    - #### mergeFrom

      ```
      public Chain.BlockHeader.raw.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                     com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                              throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Chain.BlockHeader.raw.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getTimestamp

      ```
      public long getTimestamp()
      ```

      `int64 timestamp = 1;`

      Specified by:
      :   `getTimestamp` in interface `Chain.BlockHeader.rawOrBuilder`

      Returns:
      :   The timestamp.
    - #### setTimestamp

      ```
      public Chain.BlockHeader.raw.Builder setTimestamp(long value)
      ```

      `int64 timestamp = 1;`

      Parameters:
      :   `value` - The timestamp to set.

      Returns:
      :   This builder for chaining.
    - #### clearTimestamp

      ```
      public Chain.BlockHeader.raw.Builder clearTimestamp()
      ```

      `int64 timestamp = 1;`

      Returns:
      :   This builder for chaining.
    - #### getTxTrieRoot

      ```
      public com.google.protobuf.ByteString getTxTrieRoot()
      ```

      `bytes txTrieRoot = 2;`

      Specified by:
      :   `getTxTrieRoot` in interface `Chain.BlockHeader.rawOrBuilder`

      Returns:
      :   The txTrieRoot.
    - #### setTxTrieRoot

      ```
      public Chain.BlockHeader.raw.Builder setTxTrieRoot(com.google.protobuf.ByteString value)
      ```

      `bytes txTrieRoot = 2;`

      Parameters:
      :   `value` - The txTrieRoot to set.

      Returns:
      :   This builder for chaining.
    - #### clearTxTrieRoot

      ```
      public Chain.BlockHeader.raw.Builder clearTxTrieRoot()
      ```

      `bytes txTrieRoot = 2;`

      Returns:
      :   This builder for chaining.
    - #### getParentHash

      ```
      public com.google.protobuf.ByteString getParentHash()
      ```

      `bytes parentHash = 3;`

      Specified by:
      :   `getParentHash` in interface `Chain.BlockHeader.rawOrBuilder`

      Returns:
      :   The parentHash.
    - #### setParentHash

      ```
      public Chain.BlockHeader.raw.Builder setParentHash(com.google.protobuf.ByteString value)
      ```

      `bytes parentHash = 3;`

      Parameters:
      :   `value` - The parentHash to set.

      Returns:
      :   This builder for chaining.
    - #### clearParentHash

      ```
      public Chain.BlockHeader.raw.Builder clearParentHash()
      ```

      `bytes parentHash = 3;`

      Returns:
      :   This builder for chaining.
    - #### getNumber

      ```
      public long getNumber()
      ```

      ```
       bytes nonce = 5;
       bytes difficulty = 6;
      ```

      `int64 number = 7;`

      Specified by:
      :   `getNumber` in interface `Chain.BlockHeader.rawOrBuilder`

      Returns:
      :   The number.
    - #### setNumber

      ```
      public Chain.BlockHeader.raw.Builder setNumber(long value)
      ```

      ```
       bytes nonce = 5;
       bytes difficulty = 6;
      ```

      `int64 number = 7;`

      Parameters:
      :   `value` - The number to set.

      Returns:
      :   This builder for chaining.
    - #### clearNumber

      ```
      public Chain.BlockHeader.raw.Builder clearNumber()
      ```

      ```
       bytes nonce = 5;
       bytes difficulty = 6;
      ```

      `int64 number = 7;`

      Returns:
      :   This builder for chaining.
    - #### getWitnessId

      ```
      public long getWitnessId()
      ```

      `int64 witness_id = 8;`

      Specified by:
      :   `getWitnessId` in interface `Chain.BlockHeader.rawOrBuilder`

      Returns:
      :   The witnessId.
    - #### setWitnessId

      ```
      public Chain.BlockHeader.raw.Builder setWitnessId(long value)
      ```

      `int64 witness_id = 8;`

      Parameters:
      :   `value` - The witnessId to set.

      Returns:
      :   This builder for chaining.
    - #### clearWitnessId

      ```
      public Chain.BlockHeader.raw.Builder clearWitnessId()
      ```

      `int64 witness_id = 8;`

      Returns:
      :   This builder for chaining.
    - #### getWitnessAddress

      ```
      public com.google.protobuf.ByteString getWitnessAddress()
      ```

      `bytes witness_address = 9;`

      Specified by:
      :   `getWitnessAddress` in interface `Chain.BlockHeader.rawOrBuilder`

      Returns:
      :   The witnessAddress.
    - #### setWitnessAddress

      ```
      public Chain.BlockHeader.raw.Builder setWitnessAddress(com.google.protobuf.ByteString value)
      ```

      `bytes witness_address = 9;`

      Parameters:
      :   `value` - The witnessAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearWitnessAddress

      ```
      public Chain.BlockHeader.raw.Builder clearWitnessAddress()
      ```

      `bytes witness_address = 9;`

      Returns:
      :   This builder for chaining.
    - #### getVersion

      ```
      public int getVersion()
      ```

      `int32 version = 10;`

      Specified by:
      :   `getVersion` in interface `Chain.BlockHeader.rawOrBuilder`

      Returns:
      :   The version.
    - #### setVersion

      ```
      public Chain.BlockHeader.raw.Builder setVersion(int value)
      ```

      `int32 version = 10;`

      Parameters:
      :   `value` - The version to set.

      Returns:
      :   This builder for chaining.
    - #### clearVersion

      ```
      public Chain.BlockHeader.raw.Builder clearVersion()
      ```

      `int32 version = 10;`

      Returns:
      :   This builder for chaining.
    - #### getAccountStateRoot

      ```
      public com.google.protobuf.ByteString getAccountStateRoot()
      ```

      `bytes accountStateRoot = 11;`

      Specified by:
      :   `getAccountStateRoot` in interface `Chain.BlockHeader.rawOrBuilder`

      Returns:
      :   The accountStateRoot.
    - #### setAccountStateRoot

      ```
      public Chain.BlockHeader.raw.Builder setAccountStateRoot(com.google.protobuf.ByteString value)
      ```

      `bytes accountStateRoot = 11;`

      Parameters:
      :   `value` - The accountStateRoot to set.

      Returns:
      :   This builder for chaining.
    - #### clearAccountStateRoot

      ```
      public Chain.BlockHeader.raw.Builder clearAccountStateRoot()
      ```

      `bytes accountStateRoot = 11;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Chain.BlockHeader.raw.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.raw.Builder>`
    - #### mergeUnknownFields

      ```
      public final Chain.BlockHeader.raw.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.raw.Builder>`