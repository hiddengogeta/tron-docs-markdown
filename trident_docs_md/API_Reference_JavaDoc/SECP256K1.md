

org.tron.trident.crypto

## Class SECP256K1

* java.lang.Object
* + org.tron.trident.crypto.SECP256K1

* ---

    

  ```
  public class SECP256K1
  extends java.lang.Object
  ```

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `SECP256K1.KeyPair` |
    | `static class` | `SECP256K1.PrivateKey` |
    | `static class` | `SECP256K1.PublicKey` |
    | `static class` | `SECP256K1.Signature` |
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static java.lang.String` | `ALGORITHM` |
    | `static org.bouncycastle.crypto.params.ECDomainParameters` | `CURVE` |
    | `static java.lang.String` | `CURVE_NAME` |
    | `static java.math.BigInteger` | `HALF_CURVE_ORDER` |
    | `static java.lang.String` | `PROVIDER` |
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `SECP256K1()` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static Bytes32` | `calculateECDHKeyAgreement(SECP256K1.PrivateKey privKey, SECP256K1.PublicKey theirPubKey)` Calculates an ECDH key agreement between the private and the public key. |
    | `static SECP256K1.Signature` | `normaliseSignature(java.math.BigInteger nativeR, java.math.BigInteger nativeS, SECP256K1.PublicKey publicKey, Bytes32 dataHash)` |
    | `static SECP256K1.Signature` | `sign(Bytes32 dataHash, SECP256K1.KeyPair keyPair)` |
    | `static boolean` | `verify(Bytes data, SECP256K1.Signature signature, SECP256K1.PublicKey pub)` Verifies the given ECDSA signature against the message bytes using the public key bytes. |
    | `static boolean` | `verify(Bytes data, SECP256K1.Signature signature, SECP256K1.PublicKey pub, java.util.function.UnaryOperator<Bytes> preprocessor)` Verifies the given ECDSA signature using the public key bytes against the message bytes, previously passed through a preprocessor function, which is normally a hashing function. |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Field Detail

    - #### ALGORITHM

      ```
      public static final java.lang.String ALGORITHM
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.crypto.SECP256K1.ALGORITHM)
    - #### CURVE\_NAME

      ```
      public static final java.lang.String CURVE_NAME
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.crypto.SECP256K1.CURVE_NAME)
    - #### PROVIDER

      ```
      public static final java.lang.String PROVIDER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.crypto.SECP256K1.PROVIDER)
    - #### CURVE

      ```
      public static final org.bouncycastle.crypto.params.ECDomainParameters CURVE
      ```
    - #### HALF\_CURVE\_ORDER

      ```
      public static final java.math.BigInteger HALF_CURVE_ORDER
      ```
  + ### Constructor Detail

    - #### SECP256K1

      ```
      public SECP256K1()
      ```
  + ### Method Detail

    - #### sign

      ```
      public static SECP256K1.Signature sign(Bytes32 dataHash,
                                             SECP256K1.KeyPair keyPair)
      ```
    - #### verify

      ```
      public static boolean verify(Bytes data,
                                   SECP256K1.Signature signature,
                                   SECP256K1.PublicKey pub)
      ```

      Verifies the given ECDSA signature against the message bytes using the public key bytes.

      When using native ECDSA verification, data must be 32 bytes, and no element may be larger
      than 520 bytes.

      Parameters:
      :   `data` - Hash of the data to verify.
      :   `signature` - ASN.1 encoded signature.
      :   `pub` - The public key bytes to use.

      Returns:
      :   True if the verification is successful.
    - #### verify

      ```
      public static boolean verify(Bytes data,
                                   SECP256K1.Signature signature,
                                   SECP256K1.PublicKey pub,
                                   java.util.function.UnaryOperator<Bytes> preprocessor)
      ```

      Verifies the given ECDSA signature using the public key bytes against the message bytes,
      previously passed through a preprocessor function, which is normally a hashing function.

      Parameters:
      :   `data` - The data to verify.
      :   `signature` - ASN.1 encoded signature.
      :   `pub` - The public key bytes to use.
      :   `preprocessor` - The function to apply to the data before verifying the signature, normally
          a hashing function.

      Returns:
      :   True if the verification is successful.
    - #### normaliseSignature

      ```
      public static SECP256K1.Signature normaliseSignature(java.math.BigInteger nativeR,
                                                           java.math.BigInteger nativeS,
                                                           SECP256K1.PublicKey publicKey,
                                                           Bytes32 dataHash)
      ```
    - #### calculateECDHKeyAgreement

      ```
      public static Bytes32 calculateECDHKeyAgreement(SECP256K1.PrivateKey privKey,
                                                      SECP256K1.PublicKey theirPubKey)
      ```

      Calculates an ECDH key agreement between the private and the public key.

      Parameters:
      :   `privKey` - The private key.
      :   `theirPubKey` - The public key.

      Returns:
      :   The agreed secret.