

org.tron.trident.abi.datatypes

## Class Address

* java.lang.Object
* + org.tron.trident.abi.datatypes.Address

* All Implemented Interfaces:
  :   [Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")<java.lang.String>

  ---

    

  ```
  public class Address
  extends java.lang.Object
  implements Type<java.lang.String>
  ```

  Address type, which by default is equivalent to uint160 which follows the Ethereum specification.

* + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static Address` | `DEFAULT` |
    | `static int` | `DEFAULT_LENGTH` |
    | `static java.lang.String` | `TYPE_NAME` |

    - ### Fields inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `MAX_BIT_LENGTH, MAX_BYTE_LENGTH`
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `Address(java.math.BigInteger value)` |
    | `Address(int bitSize, java.math.BigInteger value)` |
    | `Address(int bitSize, java.lang.String hexValue)` |
    | `Address(java.lang.String value)` |
    | `Address(Uint value)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `boolean` | `equals(java.lang.Object o)` |
    | `java.lang.String` | `getTypeAsString()` |
    | `java.lang.String` | `getValue()` |
    | `int` | `hashCode()` |
    | `java.lang.String` | `toString()` |
    | `Uint` | `toUint()` |

    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, wait, wait, wait`
    - ### Methods inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `bytes32PaddedLength`

* + ### Field Detail

    - #### TYPE\_NAME

      ```
      public static final java.lang.String TYPE_NAME
      ```

      See Also:
      :   [Constant Field Values](../../../../../constant-values.html#org.tron.trident.abi.datatypes.Address.TYPE_NAME)
    - #### DEFAULT\_LENGTH

      ```
      public static final int DEFAULT_LENGTH
      ```

      See Also:
      :   [Constant Field Values](../../../../../constant-values.html#org.tron.trident.abi.datatypes.Address.DEFAULT_LENGTH)
    - #### DEFAULT

      ```
      public static final Address DEFAULT
      ```
  + ### Constructor Detail

    - #### Address

      ```
      public Address(Uint value)
      ```
    - #### Address

      ```
      public Address(java.math.BigInteger value)
      ```
    - #### Address

      ```
      public Address(int bitSize,
                     java.math.BigInteger value)
      ```
    - #### Address

      ```
      public Address(java.lang.String value)
      ```
    - #### Address

      ```
      public Address(int bitSize,
                     java.lang.String hexValue)
      ```
  + ### Method Detail

    - #### toUint

      ```
      public Uint toUint()
      ```
    - #### getTypeAsString

      ```
      public java.lang.String getTypeAsString()
      ```

      Specified by:
      :   `getTypeAsString` in interface `Type<java.lang.String>`
    - #### toString

      ```
      public java.lang.String toString()
      ```

      Overrides:
      :   `toString` in class `java.lang.Object`
    - #### getValue

      ```
      public java.lang.String getValue()
      ```

      Specified by:
      :   `getValue` in interface `Type<java.lang.String>`
    - #### equals

      ```
      public boolean equals(java.lang.Object o)
      ```

      Overrides:
      :   `equals` in class `java.lang.Object`
    - #### hashCode

      ```
      public int hashCode()
      ```

      Overrides:
      :   `hashCode` in class `java.lang.Object`