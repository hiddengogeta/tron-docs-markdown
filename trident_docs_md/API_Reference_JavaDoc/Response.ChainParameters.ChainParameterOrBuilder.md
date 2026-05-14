

org.tron.trident.proto

## Interface Response.ChainParameters.ChainParameterOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.ChainParameters.ChainParameter](../../../../org/tron/trident/proto/Response.ChainParameters.ChainParameter.html "class in org.tron.trident.proto"), [Response.ChainParameters.ChainParameter.Builder](../../../../org/tron/trident/proto/Response.ChainParameters.ChainParameter.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response.ChainParameters](../../../../org/tron/trident/proto/Response.ChainParameters.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.ChainParameters.ChainParameterOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `java.lang.String` | `getKey()` `string key = 1;` |
    | `com.google.protobuf.ByteString` | `getKeyBytes()` `string key = 1;` |
    | `long` | `getValue()` `int64 value = 2;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getKey

      ```
      java.lang.String getKey()
      ```

      `string key = 1;`

      Returns:
      :   The key.
    - #### getKeyBytes

      ```
      com.google.protobuf.ByteString getKeyBytes()
      ```

      `string key = 1;`

      Returns:
      :   The bytes for key.
    - #### getValue

      ```
      long getValue()
      ```

      `int64 value = 2;`

      Returns:
      :   The value.