

org.tron.trident.core

## Enum NodeType

* java.lang.Object
* + java.lang.Enum<[NodeType](../../../../org/tron/trident/core/NodeType.html "enum in org.tron.trident.core")>
  + - org.tron.trident.core.NodeType

* All Implemented Interfaces:
  :   java.io.Serializable, java.lang.Comparable<[NodeType](../../../../org/tron/trident/core/NodeType.html "enum in org.tron.trident.core")>

  ---

    

  ```
  public enum NodeType
  extends java.lang.Enum<NodeType>
  ```

* + ### Enum Constant Summary

    Enum Constants

    | Enum Constant and Description |
    | `FULL_NODE` |
    | `SOLIDITY_NODE` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static NodeType` | `valueOf(java.lang.String name)` Returns the enum constant of this type with the specified name. |
    | `static NodeType[]` | `values()` Returns an array containing the constants of this enum type, in the order they are declared. |

    - ### Methods inherited from class java.lang.Enum

      `clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
    - ### Methods inherited from class java.lang.Object

      `getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

    - #### FULL\_NODE

      ```
      public static final NodeType FULL_NODE
      ```
    - #### SOLIDITY\_NODE

      ```
      public static final NodeType SOLIDITY_NODE
      ```
  + ### Method Detail

    - #### values

      ```
      public static NodeType[] values()
      ```

      Returns an array containing the constants of this enum type, in
      the order they are declared. This method may be used to iterate
      over the constants as follows:

      ```
      for (NodeType c : NodeType.values())
          System.out.println(c);
      ```

      Returns:
      :   an array containing the constants of this enum type, in the order they are declared
    - #### valueOf

      ```
      public static NodeType valueOf(java.lang.String name)
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