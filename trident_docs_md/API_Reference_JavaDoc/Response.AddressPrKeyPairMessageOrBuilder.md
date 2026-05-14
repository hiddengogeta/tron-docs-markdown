

org.tron.trident.proto

## Interface Response.AddressPrKeyPairMessageOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.AddressPrKeyPairMessage](../../../../org/tron/trident/proto/Response.AddressPrKeyPairMessage.html "class in org.tron.trident.proto"), [Response.AddressPrKeyPairMessage.Builder](../../../../org/tron/trident/proto/Response.AddressPrKeyPairMessage.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.AddressPrKeyPairMessageOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `java.lang.String` | `getAddress()` `string address = 1;` |
    | `com.google.protobuf.ByteString` | `getAddressBytes()` `string address = 1;` |
    | `java.lang.String` | `getPrivateKey()` `string privateKey = 2;` |
    | `com.google.protobuf.ByteString` | `getPrivateKeyBytes()` `string privateKey = 2;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getAddress

      ```
      java.lang.String getAddress()
      ```

      `string address = 1;`

      Returns:
      :   The address.
    - #### getAddressBytes

      ```
      com.google.protobuf.ByteString getAddressBytes()
      ```

      `string address = 1;`

      Returns:
      :   The bytes for address.
    - #### getPrivateKey

      ```
      java.lang.String getPrivateKey()
      ```

      `string privateKey = 2;`

      Returns:
      :   The privateKey.
    - #### getPrivateKeyBytes

      ```
      com.google.protobuf.ByteString getPrivateKeyBytes()
      ```

      `string privateKey = 2;`

      Returns:
      :   The bytes for privateKey.