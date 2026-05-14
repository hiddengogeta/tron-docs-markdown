

org.tron.trident.core.contract

## Class ContractConstructor

* java.lang.Object
* + org.tron.trident.core.contract.ContractConstructor

* ---

    

  ```
  public class ContractConstructor
  extends java.lang.Object
  ```

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `ContractConstructor(Common.SmartContract.ABI.Entry raw)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `void` | `encodeParameter(java.util.List<Type<?>> params)` |
    | `com.google.protobuf.ByteString` | `getBytecode()` |
    | `java.util.List<java.lang.String>` | `getParamTypes()` |
    | `boolean` | `getPayable()` |
    | `Common.SmartContract.ABI.Entry` | `getRawConstructor()` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### ContractConstructor

      ```
      public ContractConstructor(Common.SmartContract.ABI.Entry raw)
      ```
  + ### Method Detail

    - #### getRawConstructor

      ```
      public Common.SmartContract.ABI.Entry getRawConstructor()
      ```
    - #### getParamTypes

      ```
      public java.util.List<java.lang.String> getParamTypes()
      ```
    - #### getPayable

      ```
      public boolean getPayable()
      ```
    - #### getBytecode

      ```
      public com.google.protobuf.ByteString getBytecode()
      ```
    - #### encodeParameter

      ```
      public void encodeParameter(java.util.List<Type<?>> params)
                           throws ContractCreateException
      ```

      Throws:
      :   `ContractCreateException`