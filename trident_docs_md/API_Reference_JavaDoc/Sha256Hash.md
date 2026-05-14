

org.tron.trident.core.utils

## Class Sha256Hash

* java.lang.Object
* + org.tron.trident.core.utils.Sha256Hash

* All Implemented Interfaces:
  :   java.io.Serializable, java.lang.Comparable<[Sha256Hash](../../../../../org/tron/trident/core/utils/Sha256Hash.html "class in org.tron.trident.core.utils")>

  Direct Known Subclasses:
  :   [BlockId](../../../../../org/tron/trident/core/transaction/BlockId.html "class in org.tron.trident.core.transaction")

  ---

    

  ```
  public class Sha256Hash
  extends java.lang.Object
  implements java.io.Serializable, java.lang.Comparable<Sha256Hash>
  ```

  A Sha256Hash just wraps a byte[] so that equals and hashcode work correctly, allowing it to be
  used as keys in a map. It also checks that the length is correct and provides a bit more type
  safety.

  See Also:
  :   [Serialized Form](../../../../../serialized-form.html#org.tron.trident.core.utils.Sha256Hash)

* + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `LENGTH` |
    | `static Sha256Hash` | `ZERO_HASH` |
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `Sha256Hash(byte[] rawHashBytes)` Deprecated. |
    | `Sha256Hash(long num, byte[] hash)` |
    | `Sha256Hash(long num, Sha256Hash hash)` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `int` | `compareTo(Sha256Hash other)` |
    | `static Sha256Hash` | `create(boolean isSha256, byte[] contents)` Deprecated. |
    | `static Sha256Hash` | `createDouble(boolean isSha256, byte[] contents)` Deprecated. |
    | `boolean` | `equals(java.lang.Object o)` |
    | `byte[]` | `getBytes()` Returns the internal byte array, without defensively copying. |
    | `com.google.protobuf.ByteString` | `getByteString()` For pb return ByteString. |
    | `static byte[]` | `hash(boolean isSha256, byte[] input)` Calculates the SHA-256 hash of the given bytes. |
    | `static byte[]` | `hash(boolean isSha256, byte[] input, int offset, int length)` Calculates the SHA-256 hash of the given byte range. |
    | `int` | `hashCode()` Returns the last four bytes of the wrapped hash. |
    | `static byte[]` | `hashTwice(boolean isSha256, byte[] input)` Calculates the SHA-256 hash of the given bytes, and then hashes the resulting hash again. |
    | `static byte[]` | `hashTwice(boolean isSha256, byte[] input, int offset, int length)` Calculates the SHA-256 hash of the given byte range, and then hashes the resulting hash again. |
    | `static byte[]` | `hashTwice(boolean isSha256, byte[] input1, int offset1, int length1, byte[] input2, int offset2, int length2)` Calculates the hash of hash on the given byte ranges. |
    | `static java.security.MessageDigest` | `newDigest()` Returns a new SHA-256 MessageDigest instance. |
    | `static org.bouncycastle.crypto.digests.SM3Digest` | `newSM3Digest()` Returns a new SM3 MessageDigest instance. |
    | `static Sha256Hash` | `of(boolean isSha256, byte[] contents)` Creates a new instance containing the calculated (one-time) hash of the given bytes. |
    | `static Sha256Hash` | `of(boolean isSha256, java.io.File file)` Creates a new instance containing the calculated (one-time) hash of the given file's contents. |
    | `java.math.BigInteger` | `toBigInteger()` Returns the bytes interpreted as a positive integer. |
    | `java.lang.String` | `toString()` |
    | `static Sha256Hash` | `twiceOf(boolean isSha256, byte[] contents)` Creates a new instance containing the hash of the calculated hash of the given bytes. |
    | `static Sha256Hash` | `wrap(byte[] rawHashBytes)` Creates a new instance that wraps the given hash value. |
    | `static Sha256Hash` | `wrap(com.google.protobuf.ByteString rawHashByteString)` |

    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

* + ### Field Detail

    - #### LENGTH

      ```
      public static final int LENGTH
      ```

      See Also:
      :   [Constant Field Values](../../../../../constant-values.html#org.tron.trident.core.utils.Sha256Hash.LENGTH)
    - #### ZERO\_HASH

      ```
      public static final Sha256Hash ZERO_HASH
      ```
  + ### Constructor Detail

    - #### Sha256Hash

      ```
      public Sha256Hash(long num,
                        byte[] hash)
      ```
    - #### Sha256Hash

      ```
      public Sha256Hash(long num,
                        Sha256Hash hash)
      ```
    - #### Sha256Hash

      ```
      @Deprecated
      public Sha256Hash(byte[] rawHashBytes)
      ```

      Deprecated.

      Use [`wrap(byte[])`](../../../../../org/tron/trident/core/utils/Sha256Hash.html#wrap-byte:A-) instead.
  + ### Method Detail

    - #### wrap

      ```
      public static Sha256Hash wrap(byte[] rawHashBytes)
      ```

      Creates a new instance that wraps the given hash value.

      Parameters:
      :   `rawHashBytes` - the raw hash bytes to wrap

      Returns:
      :   a new instance

      Throws:
      :   `java.lang.IllegalArgumentException` - if the given array length is not exactly 32
    - #### wrap

      ```
      public static Sha256Hash wrap(com.google.protobuf.ByteString rawHashByteString)
      ```
    - #### create

      ```
      @Deprecated
      public static Sha256Hash create(boolean isSha256,
                                                  byte[] contents)
      ```

      Deprecated.

      Use [`of(boolean, byte[])`](../../../../../org/tron/trident/core/utils/Sha256Hash.html#of-boolean-byte:A-) instead: this old name is ambiguous.
    - #### of

      ```
      public static Sha256Hash of(boolean isSha256,
                                  byte[] contents)
      ```

      Creates a new instance containing the calculated (one-time) hash of the given bytes.

      Parameters:
      :   `contents` - the bytes on which the hash value is calculated

      Returns:
      :   a new instance containing the calculated (one-time) hash
    - #### of

      ```
      public static Sha256Hash of(boolean isSha256,
                                  java.io.File file)
                           throws java.io.IOException
      ```

      Creates a new instance containing the calculated (one-time) hash of the given file's contents.
      The file contents are read fully into memory, so this method should only be used with small
      files.

      Parameters:
      :   `file` - the file on which the hash value is calculated

      Returns:
      :   a new instance containing the calculated (one-time) hash

      Throws:
      :   `java.io.IOException` - if an error occurs while reading the file
    - #### createDouble

      ```
      @Deprecated
      public static Sha256Hash createDouble(boolean isSha256,
                                                        byte[] contents)
      ```

      Deprecated.

      Use [`twiceOf(boolean, byte[])`](../../../../../org/tron/trident/core/utils/Sha256Hash.html#twiceOf-boolean-byte:A-) instead: this old name is ambiguous.
    - #### twiceOf

      ```
      public static Sha256Hash twiceOf(boolean isSha256,
                                       byte[] contents)
      ```

      Creates a new instance containing the hash of the calculated hash of the given bytes.

      Parameters:
      :   `contents` - the bytes on which the hash value is calculated

      Returns:
      :   a new instance containing the calculated (two-time) hash
    - #### newDigest

      ```
      public static java.security.MessageDigest newDigest()
      ```

      Returns a new SHA-256 MessageDigest instance. This is a convenience method which wraps the
      checked exception that can never occur with a RuntimeException.

      Returns:
      :   a new SHA-256 MessageDigest instance
    - #### newSM3Digest

      ```
      public static org.bouncycastle.crypto.digests.SM3Digest newSM3Digest()
      ```

      Returns a new SM3 MessageDigest instance. This is a convenience method which wraps the checked
      exception that can never occur with a RuntimeException.

      Returns:
      :   a new SM3 MessageDigest instance
    - #### hash

      ```
      public static byte[] hash(boolean isSha256,
                                byte[] input)
      ```

      Calculates the SHA-256 hash of the given bytes.

      Parameters:
      :   `input` - the bytes to hash

      Returns:
      :   the hash (in big-endian order)
    - #### hash

      ```
      public static byte[] hash(boolean isSha256,
                                byte[] input,
                                int offset,
                                int length)
      ```

      Calculates the SHA-256 hash of the given byte range.

      Parameters:
      :   `input` - the array containing the bytes to hash
      :   `offset` - the offset within the array of the bytes to hash
      :   `length` - the number of bytes to hash

      Returns:
      :   the hash (in big-endian order)
    - #### hashTwice

      ```
      public static byte[] hashTwice(boolean isSha256,
                                     byte[] input)
      ```

      Calculates the SHA-256 hash of the given bytes, and then hashes the resulting hash again.

      Parameters:
      :   `input` - the bytes to hash

      Returns:
      :   the double-hash (in big-endian order)
    - #### hashTwice

      ```
      public static byte[] hashTwice(boolean isSha256,
                                     byte[] input,
                                     int offset,
                                     int length)
      ```

      Calculates the SHA-256 hash of the given byte range, and then hashes the resulting hash again.

      Parameters:
      :   `input` - the array containing the bytes to hash
      :   `offset` - the offset within the array of the bytes to hash
      :   `length` - the number of bytes to hash

      Returns:
      :   the double-hash (in big-endian order)
    - #### hashTwice

      ```
      public static byte[] hashTwice(boolean isSha256,
                                     byte[] input1,
                                     int offset1,
                                     int length1,
                                     byte[] input2,
                                     int offset2,
                                     int length2)
      ```

      Calculates the hash of hash on the given byte ranges. This is equivalent to concatenating the
      two ranges and then passing the result to [`hashTwice(boolean,byte[])`](../../../../../org/tron/trident/core/utils/Sha256Hash.html#hashTwice-boolean-byte:A-).
    - #### equals

      ```
      public boolean equals(java.lang.Object o)
      ```

      Overrides:
      :   `equals` in class `java.lang.Object`
    - #### toString

      ```
      public java.lang.String toString()
      ```

      Overrides:
      :   `toString` in class `java.lang.Object`
    - #### hashCode

      ```
      public int hashCode()
      ```

      Returns the last four bytes of the wrapped hash. This should be unique enough to be a suitable
      hash code even for blocks, where the goal is to try and get the first bytes to be zeros (i.e.
      the value as a big integer lower than the target value).

      Overrides:
      :   `hashCode` in class `java.lang.Object`
    - #### toBigInteger

      ```
      public java.math.BigInteger toBigInteger()
      ```

      Returns the bytes interpreted as a positive integer.
    - #### getBytes

      ```
      public byte[] getBytes()
      ```

      Returns the internal byte array, without defensively copying. Therefore do NOT modify the
      returned array.
    - #### getByteString

      ```
      public com.google.protobuf.ByteString getByteString()
      ```

      For pb return ByteString.
    - #### compareTo

      ```
      public int compareTo(Sha256Hash other)
      ```

      Specified by:
      :   `compareTo` in interface `java.lang.Comparable<Sha256Hash>`