

org.tron.trident.proto

## Class Response.Witness.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.Witness.Builder](../../../../org/tron/trident/proto/Response.Witness.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.Witness.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.WitnessOrBuilder](../../../../org/tron/trident/proto/Response.WitnessOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.Witness](../../../../org/tron/trident/proto/Response.Witness.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.Witness.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.Witness.Builder>
  implements Response.WitnessOrBuilder
  ```

  ```
   Witness
  ```

  Protobuf type `protocol.Witness`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.Witness.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.Witness` | `build()` |
    | `Response.Witness` | `buildPartial()` |
    | `Response.Witness.Builder` | `clear()` |
    | `Response.Witness.Builder` | `clearAddress()` `bytes address = 1;` |
    | `Response.Witness.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.Witness.Builder` | `clearIsJobs()` `bool isJobs = 9;` |
    | `Response.Witness.Builder` | `clearLatestBlockNum()` `int64 latestBlockNum = 7;` |
    | `Response.Witness.Builder` | `clearLatestSlotNum()` `int64 latestSlotNum = 8;` |
    | `Response.Witness.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.Witness.Builder` | `clearPubKey()` `bytes pubKey = 3;` |
    | `Response.Witness.Builder` | `clearTotalMissed()` `int64 totalMissed = 6;` |
    | `Response.Witness.Builder` | `clearTotalProduced()` `int64 totalProduced = 5;` |
    | `Response.Witness.Builder` | `clearUrl()` `string url = 4;` |
    | `Response.Witness.Builder` | `clearVoteCount()` `int64 voteCount = 2;` |
    | `Response.Witness.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getAddress()` `bytes address = 1;` |
    | `Response.Witness` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `boolean` | `getIsJobs()` `bool isJobs = 9;` |
    | `long` | `getLatestBlockNum()` `int64 latestBlockNum = 7;` |
    | `long` | `getLatestSlotNum()` `int64 latestSlotNum = 8;` |
    | `com.google.protobuf.ByteString` | `getPubKey()` `bytes pubKey = 3;` |
    | `long` | `getTotalMissed()` `int64 totalMissed = 6;` |
    | `long` | `getTotalProduced()` `int64 totalProduced = 5;` |
    | `java.lang.String` | `getUrl()` `string url = 4;` |
    | `com.google.protobuf.ByteString` | `getUrlBytes()` `string url = 4;` |
    | `long` | `getVoteCount()` `int64 voteCount = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.Witness.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.Witness.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.Witness.Builder` | `mergeFrom(Response.Witness other)` |
    | `Response.Witness.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.Witness.Builder` | `setAddress(com.google.protobuf.ByteString value)` `bytes address = 1;` |
    | `Response.Witness.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.Witness.Builder` | `setIsJobs(boolean value)` `bool isJobs = 9;` |
    | `Response.Witness.Builder` | `setLatestBlockNum(long value)` `int64 latestBlockNum = 7;` |
    | `Response.Witness.Builder` | `setLatestSlotNum(long value)` `int64 latestSlotNum = 8;` |
    | `Response.Witness.Builder` | `setPubKey(com.google.protobuf.ByteString value)` `bytes pubKey = 3;` |
    | `Response.Witness.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.Witness.Builder` | `setTotalMissed(long value)` `int64 totalMissed = 6;` |
    | `Response.Witness.Builder` | `setTotalProduced(long value)` `int64 totalProduced = 5;` |
    | `Response.Witness.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.Witness.Builder` | `setUrl(java.lang.String value)` `string url = 4;` |
    | `Response.Witness.Builder` | `setUrlBytes(com.google.protobuf.ByteString value)` `string url = 4;` |
    | `Response.Witness.Builder` | `setVoteCount(long value)` `int64 voteCount = 2;` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Witness.Builder>`
    - #### clear

      ```
      public Response.Witness.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Witness.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Witness.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.Witness getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.Witness build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.Witness buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.Witness.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Witness.Builder>`
    - #### setField

      ```
      public Response.Witness.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                               java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Witness.Builder>`
    - #### clearField

      ```
      public Response.Witness.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Witness.Builder>`
    - #### clearOneof

      ```
      public Response.Witness.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Witness.Builder>`
    - #### setRepeatedField

      ```
      public Response.Witness.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       int index,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Witness.Builder>`
    - #### addRepeatedField

      ```
      public Response.Witness.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Witness.Builder>`
    - #### mergeFrom

      ```
      public Response.Witness.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.Witness.Builder>`
    - #### mergeFrom

      ```
      public Response.Witness.Builder mergeFrom(Response.Witness other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Witness.Builder>`
    - #### mergeFrom

      ```
      public Response.Witness.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                         throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.Witness.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getAddress

      ```
      public com.google.protobuf.ByteString getAddress()
      ```

      `bytes address = 1;`

      Specified by:
      :   `getAddress` in interface `Response.WitnessOrBuilder`

      Returns:
      :   The address.
    - #### setAddress

      ```
      public Response.Witness.Builder setAddress(com.google.protobuf.ByteString value)
      ```

      `bytes address = 1;`

      Parameters:
      :   `value` - The address to set.

      Returns:
      :   This builder for chaining.
    - #### clearAddress

      ```
      public Response.Witness.Builder clearAddress()
      ```

      `bytes address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getVoteCount

      ```
      public long getVoteCount()
      ```

      `int64 voteCount = 2;`

      Specified by:
      :   `getVoteCount` in interface `Response.WitnessOrBuilder`

      Returns:
      :   The voteCount.
    - #### setVoteCount

      ```
      public Response.Witness.Builder setVoteCount(long value)
      ```

      `int64 voteCount = 2;`

      Parameters:
      :   `value` - The voteCount to set.

      Returns:
      :   This builder for chaining.
    - #### clearVoteCount

      ```
      public Response.Witness.Builder clearVoteCount()
      ```

      `int64 voteCount = 2;`

      Returns:
      :   This builder for chaining.
    - #### getPubKey

      ```
      public com.google.protobuf.ByteString getPubKey()
      ```

      `bytes pubKey = 3;`

      Specified by:
      :   `getPubKey` in interface `Response.WitnessOrBuilder`

      Returns:
      :   The pubKey.
    - #### setPubKey

      ```
      public Response.Witness.Builder setPubKey(com.google.protobuf.ByteString value)
      ```

      `bytes pubKey = 3;`

      Parameters:
      :   `value` - The pubKey to set.

      Returns:
      :   This builder for chaining.
    - #### clearPubKey

      ```
      public Response.Witness.Builder clearPubKey()
      ```

      `bytes pubKey = 3;`

      Returns:
      :   This builder for chaining.
    - #### getUrl

      ```
      public java.lang.String getUrl()
      ```

      `string url = 4;`

      Specified by:
      :   `getUrl` in interface `Response.WitnessOrBuilder`

      Returns:
      :   The url.
    - #### getUrlBytes

      ```
      public com.google.protobuf.ByteString getUrlBytes()
      ```

      `string url = 4;`

      Specified by:
      :   `getUrlBytes` in interface `Response.WitnessOrBuilder`

      Returns:
      :   The bytes for url.
    - #### setUrl

      ```
      public Response.Witness.Builder setUrl(java.lang.String value)
      ```

      `string url = 4;`

      Parameters:
      :   `value` - The url to set.

      Returns:
      :   This builder for chaining.
    - #### clearUrl

      ```
      public Response.Witness.Builder clearUrl()
      ```

      `string url = 4;`

      Returns:
      :   This builder for chaining.
    - #### setUrlBytes

      ```
      public Response.Witness.Builder setUrlBytes(com.google.protobuf.ByteString value)
      ```

      `string url = 4;`

      Parameters:
      :   `value` - The bytes for url to set.

      Returns:
      :   This builder for chaining.
    - #### getTotalProduced

      ```
      public long getTotalProduced()
      ```

      `int64 totalProduced = 5;`

      Specified by:
      :   `getTotalProduced` in interface `Response.WitnessOrBuilder`

      Returns:
      :   The totalProduced.
    - #### setTotalProduced

      ```
      public Response.Witness.Builder setTotalProduced(long value)
      ```

      `int64 totalProduced = 5;`

      Parameters:
      :   `value` - The totalProduced to set.

      Returns:
      :   This builder for chaining.
    - #### clearTotalProduced

      ```
      public Response.Witness.Builder clearTotalProduced()
      ```

      `int64 totalProduced = 5;`

      Returns:
      :   This builder for chaining.
    - #### getTotalMissed

      ```
      public long getTotalMissed()
      ```

      `int64 totalMissed = 6;`

      Specified by:
      :   `getTotalMissed` in interface `Response.WitnessOrBuilder`

      Returns:
      :   The totalMissed.
    - #### setTotalMissed

      ```
      public Response.Witness.Builder setTotalMissed(long value)
      ```

      `int64 totalMissed = 6;`

      Parameters:
      :   `value` - The totalMissed to set.

      Returns:
      :   This builder for chaining.
    - #### clearTotalMissed

      ```
      public Response.Witness.Builder clearTotalMissed()
      ```

      `int64 totalMissed = 6;`

      Returns:
      :   This builder for chaining.
    - #### getLatestBlockNum

      ```
      public long getLatestBlockNum()
      ```

      `int64 latestBlockNum = 7;`

      Specified by:
      :   `getLatestBlockNum` in interface `Response.WitnessOrBuilder`

      Returns:
      :   The latestBlockNum.
    - #### setLatestBlockNum

      ```
      public Response.Witness.Builder setLatestBlockNum(long value)
      ```

      `int64 latestBlockNum = 7;`

      Parameters:
      :   `value` - The latestBlockNum to set.

      Returns:
      :   This builder for chaining.
    - #### clearLatestBlockNum

      ```
      public Response.Witness.Builder clearLatestBlockNum()
      ```

      `int64 latestBlockNum = 7;`

      Returns:
      :   This builder for chaining.
    - #### getLatestSlotNum

      ```
      public long getLatestSlotNum()
      ```

      `int64 latestSlotNum = 8;`

      Specified by:
      :   `getLatestSlotNum` in interface `Response.WitnessOrBuilder`

      Returns:
      :   The latestSlotNum.
    - #### setLatestSlotNum

      ```
      public Response.Witness.Builder setLatestSlotNum(long value)
      ```

      `int64 latestSlotNum = 8;`

      Parameters:
      :   `value` - The latestSlotNum to set.

      Returns:
      :   This builder for chaining.
    - #### clearLatestSlotNum

      ```
      public Response.Witness.Builder clearLatestSlotNum()
      ```

      `int64 latestSlotNum = 8;`

      Returns:
      :   This builder for chaining.
    - #### getIsJobs

      ```
      public boolean getIsJobs()
      ```

      `bool isJobs = 9;`

      Specified by:
      :   `getIsJobs` in interface `Response.WitnessOrBuilder`

      Returns:
      :   The isJobs.
    - #### setIsJobs

      ```
      public Response.Witness.Builder setIsJobs(boolean value)
      ```

      `bool isJobs = 9;`

      Parameters:
      :   `value` - The isJobs to set.

      Returns:
      :   This builder for chaining.
    - #### clearIsJobs

      ```
      public Response.Witness.Builder clearIsJobs()
      ```

      `bool isJobs = 9;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.Witness.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Witness.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.Witness.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Witness.Builder>`