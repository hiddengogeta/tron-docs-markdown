

org.tron.trident.proto

## Class Response.DelegatedResourceList

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite
  + - com.google.protobuf.AbstractMessage
    - * com.google.protobuf.GeneratedMessageV3
      * + org.tron.trident.proto.Response.DelegatedResourceList

* All Implemented Interfaces:
  :   com.google.protobuf.Message, com.google.protobuf.MessageLite, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.io.Serializable, [Response.DelegatedResourceListOrBuilder](../../../../org/tron/trident/proto/Response.DelegatedResourceListOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.DelegatedResourceList
  extends com.google.protobuf.GeneratedMessageV3
  implements Response.DelegatedResourceListOrBuilder
  ```

  Protobuf type `protocol.DelegatedResourceList`

  See Also:
  :   [Serialized Form](../../../../serialized-form.html#org.tron.trident.proto.Response.DelegatedResourceList)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class and Description |
    | `static class` | `Response.DelegatedResourceList.Builder` Protobuf type `protocol.DelegatedResourceList` |

    - ### Nested classes/interfaces inherited from class com.google.protobuf.GeneratedMessageV3

      `com.google.protobuf.GeneratedMessageV3.BuilderParent, com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>,BuilderT extends com.google.protobuf.GeneratedMessageV3.ExtendableBuilder<MessageT,BuilderT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.ExtendableMessageOrBuilder<MessageT extends com.google.protobuf.GeneratedMessageV3.ExtendableMessage<MessageT>>, com.google.protobuf.GeneratedMessageV3.FieldAccessorTable, com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter`
    - ### Nested classes/interfaces inherited from class com.google.protobuf.AbstractMessageLite

      `com.google.protobuf.AbstractMessageLite.InternalOneOfEnum`
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `DELEGATEDRESOURCE_FIELD_NUMBER` |

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
    | `static Response.DelegatedResourceList` | `getDefaultInstance()` |
    | `Response.DelegatedResourceList` | `getDefaultInstanceForType()` |
    | `Response.DelegatedResource` | `getDelegatedResource(int index)` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `int` | `getDelegatedResourceCount()` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `java.util.List<Response.DelegatedResource>` | `getDelegatedResourceList()` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `Response.DelegatedResourceOrBuilder` | `getDelegatedResourceOrBuilder(int index)` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `java.util.List<? extends Response.DelegatedResourceOrBuilder>` | `getDelegatedResourceOrBuilderList()` `repeated .protocol.DelegatedResource delegatedResource = 1;` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Parser<Response.DelegatedResourceList>` | `getParserForType()` |
    | `int` | `getSerializedSize()` |
    | `int` | `hashCode()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `static Response.DelegatedResourceList.Builder` | `newBuilder()` |
    | `static Response.DelegatedResourceList.Builder` | `newBuilder(Response.DelegatedResourceList prototype)` |
    | `Response.DelegatedResourceList.Builder` | `newBuilderForType()` |
    | `protected Response.DelegatedResourceList.Builder` | `newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)` |
    | `protected java.lang.Object` | `newInstance(com.google.protobuf.GeneratedMessageV3.UnusedPrivateParameter unused)` |
    | `static Response.DelegatedResourceList` | `parseDelimitedFrom(java.io.InputStream input)` |
    | `static Response.DelegatedResourceList` | `parseDelimitedFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.DelegatedResourceList` | `parseFrom(byte[] data)` |
    | `static Response.DelegatedResourceList` | `parseFrom(byte[] data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.DelegatedResourceList` | `parseFrom(java.nio.ByteBuffer data)` |
    | `static Response.DelegatedResourceList` | `parseFrom(java.nio.ByteBuffer data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.DelegatedResourceList` | `parseFrom(com.google.protobuf.ByteString data)` |
    | `static Response.DelegatedResourceList` | `parseFrom(com.google.protobuf.ByteString data, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.DelegatedResourceList` | `parseFrom(com.google.protobuf.CodedInputStream input)` |
    | `static Response.DelegatedResourceList` | `parseFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static Response.DelegatedResourceList` | `parseFrom(java.io.InputStream input)` |
    | `static Response.DelegatedResourceList` | `parseFrom(java.io.InputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `static com.google.protobuf.Parser<Response.DelegatedResourceList>` | `parser()` |
    | `Response.DelegatedResourceList.Builder` | `toBuilder()` |
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

    - #### DELEGATEDRESOURCE\_FIELD\_NUMBER

      ```
      public static final int DELEGATEDRESOURCE_FIELD_NUMBER
      ```

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.DelegatedResourceList.DELEGATEDRESOURCE_FIELD_NUMBER)
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
    - #### getDelegatedResourceList

      ```
      public java.util.List<Response.DelegatedResource> getDelegatedResourceList()
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`

      Specified by:
      :   `getDelegatedResourceList` in interface `Response.DelegatedResourceListOrBuilder`
    - #### getDelegatedResourceOrBuilderList

      ```
      public java.util.List<? extends Response.DelegatedResourceOrBuilder> getDelegatedResourceOrBuilderList()
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`

      Specified by:
      :   `getDelegatedResourceOrBuilderList` in interface `Response.DelegatedResourceListOrBuilder`
    - #### getDelegatedResourceCount

      ```
      public int getDelegatedResourceCount()
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`

      Specified by:
      :   `getDelegatedResourceCount` in interface `Response.DelegatedResourceListOrBuilder`
    - #### getDelegatedResource

      ```
      public Response.DelegatedResource getDelegatedResource(int index)
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`

      Specified by:
      :   `getDelegatedResource` in interface `Response.DelegatedResourceListOrBuilder`
    - #### getDelegatedResourceOrBuilder

      ```
      public Response.DelegatedResourceOrBuilder getDelegatedResourceOrBuilder(int index)
      ```

      `repeated .protocol.DelegatedResource delegatedResource = 1;`

      Specified by:
      :   `getDelegatedResourceOrBuilder` in interface `Response.DelegatedResourceListOrBuilder`
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
      public static Response.DelegatedResourceList parseFrom(java.nio.ByteBuffer data)
                                                      throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DelegatedResourceList parseFrom(java.nio.ByteBuffer data,
                                                             com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                      throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DelegatedResourceList parseFrom(com.google.protobuf.ByteString data)
                                                      throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DelegatedResourceList parseFrom(com.google.protobuf.ByteString data,
                                                             com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                      throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DelegatedResourceList parseFrom(byte[] data)
                                                      throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DelegatedResourceList parseFrom(byte[] data,
                                                             com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                      throws com.google.protobuf.InvalidProtocolBufferException
      ```

      Throws:
      :   `com.google.protobuf.InvalidProtocolBufferException`
    - #### parseFrom

      ```
      public static Response.DelegatedResourceList parseFrom(java.io.InputStream input)
                                                      throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.DelegatedResourceList parseFrom(java.io.InputStream input,
                                                             com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                      throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.DelegatedResourceList parseDelimitedFrom(java.io.InputStream input)
                                                               throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseDelimitedFrom

      ```
      public static Response.DelegatedResourceList parseDelimitedFrom(java.io.InputStream input,
                                                                      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                               throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.DelegatedResourceList parseFrom(com.google.protobuf.CodedInputStream input)
                                                      throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### parseFrom

      ```
      public static Response.DelegatedResourceList parseFrom(com.google.protobuf.CodedInputStream input,
                                                             com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                      throws java.io.IOException
      ```

      Throws:
      :   `java.io.IOException`
    - #### newBuilderForType

      ```
      public Response.DelegatedResourceList.Builder newBuilderForType()
      ```

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `newBuilderForType` in interface `com.google.protobuf.MessageLite`
    - #### newBuilder

      ```
      public static Response.DelegatedResourceList.Builder newBuilder()
      ```
    - #### newBuilder

      ```
      public static Response.DelegatedResourceList.Builder newBuilder(Response.DelegatedResourceList prototype)
      ```
    - #### toBuilder

      ```
      public Response.DelegatedResourceList.Builder toBuilder()
      ```

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.Message`

      Specified by:
      :   `toBuilder` in interface `com.google.protobuf.MessageLite`
    - #### newBuilderForType

      ```
      protected Response.DelegatedResourceList.Builder newBuilderForType(com.google.protobuf.GeneratedMessageV3.BuilderParent parent)
      ```

      Specified by:
      :   `newBuilderForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstance

      ```
      public static Response.DelegatedResourceList getDefaultInstance()
      ```
    - #### parser

      ```
      public static com.google.protobuf.Parser<Response.DelegatedResourceList> parser()
      ```
    - #### getParserForType

      ```
      public com.google.protobuf.Parser<Response.DelegatedResourceList> getParserForType()
      ```

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.Message`

      Specified by:
      :   `getParserForType` in interface `com.google.protobuf.MessageLite`

      Overrides:
      :   `getParserForType` in class `com.google.protobuf.GeneratedMessageV3`
    - #### getDefaultInstanceForType

      ```
      public Response.DelegatedResourceList getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`