

org.tron.trident.api

## Interface GrpcAPI.IncomingViewingKeyDiversifierMessageOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.IncomingViewingKeyDiversifierMessage](../../../../org/tron/trident/api/GrpcAPI.IncomingViewingKeyDiversifierMessage.html "class in org.tron.trident.api"), [GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.IncomingViewingKeyDiversifierMessage.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.IncomingViewingKeyDiversifierMessageOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.DiversifierMessage` | `getD()` `.protocol.DiversifierMessage d = 2;` |
    | `GrpcAPI.DiversifierMessageOrBuilder` | `getDOrBuilder()` `.protocol.DiversifierMessage d = 2;` |
    | `GrpcAPI.IncomingViewingKeyMessage` | `getIvk()` `.protocol.IncomingViewingKeyMessage ivk = 1;` |
    | `GrpcAPI.IncomingViewingKeyMessageOrBuilder` | `getIvkOrBuilder()` `.protocol.IncomingViewingKeyMessage ivk = 1;` |
    | `boolean` | `hasD()` `.protocol.DiversifierMessage d = 2;` |
    | `boolean` | `hasIvk()` `.protocol.IncomingViewingKeyMessage ivk = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### hasIvk

      ```
      boolean hasIvk()
      ```

      `.protocol.IncomingViewingKeyMessage ivk = 1;`

      Returns:
      :   Whether the ivk field is set.
    - #### getIvk

      ```
      GrpcAPI.IncomingViewingKeyMessage getIvk()
      ```

      `.protocol.IncomingViewingKeyMessage ivk = 1;`

      Returns:
      :   The ivk.
    - #### getIvkOrBuilder

      ```
      GrpcAPI.IncomingViewingKeyMessageOrBuilder getIvkOrBuilder()
      ```

      `.protocol.IncomingViewingKeyMessage ivk = 1;`
    - #### hasD

      ```
      boolean hasD()
      ```

      `.protocol.DiversifierMessage d = 2;`

      Returns:
      :   Whether the d field is set.
    - #### getD

      ```
      GrpcAPI.DiversifierMessage getD()
      ```

      `.protocol.DiversifierMessage d = 2;`

      Returns:
      :   The d.
    - #### getDOrBuilder

      ```
      GrpcAPI.DiversifierMessageOrBuilder getDOrBuilder()
      ```

      `.protocol.DiversifierMessage d = 2;`