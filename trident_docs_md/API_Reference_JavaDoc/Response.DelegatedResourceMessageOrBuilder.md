

org.tron.trident.proto

## Interface Response.DelegatedResourceMessageOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.DelegatedResourceMessage](../../../../org/tron/trident/proto/Response.DelegatedResourceMessage.html "class in org.tron.trident.proto"), [Response.DelegatedResourceMessage.Builder](../../../../org/tron/trident/proto/Response.DelegatedResourceMessage.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.DelegatedResourceMessageOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getFromAddress()` `bytes from_address = 1;` |
    | `com.google.protobuf.ByteString` | `getToAddress()` `bytes to_address = 2;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getFromAddress

      ```
      com.google.protobuf.ByteString getFromAddress()
      ```

      `bytes from_address = 1;`

      Returns:
      :   The fromAddress.
    - #### getToAddress

      ```
      com.google.protobuf.ByteString getToAddress()
      ```

      `bytes to_address = 2;`

      Returns:
      :   The toAddress.