

org.tron.trident.abi

## Class EventEncoder

* java.lang.Object
* + org.tron.trident.abi.EventEncoder

* ---

    

  ```
  public class EventEncoder
  extends java.lang.Object
  ```

  Ethereum filter encoding. Further limited details are available [here](https://github.com/ethereum/wiki/wiki/Ethereum-Contract-ABI#events).

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static java.lang.String` | `buildEventSignature(java.lang.String methodSignature)` |
    | `static java.lang.String` | `encode(Event event)` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Method Detail

    - #### encode

      ```
      public static java.lang.String encode(Event event)
      ```
    - #### buildEventSignature

      ```
      public static java.lang.String buildEventSignature(java.lang.String methodSignature)
      ```