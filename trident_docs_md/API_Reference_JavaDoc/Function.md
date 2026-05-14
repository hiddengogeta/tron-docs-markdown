

org.tron.trident.abi.datatypes

## Class Function

* java.lang.Object
* + org.tron.trident.abi.datatypes.Function

* ---

    

  ```
  public class Function
  extends java.lang.Object
  ```

  Function type.

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `Function(java.lang.String name, java.util.List<Type> inputParameters, java.util.List<TypeReference<?>> outputParameters)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `java.util.List<Type>` | `getInputParameters()` |
    | `java.lang.String` | `getName()` |
    | `java.util.List<TypeReference<Type>>` | `getOutputParameters()` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### Function

      ```
      public Function(java.lang.String name,
                      java.util.List<Type> inputParameters,
                      java.util.List<TypeReference<?>> outputParameters)
      ```
  + ### Method Detail

    - #### getName

      ```
      public java.lang.String getName()
      ```
    - #### getInputParameters

      ```
      public java.util.List<Type> getInputParameters()
      ```
    - #### getOutputParameters

      ```
      public java.util.List<TypeReference<Type>> getOutputParameters()
      ```