

org.tron.trident.crypto

## Class Hash

* java.lang.Object
* + org.tron.trident.crypto.Hash

* ---

    

  ```
  public class Hash
  extends java.lang.Object
  ```

  Cryptographic hash functions.

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static byte[]` | `blake2b256(byte[] input)` Blake2-256 hash function. |
    | `static byte[]` | `hash(byte[] input, java.lang.String algorithm)` Generates a digest for the given `input`. |
    | `static byte[]` | `hmacSha512(byte[] key, byte[] input)` |
    | `static byte[]` | `sha256(byte[] input)` Generates SHA-256 digest for the given `input`. |
    | `static byte[]` | `sha256hash160(byte[] input)` |
    | `static byte[]` | `sha3(byte[] input)` Keccak-256 hash function. |
    | `static byte[]` | `sha3(byte[] input, int offset, int length)` Keccak-256 hash function. |
    | `static java.lang.String` | `sha3(java.lang.String hexInput)` Keccak-256 hash function. |
    | `static java.lang.String` | `sha3String(java.lang.String utf8String)` Keccak-256 hash function that operates on a UTF-8 encoded String. |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Method Detail

    - #### hash

      ```
      public static byte[] hash(byte[] input,
                                java.lang.String algorithm)
      ```

      Generates a digest for the given `input`.

      Parameters:
      :   `input` - The input to digest
      :   `algorithm` - The hash algorithm to use

      Returns:
      :   The hash value for the given input

      Throws:
      :   `java.lang.RuntimeException` - If we couldn't find any provider for the given algorithm
    - #### sha3

      ```
      public static java.lang.String sha3(java.lang.String hexInput)
      ```

      Keccak-256 hash function.

      Parameters:
      :   `hexInput` - hex encoded input data with optional 0x prefix

      Returns:
      :   hash value as hex encoded string
    - #### sha3

      ```
      public static byte[] sha3(byte[] input,
                                int offset,
                                int length)
      ```

      Keccak-256 hash function.

      Parameters:
      :   `input` - binary encoded input data
      :   `offset` - of start of data
      :   `length` - of data

      Returns:
      :   hash value
    - #### sha3

      ```
      public static byte[] sha3(byte[] input)
      ```

      Keccak-256 hash function.

      Parameters:
      :   `input` - binary encoded input data

      Returns:
      :   hash value
    - #### sha3String

      ```
      public static java.lang.String sha3String(java.lang.String utf8String)
      ```

      Keccak-256 hash function that operates on a UTF-8 encoded String.

      Parameters:
      :   `utf8String` - UTF-8 encoded string

      Returns:
      :   hash value as hex encoded string
    - #### sha256

      ```
      public static byte[] sha256(byte[] input)
      ```

      Generates SHA-256 digest for the given `input`.

      Parameters:
      :   `input` - The input to digest

      Returns:
      :   The hash value for the given input

      Throws:
      :   `java.lang.RuntimeException` - If we couldn't find any SHA-256 provider
    - #### hmacSha512

      ```
      public static byte[] hmacSha512(byte[] key,
                                      byte[] input)
      ```
    - #### sha256hash160

      ```
      public static byte[] sha256hash160(byte[] input)
      ```
    - #### blake2b256

      ```
      public static byte[] blake2b256(byte[] input)
      ```

      Blake2-256 hash function.

      Parameters:
      :   `input` - binary encoded input data

      Returns:
      :   hash value