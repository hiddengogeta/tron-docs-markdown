

org.tron.trident.proto

## Class Response.WitnessList.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.WitnessList.Builder](../../../../org/tron/trident/proto/Response.WitnessList.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.WitnessList.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.WitnessListOrBuilder](../../../../org/tron/trident/proto/Response.WitnessListOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.WitnessList](../../../../org/tron/trident/proto/Response.WitnessList.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.WitnessList.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.WitnessList.Builder>
  implements Response.WitnessListOrBuilder
  ```

  Protobuf type `protocol.WitnessList`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.WitnessList.Builder` | `addAllWitnesses(java.lang.Iterable<? extends Response.Witness> values)` `repeated .protocol.Witness witnesses = 1;` |
    | `Response.WitnessList.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.WitnessList.Builder` | `addWitnesses(int index, Response.Witness.Builder builderForValue)` `repeated .protocol.Witness witnesses = 1;` |
    | `Response.WitnessList.Builder` | `addWitnesses(int index, Response.Witness value)` `repeated .protocol.Witness witnesses = 1;` |
    | `Response.WitnessList.Builder` | `addWitnesses(Response.Witness.Builder builderForValue)` `repeated .protocol.Witness witnesses = 1;` |
    | `Response.WitnessList.Builder` | `addWitnesses(Response.Witness value)` `repeated .protocol.Witness witnesses = 1;` |
    | `Response.Witness.Builder` | `addWitnessesBuilder()` `repeated .protocol.Witness witnesses = 1;` |
    | `Response.Witness.Builder` | `addWitnessesBuilder(int index)` `repeated .protocol.Witness witnesses = 1;` |
    | `Response.WitnessList` | `build()` |
    | `Response.WitnessList` | `buildPartial()` |
    | `Response.WitnessList.Builder` | `clear()` |
    | `Response.WitnessList.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.WitnessList.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.WitnessList.Builder` | `clearWitnesses()` `repeated .protocol.Witness witnesses = 1;` |
    | `Response.WitnessList.Builder` | `clone()` |
    | `Response.WitnessList` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Response.Witness` | `getWitnesses(int index)` `repeated .protocol.Witness witnesses = 1;` |
    | `Response.Witness.Builder` | `getWitnessesBuilder(int index)` `repeated .protocol.Witness witnesses = 1;` |
    | `java.util.List<Response.Witness.Builder>` | `getWitnessesBuilderList()` `repeated .protocol.Witness witnesses = 1;` |
    | `int` | `getWitnessesCount()` `repeated .protocol.Witness witnesses = 1;` |
    | `java.util.List<Response.Witness>` | `getWitnessesList()` `repeated .protocol.Witness witnesses = 1;` |
    | `Response.WitnessOrBuilder` | `getWitnessesOrBuilder(int index)` `repeated .protocol.Witness witnesses = 1;` |
    | `java.util.List<? extends Response.WitnessOrBuilder>` | `getWitnessesOrBuilderList()` `repeated .protocol.Witness witnesses = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.WitnessList.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.WitnessList.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.WitnessList.Builder` | `mergeFrom(Response.WitnessList other)` |
    | `Response.WitnessList.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.WitnessList.Builder` | `removeWitnesses(int index)` `repeated .protocol.Witness witnesses = 1;` |
    | `Response.WitnessList.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.WitnessList.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.WitnessList.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.WitnessList.Builder` | `setWitnesses(int index, Response.Witness.Builder builderForValue)` `repeated .protocol.Witness witnesses = 1;` |
    | `Response.WitnessList.Builder` | `setWitnesses(int index, Response.Witness value)` `repeated .protocol.Witness witnesses = 1;` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.WitnessList.Builder>`
    - #### clear

      ```
      public Response.WitnessList.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.WitnessList.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.WitnessList.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.WitnessList getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.WitnessList build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.WitnessList buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.WitnessList.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.WitnessList.Builder>`
    - #### setField

      ```
      public Response.WitnessList.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                   java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.WitnessList.Builder>`
    - #### clearField

      ```
      public Response.WitnessList.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.WitnessList.Builder>`
    - #### clearOneof

      ```
      public Response.WitnessList.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.WitnessList.Builder>`
    - #### setRepeatedField

      ```
      public Response.WitnessList.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                           int index,
                                                           java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.WitnessList.Builder>`
    - #### addRepeatedField

      ```
      public Response.WitnessList.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                           java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.WitnessList.Builder>`
    - #### mergeFrom

      ```
      public Response.WitnessList.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.WitnessList.Builder>`
    - #### mergeFrom

      ```
      public Response.WitnessList.Builder mergeFrom(Response.WitnessList other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.WitnessList.Builder>`
    - #### mergeFrom

      ```
      public Response.WitnessList.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                    com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                             throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.WitnessList.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getWitnessesList

      ```
      public java.util.List<Response.Witness> getWitnessesList()
      ```

      `repeated .protocol.Witness witnesses = 1;`

      Specified by:
      :   `getWitnessesList` in interface `Response.WitnessListOrBuilder`
    - #### getWitnessesCount

      ```
      public int getWitnessesCount()
      ```

      `repeated .protocol.Witness witnesses = 1;`

      Specified by:
      :   `getWitnessesCount` in interface `Response.WitnessListOrBuilder`
    - #### getWitnesses

      ```
      public Response.Witness getWitnesses(int index)
      ```

      `repeated .protocol.Witness witnesses = 1;`

      Specified by:
      :   `getWitnesses` in interface `Response.WitnessListOrBuilder`
    - #### setWitnesses

      ```
      public Response.WitnessList.Builder setWitnesses(int index,
                                                       Response.Witness value)
      ```

      `repeated .protocol.Witness witnesses = 1;`
    - #### setWitnesses

      ```
      public Response.WitnessList.Builder setWitnesses(int index,
                                                       Response.Witness.Builder builderForValue)
      ```

      `repeated .protocol.Witness witnesses = 1;`
    - #### addWitnesses

      ```
      public Response.WitnessList.Builder addWitnesses(Response.Witness value)
      ```

      `repeated .protocol.Witness witnesses = 1;`
    - #### addWitnesses

      ```
      public Response.WitnessList.Builder addWitnesses(int index,
                                                       Response.Witness value)
      ```

      `repeated .protocol.Witness witnesses = 1;`
    - #### addWitnesses

      ```
      public Response.WitnessList.Builder addWitnesses(Response.Witness.Builder builderForValue)
      ```

      `repeated .protocol.Witness witnesses = 1;`
    - #### addWitnesses

      ```
      public Response.WitnessList.Builder addWitnesses(int index,
                                                       Response.Witness.Builder builderForValue)
      ```

      `repeated .protocol.Witness witnesses = 1;`
    - #### addAllWitnesses

      ```
      public Response.WitnessList.Builder addAllWitnesses(java.lang.Iterable<? extends Response.Witness> values)
      ```

      `repeated .protocol.Witness witnesses = 1;`
    - #### clearWitnesses

      ```
      public Response.WitnessList.Builder clearWitnesses()
      ```

      `repeated .protocol.Witness witnesses = 1;`
    - #### removeWitnesses

      ```
      public Response.WitnessList.Builder removeWitnesses(int index)
      ```

      `repeated .protocol.Witness witnesses = 1;`
    - #### getWitnessesBuilder

      ```
      public Response.Witness.Builder getWitnessesBuilder(int index)
      ```

      `repeated .protocol.Witness witnesses = 1;`
    - #### getWitnessesOrBuilder

      ```
      public Response.WitnessOrBuilder getWitnessesOrBuilder(int index)
      ```

      `repeated .protocol.Witness witnesses = 1;`

      Specified by:
      :   `getWitnessesOrBuilder` in interface `Response.WitnessListOrBuilder`
    - #### getWitnessesOrBuilderList

      ```
      public java.util.List<? extends Response.WitnessOrBuilder> getWitnessesOrBuilderList()
      ```

      `repeated .protocol.Witness witnesses = 1;`

      Specified by:
      :   `getWitnessesOrBuilderList` in interface `Response.WitnessListOrBuilder`
    - #### addWitnessesBuilder

      ```
      public Response.Witness.Builder addWitnessesBuilder()
      ```

      `repeated .protocol.Witness witnesses = 1;`
    - #### addWitnessesBuilder

      ```
      public Response.Witness.Builder addWitnessesBuilder(int index)
      ```

      `repeated .protocol.Witness witnesses = 1;`
    - #### getWitnessesBuilderList

      ```
      public java.util.List<Response.Witness.Builder> getWitnessesBuilderList()
      ```

      `repeated .protocol.Witness witnesses = 1;`
    - #### setUnknownFields

      ```
      public final Response.WitnessList.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.WitnessList.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.WitnessList.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.WitnessList.Builder>`