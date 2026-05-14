

org.tron.trident.proto

## Class Response.Account.FreezeV2.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.Account.FreezeV2.Builder](../../../../org/tron/trident/proto/Response.Account.FreezeV2.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.Account.FreezeV2.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.Account.FreezeV2OrBuilder](../../../../org/tron/trident/proto/Response.Account.FreezeV2OrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.Account.FreezeV2](../../../../org/tron/trident/proto/Response.Account.FreezeV2.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.Account.FreezeV2.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.FreezeV2.Builder>
  implements Response.Account.FreezeV2OrBuilder
  ```

  Protobuf type `protocol.Account.FreezeV2`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.Account.FreezeV2.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.Account.FreezeV2` | `build()` |
    | `Response.Account.FreezeV2` | `buildPartial()` |
    | `Response.Account.FreezeV2.Builder` | `clear()` |
    | `Response.Account.FreezeV2.Builder` | `clearAmount()` `int64 amount = 2;` |
    | `Response.Account.FreezeV2.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.Account.FreezeV2.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.Account.FreezeV2.Builder` | `clearType()` `.protocol.ResourceCode type = 1;` |
    | `Response.Account.FreezeV2.Builder` | `clone()` |
    | `long` | `getAmount()` `int64 amount = 2;` |
    | `Response.Account.FreezeV2` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Common.ResourceCode` | `getType()` `.protocol.ResourceCode type = 1;` |
    | `int` | `getTypeValue()` `.protocol.ResourceCode type = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.Account.FreezeV2.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.Account.FreezeV2.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.Account.FreezeV2.Builder` | `mergeFrom(Response.Account.FreezeV2 other)` |
    | `Response.Account.FreezeV2.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.Account.FreezeV2.Builder` | `setAmount(long value)` `int64 amount = 2;` |
    | `Response.Account.FreezeV2.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.Account.FreezeV2.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.Account.FreezeV2.Builder` | `setType(Common.ResourceCode value)` `.protocol.ResourceCode type = 1;` |
    | `Response.Account.FreezeV2.Builder` | `setTypeValue(int value)` `.protocol.ResourceCode type = 1;` |
    | `Response.Account.FreezeV2.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.FreezeV2.Builder>`
    - #### clear

      ```
      public Response.Account.FreezeV2.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.FreezeV2.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.FreezeV2.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.Account.FreezeV2 getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.Account.FreezeV2 build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.Account.FreezeV2 buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.Account.FreezeV2.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.FreezeV2.Builder>`
    - #### setField

      ```
      public Response.Account.FreezeV2.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                        java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.FreezeV2.Builder>`
    - #### clearField

      ```
      public Response.Account.FreezeV2.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.FreezeV2.Builder>`
    - #### clearOneof

      ```
      public Response.Account.FreezeV2.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.FreezeV2.Builder>`
    - #### setRepeatedField

      ```
      public Response.Account.FreezeV2.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                int index,
                                                                java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.FreezeV2.Builder>`
    - #### addRepeatedField

      ```
      public Response.Account.FreezeV2.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.FreezeV2.Builder>`
    - #### mergeFrom

      ```
      public Response.Account.FreezeV2.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.Account.FreezeV2.Builder>`
    - #### mergeFrom

      ```
      public Response.Account.FreezeV2.Builder mergeFrom(Response.Account.FreezeV2 other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.FreezeV2.Builder>`
    - #### mergeFrom

      ```
      public Response.Account.FreezeV2.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                         com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                  throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.Account.FreezeV2.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getTypeValue

      ```
      public int getTypeValue()
      ```

      `.protocol.ResourceCode type = 1;`

      Specified by:
      :   `getTypeValue` in interface `Response.Account.FreezeV2OrBuilder`

      Returns:
      :   The enum numeric value on the wire for type.
    - #### setTypeValue

      ```
      public Response.Account.FreezeV2.Builder setTypeValue(int value)
      ```

      `.protocol.ResourceCode type = 1;`

      Parameters:
      :   `value` - The enum numeric value on the wire for type to set.

      Returns:
      :   This builder for chaining.
    - #### getType

      ```
      public Common.ResourceCode getType()
      ```

      `.protocol.ResourceCode type = 1;`

      Specified by:
      :   `getType` in interface `Response.Account.FreezeV2OrBuilder`

      Returns:
      :   The type.
    - #### setType

      ```
      public Response.Account.FreezeV2.Builder setType(Common.ResourceCode value)
      ```

      `.protocol.ResourceCode type = 1;`

      Parameters:
      :   `value` - The type to set.

      Returns:
      :   This builder for chaining.
    - #### clearType

      ```
      public Response.Account.FreezeV2.Builder clearType()
      ```

      `.protocol.ResourceCode type = 1;`

      Returns:
      :   This builder for chaining.
    - #### getAmount

      ```
      public long getAmount()
      ```

      `int64 amount = 2;`

      Specified by:
      :   `getAmount` in interface `Response.Account.FreezeV2OrBuilder`

      Returns:
      :   The amount.
    - #### setAmount

      ```
      public Response.Account.FreezeV2.Builder setAmount(long value)
      ```

      `int64 amount = 2;`

      Parameters:
      :   `value` - The amount to set.

      Returns:
      :   This builder for chaining.
    - #### clearAmount

      ```
      public Response.Account.FreezeV2.Builder clearAmount()
      ```

      `int64 amount = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.Account.FreezeV2.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.FreezeV2.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.Account.FreezeV2.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.Account.FreezeV2.Builder>`