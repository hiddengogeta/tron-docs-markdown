

org.tron.trident.abi

## Class EventValues

* java.lang.Object
* + org.tron.trident.abi.EventValues

* ---

    

  ```
  public class EventValues
  extends java.lang.Object
  ```

  Persisted solidity event parameters.

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `EventValues(java.util.List<Type> indexedValues, java.util.List<Type> nonIndexedValues)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `java.util.List<Type>` | `getIndexedValues()` |
    | `java.util.List<Type>` | `getNonIndexedValues()` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### EventValues

      ```
      public EventValues(java.util.List<Type> indexedValues,
                         java.util.List<Type> nonIndexedValues)
      ```
  + ### Method Detail

    - #### getIndexedValues

      ```
      public java.util.List<Type> getIndexedValues()
      ```
    - #### getNonIndexedValues

      ```
      public java.util.List<Type> getNonIndexedValues()
      ```