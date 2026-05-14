

org.tron.trident.proto

## Interface Response.DelegatedResourceAccountIndexOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.DelegatedResourceAccountIndex](../../../../org/tron/trident/proto/Response.DelegatedResourceAccountIndex.html "class in org.tron.trident.proto"), [Response.DelegatedResourceAccountIndex.Builder](../../../../org/tron/trident/proto/Response.DelegatedResourceAccountIndex.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.DelegatedResourceAccountIndexOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getAccount()` `bytes account = 1;` |
    | `com.google.protobuf.ByteString` | `getFromAccounts(int index)` `repeated bytes fromAccounts = 2;` |
    | `int` | `getFromAccountsCount()` `repeated bytes fromAccounts = 2;` |
    | `java.util.List<com.google.protobuf.ByteString>` | `getFromAccountsList()` `repeated bytes fromAccounts = 2;` |
    | `long` | `getTimestamp()` `int64 timestamp = 4;` |
    | `com.google.protobuf.ByteString` | `getToAccounts(int index)` `repeated bytes toAccounts = 3;` |
    | `int` | `getToAccountsCount()` `repeated bytes toAccounts = 3;` |
    | `java.util.List<com.google.protobuf.ByteString>` | `getToAccountsList()` `repeated bytes toAccounts = 3;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getAccount

      ```
      com.google.protobuf.ByteString getAccount()
      ```

      `bytes account = 1;`

      Returns:
      :   The account.
    - #### getFromAccountsList

      ```
      java.util.List<com.google.protobuf.ByteString> getFromAccountsList()
      ```

      `repeated bytes fromAccounts = 2;`

      Returns:
      :   A list containing the fromAccounts.
    - #### getFromAccountsCount

      ```
      int getFromAccountsCount()
      ```

      `repeated bytes fromAccounts = 2;`

      Returns:
      :   The count of fromAccounts.
    - #### getFromAccounts

      ```
      com.google.protobuf.ByteString getFromAccounts(int index)
      ```

      `repeated bytes fromAccounts = 2;`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The fromAccounts at the given index.
    - #### getToAccountsList

      ```
      java.util.List<com.google.protobuf.ByteString> getToAccountsList()
      ```

      `repeated bytes toAccounts = 3;`

      Returns:
      :   A list containing the toAccounts.
    - #### getToAccountsCount

      ```
      int getToAccountsCount()
      ```

      `repeated bytes toAccounts = 3;`

      Returns:
      :   The count of toAccounts.
    - #### getToAccounts

      ```
      com.google.protobuf.ByteString getToAccounts(int index)
      ```

      `repeated bytes toAccounts = 3;`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The toAccounts at the given index.
    - #### getTimestamp

      ```
      long getTimestamp()
      ```

      `int64 timestamp = 4;`

      Returns:
      :   The timestamp.