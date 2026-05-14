

org.tron.trident.proto

## Interface Common.NoteOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Common.Note](../../../../org/tron/trident/proto/Common.Note.html "class in org.tron.trident.proto"), [Common.Note.Builder](../../../../org/tron/trident/proto/Common.Note.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Common](../../../../org/tron/trident/proto/Common.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Common.NoteOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getMemo()` `bytes memo = 4;` |
    | `java.lang.String` | `getPaymentAddress()` `string payment_address = 2;` |
    | `com.google.protobuf.ByteString` | `getPaymentAddressBytes()` `string payment_address = 2;` |
    | `com.google.protobuf.ByteString` | `getRcm()` random 32 |
    | `long` | `getValue()` `int64 value = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getValue

      ```
      long getValue()
      ```

      `int64 value = 1;`

      Returns:
      :   The value.
    - #### getPaymentAddress

      ```
      java.lang.String getPaymentAddress()
      ```

      `string payment_address = 2;`

      Returns:
      :   The paymentAddress.
    - #### getPaymentAddressBytes

      ```
      com.google.protobuf.ByteString getPaymentAddressBytes()
      ```

      `string payment_address = 2;`

      Returns:
      :   The bytes for paymentAddress.
    - #### getRcm

      ```
      com.google.protobuf.ByteString getRcm()
      ```

      ```
       random 32
      ```

      `bytes rcm = 3;`

      Returns:
      :   The rcm.
    - #### getMemo

      ```
      com.google.protobuf.ByteString getMemo()
      ```

      `bytes memo = 4;`

      Returns:
      :   The memo.