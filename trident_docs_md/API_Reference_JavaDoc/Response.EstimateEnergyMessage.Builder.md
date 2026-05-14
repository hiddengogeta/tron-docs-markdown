

org.tron.trident.proto

## Class Response.EstimateEnergyMessage.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.EstimateEnergyMessage.Builder](../../../../org/tron/trident/proto/Response.EstimateEnergyMessage.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.EstimateEnergyMessage.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.EstimateEnergyMessageOrBuilder](../../../../org/tron/trident/proto/Response.EstimateEnergyMessageOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.EstimateEnergyMessage](../../../../org/tron/trident/proto/Response.EstimateEnergyMessage.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.EstimateEnergyMessage.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.EstimateEnergyMessage.Builder>
  implements Response.EstimateEnergyMessageOrBuilder
  ```

  Protobuf type `protocol.EstimateEnergyMessage`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.EstimateEnergyMessage.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.EstimateEnergyMessage` | `build()` |
    | `Response.EstimateEnergyMessage` | `buildPartial()` |
    | `Response.EstimateEnergyMessage.Builder` | `clear()` |
    | `Response.EstimateEnergyMessage.Builder` | `clearEnergyRequired()` `int64 energy_required = 2;` |
    | `Response.EstimateEnergyMessage.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.EstimateEnergyMessage.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.EstimateEnergyMessage.Builder` | `clearResult()` `.protocol.TransactionReturn result = 1;` |
    | `Response.EstimateEnergyMessage.Builder` | `clone()` |
    | `Response.EstimateEnergyMessage` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `long` | `getEnergyRequired()` `int64 energy_required = 2;` |
    | `Response.TransactionReturn` | `getResult()` `.protocol.TransactionReturn result = 1;` |
    | `Response.TransactionReturn.Builder` | `getResultBuilder()` `.protocol.TransactionReturn result = 1;` |
    | `Response.TransactionReturnOrBuilder` | `getResultOrBuilder()` `.protocol.TransactionReturn result = 1;` |
    | `boolean` | `hasResult()` `.protocol.TransactionReturn result = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.EstimateEnergyMessage.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.EstimateEnergyMessage.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.EstimateEnergyMessage.Builder` | `mergeFrom(Response.EstimateEnergyMessage other)` |
    | `Response.EstimateEnergyMessage.Builder` | `mergeResult(Response.TransactionReturn value)` `.protocol.TransactionReturn result = 1;` |
    | `Response.EstimateEnergyMessage.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.EstimateEnergyMessage.Builder` | `setEnergyRequired(long value)` `int64 energy_required = 2;` |
    | `Response.EstimateEnergyMessage.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.EstimateEnergyMessage.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.EstimateEnergyMessage.Builder` | `setResult(Response.TransactionReturn.Builder builderForValue)` `.protocol.TransactionReturn result = 1;` |
    | `Response.EstimateEnergyMessage.Builder` | `setResult(Response.TransactionReturn value)` `.protocol.TransactionReturn result = 1;` |
    | `Response.EstimateEnergyMessage.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EstimateEnergyMessage.Builder>`
    - #### clear

      ```
      public Response.EstimateEnergyMessage.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EstimateEnergyMessage.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EstimateEnergyMessage.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.EstimateEnergyMessage getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.EstimateEnergyMessage build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.EstimateEnergyMessage buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.EstimateEnergyMessage.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EstimateEnergyMessage.Builder>`
    - #### setField

      ```
      public Response.EstimateEnergyMessage.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                             java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EstimateEnergyMessage.Builder>`
    - #### clearField

      ```
      public Response.EstimateEnergyMessage.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EstimateEnergyMessage.Builder>`
    - #### clearOneof

      ```
      public Response.EstimateEnergyMessage.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EstimateEnergyMessage.Builder>`
    - #### setRepeatedField

      ```
      public Response.EstimateEnergyMessage.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     int index,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EstimateEnergyMessage.Builder>`
    - #### addRepeatedField

      ```
      public Response.EstimateEnergyMessage.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EstimateEnergyMessage.Builder>`
    - #### mergeFrom

      ```
      public Response.EstimateEnergyMessage.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.EstimateEnergyMessage.Builder>`
    - #### mergeFrom

      ```
      public Response.EstimateEnergyMessage.Builder mergeFrom(Response.EstimateEnergyMessage other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EstimateEnergyMessage.Builder>`
    - #### mergeFrom

      ```
      public Response.EstimateEnergyMessage.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                       throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.EstimateEnergyMessage.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### hasResult

      ```
      public boolean hasResult()
      ```

      `.protocol.TransactionReturn result = 1;`

      Specified by:
      :   `hasResult` in interface `Response.EstimateEnergyMessageOrBuilder`

      Returns:
      :   Whether the result field is set.
    - #### getResult

      ```
      public Response.TransactionReturn getResult()
      ```

      `.protocol.TransactionReturn result = 1;`

      Specified by:
      :   `getResult` in interface `Response.EstimateEnergyMessageOrBuilder`

      Returns:
      :   The result.
    - #### setResult

      ```
      public Response.EstimateEnergyMessage.Builder setResult(Response.TransactionReturn value)
      ```

      `.protocol.TransactionReturn result = 1;`
    - #### setResult

      ```
      public Response.EstimateEnergyMessage.Builder setResult(Response.TransactionReturn.Builder builderForValue)
      ```

      `.protocol.TransactionReturn result = 1;`
    - #### mergeResult

      ```
      public Response.EstimateEnergyMessage.Builder mergeResult(Response.TransactionReturn value)
      ```

      `.protocol.TransactionReturn result = 1;`
    - #### clearResult

      ```
      public Response.EstimateEnergyMessage.Builder clearResult()
      ```

      `.protocol.TransactionReturn result = 1;`
    - #### getResultBuilder

      ```
      public Response.TransactionReturn.Builder getResultBuilder()
      ```

      `.protocol.TransactionReturn result = 1;`
    - #### getResultOrBuilder

      ```
      public Response.TransactionReturnOrBuilder getResultOrBuilder()
      ```

      `.protocol.TransactionReturn result = 1;`

      Specified by:
      :   `getResultOrBuilder` in interface `Response.EstimateEnergyMessageOrBuilder`
    - #### getEnergyRequired

      ```
      public long getEnergyRequired()
      ```

      `int64 energy_required = 2;`

      Specified by:
      :   `getEnergyRequired` in interface `Response.EstimateEnergyMessageOrBuilder`

      Returns:
      :   The energyRequired.
    - #### setEnergyRequired

      ```
      public Response.EstimateEnergyMessage.Builder setEnergyRequired(long value)
      ```

      `int64 energy_required = 2;`

      Parameters:
      :   `value` - The energyRequired to set.

      Returns:
      :   This builder for chaining.
    - #### clearEnergyRequired

      ```
      public Response.EstimateEnergyMessage.Builder clearEnergyRequired()
      ```

      `int64 energy_required = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.EstimateEnergyMessage.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EstimateEnergyMessage.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.EstimateEnergyMessage.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.EstimateEnergyMessage.Builder>`