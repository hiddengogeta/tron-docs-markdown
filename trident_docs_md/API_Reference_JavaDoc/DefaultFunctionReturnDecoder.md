

org.tron.trident.abi

## Class DefaultFunctionReturnDecoder

* java.lang.Object
* + [org.tron.trident.abi.FunctionReturnDecoder](../../../../org/tron/trident/abi/FunctionReturnDecoder.html "class in org.tron.trident.abi")
  + - org.tron.trident.abi.DefaultFunctionReturnDecoder

* ---

    

  ```
  public class DefaultFunctionReturnDecoder
  extends FunctionReturnDecoder
  ```

  Ethereum Contract Application Binary Interface (ABI) encoding for functions. Further details are
  available [here](https://github.com/ethereum/wiki/wiki/Ethereum-Contract-ABI).

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `DefaultFunctionReturnDecoder()` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `<T extends Type> Type` | `decodeEventParameter(java.lang.String rawInput, TypeReference<T> typeReference)` |
    | `java.util.List<Type>` | `decodeFunctionResult(java.lang.String rawInput, java.util.List<TypeReference<Type>> outputParameters)` |

    - ### Methods inherited from class org.tron.trident.abi.[FunctionReturnDecoder](../../../../org/tron/trident/abi/FunctionReturnDecoder.html "class in org.tron.trident.abi")

      `decode, decodeIndexedValue`
    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### DefaultFunctionReturnDecoder

      ```
      public DefaultFunctionReturnDecoder()
      ```
  + ### Method Detail

    - #### decodeFunctionResult

      ```
      public java.util.List<Type> decodeFunctionResult(java.lang.String rawInput,
                                                       java.util.List<TypeReference<Type>> outputParameters)
      ```

      Specified by:
      :   `decodeFunctionResult` in class `FunctionReturnDecoder`
    - #### decodeEventParameter

      ```
      public <T extends Type> Type decodeEventParameter(java.lang.String rawInput,
                                                        TypeReference<T> typeReference)
      ```

      Specified by:
      :   `decodeEventParameter` in class `FunctionReturnDecoder`