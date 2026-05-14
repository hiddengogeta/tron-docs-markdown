

org.tron.trident.proto

## Interface Response.Account.UnFreezeV2OrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.Account.UnFreezeV2](../../../../org/tron/trident/proto/Response.Account.UnFreezeV2.html "class in org.tron.trident.proto"), [Response.Account.UnFreezeV2.Builder](../../../../org/tron/trident/proto/Response.Account.UnFreezeV2.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response.Account](../../../../org/tron/trident/proto/Response.Account.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.Account.UnFreezeV2OrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Common.ResourceCode` | `getType()` `.protocol.ResourceCode type = 1;` |
    | `int` | `getTypeValue()` `.protocol.ResourceCode type = 1;` |
    | `long` | `getUnfreezeAmount()` `int64 unfreeze_amount = 3;` |
    | `long` | `getUnfreezeExpireTime()` `int64 unfreeze_expire_time = 4;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getTypeValue

      ```
      int getTypeValue()
      ```

      `.protocol.ResourceCode type = 1;`

      Returns:
      :   The enum numeric value on the wire for type.
    - #### getType

      ```
      Common.ResourceCode getType()
      ```

      `.protocol.ResourceCode type = 1;`

      Returns:
      :   The type.
    - #### getUnfreezeAmount

      ```
      long getUnfreezeAmount()
      ```

      `int64 unfreeze_amount = 3;`

      Returns:
      :   The unfreezeAmount.
    - #### getUnfreezeExpireTime

      ```
      long getUnfreezeExpireTime()
      ```

      `int64 unfreeze_expire_time = 4;`

      Returns:
      :   The unfreezeExpireTime.