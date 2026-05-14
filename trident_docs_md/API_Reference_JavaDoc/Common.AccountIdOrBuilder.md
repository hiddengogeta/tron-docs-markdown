

org.tron.trident.proto

## Interface Common.AccountIdOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Common.AccountId](../../../../org/tron/trident/proto/Common.AccountId.html "class in org.tron.trident.proto"), [Common.AccountId.Builder](../../../../org/tron/trident/proto/Common.AccountId.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Common](../../../../org/tron/trident/proto/Common.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Common.AccountIdOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getAddress()` `bytes address = 2;` |
    | `com.google.protobuf.ByteString` | `getName()` `bytes name = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getName

      ```
      com.google.protobuf.ByteString getName()
      ```

      `bytes name = 1;`

      Returns:
      :   The name.
    - #### getAddress

      ```
      com.google.protobuf.ByteString getAddress()
      ```

      `bytes address = 2;`

      Returns:
      :   The address.