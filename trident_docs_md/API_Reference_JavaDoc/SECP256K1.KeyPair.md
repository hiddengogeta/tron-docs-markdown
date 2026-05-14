

org.tron.trident.crypto

## Class SECP256K1.KeyPair

* java.lang.Object
* + org.tron.trident.crypto.SECP256K1.KeyPair

* Enclosing class:
  :   [SECP256K1](../../../../org/tron/trident/crypto/SECP256K1.html "class in org.tron.trident.crypto")

  ---

    

  ```
  public static class SECP256K1.KeyPair
  extends java.lang.Object
  ```

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `KeyPair(SECP256K1.PrivateKey privateKey, SECP256K1.PublicKey publicKey)` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static SECP256K1.KeyPair` | `create(SECP256K1.PrivateKey privateKey)` |
    | `boolean` | `equals(java.lang.Object other)` |
    | `static SECP256K1.KeyPair` | `generate()` |
    | `SECP256K1.PrivateKey` | `getPrivateKey()` |
    | `SECP256K1.PublicKey` | `getPublicKey()` |
    | `int` | `hashCode()` |

    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### KeyPair

      ```
      public KeyPair(SECP256K1.PrivateKey privateKey,
                     SECP256K1.PublicKey publicKey)
      ```
  + ### Method Detail

    - #### create

      ```
      public static SECP256K1.KeyPair create(SECP256K1.PrivateKey privateKey)
      ```
    - #### generate

      ```
      public static SECP256K1.KeyPair generate()
      ```
    - #### hashCode

      ```
      public int hashCode()
      ```

      Overrides:
      :   `hashCode` in class `java.lang.Object`
    - #### equals

      ```
      public boolean equals(java.lang.Object other)
      ```

      Overrides:
      :   `equals` in class `java.lang.Object`
    - #### getPrivateKey

      ```
      public SECP256K1.PrivateKey getPrivateKey()
      ```
    - #### getPublicKey

      ```
      public SECP256K1.PublicKey getPublicKey()
      ```