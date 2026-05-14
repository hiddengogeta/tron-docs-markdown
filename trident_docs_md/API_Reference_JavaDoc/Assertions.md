

org.tron.trident.utils

## Class Assertions

* java.lang.Object
* + org.tron.trident.utils.Assertions

* ---

    

  ```
  public class Assertions
  extends java.lang.Object
  ```

  Assertion utility functions.

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `Assertions()` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static void` | `verifyPrecondition(boolean assertionResult, java.lang.String errorMessage)` Verify that the provided precondition holds true. |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### Assertions

      ```
      public Assertions()
      ```
  + ### Method Detail

    - #### verifyPrecondition

      ```
      public static void verifyPrecondition(boolean assertionResult,
                                            java.lang.String errorMessage)
      ```

      Verify that the provided precondition holds true.

      Parameters:
      :   `assertionResult` - assertion value
      :   `errorMessage` - error message if precondition failure