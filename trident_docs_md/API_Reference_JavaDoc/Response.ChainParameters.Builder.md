

org.tron.trident.proto

## Class Response.ChainParameters.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.ChainParameters.Builder](../../../../org/tron/trident/proto/Response.ChainParameters.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.ChainParameters.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.ChainParametersOrBuilder](../../../../org/tron/trident/proto/Response.ChainParametersOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.ChainParameters](../../../../org/tron/trident/proto/Response.ChainParameters.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.ChainParameters.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.Builder>
  implements Response.ChainParametersOrBuilder
  ```

  Protobuf type `protocol.ChainParameters`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.ChainParameters.Builder` | `addAllChainParameter(java.lang.Iterable<? extends Response.ChainParameters.ChainParameter> values)` `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;` |
    | `Response.ChainParameters.Builder` | `addChainParameter(int index, Response.ChainParameters.ChainParameter.Builder builderForValue)` `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;` |
    | `Response.ChainParameters.Builder` | `addChainParameter(int index, Response.ChainParameters.ChainParameter value)` `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;` |
    | `Response.ChainParameters.Builder` | `addChainParameter(Response.ChainParameters.ChainParameter.Builder builderForValue)` `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;` |
    | `Response.ChainParameters.Builder` | `addChainParameter(Response.ChainParameters.ChainParameter value)` `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;` |
    | `Response.ChainParameters.ChainParameter.Builder` | `addChainParameterBuilder()` `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;` |
    | `Response.ChainParameters.ChainParameter.Builder` | `addChainParameterBuilder(int index)` `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;` |
    | `Response.ChainParameters.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.ChainParameters` | `build()` |
    | `Response.ChainParameters` | `buildPartial()` |
    | `Response.ChainParameters.Builder` | `clear()` |
    | `Response.ChainParameters.Builder` | `clearChainParameter()` `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;` |
    | `Response.ChainParameters.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.ChainParameters.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.ChainParameters.Builder` | `clone()` |
    | `Response.ChainParameters.ChainParameter` | `getChainParameter(int index)` `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;` |
    | `Response.ChainParameters.ChainParameter.Builder` | `getChainParameterBuilder(int index)` `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;` |
    | `java.util.List<Response.ChainParameters.ChainParameter.Builder>` | `getChainParameterBuilderList()` `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;` |
    | `int` | `getChainParameterCount()` `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;` |
    | `java.util.List<Response.ChainParameters.ChainParameter>` | `getChainParameterList()` `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;` |
    | `Response.ChainParameters.ChainParameterOrBuilder` | `getChainParameterOrBuilder(int index)` `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;` |
    | `java.util.List<? extends Response.ChainParameters.ChainParameterOrBuilder>` | `getChainParameterOrBuilderList()` `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;` |
    | `Response.ChainParameters` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.ChainParameters.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.ChainParameters.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.ChainParameters.Builder` | `mergeFrom(Response.ChainParameters other)` |
    | `Response.ChainParameters.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.ChainParameters.Builder` | `removeChainParameter(int index)` `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;` |
    | `Response.ChainParameters.Builder` | `setChainParameter(int index, Response.ChainParameters.ChainParameter.Builder builderForValue)` `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;` |
    | `Response.ChainParameters.Builder` | `setChainParameter(int index, Response.ChainParameters.ChainParameter value)` `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;` |
    | `Response.ChainParameters.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.ChainParameters.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.ChainParameters.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.Builder>`
    - #### clear

      ```
      public Response.ChainParameters.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.ChainParameters getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.ChainParameters build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.ChainParameters buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.ChainParameters.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.Builder>`
    - #### setField

      ```
      public Response.ChainParameters.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.Builder>`
    - #### clearField

      ```
      public Response.ChainParameters.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.Builder>`
    - #### clearOneof

      ```
      public Response.ChainParameters.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.Builder>`
    - #### setRepeatedField

      ```
      public Response.ChainParameters.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               int index,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.Builder>`
    - #### addRepeatedField

      ```
      public Response.ChainParameters.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.Builder>`
    - #### mergeFrom

      ```
      public Response.ChainParameters.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.ChainParameters.Builder>`
    - #### mergeFrom

      ```
      public Response.ChainParameters.Builder mergeFrom(Response.ChainParameters other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.Builder>`
    - #### mergeFrom

      ```
      public Response.ChainParameters.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                 throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.ChainParameters.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getChainParameterList

      ```
      public java.util.List<Response.ChainParameters.ChainParameter> getChainParameterList()
      ```

      `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;`

      Specified by:
      :   `getChainParameterList` in interface `Response.ChainParametersOrBuilder`
    - #### getChainParameterCount

      ```
      public int getChainParameterCount()
      ```

      `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;`

      Specified by:
      :   `getChainParameterCount` in interface `Response.ChainParametersOrBuilder`
    - #### getChainParameter

      ```
      public Response.ChainParameters.ChainParameter getChainParameter(int index)
      ```

      `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;`

      Specified by:
      :   `getChainParameter` in interface `Response.ChainParametersOrBuilder`
    - #### setChainParameter

      ```
      public Response.ChainParameters.Builder setChainParameter(int index,
                                                                Response.ChainParameters.ChainParameter value)
      ```

      `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;`
    - #### setChainParameter

      ```
      public Response.ChainParameters.Builder setChainParameter(int index,
                                                                Response.ChainParameters.ChainParameter.Builder builderForValue)
      ```

      `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;`
    - #### addChainParameter

      ```
      public Response.ChainParameters.Builder addChainParameter(Response.ChainParameters.ChainParameter value)
      ```

      `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;`
    - #### addChainParameter

      ```
      public Response.ChainParameters.Builder addChainParameter(int index,
                                                                Response.ChainParameters.ChainParameter value)
      ```

      `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;`
    - #### addChainParameter

      ```
      public Response.ChainParameters.Builder addChainParameter(Response.ChainParameters.ChainParameter.Builder builderForValue)
      ```

      `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;`
    - #### addChainParameter

      ```
      public Response.ChainParameters.Builder addChainParameter(int index,
                                                                Response.ChainParameters.ChainParameter.Builder builderForValue)
      ```

      `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;`
    - #### addAllChainParameter

      ```
      public Response.ChainParameters.Builder addAllChainParameter(java.lang.Iterable<? extends Response.ChainParameters.ChainParameter> values)
      ```

      `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;`
    - #### clearChainParameter

      ```
      public Response.ChainParameters.Builder clearChainParameter()
      ```

      `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;`
    - #### removeChainParameter

      ```
      public Response.ChainParameters.Builder removeChainParameter(int index)
      ```

      `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;`
    - #### getChainParameterBuilder

      ```
      public Response.ChainParameters.ChainParameter.Builder getChainParameterBuilder(int index)
      ```

      `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;`
    - #### getChainParameterOrBuilder

      ```
      public Response.ChainParameters.ChainParameterOrBuilder getChainParameterOrBuilder(int index)
      ```

      `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;`

      Specified by:
      :   `getChainParameterOrBuilder` in interface `Response.ChainParametersOrBuilder`
    - #### getChainParameterOrBuilderList

      ```
      public java.util.List<? extends Response.ChainParameters.ChainParameterOrBuilder> getChainParameterOrBuilderList()
      ```

      `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;`

      Specified by:
      :   `getChainParameterOrBuilderList` in interface `Response.ChainParametersOrBuilder`
    - #### addChainParameterBuilder

      ```
      public Response.ChainParameters.ChainParameter.Builder addChainParameterBuilder()
      ```

      `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;`
    - #### addChainParameterBuilder

      ```
      public Response.ChainParameters.ChainParameter.Builder addChainParameterBuilder(int index)
      ```

      `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;`
    - #### getChainParameterBuilderList

      ```
      public java.util.List<Response.ChainParameters.ChainParameter.Builder> getChainParameterBuilderList()
      ```

      `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;`
    - #### setUnknownFields

      ```
      public final Response.ChainParameters.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.ChainParameters.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ChainParameters.Builder>`