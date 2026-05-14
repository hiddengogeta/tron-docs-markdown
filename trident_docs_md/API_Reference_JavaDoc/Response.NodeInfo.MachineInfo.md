

org.tron.trident.proto

## Class Response.NodeInfo.MachineInfo

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.NodeInfo.MachineInfo

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.NodeInfo.MachineInfoOrBuilder](../../../../org/tron/trident/proto/Response.NodeInfo.MachineInfoOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.NodeInfo](../../../../org/tron/trident/proto/Response.NodeInfo.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.NodeInfo.MachineInfo
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.NodeInfo.MachineInfoOrBuilder
  ```

  Protobuf type `protocol.NodeInfo.MachineInfo`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.NodeInfo.MachineInfo.Builder` Protobuf type `protocol.NodeInfo.MachineInfo` |
    | `static class` | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo` Protobuf type `protocol.NodeInfo.MachineInfo.DeadLockThreadInfo` |
    | `static interface` | `Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder` |
    | `static class` | `Response.NodeInfo.MachineInfo.MemoryDescInfo` Protobuf type `protocol.NodeInfo.MachineInfo.MemoryDescInfo` |
    | `static interface` | `Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `CPUCOUNT_FIELD_NUMBER` |
    | `static int` | `CPURATE_FIELD_NUMBER` |
    | `static int` | `DEADLOCKTHREADCOUNT_FIELD_NUMBER` |
    | `static int` | `DEADLOCKTHREADINFOLIST_FIELD_NUMBER` |
    | `static int` | `FREEMEMORY_FIELD_NUMBER` |
    | `static int` | `JAVAVERSION_FIELD_NUMBER` |
    | `static int` | `JVMFREEMEMORY_FIELD_NUMBER` |
    | `static int` | `JVMTOTALMEMOERY_FIELD_NUMBER` |
    | `static int` | `MEMORYDESCINFOLIST_FIELD_NUMBER` |
    | `static int` | `OSNAME_FIELD_NUMBER` |
    | `static int` | `PROCESSCPURATE_FIELD_NUMBER` |
    | `static int` | `THREADCOUNT_FIELD_NUMBER` |
    | `static int` | `TOTALMEMORY_FIELD_NUMBER` |

    - ### Fields inherited from class com.google.protobuf.GeneratedMessageV3

      `alwaysUseFieldBuilders, unknownFields`
    - ### Fields inherited from class com.google.protobuf.AbstractMessage

      `memoizedSize`
    - ### Fields inherited from class com.google.protobuf.AbstractMessageLite

      `memoizedHashCode`
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `boolean` | `equals(java.lang.Object obj)` |
    | `int` | `getCpuCount()` `int32 cpuCount = 3;` |
    | `double` | `getCpuRate()` `double cpuRate = 6;` |
    | `int` | `getDeadLockThreadCount()` `int32 deadLockThreadCount = 2;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo` | `getDeadLockThreadInfoList(int index)` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `int` | `getDeadLockThreadInfoListCount()` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `java.util.List<Response.NodeInfo.MachineInfo.DeadLockThreadInfo>` | `getDeadLockThreadInfoListList()` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder` | `getDeadLockThreadInfoListOrBuilder(int index)` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `java.util.List<? extends Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder>` | `getDeadLockThreadInfoListOrBuilderList()` `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;` |
    | `static Response.NodeInfo.MachineInfo` | `getDefaultInstance()` |
    | `Response.NodeInfo.MachineInfo` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
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
    | `com.google.protobuf.Parser<Response.NodeInfo.MachineInfo>` | `getParserForType()` |
    | `double` | `getProcessCpuRate()` `double processCpuRate = 11;` |
    | `int` | `getSerializedSize()` |
    | `int` | `getThreadCount()` `int32 threadCount = 1;` |
    | `long` | `getTotalMemory()` `int64 totalMemory = 4;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Response.NodeInfo.MachineInfo.Builder` | `newBuilder()` |
    | `static Response.NodeInfo.MachineInfo.Builder` | `newBuilder(Response.NodeInfo.MachineInfo prototype)` |
    | `Response.NodeInfo.MachineInfo.Builder` | `newBuilderForType()` |
    | `protected Response.NodeInfo.MachineInfo.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.NodeInfo.MachineInfo` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.NodeInfo.MachineInfo` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.MachineInfo` | `parseFrom(byte[] data)` |
    | `static Response.NodeInfo.MachineInfo` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.MachineInfo` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.NodeInfo.MachineInfo` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.MachineInfo` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.NodeInfo.MachineInfo` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.MachineInfo` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.NodeInfo.MachineInfo` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.MachineInfo` | `parseFrom(java.io.InputStream input)` |
    | `static Response.NodeInfo.MachineInfo` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.NodeInfo.MachineInfo>` | `parser()` |
    | `Response.NodeInfo.MachineInfo.Builder` | `toBuilder()` |
    | `void` | `writeTo(com.google.protobuf.CodedOutputStream output)` |

    - ### Methods inherited from class com.google.protobuf.GeneratedMessageV3

      `canUseUnsafe, computeStringSize, computeStringSizeNoTag, emptyBooleanList, emptyDoubleList, emptyFloatList, emptyIntList, emptyList, emptyLongList, getAllFields, getDescriptorForType, getField, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof, internalGetMapField, internalGetMapFieldReflection, isStringEmpty, makeExtensionsImmutable, makeMutableCopy, makeMutableCopy, mergeFromAndMakeImmutableInternal, mutableCopy, mutableCopy, mutableCopy, mutableCopy, mutableCopy, newBooleanList, newBuilderForType, newDoubleList, newFloatList, newIntList, newLongList, parseDelimitedWithIOException, parseDelimitedWithIOException, parseUnknownField, parseUnknownFieldProto3, parseWithIOException, parseWithIOException, parseWithIOException, parseWithIOException, serializeBooleanMapTo, serializeIntegerMapTo, serializeLongMapTo, serializeStringMapTo, writeReplace, writeString, writeStringNoTag`
    - ### Methods inherited from class com.google.protobuf.AbstractMessage

      `findInitializationErrors, getInitializationErrorString, hashBoolean, hashEnum, hashEnumList, hashFields, hashLong, toString`
    - ### Methods inherited from class com.google.protobuf.AbstractMessageLite

      `addAll, addAll, checkByteStringIsUtf8, toByteArray, toByteString, writeDelimitedTo, writeTo`
    - ### Methods inherited from class java.lang.Object

      `clone, finalize, getClass, notify, notifyAll, wait, wait, wait`
    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLite

      `toByteArray, toByteString, writeDelimitedTo, writeTo`

* + ### Field Detail

    - #### THREADCOUNT\_FIELD\_NUMBER

      ```
      public static final int THREADCOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.THREADCOUNT_FIELD_NUMBER)
    - #### DEADLOCKTHREADCOUNT\_FIELD\_NUMBER

      ```
      public static final int DEADLOCKTHREADCOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.DEADLOCKTHREADCOUNT_FIELD_NUMBER)
    - #### CPUCOUNT\_FIELD\_NUMBER

      ```
      public static final int CPUCOUNT_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.CPUCOUNT_FIELD_NUMBER)
    - #### TOTALMEMORY\_FIELD\_NUMBER

      ```
      public static final int TOTALMEMORY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.TOTALMEMORY_FIELD_NUMBER)
    - #### FREEMEMORY\_FIELD\_NUMBER

      ```
      public static final int FREEMEMORY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.FREEMEMORY_FIELD_NUMBER)
    - #### CPURATE\_FIELD\_NUMBER

      ```
      public static final int CPURATE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.CPURATE_FIELD_NUMBER)
    - #### JAVAVERSION\_FIELD\_NUMBER

      ```
      public static final int JAVAVERSION_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.JAVAVERSION_FIELD_NUMBER)
    - #### OSNAME\_FIELD\_NUMBER

      ```
      public static final int OSNAME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.OSNAME_FIELD_NUMBER)
    - #### JVMTOTALMEMOERY\_FIELD\_NUMBER

      ```
      public static final int JVMTOTALMEMOERY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.JVMTOTALMEMOERY_FIELD_NUMBER)
    - #### JVMFREEMEMORY\_FIELD\_NUMBER

      ```
      public static final int JVMFREEMEMORY_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.JVMFREEMEMORY_FIELD_NUMBER)
    - #### PROCESSCPURATE\_FIELD\_NUMBER

      ```
      public static final int PROCESSCPURATE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.PROCESSCPURATE_FIELD_NUMBER)
    - #### MEMORYDESCINFOLIST\_FIELD\_NUMBER

      ```
      public static final int MEMORYDESCINFOLIST_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.MEMORYDESCINFOLIST_FIELD_NUMBER)
    - #### DEADLOCKTHREADINFOLIST\_FIELD\_NUMBER

      ```
      public static final int DEADLOCKTHREADINFOLIST_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.DEADLOCKTHREADINFOLIST_FIELD_NUMBER)
  + ### Method Detail

    - #### newInstance

      ```
      protected java.lang.Object newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)
      ```

      Overrides:
      :   `newInstance` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDescriptor

      ```
      public static final com.google.protobuf.Descriptors.Descriptor getDescriptor()
      ```
    - #### internalGetFieldAccessorTable

      ```
      protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()
      ```

      Specified by:
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getThreadCount

      ```
      public int getThreadCount()
      ```

      `int32 threadCount = 1;`

      Specified by:
      :   `getThreadCount` in interface `Response.NodeInfo.MachineInfoOrBuilder`

      Returns:
      :   The threadCount.
    - #### getDeadLockThreadCount

      ```
      public int getDeadLockThreadCount()
      ```

      `int32 deadLockThreadCount = 2;`

      Specified by:
      :   `getDeadLockThreadCount` in interface `Response.NodeInfo.MachineInfoOrBuilder`

      Returns:
      :   The deadLockThreadCount.
    - #### getCpuCount

      ```
      public int getCpuCount()
      ```

      `int32 cpuCount = 3;`

      Specified by:
      :   `getCpuCount` in interface `Response.NodeInfo.MachineInfoOrBuilder`

      Returns:
      :   The cpuCount.
    - #### getTotalMemory

      ```
      public long getTotalMemory()
      ```

      `int64 totalMemory = 4;`

      Specified by:
      :   `getTotalMemory` in interface `Response.NodeInfo.MachineInfoOrBuilder`

      Returns:
      :   The totalMemory.
    - #### getFreeMemory

      ```
      public long getFreeMemory()
      ```

      `int64 freeMemory = 5;`

      Specified by:
      :   `getFreeMemory` in interface `Response.NodeInfo.MachineInfoOrBuilder`

      Returns:
      :   The freeMemory.
    - #### getCpuRate

      ```
      public double getCpuRate()
      ```

      `double cpuRate = 6;`

      Specified by:
      :   `getCpuRate` in interface `Response.NodeInfo.MachineInfoOrBuilder`

      Returns:
      :   The cpuRate.
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
    - #### getJvmTotalMemoery

      ```
      public long getJvmTotalMemoery()
      ```

      `int64 jvmTotalMemoery = 9;`

      Specified by:
      :   `getJvmTotalMemoery` in interface `Response.NodeInfo.MachineInfoOrBuilder`

      Returns:
      :   The jvmTotalMemoery.
    - #### getJvmFreeMemory

      ```
      public long getJvmFreeMemory()
      ```

      `int64 jvmFreeMemory = 10;`

      Specified by:
      :   `getJvmFreeMemory` in interface `Response.NodeInfo.MachineInfoOrBuilder`

      Returns:
      :   The jvmFreeMemory.
    - #### getProcessCpuRate

      ```
      public double getProcessCpuRate()
      ```

      `double processCpuRate = 11;`

      Specified by:
      :   `getProcessCpuRate` in interface `Response.NodeInfo.MachineInfoOrBuilder`

      Returns:
      :   The processCpuRate.
    - #### getMemoryDescInfoListList

      ```
      public java.util.List<Response.NodeInfo.MachineInfo.MemoryDescInfo> getMemoryDescInfoListList()
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`

      Specified by:
      :   `getMemoryDescInfoListList` in interface `Response.NodeInfo.MachineInfoOrBuilder`
    - #### getMemoryDescInfoListOrBuilderList

      ```
      public java.util.List<? extends Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder> getMemoryDescInfoListOrBuilderList()
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`

      Specified by:
      :   `getMemoryDescInfoListOrBuilderList` in interface `Response.NodeInfo.MachineInfoOrBuilder`
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
    - #### getMemoryDescInfoListOrBuilder

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder getMemoryDescInfoListOrBuilder(int index)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.MemoryDescInfo memoryDescInfoList = 12;`

      Specified by:
      :   `getMemoryDescInfoListOrBuilder` in interface `Response.NodeInfo.MachineInfoOrBuilder`
    - #### getDeadLockThreadInfoListList

      ```
      public java.util.List<Response.NodeInfo.MachineInfo.DeadLockThreadInfo> getDeadLockThreadInfoListList()
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`

      Specified by:
      :   `getDeadLockThreadInfoListList` in interface `Response.NodeInfo.MachineInfoOrBuilder`
    - #### getDeadLockThreadInfoListOrBuilderList

      ```
      public java.util.List<? extends Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder> getDeadLockThreadInfoListOrBuilderList()
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`

      Specified by:
      :   `getDeadLockThreadInfoListOrBuilderList` in interface `Response.NodeInfo.MachineInfoOrBuilder`
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
    - #### getDeadLockThreadInfoListOrBuilder

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder getDeadLockThreadInfoListOrBuilder(int index)
      ```

      `repeated .protocol.NodeInfo.MachineInfo.DeadLockThreadInfo deadLockThreadInfoList = 13;`

      Specified by:
      :   `getDeadLockThreadInfoListOrBuilder` in interface `Response.NodeInfo.MachineInfoOrBuilder`
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3`
    - #### writeTo

      ```
      public void writeTo(com.google.protobuf.CodedOutputStream output)
                   throws java.io.IOException
      ```

      Specified by:
      :   `writeTo` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `writeTo` in class `com.google.protobuf.GeneratedMessageV3`

      Throws:
      :   `java.io.IOException`
    - #### getSerializedSize

      ```
      public int getSerializedSize()
      ```

      Specified by:
      :   `getSerializedSize` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getSerializedSize` in class `com.google.protobuf.GeneratedMessageV3`
    - #### equals

      ```
      public boolean equals(java.lang.Object obj)
      ```

      Specified by:
      :   `equals` in interface `com.google.protobuf.Message`

      Overrides:
      :   `equals` in class `com.google.protobuf.AbstractMessage`
    - #### hashCode

      ```
      public int hashCode()
      ```

      Specified by:
      :   `hashCode` in interface `com.google.protobuf.Message`

      Overrides:
      :   `hashCode` in class `com.google.protobuf.AbstractMessage`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo parseFrom(java.nio.ByteBuffer data)
                                                     throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo parseFrom(java.nio.ByteBuffer data,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo parseFrom(com.google.protobuf.ByteString data)
                                                     throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo parseFrom(com.google.protobuf.ByteString data,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo parseFrom(byte[] data)
                                                     throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo parseFrom(byte[] data,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo parseFrom(java.io.InputStream input)
                                                     throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo parseFrom(java.io.InputStream input,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.NodeInfo.MachineInfo parseDelimitedFrom(java.io.InputStream input)
                                                              throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.NodeInfo.MachineInfo parseDelimitedFrom(java.io.InputStream input,
                                                                     com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                              throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo parseFrom(com.google.protobuf.CodedInputStream input)
                                                     throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo parseFrom(com.google.protobuf.CodedInputStream input,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.NodeInfo.MachineInfo.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.NodeInfo.MachineInfo.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.NodeInfo.MachineInfo.Builder newBuilder(Response.NodeInfo.MachineInfo prototype)
      ```
    - #### toBuilder

      ```
      public Response.NodeInfo.MachineInfo.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.NodeInfo.MachineInfo.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.NodeInfo.MachineInfo getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.NodeInfo.MachineInfo> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.NodeInfo.MachineInfo> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.NodeInfo.MachineInfo getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`