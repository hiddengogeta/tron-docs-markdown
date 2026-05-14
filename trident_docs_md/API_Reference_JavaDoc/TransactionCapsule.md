

org.tron.trident.core.transaction

## Class TransactionCapsule

* java.lang.Object
* + org.tron.trident.core.transaction.TransactionCapsule

* ---

    

  ```
  public class TransactionCapsule
  extends java.lang.Object
  ```

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `TransactionCapsule(com.google.protobuf.Message message, Chain.Transaction.Contract.ContractType contractType)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `long` | `getBlockNum()` |
    | `long` | `getOrder()` |
    | `long` | `getTime()` |
    | `Chain.Transaction` | `getTransaction()` |
    | `boolean` | `isTransactionCreate()` |
    | `boolean` | `isVerified()` |
    | `void` | `setBlockNum(long blockNum)` |
    | `void` | `setExpiration(long expiration)` |
    | `void` | `setOrder(long order)` |
    | `void` | `setReference(long blockNum, byte[] blockHash)` |
    | `void` | `setTime(long time)` |
    | `void` | `setTimestamp()` |
    | `void` | `setTransaction(Chain.Transaction transaction)` |
    | `void` | `setTransactionCreate(boolean transactionCreate)` |
    | `void` | `setVerified(boolean verified)` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### TransactionCapsule

      ```
      public TransactionCapsule(com.google.protobuf.Message message,
                                Chain.Transaction.Contract.ContractType contractType)
      ```
  + ### Method Detail

    - #### isTransactionCreate

      ```
      public boolean isTransactionCreate()
      ```
    - #### setTransactionCreate

      ```
      public void setTransactionCreate(boolean transactionCreate)
      ```
    - #### getTransaction

      ```
      public Chain.Transaction getTransaction()
      ```
    - #### setTransaction

      ```
      public void setTransaction(Chain.Transaction transaction)
      ```
    - #### isVerified

      ```
      public boolean isVerified()
      ```
    - #### setVerified

      ```
      public void setVerified(boolean verified)
      ```
    - #### getBlockNum

      ```
      public long getBlockNum()
      ```
    - #### setBlockNum

      ```
      public void setBlockNum(long blockNum)
      ```
    - #### getTime

      ```
      public long getTime()
      ```
    - #### setTime

      ```
      public void setTime(long time)
      ```
    - #### getOrder

      ```
      public long getOrder()
      ```
    - #### setOrder

      ```
      public void setOrder(long order)
      ```
    - #### setReference

      ```
      public void setReference(long blockNum,
                               byte[] blockHash)
      ```
    - #### setExpiration

      ```
      public void setExpiration(long expiration)
      ```
    - #### setTimestamp

      ```
      public void setTimestamp()
      ```