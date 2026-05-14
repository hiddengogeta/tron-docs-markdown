

org.tron.trident.proto

## Class Response.MarketOrderList.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.MarketOrderList.Builder](../../../../org/tron/trident/proto/Response.MarketOrderList.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.MarketOrderList.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.MarketOrderListOrBuilder](../../../../org/tron/trident/proto/Response.MarketOrderListOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.MarketOrderList](../../../../org/tron/trident/proto/Response.MarketOrderList.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.MarketOrderList.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderList.Builder>
  implements Response.MarketOrderListOrBuilder
  ```

  Protobuf type `protocol.MarketOrderList`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.MarketOrderList.Builder` | `addAllOrders(java.lang.Iterable<? extends Response.MarketOrder> values)` `repeated .protocol.MarketOrder orders = 1;` |
    | `Response.MarketOrderList.Builder` | `addOrders(int index, Response.MarketOrder.Builder builderForValue)` `repeated .protocol.MarketOrder orders = 1;` |
    | `Response.MarketOrderList.Builder` | `addOrders(int index, Response.MarketOrder value)` `repeated .protocol.MarketOrder orders = 1;` |
    | `Response.MarketOrderList.Builder` | `addOrders(Response.MarketOrder.Builder builderForValue)` `repeated .protocol.MarketOrder orders = 1;` |
    | `Response.MarketOrderList.Builder` | `addOrders(Response.MarketOrder value)` `repeated .protocol.MarketOrder orders = 1;` |
    | `Response.MarketOrder.Builder` | `addOrdersBuilder()` `repeated .protocol.MarketOrder orders = 1;` |
    | `Response.MarketOrder.Builder` | `addOrdersBuilder(int index)` `repeated .protocol.MarketOrder orders = 1;` |
    | `Response.MarketOrderList.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.MarketOrderList` | `build()` |
    | `Response.MarketOrderList` | `buildPartial()` |
    | `Response.MarketOrderList.Builder` | `clear()` |
    | `Response.MarketOrderList.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.MarketOrderList.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.MarketOrderList.Builder` | `clearOrders()` `repeated .protocol.MarketOrder orders = 1;` |
    | `Response.MarketOrderList.Builder` | `clone()` |
    | `Response.MarketOrderList` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Response.MarketOrder` | `getOrders(int index)` `repeated .protocol.MarketOrder orders = 1;` |
    | `Response.MarketOrder.Builder` | `getOrdersBuilder(int index)` `repeated .protocol.MarketOrder orders = 1;` |
    | `java.util.List<Response.MarketOrder.Builder>` | `getOrdersBuilderList()` `repeated .protocol.MarketOrder orders = 1;` |
    | `int` | `getOrdersCount()` `repeated .protocol.MarketOrder orders = 1;` |
    | `java.util.List<Response.MarketOrder>` | `getOrdersList()` `repeated .protocol.MarketOrder orders = 1;` |
    | `Response.MarketOrderOrBuilder` | `getOrdersOrBuilder(int index)` `repeated .protocol.MarketOrder orders = 1;` |
    | `java.util.List<? extends Response.MarketOrderOrBuilder>` | `getOrdersOrBuilderList()` `repeated .protocol.MarketOrder orders = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.MarketOrderList.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.MarketOrderList.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.MarketOrderList.Builder` | `mergeFrom(Response.MarketOrderList other)` |
    | `Response.MarketOrderList.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.MarketOrderList.Builder` | `removeOrders(int index)` `repeated .protocol.MarketOrder orders = 1;` |
    | `Response.MarketOrderList.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.MarketOrderList.Builder` | `setOrders(int index, Response.MarketOrder.Builder builderForValue)` `repeated .protocol.MarketOrder orders = 1;` |
    | `Response.MarketOrderList.Builder` | `setOrders(int index, Response.MarketOrder value)` `repeated .protocol.MarketOrder orders = 1;` |
    | `Response.MarketOrderList.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.MarketOrderList.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderList.Builder>`
    - #### clear

      ```
      public Response.MarketOrderList.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderList.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderList.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.MarketOrderList getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.MarketOrderList build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.MarketOrderList buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.MarketOrderList.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderList.Builder>`
    - #### setField

      ```
      public Response.MarketOrderList.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderList.Builder>`
    - #### clearField

      ```
      public Response.MarketOrderList.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderList.Builder>`
    - #### clearOneof

      ```
      public Response.MarketOrderList.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderList.Builder>`
    - #### setRepeatedField

      ```
      public Response.MarketOrderList.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               int index,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderList.Builder>`
    - #### addRepeatedField

      ```
      public Response.MarketOrderList.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderList.Builder>`
    - #### mergeFrom

      ```
      public Response.MarketOrderList.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.MarketOrderList.Builder>`
    - #### mergeFrom

      ```
      public Response.MarketOrderList.Builder mergeFrom(Response.MarketOrderList other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderList.Builder>`
    - #### mergeFrom

      ```
      public Response.MarketOrderList.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                 throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.MarketOrderList.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOrdersList

      ```
      public java.util.List<Response.MarketOrder> getOrdersList()
      ```

      `repeated .protocol.MarketOrder orders = 1;`

      Specified by:
      :   `getOrdersList` in interface `Response.MarketOrderListOrBuilder`
    - #### getOrdersCount

      ```
      public int getOrdersCount()
      ```

      `repeated .protocol.MarketOrder orders = 1;`

      Specified by:
      :   `getOrdersCount` in interface `Response.MarketOrderListOrBuilder`
    - #### getOrders

      ```
      public Response.MarketOrder getOrders(int index)
      ```

      `repeated .protocol.MarketOrder orders = 1;`

      Specified by:
      :   `getOrders` in interface `Response.MarketOrderListOrBuilder`
    - #### setOrders

      ```
      public Response.MarketOrderList.Builder setOrders(int index,
                                                        Response.MarketOrder value)
      ```

      `repeated .protocol.MarketOrder orders = 1;`
    - #### setOrders

      ```
      public Response.MarketOrderList.Builder setOrders(int index,
                                                        Response.MarketOrder.Builder builderForValue)
      ```

      `repeated .protocol.MarketOrder orders = 1;`
    - #### addOrders

      ```
      public Response.MarketOrderList.Builder addOrders(Response.MarketOrder value)
      ```

      `repeated .protocol.MarketOrder orders = 1;`
    - #### addOrders

      ```
      public Response.MarketOrderList.Builder addOrders(int index,
                                                        Response.MarketOrder value)
      ```

      `repeated .protocol.MarketOrder orders = 1;`
    - #### addOrders

      ```
      public Response.MarketOrderList.Builder addOrders(Response.MarketOrder.Builder builderForValue)
      ```

      `repeated .protocol.MarketOrder orders = 1;`
    - #### addOrders

      ```
      public Response.MarketOrderList.Builder addOrders(int index,
                                                        Response.MarketOrder.Builder builderForValue)
      ```

      `repeated .protocol.MarketOrder orders = 1;`
    - #### addAllOrders

      ```
      public Response.MarketOrderList.Builder addAllOrders(java.lang.Iterable<? extends Response.MarketOrder> values)
      ```

      `repeated .protocol.MarketOrder orders = 1;`
    - #### clearOrders

      ```
      public Response.MarketOrderList.Builder clearOrders()
      ```

      `repeated .protocol.MarketOrder orders = 1;`
    - #### removeOrders

      ```
      public Response.MarketOrderList.Builder removeOrders(int index)
      ```

      `repeated .protocol.MarketOrder orders = 1;`
    - #### getOrdersBuilder

      ```
      public Response.MarketOrder.Builder getOrdersBuilder(int index)
      ```

      `repeated .protocol.MarketOrder orders = 1;`
    - #### getOrdersOrBuilder

      ```
      public Response.MarketOrderOrBuilder getOrdersOrBuilder(int index)
      ```

      `repeated .protocol.MarketOrder orders = 1;`

      Specified by:
      :   `getOrdersOrBuilder` in interface `Response.MarketOrderListOrBuilder`
    - #### getOrdersOrBuilderList

      ```
      public java.util.List<? extends Response.MarketOrderOrBuilder> getOrdersOrBuilderList()
      ```

      `repeated .protocol.MarketOrder orders = 1;`

      Specified by:
      :   `getOrdersOrBuilderList` in interface `Response.MarketOrderListOrBuilder`
    - #### addOrdersBuilder

      ```
      public Response.MarketOrder.Builder addOrdersBuilder()
      ```

      `repeated .protocol.MarketOrder orders = 1;`
    - #### addOrdersBuilder

      ```
      public Response.MarketOrder.Builder addOrdersBuilder(int index)
      ```

      `repeated .protocol.MarketOrder orders = 1;`
    - #### getOrdersBuilderList

      ```
      public java.util.List<Response.MarketOrder.Builder> getOrdersBuilderList()
      ```

      `repeated .protocol.MarketOrder orders = 1;`
    - #### setUnknownFields

      ```
      public final Response.MarketOrderList.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderList.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.MarketOrderList.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.MarketOrderList.Builder>`