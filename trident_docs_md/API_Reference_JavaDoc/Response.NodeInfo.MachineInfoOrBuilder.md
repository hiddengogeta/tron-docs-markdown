

org.tron.trident.proto

## Interface Response.NodeInfo.MachineInfoOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.NodeInfo.MachineInfo](../../../../org/tron/trident/proto/Response.NodeInfo.MachineInfo.html "class in org.tron.trident.proto"), [Response.NodeInfo.MachineInfo.Builder](../../../../org/tron/trident/proto/Response.NodeInfo.MachineInfo.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response.NodeInfo](../../../../org/tron/trident/proto/Response.NodeInfo.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.NodeInfo.MachineInfoOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `int` | `getCpuCount()` `int32 cpuCount = 3;` |
    | `double` | `getCpuRate()` `double cpuRate = 6;` |
    | `int` | `getDeadLockThreadCount()` `int32 deadLockThreadCount = 2;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo` | `getDeadLockThreadInfoList(int index)` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `int` | `getDeadLockThreadInfoListCount()` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `java.util.List<Response.NodeInfo.MachineInfo.DeadLockThreadInfo>` | `getDeadLockThreadInfoListList()` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder` | `getDeadLockThreadInfoListOrBuilder(int index)` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `java.util.List<? extends Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder>` | `getDeadLockThreadInfoListOrBuilderList()` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `long` | `getFreeMemory()` `int64 freeMemory = 5;` |
    | `java.lang.String` | `getJavaVersion()` `string javaVersion = 7;` |
    | `com.google.protobuf.ByteString` | `getJavaVersionBytes()` `string javaVersion = 7;` |
    | `long` | `getJvmFreeMemory()` `int64 jvmFreeMemory = 10;` |
    | `long` | `getJvmTotalMemoery()` `int64 jvmTotalMemoery = 9;` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo` | `getMemoryDescInfoList(int index)` `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;` |
    | `int` | `getMemoryDescInfoListCount()` `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;` |
    | `java.util.List<Response.NodeInfo.MachineInfo.MemoryDescInfo>` | `getMemoryDescInfoListList()` `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder` | `getMemoryDescInfoListOrBuilder(int index)` `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;` |
    | `java.util.List<? extends Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder>` | `getMemoryDescInfoListOrBuilderList()` `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;` |
    | `java.lang.String` | `getOsName()` `string osName = 8;` |
    | `com.google.protobuf.ByteString` | `getOsNameBytes()` `string osName = 8;` |
    | `double` | `getProcessCpuRate()` `double processCpuRate = 11;` |
    | `int` | `getThreadCount()` `int32 threadCount = 1;` |
    | `long` | `getTotalMemory()` `int64 totalMemory = 4;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getThreadCount

      ```
      int getThreadCount()
      ```

      `int32 threadCount = 1;`

      Returns:
      :   The threadCount.
    - #### getDeadLockThreadCount

      ```
      int getDeadLockThreadCount()
      ```

      `int32 deadLockThreadCount = 2;`

      Returns:
      :   The deadLockThreadCount.
    - #### getCpuCount

      ```
      int getCpuCount()
      ```

      `int32 cpuCount = 3;`

      Returns:
      :   The cpuCount.
    - #### getTotalMemory

      ```
      long getTotalMemory()
      ```

      `int64 totalMemory = 4;`

      Returns:
      :   The totalMemory.
    - #### getFreeMemory

      ```
      long getFreeMemory()
      ```

      `int64 freeMemory = 5;`

      Returns:
      :   The freeMemory.
    - #### getCpuRate

      ```
      double getCpuRate()
      ```

      `double cpuRate = 6;`

      Returns:
      :   The cpuRate.
    - #### getJavaVersion

      ```
      java.lang.String getJavaVersion()
      ```

      `string javaVersion = 7;`

      Returns:
      :   The javaVersion.
    - #### getJavaVersionBytes

      ```
      com.google.protobuf.ByteString getJavaVersionBytes()
      ```

      `string javaVersion = 7;`

      Returns:
      :   The bytes for javaVersion.
    - #### getOsName

      ```
      java.lang.String getOsName()
      ```

      `string osName = 8;`

      Returns:
      :   The osName.
    - #### getOsNameBytes

      ```
      com.google.protobuf.ByteString getOsNameBytes()
      ```

      `string osName = 8;`

      Returns:
      :   The bytes for osName.
    - #### getJvmTotalMemoery

      ```
      long getJvmTotalMemoery()
      ```

      `int64 jvmTotalMemoery = 9;`

      Returns:
      :   The jvmTotalMemoery.
    - #### getJvmFreeMemory

      ```
      long getJvmFreeMemory()
      ```

      `int64 jvmFreeMemory = 10;`

      Returns:
      :   The jvmFreeMemory.
    - #### getProcessCpuRate

      ```
      double getProcessCpuRate()
      ```

      `double processCpuRate = 11;`

      Returns:
      :   The processCpuRate.
    - #### getMemoryDescInfoListList

      ```
      java.util.List<Response.NodeInfo.MachineInfo.MemoryDescInfo> getMemoryDescInfoListList()
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`
    - #### getMemoryDescInfoList

      ```
      Response.NodeInfo.MachineInfo.MemoryDescInfo getMemoryDescInfoList(int index)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`
    - #### getMemoryDescInfoListCount

      ```
      int getMemoryDescInfoListCount()
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`
    - #### getMemoryDescInfoListOrBuilderList

      ```
      java.util.List<? extends Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder> getMemoryDescInfoListOrBuilderList()
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`
    - #### getMemoryDescInfoListOrBuilder

      ```
      Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder getMemoryDescInfoListOrBuilder(int index)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`
    - #### getDeadLockThreadInfoListList

      ```
      java.util.List<Response.NodeInfo.MachineInfo.DeadLockThreadInfo> getDeadLockThreadInfoListList()
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`
    - #### getDeadLockThreadInfoList

      ```
      Response.NodeInfo.MachineInfo.DeadLockThreadInfo getDeadLockThreadInfoList(int index)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`
    - #### getDeadLockThreadInfoListCount

      ```
      int getDeadLockThreadInfoListCount()
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`
    - #### getDeadLockThreadInfoListOrBuilderList

      ```
      java.util.List<? extends Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder> getDeadLockThreadInfoListOrBuilderList()
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`
    - #### getDeadLockThreadInfoListOrBuilder

      ```
      Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder getDeadLockThreadInfoListOrBuilder(int index)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`