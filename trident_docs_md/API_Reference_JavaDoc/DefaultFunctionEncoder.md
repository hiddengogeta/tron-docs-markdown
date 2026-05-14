

org.tron.trident.abi

## Class DefaultFunctionEncoder

* java.lang.Object
* + [org.tron.trident.abi.FunctionEncoder](../../../../org/tron/trident/abi/FunctionEncoder.html "class in org.tron.trident.abi")
  + - org.tron.trident.abi.DefaultFunctionEncoder

* ---

    

  ```
  public class DefaultFunctionEncoder
  extends FunctionEncoder
  ```

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `DefaultFunctionEncoder()` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `java.lang.String` | `encodeFunction(Function function)` |
    | `java.lang.String` | `encodeParameters(java.util.List<Type> parameters)` |

    - ### Methods inherited from class org.tron.trident.abi.[FunctionEncoder](../../../../org/tron/trident/abi/FunctionEncoder.html "class in org.tron.trident.abi")

      `buildMethodId, buildMethodSignature, encode, encodeConstructor, makeFunction`
    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### DefaultFunctionEncoder

      ```
      public DefaultFunctionEncoder()
      ```
  + ### Method Detail

    - #### encodeFunction

      ```
      public java.lang.String encodeFunction(Function function)
      ```

      Specified by:
      :   `encodeFunction` in class `FunctionEncoder`
    - #### encodeParameters

      ```
      public java.lang.String encodeParameters(java.util.List<Type> parameters)
      ```

      Specified by:
      :   `encodeParameters` in class `FunctionEncoder`