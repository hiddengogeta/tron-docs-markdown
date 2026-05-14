

org.tron.trident.api

## Interface GrpcAPI.CanDelegatedMaxSizeResponseMessageOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.CanDelegatedMaxSizeResponseMessage](../../../../org/tron/trident/api/GrpcAPI.CanDelegatedMaxSizeResponseMessage.html "class in org.tron.trident.api"), [GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.CanDelegatedMaxSizeResponseMessage.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.CanDelegatedMaxSizeResponseMessageOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getMaxSize()` `int64 max_size = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getMaxSize

      ```
      long getMaxSize()
      ```

      `int64 max_size = 1;`

      Returns:
      :   The maxSize.