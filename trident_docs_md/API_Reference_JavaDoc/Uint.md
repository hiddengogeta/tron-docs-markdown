

org.tron.trident.abi.datatypes

## Class Uint

* java.lang.Object
* + [org.tron.trident.abi.datatypes.NumericType](../../../../../org/tron/trident/abi/datatypes/NumericType.html "class in org.tron.trident.abi.datatypes")
  + - [org.tron.trident.abi.datatypes.IntType](../../../../../org/tron/trident/abi/datatypes/IntType.html "class in org.tron.trident.abi.datatypes")
    - * org.tron.trident.abi.datatypes.Uint

* All Implemented Interfaces:
  :   [Type](../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")<java.math.BigInteger>

  Direct Known Subclasses:
  :   [Uint104](../../../../../org/tron/trident/abi/datatypes/generated/Uint104.html "class in org.tron.trident.abi.datatypes.generated"), [Uint112](../../../../../org/tron/trident/abi/datatypes/generated/Uint112.html "class in org.tron.trident.abi.datatypes.generated"), [Uint120](../../../../../org/tron/trident/abi/datatypes/generated/Uint120.html "class in org.tron.trident.abi.datatypes.generated"), [Uint128](../../../../../org/tron/trident/abi/datatypes/generated/Uint128.html "class in org.tron.trident.abi.datatypes.generated"), [Uint136](../../../../../org/tron/trident/abi/datatypes/generated/Uint136.html "class in org.tron.trident.abi.datatypes.generated"), [Uint144](../../../../../org/tron/trident/abi/datatypes/generated/Uint144.html "class in org.tron.trident.abi.datatypes.generated"), [Uint152](../../../../../org/tron/trident/abi/datatypes/generated/Uint152.html "class in org.tron.trident.abi.datatypes.generated"), [Uint16](../../../../../org/tron/trident/abi/datatypes/generated/Uint16.html "class in org.tron.trident.abi.datatypes.generated"), [Uint160](../../../../../org/tron/trident/abi/datatypes/generated/Uint160.html "class in org.tron.trident.abi.datatypes.generated"), [Uint168](../../../../../org/tron/trident/abi/datatypes/generated/Uint168.html "class in org.tron.trident.abi.datatypes.generated"), [Uint176](../../../../../org/tron/trident/abi/datatypes/generated/Uint176.html "class in org.tron.trident.abi.datatypes.generated"), [Uint184](../../../../../org/tron/trident/abi/datatypes/generated/Uint184.html "class in org.tron.trident.abi.datatypes.generated"), [Uint192](../../../../../org/tron/trident/abi/datatypes/generated/Uint192.html "class in org.tron.trident.abi.datatypes.generated"), [Uint200](../../../../../org/tron/trident/abi/datatypes/generated/Uint200.html "class in org.tron.trident.abi.datatypes.generated"), [Uint208](../../../../../org/tron/trident/abi/datatypes/generated/Uint208.html "class in org.tron.trident.abi.datatypes.generated"), [Uint216](../../../../../org/tron/trident/abi/datatypes/generated/Uint216.html "class in org.tron.trident.abi.datatypes.generated"), [Uint224](../../../../../org/tron/trident/abi/datatypes/generated/Uint224.html "class in org.tron.trident.abi.datatypes.generated"), [Uint232](../../../../../org/tron/trident/abi/datatypes/generated/Uint232.html "class in org.tron.trident.abi.datatypes.generated"), [Uint24](../../../../../org/tron/trident/abi/datatypes/generated/Uint24.html "class in org.tron.trident.abi.datatypes.generated"), [Uint240](../../../../../org/tron/trident/abi/datatypes/generated/Uint240.html "class in org.tron.trident.abi.datatypes.generated"), [Uint248](../../../../../org/tron/trident/abi/datatypes/generated/Uint248.html "class in org.tron.trident.abi.datatypes.generated"), [Uint256](../../../../../org/tron/trident/abi/datatypes/generated/Uint256.html "class in org.tron.trident.abi.datatypes.generated"), [Uint32](../../../../../org/tron/trident/abi/datatypes/generated/Uint32.html "class in org.tron.trident.abi.datatypes.generated"), [Uint40](../../../../../org/tron/trident/abi/datatypes/generated/Uint40.html "class in org.tron.trident.abi.datatypes.generated"), [Uint48](../../../../../org/tron/trident/abi/datatypes/generated/Uint48.html "class in org.tron.trident.abi.datatypes.generated"), [Uint56](../../../../../org/tron/trident/abi/datatypes/generated/Uint56.html "class in org.tron.trident.abi.datatypes.generated"), [Uint64](../../../../../org/tron/trident/abi/datatypes/generated/Uint64.html "class in org.tron.trident.abi.datatypes.generated"), [Uint72](../../../../../org/tron/trident/abi/datatypes/generated/Uint72.html "class in org.tron.trident.abi.datatypes.generated"), [Uint8](../../../../../org/tron/trident/abi/datatypes/generated/Uint8.html "class in org.tron.trident.abi.datatypes.generated"), [Uint80](../../../../../org/tron/trident/abi/datatypes/generated/Uint80.html "class in org.tron.trident.abi.datatypes.generated"), [Uint88](../../../../../org/tron/trident/abi/datatypes/generated/Uint88.html "class in org.tron.trident.abi.datatypes.generated"), [Uint96](../../../../../org/tron/trident/abi/datatypes/generated/Uint96.html "class in org.tron.trident.abi.datatypes.generated")

  ---

    

  ```
  public class Uint
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
    |  | `Uint(java.math.BigInteger value)` |
    | `protected` | `Uint(int bitSize, java.math.BigInteger value)` |
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
      :   [Constant Field Values](../../../../../constant-values.html#org.tron.trident.abi.datatypes.Uint.TYPE_NAME)
    - #### DEFAULT

      ```
      public static final Uint DEFAULT
      ```
  + ### Constructor Detail

    - #### Uint

      ```
      protected Uint(int bitSize,
                     java.math.BigInteger value)
      ```
    - #### Uint

      ```
      public Uint(java.math.BigInteger value)
      ```
  + ### Method Detail

    - #### valid

      ```
      protected boolean valid()
      ```

      Overrides:
      :   `valid` in class `IntType`