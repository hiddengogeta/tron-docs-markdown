

org.tron.trident.core.contract

## Class ContractFunction.Builder

* java.lang.Object
* + org.tron.trident.core.contract.ContractFunction.Builder

* Enclosing class:
  :   [ContractFunction](../../../../../org/tron/trident/core/contract/ContractFunction.html "class in org.tron.trident.core.contract")

  ---

    

  ```
  public static class ContractFunction.Builder
  extends java.lang.Object
  ```

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `Builder()` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `ContractFunction` | `build()` |
    | `ContractFunction.Builder` | `setAbi(Common.SmartContract.ABI.Entry abi)` |
    | `ContractFunction.Builder` | `setCallTokenId(int callTokenId)` |
    | `ContractFunction.Builder` | `setCallTokenValue(long callTokenValue)` |
    | `ContractFunction.Builder` | `setCallValue(long callValue)` |
    | `ContractFunction.Builder` | `setCntr(Contract cntr)` |
    | `ContractFunction.Builder` | `setInputParams(java.util.List<java.lang.String> inputParams)` |
    | `ContractFunction.Builder` | `setInputTypes(java.util.List<java.lang.String> inputTypes)` |
    | `ContractFunction.Builder` | `setName(java.lang.String name)` |
    | `ContractFunction.Builder` | `setOutput(java.lang.String output)` |
    | `ContractFunction.Builder` | `setOutputType(java.lang.String outputType)` |
    | `ContractFunction.Builder` | `setOwnerAddr(com.google.protobuf.ByteString ownerAddr)` |
    | `ContractFunction.Builder` | `setStateMutability(java.lang.String stateMutability)` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### Builder

      ```
      public Builder()
      ```
  + ### Method Detail

    - #### setName

      ```
      public ContractFunction.Builder setName(java.lang.String name)
      ```
    - #### setAbi

      ```
      public ContractFunction.Builder setAbi(Common.SmartContract.ABI.Entry abi)
      ```
    - #### setCntr

      ```
      public ContractFunction.Builder setCntr(Contract cntr)
      ```
    - #### setOwnerAddr

      ```
      public ContractFunction.Builder setOwnerAddr(com.google.protobuf.ByteString ownerAddr)
      ```
    - #### setInputParams

      ```
      public ContractFunction.Builder setInputParams(java.util.List<java.lang.String> inputParams)
      ```
    - #### setInputTypes

      ```
      public ContractFunction.Builder setInputTypes(java.util.List<java.lang.String> inputTypes)
      ```
    - #### setOutput

      ```
      public ContractFunction.Builder setOutput(java.lang.String output)
      ```
    - #### setOutputType

      ```
      public ContractFunction.Builder setOutputType(java.lang.String outputType)
      ```
    - #### setCallValue

      ```
      public ContractFunction.Builder setCallValue(long callValue)
      ```
    - #### setCallTokenValue

      ```
      public ContractFunction.Builder setCallTokenValue(long callTokenValue)
      ```
    - #### setCallTokenId

      ```
      public ContractFunction.Builder setCallTokenId(int callTokenId)
      ```
    - #### setStateMutability

      ```
      public ContractFunction.Builder setStateMutability(java.lang.String stateMutability)
      ```
    - #### build

      ```
      public ContractFunction build()
      ```