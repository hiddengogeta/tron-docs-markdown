

org.tron.trident.core.key

## Class KeyPair

* java.lang.Object
* + org.tron.trident.core.key.KeyPair

* ---

    

  ```
  public class KeyPair
  extends java.lang.Object
  ```

  This is a wrapper class for the raw SECP256K1 keypair.

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `KeyPair(SECP256K1.KeyPair keyPair)` |
    | `KeyPair(java.lang.String hexPrivateKey)` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static KeyPair` | `generate()` |
    | `SECP256K1.KeyPair` | `getRawPair()` |
    | `static byte[]` | `publicKeyToAddress(SECP256K1.PublicKey pubKey)` |
    | `static java.lang.String` | `publicKeyToBase58CheckAddress(SECP256K1.PublicKey pubKey)` |
    | `static java.lang.String` | `publicKeyToHexAddress(SECP256K1.PublicKey pubKey)` |
    | `static byte[]` | `signTransaction(byte[] txid, KeyPair keyPair)` Return a signature message in byte[] |
    | `java.lang.String` | `toBase58CheckAddress()` |
    | `java.lang.String` | `toHexAddress()` |
    | `java.lang.String` | `toPrivateKey()` |
    | `java.lang.String` | `toPublicKey()` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### KeyPair

      ```
      public KeyPair(SECP256K1.KeyPair keyPair)
      ```
    - #### KeyPair

      ```
      public KeyPair(java.lang.String hexPrivateKey)
      ```
  + ### Method Detail

    - #### getRawPair

      ```
      public SECP256K1.KeyPair getRawPair()
      ```
    - #### generate

      ```
      public static KeyPair generate()
      ```
    - #### toPrivateKey

      ```
      public java.lang.String toPrivateKey()
      ```
    - #### toPublicKey

      ```
      public java.lang.String toPublicKey()
      ```
    - #### toBase58CheckAddress

      ```
      public java.lang.String toBase58CheckAddress()
      ```
    - #### toHexAddress

      ```
      public java.lang.String toHexAddress()
      ```
    - #### publicKeyToAddress

      ```
      public static byte[] publicKeyToAddress(SECP256K1.PublicKey pubKey)
      ```
    - #### publicKeyToBase58CheckAddress

      ```
      public static java.lang.String publicKeyToBase58CheckAddress(SECP256K1.PublicKey pubKey)
      ```
    - #### publicKeyToHexAddress

      ```
      public static java.lang.String publicKeyToHexAddress(SECP256K1.PublicKey pubKey)
      ```
    - #### signTransaction

      ```
      public static byte[] signTransaction(byte[] txid,
                                           KeyPair keyPair)
      ```

      Return a signature message in byte[]

      Parameters:
      :   `txid` - the transaction hash waiting for signature

      Returns:
      :   the signature message in byte[]