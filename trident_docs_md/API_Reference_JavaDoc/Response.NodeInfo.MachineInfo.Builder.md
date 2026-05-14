

org.tron.trident.proto

## Class Response.NodeInfo.MachineInfo.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.NodeInfo.MachineInfo.Builder](../../../../org/tron/trident/proto/Response.NodeInfo.MachineInfo.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.NodeInfo.MachineInfo.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.NodeInfo.MachineInfoOrBuilder](../../../../org/tron/trident/proto/Response.NodeInfo.MachineInfoOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.NodeInfo.MachineInfo](../../../../org/tron/trident/proto/Response.NodeInfo.MachineInfo.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.NodeInfo.MachineInfo.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.Builder>
  implements Response.NodeInfo.MachineInfoOrBuilder
  ```

  Protobuf type `protocol.NodeInfo.MachineInfo`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.NodeInfo.MachineInfo.Builder` | `addAllDeadLockThreadInfoList(java.lang.Iterable<? extends Response.NodeInfo.MachineInfo.DeadLockThreadInfo> values)` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `addAllMemoryDescInfoList(java.lang.Iterable<? extends Response.NodeInfo.MachineInfo.MemoryDescInfo> values)` `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `addDeadLockThreadInfoList(int index, Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder builderForValue)` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `addDeadLockThreadInfoList(int index, Response.NodeInfo.MachineInfo.DeadLockThreadInfo value)` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `addDeadLockThreadInfoList(Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder builderForValue)` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `addDeadLockThreadInfoList(Response.NodeInfo.MachineInfo.DeadLockThreadInfo value)` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `addDeadLockThreadInfoListBuilder()` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `addDeadLockThreadInfoListBuilder(int index)` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `addMemoryDescInfoList(int index, Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder builderForValue)` `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `addMemoryDescInfoList(int index, Response.NodeInfo.MachineInfo.MemoryDescInfo value)` `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `addMemoryDescInfoList(Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder builderForValue)` `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `addMemoryDescInfoList(Response.NodeInfo.MachineInfo.MemoryDescInfo value)` `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `addMemoryDescInfoListBuilder()` `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `addMemoryDescInfoListBuilder(int index)` `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.NodeInfo.MachineInfo` | `build()` |
    | `Response.NodeInfo.MachineInfo` | `buildPartial()` |
    | `Response.NodeInfo.MachineInfo.Builder` | `clear()` |
    | `Response.NodeInfo.MachineInfo.Builder` | `clearCpuCount()` `int32 cpuCount = 3;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `clearCpuRate()` `double cpuRate = 6;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `clearDeadLockThreadCount()` `int32 deadLockThreadCount = 2;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `clearDeadLockThreadInfoList()` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.NodeInfo.MachineInfo.Builder` | `clearFreeMemory()` `int64 freeMemory = 5;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `clearJavaVersion()` `string javaVersion = 7;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `clearJvmFreeMemory()` `int64 jvmFreeMemory = 10;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `clearJvmTotalMemoery()` `int64 jvmTotalMemoery = 9;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `clearMemoryDescInfoList()` `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.NodeInfo.MachineInfo.Builder` | `clearOsName()` `string osName = 8;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `clearProcessCpuRate()` `double processCpuRate = 11;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `clearThreadCount()` `int32 threadCount = 1;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `clearTotalMemory()` `int64 totalMemory = 4;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `clone()` |
    | `int` | `getCpuCount()` `int32 cpuCount = 3;` |
    | `double` | `getCpuRate()` `double cpuRate = 6;` |
    | `int` | `getDeadLockThreadCount()` `int32 deadLockThreadCount = 2;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo` | `getDeadLockThreadInfoList(int index)` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `getDeadLockThreadInfoListBuilder(int index)` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `java.util.List<Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder>` | `getDeadLockThreadInfoListBuilderList()` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `int` | `getDeadLockThreadInfoListCount()` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `java.util.List<Response.NodeInfo.MachineInfo.DeadLockThreadInfo>` | `getDeadLockThreadInfoListList()` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder` | `getDeadLockThreadInfoListOrBuilder(int index)` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `java.util.List<? extends Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder>` | `getDeadLockThreadInfoListOrBuilderList()` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `Response.NodeInfo.MachineInfo` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getFreeMemory()` `int64 freeMemory = 5;` |
    | `java.lang.String` | `getJavaVersion()` `string javaVersion = 7;` |
    | `com.google.protobuf.ByteString` | `getJavaVersionBytes()` `string javaVersion = 7;` |
    | `long` | `getJvmFreeMemory()` `int64 jvmFreeMemory = 10;` |
    | `long` | `getJvmTotalMemoery()` `int64 jvmTotalMemoery = 9;` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo` | `getMemoryDescInfoList(int index)` `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `getMemoryDescInfoListBuilder(int index)` `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;` |
    | `java.util.List<Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder>` | `getMemoryDescInfoListBuilderList()` `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;` |
    | `int` | `getMemoryDescInfoListCount()` `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;` |
    | `java.util.List<Response.NodeInfo.MachineInfo.MemoryDescInfo>` | `getMemoryDescInfoListList()` `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder` | `getMemoryDescInfoListOrBuilder(int index)` `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;` |
    | `java.util.List<? extends Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder>` | `getMemoryDescInfoListOrBuilderList()` `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;` |
    | `java.lang.String` | `getOsName()` `string osName = 8;` |
    | `com.google.protobuf.ByteString` | `getOsNameBytes()` `string osName = 8;` |
    | `double` | `getProcessCpuRate()` `double processCpuRate = 11;` |
    | `int` | `getThreadCount()` `int32 threadCount = 1;` |
    | `long` | `getTotalMemory()` `int64 totalMemory = 4;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.NodeInfo.MachineInfo.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.NodeInfo.MachineInfo.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.NodeInfo.MachineInfo.Builder` | `mergeFrom(Response.NodeInfo.MachineInfo other)` |
    | `Response.NodeInfo.MachineInfo.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.NodeInfo.MachineInfo.Builder` | `removeDeadLockThreadInfoList(int index)` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `removeMemoryDescInfoList(int index)` `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `setCpuCount(int value)` `int32 cpuCount = 3;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `setCpuRate(double value)` `double cpuRate = 6;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `setDeadLockThreadCount(int value)` `int32 deadLockThreadCount = 2;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `setDeadLockThreadInfoList(int index, Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder builderForValue)` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `setDeadLockThreadInfoList(int index, Response.NodeInfo.MachineInfo.DeadLockThreadInfo value)` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.NodeInfo.MachineInfo.Builder` | `setFreeMemory(long value)` `int64 freeMemory = 5;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `setJavaVersion(java.lang.String value)` `string javaVersion = 7;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `setJavaVersionBytes(com.google.protobuf.ByteString value)` `string javaVersion = 7;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `setJvmFreeMemory(long value)` `int64 jvmFreeMemory = 10;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `setJvmTotalMemoery(long value)` `int64 jvmTotalMemoery = 9;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `setMemoryDescInfoList(int index, Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder builderForValue)` `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `setMemoryDescInfoList(int index, Response.NodeInfo.MachineInfo.MemoryDescInfo value)` `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `setOsName(java.lang.String value)` `string osName = 8;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `setOsNameBytes(com.google.protobuf.ByteString value)` `string osName = 8;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `setProcessCpuRate(double value)` `double processCpuRate = 11;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.NodeInfo.MachineInfo.Builder` | `setThreadCount(int value)` `int32 threadCount = 1;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `setTotalMemory(long value)` `int64 totalMemory = 4;` |
    | `Response.NodeInfo.MachineInfo.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

    - ### Methods inherited from class com.google.protobuf.GeneratedMessageV3.Builder

      `getAllFields, getField, getFieldBuilder, getOneofFieldDescriptor, getParentForChildren, getRepeatedField, getRepeatedFieldBuilder, getRepeatedFieldCount, getUnknownFields, getUnknownFieldSetBuilder, hasField, hasOneof, internalGetMapField, internalGetMapFieldReflection, internalGetMutableMapField, internalGetMutableMapFieldReflection, isClean, markClean, mergeUnknownLengthDelimitedField, mergeUnknownVarintField, newBuilderForField, onBuilt, onChanged, parseUnknownField, setUnknownFieldSetBuilder, setUnknownFieldsProto3`
    - ### Methods inherited from class com.google.protobuf.AbstractMessage.Builder

      `findInitializationErrors, getInitializationErrorString, internalMergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, mergeFrom, newUninitializedMessageException, toString`
    - ### Methods inherited from class com.google.protobuf.AbstractMessageLite.Builder

      `addAll, addAll, mergeDelimitedFrom, mergeDelimitedFrom, newUninitializedMessageException`
    - ### Methods inherited from class java.lang.Object

      `equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`
    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.Message.Builder

      `mergeDelimitedFrom, mergeDelimitedFrom`

