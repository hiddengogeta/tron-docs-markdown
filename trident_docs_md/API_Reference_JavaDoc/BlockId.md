

org.tron.trident.core.transaction

## Class BlockId

* java.lang.Object
* + [org.tron.trident.core.utils.Sha256Hash](../../../../../org/tron/trident/core/utils/Sha256Hash.html "class in org.tron.trident.core.utils")
  + - org.tron.trident.core.transaction.BlockId

* All Implemented Interfaces:
  :   java.io.Serializable, java.lang.Comparable<[Sha256Hash](../../../../../org/tron/trident/core/utils/Sha256Hash.html "class in org.tron.trident.core.utils")>

  ---

    

  ```
  public class BlockId
  extends Sha256Hash
  ```

  See Also:
  :   [Serialized Form](../../../../../serialized-form.html#org.tron.trident.core.transaction.BlockId)

* + ### Field Summary

    - ### Fields inherited from class org.tron.trident.core.utils.[Sha256Hash](../../../../../org/tron/trident/core/utils/Sha256Hash.html "class in org.tron.trident.core.utils")

      `LENGTH, ZERO_HASH`
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `BlockId()` |
    | `BlockId(byte[] hash, long num)` |
    | `BlockId(com.google.protobuf.ByteString hash, long num)` |
    | `BlockId(Sha256Hash blockId)` |
    | `BlockId(Sha256Hash hash, long num)` Use [`Sha256Hash.wrap(byte[])`](../../../../../org/tron/trident/core/utils/Sha256Hash.html#wrap-byte:A-) instead. |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `int` | `compareTo(Sha256Hash other)` |
    | `boolean` | `equals(java.lang.Object o)` |
    | `long` | `getNum()` |
    | `java.lang.String` | `getString()` |
    | `int` | `hashCode()` Returns the last four bytes of the wrapped hash. |
    | `java.lang.String` | `toString()` |

    - ### Methods inherited from class org.tron.trident.core.utils.[Sha256Hash](../../../../../org/tron/trident/core/utils/Sha256Hash.html "class in org.tron.trident.core.utils")

      `create, createDouble, getBytes, getByteString, hash, hash, hashTwice, hashTwice, hashTwice, newDigest, newSM3Digest, of, of, toBigInteger, twiceOf, wrap, wrap`
    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

    - #### BlockId

      ```
      public BlockId()
      ```
    - #### BlockId

      ```
      public BlockId(Sha256Hash blockId)
      ```
    - #### BlockId

      ```
      public BlockId(Sha256Hash hash,
                     long num)
      ```

      Use [`Sha256Hash.wrap(byte[])`](../../../../../org/tron/trident/core/utils/Sha256Hash.html#wrap-byte:A-) instead.
    - #### BlockId

      ```
      public BlockId(byte[] hash,
                     long num)
      ```
    - #### BlockId

      ```
      public BlockId(com.google.protobuf.ByteString hash,
                     long num)
      ```
  + ### Method Detail

    - #### equals

      ```
      public boolean equals(java.lang.Object o)
      ```

      Overrides:
      :   `equals` in class `Sha256Hash`
    - #### getString

      ```
      public java.lang.String getString()
      ```
    - #### toString

      ```
      public java.lang.String toString()
      ```

      Overrides:
      :   `toString` in class `Sha256Hash`
    - #### hashCode

      ```
      public int hashCode()
      ```

      Description copied from class: `Sha256Hash`

      Returns the last four bytes of the wrapped hash. This should be unique enough to be a suitable
      hash code even for blocks, where the goal is to try and get the first bytes to be zeros (i.e.
      the value as a big integer lower than the target value).

      Overrides:
      :   `hashCode` in class `Sha256Hash`
    - #### compareTo

      ```
      public int compareTo(Sha256Hash other)
      ```

      Specified by:
      :   `compareTo` in interface `java.lang.Comparable<Sha256Hash>`

      Overrides:
      :   `compareTo` in class `Sha256Hash`
    - #### getNum

      ```
      public long getNum()
      ```