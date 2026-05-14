

org.tron.trident.abi.datatypes

## Class TrcToken

* java.lang.Object
* + [org.tron.trident.abi.datatypes.NumericType](../../../../../org/tron/trident/abi/datatypes/NumericType.html "class in org.tron.trident.abi.datatypes")
  + - [org.tron.trident.abi.datatypes.IntType](../../../../../org/tron/trident/abi/datatypes/IntType.html "class in org.tron.trident.abi.datatypes")
    - * org.tron.trident.abi.datatypes.TrcToken

* All Implemented Interfaces:
  :   [Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")<java.math.BigInteger>

  ---

    

  ```
  public class TrcToken
  extends IntType
  ```

  Unsigned integer type.

* + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static Uint` | `DEFAULT` |
    | `static java.lang.String` | `TYPE_NAME` |

    - ### Fields inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `MAX_BIT_LENGTH, MAX_BYTE_LENGTH`
  + ### Constructor Summary

    Constructors

    | Modifier | Constructor and Description |
    |  | `TrcToken(java.math.BigInteger value)` |
    |  | `TrcToken(int value)` |
    | `protected` | `TrcToken(int bitSize, java.math.BigInteger value)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `protected boolean` | `valid()` |

    - ### Methods inherited from class org.tron.trident.abi.datatypes.[IntType](../../../../../org/tron/trident/abi/datatypes/IntType.html "class in org.tron.trident.abi.datatypes")

      `getBitSize`
    - ### Methods inherited from class org.tron.trident.abi.datatypes.[NumericType](../../../../../org/tron/trident/abi/datatypes/NumericType.html "class in org.tron.trident.abi.datatypes")

      `equals, getTypeAsString, getValue, hashCode`
    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`
    - ### Methods inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `bytes32PaddedLength`

* + ### Field Detail

    - #### TYPE\_NAME

      ```
      public static final java.lang.String TYPE_NAME
      ```

      See Also:
      :   [Constant Field Values](../../../../../constant-values.html#org.tron.trident.abi.datatypes.TrcToken.TYPE_NAME)
    - #### DEFAULT

      ```
      public static final Uint DEFAULT
      ```
  + ### Constructor Detail

    - #### TrcToken

      ```
      protected TrcToken(int bitSize,
                         java.math.BigInteger value)
      ```
    - #### TrcToken

      ```
      public TrcToken(int value)
      ```
    - #### TrcToken

      ```
      public TrcToken(java.math.BigInteger value)
      ```
  + ### Method Detail

    - #### valid

      ```
      protected boolean valid()
      ```

      Overrides:
      :   `valid` in class `IntType`