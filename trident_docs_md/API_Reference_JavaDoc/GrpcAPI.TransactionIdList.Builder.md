

org.tron.trident.api

## Class GrpcAPI.TransactionIdList.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.TransactionIdList.Builder](../../../../org/tron/trident/api/GrpcAPI.TransactionIdList.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.TransactionIdList.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.TransactionIdListOrBuilder](../../../../org/tron/trident/api/GrpcAPI.TransactionIdListOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.TransactionIdList](../../../../org/tron/trident/api/GrpcAPI.TransactionIdList.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.TransactionIdList.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.TransactionIdList.Builder>
  implements GrpcAPI.TransactionIdListOrBuilder
  ```

  Protobuf type `protocol.TransactionIdList`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.TransactionIdList.Builder` | `addAllTxId(java.lang.Iterable<java.lang.String> values)` `repeated string txId = 1;` |
    | `GrpcAPI.TransactionIdList.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.TransactionIdList.Builder` | `addTxId(java.lang.String value)` `repeated string txId = 1;` |
    | `GrpcAPI.TransactionIdList.Builder` | `addTxIdBytes(com.google.protobuf.ByteString value)` `repeated string txId = 1;` |
    | `GrpcAPI.TransactionIdList` | `build()` |
    | `GrpcAPI.TransactionIdList` | `buildPartial()` |
    | `GrpcAPI.TransactionIdList.Builder` | `clear()` |
    | `GrpcAPI.TransactionIdList.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.TransactionIdList.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.TransactionIdList.Builder` | `clearTxId()` `repeated string txId = 1;` |
    | `GrpcAPI.TransactionIdList.Builder` | `clone()` |
    | `GrpcAPI.TransactionIdList` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `java.lang.String` | `getTxId(int index)` `repeated string txId = 1;` |
    | `com.google.protobuf.ByteString` | `getTxIdBytes(int index)` `repeated string txId = 1;` |
    | `int` | `getTxIdCount()` `repeated string txId = 1;` |
    | `com.google.protobuf.ProtocolStringList` | `getTxIdList()` `repeated string txId = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.TransactionIdList.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.TransactionIdList.Builder` | `mergeFrom(GrpcAPI.TransactionIdList other)` |
    | `GrpcAPI.TransactionIdList.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.TransactionIdList.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.TransactionIdList.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.TransactionIdList.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.TransactionIdList.Builder` | `setTxId(int index, java.lang.String value)` `repeated string txId = 1;` |
    | `GrpcAPI.TransactionIdList.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.TransactionIdList.Builder>`
    - #### clear

      ```
      public GrpcAPI.TransactionIdList.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.TransactionIdList.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.TransactionIdList.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.TransactionIdList getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.TransactionIdList build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.TransactionIdList buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.TransactionIdList.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.TransactionIdList.Builder>`
    - #### setField

      ```
      public GrpcAPI.TransactionIdList.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                        java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.TransactionIdList.Builder>`
    - #### clearField

      ```
      public GrpcAPI.TransactionIdList.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.TransactionIdList.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.TransactionIdList.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.TransactionIdList.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.TransactionIdList.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                int index,
                                                                java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.TransactionIdList.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.TransactionIdList.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.TransactionIdList.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.TransactionIdList.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.TransactionIdList.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.TransactionIdList.Builder mergeFrom(GrpcAPI.TransactionIdList other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.TransactionIdList.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.TransactionIdList.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.TransactionIdList.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getTxIdList

      ```
      public com.google.protobuf.ProtocolStringList getTxIdList()
      ```

      `repeated string txId = 1;`

      Specified by:
      :   `getTxIdList` in interface `GrpcAPI.TransactionIdListOrBuilder`

      Returns:
      :   A list containing the txId.
    - #### getTxIdCount

      ```
      public int getTxIdCount()
      ```

      `repeated string txId = 1;`

      Specified by:
      :   `getTxIdCount` in interface `GrpcAPI.TransactionIdListOrBuilder`

      Returns:
      :   The count of txId.
    - #### getTxId

      ```
      public java.lang.String getTxId(int index)
      ```

      `repeated string txId = 1;`

      Specified by:
      :   `getTxId` in interface `GrpcAPI.TransactionIdListOrBuilder`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The txId at the given index.
    - #### getTxIdBytes

      ```
      public com.google.protobuf.ByteString getTxIdBytes(int index)
      ```

      `repeated string txId = 1;`

      Specified by:
      :   `getTxIdBytes` in interface `GrpcAPI.TransactionIdListOrBuilder`

      Parameters:
      :   `index` - The index of the value to return.

      Returns:
      :   The bytes of the txId at the given index.
    - #### setTxId

      ```
      public GrpcAPI.TransactionIdList.Builder setTxId(int index,
                                                       java.lang.String value)
      ```

      `repeated string txId = 1;`

      Parameters:
      :   `index` - The index to set the value at.
      :   `value` - The txId to set.

      Returns:
      :   This builder for chaining.
    - #### addTxId

      ```
      public GrpcAPI.TransactionIdList.Builder addTxId(java.lang.String value)
      ```

      `repeated string txId = 1;`

      Parameters:
      :   `value` - The txId to add.

      Returns:
      :   This builder for chaining.
    - #### addAllTxId

      ```
      public GrpcAPI.TransactionIdList.Builder addAllTxId(java.lang.Iterable<java.lang.String> values)
      ```

      `repeated string txId = 1;`

      Parameters:
      :   `values` - The txId to add.

      Returns:
      :   This builder for chaining.
    - #### clearTxId

      ```
      public GrpcAPI.TransactionIdList.Builder clearTxId()
      ```

      `repeated string txId = 1;`

      Returns:
      :   This builder for chaining.
    - #### addTxIdBytes

      ```
      public GrpcAPI.TransactionIdList.Builder addTxIdBytes(com.google.protobuf.ByteString value)
      ```

      `repeated string txId = 1;`

      Parameters:
      :   `value` - The bytes of the txId to add.

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.TransactionIdList.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.TransactionIdList.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.TransactionIdList.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.TransactionIdList.Builder>`