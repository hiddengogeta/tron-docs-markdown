

org.tron.trident.crypto

## Class SECP256K1.Signature

* java.lang.Object
* + org.tron.trident.crypto.SECP256K1.Signature

* Enclosing class:
  :   [SECP256K1](../../../../org/tron/trident/crypto/SECP256K1.html "class in org.tron.trident.crypto")

  ---

    

  ```
  public static class SECP256K1.Signature
  extends java.lang.Object
  ```

* + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `BYTES_REQUIRED` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static SECP256K1.Signature` | `create(java.math.BigInteger r, java.math.BigInteger s, byte recId)` Creates a new signature object given its parameters. |
    | `static SECP256K1.Signature` | `decode(Bytes bytes)` |
    | `Bytes` | `encodedBytes()` |
    | `boolean` | `equals(java.lang.Object other)` |
    | `java.math.BigInteger` | `getR()` |
    | `byte` | `getRecId()` |
    | `java.math.BigInteger` | `getS()` |
    | `int` | `hashCode()` |
    | `java.lang.String` | `toString()` |

    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

* + ### Field Detail

    - #### BYTES\_REQUIRED

      ```
      public static final int BYTES_REQUIRED
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.crypto.SECP256K1.Signature.BYTES_REQUIRED)
  + ### Method Detail

    - #### create

      ```
      public static SECP256K1.Signature create(java.math.BigInteger r,
                                               java.math.BigInteger s,
                                               byte recId)
      ```

      Creates a new signature object given its parameters.

      Parameters:
      :   `r` - the 'r' part of the signature.
      :   `s` - the 's' part of the signature.
      :   `recId` - the recovery id part of the signature.

      Returns:
      :   the created [`SECP256K1.Signature`](../../../../org/tron/trident/crypto/SECP256K1.Signature.html "class in org.tron.trident.crypto") object.

      Throws:
      :   `java.lang.NullPointerException` - if `r` or `s` are `null`.
      :   `java.lang.IllegalArgumentException` - if any argument is invalid (for instance, `v` is
          neither 27 or 28).
    - #### decode

      ```
      public static SECP256K1.Signature decode(Bytes bytes)
      ```
    - #### encodedBytes

      ```
      public Bytes encodedBytes()
      ```
    - #### equals

      ```
      public boolean equals(java.lang.Object other)
      ```

      Overrides:
      :   `equals` in class `java.lang.Object`
    - #### hashCode

      ```
      public int hashCode()
      ```

      Overrides:
      :   `hashCode` in class `java.lang.Object`
    - #### getRecId

      ```
      public byte getRecId()
      ```
    - #### getR

      ```
      public java.math.BigInteger getR()
      ```
    - #### getS

      ```
      public java.math.BigInteger getS()
      ```
    - #### toString

      ```
      public java.lang.String toString()
      ```

      Overrides:
      :   `toString` in class `java.lang.Object`