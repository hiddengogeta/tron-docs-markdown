

org.tron.trident.core.contract

## Class ContractFunction

* java.lang.Object
* + org.tron.trident.core.contract.ContractFunction

* ---

    

  ```
  public class ContractFunction
  extends java.lang.Object
  ```

  The class `ContractFunction` provides a easier way to access smart contract
  functions.

  With a `ContractFunction` object, it's easy for users to see the function
  declaration and easy to call by construct a [`Function`](../../../../../org/tron/trident/abi/datatypes/Function.html "class in org.tron.trident.abi.datatypes")

  Since:
  :   jdk 1.8.0\_231

  See Also:
  :   [`Function`](../../../../../org/tron/trident/abi/datatypes/Function.html "class in org.tron.trident.abi.datatypes"),
      [`Common.SmartContract`](../../../../../org/tron/trident/proto/Common.SmartContract.html "class in org.tron.trident.proto")

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `ContractFunction.Builder` |
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `ContractFunction(ContractFunction.Builder builder)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Common.SmartContract.ABI.Entry` | `getAbi()` |
    | `int` | `getCallTokenId()` |
    | `long` | `getCallTokenValue()` |
    | `long` | `getCallValue()` |
    | `Contract` | `getCntr()` |
    | `java.util.List<java.lang.String>` | `getInputParams()` |
    | `java.util.List<java.lang.String>` | `getInputTypes()` |
    | `java.lang.String` | `getName()` |
    | `java.lang.String` | `getOutput()` |
    | `java.lang.String` | `getOutputType()` |
    | `com.google.protobuf.ByteString` | `getOwnerAddr()` |
    | `java.lang.String` | `getStateMutability()` |
    | `void` | `setAbi(Common.SmartContract.ABI.Entry abi)` |
    | `void` | `setCallTokenId(int callTokenId)` |
    | `void` | `setCallTokenValue(long callTokenValue)` |
    | `void` | `setCallValue(long callValue)` |
    | `void` | `setCntr(Contract cntr)` |
    | `void` | `setInputParams(java.util.List<java.lang.String> inputParams)` |
    | `void` | `setInputTypes(java.util.List<java.lang.String> inputTypes)` |
    | `void` | `setName(java.lang.String name)` |
    | `void` | `setOutput(java.lang.String outputs)` |
    | `void` | `setOutputType(java.lang.String outputType)` |
    | `void` | `setOwnerAddr(com.google.protobuf.ByteString ownerAddr)` |
    | `void` | `setStateMutability(java.lang.String stateMutability)` |
    | `java.lang.String` | `toString()` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

    - #### ContractFunction

      ```
      public ContractFunction(ContractFunction.Builder builder)
      ```
  + ### Method Detail

    - #### getName

      ```
      public java.lang.String getName()
      ```
    - #### setName

      ```
      public void setName(java.lang.String name)
      ```
    - #### getAbi

      ```
      public Common.SmartContract.ABI.Entry getAbi()
      ```
    - #### setAbi

      ```
      public void setAbi(Common.SmartContract.ABI.Entry abi)
      ```
    - #### getCntr

      ```
      public Contract getCntr()
      ```
    - #### setCntr

      ```
      public void setCntr(Contract cntr)
      ```
    - #### getOwnerAddr

      ```
      public com.google.protobuf.ByteString getOwnerAddr()
      ```
    - #### setOwnerAddr

      ```
      public void setOwnerAddr(com.google.protobuf.ByteString ownerAddr)
      ```
    - #### getInputParams

      ```
      public java.util.List<java.lang.String> getInputParams()
      ```
    - #### setInputParams

      ```
      public void setInputParams(java.util.List<java.lang.String> inputParams)
      ```
    - #### getInputTypes

      ```
      public java.util.List<java.lang.String> getInputTypes()
      ```
    - #### setInputTypes

      ```
      public void setInputTypes(java.util.List<java.lang.String> inputTypes)
      ```
    - #### getOutput

      ```
      public java.lang.String getOutput()
      ```
    - #### setOutput

      ```
      public void setOutput(java.lang.String outputs)
      ```
    - #### getOutputType

      ```
      public java.lang.String getOutputType()
      ```
    - #### setOutputType

      ```
      public void setOutputType(java.lang.String outputType)
      ```
    - #### getCallValue

      ```
      public long getCallValue()
      ```
    - #### setCallValue

      ```
      public void setCallValue(long callValue)
      ```
    - #### getCallTokenValue

      ```
      public long getCallTokenValue()
      ```
    - #### setCallTokenValue

      ```
      public void setCallTokenValue(long callTokenValue)
      ```
    - #### getCallTokenId

      ```
      public int getCallTokenId()
      ```
    - #### setCallTokenId

      ```
      public void setCallTokenId(int callTokenId)
      ```
    - #### getStateMutability

      ```
      public java.lang.String getStateMutability()
      ```
    - #### setStateMutability

      ```
      public void setStateMutability(java.lang.String stateMutability)
      ```
    - #### toString

      ```
      public java.lang.String toString()
      ```

      Overrides:
      :   `toString` in class `java.lang.Object`