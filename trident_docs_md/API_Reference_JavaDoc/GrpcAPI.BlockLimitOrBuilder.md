

org.tron.trident.api

## Interface GrpcAPI.BlockLimitOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.BlockLimit](../../../../org/tron/trident/api/GrpcAPI.BlockLimit.html "class in org.tron.trident.api"), [GrpcAPI.BlockLimit.Builder](../../../../org/tron/trident/api/GrpcAPI.BlockLimit.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.BlockLimitOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getEndNum()` `int64 endNum = 2;` |
    | `long` | `getStartNum()` `int64 startNum = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getStartNum

      ```
      long getStartNum()
      ```

      `int64 startNum = 1;`

      Returns:
      :   The startNum.
    - #### getEndNum

      ```
      long getEndNum()
      ```

      `int64 endNum = 2;`

      Returns:
      :   The endNum.