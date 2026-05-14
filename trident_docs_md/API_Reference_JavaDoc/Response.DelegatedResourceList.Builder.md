

org.tron.trident.proto

## Class Response.DelegatedResourceList.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.DelegatedResourceList.Builder](../../../../org/tron/trident/proto/Response.DelegatedResourceList.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.DelegatedResourceList.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.DelegatedResourceListOrBuilder](../../../../org/tron/trident/proto/Response.DelegatedResourceListOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.DelegatedResourceList](../../../../org/tron/trident/proto/Response.DelegatedResourceList.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.DelegatedResourceList.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceList.Builder>
  implements Response.DelegatedResourceListOrBuilder
  ```

  Protobuf type `protocol.DelegatedResourceList`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.DelegatedResourceList.Builder` | `addAllDelegatedResource(java.lang.Iterable<? extends Response.DelegatedResource> values)` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `Response.DelegatedResourceList.Builder` | `addDelegatedResource(int index, Response.DelegatedResource.Builder builderForValue)` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `Response.DelegatedResourceList.Builder` | `addDelegatedResource(int index, Response.DelegatedResource value)` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `Response.DelegatedResourceList.Builder` | `addDelegatedResource(Response.DelegatedResource.Builder builderForValue)` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `Response.DelegatedResourceList.Builder` | `addDelegatedResource(Response.DelegatedResource value)` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `Response.DelegatedResource.Builder` | `addDelegatedResourceBuilder()` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `Response.DelegatedResource.Builder` | `addDelegatedResourceBuilder(int index)` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `Response.DelegatedResourceList.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.DelegatedResourceList` | `build()` |
    | `Response.DelegatedResourceList` | `buildPartial()` |
    | `Response.DelegatedResourceList.Builder` | `clear()` |
    | `Response.DelegatedResourceList.Builder` | `clearDelegatedResource()` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `Response.DelegatedResourceList.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.DelegatedResourceList.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.DelegatedResourceList.Builder` | `clone()` |
    | `Response.DelegatedResourceList` | `getDefaultInstanceForType()` |
    | `Response.DelegatedResource` | `getDelegatedResource(int index)` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `Response.DelegatedResource.Builder` | `getDelegatedResourceBuilder(int index)` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `java.util.List<Response.DelegatedResource.Builder>` | `getDelegatedResourceBuilderList()` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `int` | `getDelegatedResourceCount()` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `java.util.List<Response.DelegatedResource>` | `getDelegatedResourceList()` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `Response.DelegatedResourceOrBuilder` | `getDelegatedResourceOrBuilder(int index)` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `java.util.List<? extends Response.DelegatedResourceOrBuilder>` | `getDelegatedResourceOrBuilderList()` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.DelegatedResourceList.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.DelegatedResourceList.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.DelegatedResourceList.Builder` | `mergeFrom(Response.DelegatedResourceList other)` |
    | `Response.DelegatedResourceList.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.DelegatedResourceList.Builder` | `removeDelegatedResource(int index)` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `Response.DelegatedResourceList.Builder` | `setDelegatedResource(int index, Response.DelegatedResource.Builder builderForValue)` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `Response.DelegatedResourceList.Builder` | `setDelegatedResource(int index, Response.DelegatedResource value)` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `Response.DelegatedResourceList.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.DelegatedResourceList.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.DelegatedResourceList.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceList.Builder>`
    - #### clear

      ```
      public Response.DelegatedResourceList.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceList.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceList.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.DelegatedResourceList getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.DelegatedResourceList build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.DelegatedResourceList buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.DelegatedResourceList.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceList.Builder>`
    - #### setField

      ```
      public Response.DelegatedResourceList.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                             java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceList.Builder>`
    - #### clearField

      ```
      public Response.DelegatedResourceList.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceList.Builder>`
    - #### clearOneof

      ```
      public Response.DelegatedResourceList.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceList.Builder>`
    - #### setRepeatedField

      ```
      public Response.DelegatedResourceList.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     int index,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceList.Builder>`
    - #### addRepeatedField

      ```
      public Response.DelegatedResourceList.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceList.Builder>`
    - #### mergeFrom

      ```
      public Response.DelegatedResourceList.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.DelegatedResourceList.Builder>`
    - #### mergeFrom

      ```
      public Response.DelegatedResourceList.Builder mergeFrom(Response.DelegatedResourceList other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceList.Builder>`
    - #### mergeFrom

      ```
      public Response.DelegatedResourceList.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.DelegatedResourceList.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getDelegatedResourceList

      ```
      public java.util.List<Response.DelegatedResource> getDelegatedResourceList()
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`

      Specified by:
      :   `getDelegatedResourceList` in interface `Response.DelegatedResourceListOrBuilder`
    - #### getDelegatedResourceCount

      ```
      public int getDelegatedResourceCount()
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`

      Specified by:
      :   `getDelegatedResourceCount` in interface `Response.DelegatedResourceListOrBuilder`
    - #### getDelegatedResource

      ```
      public Response.DelegatedResource getDelegatedResource(int index)
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`

      Specified by:
      :   `getDelegatedResource` in interface `Response.DelegatedResourceListOrBuilder`
    - #### setDelegatedResource

      ```
      public Response.DelegatedResourceList.Builder setDelegatedResource(int index,
                                                                         Response.DelegatedResource value)
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`
    - #### setDelegatedResource

      ```
      public Response.DelegatedResourceList.Builder setDelegatedResource(int index,
                                                                         Response.DelegatedResource.Builder builderForValue)
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`
    - #### addDelegatedResource

      ```
      public Response.DelegatedResourceList.Builder addDelegatedResource(Response.DelegatedResource value)
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`
    - #### addDelegatedResource

      ```
      public Response.DelegatedResourceList.Builder addDelegatedResource(int index,
                                                                         Response.DelegatedResource value)
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`
    - #### addDelegatedResource

      ```
      public Response.DelegatedResourceList.Builder addDelegatedResource(Response.DelegatedResource.Builder builderForValue)
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`
    - #### addDelegatedResource

      ```
      public Response.DelegatedResourceList.Builder addDelegatedResource(int index,
                                                                         Response.DelegatedResource.Builder builderForValue)
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`
    - #### addAllDelegatedResource

      ```
      public Response.DelegatedResourceList.Builder addAllDelegatedResource(java.lang.Iterable<? extends Response.DelegatedResource> values)
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`
    - #### clearDelegatedResource

      ```
      public Response.DelegatedResourceList.Builder clearDelegatedResource()
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`
    - #### removeDelegatedResource

      ```
      public Response.DelegatedResourceList.Builder removeDelegatedResource(int index)
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`
    - #### getDelegatedResourceBuilder

      ```
      public Response.DelegatedResource.Builder getDelegatedResourceBuilder(int index)
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`
    - #### getDelegatedResourceOrBuilder

      ```
      public Response.DelegatedResourceOrBuilder getDelegatedResourceOrBuilder(int index)
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`

      Specified by:
      :   `getDelegatedResourceOrBuilder` in interface `Response.DelegatedResourceListOrBuilder`
    - #### getDelegatedResourceOrBuilderList

      ```
      public java.util.List<? extends Response.DelegatedResourceOrBuilder> getDelegatedResourceOrBuilderList()
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`

      Specified by:
      :   `getDelegatedResourceOrBuilderList` in interface `Response.DelegatedResourceListOrBuilder`
    - #### addDelegatedResourceBuilder

      ```
      public Response.DelegatedResource.Builder addDelegatedResourceBuilder()
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`
    - #### addDelegatedResourceBuilder

      ```
      public Response.DelegatedResource.Builder addDelegatedResourceBuilder(int index)
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`
    - #### getDelegatedResourceBuilderList

      ```
      public java.util.List<Response.DelegatedResource.Builder> getDelegatedResourceBuilderList()
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`
    - #### setUnknownFields

      ```
      public final Response.DelegatedResourceList.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceList.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.DelegatedResourceList.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DelegatedResourceList.Builder>`