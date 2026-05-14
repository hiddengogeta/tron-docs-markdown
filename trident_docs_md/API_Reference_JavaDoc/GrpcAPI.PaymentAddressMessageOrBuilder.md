

org.tron.trident.api

## Interface GrpcAPI.PaymentAddressMessageOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.PaymentAddressMessage](../../../../org/tron/trident/api/GrpcAPI.PaymentAddressMessage.html "class in org.tron.trident.api"), [GrpcAPI.PaymentAddressMessage.Builder](../../../../org/tron/trident/api/GrpcAPI.PaymentAddressMessage.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.PaymentAddressMessageOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.DiversifierMessage` | `getD()` `.protocol.DiversifierMessage d = 1;` |
    | `GrpcAPI.DiversifierMessageOrBuilder` | `getDOrBuilder()` `.protocol.DiversifierMessage d = 1;` |
    | `java.lang.String` | `getPaymentAddress()` `string payment_address = 3;` |
    | `com.google.protobuf.ByteString` | `getPaymentAddressBytes()` `string payment_address = 3;` |
    | `com.google.protobuf.ByteString` | `getPkD()` `bytes pkD = 2;` |
    | `boolean` | `hasD()` `.protocol.DiversifierMessage d = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### hasD

      ```
      boolean hasD()
      ```

      `.protocol.DiversifierMessage d = 1;`

      Returns:
      :   Whether the d field is set.
    - #### getD

      ```
      GrpcAPI.DiversifierMessage getD()
      ```

      `.protocol.DiversifierMessage d = 1;`

      Returns:
      :   The d.
    - #### getDOrBuilder

      ```
      GrpcAPI.DiversifierMessageOrBuilder getDOrBuilder()
      ```

      `.protocol.DiversifierMessage d = 1;`
    - #### getPkD

      ```
      com.google.protobuf.ByteString getPkD()
      ```

      `bytes pkD = 2;`

      Returns:
      :   The pkD.
    - #### getPaymentAddress

      ```
      java.lang.String getPaymentAddress()
      ```

      `string payment_address = 3;`

      Returns:
      :   The paymentAddress.
    - #### getPaymentAddressBytes

      ```
      com.google.protobuf.ByteString getPaymentAddressBytes()
      ```

      `string payment_address = 3;`

      Returns:
      :   The bytes for paymentAddress.