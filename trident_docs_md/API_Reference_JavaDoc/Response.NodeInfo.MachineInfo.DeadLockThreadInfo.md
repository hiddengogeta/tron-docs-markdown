

org.tron.trident.proto

## Class Response.NodeInfo.MachineInfo.DeadLockThreadInfo

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.NodeInfo.MachineInfo.DeadLockThreadInfo

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder](../../../../org/tron/trident/proto/Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.NodeInfo.MachineInfo](../../../../org/tron/trident/proto/Response.NodeInfo.MachineInfo.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.NodeInfo.MachineInfo.DeadLockThreadInfo
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder
  ```

  Protobuf type `protocol.NodeInfo.MachineInfo.DeadLockThreadInfo`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.DeadLockThreadInfo)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` Protobuf type `protocol.NodeInfo.MachineInfo.DeadLockThreadInfo` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `BLOCKTIME_FIELD_NUMBER` |
    | `static int` | `LOCKNAME_FIELD_NUMBER` |
    | `static int` | `LOCKOWNER_FIELD_NUMBER` |
    | `static int` | `NAME_FIELD_NUMBER` |
    | `static int` | `STACKTRACE_FIELD_NUMBER` |
    | `static int` | `STATE_FIELD_NUMBER` |
    | `static int` | `WAITTIME_FIELD_NUMBER` |

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
    | `long` | `getBlockTime()` `int64 blockTime = 5;` |
    | `static Response.NodeInfo.MachineInfo.DeadLockThreadInfo` | `getDefaultInstance()` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `java.lang.String` | `getLockName()` `string lockName = 2;` |
    | `com.google.protobuf.ByteString` | `getLockNameBytes()` `string lockName = 2;` |
    | `java.lang.String` | `getLockOwner()` `string lockOwner = 3;` |
    | `com.google.protobuf.ByteString` | `getLockOwnerBytes()` `string lockOwner = 3;` |
    | `java.lang.String` | `getName()` `string name = 1;` |
    | `com.google.protobuf.ByteString` | `getNameBytes()` `string name = 1;` |
    | `com.google.protobuf.Parser<Response.NodeInfo.MachineInfo.DeadLockThreadInfo>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `java.lang.String` | `getStackTrace()` `string stackTrace = 7;` |
    | `com.google.protobuf.ByteString` | `getStackTraceBytes()` `string stackTrace = 7;` |
    | `java.lang.String` | `getState()` `string state = 4;` |
    | `com.google.protobuf.ByteString` | `getStateBytes()` `string state = 4;` |
    | `long` | `getWaitTime()` `int64 waitTime = 6;` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `newBuilder()` |
    | `static Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `newBuilder(Response.NodeInfo.MachineInfo.DeadLockThreadInfo prototype)` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `newBuilderForType()` |
    | `protected Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.NodeInfo.MachineInfo.DeadLockThreadInfo` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.NodeInfo.MachineInfo.DeadLockThreadInfo` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.MachineInfo.DeadLockThreadInfo` | `parseFrom(byte[] data)` |
    | `static Response.NodeInfo.MachineInfo.DeadLockThreadInfo` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.MachineInfo.DeadLockThreadInfo` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.NodeInfo.MachineInfo.DeadLockThreadInfo` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.MachineInfo.DeadLockThreadInfo` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.NodeInfo.MachineInfo.DeadLockThreadInfo` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.MachineInfo.DeadLockThreadInfo` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.NodeInfo.MachineInfo.DeadLockThreadInfo` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.NodeInfo.MachineInfo.DeadLockThreadInfo` | `parseFrom(java.io.InputStream input)` |
    | `static Response.NodeInfo.MachineInfo.DeadLockThreadInfo` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.NodeInfo.MachineInfo.DeadLockThreadInfo>` | `parser()` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `toBuilder()` |
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

    - #### NAME\_FIELD\_NUMBER

      ```
      public static final int NAME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.DeadLockThreadInfo.NAME_FIELD_NUMBER)
    - #### LOCKNAME\_FIELD\_NUMBER

      ```
      public static final int LOCKNAME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.DeadLockThreadInfo.LOCKNAME_FIELD_NUMBER)
    - #### LOCKOWNER\_FIELD\_NUMBER

      ```
      public static final int LOCKOWNER_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.DeadLockThreadInfo.LOCKOWNER_FIELD_NUMBER)
    - #### STATE\_FIELD\_NUMBER

      ```
      public static final int STATE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.DeadLockThreadInfo.STATE_FIELD_NUMBER)
    - #### BLOCKTIME\_FIELD\_NUMBER

      ```
      public static final int BLOCKTIME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.DeadLockThreadInfo.BLOCKTIME_FIELD_NUMBER)
    - #### WAITTIME\_FIELD\_NUMBER

      ```
      public static final int WAITTIME_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.DeadLockThreadInfo.WAITTIME_FIELD_NUMBER)
    - #### STACKTRACE\_FIELD\_NUMBER

      ```
      public static final int STACKTRACE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.NodeInfo.MachineInfo.DeadLockThreadInfo.STACKTRACE_FIELD_NUMBER)
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
    - #### getName

      ```
      public java.lang.String getName()
      ```

      `string name = 1;`

      Specified by:
      :   `getName` in interface `Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder`

      Returns:
      :   The name.
    - #### getNameBytes

      ```
      public com.google.protobuf.ByteString getNameBytes()
      ```

      `string name = 1;`

      Specified by:
      :   `getNameBytes` in interface `Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder`

      Returns:
      :   The bytes for name.
    - #### getLockName

      ```
      public java.lang.String getLockName()
      ```

      `string lockName = 2;`

      Specified by:
      :   `getLockName` in interface `Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder`

      Returns:
      :   The lockName.
    - #### getLockNameBytes

      ```
      public com.google.protobuf.ByteString getLockNameBytes()
      ```

      `string lockName = 2;`

      Specified by:
      :   `getLockNameBytes` in interface `Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder`

      Returns:
      :   The bytes for lockName.
    - #### getLockOwner

      ```
      public java.lang.String getLockOwner()
      ```

      `string lockOwner = 3;`

      Specified by:
      :   `getLockOwner` in interface `Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder`

      Returns:
      :   The lockOwner.
    - #### getLockOwnerBytes

      ```
      public com.google.protobuf.ByteString getLockOwnerBytes()
      ```

      `string lockOwner = 3;`

      Specified by:
      :   `getLockOwnerBytes` in interface `Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder`

      Returns:
      :   The bytes for lockOwner.
    - #### getState

      ```
      public java.lang.String getState()
      ```

      `string state = 4;`

      Specified by:
      :   `getState` in interface `Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder`

      Returns:
      :   The state.
    - #### getStateBytes

      ```
      public com.google.protobuf.ByteString getStateBytes()
      ```

      `string state = 4;`

      Specified by:
      :   `getStateBytes` in interface `Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder`

      Returns:
      :   The bytes for state.
    - #### getBlockTime

      ```
      public long getBlockTime()
      ```

      `int64 blockTime = 5;`

      Specified by:
      :   `getBlockTime` in interface `Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder`

      Returns:
      :   The blockTime.
    - #### getWaitTime

      ```
      public long getWaitTime()
      ```

      `int64 waitTime = 6;`

      Specified by:
      :   `getWaitTime` in interface `Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder`

      Returns:
      :   The waitTime.
    - #### getStackTrace

      ```
      public java.lang.String getStackTrace()
      ```

      `string stackTrace = 7;`

      Specified by:
      :   `getStackTrace` in interface `Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder`

      Returns:
      :   The stackTrace.
    - #### getStackTraceBytes

      ```
      public com.google.protobuf.ByteString getStackTraceBytes()
      ```

      `string stackTrace = 7;`

      Specified by:
      :   `getStackTraceBytes` in interface `Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder`

      Returns:
      :   The bytes for stackTrace.
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
      public static Response.NodeInfo.MachineInfo.DeadLockThreadInfo parseFrom(java.nio.ByteBuffer data)
                                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo.DeadLockThreadInfo parseFrom(java.nio.ByteBuffer data,
                                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo.DeadLockThreadInfo parseFrom(com.google.protobuf.ByteString data)
                                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo.DeadLockThreadInfo parseFrom(com.google.protobuf.ByteString data,
                                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo.DeadLockThreadInfo parseFrom(byte[] data)
                                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo.DeadLockThreadInfo parseFrom(byte[] data,
                                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                        throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo.DeadLockThreadInfo parseFrom(java.io.InputStream input)
                                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo.DeadLockThreadInfo parseFrom(java.io.InputStream input,
                                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.NodeInfo.MachineInfo.DeadLockThreadInfo parseDelimitedFrom(java.io.InputStream input)
                                                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.NodeInfo.MachineInfo.DeadLockThreadInfo parseDelimitedFrom(java.io.InputStream input,
                                                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                                 throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo.DeadLockThreadInfo parseFrom(com.google.protobuf.CodedInputStream input)
                                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.NodeInfo.MachineInfo.DeadLockThreadInfo parseFrom(com.google.protobuf.CodedInputStream input,
                                                                               com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                        throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder newBuilder(Response.NodeInfo.MachineInfo.DeadLockThreadInfo prototype)
      ```
    - #### toBuilder

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.NodeInfo.MachineInfo.DeadLockThreadInfo getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.NodeInfo.MachineInfo.DeadLockThreadInfo> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.NodeInfo.MachineInfo.DeadLockThreadInfo> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`