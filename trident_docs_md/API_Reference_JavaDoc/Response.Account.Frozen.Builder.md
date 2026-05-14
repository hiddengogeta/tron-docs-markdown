

org.tron.trident.proto

## Class Response.Account.Frozen.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.Account.Frozen.Builder](../../../../org/tron/trident/proto/Response.Account.Frozen.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.Account.Frozen.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.Account.FrozenOrBuilder](../../../../org/tron/trident/proto/Response.Account.FrozenOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.Account.Frozen](../../../../org/tron/trident/proto/Response.Account.Frozen.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.Account.Frozen.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Frozen.Builder>
  implements Response.Account.FrozenOrBuilder
  ```

  ```
   frozen balance
  ```

  Protobuf type `protocol.Account.Frozen`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.Account.Frozen.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.Account.Frozen` | `build()` |
    | `Response.Account.Frozen` | `buildPartial()` |
    | `Response.Account.Frozen.Builder` | `clear()` |
    | `Response.Account.Frozen.Builder` | `clearExpireTime()` the expire time |
    | `Response.Account.Frozen.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.Account.Frozen.Builder` | `clearFrozenBalance()` the frozen trx balance |
    | `Response.Account.Frozen.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.Account.Frozen.Builder` | `clone()` |
    | `Response.Account.Frozen` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getExpireTime()` the expire time |
    | `long` | `getFrozenBalance()` the frozen trx balance |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.Account.Frozen.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.Account.Frozen.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.Account.Frozen.Builder` | `mergeFrom(Response.Account.Frozen other)` |
    | `Response.Account.Frozen.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.Account.Frozen.Builder` | `setExpireTime(long value)` the expire time |
    | `Response.Account.Frozen.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.Account.Frozen.Builder` | `setFrozenBalance(long value)` the frozen trx balance |
    | `Response.Account.Frozen.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.Account.Frozen.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Frozen.Builder>`
    - #### clear

      ```
      public Response.Account.Frozen.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Frozen.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Frozen.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.Account.Frozen getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.Account.Frozen build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.Account.Frozen buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.Account.Frozen.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Frozen.Builder>`
    - #### setField

      ```
      public Response.Account.Frozen.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                      java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Frozen.Builder>`
    - #### clearField

      ```
      public Response.Account.Frozen.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Frozen.Builder>`
    - #### clearOneof

      ```
      public Response.Account.Frozen.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Frozen.Builder>`
    - #### setRepeatedField

      ```
      public Response.Account.Frozen.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                              int index,
                                                              java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Frozen.Builder>`
    - #### addRepeatedField

      ```
      public Response.Account.Frozen.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                              java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Frozen.Builder>`
    - #### mergeFrom

      ```
      public Response.Account.Frozen.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.Account.Frozen.Builder>`
    - #### mergeFrom

      ```
      public Response.Account.Frozen.Builder mergeFrom(Response.Account.Frozen other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Frozen.Builder>`
    - #### mergeFrom

      ```
      public Response.Account.Frozen.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.Account.Frozen.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getFrozenBalance

      ```
      public long getFrozenBalance()
      ```

      ```
       the frozen trx balance
      ```

      `int64 frozen_balance = 1;`

      Specified by:
      :   `getFrozenBalance` in interface `Response.Account.FrozenOrBuilder`

      Returns:
      :   The frozenBalance.
    - #### setFrozenBalance

      ```
      public Response.Account.Frozen.Builder setFrozenBalance(long value)
      ```

      ```
       the frozen trx balance
      ```

      `int64 frozen_balance = 1;`

      Parameters:
      :   `value` - The frozenBalance to set.

      Returns:
      :   This builder for chaining.
    - #### clearFrozenBalance

      ```
      public Response.Account.Frozen.Builder clearFrozenBalance()
      ```

      ```
       the frozen trx balance
      ```

      `int64 frozen_balance = 1;`

      Returns:
      :   This builder for chaining.
    - #### getExpireTime

      ```
      public long getExpireTime()
      ```

      ```
       the expire time
      ```

      `int64 expire_time = 2;`

      Specified by:
      :   `getExpireTime` in interface `Response.Account.FrozenOrBuilder`

      Returns:
      :   The expireTime.
    - #### setExpireTime

      ```
      public Response.Account.Frozen.Builder setExpireTime(long value)
      ```

      ```
       the expire time
      ```

      `int64 expire_time = 2;`

      Parameters:
      :   `value` - The expireTime to set.

      Returns:
      :   This builder for chaining.
    - #### clearExpireTime

      ```
      public Response.Account.Frozen.Builder clearExpireTime()
      ```

      ```
       the expire time
      ```

      `int64 expire_time = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.Account.Frozen.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Frozen.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.Account.Frozen.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.Frozen.Builder>`