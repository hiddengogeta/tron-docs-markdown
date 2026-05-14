

org.tron.trident.api

## Interface GrpcAPI.ShieldedAddressInfoOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.ShieldedAddressInfo](../../../../org/tron/trident/api/GrpcAPI.ShieldedAddressInfo.html "class in org.tron.trident.api"), [GrpcAPI.ShieldedAddressInfo.Builder](../../../../org/tron/trident/api/GrpcAPI.ShieldedAddressInfo.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.ShieldedAddressInfoOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getAk()` `bytes ak = 5;` |
    | `com.google.protobuf.ByteString` | `getAsk()` `bytes ask = 2;` |
    | `com.google.protobuf.ByteString` | `getD()` `bytes d = 8;` |
    | `com.google.protobuf.ByteString` | `getIvk()` `bytes ivk = 7;` |
    | `com.google.protobuf.ByteString` | `getNk()` `bytes nk = 6;` |
    | `com.google.protobuf.ByteString` | `getNsk()` `bytes nsk = 3;` |
    | `com.google.protobuf.ByteString` | `getOvk()` `bytes ovk = 4;` |
    | `java.lang.String` | `getPaymentAddress()` `string payment_address = 10;` |
    | `com.google.protobuf.ByteString` | `getPaymentAddressBytes()` `string payment_address = 10;` |
    | `com.google.protobuf.ByteString` | `getPkD()` `bytes pkD = 9;` |
    | `com.google.protobuf.ByteString` | `getSk()` `bytes sk = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getSk

      ```
      com.google.protobuf.ByteString getSk()
      ```

      `bytes sk = 1;`

      Returns:
      :   The sk.
    - #### getAsk

      ```
      com.google.protobuf.ByteString getAsk()
      ```

      `bytes ask = 2;`

      Returns:
      :   The ask.
    - #### getNsk

      ```
      com.google.protobuf.ByteString getNsk()
      ```

      `bytes nsk = 3;`

      Returns:
      :   The nsk.
    - #### getOvk

      ```
      com.google.protobuf.ByteString getOvk()
      ```

      `bytes ovk = 4;`

      Returns:
      :   The ovk.
    - #### getAk

      ```
      com.google.protobuf.ByteString getAk()
      ```

      `bytes ak = 5;`

      Returns:
      :   The ak.
    - #### getNk

      ```
      com.google.protobuf.ByteString getNk()
      ```

      `bytes nk = 6;`

      Returns:
      :   The nk.
    - #### getIvk

      ```
      com.google.protobuf.ByteString getIvk()
      ```

      `bytes ivk = 7;`

      Returns:
      :   The ivk.
    - #### getD

      ```
      com.google.protobuf.ByteString getD()
      ```

      `bytes d = 8;`

      Returns:
      :   The d.
    - #### getPkD

      ```
      com.google.protobuf.ByteString getPkD()
      ```

      `bytes pkD = 9;`

      Returns:
      :   The pkD.
    - #### getPaymentAddress

      ```
      java.lang.String getPaymentAddress()
      ```

      `string payment_address = 10;`

      Returns:
      :   The paymentAddress.
    - #### getPaymentAddressBytes

      ```
      com.google.protobuf.ByteString getPaymentAddressBytes()
      ```

      `string payment_address = 10;`

      Returns:
      :   The bytes for paymentAddress.