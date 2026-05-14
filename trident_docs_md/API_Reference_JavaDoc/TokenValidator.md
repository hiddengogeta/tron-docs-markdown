

org.tron.trident.core.utils

## Class TokenValidator

* java.lang.Object
* + org.tron.trident.core.utils.TokenValidator

* ---

    

  ```
  public class TokenValidator
  extends java.lang.Object
  ```

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `TokenValidator()` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static void` | `validateCallValue(long callValue)` |
    | `static void` | `validateTokenId(java.lang.String tokenId)` Validates the general format and value of a token ID |
    | `static void` | `validateTokenValue(long tokenValue)` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### TokenValidator

      ```
      public TokenValidator()
      ```
  + ### Method Detail

    - #### validateCallValue

      ```
      public static void validateCallValue(long callValue)
      ```
    - #### validateTokenId

      ```
      public static void validateTokenId(java.lang.String tokenId)
      ```

      Validates the general format and value of a token ID

      Parameters:
      :   `tokenId` - The token ID to validate

      Throws:
      :   `java.lang.IllegalArgumentException` - if the token ID is invalid
    - #### validateTokenValue

      ```
      public static void validateTokenValue(long tokenValue)
      ```