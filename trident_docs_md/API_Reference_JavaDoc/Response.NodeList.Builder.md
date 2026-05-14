

org.tron.trident.proto

## Class Response.NodeList.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.NodeList.Builder](../../../../org/tron/trident/proto/Response.NodeList.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.NodeList.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.NodeListOrBuilder](../../../../org/tron/trident/proto/Response.NodeListOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.NodeList](../../../../org/tron/trident/proto/Response.NodeList.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.NodeList.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Builder>
  implements Response.NodeListOrBuilder
  ```

  ```
   Gossip node list
  ```

  Protobuf type `protocol.NodeList`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.NodeList.Builder` | `addAllNodes(java.lang.Iterable<? extends Response.NodeList.Node> values)` `repeated .protocol.NodeList.Node nodes = 1;` |
    | `Response.NodeList.Builder` | `addNodes(int index, Response.NodeList.Node.Builder builderForValue)` `repeated .protocol.NodeList.Node nodes = 1;` |
    | `Response.NodeList.Builder` | `addNodes(int index, Response.NodeList.Node value)` `repeated .protocol.NodeList.Node nodes = 1;` |
    | `Response.NodeList.Builder` | `addNodes(Response.NodeList.Node.Builder builderForValue)` `repeated .protocol.NodeList.Node nodes = 1;` |
    | `Response.NodeList.Builder` | `addNodes(Response.NodeList.Node value)` `repeated .protocol.NodeList.Node nodes = 1;` |
    | `Response.NodeList.Node.Builder` | `addNodesBuilder()` `repeated .protocol.NodeList.Node nodes = 1;` |
    | `Response.NodeList.Node.Builder` | `addNodesBuilder(int index)` `repeated .protocol.NodeList.Node nodes = 1;` |
    | `Response.NodeList.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.NodeList` | `build()` |
    | `Response.NodeList` | `buildPartial()` |
    | `Response.NodeList.Builder` | `clear()` |
    | `Response.NodeList.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.NodeList.Builder` | `clearNodes()` `repeated .protocol.NodeList.Node nodes = 1;` |
    | `Response.NodeList.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.NodeList.Builder` | `clone()` |
    | `Response.NodeList` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Response.NodeList.Node` | `getNodes(int index)` `repeated .protocol.NodeList.Node nodes = 1;` |
    | `Response.NodeList.Node.Builder` | `getNodesBuilder(int index)` `repeated .protocol.NodeList.Node nodes = 1;` |
    | `java.util.List<Response.NodeList.Node.Builder>` | `getNodesBuilderList()` `repeated .protocol.NodeList.Node nodes = 1;` |
    | `int` | `getNodesCount()` `repeated .protocol.NodeList.Node nodes = 1;` |
    | `java.util.List<Response.NodeList.Node>` | `getNodesList()` `repeated .protocol.NodeList.Node nodes = 1;` |
    | `Response.NodeList.NodeOrBuilder` | `getNodesOrBuilder(int index)` `repeated .protocol.NodeList.Node nodes = 1;` |
    | `java.util.List<? extends Response.NodeList.NodeOrBuilder>` | `getNodesOrBuilderList()` `repeated .protocol.NodeList.Node nodes = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.NodeList.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.NodeList.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.NodeList.Builder` | `mergeFrom(Response.NodeList other)` |
    | `Response.NodeList.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.NodeList.Builder` | `removeNodes(int index)` `repeated .protocol.NodeList.Node nodes = 1;` |
    | `Response.NodeList.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.NodeList.Builder` | `setNodes(int index, Response.NodeList.Node.Builder builderForValue)` `repeated .protocol.NodeList.Node nodes = 1;` |
    | `Response.NodeList.Builder` | `setNodes(int index, Response.NodeList.Node value)` `repeated .protocol.NodeList.Node nodes = 1;` |
    | `Response.NodeList.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.NodeList.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Builder>`
    - #### clear

      ```
      public Response.NodeList.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.NodeList getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.NodeList build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.NodeList buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.NodeList.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Builder>`
    - #### setField

      ```
      public Response.NodeList.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Builder>`
    - #### clearField

      ```
      public Response.NodeList.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Builder>`
    - #### clearOneof

      ```
      public Response.NodeList.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Builder>`
    - #### setRepeatedField

      ```
      public Response.NodeList.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                        int index,
                                                        java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Builder>`
    - #### addRepeatedField

      ```
      public Response.NodeList.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                        java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeList.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.NodeList.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeList.Builder mergeFrom(Response.NodeList other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeList.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                 com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                          throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.NodeList.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getNodesList

      ```
      public java.util.List<Response.NodeList.Node> getNodesList()
      ```

      `repeated .protocol.NodeList.Node nodes = 1;`

      Specified by:
      :   `getNodesList` in interface `Response.NodeListOrBuilder`
    - #### getNodesCount

      ```
      public int getNodesCount()
      ```

      `repeated .protocol.NodeList.Node nodes = 1;`

      Specified by:
      :   `getNodesCount` in interface `Response.NodeListOrBuilder`
    - #### getNodes

      ```
      public Response.NodeList.Node getNodes(int index)
      ```

      `repeated .protocol.NodeList.Node nodes = 1;`

      Specified by:
      :   `getNodes` in interface `Response.NodeListOrBuilder`
    - #### setNodes

      ```
      public Response.NodeList.Builder setNodes(int index,
                                                Response.NodeList.Node value)
      ```

      `repeated .protocol.NodeList.Node nodes = 1;`
    - #### setNodes

      ```
      public Response.NodeList.Builder setNodes(int index,
                                                Response.NodeList.Node.Builder builderForValue)
      ```

      `repeated .protocol.NodeList.Node nodes = 1;`
    - #### addNodes

      ```
      public Response.NodeList.Builder addNodes(Response.NodeList.Node value)
      ```

      `repeated .protocol.NodeList.Node nodes = 1;`
    - #### addNodes

      ```
      public Response.NodeList.Builder addNodes(int index,
                                                Response.NodeList.Node value)
      ```

      `repeated .protocol.NodeList.Node nodes = 1;`
    - #### addNodes

      ```
      public Response.NodeList.Builder addNodes(Response.NodeList.Node.Builder builderForValue)
      ```

      `repeated .protocol.NodeList.Node nodes = 1;`
    - #### addNodes

      ```
      public Response.NodeList.Builder addNodes(int index,
                                                Response.NodeList.Node.Builder builderForValue)
      ```

      `repeated .protocol.NodeList.Node nodes = 1;`
    - #### addAllNodes

      ```
      public Response.NodeList.Builder addAllNodes(java.lang.Iterable<? extends Response.NodeList.Node> values)
      ```

      `repeated .protocol.NodeList.Node nodes = 1;`
    - #### clearNodes

      ```
      public Response.NodeList.Builder clearNodes()
      ```

      `repeated .protocol.NodeList.Node nodes = 1;`
    - #### removeNodes

      ```
      public Response.NodeList.Builder removeNodes(int index)
      ```

      `repeated .protocol.NodeList.Node nodes = 1;`
    - #### getNodesBuilder

      ```
      public Response.NodeList.Node.Builder getNodesBuilder(int index)
      ```

      `repeated .protocol.NodeList.Node nodes = 1;`
    - #### getNodesOrBuilder

      ```
      public Response.NodeList.NodeOrBuilder getNodesOrBuilder(int index)
      ```

      `repeated .protocol.NodeList.Node nodes = 1;`

      Specified by:
      :   `getNodesOrBuilder` in interface `Response.NodeListOrBuilder`
    - #### getNodesOrBuilderList

      ```
      public java.util.List<? extends Response.NodeList.NodeOrBuilder> getNodesOrBuilderList()
      ```

      `repeated .protocol.NodeList.Node nodes = 1;`

      Specified by:
      :   `getNodesOrBuilderList` in interface `Response.NodeListOrBuilder`
    - #### addNodesBuilder

      ```
      public Response.NodeList.Node.Builder addNodesBuilder()
      ```

      `repeated .protocol.NodeList.Node nodes = 1;`
    - #### addNodesBuilder

      ```
      public Response.NodeList.Node.Builder addNodesBuilder(int index)
      ```

      `repeated .protocol.NodeList.Node nodes = 1;`
    - #### getNodesBuilderList

      ```
      public java.util.List<Response.NodeList.Node.Builder> getNodesBuilderList()
      ```

      `repeated .protocol.NodeList.Node nodes = 1;`
    - #### setUnknownFields

      ```
      public final Response.NodeList.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.NodeList.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeList.Builder>`