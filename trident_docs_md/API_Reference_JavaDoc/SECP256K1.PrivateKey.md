

org.tron.trident.crypto

## Class SECP256K1.PrivateKey

* java.lang.Object
* + org.tron.trident.crypto.SECP256K1.PrivateKey

* All Implemented Interfaces:
  :   java.io.Serializable, java.security.Key, java.security.PrivateKey, javax.security.auth.Destroyable

  Enclosing class:
  :   [SECP256K1](../../../../org/tron/trident/crypto/SECP256K1.html "class in org.tron.trident.crypto")

  ---

    

  ```
  public static class SECP256K1.PrivateKey
  extends java.lang.Object
  implements java.security.PrivateKey
  ```

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.crypto.SECP256K1.PrivateKey)

* + ### Field Summary

    - ### Fields inherited from interface java.security.PrivateKey

      `serialVersionUID`
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static SECP256K1.PrivateKey` | `create(java.math.BigInteger key)` |
    | `static SECP256K1.PrivateKey` | `create(Bytes32 key)` |
    | `static SECP256K1.PrivateKey` | `create(java.lang.String hexKey)` |
    | `boolean` | `equals(java.lang.Object other)` |
    | `java.lang.String` | `getAlgorithm()` |
    | `java.math.BigInteger` | `getD()` |
    | `byte[]` | `getEncoded()` |
    | `Bytes32` | `getEncodedBytes()` |
    | `java.lang.String` | `getFormat()` |
    | `int` | `hashCode()` |
    | `java.lang.String` | `toString()` |

    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, wait, wait, wait`
    - ### Methods inherited from interface javax.security.auth.Destroyable

      `destroy, isDestroyed`

* + ### Method Detail

    - #### create

      ```
      public static SECP256K1.PrivateKey create(java.math.BigInteger key)
      ```
    - #### create

      ```
      public static SECP256K1.PrivateKey create(Bytes32 key)
      ```
    - #### create

      ```
      public static SECP256K1.PrivateKey create(java.lang.String hexKey)
      ```
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
      public Bytes32 getEncodedBytes()
      ```
    - #### getD

      ```
      public java.math.BigInteger getD()
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