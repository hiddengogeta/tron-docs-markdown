

org.tron.trident.proto

## Class Response.ExchangeList.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.ExchangeList.Builder](../../../../org/tron/trident/proto/Response.ExchangeList.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.ExchangeList.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.ExchangeListOrBuilder](../../../../org/tron/trident/proto/Response.ExchangeListOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.ExchangeList](../../../../org/tron/trident/proto/Response.ExchangeList.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.ExchangeList.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.ExchangeList.Builder>
  implements Response.ExchangeListOrBuilder
  ```

  Protobuf type `protocol.ExchangeList`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.ExchangeList.Builder` | `addAllExchanges(java.lang.Iterable<? extends Response.Exchange> values)` `repeated .protocol.Exchange exchanges = 1;` |
    | `Response.ExchangeList.Builder` | `addExchanges(int index, Response.Exchange.Builder builderForValue)` `repeated .protocol.Exchange exchanges = 1;` |
    | `Response.ExchangeList.Builder` | `addExchanges(int index, Response.Exchange value)` `repeated .protocol.Exchange exchanges = 1;` |
    | `Response.ExchangeList.Builder` | `addExchanges(Response.Exchange.Builder builderForValue)` `repeated .protocol.Exchange exchanges = 1;` |
    | `Response.ExchangeList.Builder` | `addExchanges(Response.Exchange value)` `repeated .protocol.Exchange exchanges = 1;` |
    | `Response.Exchange.Builder` | `addExchangesBuilder()` `repeated .protocol.Exchange exchanges = 1;` |
    | `Response.Exchange.Builder` | `addExchangesBuilder(int index)` `repeated .protocol.Exchange exchanges = 1;` |
    | `Response.ExchangeList.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.ExchangeList` | `build()` |
    | `Response.ExchangeList` | `buildPartial()` |
    | `Response.ExchangeList.Builder` | `clear()` |
    | `Response.ExchangeList.Builder` | `clearExchanges()` `repeated .protocol.Exchange exchanges = 1;` |
    | `Response.ExchangeList.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.ExchangeList.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.ExchangeList.Builder` | `clone()` |
    | `Response.ExchangeList` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Response.Exchange` | `getExchanges(int index)` `repeated .protocol.Exchange exchanges = 1;` |
    | `Response.Exchange.Builder` | `getExchangesBuilder(int index)` `repeated .protocol.Exchange exchanges = 1;` |
    | `java.util.List<Response.Exchange.Builder>` | `getExchangesBuilderList()` `repeated .protocol.Exchange exchanges = 1;` |
    | `int` | `getExchangesCount()` `repeated .protocol.Exchange exchanges = 1;` |
    | `java.util.List<Response.Exchange>` | `getExchangesList()` `repeated .protocol.Exchange exchanges = 1;` |
    | `Response.ExchangeOrBuilder` | `getExchangesOrBuilder(int index)` `repeated .protocol.Exchange exchanges = 1;` |
    | `java.util.List<? extends Response.ExchangeOrBuilder>` | `getExchangesOrBuilderList()` `repeated .protocol.Exchange exchanges = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.ExchangeList.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.ExchangeList.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.ExchangeList.Builder` | `mergeFrom(Response.ExchangeList other)` |
    | `Response.ExchangeList.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.ExchangeList.Builder` | `removeExchanges(int index)` `repeated .protocol.Exchange exchanges = 1;` |
    | `Response.ExchangeList.Builder` | `setExchanges(int index, Response.Exchange.Builder builderForValue)` `repeated .protocol.Exchange exchanges = 1;` |
    | `Response.ExchangeList.Builder` | `setExchanges(int index, Response.Exchange value)` `repeated .protocol.Exchange exchanges = 1;` |
    | `Response.ExchangeList.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.ExchangeList.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.ExchangeList.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ExchangeList.Builder>`
    - #### clear

      ```
      public Response.ExchangeList.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ExchangeList.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ExchangeList.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.ExchangeList getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.ExchangeList build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.ExchangeList buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.ExchangeList.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ExchangeList.Builder>`
    - #### setField

      ```
      public Response.ExchangeList.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                    java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ExchangeList.Builder>`
    - #### clearField

      ```
      public Response.ExchangeList.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ExchangeList.Builder>`
    - #### clearOneof

      ```
      public Response.ExchangeList.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ExchangeList.Builder>`
    - #### setRepeatedField

      ```
      public Response.ExchangeList.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                            int index,
                                                            java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ExchangeList.Builder>`
    - #### addRepeatedField

      ```
      public Response.ExchangeList.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                            java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ExchangeList.Builder>`
    - #### mergeFrom

      ```
      public Response.ExchangeList.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.ExchangeList.Builder>`
    - #### mergeFrom

      ```
      public Response.ExchangeList.Builder mergeFrom(Response.ExchangeList other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ExchangeList.Builder>`
    - #### mergeFrom

      ```
      public Response.ExchangeList.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                     com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                              throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.ExchangeList.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getExchangesList

      ```
      public java.util.List<Response.Exchange> getExchangesList()
      ```

      `repeated .protocol.Exchange exchanges = 1;`

      Specified by:
      :   `getExchangesList` in interface `Response.ExchangeListOrBuilder`
    - #### getExchangesCount

      ```
      public int getExchangesCount()
      ```

      `repeated .protocol.Exchange exchanges = 1;`

      Specified by:
      :   `getExchangesCount` in interface `Response.ExchangeListOrBuilder`
    - #### getExchanges

      ```
      public Response.Exchange getExchanges(int index)
      ```

      `repeated .protocol.Exchange exchanges = 1;`

      Specified by:
      :   `getExchanges` in interface `Response.ExchangeListOrBuilder`
    - #### setExchanges

      ```
      public Response.ExchangeList.Builder setExchanges(int index,
                                                        Response.Exchange value)
      ```

      `repeated .protocol.Exchange exchanges = 1;`
    - #### setExchanges

      ```
      public Response.ExchangeList.Builder setExchanges(int index,
                                                        Response.Exchange.Builder builderForValue)
      ```

      `repeated .protocol.Exchange exchanges = 1;`
    - #### addExchanges

      ```
      public Response.ExchangeList.Builder addExchanges(Response.Exchange value)
      ```

      `repeated .protocol.Exchange exchanges = 1;`
    - #### addExchanges

      ```
      public Response.ExchangeList.Builder addExchanges(int index,
                                                        Response.Exchange value)
      ```

      `repeated .protocol.Exchange exchanges = 1;`
    - #### addExchanges

      ```
      public Response.ExchangeList.Builder addExchanges(Response.Exchange.Builder builderForValue)
      ```

      `repeated .protocol.Exchange exchanges = 1;`
    - #### addExchanges

      ```
      public Response.ExchangeList.Builder addExchanges(int index,
                                                        Response.Exchange.Builder builderForValue)
      ```

      `repeated .protocol.Exchange exchanges = 1;`
    - #### addAllExchanges

      ```
      public Response.ExchangeList.Builder addAllExchanges(java.lang.Iterable<? extends Response.Exchange> values)
      ```

      `repeated .protocol.Exchange exchanges = 1;`
    - #### clearExchanges

      ```
      public Response.ExchangeList.Builder clearExchanges()
      ```

      `repeated .protocol.Exchange exchanges = 1;`
    - #### removeExchanges

      ```
      public Response.ExchangeList.Builder removeExchanges(int index)
      ```

      `repeated .protocol.Exchange exchanges = 1;`
    - #### getExchangesBuilder

      ```
      public Response.Exchange.Builder getExchangesBuilder(int index)
      ```

      `repeated .protocol.Exchange exchanges = 1;`
    - #### getExchangesOrBuilder

      ```
      public Response.ExchangeOrBuilder getExchangesOrBuilder(int index)
      ```

      `repeated .protocol.Exchange exchanges = 1;`

      Specified by:
      :   `getExchangesOrBuilder` in interface `Response.ExchangeListOrBuilder`
    - #### getExchangesOrBuilderList

      ```
      public java.util.List<? extends Response.ExchangeOrBuilder> getExchangesOrBuilderList()
      ```

      `repeated .protocol.Exchange exchanges = 1;`

      Specified by:
      :   `getExchangesOrBuilderList` in interface `Response.ExchangeListOrBuilder`
    - #### addExchangesBuilder

      ```
      public Response.Exchange.Builder addExchangesBuilder()
      ```

      `repeated .protocol.Exchange exchanges = 1;`
    - #### addExchangesBuilder

      ```
      public Response.Exchange.Builder addExchangesBuilder(int index)
      ```

      `repeated .protocol.Exchange exchanges = 1;`
    - #### getExchangesBuilderList

      ```
      public java.util.List<Response.Exchange.Builder> getExchangesBuilderList()
      ```

      `repeated .protocol.Exchange exchanges = 1;`
    - #### setUnknownFields

      ```
      public final Response.ExchangeList.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ExchangeList.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.ExchangeList.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ExchangeList.Builder>`