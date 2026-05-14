

org.tron.trident.proto

## Class Response.DecryptNotesTRC20.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.DecryptNotesTRC20.Builder](../../../../org/tron/trident/proto/Response.DecryptNotesTRC20.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.DecryptNotesTRC20.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.DecryptNotesTRC20OrBuilder](../../../../org/tron/trident/proto/Response.DecryptNotesTRC20OrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.DecryptNotesTRC20](../../../../org/tron/trident/proto/Response.DecryptNotesTRC20.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.DecryptNotesTRC20.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.Builder>
  implements Response.DecryptNotesTRC20OrBuilder
  ```

  Protobuf type `protocol.DecryptNotesTRC20`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.DecryptNotesTRC20.Builder` | `addAllNoteTxs(java.lang.Iterable<? extends Response.DecryptNotesTRC20.NoteTx> values)` `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;` |
    | `Response.DecryptNotesTRC20.Builder` | `addNoteTxs(int index, Response.DecryptNotesTRC20.NoteTx.Builder builderForValue)` `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;` |
    | `Response.DecryptNotesTRC20.Builder` | `addNoteTxs(int index, Response.DecryptNotesTRC20.NoteTx value)` `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;` |
    | `Response.DecryptNotesTRC20.Builder` | `addNoteTxs(Response.DecryptNotesTRC20.NoteTx.Builder builderForValue)` `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;` |
    | `Response.DecryptNotesTRC20.Builder` | `addNoteTxs(Response.DecryptNotesTRC20.NoteTx value)` `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `addNoteTxsBuilder()` `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `addNoteTxsBuilder(int index)` `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;` |
    | `Response.DecryptNotesTRC20.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.DecryptNotesTRC20` | `build()` |
    | `Response.DecryptNotesTRC20` | `buildPartial()` |
    | `Response.DecryptNotesTRC20.Builder` | `clear()` |
    | `Response.DecryptNotesTRC20.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.DecryptNotesTRC20.Builder` | `clearNoteTxs()` `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;` |
    | `Response.DecryptNotesTRC20.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.DecryptNotesTRC20.Builder` | `clone()` |
    | `Response.DecryptNotesTRC20` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Response.DecryptNotesTRC20.NoteTx` | `getNoteTxs(int index)` `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;` |
    | `Response.DecryptNotesTRC20.NoteTx.Builder` | `getNoteTxsBuilder(int index)` `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;` |
    | `java.util.List<Response.DecryptNotesTRC20.NoteTx.Builder>` | `getNoteTxsBuilderList()` `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;` |
    | `int` | `getNoteTxsCount()` `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;` |
    | `java.util.List<Response.DecryptNotesTRC20.NoteTx>` | `getNoteTxsList()` `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;` |
    | `Response.DecryptNotesTRC20.NoteTxOrBuilder` | `getNoteTxsOrBuilder(int index)` `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;` |
    | `java.util.List<? extends Response.DecryptNotesTRC20.NoteTxOrBuilder>` | `getNoteTxsOrBuilderList()` `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.DecryptNotesTRC20.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.DecryptNotesTRC20.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.DecryptNotesTRC20.Builder` | `mergeFrom(Response.DecryptNotesTRC20 other)` |
    | `Response.DecryptNotesTRC20.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.DecryptNotesTRC20.Builder` | `removeNoteTxs(int index)` `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;` |
    | `Response.DecryptNotesTRC20.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.DecryptNotesTRC20.Builder` | `setNoteTxs(int index, Response.DecryptNotesTRC20.NoteTx.Builder builderForValue)` `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;` |
    | `Response.DecryptNotesTRC20.Builder` | `setNoteTxs(int index, Response.DecryptNotesTRC20.NoteTx value)` `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;` |
    | `Response.DecryptNotesTRC20.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.DecryptNotesTRC20.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.Builder>`
    - #### clear

      ```
      public Response.DecryptNotesTRC20.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.DecryptNotesTRC20 getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.DecryptNotesTRC20 build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.DecryptNotesTRC20 buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.DecryptNotesTRC20.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.Builder>`
    - #### setField

      ```
      public Response.DecryptNotesTRC20.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                         java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.Builder>`
    - #### clearField

      ```
      public Response.DecryptNotesTRC20.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.Builder>`
    - #### clearOneof

      ```
      public Response.DecryptNotesTRC20.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.Builder>`
    - #### setRepeatedField

      ```
      public Response.DecryptNotesTRC20.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                 int index,
                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.Builder>`
    - #### addRepeatedField

      ```
      public Response.DecryptNotesTRC20.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.Builder>`
    - #### mergeFrom

      ```
      public Response.DecryptNotesTRC20.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.DecryptNotesTRC20.Builder>`
    - #### mergeFrom

      ```
      public Response.DecryptNotesTRC20.Builder mergeFrom(Response.DecryptNotesTRC20 other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.Builder>`
    - #### mergeFrom

      ```
      public Response.DecryptNotesTRC20.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.DecryptNotesTRC20.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getNoteTxsList

      ```
      public java.util.List<Response.DecryptNotesTRC20.NoteTx> getNoteTxsList()
      ```

      `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;`

      Specified by:
      :   `getNoteTxsList` in interface `Response.DecryptNotesTRC20OrBuilder`
    - #### getNoteTxsCount

      ```
      public int getNoteTxsCount()
      ```

      `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;`

      Specified by:
      :   `getNoteTxsCount` in interface `Response.DecryptNotesTRC20OrBuilder`
    - #### getNoteTxs

      ```
      public Response.DecryptNotesTRC20.NoteTx getNoteTxs(int index)
      ```

      `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;`

      Specified by:
      :   `getNoteTxs` in interface `Response.DecryptNotesTRC20OrBuilder`
    - #### setNoteTxs

      ```
      public Response.DecryptNotesTRC20.Builder setNoteTxs(int index,
                                                           Response.DecryptNotesTRC20.NoteTx value)
      ```

      `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;`
    - #### setNoteTxs

      ```
      public Response.DecryptNotesTRC20.Builder setNoteTxs(int index,
                                                           Response.DecryptNotesTRC20.NoteTx.Builder builderForValue)
      ```

      `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;`
    - #### addNoteTxs

      ```
      public Response.DecryptNotesTRC20.Builder addNoteTxs(Response.DecryptNotesTRC20.NoteTx value)
      ```

      `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;`
    - #### addNoteTxs

      ```
      public Response.DecryptNotesTRC20.Builder addNoteTxs(int index,
                                                           Response.DecryptNotesTRC20.NoteTx value)
      ```

      `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;`
    - #### addNoteTxs

      ```
      public Response.DecryptNotesTRC20.Builder addNoteTxs(Response.DecryptNotesTRC20.NoteTx.Builder builderForValue)
      ```

      `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;`
    - #### addNoteTxs

      ```
      public Response.DecryptNotesTRC20.Builder addNoteTxs(int index,
                                                           Response.DecryptNotesTRC20.NoteTx.Builder builderForValue)
      ```

      `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;`
    - #### addAllNoteTxs

      ```
      public Response.DecryptNotesTRC20.Builder addAllNoteTxs(java.lang.Iterable<? extends Response.DecryptNotesTRC20.NoteTx> values)
      ```

      `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;`
    - #### clearNoteTxs

      ```
      public Response.DecryptNotesTRC20.Builder clearNoteTxs()
      ```

      `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;`
    - #### removeNoteTxs

      ```
      public Response.DecryptNotesTRC20.Builder removeNoteTxs(int index)
      ```

      `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;`
    - #### getNoteTxsBuilder

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder getNoteTxsBuilder(int index)
      ```

      `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;`
    - #### getNoteTxsOrBuilder

      ```
      public Response.DecryptNotesTRC20.NoteTxOrBuilder getNoteTxsOrBuilder(int index)
      ```

      `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;`

      Specified by:
      :   `getNoteTxsOrBuilder` in interface `Response.DecryptNotesTRC20OrBuilder`
    - #### getNoteTxsOrBuilderList

      ```
      public java.util.List<? extends Response.DecryptNotesTRC20.NoteTxOrBuilder> getNoteTxsOrBuilderList()
      ```

      `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;`

      Specified by:
      :   `getNoteTxsOrBuilderList` in interface `Response.DecryptNotesTRC20OrBuilder`
    - #### addNoteTxsBuilder

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder addNoteTxsBuilder()
      ```

      `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;`
    - #### addNoteTxsBuilder

      ```
      public Response.DecryptNotesTRC20.NoteTx.Builder addNoteTxsBuilder(int index)
      ```

      `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;`
    - #### getNoteTxsBuilderList

      ```
      public java.util.List<Response.DecryptNotesTRC20.NoteTx.Builder> getNoteTxsBuilderList()
      ```

      `repeated .protocol.DecryptNotesTRC20.NoteTx noteTxs = 1;`
    - #### setUnknownFields

      ```
      public final Response.DecryptNotesTRC20.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.DecryptNotesTRC20.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.DecryptNotesTRC20.Builder>`