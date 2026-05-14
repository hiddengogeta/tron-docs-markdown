

org.tron.trident.proto

## Interface Common.KeyOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Common.Key](../../../../org/tron/trident/proto/Common.Key.html "class in org.tron.trident.proto"), [Common.Key.Builder](../../../../org/tron/trident/proto/Common.Key.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Common](../../../../org/tron/trident/proto/Common.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Common.KeyOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getAddress()` `bytes address = 1;` |
    | `long` | `getWeight()` `int64 weight = 2;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getAddress

      ```
      com.google.protobuf.ByteString getAddress()
      ```

      `bytes address = 1;`

      Returns:
      :   The address.
    - #### getWeight

      ```
      long getWeight()
      ```

      `int64 weight = 2;`

      Returns:
      :   The weight.