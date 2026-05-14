

org.tron.trident.proto

## Class Response.TransactionInfoList.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.TransactionInfoList.Builder](../../../../org/tron/trident/proto/Response.TransactionInfoList.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.TransactionInfoList.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.TransactionInfoListOrBuilder](../../../../org/tron/trident/proto/Response.TransactionInfoListOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.TransactionInfoList](../../../../org/tron/trident/proto/Response.TransactionInfoList.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.TransactionInfoList.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfoList.Builder>
  implements Response.TransactionInfoListOrBuilder
  ```

  Protobuf type `protocol.TransactionInfoList`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.TransactionInfoList.Builder` | `addAllTransactionInfo(java.lang.Iterable<? extends Response.TransactionInfo> values)` `repeated .protocol.TransactionInfo transactionInfo = 1;` |
    | `Response.TransactionInfoList.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionInfoList.Builder` | `addTransactionInfo(int index, Response.TransactionInfo.Builder builderForValue)` `repeated .protocol.TransactionInfo transactionInfo = 1;` |
    | `Response.TransactionInfoList.Builder` | `addTransactionInfo(int index, Response.TransactionInfo value)` `repeated .protocol.TransactionInfo transactionInfo = 1;` |
    | `Response.TransactionInfoList.Builder` | `addTransactionInfo(Response.TransactionInfo.Builder builderForValue)` `repeated .protocol.TransactionInfo transactionInfo = 1;` |
    | `Response.TransactionInfoList.Builder` | `addTransactionInfo(Response.TransactionInfo value)` `repeated .protocol.TransactionInfo transactionInfo = 1;` |
    | `Response.TransactionInfo.Builder` | `addTransactionInfoBuilder()` `repeated .protocol.TransactionInfo transactionInfo = 1;` |
    | `Response.TransactionInfo.Builder` | `addTransactionInfoBuilder(int index)` `repeated .protocol.TransactionInfo transactionInfo = 1;` |
    | `Response.TransactionInfoList` | `build()` |
    | `Response.TransactionInfoList` | `buildPartial()` |
    | `Response.TransactionInfoList.Builder` | `clear()` |
    | `Response.TransactionInfoList.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.TransactionInfoList.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.TransactionInfoList.Builder` | `clearTransactionInfo()` `repeated .protocol.TransactionInfo transactionInfo = 1;` |
    | `Response.TransactionInfoList.Builder` | `clone()` |
    | `Response.TransactionInfoList` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Response.TransactionInfo` | `getTransactionInfo(int index)` `repeated .protocol.TransactionInfo transactionInfo = 1;` |
    | `Response.TransactionInfo.Builder` | `getTransactionInfoBuilder(int index)` `repeated .protocol.TransactionInfo transactionInfo = 1;` |
    | `java.util.List<Response.TransactionInfo.Builder>` | `getTransactionInfoBuilderList()` `repeated .protocol.TransactionInfo transactionInfo = 1;` |
    | `int` | `getTransactionInfoCount()` `repeated .protocol.TransactionInfo transactionInfo = 1;` |
    | `java.util.List<Response.TransactionInfo>` | `getTransactionInfoList()` `repeated .protocol.TransactionInfo transactionInfo = 1;` |
    | `Response.TransactionInfoOrBuilder` | `getTransactionInfoOrBuilder(int index)` `repeated .protocol.TransactionInfo transactionInfo = 1;` |
    | `java.util.List<? extends Response.TransactionInfoOrBuilder>` | `getTransactionInfoOrBuilderList()` `repeated .protocol.TransactionInfo transactionInfo = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.TransactionInfoList.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.TransactionInfoList.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.TransactionInfoList.Builder` | `mergeFrom(Response.TransactionInfoList other)` |
    | `Response.TransactionInfoList.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.TransactionInfoList.Builder` | `removeTransactionInfo(int index)` `repeated .protocol.TransactionInfo transactionInfo = 1;` |
    | `Response.TransactionInfoList.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.TransactionInfoList.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.TransactionInfoList.Builder` | `setTransactionInfo(int index, Response.TransactionInfo.Builder builderForValue)` `repeated .protocol.TransactionInfo transactionInfo = 1;` |
    | `Response.TransactionInfoList.Builder` | `setTransactionInfo(int index, Response.TransactionInfo value)` `repeated .protocol.TransactionInfo transactionInfo = 1;` |
    | `Response.TransactionInfoList.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfoList.Builder>`
    - #### clear

      ```
      public Response.TransactionInfoList.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfoList.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfoList.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.TransactionInfoList getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.TransactionInfoList build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.TransactionInfoList buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.TransactionInfoList.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfoList.Builder>`
    - #### setField

      ```
      public Response.TransactionInfoList.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                           java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfoList.Builder>`
    - #### clearField

      ```
      public Response.TransactionInfoList.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfoList.Builder>`
    - #### clearOneof

      ```
      public Response.TransactionInfoList.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfoList.Builder>`
    - #### setRepeatedField

      ```
      public Response.TransactionInfoList.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                   int index,
                                                                   java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfoList.Builder>`
    - #### addRepeatedField

      ```
      public Response.TransactionInfoList.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                   java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfoList.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionInfoList.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionInfoList.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionInfoList.Builder mergeFrom(Response.TransactionInfoList other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfoList.Builder>`
    - #### mergeFrom

      ```
      public Response.TransactionInfoList.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.TransactionInfoList.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getTransactionInfoList

      ```
      public java.util.List<Response.TransactionInfo> getTransactionInfoList()
      ```

      `repeated .protocol.TransactionInfo transactionInfo = 1;`

      Specified by:
      :   `getTransactionInfoList` in interface `Response.TransactionInfoListOrBuilder`
    - #### getTransactionInfoCount

      ```
      public int getTransactionInfoCount()
      ```

      `repeated .protocol.TransactionInfo transactionInfo = 1;`

      Specified by:
      :   `getTransactionInfoCount` in interface `Response.TransactionInfoListOrBuilder`
    - #### getTransactionInfo

      ```
      public Response.TransactionInfo getTransactionInfo(int index)
      ```

      `repeated .protocol.TransactionInfo transactionInfo = 1;`

      Specified by:
      :   `getTransactionInfo` in interface `Response.TransactionInfoListOrBuilder`
    - #### setTransactionInfo

      ```
      public Response.TransactionInfoList.Builder setTransactionInfo(int index,
                                                                     Response.TransactionInfo value)
      ```

      `repeated .protocol.TransactionInfo transactionInfo = 1;`
    - #### setTransactionInfo

      ```
      public Response.TransactionInfoList.Builder setTransactionInfo(int index,
                                                                     Response.TransactionInfo.Builder builderForValue)
      ```

      `repeated .protocol.TransactionInfo transactionInfo = 1;`
    - #### addTransactionInfo

      ```
      public Response.TransactionInfoList.Builder addTransactionInfo(Response.TransactionInfo value)
      ```

      `repeated .protocol.TransactionInfo transactionInfo = 1;`
    - #### addTransactionInfo

      ```
      public Response.TransactionInfoList.Builder addTransactionInfo(int index,
                                                                     Response.TransactionInfo value)
      ```

      `repeated .protocol.TransactionInfo transactionInfo = 1;`
    - #### addTransactionInfo

      ```
      public Response.TransactionInfoList.Builder addTransactionInfo(Response.TransactionInfo.Builder builderForValue)
      ```

      `repeated .protocol.TransactionInfo transactionInfo = 1;`
    - #### addTransactionInfo

      ```
      public Response.TransactionInfoList.Builder addTransactionInfo(int index,
                                                                     Response.TransactionInfo.Builder builderForValue)
      ```

      `repeated .protocol.TransactionInfo transactionInfo = 1;`
    - #### addAllTransactionInfo

      ```
      public Response.TransactionInfoList.Builder addAllTransactionInfo(java.lang.Iterable<? extends Response.TransactionInfo> values)
      ```

      `repeated .protocol.TransactionInfo transactionInfo = 1;`
    - #### clearTransactionInfo

      ```
      public Response.TransactionInfoList.Builder clearTransactionInfo()
      ```

      `repeated .protocol.TransactionInfo transactionInfo = 1;`
    - #### removeTransactionInfo

      ```
      public Response.TransactionInfoList.Builder removeTransactionInfo(int index)
      ```

      `repeated .protocol.TransactionInfo transactionInfo = 1;`
    - #### getTransactionInfoBuilder

      ```
      public Response.TransactionInfo.Builder getTransactionInfoBuilder(int index)
      ```

      `repeated .protocol.TransactionInfo transactionInfo = 1;`
    - #### getTransactionInfoOrBuilder

      ```
      public Response.TransactionInfoOrBuilder getTransactionInfoOrBuilder(int index)
      ```

      `repeated .protocol.TransactionInfo transactionInfo = 1;`

      Specified by:
      :   `getTransactionInfoOrBuilder` in interface `Response.TransactionInfoListOrBuilder`
    - #### getTransactionInfoOrBuilderList

      ```
      public java.util.List<? extends Response.TransactionInfoOrBuilder> getTransactionInfoOrBuilderList()
      ```

      `repeated .protocol.TransactionInfo transactionInfo = 1;`

      Specified by:
      :   `getTransactionInfoOrBuilderList` in interface `Response.TransactionInfoListOrBuilder`
    - #### addTransactionInfoBuilder

      ```
      public Response.TransactionInfo.Builder addTransactionInfoBuilder()
      ```

      `repeated .protocol.TransactionInfo transactionInfo = 1;`
    - #### addTransactionInfoBuilder

      ```
      public Response.TransactionInfo.Builder addTransactionInfoBuilder(int index)
      ```

      `repeated .protocol.TransactionInfo transactionInfo = 1;`
    - #### getTransactionInfoBuilderList

      ```
      public java.util.List<Response.TransactionInfo.Builder> getTransactionInfoBuilderList()
      ```

      `repeated .protocol.TransactionInfo transactionInfo = 1;`
    - #### setUnknownFields

      ```
      public final Response.TransactionInfoList.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfoList.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.TransactionInfoList.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.TransactionInfoList.Builder>`