* + ### Method Detail

    - #### getDescriptor

      ```
      public static final com.google.protobuf.Descriptors.Descriptor getDescriptor()
      ```
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.Builder>`
    - #### clear

      ```
      public Response.NodeInfo.MachineInfo.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.NodeInfo.MachineInfo getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.NodeInfo.MachineInfo build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.NodeInfo.MachineInfo buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.NodeInfo.MachineInfo.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.Builder>`
    - #### setField

      ```
      public Response.NodeInfo.MachineInfo.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                            java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.Builder>`
    - #### clearField

      ```
      public Response.NodeInfo.MachineInfo.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.Builder>`
    - #### clearOneof

      ```
      public Response.NodeInfo.MachineInfo.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.Builder>`
    - #### setRepeatedField

      ```
      public Response.NodeInfo.MachineInfo.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                    int index,
                                                                    java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.Builder>`
    - #### addRepeatedField

      ```
      public Response.NodeInfo.MachineInfo.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                    java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeInfo.MachineInfo.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.NodeInfo.MachineInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeInfo.MachineInfo.Builder mergeFrom(Response.NodeInfo.MachineInfo other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeInfo.MachineInfo.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                             com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                      throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.NodeInfo.MachineInfo.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getThreadCount

      ```
      public int getThreadCount()
      ```

      `int32 threadCount = 1;`

      Specified by:
      :   `getThreadCount` in interface `Response.NodeInfo.MachineInfoOrBuilder`

      Returns:
      :   The threadCount.
    - #### setThreadCount

      ```
      public Response.NodeInfo.MachineInfo.Builder setThreadCount(int value)
      ```

      `int32 threadCount = 1;`

      Parameters:
      :   `value` - The threadCount to set.

      Returns:
      :   This builder for chaining.
    - #### clearThreadCount

      ```
      public Response.NodeInfo.MachineInfo.Builder clearThreadCount()
      ```

      `int32 threadCount = 1;`

      Returns:
      :   This builder for chaining.
    - #### getDeadLockThreadCount

      ```
      public int getDeadLockThreadCount()
      ```

      `int32 deadLockThreadCount = 2;`

      Specified by:
      :   `getDeadLockThreadCount` in interface `Response.NodeInfo.MachineInfoOrBuilder`

      Returns:
      :   The deadLockThreadCount.
    - #### setDeadLockThreadCount

      ```
      public Response.NodeInfo.MachineInfo.Builder setDeadLockThreadCount(int value)
      ```

      `int32 deadLockThreadCount = 2;`

      Parameters:
      :   `value` - The deadLockThreadCount to set.

      Returns:
      :   This builder for chaining.
    - #### clearDeadLockThreadCount

      ```
      public Response.NodeInfo.MachineInfo.Builder clearDeadLockThreadCount()
      ```

      `int32 deadLockThreadCount = 2;`

      Returns:
      :   This builder for chaining.
    - #### getCpuCount

      ```
      public int getCpuCount()
      ```

      `int32 cpuCount = 3;`

      Specified by:
      :   `getCpuCount` in interface `Response.NodeInfo.MachineInfoOrBuilder`

      Returns:
      :   The cpuCount.
    - #### setCpuCount

      ```
      public Response.NodeInfo.MachineInfo.Builder setCpuCount(int value)
      ```

      `int32 cpuCount = 3;`

      Parameters:
      :   `value` - The cpuCount to set.

      Returns:
      :   This builder for chaining.
    - #### clearCpuCount

      ```
      public Response.NodeInfo.MachineInfo.Builder clearCpuCount()
      ```

      `int32 cpuCount = 3;`

      Returns:
      :   This builder for chaining.
    - #### getTotalMemory

      ```
      public long getTotalMemory()
      ```

      `int64 totalMemory = 4;`

      Specified by:
      :   `getTotalMemory` in interface `Response.NodeInfo.MachineInfoOrBuilder`

      Returns:
      :   The totalMemory.
    - #### setTotalMemory

      ```
      public Response.NodeInfo.MachineInfo.Builder setTotalMemory(long value)
      ```

      `int64 totalMemory = 4;`

      Parameters:
      :   `value` - The totalMemory to set.

      Returns:
      :   This builder for chaining.
    - #### clearTotalMemory

      ```
      public Response.NodeInfo.MachineInfo.Builder clearTotalMemory()
      ```

      `int64 totalMemory = 4;`

      Returns:
      :   This builder for chaining.
    - #### getFreeMemory

      ```
      public long getFreeMemory()
      ```

      `int64 freeMemory = 5;`

      Specified by:
      :   `getFreeMemory` in interface `Response.NodeInfo.MachineInfoOrBuilder`

      Returns:
      :   The freeMemory.
    - #### setFreeMemory

      ```
      public Response.NodeInfo.MachineInfo.Builder setFreeMemory(long value)
      ```

      `int64 freeMemory = 5;`

      Parameters:
      :   `value` - The freeMemory to set.

      Returns:
      :   This builder for chaining.
    - #### clearFreeMemory

      ```
      public Response.NodeInfo.MachineInfo.Builder clearFreeMemory()
      ```

      `int64 freeMemory = 5;`

      Returns:
      :   This builder for chaining.
    - #### getCpuRate

      ```
      public double getCpuRate()
      ```

      `double cpuRate = 6;`

      Specified by:
      :   `getCpuRate` in interface `Response.NodeInfo.MachineInfoOrBuilder`

      Returns:
      :   The cpuRate.
    - #### setCpuRate

      ```
      public Response.NodeInfo.MachineInfo.Builder setCpuRate(double value)
      ```

      `double cpuRate = 6;`

      Parameters:
      :   `value` - The cpuRate to set.

      Returns:
      :   This builder for chaining.
    - #### clearCpuRate

      ```
      public Response.NodeInfo.MachineInfo.Builder clearCpuRate()
      ```

      `double cpuRate = 6;`

      Returns:
      :   This builder for chaining.
    - #### getJavaVersion

      ```
      public java.lang.String getJavaVersion()
      ```

      `string javaVersion = 7;`

      Specified by:
      :   `getJavaVersion` in interface `Response.NodeInfo.MachineInfoOrBuilder`

      Returns:
      :   The javaVersion.
    - #### getJavaVersionBytes

      ```
      public com.google.protobuf.ByteString getJavaVersionBytes()
      ```

      `string javaVersion = 7;`

      Specified by:
      :   `getJavaVersionBytes` in interface `Response.NodeInfo.MachineInfoOrBuilder`

      Returns:
      :   The bytes for javaVersion.
    - #### setJavaVersion

      ```
      public Response.NodeInfo.MachineInfo.Builder setJavaVersion(java.lang.String value)
      ```

      `string javaVersion = 7;`

      Parameters:
      :   `value` - The javaVersion to set.

      Returns:
      :   This builder for chaining.
    - #### clearJavaVersion

      ```
      public Response.NodeInfo.MachineInfo.Builder clearJavaVersion()
      ```

      `string javaVersion = 7;`

      Returns:
      :   This builder for chaining.
    - #### setJavaVersionBytes

      ```
      public Response.NodeInfo.MachineInfo.Builder setJavaVersionBytes(com.google.protobuf.ByteString value)
      ```

      `string javaVersion = 7;`

      Parameters:
      :   `value` - The bytes for javaVersion to set.

      Returns:
      :   This builder for chaining.
    - #### getOsName

      ```
      public java.lang.String getOsName()
      ```

      `string osName = 8;`

      Specified by:
      :   `getOsName` in interface `Response.NodeInfo.MachineInfoOrBuilder`

      Returns:
      :   The osName.
    - #### getOsNameBytes

      ```
      public com.google.protobuf.ByteString getOsNameBytes()
      ```

      `string osName = 8;`

      Specified by:
      :   `getOsNameBytes` in interface `Response.NodeInfo.MachineInfoOrBuilder`

      Returns:
      :   The bytes for osName.
    - #### setOsName

      ```
      public Response.NodeInfo.MachineInfo.Builder setOsName(java.lang.String value)
      ```

      `string osName = 8;`

      Parameters:
      :   `value` - The osName to set.

      Returns:
      :   This builder for chaining.
    - #### clearOsName

      ```
      public Response.NodeInfo.MachineInfo.Builder clearOsName()
      ```

      `string osName = 8;`

      Returns:
      :   This builder for chaining.
    - #### setOsNameBytes

      ```
      public Response.NodeInfo.MachineInfo.Builder setOsNameBytes(com.google.protobuf.ByteString value)
      ```

      `string osName = 8;`

      Parameters:
      :   `value` - The bytes for osName to set.

      Returns:
      :   This builder for chaining.
    - #### getJvmTotalMemoery

      ```
      public long getJvmTotalMemoery()
      ```

      `int64 jvmTotalMemoery = 9;`

      Specified by:
      :   `getJvmTotalMemoery` in interface `Response.NodeInfo.MachineInfoOrBuilder`

      Returns:
      :   The jvmTotalMemoery.
    - #### setJvmTotalMemoery

      ```
      public Response.NodeInfo.MachineInfo.Builder setJvmTotalMemoery(long value)
      ```

      `int64 jvmTotalMemoery = 9;`

      Parameters:
      :   `value` - The jvmTotalMemoery to set.

      Returns:
      :   This builder for chaining.
    - #### clearJvmTotalMemoery

      ```
      public Response.NodeInfo.MachineInfo.Builder clearJvmTotalMemoery()
      ```

      `int64 jvmTotalMemoery = 9;`

      Returns:
      :   This builder for chaining.
    - #### getJvmFreeMemory

      ```
      public long getJvmFreeMemory()
      ```

      `int64 jvmFreeMemory = 10;`

      Specified by:
      :   `getJvmFreeMemory` in interface `Response.NodeInfo.MachineInfoOrBuilder`

      Returns:
      :   The jvmFreeMemory.
    - #### setJvmFreeMemory

      ```
      public Response.NodeInfo.MachineInfo.Builder setJvmFreeMemory(long value)
      ```

      `int64 jvmFreeMemory = 10;`

      Parameters:
      :   `value` - The jvmFreeMemory to set.

      Returns:
      :   This builder for chaining.
    - #### clearJvmFreeMemory

      ```
      public Response.NodeInfo.MachineInfo.Builder clearJvmFreeMemory()
      ```

      `int64 jvmFreeMemory = 10;`

      Returns:
      :   This builder for chaining.
    - #### getProcessCpuRate

      ```
      public double getProcessCpuRate()
      ```

      `double processCpuRate = 11;`

      Specified by:
      :   `getProcessCpuRate` in interface `Response.NodeInfo.MachineInfoOrBuilder`

      Returns:
      :   The processCpuRate.
    - #### setProcessCpuRate

      ```
      public Response.NodeInfo.MachineInfo.Builder setProcessCpuRate(double value)
      ```

      `double processCpuRate = 11;`

      Parameters:
      :   `value` - The processCpuRate to set.

      Returns:
      :   This builder for chaining.
    - #### clearProcessCpuRate

      ```
      public Response.NodeInfo.MachineInfo.Builder clearProcessCpuRate()
      ```

      `double processCpuRate = 11;`

      Returns:
      :   This builder for chaining.
    - #### getMemoryDescInfoListList

      ```
      public java.util.List<Response.NodeInfo.MachineInfo.MemoryDescInfo> getMemoryDescInfoListList()
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`

      Specified by:
      :   `getMemoryDescInfoListList` in interface `Response.NodeInfo.MachineInfoOrBuilder`
    - #### getMemoryDescInfoListCount

      ```
      public int getMemoryDescInfoListCount()
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`

      Specified by:
      :   `getMemoryDescInfoListCount` in interface `Response.NodeInfo.MachineInfoOrBuilder`
    - #### getMemoryDescInfoList

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo getMemoryDescInfoList(int index)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`

      Specified by:
      :   `getMemoryDescInfoList` in interface `Response.NodeInfo.MachineInfoOrBuilder`
    - #### setMemoryDescInfoList

      ```
      public Response.NodeInfo.MachineInfo.Builder setMemoryDescInfoList(int index,
                                                                         Response.NodeInfo.MachineInfo.MemoryDescInfo value)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`
    - #### setMemoryDescInfoList

      ```
      public Response.NodeInfo.MachineInfo.Builder setMemoryDescInfoList(int index,
                                                                         Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder builderForValue)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`
    - #### addMemoryDescInfoList

      ```
      public Response.NodeInfo.MachineInfo.Builder addMemoryDescInfoList(Response.NodeInfo.MachineInfo.MemoryDescInfo value)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`
    - #### addMemoryDescInfoList

      ```
      public Response.NodeInfo.MachineInfo.Builder addMemoryDescInfoList(int index,
                                                                         Response.NodeInfo.MachineInfo.MemoryDescInfo value)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`
    - #### addMemoryDescInfoList

      ```
      public Response.NodeInfo.MachineInfo.Builder addMemoryDescInfoList(Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder builderForValue)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`
    - #### addMemoryDescInfoList

      ```
      public Response.NodeInfo.MachineInfo.Builder addMemoryDescInfoList(int index,
                                                                         Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder builderForValue)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`
    - #### addAllMemoryDescInfoList

      ```
      public Response.NodeInfo.MachineInfo.Builder addAllMemoryDescInfoList(java.lang.Iterable<? extends Response.NodeInfo.MachineInfo.MemoryDescInfo> values)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`
    - #### clearMemoryDescInfoList

      ```
      public Response.NodeInfo.MachineInfo.Builder clearMemoryDescInfoList()
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`
    - #### removeMemoryDescInfoList

      ```
      public Response.NodeInfo.MachineInfo.Builder removeMemoryDescInfoList(int index)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`
    - #### getMemoryDescInfoListBuilder

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder getMemoryDescInfoListBuilder(int index)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`
    - #### getMemoryDescInfoListOrBuilder

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder getMemoryDescInfoListOrBuilder(int index)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`

      Specified by:
      :   `getMemoryDescInfoListOrBuilder` in interface `Response.NodeInfo.MachineInfoOrBuilder`
    - #### getMemoryDescInfoListOrBuilderList

      ```
      public java.util.List<? extends Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder> getMemoryDescInfoListOrBuilderList()
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`

      Specified by:
      :   `getMemoryDescInfoListOrBuilderList` in interface `Response.NodeInfo.MachineInfoOrBuilder`
    - #### addMemoryDescInfoListBuilder

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder addMemoryDescInfoListBuilder()
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`
    - #### addMemoryDescInfoListBuilder

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder addMemoryDescInfoListBuilder(int index)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`
    - #### getMemoryDescInfoListBuilderList

      ```
      public java.util.List<Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder> getMemoryDescInfoListBuilderList()
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`
    - #### getDeadLockThreadInfoListList

      ```
      public java.util.List<Response.NodeInfo.MachineInfo.DeadLockThreadInfo> getDeadLockThreadInfoListList()
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`

      Specified by:
      :   `getDeadLockThreadInfoListList` in interface `Response.NodeInfo.MachineInfoOrBuilder`
    - #### getDeadLockThreadInfoListCount

      ```
      public int getDeadLockThreadInfoListCount()
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`

      Specified by:
      :   `getDeadLockThreadInfoListCount` in interface `Response.NodeInfo.MachineInfoOrBuilder`
    - #### getDeadLockThreadInfoList

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo getDeadLockThreadInfoList(int index)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`

      Specified by:
      :   `getDeadLockThreadInfoList` in interface `Response.NodeInfo.MachineInfoOrBuilder`
    - #### setDeadLockThreadInfoList

      ```
      public Response.NodeInfo.MachineInfo.Builder setDeadLockThreadInfoList(int index,
                                                                             Response.NodeInfo.MachineInfo.DeadLockThreadInfo value)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`
    - #### setDeadLockThreadInfoList

      ```
      public Response.NodeInfo.MachineInfo.Builder setDeadLockThreadInfoList(int index,
                                                                             Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder builderForValue)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`
    - #### addDeadLockThreadInfoList

      ```
      public Response.NodeInfo.MachineInfo.Builder addDeadLockThreadInfoList(Response.NodeInfo.MachineInfo.DeadLockThreadInfo value)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`
    - #### addDeadLockThreadInfoList

      ```
      public Response.NodeInfo.MachineInfo.Builder addDeadLockThreadInfoList(int index,
                                                                             Response.NodeInfo.MachineInfo.DeadLockThreadInfo value)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`
    - #### addDeadLockThreadInfoList

      ```
      public Response.NodeInfo.MachineInfo.Builder addDeadLockThreadInfoList(Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder builderForValue)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`
    - #### addDeadLockThreadInfoList

      ```
      public Response.NodeInfo.MachineInfo.Builder addDeadLockThreadInfoList(int index,
                                                                             Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder builderForValue)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`
    - #### addAllDeadLockThreadInfoList

      ```
      public Response.NodeInfo.MachineInfo.Builder addAllDeadLockThreadInfoList(java.lang.Iterable<? extends Response.NodeInfo.MachineInfo.DeadLockThreadInfo> values)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`
    - #### clearDeadLockThreadInfoList

      ```
      public Response.NodeInfo.MachineInfo.Builder clearDeadLockThreadInfoList()
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`
    - #### removeDeadLockThreadInfoList

      ```
      public Response.NodeInfo.MachineInfo.Builder removeDeadLockThreadInfoList(int index)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`
    - #### getDeadLockThreadInfoListBuilder

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder getDeadLockThreadInfoListBuilder(int index)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`
    - #### getDeadLockThreadInfoListOrBuilder

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder getDeadLockThreadInfoListOrBuilder(int index)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`

      Specified by:
      :   `getDeadLockThreadInfoListOrBuilder` in interface `Response.NodeInfo.MachineInfoOrBuilder`
    - #### getDeadLockThreadInfoListOrBuilderList

      ```
      public java.util.List<? extends Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder> getDeadLockThreadInfoListOrBuilderList()
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`

      Specified by:
      :   `getDeadLockThreadInfoListOrBuilderList` in interface `Response.NodeInfo.MachineInfoOrBuilder`
    - #### addDeadLockThreadInfoListBuilder

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder addDeadLockThreadInfoListBuilder()
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`
    - #### addDeadLockThreadInfoListBuilder

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder addDeadLockThreadInfoListBuilder(int index)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`
    - #### getDeadLockThreadInfoListBuilderList

      ```
      public java.util.List<Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder> getDeadLockThreadInfoListBuilderList()
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`
    - #### setUnknownFields

      ```
      public final Response.NodeInfo.MachineInfo.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.NodeInfo.MachineInfo.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.Builder>`