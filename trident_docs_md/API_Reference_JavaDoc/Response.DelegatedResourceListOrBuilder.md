

org.tron.trident.proto

## Interface Response.DelegatedResourceListOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.DelegatedResourceList](../../../../org/tron/trident/proto/Response.DelegatedResourceList.html "class in org.tron.trident.proto"), [Response.DelegatedResourceList.Builder](../../../../org/tron/trident/proto/Response.DelegatedResourceList.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.DelegatedResourceListOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Response.DelegatedResource` | `getDelegatedResource(int index)` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `int` | `getDelegatedResourceCount()` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `java.util.List<Response.DelegatedResource>` | `getDelegatedResourceList()` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `Response.DelegatedResourceOrBuilder` | `getDelegatedResourceOrBuilder(int index)` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `java.util.List<? extends Response.DelegatedResourceOrBuilder>` | `getDelegatedResourceOrBuilderList()` `repeated .protocol.DelegatedResource delegatedResource = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getDelegatedResourceList

      ```
      java.util.List<Response.DelegatedResource> getDelegatedResourceList()
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`
    - #### getDelegatedResource

      ```
      Response.DelegatedResource getDelegatedResource(int index)
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`
    - #### getDelegatedResourceCount

      ```
      int getDelegatedResourceCount()
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`
    - #### getDelegatedResourceOrBuilderList

      ```
      java.util.List<? extends Response.DelegatedResourceOrBuilder> getDelegatedResourceOrBuilderList()
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`
    - #### getDelegatedResourceOrBuilder

      ```
      Response.DelegatedResourceOrBuilder getDelegatedResourceOrBuilder(int index)
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`