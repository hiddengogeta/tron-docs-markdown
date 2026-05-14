

org.tron.trident.core.transaction

## Class TransactionBuilder

* java.lang.Object
* + org.tron.trident.core.transaction.TransactionBuilder

* ---

    

  ```
  public class TransactionBuilder
  extends java.lang.Object
  ```

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `TransactionBuilder(Chain.Transaction transaction)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Chain.Transaction` | `build()` |
    | `TransactionBuilder` | `setContractPermissionId(int permissionId)` Set permission id for Transaction.Contract This is a helper method for multi-sign transactions |
    | `TransactionBuilder` | `setFeeLimit(long feeLimit)` |
    | `TransactionBuilder` | `setMemo(byte[] memo)` |
    | `TransactionBuilder` | `setMemo(java.lang.String memo)` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### TransactionBuilder

      ```
      public TransactionBuilder(Chain.Transaction transaction)
      ```
  + ### Method Detail

    - #### setFeeLimit

      ```
      public TransactionBuilder setFeeLimit(long feeLimit)
      ```
    - #### setMemo

      ```
      public TransactionBuilder setMemo(byte[] memo)
      ```
    - #### setMemo

      ```
      public TransactionBuilder setMemo(java.lang.String memo)
      ```
    - #### setContractPermissionId

      ```
      public TransactionBuilder setContractPermissionId(int permissionId)
      ```

      Set permission id for Transaction.Contract
      This is a helper method for multi-sign transactions
    - #### build

      ```
      public Chain.Transaction build()
      ```