

org.tron.trident.abi.datatypes

## Class AbiTypes

* java.lang.Object
* + org.tron.trident.abi.datatypes.AbiTypes

* ---

    

  ```
  public final class AbiTypes
  extends java.lang.Object
  ```

  Maps Solidity types to web3j data types, allowing to use Java primitive types for numbers. The
  used primitive type is the smallest that can hold a Solidity value for a specific bit length,
  e.g. `Short` for `int8`, `int16` and `uint8`;
  `Integer` for `int24`, `int32`, `uint16` and
  `uint24`, etc.

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static java.lang.Class<? extends Type>` | `getType(java.lang.String type)` Returns the web3j data type for the given type, without using primitive types. |
    | `static java.lang.Class<? extends Type>` | `getType(java.lang.String type, boolean primitives)` Returns the web3j data type for the given type. |
    | `static java.lang.String` | `getTypeAString(java.lang.Class<? extends Type> type)` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Method Detail

    - #### getType

      ```
      public static java.lang.Class<? extends Type> getType(java.lang.String type)
      ```

      Returns the web3j data type for the given type, without using primitive types.

      Parameters:
      :   `type` - A Solidity type.

      Returns:
      :   The web3j Java class to represent this Solidity type.
    - #### getType

      ```
      public static java.lang.Class<? extends Type> getType(java.lang.String type,
                                                            boolean primitives)
      ```

      Returns the web3j data type for the given type.

      Parameters:
      :   `type` - A Solidity type.
      :   `primitives` - Use Java primitive types to wrap contract parameters.

      Returns:
      :   The web3j Java class to represent this Solidity type.
    - #### getTypeAString

      ```
      public static java.lang.String getTypeAString(java.lang.Class<? extends Type> type)
      ```