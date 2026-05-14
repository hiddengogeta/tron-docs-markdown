

org.tron.trident.utils

## Enum Convert.Unit

* java.lang.Object
* + java.lang.Enum<[Convert.Unit](../../../../org/tron/trident/utils/Convert.Unit.html "enum in org.tron.trident.utils")>
  + - org.tron.trident.utils.Convert.Unit

* All Implemented Interfaces:
  :   java.io.Serializable, java.lang.Comparable<[Convert.Unit](../../../../org/tron/trident/utils/Convert.Unit.html "enum in org.tron.trident.utils")>

  Enclosing class:
  :   [Convert](../../../../org/tron/trident/utils/Convert.html "class in org.tron.trident.utils")

  ---

    

  ```
  public static enum Convert.Unit
  extends java.lang.Enum<Convert.Unit>
  ```

* + ### Enum Constant Summary

    Enum Constants

    | Enum Constant and Description |
    | `SUN` |
    | `TRX` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static Convert.Unit` | `fromString(java.lang.String name)` |
    | `java.math.BigDecimal` | `getSunFactor()` |
    | `java.lang.String` | `toString()` |
    | `static Convert.Unit` | `valueOf(java.lang.String name)` Returns the enum constant of this type with the specified name. |
    | `static Convert.Unit[]` | `values()` Returns an array containing the constants of this enum type, in the order they are declared. |

    - ### Methods inherited from class java.lang.Enum

      `clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, valueOf`
    - ### Methods inherited from class java.lang.Object

      `getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

    - #### SUN

      ```
      public static final Convert.Unit SUN
      ```
    - #### TRX

      ```
      public static final Convert.Unit TRX
      ```
  + ### Method Detail

    - #### values

      ```
      public static Convert.Unit[] values()
      ```

      Returns an array containing the constants of this enum type, in
      the order they are declared. This method may be used to iterate
      over the constants as follows:

      ```
      for (Convert.Unit c : Convert.Unit.values())
          System.out.println(c);
      ```

      Returns:
      :   an array containing the constants of this enum type, in the order they are declared
    - #### valueOf

      ```
      public static Convert.Unit valueOf(java.lang.String name)
      ```

      Returns the enum constant of this type with the specified name.
      The string must match *exactly* an identifier used to declare an
      enum constant in this type. (Extraneous whitespace characters are
      not permitted.)

      Parameters:
      :   `name` - the name of the enum constant to be returned.

      Returns:
      :   the enum constant with the specified name

      Throws:
      :   `java.lang.IllegalArgumentException` - if this enum type has no constant with the specified name
      :   `java.lang.NullPointerException` - if the argument is null
    - #### getSunFactor

      ```
      public java.math.BigDecimal getSunFactor()
      ```
    - #### toString

      ```
      public java.lang.String toString()
      ```

      Overrides:
      :   `toString` in class `java.lang.Enum<Convert.Unit>`
    - #### fromString

      ```
      public static Convert.Unit fromString(java.lang.String name)
      ```