

org.tron.trident.proto

## Interface Response.BlockIdentifierOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.BlockIdentifier](../../../../org/tron/trident/proto/Response.BlockIdentifier.html "class in org.tron.trident.proto"), [Response.BlockIdentifier.Builder](../../../../org/tron/trident/proto/Response.BlockIdentifier.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.BlockIdentifierOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getHash()` `bytes hash = 1;` |
    | `long` | `getNumber()` `int64 number = 2;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getHash

      ```
      com.google.protobuf.ByteString getHash()
      ```

      `bytes hash = 1;`

      Returns:
      :   The hash.
    - #### getNumber

      ```
      long getNumber()
      ```

      `int64 number = 2;`

      Returns:
      :   The number.