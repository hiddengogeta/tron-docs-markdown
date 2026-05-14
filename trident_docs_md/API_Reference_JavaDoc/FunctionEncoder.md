

org.tron.trident.abi

## Class FunctionEncoder

* java.lang.Object
* + org.tron.trident.abi.FunctionEncoder

* Direct Known Subclasses:
  :   [DefaultFunctionEncoder](../../../../org/tron/trident/abi/DefaultFunctionEncoder.html "class in org.tron.trident.abi")

  ---

    

  ```
  public abstract class FunctionEncoder
  extends java.lang.Object
  ```

  Delegates to [`DefaultFunctionEncoder`](../../../../org/tron/trident/abi/DefaultFunctionEncoder.html "class in org.tron.trident.abi") unless a [`FunctionEncoderProvider`](../../../../org/tron/trident/abi/spi/FunctionEncoderProvider.html "interface in org.tron.trident.abi.spi") SPI is
  found, in which case the first implementation found will be used.

  See Also:
  :   [`DefaultFunctionEncoder`](../../../../org/tron/trident/abi/DefaultFunctionEncoder.html "class in org.tron.trident.abi"),
      [`FunctionEncoderProvider`](../../../../org/tron/trident/abi/spi/FunctionEncoderProvider.html "interface in org.tron.trident.abi.spi")

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `FunctionEncoder()` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `protected static java.lang.String` | `buildMethodId(java.lang.String methodSignature)` |
    | `protected static java.lang.String` | `buildMethodSignature(java.lang.String methodName, java.util.List<Type> parameters)` |
    | `static java.lang.String` | `encode(Function function)` |
    | `static java.lang.String` | `encodeConstructor(java.util.List<Type> parameters)` |
    | `protected abstract java.lang.String` | `encodeFunction(Function function)` |
    | `protected abstract java.lang.String` | `encodeParameters(java.util.List<Type> parameters)` |
    | `static Function` | `makeFunction(java.lang.String fnname, java.util.List<java.lang.String> solidityInputTypes, java.util.List<java.lang.Object> arguments, java.util.List<java.lang.String> solidityOutputTypes)` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### FunctionEncoder

      ```
      public FunctionEncoder()
      ```
  + ### Method Detail

    - #### encode

      ```
      public static java.lang.String encode(Function function)
      ```
    - #### encodeConstructor

      ```
      public static java.lang.String encodeConstructor(java.util.List<Type> parameters)
      ```
    - #### makeFunction

      ```
      public static Function makeFunction(java.lang.String fnname,
                                          java.util.List<java.lang.String> solidityInputTypes,
                                          java.util.List<java.lang.Object> arguments,
                                          java.util.List<java.lang.String> solidityOutputTypes)
                                   throws java.lang.ClassNotFoundException,
                                          java.lang.NoSuchMethodException,
                                          java.lang.InstantiationException,
                                          java.lang.IllegalAccessException,
                                          java.lang.reflect.InvocationTargetException
      ```

      Throws:
      :   `java.lang.ClassNotFoundException`
      :   `java.lang.NoSuchMethodException`
      :   `java.lang.InstantiationException`
      :   `java.lang.IllegalAccessException`
      :   `java.lang.reflect.InvocationTargetException`
    - #### encodeFunction

      ```
      protected abstract java.lang.String encodeFunction(Function function)
      ```
    - #### encodeParameters

      ```
      protected abstract java.lang.String encodeParameters(java.util.List<Type> parameters)
      ```
    - #### buildMethodSignature

      ```
      protected static java.lang.String buildMethodSignature(java.lang.String methodName,
                                                             java.util.List<Type> parameters)
      ```
    - #### buildMethodId

      ```
      protected static java.lang.String buildMethodId(java.lang.String methodSignature)
      ```