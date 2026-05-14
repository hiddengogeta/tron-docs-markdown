

org.tron.trident.proto

## Class Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder](../../../../org/tron/trident/proto/Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder](../../../../org/tron/trident/proto/Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.NodeInfo.MachineInfo.MemoryDescInfo](../../../../org/tron/trident/proto/Response.NodeInfo.MachineInfo.MemoryDescInfo.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder>
  implements Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder
  ```

  Protobuf type `protocol.NodeInfo.MachineInfo.MemoryDescInfo`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo` | `build()` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo` | `buildPartial()` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `clear()` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `clearInitSize()` `int64 initSize = 2;` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `clearMaxSize()` `int64 maxSize = 4;` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `clearName()` `string name = 1;` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `clearUseRate()` `double useRate = 5;` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `clearUseSize()` `int64 useSize = 3;` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `clone()` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getInitSize()` `int64 initSize = 2;` |
    | `long` | `getMaxSize()` `int64 maxSize = 4;` |
    | `java.lang.String` | `getName()` `string name = 1;` |
    | `com.google.protobuf.ByteString` | `getNameBytes()` `string name = 1;` |
    | `double` | `getUseRate()` `double useRate = 5;` |
    | `long` | `getUseSize()` `int64 useSize = 3;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `mergeFrom(Response.NodeInfo.MachineInfo.MemoryDescInfo other)` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `setInitSize(long value)` `int64 initSize = 2;` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `setMaxSize(long value)` `int64 maxSize = 4;` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `setName(java.lang.String value)` `string name = 1;` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `setNameBytes(com.google.protobuf.ByteString value)` `string name = 1;` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `setUseRate(double value)` `double useRate = 5;` |
    | `Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder` | `setUseSize(long value)` `int64 useSize = 3;` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder>`
    - #### clear

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder>`
    - #### setField

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                           java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder>`
    - #### clearField

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder>`
    - #### clearOneof

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder>`
    - #### setRepeatedField

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                   int index,
                                                                                   java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder>`
    - #### addRepeatedField

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                   java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder mergeFrom(Response.NodeInfo.MachineInfo.MemoryDescInfo other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder>`
    - #### mergeFrom

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                     throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getName

      ```
      public java.lang.String getName()
      ```

      `string name = 1;`

      Specified by:
      :   `getName` in interface `Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder`

      Returns:
      :   The name.
    - #### getNameBytes

      ```
      public com.google.protobuf.ByteString getNameBytes()
      ```

      `string name = 1;`

      Specified by:
      :   `getNameBytes` in interface `Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder`

      Returns:
      :   The bytes for name.
    - #### setName

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder setName(java.lang.String value)
      ```

      `string name = 1;`

      Parameters:
      :   `value` - The name to set.

      Returns:
      :   This builder for chaining.
    - #### clearName

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder clearName()
      ```

      `string name = 1;`

      Returns:
      :   This builder for chaining.
    - #### setNameBytes

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder setNameBytes(com.google.protobuf.ByteString value)
      ```

      `string name = 1;`

      Parameters:
      :   `value` - The bytes for name to set.

      Returns:
      :   This builder for chaining.
    - #### getInitSize

      ```
      public long getInitSize()
      ```

      `int64 initSize = 2;`

      Specified by:
      :   `getInitSize` in interface `Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder`

      Returns:
      :   The initSize.
    - #### setInitSize

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder setInitSize(long value)
      ```

      `int64 initSize = 2;`

      Parameters:
      :   `value` - The initSize to set.

      Returns:
      :   This builder for chaining.
    - #### clearInitSize

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder clearInitSize()
      ```

      `int64 initSize = 2;`

      Returns:
      :   This builder for chaining.
    - #### getUseSize

      ```
      public long getUseSize()
      ```

      `int64 useSize = 3;`

      Specified by:
      :   `getUseSize` in interface `Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder`

      Returns:
      :   The useSize.
    - #### setUseSize

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder setUseSize(long value)
      ```

      `int64 useSize = 3;`

      Parameters:
      :   `value` - The useSize to set.

      Returns:
      :   This builder for chaining.
    - #### clearUseSize

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder clearUseSize()
      ```

      `int64 useSize = 3;`

      Returns:
      :   This builder for chaining.
    - #### getMaxSize

      ```
      public long getMaxSize()
      ```

      `int64 maxSize = 4;`

      Specified by:
      :   `getMaxSize` in interface `Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder`

      Returns:
      :   The maxSize.
    - #### setMaxSize

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder setMaxSize(long value)
      ```

      `int64 maxSize = 4;`

      Parameters:
      :   `value` - The maxSize to set.

      Returns:
      :   This builder for chaining.
    - #### clearMaxSize

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder clearMaxSize()
      ```

      `int64 maxSize = 4;`

      Returns:
      :   This builder for chaining.
    - #### getUseRate

      ```
      public double getUseRate()
      ```

      `double useRate = 5;`

      Specified by:
      :   `getUseRate` in interface `Response.NodeInfo.MachineInfo.MemoryDescInfoOrBuilder`

      Returns:
      :   The useRate.
    - #### setUseRate

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder setUseRate(double value)
      ```

      `double useRate = 5;`

      Parameters:
      :   `value` - The useRate to set.

      Returns:
      :   This builder for chaining.
    - #### clearUseRate

      ```
      public Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder clearUseRate()
      ```

      `double useRate = 5;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.NodeInfo.MachineInfo.MemoryDescInfo.Builder>`