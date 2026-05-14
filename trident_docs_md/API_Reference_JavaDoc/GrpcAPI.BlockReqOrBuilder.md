

org.tron.trident.api

## Interface GrpcAPI.BlockReqOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.BlockReq](../../../../org/tron/trident/api/GrpcAPI.BlockReq.html "class in org.tron.trident.api"), [GrpcAPI.BlockReq.Builder](../../../../org/tron/trident/api/GrpcAPI.BlockReq.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.BlockReqOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `boolean` | `getDetail()` `bool detail = 2;` |
    | `java.lang.String` | `getIdOrNum()` `string id_or_num = 1;` |
    | `com.google.protobuf.ByteString` | `getIdOrNumBytes()` `string id_or_num = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getIdOrNum

      ```
      java.lang.String getIdOrNum()
      ```

      `string id_or_num = 1;`

      Returns:
      :   The idOrNum.
    - #### getIdOrNumBytes

      ```
      com.google.protobuf.ByteString getIdOrNumBytes()
      ```

      `string id_or_num = 1;`

      Returns:
      :   The bytes for idOrNum.
    - #### getDetail

      ```
      boolean getDetail()
      ```

      `bool detail = 2;`

      Returns:
      :   The detail.