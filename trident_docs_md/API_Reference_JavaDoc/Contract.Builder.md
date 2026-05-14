

org.tron.trident.core.contract

## Class Contract.Builder

* java.lang.Object
* + org.tron.trident.core.contract.Contract.Builder

* Enclosing class:
  :   [Contract](../../../../../org/tron/trident/core/contract/Contract.html "class in org.tron.trident.core.contract")

  ---

    

  ```
  public static class Contract.Builder
  extends java.lang.Object
  ```

* + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `protected Common.SmartContract.ABI` | `abi` |
    | `protected com.google.protobuf.ByteString` | `bytecode` |
    | `protected long` | `callValue` |
    | `protected com.google.protobuf.ByteString` | `cntrAddr` |
    | `protected com.google.protobuf.ByteString` | `codeHash` |
    | `protected long` | `consumeUserResourcePercent` |
    | `protected java.lang.String` | `name` |
    | `protected com.google.protobuf.ByteString` | `originAddr` |
    | `protected long` | `originEnergyLimit` |
    | `protected com.google.protobuf.ByteString` | `ownerAddr` |
    | `protected com.google.protobuf.ByteString` | `trxHash` |
    | `protected int` | `version` |
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `Builder()` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract` | `build()` |
    | `Contract.Builder` | `setAbi(Common.SmartContract.ABI abi)` |
    | `Contract.Builder` | `setAbi(java.lang.String abiString)` |
    | `Contract.Builder` | `setBytecode(com.google.protobuf.ByteString bytecode)` |
    | `Contract.Builder` | `setCallValue(long callValue)` |
    | `Contract.Builder` | `setCntrAddr(com.google.protobuf.ByteString cntrAddr)` |
    | `Contract.Builder` | `setCodeHash(com.google.protobuf.ByteString codeHash)` |
    | `Contract.Builder` | `setConsumeUserResourcePercent(long consumeUserResourcePercent)` |
    | `Contract.Builder` | `setName(java.lang.String name)` |
    | `Contract.Builder` | `setOriginAddr(com.google.protobuf.ByteString originAddr)` |
    | `Contract.Builder` | `setOriginEnergyLimit(long originEnergyLimit)` |
    | `Contract.Builder` | `setOwnerAddr(com.google.protobuf.ByteString ownerAddr)` |
    | `Contract.Builder` | `setTrxHash(com.google.protobuf.ByteString trxHash)` |
    | `Contract.Builder` | `setVersion(int version)` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Field Detail

    - #### originAddr

      ```
      protected com.google.protobuf.ByteString originAddr
      ```
    - #### cntrAddr

      ```
      protected com.google.protobuf.ByteString cntrAddr
      ```
    - #### abi

      ```
      protected Common.SmartContract.ABI abi
      ```
    - #### bytecode

      ```
      protected com.google.protobuf.ByteString bytecode
      ```
    - #### callValue

      ```
      protected long callValue
      ```
    - #### consumeUserResourcePercent

      ```
      protected long consumeUserResourcePercent
      ```
    - #### name

      ```
      protected java.lang.String name
      ```
    - #### originEnergyLimit

      ```
      protected long originEnergyLimit
      ```
    - #### codeHash

      ```
      protected com.google.protobuf.ByteString codeHash
      ```
    - #### trxHash

      ```
      protected com.google.protobuf.ByteString trxHash
      ```
    - #### version

      ```
      protected int version
      ```
    - #### ownerAddr

      ```
      protected com.google.protobuf.ByteString ownerAddr
      ```
  + ### Constructor Detail

    - #### Builder

      ```
      public Builder()
      ```
  + ### Method Detail

    - #### setOriginAddr

      ```
      public Contract.Builder setOriginAddr(com.google.protobuf.ByteString originAddr)
      ```
    - #### setCntrAddr

      ```
      public Contract.Builder setCntrAddr(com.google.protobuf.ByteString cntrAddr)
      ```
    - #### setAbi

      ```
      public Contract.Builder setAbi(Common.SmartContract.ABI abi)
      ```
    - #### setAbi

      ```
      public Contract.Builder setAbi(java.lang.String abiString)
                              throws java.lang.Exception
      ```

      Throws:
      :   `java.lang.Exception`
    - #### setBytecode

      ```
      public Contract.Builder setBytecode(com.google.protobuf.ByteString bytecode)
      ```
    - #### setCallValue

      ```
      public Contract.Builder setCallValue(long callValue)
      ```
    - #### setConsumeUserResourcePercent

      ```
      public Contract.Builder setConsumeUserResourcePercent(long consumeUserResourcePercent)
      ```
    - #### setName

      ```
      public Contract.Builder setName(java.lang.String name)
      ```
    - #### setOriginEnergyLimit

      ```
      public Contract.Builder setOriginEnergyLimit(long originEnergyLimit)
      ```
    - #### setCodeHash

      ```
      public Contract.Builder setCodeHash(com.google.protobuf.ByteString codeHash)
      ```
    - #### setTrxHash

      ```
      public Contract.Builder setTrxHash(com.google.protobuf.ByteString trxHash)
      ```
    - #### setVersion

      ```
      public Contract.Builder setVersion(int version)
      ```
    - #### setOwnerAddr

      ```
      public Contract.Builder setOwnerAddr(com.google.protobuf.ByteString ownerAddr)
      ```
    - #### build

      ```
      public Contract build()
      ```