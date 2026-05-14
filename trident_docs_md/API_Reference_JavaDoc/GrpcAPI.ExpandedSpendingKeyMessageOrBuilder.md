

org.tron.trident.api

## Interface GrpcAPI.ExpandedSpendingKeyMessageOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.ExpandedSpendingKeyMessage](../../../../org/tron/trident/api/GrpcAPI.ExpandedSpendingKeyMessage.html "class in org.tron.trident.api"), [GrpcAPI.ExpandedSpendingKeyMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.ExpandedSpendingKeyMessage.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.ExpandedSpendingKeyMessageOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getAsk()` `bytes ask = 1;` |
    | `com.google.protobuf.ByteString` | `getNsk()` `bytes nsk = 2;` |
    | `com.google.protobuf.ByteString` | `getOvk()` `bytes ovk = 3;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getAsk

      ```
      com.google.protobuf.ByteString getAsk()
      ```

      `bytes ask = 1;`

      Returns:
      :   The ask.
    - #### getNsk

      ```
      com.google.protobuf.ByteString getNsk()
      ```

      `bytes nsk = 2;`

      Returns:
      :   The nsk.
    - #### getOvk

      ```
      com.google.protobuf.ByteString getOvk()
      ```

      `bytes ovk = 3;`

      Returns:
      :   The ovk.