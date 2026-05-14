

org.tron.trident.proto

## Interface Response.NodeListOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.NodeList](../../../../org/tron/trident/proto/Response.NodeList.html "class in org.tron.trident.proto"), [Response.NodeList.Builder](../../../../org/tron/trident/proto/Response.NodeList.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.NodeListOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Response.NodeList.Node` | `getNodes(int index)` `repeated .protocol.NodeList.Node nodes = 1;` |
    | `int` | `getNodesCount()` `repeated .protocol.NodeList.Node nodes = 1;` |
    | `java.util.List<Response.NodeList.Node>` | `getNodesList()` `repeated .protocol.NodeList.Node nodes = 1;` |
    | `Response.NodeList.NodeOrBuilder` | `getNodesOrBuilder(int index)` `repeated .protocol.NodeList.Node nodes = 1;` |
    | `java.util.List<? extends Response.NodeList.NodeOrBuilder>` | `getNodesOrBuilderList()` `repeated .protocol.NodeList.Node nodes = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getNodesList

      ```
      java.util.List<Response.NodeList.Node> getNodesList()
      ```

      `repeated .protocol.NodeList.Node nodes = 1;`
    - #### getNodes

      ```
      Response.NodeList.Node getNodes(int index)
      ```

      `repeated .protocol.NodeList.Node nodes = 1;`
    - #### getNodesCount

      ```
      int getNodesCount()
      ```

      `repeated .protocol.NodeList.Node nodes = 1;`
    - #### getNodesOrBuilderList

      ```
      java.util.List<? extends Response.NodeList.NodeOrBuilder> getNodesOrBuilderList()
      ```

      `repeated .protocol.NodeList.Node nodes = 1;`
    - #### getNodesOrBuilder

      ```
      Response.NodeList.NodeOrBuilder getNodesOrBuilder(int index)
      ```

      `repeated .protocol.NodeList.Node nodes = 1;`