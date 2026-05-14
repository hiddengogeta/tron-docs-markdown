

org.tron.trident.proto

## Interface Response.BlockListOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.BlockList](../../../../org/tron/trident/proto/Response.BlockList.html "class in org.tron.trident.proto"), [Response.BlockList.Builder](../../../../org/tron/trident/proto/Response.BlockList.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.BlockListOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Chain.Block` | `getBlock(int index)` `repeated .protocol.Block block = 1;` |
    | `int` | `getBlockCount()` `repeated .protocol.Block block = 1;` |
    | `java.util.List<Chain.Block>` | `getBlockList()` `repeated .protocol.Block block = 1;` |
    | `Chain.BlockOrBuilder` | `getBlockOrBuilder(int index)` `repeated .protocol.Block block = 1;` |
    | `java.util.List<? extends Chain.BlockOrBuilder>` | `getBlockOrBuilderList()` `repeated .protocol.Block block = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getBlockList

      ```
      java.util.List<Chain.Block> getBlockList()
      ```

      `repeated .protocol.Block block = 1;`
    - #### getBlock

      ```
      Chain.Block getBlock(int index)
      ```

      `repeated .protocol.Block block = 1;`
    - #### getBlockCount

      ```
      int getBlockCount()
      ```

      `repeated .protocol.Block block = 1;`
    - #### getBlockOrBuilderList

      ```
      java.util.List<? extends Chain.BlockOrBuilder> getBlockOrBuilderList()
      ```

      `repeated .protocol.Block block = 1;`
    - #### getBlockOrBuilder

      ```
      Chain.BlockOrBuilder getBlockOrBuilder(int index)
      ```

      `repeated .protocol.Block block = 1;`