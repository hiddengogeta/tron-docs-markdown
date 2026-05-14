

org.tron.trident.api

## Interface GrpcAPI.ViewingKeyMessageOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.ViewingKeyMessage](../../../../org/tron/trident/api/GrpcAPI.ViewingKeyMessage.html "class in org.tron.trident.api"), [GrpcAPI.ViewingKeyMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.ViewingKeyMessage.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.ViewingKeyMessageOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getAk()` `bytes ak = 1;` |
    | `com.google.protobuf.ByteString` | `getNk()` `bytes nk = 2;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getAk

      ```
      com.google.protobuf.ByteString getAk()
      ```

      `bytes ak = 1;`

      Returns:
      :   The ak.
    - #### getNk

      ```
      com.google.protobuf.ByteString getNk()
      ```

      `bytes nk = 2;`

      Returns:
      :   The nk.