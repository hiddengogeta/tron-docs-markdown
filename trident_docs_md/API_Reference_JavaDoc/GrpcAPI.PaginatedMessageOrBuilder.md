

org.tron.trident.api

## Interface GrpcAPI.PaginatedMessageOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.PaginatedMessage](../../../../org/tron/trident/api/GrpcAPI.PaginatedMessage.html "class in org.tron.trident.api"), [GrpcAPI.PaginatedMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.PaginatedMessage.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.PaginatedMessageOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getLimit()` `int64 limit = 2;` |
    | `long` | `getOffset()` `int64 offset = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getOffset

      ```
      long getOffset()
      ```

      `int64 offset = 1;`

      Returns:
      :   The offset.
    - #### getLimit

      ```
      long getLimit()
      ```

      `int64 limit = 2;`

      Returns:
      :   The limit.