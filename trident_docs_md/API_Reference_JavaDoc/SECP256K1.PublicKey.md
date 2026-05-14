

org.tron.trident.crypto

## Class SECP256K1.PublicKey

* java.lang.Object
* + org.tron.trident.crypto.SECP256K1.PublicKey

* All Implemented Interfaces:
  :   java.io.Serializable, java.security.Key, java.security.PublicKey

  Enclosing class:
  :   [SECP256K1](../../../../org/tron/trident/crypto/SECP256K1.html "class in org.tron.trident.crypto")

  ---

    

  ```
  public static class SECP256K1.PublicKey
  extends java.lang.Object
  implements java.security.PublicKey
  ```

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.crypto.SECP256K1.PublicKey)

* + ### Field Summary

    - ### Fields inherited from interface java.security.PublicKey

      `serialVersionUID`
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `org.bouncycastle.math.ec.ECPoint` | `asEcPoint()` Returns this public key as an `ECPoint` of Bouncy Castle, to facilitate cryptographic operations. |
    | `static SECP256K1.PublicKey` | `create(java.math.BigInteger key)` |
    | `static SECP256K1.PublicKey` | `create(Bytes encoded)` |
    | `static SECP256K1.PublicKey` | `create(SECP256K1.PrivateKey privateKey)` |
    | `boolean` | `equals(java.lang.Object other)` |
    | `java.lang.String` | `getAlgorithm()` |
    | `byte[]` | `getEncoded()` |
    | `Bytes` | `getEncodedBytes()` |
    | `java.lang.String` | `getFormat()` |
    | `int` | `hashCode()` |
    | `static java.util.Optional<SECP256K1.PublicKey>` | `recoverFromSignature(Bytes32 dataHash, SECP256K1.Signature signature)` |
    | `java.lang.String` | `toString()` |

    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

* + ### Method Detail

    - #### create

      ```
      public static SECP256K1.PublicKey create(SECP256K1.PrivateKey privateKey)
      ```
    - #### create

      ```
      public static SECP256K1.PublicKey create(java.math.BigInteger key)
      ```
    - #### create

      ```
      public static SECP256K1.PublicKey create(Bytes encoded)
      ```
    - #### recoverFromSignature

      ```
      public static java.util.Optional<SECP256K1.PublicKey> recoverFromSignature(Bytes32 dataHash,
                                                                                 SECP256K1.Signature signature)
      ```
    - #### asEcPoint

      ```
      public org.bouncycastle.math.ec.ECPoint asEcPoint()
      ```

      Returns this public key as an `ECPoint` of Bouncy Castle, to facilitate cryptographic
      operations.

      Returns:
      :   This public key represented as an Elliptic Curve point.
    - #### equals

      ```
      public boolean equals(java.lang.Object other)
      ```

      Overrides:
      :   `equals` in class `java.lang.Object`
    - #### getEncoded

      ```
      public byte[] getEncoded()
      ```

      Specified by:
      :   `getEncoded` in interface `java.security.Key`
    - #### getEncodedBytes

      ```
      public Bytes getEncodedBytes()
      ```
    - #### getAlgorithm

      ```
      public java.lang.String getAlgorithm()
      ```

      Specified by:
      :   `getAlgorithm` in interface `java.security.Key`
    - #### getFormat

      ```
      public java.lang.String getFormat()
      ```

      Specified by:
      :   `getFormat` in interface `java.security.Key`
    - #### hashCode

      ```
      public int hashCode()
      ```

      Overrides:
      :   `hashCode` in class `java.lang.Object`
    - #### toString

      ```
      public java.lang.String toString()
      ```

      Overrides:
      :   `toString` in class `java.lang.Object`