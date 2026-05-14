

org.tron.trident.proto

## Class Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder](../../../../org/tron/trident/proto/Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder](../../../../org/tron/trident/proto/Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.NodeInfo.MachineInfo.DeadLockThreadInfo](../../../../org/tron/trident/proto/Response.NodeInfo.MachineInfo.DeadLockThreadInfo.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder>
  implements Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder
  ```

  Protobuf type `protocol.NodeInfo.MachineInfo.DeadLockThreadInfo`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo` | `build()` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo` | `buildPartial()` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `clear()` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `clearBlockTime()` `int64 blockTime = 5;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `clearLockName()` `string lockName = 2;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `clearLockOwner()` `string lockOwner = 3;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `clearName()` `string name = 1;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `clearStackTrace()` `string stackTrace = 7;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `clearState()` `string state = 4;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `clearWaitTime()` `int64 waitTime = 6;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `clone()` |
    | `long` | `getBlockTime()` `int64 blockTime = 5;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
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
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `mergeFrom(Response.NodeInfo.MachineInfo.DeadLockThreadInfo other)` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `setBlockTime(long value)` `int64 blockTime = 5;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `setLockName(java.lang.String value)` `string lockName = 2;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `setLockNameBytes(com.google.protobuf.ByteString value)` `string lockName = 2;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `setLockOwner(java.lang.String value)` `string lockOwner = 3;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `setLockOwnerBytes(com.google.protobuf.ByteString value)` `string lockOwner = 3;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `setName(java.lang.String value)` `string name = 1;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `setNameBytes(com.google.protobuf.ByteString value)` `string name = 1;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `setStackTrace(java.lang.String value)` `string stackTrace = 7;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `setStackTraceBytes(com.google.protobuf.ByteString value)` `string stackTrace = 7;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `setState(java.lang.String value)` `string state = 4;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `setStateBytes(com.google.protobuf.ByteString value)` `string state = 4;` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder` | `setWaitTime(long value)` `int64 waitTime = 6;` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder>`
    - #### clear

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder>`
    - #### setField

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder>`
    - #### clearField

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder>`
    - #### clearOneof

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder>`
    - #### setRepeatedField

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                       int index,
                                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder>`
    - #### addRepeatedField

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder mergeFrom(Response.NodeInfo.MachineInfo.DeadLockThreadInfo other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                                com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                         throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder>`

      Throws:
      :   `java.io.IOException`
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
    - #### setName

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder setName(java.lang.String value)
      ```

      `string name = 1;`

      Parameters:
      :   `value` - The name to set.

      Returns:
      :   This builder for chaining.
    - #### clearName

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder clearName()
      ```

      `string name = 1;`

      Returns:
      :   This builder for chaining.
    - #### setNameBytes

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder setNameBytes(com.google.protobuf.ByteString value)
      ```

      `string name = 1;`

      Parameters:
      :   `value` - The bytes for name to set.

      Returns:
      :   This builder for chaining.
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
    - #### setLockName

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder setLockName(java.lang.String value)
      ```

      `string lockName = 2;`

      Parameters:
      :   `value` - The lockName to set.

      Returns:
      :   This builder for chaining.
    - #### clearLockName

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder clearLockName()
      ```

      `string lockName = 2;`

      Returns:
      :   This builder for chaining.
    - #### setLockNameBytes

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder setLockNameBytes(com.google.protobuf.ByteString value)
      ```

      `string lockName = 2;`

      Parameters:
      :   `value` - The bytes for lockName to set.

      Returns:
      :   This builder for chaining.
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
    - #### setLockOwner

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder setLockOwner(java.lang.String value)
      ```

      `string lockOwner = 3;`

      Parameters:
      :   `value` - The lockOwner to set.

      Returns:
      :   This builder for chaining.
    - #### clearLockOwner

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder clearLockOwner()
      ```

      `string lockOwner = 3;`

      Returns:
      :   This builder for chaining.
    - #### setLockOwnerBytes

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder setLockOwnerBytes(com.google.protobuf.ByteString value)
      ```

      `string lockOwner = 3;`

      Parameters:
      :   `value` - The bytes for lockOwner to set.

      Returns:
      :   This builder for chaining.
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
    - #### setState

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder setState(java.lang.String value)
      ```

      `string state = 4;`

      Parameters:
      :   `value` - The state to set.

      Returns:
      :   This builder for chaining.
    - #### clearState

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder clearState()
      ```

      `string state = 4;`

      Returns:
      :   This builder for chaining.
    - #### setStateBytes

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder setStateBytes(com.google.protobuf.ByteString value)
      ```

      `string state = 4;`

      Parameters:
      :   `value` - The bytes for state to set.

      Returns:
      :   This builder for chaining.
    - #### getBlockTime

      ```
      public long getBlockTime()
      ```

      `int64 blockTime = 5;`

      Specified by:
      :   `getBlockTime` in interface `Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder`

      Returns:
      :   The blockTime.
    - #### setBlockTime

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder setBlockTime(long value)
      ```

      `int64 blockTime = 5;`

      Parameters:
      :   `value` - The blockTime to set.

      Returns:
      :   This builder for chaining.
    - #### clearBlockTime

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder clearBlockTime()
      ```

      `int64 blockTime = 5;`

      Returns:
      :   This builder for chaining.
    - #### getWaitTime

      ```
      public long getWaitTime()
      ```

      `int64 waitTime = 6;`

      Specified by:
      :   `getWaitTime` in interface `Response.NodeInfo.MachineInfo.DeadLockThreadInfoOrBuilder`

      Returns:
      :   The waitTime.
    - #### setWaitTime

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder setWaitTime(long value)
      ```

      `int64 waitTime = 6;`

      Parameters:
      :   `value` - The waitTime to set.

      Returns:
      :   This builder for chaining.
    - #### clearWaitTime

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder clearWaitTime()
      ```

      `int64 waitTime = 6;`

      Returns:
      :   This builder for chaining.
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
    - #### setStackTrace

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder setStackTrace(java.lang.String value)
      ```

      `string stackTrace = 7;`

      Parameters:
      :   `value` - The stackTrace to set.

      Returns:
      :   This builder for chaining.
    - #### clearStackTrace

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder clearStackTrace()
      ```

      `string stackTrace = 7;`

      Returns:
      :   This builder for chaining.
    - #### setStackTraceBytes

      ```
      public Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder setStackTraceBytes(com.google.protobuf.ByteString value)
      ```

      `string stackTrace = 7;`

      Parameters:
      :   `value` - The bytes for stackTrace to set.

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.DeadLockThreadInfo.Builder>`