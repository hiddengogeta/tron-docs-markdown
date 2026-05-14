

org.tron.trident.proto

## Interface Response.BlockListExtentionOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.BlockListExtention](../../../../org/tron/trident/proto/Response.BlockListExtention.html "class in org.tron.trident.proto"), [Response.BlockListExtention.Builder](../../../../org/tron/trident/proto/Response.BlockListExtention.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.BlockListExtentionOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Response.BlockExtention` | `getBlock(int index)` `repeated .protocol.BlockExtention block = 1;` |
    | `int` | `getBlockCount()` `repeated .protocol.BlockExtention block = 1;` |
    | `java.util.List<Response.BlockExtention>` | `getBlockList()` `repeated .protocol.BlockExtention block = 1;` |
    | `Response.BlockExtentionOrBuilder` | `getBlockOrBuilder(int index)` `repeated .protocol.BlockExtention block = 1;` |
    | `java.util.List<? extends Response.BlockExtentionOrBuilder>` | `getBlockOrBuilderList()` `repeated .protocol.BlockExtention block = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getBlockList

      ```
      java.util.List<Response.BlockExtention> getBlockList()
      ```

      `repeated .protocol.BlockExtention block = 1;`
    - #### getBlock

      ```
      Response.BlockExtention getBlock(int index)
      ```

      `repeated .protocol.BlockExtention block = 1;`
    - #### getBlockCount

      ```
      int getBlockCount()
      ```

      `repeated .protocol.BlockExtention block = 1;`
    - #### getBlockOrBuilderList

      ```
      java.util.List<? extends Response.BlockExtentionOrBuilder> getBlockOrBuilderList()
      ```

      `repeated .protocol.BlockExtention block = 1;`
    - #### getBlockOrBuilder

      ```
      Response.BlockExtentionOrBuilder getBlockOrBuilder(int index)
      ```

      `repeated .protocol.BlockExtention block = 1;`