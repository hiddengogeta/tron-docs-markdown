

org.tron.trident.proto

## Class Response.AssetIssueList.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.AssetIssueList.Builder](../../../../org/tron/trident/proto/Response.AssetIssueList.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.AssetIssueList.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.AssetIssueListOrBuilder](../../../../org/tron/trident/proto/Response.AssetIssueListOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.AssetIssueList](../../../../org/tron/trident/proto/Response.AssetIssueList.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.AssetIssueList.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.AssetIssueList.Builder>
  implements Response.AssetIssueListOrBuilder
  ```

  Protobuf type `protocol.AssetIssueList`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.AssetIssueList.Builder` | `addAllAssets(java.lang.Iterable<? extends Contract.AssetIssueContract> values)` `repeated .protocol.AssetIssueContract assets = 1;` |
    | `Response.AssetIssueList.Builder` | `addAssets(Contract.AssetIssueContract.Builder builderForValue)` `repeated .protocol.AssetIssueContract assets = 1;` |
    | `Response.AssetIssueList.Builder` | `addAssets(Contract.AssetIssueContract value)` `repeated .protocol.AssetIssueContract assets = 1;` |
    | `Response.AssetIssueList.Builder` | `addAssets(int index, Contract.AssetIssueContract.Builder builderForValue)` `repeated .protocol.AssetIssueContract assets = 1;` |
    | `Response.AssetIssueList.Builder` | `addAssets(int index, Contract.AssetIssueContract value)` `repeated .protocol.AssetIssueContract assets = 1;` |
    | `Contract.AssetIssueContract.Builder` | `addAssetsBuilder()` `repeated .protocol.AssetIssueContract assets = 1;` |
    | `Contract.AssetIssueContract.Builder` | `addAssetsBuilder(int index)` `repeated .protocol.AssetIssueContract assets = 1;` |
    | `Response.AssetIssueList.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.AssetIssueList` | `build()` |
    | `Response.AssetIssueList` | `buildPartial()` |
    | `Response.AssetIssueList.Builder` | `clear()` |
    | `Response.AssetIssueList.Builder` | `clearAssets()` `repeated .protocol.AssetIssueContract assets = 1;` |
    | `Response.AssetIssueList.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.AssetIssueList.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.AssetIssueList.Builder` | `clone()` |
    | `Contract.AssetIssueContract` | `getAssets(int index)` `repeated .protocol.AssetIssueContract assets = 1;` |
    | `Contract.AssetIssueContract.Builder` | `getAssetsBuilder(int index)` `repeated .protocol.AssetIssueContract assets = 1;` |
    | `java.util.List<Contract.AssetIssueContract.Builder>` | `getAssetsBuilderList()` `repeated .protocol.AssetIssueContract assets = 1;` |
    | `int` | `getAssetsCount()` `repeated .protocol.AssetIssueContract assets = 1;` |
    | `java.util.List<Contract.AssetIssueContract>` | `getAssetsList()` `repeated .protocol.AssetIssueContract assets = 1;` |
    | `Contract.AssetIssueContractOrBuilder` | `getAssetsOrBuilder(int index)` `repeated .protocol.AssetIssueContract assets = 1;` |
    | `java.util.List<? extends Contract.AssetIssueContractOrBuilder>` | `getAssetsOrBuilderList()` `repeated .protocol.AssetIssueContract assets = 1;` |
    | `Response.AssetIssueList` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.AssetIssueList.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.AssetIssueList.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.AssetIssueList.Builder` | `mergeFrom(Response.AssetIssueList other)` |
    | `Response.AssetIssueList.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.AssetIssueList.Builder` | `removeAssets(int index)` `repeated .protocol.AssetIssueContract assets = 1;` |
    | `Response.AssetIssueList.Builder` | `setAssets(int index, Contract.AssetIssueContract.Builder builderForValue)` `repeated .protocol.AssetIssueContract assets = 1;` |
    | `Response.AssetIssueList.Builder` | `setAssets(int index, Contract.AssetIssueContract value)` `repeated .protocol.AssetIssueContract assets = 1;` |
    | `Response.AssetIssueList.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.AssetIssueList.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.AssetIssueList.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AssetIssueList.Builder>`
    - #### clear

      ```
      public Response.AssetIssueList.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AssetIssueList.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AssetIssueList.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.AssetIssueList getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.AssetIssueList build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.AssetIssueList buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.AssetIssueList.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AssetIssueList.Builder>`
    - #### setField

      ```
      public Response.AssetIssueList.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                      java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AssetIssueList.Builder>`
    - #### clearField

      ```
      public Response.AssetIssueList.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AssetIssueList.Builder>`
    - #### clearOneof

      ```
      public Response.AssetIssueList.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AssetIssueList.Builder>`
    - #### setRepeatedField

      ```
      public Response.AssetIssueList.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                              int index,
                                                              java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AssetIssueList.Builder>`
    - #### addRepeatedField

      ```
      public Response.AssetIssueList.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                              java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AssetIssueList.Builder>`
    - #### mergeFrom

      ```
      public Response.AssetIssueList.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.AssetIssueList.Builder>`
    - #### mergeFrom

      ```
      public Response.AssetIssueList.Builder mergeFrom(Response.AssetIssueList other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AssetIssueList.Builder>`
    - #### mergeFrom

      ```
      public Response.AssetIssueList.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                       com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.AssetIssueList.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getAssetsList

      ```
      public java.util.List<Contract.AssetIssueContract> getAssetsList()
      ```

      `repeated .protocol.AssetIssueContract assets = 1;`

      Specified by:
      :   `getAssetsList` in interface `Response.AssetIssueListOrBuilder`
    - #### getAssetsCount

      ```
      public int getAssetsCount()
      ```

      `repeated .protocol.AssetIssueContract assets = 1;`

      Specified by:
      :   `getAssetsCount` in interface `Response.AssetIssueListOrBuilder`
    - #### getAssets

      ```
      public Contract.AssetIssueContract getAssets(int index)
      ```

      `repeated .protocol.AssetIssueContract assets = 1;`

      Specified by:
      :   `getAssets` in interface `Response.AssetIssueListOrBuilder`
    - #### setAssets

      ```
      public Response.AssetIssueList.Builder setAssets(int index,
                                                       Contract.AssetIssueContract value)
      ```

      `repeated .protocol.AssetIssueContract assets = 1;`
    - #### setAssets

      ```
      public Response.AssetIssueList.Builder setAssets(int index,
                                                       Contract.AssetIssueContract.Builder builderForValue)
      ```

      `repeated .protocol.AssetIssueContract assets = 1;`
    - #### addAssets

      ```
      public Response.AssetIssueList.Builder addAssets(Contract.AssetIssueContract value)
      ```

      `repeated .protocol.AssetIssueContract assets = 1;`
    - #### addAssets

      ```
      public Response.AssetIssueList.Builder addAssets(int index,
                                                       Contract.AssetIssueContract value)
      ```

      `repeated .protocol.AssetIssueContract assets = 1;`
    - #### addAssets

      ```
      public Response.AssetIssueList.Builder addAssets(Contract.AssetIssueContract.Builder builderForValue)
      ```

      `repeated .protocol.AssetIssueContract assets = 1;`
    - #### addAssets

      ```
      public Response.AssetIssueList.Builder addAssets(int index,
                                                       Contract.AssetIssueContract.Builder builderForValue)
      ```

      `repeated .protocol.AssetIssueContract assets = 1;`
    - #### addAllAssets

      ```
      public Response.AssetIssueList.Builder addAllAssets(java.lang.Iterable<? extends Contract.AssetIssueContract> values)
      ```

      `repeated .protocol.AssetIssueContract assets = 1;`
    - #### clearAssets

      ```
      public Response.AssetIssueList.Builder clearAssets()
      ```

      `repeated .protocol.AssetIssueContract assets = 1;`
    - #### removeAssets

      ```
      public Response.AssetIssueList.Builder removeAssets(int index)
      ```

      `repeated .protocol.AssetIssueContract assets = 1;`
    - #### getAssetsBuilder

      ```
      public Contract.AssetIssueContract.Builder getAssetsBuilder(int index)
      ```

      `repeated .protocol.AssetIssueContract assets = 1;`
    - #### getAssetsOrBuilder

      ```
      public Contract.AssetIssueContractOrBuilder getAssetsOrBuilder(int index)
      ```

      `repeated .protocol.AssetIssueContract assets = 1;`

      Specified by:
      :   `getAssetsOrBuilder` in interface `Response.AssetIssueListOrBuilder`
    - #### getAssetsOrBuilderList

      ```
      public java.util.List<? extends Contract.AssetIssueContractOrBuilder> getAssetsOrBuilderList()
      ```

      `repeated .protocol.AssetIssueContract assets = 1;`

      Specified by:
      :   `getAssetsOrBuilderList` in interface `Response.AssetIssueListOrBuilder`
    - #### addAssetsBuilder

      ```
      public Contract.AssetIssueContract.Builder addAssetsBuilder()
      ```

      `repeated .protocol.AssetIssueContract assets = 1;`
    - #### addAssetsBuilder

      ```
      public Contract.AssetIssueContract.Builder addAssetsBuilder(int index)
      ```

      `repeated .protocol.AssetIssueContract assets = 1;`
    - #### getAssetsBuilderList

      ```
      public java.util.List<Contract.AssetIssueContract.Builder> getAssetsBuilderList()
      ```

      `repeated .protocol.AssetIssueContract assets = 1;`
    - #### setUnknownFields

      ```
      public final Response.AssetIssueList.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AssetIssueList.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.AssetIssueList.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.AssetIssueList.Builder>`