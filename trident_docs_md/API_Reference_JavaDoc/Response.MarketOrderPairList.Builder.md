

org.tron.trident.proto

## Class Response.MarketOrderPairList.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.MarketOrderPairList.Builder](../../../../org/tron/trident/proto/Response.MarketOrderPairList.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.MarketOrderPairList.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.MarketOrderPairListOrBuilder](../../../../org/tron/trident/proto/Response.MarketOrderPairListOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.MarketOrderPairList](../../../../org/tron/trident/proto/Response.MarketOrderPairList.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.MarketOrderPairList.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPairList.Builder>
  implements Response.MarketOrderPairListOrBuilder
  ```

  Protobuf type `protocol.MarketOrderPairList`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.MarketOrderPairList.Builder` | `addAllOrderPair(java.lang.Iterable<? extends Response.MarketOrderPair> values)` `repeated .protocol.MarketOrderPair orderPair = 1;` |
    | `Response.MarketOrderPairList.Builder` | `addOrderPair(int index, Response.MarketOrderPair.Builder builderForValue)` `repeated .protocol.MarketOrderPair orderPair = 1;` |
    | `Response.MarketOrderPairList.Builder` | `addOrderPair(int index, Response.MarketOrderPair value)` `repeated .protocol.MarketOrderPair orderPair = 1;` |
    | `Response.MarketOrderPairList.Builder` | `addOrderPair(Response.MarketOrderPair.Builder builderForValue)` `repeated .protocol.MarketOrderPair orderPair = 1;` |
    | `Response.MarketOrderPairList.Builder` | `addOrderPair(Response.MarketOrderPair value)` `repeated .protocol.MarketOrderPair orderPair = 1;` |
    | `Response.MarketOrderPair.Builder` | `addOrderPairBuilder()` `repeated .protocol.MarketOrderPair orderPair = 1;` |
    | `Response.MarketOrderPair.Builder` | `addOrderPairBuilder(int index)` `repeated .protocol.MarketOrderPair orderPair = 1;` |
    | `Response.MarketOrderPairList.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.MarketOrderPairList` | `build()` |
    | `Response.MarketOrderPairList` | `buildPartial()` |
    | `Response.MarketOrderPairList.Builder` | `clear()` |
    | `Response.MarketOrderPairList.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.MarketOrderPairList.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.MarketOrderPairList.Builder` | `clearOrderPair()` `repeated .protocol.MarketOrderPair orderPair = 1;` |
    | `Response.MarketOrderPairList.Builder` | `clone()` |
    | `Response.MarketOrderPairList` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Response.MarketOrderPair` | `getOrderPair(int index)` `repeated .protocol.MarketOrderPair orderPair = 1;` |
    | `Response.MarketOrderPair.Builder` | `getOrderPairBuilder(int index)` `repeated .protocol.MarketOrderPair orderPair = 1;` |
    | `java.util.List<Response.MarketOrderPair.Builder>` | `getOrderPairBuilderList()` `repeated .protocol.MarketOrderPair orderPair = 1;` |
    | `int` | `getOrderPairCount()` `repeated .protocol.MarketOrderPair orderPair = 1;` |
    | `java.util.List<Response.MarketOrderPair>` | `getOrderPairList()` `repeated .protocol.MarketOrderPair orderPair = 1;` |
    | `Response.MarketOrderPairOrBuilder` | `getOrderPairOrBuilder(int index)` `repeated .protocol.MarketOrderPair orderPair = 1;` |
    | `java.util.List<? extends Response.MarketOrderPairOrBuilder>` | `getOrderPairOrBuilderList()` `repeated .protocol.MarketOrderPair orderPair = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.MarketOrderPairList.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.MarketOrderPairList.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.MarketOrderPairList.Builder` | `mergeFrom(Response.MarketOrderPairList other)` |
    | `Response.MarketOrderPairList.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.MarketOrderPairList.Builder` | `removeOrderPair(int index)` `repeated .protocol.MarketOrderPair orderPair = 1;` |
    | `Response.MarketOrderPairList.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.MarketOrderPairList.Builder` | `setOrderPair(int index, Response.MarketOrderPair.Builder builderForValue)` `repeated .protocol.MarketOrderPair orderPair = 1;` |
    | `Response.MarketOrderPairList.Builder` | `setOrderPair(int index, Response.MarketOrderPair value)` `repeated .protocol.MarketOrderPair orderPair = 1;` |
    | `Response.MarketOrderPairList.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.MarketOrderPairList.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPairList.Builder>`
    - #### clear

      ```
      public Response.MarketOrderPairList.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPairList.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPairList.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.MarketOrderPairList getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.MarketOrderPairList build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.MarketOrderPairList buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.MarketOrderPairList.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPairList.Builder>`
    - #### setField

      ```
      public Response.MarketOrderPairList.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                           java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPairList.Builder>`
    - #### clearField

      ```
      public Response.MarketOrderPairList.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPairList.Builder>`
    - #### clearOneof

      ```
      public Response.MarketOrderPairList.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPairList.Builder>`
    - #### setRepeatedField

      ```
      public Response.MarketOrderPairList.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                   int index,
                                                                   java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPairList.Builder>`
    - #### addRepeatedField

      ```
      public Response.MarketOrderPairList.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                   java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPairList.Builder>`
    - #### mergeFrom

      ```
      public Response.MarketOrderPairList.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.MarketOrderPairList.Builder>`
    - #### mergeFrom

      ```
      public Response.MarketOrderPairList.Builder mergeFrom(Response.MarketOrderPairList other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPairList.Builder>`
    - #### mergeFrom

      ```
      public Response.MarketOrderPairList.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.MarketOrderPairList.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOrderPairList

      ```
      public java.util.List<Response.MarketOrderPair> getOrderPairList()
      ```

      `repeated .protocol.MarketOrderPair orderPair = 1;`

      Specified by:
      :   `getOrderPairList` in interface `Response.MarketOrderPairListOrBuilder`
    - #### getOrderPairCount

      ```
      public int getOrderPairCount()
      ```

      `repeated .protocol.MarketOrderPair orderPair = 1;`

      Specified by:
      :   `getOrderPairCount` in interface `Response.MarketOrderPairListOrBuilder`
    - #### getOrderPair

      ```
      public Response.MarketOrderPair getOrderPair(int index)
      ```

      `repeated .protocol.MarketOrderPair orderPair = 1;`

      Specified by:
      :   `getOrderPair` in interface `Response.MarketOrderPairListOrBuilder`
    - #### setOrderPair

      ```
      public Response.MarketOrderPairList.Builder setOrderPair(int index,
                                                               Response.MarketOrderPair value)
      ```

      `repeated .protocol.MarketOrderPair orderPair = 1;`
    - #### setOrderPair

      ```
      public Response.MarketOrderPairList.Builder setOrderPair(int index,
                                                               Response.MarketOrderPair.Builder builderForValue)
      ```

      `repeated .protocol.MarketOrderPair orderPair = 1;`
    - #### addOrderPair

      ```
      public Response.MarketOrderPairList.Builder addOrderPair(Response.MarketOrderPair value)
      ```

      `repeated .protocol.MarketOrderPair orderPair = 1;`
    - #### addOrderPair

      ```
      public Response.MarketOrderPairList.Builder addOrderPair(int index,
                                                               Response.MarketOrderPair value)
      ```

      `repeated .protocol.MarketOrderPair orderPair = 1;`
    - #### addOrderPair

      ```
      public Response.MarketOrderPairList.Builder addOrderPair(Response.MarketOrderPair.Builder builderForValue)
      ```

      `repeated .protocol.MarketOrderPair orderPair = 1;`
    - #### addOrderPair

      ```
      public Response.MarketOrderPairList.Builder addOrderPair(int index,
                                                               Response.MarketOrderPair.Builder builderForValue)
      ```

      `repeated .protocol.MarketOrderPair orderPair = 1;`
    - #### addAllOrderPair

      ```
      public Response.MarketOrderPairList.Builder addAllOrderPair(java.lang.Iterable<? extends Response.MarketOrderPair> values)
      ```

      `repeated .protocol.MarketOrderPair orderPair = 1;`
    - #### clearOrderPair

      ```
      public Response.MarketOrderPairList.Builder clearOrderPair()
      ```

      `repeated .protocol.MarketOrderPair orderPair = 1;`
    - #### removeOrderPair

      ```
      public Response.MarketOrderPairList.Builder removeOrderPair(int index)
      ```

      `repeated .protocol.MarketOrderPair orderPair = 1;`
    - #### getOrderPairBuilder

      ```
      public Response.MarketOrderPair.Builder getOrderPairBuilder(int index)
      ```

      `repeated .protocol.MarketOrderPair orderPair = 1;`
    - #### getOrderPairOrBuilder

      ```
      public Response.MarketOrderPairOrBuilder getOrderPairOrBuilder(int index)
      ```

      `repeated .protocol.MarketOrderPair orderPair = 1;`

      Specified by:
      :   `getOrderPairOrBuilder` in interface `Response.MarketOrderPairListOrBuilder`
    - #### getOrderPairOrBuilderList

      ```
      public java.util.List<? extends Response.MarketOrderPairOrBuilder> getOrderPairOrBuilderList()
      ```

      `repeated .protocol.MarketOrderPair orderPair = 1;`

      Specified by:
      :   `getOrderPairOrBuilderList` in interface `Response.MarketOrderPairListOrBuilder`
    - #### addOrderPairBuilder

      ```
      public Response.MarketOrderPair.Builder addOrderPairBuilder()
      ```

      `repeated .protocol.MarketOrderPair orderPair = 1;`
    - #### addOrderPairBuilder

      ```
      public Response.MarketOrderPair.Builder addOrderPairBuilder(int index)
      ```

      `repeated .protocol.MarketOrderPair orderPair = 1;`
    - #### getOrderPairBuilderList

      ```
      public java.util.List<Response.MarketOrderPair.Builder> getOrderPairBuilderList()
      ```

      `repeated .protocol.MarketOrderPair orderPair = 1;`
    - #### setUnknownFields

      ```
      public final Response.MarketOrderPairList.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPairList.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.MarketOrderPairList.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderPairList.Builder>`