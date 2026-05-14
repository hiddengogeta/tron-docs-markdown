

org.tron.trident.proto

## Interface Response.TransactionSignWeightOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.TransactionSignWeight](../../../../org/tron/trident/proto/Response.TransactionSignWeight.html "class in org.tron.trident.proto"), [Response.TransactionSignWeight.Builder](../../../../org/tron/trident/proto/Response.TransactionSignWeight.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.TransactionSignWeightOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getApprovedList(int index)` `repeated bytes approved_list = 2;` |
    | `int` | `getApprovedListCount()` `repeated bytes approved_list = 2;` |
    | `java.util.List<com.google.protobuf.ByteString>` | `getApprovedListList()` `repeated bytes approved_list = 2;` |
    | `long` | `getCurrentWeight()` `int64 current_weight = 3;` |
    | `Common.Permission` | `getPermission()` `.protocol.Permission permission = 1;` |
    | `Common.PermissionOrBuilder` | `getPermissionOrBuilder()` `.protocol.Permission permission = 1;` |
    | `Response.TransactionSignWeight.Result` | `getResult()` `.protocol.TransactionSignWeight.Result result = 4;` |
    | `Response.TransactionSignWeight.ResultOrBuilder` | `getResultOrBuilder()` `.protocol.TransactionSignWeight.Result result = 4;` |
    | `Response.TransactionExtention` | `getTransaction()` `.protocol.TransactionExtention transaction = 5;` |
    | `Response.TransactionExtentionOrBuilder` | `getTransactionOrBuilder()` `.protocol.TransactionExtention transaction = 5;` |
    | `boolean` | `hasPermission()` `.protocol.Permission permission = 1;` |
    | `boolean` | `hasResult()` `.protocol.TransactionSignWeight.Result result = 4;` |
    | `boolean` | `hasTransaction()` `.protocol.TransactionExtention transaction = 5;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### hasPermission

      ```
      boolean hasPermission()
      ```

      `.protocol.Permission permission = 1;`

      Returns:
      :   Whether the permission field is set.
    - #### getPermission

      ```
      Common.Permission getPermission()
      ```

      `.protocol.Permission permission = 1;`

      Returns:
      :   The permission.
    - #### getPermissionOrBuilder

      ```
      Common.PermissionOrBuilder getPermissionOrBuilder()
      ```

      `.protocol.Permission permission = 1;`
    - #### getApprovedListList

      ```
      java.util.List<com.google.protobuf.ByteString> getApprovedListList()
      ```

      `repeated bytes approved_list = 2;`

      Returns:
      :   A list containing the approvedList.
    - #### getApprovedListCount

      ```
      int getApprovedListCount()
      ```

      `repeated bytes approved_list = 2;`

      Returns:
      :   The count of approvedList.
    - #### getApprovedList

      ```
      com.google.protobuf.ByteString getApprovedList(int index)
      ```

      `repeated bytes approved_list = 2;`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The approvedList at the given index.
    - #### getCurrentWeight

      ```
      long getCurrentWeight()
      ```

      `int64 current_weight = 3;`

      Returns:
      :   The currentWeight.
    - #### hasResult

      ```
      boolean hasResult()
      ```

      `.protocol.TransactionSignWeight.Result result = 4;`

      Returns:
      :   Whether the result field is set.
    - #### getResult

      ```
      Response.TransactionSignWeight.Result getResult()
      ```

      `.protocol.TransactionSignWeight.Result result = 4;`

      Returns:
      :   The result.
    - #### getResultOrBuilder

      ```
      Response.TransactionSignWeight.ResultOrBuilder getResultOrBuilder()
      ```

      `.protocol.TransactionSignWeight.Result result = 4;`
    - #### hasTransaction

      ```
      boolean hasTransaction()
      ```

      `.protocol.TransactionExtention transaction = 5;`

      Returns:
      :   Whether the transaction field is set.
    - #### getTransaction

      ```
      Response.TransactionExtention getTransaction()
      ```

      `.protocol.TransactionExtention transaction = 5;`

      Returns:
      :   The transaction.
    - #### getTransactionOrBuilder

      ```
      Response.TransactionExtentionOrBuilder getTransactionOrBuilder()
      ```

      `.protocol.TransactionExtention transaction = 5;`