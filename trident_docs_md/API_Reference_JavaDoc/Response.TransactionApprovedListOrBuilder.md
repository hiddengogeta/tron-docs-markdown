

org.tron.trident.proto

## Interface Response.TransactionApprovedListOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.TransactionApprovedList](../../../../org/tron/trident/proto/Response.TransactionApprovedList.html "class in org.tron.trident.proto"), [Response.TransactionApprovedList.Builder](../../../../org/tron/trident/proto/Response.TransactionApprovedList.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.TransactionApprovedListOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getApprovedList(int index)` `repeated bytes approved_list = 2;` |
    | `int` | `getApprovedListCount()` `repeated bytes approved_list = 2;` |
    | `java.util.List<com.google.protobuf.ByteString>` | `getApprovedListList()` `repeated bytes approved_list = 2;` |
    | `Response.TransactionApprovedList.Result` | `getResult()` `.protocol.TransactionApprovedList.Result result = 4;` |
    | `Response.TransactionApprovedList.ResultOrBuilder` | `getResultOrBuilder()` `.protocol.TransactionApprovedList.Result result = 4;` |
    | `Response.TransactionExtention` | `getTransaction()` `.protocol.TransactionExtention transaction = 5;` |
    | `Response.TransactionExtentionOrBuilder` | `getTransactionOrBuilder()` `.protocol.TransactionExtention transaction = 5;` |
    | `boolean` | `hasResult()` `.protocol.TransactionApprovedList.Result result = 4;` |
    | `boolean` | `hasTransaction()` `.protocol.TransactionExtention transaction = 5;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

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
    - #### hasResult

      ```
      boolean hasResult()
      ```

      `.protocol.TransactionApprovedList.Result result = 4;`

      Returns:
      :   Whether the result field is set.
    - #### getResult

      ```
      Response.TransactionApprovedList.Result getResult()
      ```

      `.protocol.TransactionApprovedList.Result result = 4;`

      Returns:
      :   The result.
    - #### getResultOrBuilder

      ```
      Response.TransactionApprovedList.ResultOrBuilder getResultOrBuilder()
      ```

      `.protocol.TransactionApprovedList.Result result = 4;`
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