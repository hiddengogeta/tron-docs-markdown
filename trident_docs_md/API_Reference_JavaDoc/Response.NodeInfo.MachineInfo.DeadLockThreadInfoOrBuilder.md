

org.tron.trident.proto

## Interface Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.NodeInfo.MachineInfo.DeadLockThreadInfo](../../../../org/tron/trident/proto/Response.NodeInfo.MachineInfo.DeadLockThreadInfo.html "class in org.tron.trident.proto"), [Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder](../../../../org/tron/trident/proto/Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response.NodeInfo.MachineInfo](../../../../org/tron/trident/proto/Response.NodeInfo.MachineInfo.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `long` | `getBlockTime()` `int64 blockTime = 5;` |
    | `java.lang.String` | `getLockName()` `string lockName = 2;` |
    | `com.google.protobuf.ByteString` | `getLockNameBytes()` `string lockName = 2;` |
    | `java.lang.String` | `getLockOwner()` `string lockOwner = 3;` |
    | `com.google.protobuf.ByteString` | `getLockOwnerBytes()` `string lockOwner = 3;` |
    | `java.lang.String` | `getName()` `string name = 1;` |
    | `com.google.protobuf.ByteString` | `getNameBytes()` `string name = 1;` |
    | `java.lang.String` | `getStackTrace()` `string stackTrace = 7;` |
    | `com.google.protobuf.ByteString` | `getStackTraceBytes()` `string stackTrace = 7;` |
    | `java.lang.String` | `getState()` `string state = 4;` |
    | `com.google.protobuf.ByteString` | `getStateBytes()` `string state = 4;` |
    | `long` | `getWaitTime()` `int64 waitTime = 6;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getName

      ```
      java.lang.String getName()
      ```

      `string name = 1;`

      Returns:
      :   The name.
    - #### getNameBytes

      ```
      com.google.protobuf.ByteString getNameBytes()
      ```

      `string name = 1;`

      Returns:
      :   The bytes for name.
    - #### getLockName

      ```
      java.lang.String getLockName()
      ```

      `string lockName = 2;`

      Returns:
      :   The lockName.
    - #### getLockNameBytes

      ```
      com.google.protobuf.ByteString getLockNameBytes()
      ```

      `string lockName = 2;`

      Returns:
      :   The bytes for lockName.
    - #### getLockOwner

      ```
      java.lang.String getLockOwner()
      ```

      `string lockOwner = 3;`

      Returns:
      :   The lockOwner.
    - #### getLockOwnerBytes

      ```
      com.google.protobuf.ByteString getLockOwnerBytes()
      ```

      `string lockOwner = 3;`

      Returns:
      :   The bytes for lockOwner.
    - #### getState

      ```
      java.lang.String getState()
      ```

      `string state = 4;`

      Returns:
      :   The state.
    - #### getStateBytes

      ```
      com.google.protobuf.ByteString getStateBytes()
      ```

      `string state = 4;`

      Returns:
      :   The bytes for state.
    - #### getBlockTime

      ```
      long getBlockTime()
      ```

      `int64 blockTime = 5;`

      Returns:
      :   The blockTime.
    - #### getWaitTime

      ```
      long getWaitTime()
      ```

      `int64 waitTime = 6;`

      Returns:
      :   The waitTime.
    - #### getStackTrace

      ```
      java.lang.String getStackTrace()
      ```

      `string stackTrace = 7;`

      Returns:
      :   The stackTrace.
    - #### getStackTraceBytes

      ```
      com.google.protobuf.ByteString getStackTraceBytes()
      ```

      `string stackTrace = 7;`

      Returns:
      :   The bytes for stackTrace.