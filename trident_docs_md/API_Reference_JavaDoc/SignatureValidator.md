

org.tron.trident.core.transaction

## Class SignatureValidator

* java.lang.Object
* + org.tron.trident.core.transaction.SignatureValidator

* ---

    

  ```
  public class SignatureValidator
  extends java.lang.Object
  ```

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `SignatureValidator()` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static boolean` | `verify(byte[] txid, byte[] signature, byte[] owner)` Verify if a transction contains a valid signature. |
    | `static boolean` | `verify(java.lang.String txid, java.lang.String signature, java.lang.String owner)` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### SignatureValidator

      ```
      public SignatureValidator()
      ```
  + ### Method Detail

    - #### verify

      ```
      public static boolean verify(byte[] txid,
                                   byte[] signature,
                                   byte[] owner)
      ```

      Verify if a transction contains a valid signature.

      Parameters:
      :   `txid` - the transaction hash
      :   `signature` - the signature message corresponding to the transaction hash
      :   `owner` - the owner of the transaction

      Returns:
      :   true if the signature is valid
    - #### verify

      ```
      public static boolean verify(java.lang.String txid,
                                   java.lang.String signature,
                                   java.lang.String owner)
      ```