

org.tron.trident.proto

## Interface Common.authorityOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Common.authority](../../../../org/tron/trident/proto/Common.authority.html "class in org.tron.trident.proto"), [Common.authority.Builder](../../../../org/tron/trident/proto/Common.authority.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Common](../../../../org/tron/trident/proto/Common.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Common.authorityOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Common.AccountId` | `getAccount()` `.protocol.AccountId account = 1;` |
    | `Common.AccountIdOrBuilder` | `getAccountOrBuilder()` `.protocol.AccountId account = 1;` |
    | `com.google.protobuf.ByteString` | `getPermissionName()` `bytes permission_name = 2;` |
    | `boolean` | `hasAccount()` `.protocol.AccountId account = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### hasAccount

      ```
      boolean hasAccount()
      ```

      `.protocol.AccountId account = 1;`

      Returns:
      :   Whether the account field is set.
    - #### getAccount

      ```
      Common.AccountId getAccount()
      ```

      `.protocol.AccountId account = 1;`

      Returns:
      :   The account.
    - #### getAccountOrBuilder

      ```
      Common.AccountIdOrBuilder getAccountOrBuilder()
      ```

      `.protocol.AccountId account = 1;`
    - #### getPermissionName

      ```
      com.google.protobuf.ByteString getPermissionName()
      ```

      `bytes permission_name = 2;`

      Returns:
      :   The permissionName.