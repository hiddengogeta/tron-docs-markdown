

org.tron.trident.proto

## Class Common.Vote.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Common.Vote.Builder](../../../../org/tron/trident/proto/Common.Vote.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Common.Vote.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Common.VoteOrBuilder](../../../../org/tron/trident/proto/Common.VoteOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Common.Vote](../../../../org/tron/trident/proto/Common.Vote.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Common.Vote.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Common.Vote.Builder>
  implements Common.VoteOrBuilder
  ```

  Protobuf type `protocol.Vote`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Common.Vote.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Common.Vote` | `build()` |
    | `Common.Vote` | `buildPartial()` |
    | `Common.Vote.Builder` | `clear()` |
    | `Common.Vote.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Common.Vote.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Common.Vote.Builder` | `clearVoteAddress()` `bytes vote_address = 1;` |
    | `Common.Vote.Builder` | `clearVoteCount()` `int64 vote_count = 2;` |
    | `Common.Vote.Builder` | `clone()` |
    | `Common.Vote` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getVoteAddress()` `bytes vote_address = 1;` |
    | `long` | `getVoteCount()` `int64 vote_count = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Common.Vote.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Common.Vote.Builder` | `mergeFrom(Common.Vote other)` |
    | `Common.Vote.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Common.Vote.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Common.Vote.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Common.Vote.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Common.Vote.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Common.Vote.Builder` | `setVoteAddress(com.google.protobuf.ByteString value)` `bytes vote_address = 1;` |
    | `Common.Vote.Builder` | `setVoteCount(long value)` `int64 vote_count = 2;` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Vote.Builder>`
    - #### clear

      ```
      public Common.Vote.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Vote.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Vote.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Common.Vote getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Common.Vote build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Common.Vote buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Common.Vote.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Vote.Builder>`
    - #### setField

      ```
      public Common.Vote.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                          java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Vote.Builder>`
    - #### clearField

      ```
      public Common.Vote.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Vote.Builder>`
    - #### clearOneof

      ```
      public Common.Vote.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Vote.Builder>`
    - #### setRepeatedField

      ```
      public Common.Vote.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                  int index,
                                                  java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Vote.Builder>`
    - #### addRepeatedField

      ```
      public Common.Vote.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                  java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Vote.Builder>`
    - #### mergeFrom

      ```
      public Common.Vote.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Common.Vote.Builder>`
    - #### mergeFrom

      ```
      public Common.Vote.Builder mergeFrom(Common.Vote other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Vote.Builder>`
    - #### mergeFrom

      ```
      public Common.Vote.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                           com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                    throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Common.Vote.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getVoteAddress

      ```
      public com.google.protobuf.ByteString getVoteAddress()
      ```

      `bytes vote_address = 1;`

      Specified by:
      :   `getVoteAddress` in interface `Common.VoteOrBuilder`

      Returns:
      :   The voteAddress.
    - #### setVoteAddress

      ```
      public Common.Vote.Builder setVoteAddress(com.google.protobuf.ByteString value)
      ```

      `bytes vote_address = 1;`

      Parameters:
      :   `value` - The voteAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearVoteAddress

      ```
      public Common.Vote.Builder clearVoteAddress()
      ```

      `bytes vote_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getVoteCount

      ```
      public long getVoteCount()
      ```

      `int64 vote_count = 2;`

      Specified by:
      :   `getVoteCount` in interface `Common.VoteOrBuilder`

      Returns:
      :   The voteCount.
    - #### setVoteCount

      ```
      public Common.Vote.Builder setVoteCount(long value)
      ```

      `int64 vote_count = 2;`

      Parameters:
      :   `value` - The voteCount to set.

      Returns:
      :   This builder for chaining.
    - #### clearVoteCount

      ```
      public Common.Vote.Builder clearVoteCount()
      ```

      `int64 vote_count = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Common.Vote.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Vote.Builder>`
    - #### mergeUnknownFields

      ```
      public final Common.Vote.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.Vote.Builder>`