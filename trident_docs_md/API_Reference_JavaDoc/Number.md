

org.tron.trident.abi.datatypes.primitive

## Class Number<T extends java.lang.Number & java.lang.Comparable<T>>

* java.lang.Object
* + [org.tron.trident.abi.datatypes.primitive.PrimitiveType](../../../../../../org/tron/trident/abi/datatypes/primitive/PrimitiveType.html "class in org.tron.trident.abi.datatypes.primitive")<T>
  + - org.tron.trident.abi.datatypes.primitive.Number<T>

* All Implemented Interfaces:
  :   [Type](../../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")<T>

  Direct Known Subclasses:
  :   [Double](../../../../../../org/tron/trident/abi/datatypes/primitive/Double.html "class in org.tron.trident.abi.datatypes.primitive"), [Float](../../../../../../org/tron/trident/abi/datatypes/primitive/Float.html "class in org.tron.trident.abi.datatypes.primitive"), [Int](../../../../../../org/tron/trident/abi/datatypes/primitive/Int.html "class in org.tron.trident.abi.datatypes.primitive"), [Long](../../../../../../org/tron/trident/abi/datatypes/primitive/Long.html "class in org.tron.trident.abi.datatypes.primitive"), [Short](../../../../../../org/tron/trident/abi/datatypes/primitive/Short.html "class in org.tron.trident.abi.datatypes.primitive")

  ---

    

  ```
  public abstract class Number<T extends java.lang.Number & java.lang.Comparable<T>>
  extends PrimitiveType<T>
  ```

* + ### Field Summary

    - ### Fields inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `MAX_BIT_LENGTH, MAX_BYTE_LENGTH`
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `abstract NumericType` | `toSolidityType()` |

    - ### Methods inherited from class org.tron.trident.abi.datatypes.primitive.[PrimitiveType](../../../../../../org/tron/trident/abi/datatypes/primitive/PrimitiveType.html "class in org.tron.trident.abi.datatypes.primitive")

      `equals, getTypeAsString, getValue, hashCode`
    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`
    - ### Methods inherited from interface org.tron.trident.abi.datatypes.[Type](../../../../../../org/tron/trident/abi/datatypes/Type.html "interface in org.tron.trident.abi.datatypes")

      `bytes32PaddedLength`

* + ### Method Detail

    - #### toSolidityType

      ```
      public abstract NumericType toSolidityType()
      ```

      Specified by:
      :   `toSolidityType` in class `PrimitiveType<T extends java.lang.Number & java.lang.Comparable<T>>`