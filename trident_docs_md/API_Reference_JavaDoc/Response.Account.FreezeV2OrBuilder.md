

org.tron.trident.proto

## Interface Response.Account.FreezeV2OrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.Account.FreezeV2](../../../../org/tron/trident/proto/Response.Account.FreezeV2.html "class in org.tron.trident.proto"), [Response.Account.FreezeV2.Builder](../../../../org/tron/trident/proto/Response.Account.FreezeV2.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response.Account](../../../../org/tron/trident/proto/Response.Account.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.Account.FreezeV2OrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getAmount()` `int64 amount = 2;` |
    | `Common.ResourceCode` | `getType()` `.protocol.ResourceCode type = 1;` |
    | `int` | `getTypeValue()` `.protocol.ResourceCode type = 1;` |

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
    - #### getAmount

      ```
      long getAmount()
      ```

      `int64 amount = 2;`

      Returns:
      :   The amount.