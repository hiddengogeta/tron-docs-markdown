

org.tron.trident.proto

## Class Response.TransactionInfo.Log.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.TransactionInfo.Log.Builder](../../../../org/tron/trident/proto/Response.TransactionInfo.Log.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.TransactionInfo.Log.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.TransactionInfo.LogOrBuilder](../../../../org/tron/trident/proto/Response.TransactionInfo.LogOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.TransactionInfo.Log](../../../../org/tron/trident/proto/Response.TransactionInfo.Log.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.TransactionInfo.Log.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Log.Builder>
  implements Response.TransactionInfo.LogOrBuilder
  ```

  Protobuf type `protocol.TransactionInfo.Log`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.TransactionInfo.Log.Builder` | `addAllTopics(java.lang.Iterable<? extends com.google.protobuf.ByteString> values)` `repeated bytes topics = 2;` |
    | `Response.TransactionInfo.Log.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionInfo.Log.Builder` | `addTopics(com.google.protobuf.ByteString value)` `repeated bytes topics = 2;` |
    | `Response.TransactionInfo.Log` | `build()` |
    | `Response.TransactionInfo.Log` | `buildPartial()` |
    | `Response.TransactionInfo.Log.Builder` | `clear()` |
    | `Response.TransactionInfo.Log.Builder` | `clearAddress()` `bytes address = 1;` |
    | `Response.TransactionInfo.Log.Builder` | `clearData()` `bytes data = 3;` |
    | `Response.TransactionInfo.Log.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.TransactionInfo.Log.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.TransactionInfo.Log.Builder` | `clearTopics()` `repeated bytes topics = 2;` |
    | `Response.TransactionInfo.Log.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getAddress()` `bytes address = 1;` |
    | `com.google.protobuf.ByteString` | `getData()` `bytes data = 3;` |
    | `Response.TransactionInfo.Log` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getTopics(int index)` `repeated bytes topics = 2;` |
    | `int` | `getTopicsCount()` `repeated bytes topics = 2;` |
    | `java.util.List<com.google.protobuf.ByteString>` | `getTopicsList()` `repeated bytes topics = 2;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.TransactionInfo.Log.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.TransactionInfo.Log.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.TransactionInfo.Log.Builder` | `mergeFrom(Response.TransactionInfo.Log other)` |
    | `Response.TransactionInfo.Log.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.TransactionInfo.Log.Builder` | `setAddress(com.google.protobuf.ByteString value)` `bytes address = 1;` |
    | `Response.TransactionInfo.Log.Builder` | `setData(com.google.protobuf.ByteString value)` `bytes data = 3;` |
    | `Response.TransactionInfo.Log.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionInfo.Log.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.TransactionInfo.Log.Builder` | `setTopics(int index, com.google.protobuf.ByteString value)` `repeated bytes topics = 2;` |
    | `Response.TransactionInfo.Log.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Log.Builder>`
    - #### clear

      ```
      public Response.TransactionInfo.Log.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Log.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Log.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.TransactionInfo.Log getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.TransactionInfo.Log build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.TransactionInfo.Log buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.TransactionInfo.Log.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Log.Builder>`
    - #### setField

      ```
      public Response.TransactionInfo.Log.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                           java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Log.Builder>`
    - #### clearField

      ```
      public Response.TransactionInfo.Log.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Log.Builder>`
    - #### clearOneof

      ```
      public Response.TransactionInfo.Log.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Log.Builder>`
    - #### setRepeatedField

      ```
      public Response.TransactionInfo.Log.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                   int index,
                                                                   java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Log.Builder>`
    - #### addRepeatedField

      ```
      public Response.TransactionInfo.Log.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                   java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Log.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionInfo.Log.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionInfo.Log.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionInfo.Log.Builder mergeFrom(Response.TransactionInfo.Log other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Log.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionInfo.Log.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionInfo.Log.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getAddress

      ```
      public com.google.protobuf.ByteString getAddress()
      ```

      `bytes address = 1;`

      Specified by:
      :   `getAddress` in interface `Response.TransactionInfo.LogOrBuilder`

      Returns:
      :   The address.
    - #### setAddress

      ```
      public Response.TransactionInfo.Log.Builder setAddress(com.google.protobuf.ByteString value)
      ```

      `bytes address = 1;`

      Parameters:
      :   `value` - The address to set.

      Returns:
      :   This builder for chaining.
    - #### clearAddress

      ```
      public Response.TransactionInfo.Log.Builder clearAddress()
      ```

      `bytes address = 1;`

      Returns:
      :   This builder for chaining.
    - #### getTopicsList

      ```
      public java.util.List<com.google.protobuf.ByteString> getTopicsList()
      ```

      `repeated bytes topics = 2;`

      Specified by:
      :   `getTopicsList` in interface `Response.TransactionInfo.LogOrBuilder`

      Returns:
      :   A list containing the topics.
    - #### getTopicsCount

      ```
      public int getTopicsCount()
      ```

      `repeated bytes topics = 2;`

      Specified by:
      :   `getTopicsCount` in interface `Response.TransactionInfo.LogOrBuilder`

      Returns:
      :   The count of topics.
    - #### getTopics

      ```
      public com.google.protobuf.ByteString getTopics(int index)
      ```

      `repeated bytes topics = 2;`

      Specified by:
      :   `getTopics` in interface `Response.TransactionInfo.LogOrBuilder`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The topics at the given index.
    - #### setTopics

      ```
      public Response.TransactionInfo.Log.Builder setTopics(int index,
                                                            com.google.protobuf.ByteString value)
      ```

      `repeated bytes topics = 2;`

      Parameters:
      :   `index` - The index to set the value at.
      :   `value` - The topics to set.

      Returns:
      :   This builder for chaining.
    - #### addTopics

      ```
      public Response.TransactionInfo.Log.Builder addTopics(com.google.protobuf.ByteString value)
      ```

      `repeated bytes topics = 2;`

      Parameters:
      :   `value` - The topics to add.

      Returns:
      :   This builder for chaining.
    - #### addAllTopics

      ```
      public Response.TransactionInfo.Log.Builder addAllTopics(java.lang.Iterable<? extends com.google.protobuf.ByteString> values)
      ```

      `repeated bytes topics = 2;`

      Parameters:
      :   `values` - The topics to add.

      Returns:
      :   This builder for chaining.
    - #### clearTopics

      ```
      public Response.TransactionInfo.Log.Builder clearTopics()
      ```

      `repeated bytes topics = 2;`

      Returns:
      :   This builder for chaining.
    - #### getData

      ```
      public com.google.protobuf.ByteString getData()
      ```

      `bytes data = 3;`

      Specified by:
      :   `getData` in interface `Response.TransactionInfo.LogOrBuilder`

      Returns:
      :   The data.
    - #### setData

      ```
      public Response.TransactionInfo.Log.Builder setData(com.google.protobuf.ByteString value)
      ```

      `bytes data = 3;`

      Parameters:
      :   `value` - The data to set.

      Returns:
      :   This builder for chaining.
    - #### clearData

      ```
      public Response.TransactionInfo.Log.Builder clearData()
      ```

      `bytes data = 3;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.TransactionInfo.Log.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Log.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.TransactionInfo.Log.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfo.Log.Builder>`