

org.tron.trident.abi.datatypes

## Class Event

* java.lang.Object
* + org.tron.trident.abi.datatypes.Event

* ---

    

  ```
  public class Event
  extends java.lang.Object
  ```

  Event wrapper type.

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `Event(java.lang.String name, java.util.List<TypeReference<?>> parameters)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `java.util.List<TypeReference<Type>>` | `getIndexedParameters()` |
    | `java.lang.String` | `getName()` |
    | `java.util.List<TypeReference<Type>>` | `getNonIndexedParameters()` |
    | `java.util.List<TypeReference<Type>>` | `getParameters()` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### Event

      ```
      public Event(java.lang.String name,
                   java.util.List<TypeReference<?>> parameters)
      ```
  + ### Method Detail

    - #### getName

      ```
      public java.lang.String getName()
      ```
    - #### getParameters

      ```
      public java.util.List<TypeReference<Type>> getParameters()
      ```
    - #### getIndexedParameters

      ```
      public java.util.List<TypeReference<Type>> getIndexedParameters()
      ```
    - #### getNonIndexedParameters

      ```
      public java.util.List<TypeReference<Type>> getNonIndexedParameters()
      ```