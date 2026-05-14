

org.tron.trident.proto

## Class Chain.Transaction.raw.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Chain.Transaction.raw.Builder](../../../../org/tron/trident/proto/Chain.Transaction.raw.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Chain.Transaction.raw.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Chain.Transaction.rawOrBuilder](../../../../org/tron/trident/proto/Chain.Transaction.rawOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Chain.Transaction.raw](../../../../org/tron/trident/proto/Chain.Transaction.raw.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Chain.Transaction.raw.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.raw.Builder>
  implements Chain.Transaction.rawOrBuilder
  ```

  Protobuf type `protocol.Transaction.raw`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Chain.Transaction.raw.Builder` | `addAllAuths(java.lang.Iterable<? extends Common.authority> values)` `repeated .protocol.authority auths = 9;` |
    | `Chain.Transaction.raw.Builder` | `addAllContract(java.lang.Iterable<? extends Chain.Transaction.Contract> values)` only support size = 1, repeated list here for extension |
    | `Chain.Transaction.raw.Builder` | `addAuths(Common.authority.Builder builderForValue)` `repeated .protocol.authority auths = 9;` |
    | `Chain.Transaction.raw.Builder` | `addAuths(Common.authority value)` `repeated .protocol.authority auths = 9;` |
    | `Chain.Transaction.raw.Builder` | `addAuths(int index, Common.authority.Builder builderForValue)` `repeated .protocol.authority auths = 9;` |
    | `Chain.Transaction.raw.Builder` | `addAuths(int index, Common.authority value)` `repeated .protocol.authority auths = 9;` |
    | `Common.authority.Builder` | `addAuthsBuilder()` `repeated .protocol.authority auths = 9;` |
    | `Common.authority.Builder` | `addAuthsBuilder(int index)` `repeated .protocol.authority auths = 9;` |
    | `Chain.Transaction.raw.Builder` | `addContract(Chain.Transaction.Contract.Builder builderForValue)` only support size = 1, repeated list here for extension |
    | `Chain.Transaction.raw.Builder` | `addContract(Chain.Transaction.Contract value)` only support size = 1, repeated list here for extension |
    | `Chain.Transaction.raw.Builder` | `addContract(int index, Chain.Transaction.Contract.Builder builderForValue)` only support size = 1, repeated list here for extension |
    | `Chain.Transaction.raw.Builder` | `addContract(int index, Chain.Transaction.Contract value)` only support size = 1, repeated list here for extension |
    | `Chain.Transaction.Contract.Builder` | `addContractBuilder()` only support size = 1, repeated list here for extension |
    | `Chain.Transaction.Contract.Builder` | `addContractBuilder(int index)` only support size = 1, repeated list here for extension |
    | `Chain.Transaction.raw.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Chain.Transaction.raw` | `build()` |
    | `Chain.Transaction.raw` | `buildPartial()` |
    | `Chain.Transaction.raw.Builder` | `clear()` |
    | `Chain.Transaction.raw.Builder` | `clearAuths()` `repeated .protocol.authority auths = 9;` |
    | `Chain.Transaction.raw.Builder` | `clearContract()` only support size = 1, repeated list here for extension |
    | `Chain.Transaction.raw.Builder` | `clearData()` data not used |
    | `Chain.Transaction.raw.Builder` | `clearExpiration()` `int64 expiration = 8;` |
    | `Chain.Transaction.raw.Builder` | `clearFeeLimit()` `int64 fee_limit = 18;` |
    | `Chain.Transaction.raw.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Chain.Transaction.raw.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Chain.Transaction.raw.Builder` | `clearRefBlockBytes()` `bytes ref_block_bytes = 1;` |
    | `Chain.Transaction.raw.Builder` | `clearRefBlockHash()` `bytes ref_block_hash = 4;` |
    | `Chain.Transaction.raw.Builder` | `clearRefBlockNum()` `int64 ref_block_num = 3;` |
    | `Chain.Transaction.raw.Builder` | `clearScripts()` scripts not used |
    | `Chain.Transaction.raw.Builder` | `clearTimestamp()` `int64 timestamp = 14;` |
    | `Chain.Transaction.raw.Builder` | `clone()` |
    | `Common.authority` | `getAuths(int index)` `repeated .protocol.authority auths = 9;` |
    | `Common.authority.Builder` | `getAuthsBuilder(int index)` `repeated .protocol.authority auths = 9;` |
    | `java.util.List<Common.authority.Builder>` | `getAuthsBuilderList()` `repeated .protocol.authority auths = 9;` |
    | `int` | `getAuthsCount()` `repeated .protocol.authority auths = 9;` |
    | `java.util.List<Common.authority>` | `getAuthsList()` `repeated .protocol.authority auths = 9;` |
    | `Common.authorityOrBuilder` | `getAuthsOrBuilder(int index)` `repeated .protocol.authority auths = 9;` |
    | `java.util.List<? extends Common.authorityOrBuilder>` | `getAuthsOrBuilderList()` `repeated .protocol.authority auths = 9;` |
    | `Chain.Transaction.Contract` | `getContract(int index)` only support size = 1, repeated list here for extension |
    | `Chain.Transaction.Contract.Builder` | `getContractBuilder(int index)` only support size = 1, repeated list here for extension |
    | `java.util.List<Chain.Transaction.Contract.Builder>` | `getContractBuilderList()` only support size = 1, repeated list here for extension |
    | `int` | `getContractCount()` only support size = 1, repeated list here for extension |
    | `java.util.List<Chain.Transaction.Contract>` | `getContractList()` only support size = 1, repeated list here for extension |
    | `Chain.Transaction.ContractOrBuilder` | `getContractOrBuilder(int index)` only support size = 1, repeated list here for extension |
    | `java.util.List<? extends Chain.Transaction.ContractOrBuilder>` | `getContractOrBuilderList()` only support size = 1, repeated list here for extension |
    | `com.google.protobuf.ByteString` | `getData()` data not used |
    | `Chain.Transaction.raw` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getExpiration()` `int64 expiration = 8;` |
    | `long` | `getFeeLimit()` `int64 fee_limit = 18;` |
    | `com.google.protobuf.ByteString` | `getRefBlockBytes()` `bytes ref_block_bytes = 1;` |
    | `com.google.protobuf.ByteString` | `getRefBlockHash()` `bytes ref_block_hash = 4;` |
    | `long` | `getRefBlockNum()` `int64 ref_block_num = 3;` |
    | `com.google.protobuf.ByteString` | `getScripts()` scripts not used |
    | `long` | `getTimestamp()` `int64 timestamp = 14;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Chain.Transaction.raw.Builder` | `mergeFrom(Chain.Transaction.raw other)` |
    | `Chain.Transaction.raw.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Chain.Transaction.raw.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Chain.Transaction.raw.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Chain.Transaction.raw.Builder` | `removeAuths(int index)` `repeated .protocol.authority auths = 9;` |
    | `Chain.Transaction.raw.Builder` | `removeContract(int index)` only support size = 1, repeated list here for extension |
    | `Chain.Transaction.raw.Builder` | `setAuths(int index, Common.authority.Builder builderForValue)` `repeated .protocol.authority auths = 9;` |
    | `Chain.Transaction.raw.Builder` | `setAuths(int index, Common.authority value)` `repeated .protocol.authority auths = 9;` |
    | `Chain.Transaction.raw.Builder` | `setContract(int index, Chain.Transaction.Contract.Builder builderForValue)` only support size = 1, repeated list here for extension |
    | `Chain.Transaction.raw.Builder` | `setContract(int index, Chain.Transaction.Contract value)` only support size = 1, repeated list here for extension |
    | `Chain.Transaction.raw.Builder` | `setData(com.google.protobuf.ByteString value)` data not used |
    | `Chain.Transaction.raw.Builder` | `setExpiration(long value)` `int64 expiration = 8;` |
    | `Chain.Transaction.raw.Builder` | `setFeeLimit(long value)` `int64 fee_limit = 18;` |
    | `Chain.Transaction.raw.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Chain.Transaction.raw.Builder` | `setRefBlockBytes(com.google.protobuf.ByteString value)` `bytes ref_block_bytes = 1;` |
    | `Chain.Transaction.raw.Builder` | `setRefBlockHash(com.google.protobuf.ByteString value)` `bytes ref_block_hash = 4;` |
    | `Chain.Transaction.raw.Builder` | `setRefBlockNum(long value)` `int64 ref_block_num = 3;` |
    | `Chain.Transaction.raw.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Chain.Transaction.raw.Builder` | `setScripts(com.google.protobuf.ByteString value)` scripts not used |
    | `Chain.Transaction.raw.Builder` | `setTimestamp(long value)` `int64 timestamp = 14;` |
    | `Chain.Transaction.raw.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.raw.Builder>`
    - #### clear

      ```
      public Chain.Transaction.raw.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.raw.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.raw.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Chain.Transaction.raw getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Chain.Transaction.raw build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Chain.Transaction.raw buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Chain.Transaction.raw.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.raw.Builder>`
    - #### setField

      ```
      public Chain.Transaction.raw.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                    java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.raw.Builder>`
    - #### clearField

      ```
      public Chain.Transaction.raw.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.raw.Builder>`
    - #### clearOneof

      ```
      public Chain.Transaction.raw.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.raw.Builder>`
    - #### setRepeatedField

      ```
      public Chain.Transaction.raw.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                            int index,
                                                            java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.raw.Builder>`
    - #### addRepeatedField

      ```
      public Chain.Transaction.raw.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                            java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.raw.Builder>`
    - #### mergeFrom

      ```
      public Chain.Transaction.raw.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Chain.Transaction.raw.Builder>`
    - #### mergeFrom

      ```
      public Chain.Transaction.raw.Builder mergeFrom(Chain.Transaction.raw other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.raw.Builder>`
    - #### mergeFrom

      ```
      public Chain.Transaction.raw.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                     com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                              throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Chain.Transaction.raw.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getRefBlockBytes

      ```
      public com.google.protobuf.ByteString getRefBlockBytes()
      ```

      `bytes ref_block_bytes = 1;`

      Specified by:
      :   `getRefBlockBytes` in interface `Chain.Transaction.rawOrBuilder`

      Returns:
      :   The refBlockBytes.
    - #### setRefBlockBytes

      ```
      public Chain.Transaction.raw.Builder setRefBlockBytes(com.google.protobuf.ByteString value)
      ```

      `bytes ref_block_bytes = 1;`

      Parameters:
      :   `value` - The refBlockBytes to set.

      Returns:
      :   This builder for chaining.
    - #### clearRefBlockBytes

      ```
      public Chain.Transaction.raw.Builder clearRefBlockBytes()
      ```

      `bytes ref_block_bytes = 1;`

      Returns:
      :   This builder for chaining.
    - #### getRefBlockNum

      ```
      public long getRefBlockNum()
      ```

      `int64 ref_block_num = 3;`

      Specified by:
      :   `getRefBlockNum` in interface `Chain.Transaction.rawOrBuilder`

      Returns:
      :   The refBlockNum.
    - #### setRefBlockNum

      ```
      public Chain.Transaction.raw.Builder setRefBlockNum(long value)
      ```

      `int64 ref_block_num = 3;`

      Parameters:
      :   `value` - The refBlockNum to set.

      Returns:
      :   This builder for chaining.
    - #### clearRefBlockNum

      ```
      public Chain.Transaction.raw.Builder clearRefBlockNum()
      ```

      `int64 ref_block_num = 3;`

      Returns:
      :   This builder for chaining.
    - #### getRefBlockHash

      ```
      public com.google.protobuf.ByteString getRefBlockHash()
      ```

      `bytes ref_block_hash = 4;`

      Specified by:
      :   `getRefBlockHash` in interface `Chain.Transaction.rawOrBuilder`

      Returns:
      :   The refBlockHash.
    - #### setRefBlockHash

      ```
      public Chain.Transaction.raw.Builder setRefBlockHash(com.google.protobuf.ByteString value)
      ```

      `bytes ref_block_hash = 4;`

      Parameters:
      :   `value` - The refBlockHash to set.

      Returns:
      :   This builder for chaining.
    - #### clearRefBlockHash

      ```
      public Chain.Transaction.raw.Builder clearRefBlockHash()
      ```

      `bytes ref_block_hash = 4;`

      Returns:
      :   This builder for chaining.
    - #### getExpiration

      ```
      public long getExpiration()
      ```

      `int64 expiration = 8;`

      Specified by:
      :   `getExpiration` in interface `Chain.Transaction.rawOrBuilder`

      Returns:
      :   The expiration.
    - #### setExpiration

      ```
      public Chain.Transaction.raw.Builder setExpiration(long value)
      ```

      `int64 expiration = 8;`

      Parameters:
      :   `value` - The expiration to set.

      Returns:
      :   This builder for chaining.
    - #### clearExpiration

      ```
      public Chain.Transaction.raw.Builder clearExpiration()
      ```

      `int64 expiration = 8;`

      Returns:
      :   This builder for chaining.
    - #### getAuthsList

      ```
      public java.util.List<Common.authority> getAuthsList()
      ```

      `repeated .protocol.authority auths = 9;`

      Specified by:
      :   `getAuthsList` in interface `Chain.Transaction.rawOrBuilder`
    - #### getAuthsCount

      ```
      public int getAuthsCount()
      ```

      `repeated .protocol.authority auths = 9;`

      Specified by:
      :   `getAuthsCount` in interface `Chain.Transaction.rawOrBuilder`
    - #### getAuths

      ```
      public Common.authority getAuths(int index)
      ```

      `repeated .protocol.authority auths = 9;`

      Specified by:
      :   `getAuths` in interface `Chain.Transaction.rawOrBuilder`
    - #### setAuths

      ```
      public Chain.Transaction.raw.Builder setAuths(int index,
                                                    Common.authority value)
      ```

      `repeated .protocol.authority auths = 9;`
    - #### setAuths

      ```
      public Chain.Transaction.raw.Builder setAuths(int index,
                                                    Common.authority.Builder builderForValue)
      ```

      `repeated .protocol.authority auths = 9;`
    - #### addAuths

      ```
      public Chain.Transaction.raw.Builder addAuths(Common.authority value)
      ```

      `repeated .protocol.authority auths = 9;`
    - #### addAuths

      ```
      public Chain.Transaction.raw.Builder addAuths(int index,
                                                    Common.authority value)
      ```

      `repeated .protocol.authority auths = 9;`
    - #### addAuths

      ```
      public Chain.Transaction.raw.Builder addAuths(Common.authority.Builder builderForValue)
      ```

      `repeated .protocol.authority auths = 9;`
    - #### addAuths

      ```
      public Chain.Transaction.raw.Builder addAuths(int index,
                                                    Common.authority.Builder builderForValue)
      ```

      `repeated .protocol.authority auths = 9;`
    - #### addAllAuths

      ```
      public Chain.Transaction.raw.Builder addAllAuths(java.lang.Iterable<? extends Common.authority> values)
      ```

      `repeated .protocol.authority auths = 9;`
    - #### clearAuths

      ```
      public Chain.Transaction.raw.Builder clearAuths()
      ```

      `repeated .protocol.authority auths = 9;`
    - #### removeAuths

      ```
      public Chain.Transaction.raw.Builder removeAuths(int index)
      ```

      `repeated .protocol.authority auths = 9;`
    - #### getAuthsBuilder

      ```
      public Common.authority.Builder getAuthsBuilder(int index)
      ```

      `repeated .protocol.authority auths = 9;`
    - #### getAuthsOrBuilder

      ```
      public Common.authorityOrBuilder getAuthsOrBuilder(int index)
      ```

      `repeated .protocol.authority auths = 9;`

      Specified by:
      :   `getAuthsOrBuilder` in interface `Chain.Transaction.rawOrBuilder`
    - #### getAuthsOrBuilderList

      ```
      public java.util.List<? extends Common.authorityOrBuilder> getAuthsOrBuilderList()
      ```

      `repeated .protocol.authority auths = 9;`

      Specified by:
      :   `getAuthsOrBuilderList` in interface `Chain.Transaction.rawOrBuilder`
    - #### addAuthsBuilder

      ```
      public Common.authority.Builder addAuthsBuilder()
      ```

      `repeated .protocol.authority auths = 9;`
    - #### addAuthsBuilder

      ```
      public Common.authority.Builder addAuthsBuilder(int index)
      ```

      `repeated .protocol.authority auths = 9;`
    - #### getAuthsBuilderList

      ```
      public java.util.List<Common.authority.Builder> getAuthsBuilderList()
      ```

      `repeated .protocol.authority auths = 9;`
    - #### getData

      ```
      public com.google.protobuf.ByteString getData()
      ```

      ```
       data not used
      ```

      `bytes data = 10;`

      Specified by:
      :   `getData` in interface `Chain.Transaction.rawOrBuilder`

      Returns:
      :   The data.
    - #### setData

      ```
      public Chain.Transaction.raw.Builder setData(com.google.protobuf.ByteString value)
      ```

      ```
       data not used
      ```

      `bytes data = 10;`

      Parameters:
      :   `value` - The data to set.

      Returns:
      :   This builder for chaining.
    - #### clearData

      ```
      public Chain.Transaction.raw.Builder clearData()
      ```

      ```
       data not used
      ```

      `bytes data = 10;`

      Returns:
      :   This builder for chaining.
    - #### getContractList

      ```
      public java.util.List<Chain.Transaction.Contract> getContractList()
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`

      Specified by:
      :   `getContractList` in interface `Chain.Transaction.rawOrBuilder`
    - #### getContractCount

      ```
      public int getContractCount()
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`

      Specified by:
      :   `getContractCount` in interface `Chain.Transaction.rawOrBuilder`
    - #### getContract

      ```
      public Chain.Transaction.Contract getContract(int index)
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`

      Specified by:
      :   `getContract` in interface `Chain.Transaction.rawOrBuilder`
    - #### setContract

      ```
      public Chain.Transaction.raw.Builder setContract(int index,
                                                       Chain.Transaction.Contract value)
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`
    - #### setContract

      ```
      public Chain.Transaction.raw.Builder setContract(int index,
                                                       Chain.Transaction.Contract.Builder builderForValue)
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`
    - #### addContract

      ```
      public Chain.Transaction.raw.Builder addContract(Chain.Transaction.Contract value)
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`
    - #### addContract

      ```
      public Chain.Transaction.raw.Builder addContract(int index,
                                                       Chain.Transaction.Contract value)
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`
    - #### addContract

      ```
      public Chain.Transaction.raw.Builder addContract(Chain.Transaction.Contract.Builder builderForValue)
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`
    - #### addContract

      ```
      public Chain.Transaction.raw.Builder addContract(int index,
                                                       Chain.Transaction.Contract.Builder builderForValue)
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`
    - #### addAllContract

      ```
      public Chain.Transaction.raw.Builder addAllContract(java.lang.Iterable<? extends Chain.Transaction.Contract> values)
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`
    - #### clearContract

      ```
      public Chain.Transaction.raw.Builder clearContract()
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`
    - #### removeContract

      ```
      public Chain.Transaction.raw.Builder removeContract(int index)
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`
    - #### getContractBuilder

      ```
      public Chain.Transaction.Contract.Builder getContractBuilder(int index)
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`
    - #### getContractOrBuilder

      ```
      public Chain.Transaction.ContractOrBuilder getContractOrBuilder(int index)
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`

      Specified by:
      :   `getContractOrBuilder` in interface `Chain.Transaction.rawOrBuilder`
    - #### getContractOrBuilderList

      ```
      public java.util.List<? extends Chain.Transaction.ContractOrBuilder> getContractOrBuilderList()
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`

      Specified by:
      :   `getContractOrBuilderList` in interface `Chain.Transaction.rawOrBuilder`
    - #### addContractBuilder

      ```
      public Chain.Transaction.Contract.Builder addContractBuilder()
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`
    - #### addContractBuilder

      ```
      public Chain.Transaction.Contract.Builder addContractBuilder(int index)
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`
    - #### getContractBuilderList

      ```
      public java.util.List<Chain.Transaction.Contract.Builder> getContractBuilderList()
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`
    - #### getScripts

      ```
      public com.google.protobuf.ByteString getScripts()
      ```

      ```
       scripts not used
      ```

      `bytes scripts = 12;`

      Specified by:
      :   `getScripts` in interface `Chain.Transaction.rawOrBuilder`

      Returns:
      :   The scripts.
    - #### setScripts

      ```
      public Chain.Transaction.raw.Builder setScripts(com.google.protobuf.ByteString value)
      ```

      ```
       scripts not used
      ```

      `bytes scripts = 12;`

      Parameters:
      :   `value` - The scripts to set.

      Returns:
      :   This builder for chaining.
    - #### clearScripts

      ```
      public Chain.Transaction.raw.Builder clearScripts()
      ```

      ```
       scripts not used
      ```

      `bytes scripts = 12;`

      Returns:
      :   This builder for chaining.
    - #### getTimestamp

      ```
      public long getTimestamp()
      ```

      `int64 timestamp = 14;`

      Specified by:
      :   `getTimestamp` in interface `Chain.Transaction.rawOrBuilder`

      Returns:
      :   The timestamp.
    - #### setTimestamp

      ```
      public Chain.Transaction.raw.Builder setTimestamp(long value)
      ```

      `int64 timestamp = 14;`

      Parameters:
      :   `value` - The timestamp to set.

      Returns:
      :   This builder for chaining.
    - #### clearTimestamp

      ```
      public Chain.Transaction.raw.Builder clearTimestamp()
      ```

      `int64 timestamp = 14;`

      Returns:
      :   This builder for chaining.
    - #### getFeeLimit

      ```
      public long getFeeLimit()
      ```

      `int64 fee_limit = 18;`

      Specified by:
      :   `getFeeLimit` in interface `Chain.Transaction.rawOrBuilder`

      Returns:
      :   The feeLimit.
    - #### setFeeLimit

      ```
      public Chain.Transaction.raw.Builder setFeeLimit(long value)
      ```

      `int64 fee_limit = 18;`

      Parameters:
      :   `value` - The feeLimit to set.

      Returns:
      :   This builder for chaining.
    - #### clearFeeLimit

      ```
      public Chain.Transaction.raw.Builder clearFeeLimit()
      ```

      `int64 fee_limit = 18;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Chain.Transaction.raw.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.raw.Builder>`
    - #### mergeUnknownFields

      ```
      public final Chain.Transaction.raw.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.raw.Builder>`