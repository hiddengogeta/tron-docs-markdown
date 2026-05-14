

org.tron.trident.abi

## Class FunctionReturnDecoder

* java.lang.Object
* + org.tron.trident.abi.FunctionReturnDecoder

* Direct Known Subclasses:
  :   [DefaultFunctionReturnDecoder](../../../../org/tron/trident/abi/DefaultFunctionReturnDecoder.html "class in org.tron.trident.abi")

  ---

    

  ```
  public abstract class FunctionReturnDecoder
  extends java.lang.Object
  ```

  Decodes values returned by function or event calls.

  Delegates to [`DefaultFunctionReturnDecoder`](../../../../org/tron/trident/abi/DefaultFunctionReturnDecoder.html "class in org.tron.trident.abi") unless a [`FunctionReturnDecoderProvider`](../../../../org/tron/trident/abi/spi/FunctionReturnDecoderProvider.html "interface in org.tron.trident.abi.spi") SPI is found, in which case the first implementation found will be
  used.

  See Also:
  :   [`DefaultFunctionReturnDecoder`](../../../../org/tron/trident/abi/DefaultFunctionReturnDecoder.html "class in org.tron.trident.abi"),
      [`FunctionReturnDecoderProvider`](../../../../org/tron/trident/abi/spi/FunctionReturnDecoderProvider.html "interface in org.tron.trident.abi.spi")

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `FunctionReturnDecoder()` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static java.util.List<Type>` | `decode(java.lang.String rawInput, java.util.List<TypeReference<Type>> outputParameters)` Decode ABI encoded return values from smart contract function call. |
    | `protected abstract <T extends Type> Type` | `decodeEventParameter(java.lang.String rawInput, TypeReference<T> typeReference)` |
    | `protected abstract java.util.List<Type>` | `decodeFunctionResult(java.lang.String rawInput, java.util.List<TypeReference<Type>> outputParameters)` |
    | `static <T extends Type> Type` | `decodeIndexedValue(java.lang.String rawInput, TypeReference<T> typeReference)` Decodes an indexed parameter associated with an event. |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### FunctionReturnDecoder

      ```
      public FunctionReturnDecoder()
      ```
  + ### Method Detail

    - #### decode

      ```
      public static java.util.List<Type> decode(java.lang.String rawInput,
                                                java.util.List<TypeReference<Type>> outputParameters)
      ```

      Decode ABI encoded return values from smart contract function call.

      Parameters:
      :   `rawInput` - ABI encoded input
      :   `outputParameters` - list of return types as [`TypeReference`](../../../../org/tron/trident/abi/TypeReference.html "class in org.tron.trident.abi")

      Returns:
      :   `List` of values returned by function, `Collections.emptyList()` if
          invalid response
    - #### decodeIndexedValue

      ```
      public static <T extends Type> Type decodeIndexedValue(java.lang.String rawInput,
                                                             TypeReference<T> typeReference)
      ```

      Decodes an indexed parameter associated with an event. Indexed parameters are individually
      encoded, unlike non-indexed parameters which are encoded as per ABI-encoded function
      parameters and return values.

      If any of the following types are indexed, the Keccak-256 hashes of the values are
      returned instead. These are returned as a bytes32 value.
      * Arrays* Strings* Bytes

      See the [Solidity
      documentation](http://solidity.readthedocs.io/en/latest/contracts.html#events) for further information.

      Type Parameters:
      :   `T` - type of TypeReference

      Parameters:
      :   `rawInput` - ABI encoded input
      :   `typeReference` - of expected result type

      Returns:
      :   the decode value
    - #### decodeFunctionResult

      ```
      protected abstract java.util.List<Type> decodeFunctionResult(java.lang.String rawInput,
                                                                   java.util.List<TypeReference<Type>> outputParameters)
      ```
    - #### decodeEventParameter

      ```
      protected abstract <T extends Type> Type decodeEventParameter(java.lang.String rawInput,
                                                                    TypeReference<T> typeReference)
      ```