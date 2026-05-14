

org.tron.trident.proto

## Class Response.ProposalList.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.ProposalList.Builder](../../../../org/tron/trident/proto/Response.ProposalList.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.ProposalList.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.ProposalListOrBuilder](../../../../org/tron/trident/proto/Response.ProposalListOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.ProposalList](../../../../org/tron/trident/proto/Response.ProposalList.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.ProposalList.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.ProposalList.Builder>
  implements Response.ProposalListOrBuilder
  ```

  Protobuf type `protocol.ProposalList`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.ProposalList.Builder` | `addAllProposals(java.lang.Iterable<? extends Response.Proposal> values)` `repeated .protocol.Proposal proposals = 1;` |
    | `Response.ProposalList.Builder` | `addProposals(int index, Response.Proposal.Builder builderForValue)` `repeated .protocol.Proposal proposals = 1;` |
    | `Response.ProposalList.Builder` | `addProposals(int index, Response.Proposal value)` `repeated .protocol.Proposal proposals = 1;` |
    | `Response.ProposalList.Builder` | `addProposals(Response.Proposal.Builder builderForValue)` `repeated .protocol.Proposal proposals = 1;` |
    | `Response.ProposalList.Builder` | `addProposals(Response.Proposal value)` `repeated .protocol.Proposal proposals = 1;` |
    | `Response.Proposal.Builder` | `addProposalsBuilder()` `repeated .protocol.Proposal proposals = 1;` |
    | `Response.Proposal.Builder` | `addProposalsBuilder(int index)` `repeated .protocol.Proposal proposals = 1;` |
    | `Response.ProposalList.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.ProposalList` | `build()` |
    | `Response.ProposalList` | `buildPartial()` |
    | `Response.ProposalList.Builder` | `clear()` |
    | `Response.ProposalList.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.ProposalList.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.ProposalList.Builder` | `clearProposals()` `repeated .protocol.Proposal proposals = 1;` |
    | `Response.ProposalList.Builder` | `clone()` |
    | `Response.ProposalList` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Response.Proposal` | `getProposals(int index)` `repeated .protocol.Proposal proposals = 1;` |
    | `Response.Proposal.Builder` | `getProposalsBuilder(int index)` `repeated .protocol.Proposal proposals = 1;` |
    | `java.util.List<Response.Proposal.Builder>` | `getProposalsBuilderList()` `repeated .protocol.Proposal proposals = 1;` |
    | `int` | `getProposalsCount()` `repeated .protocol.Proposal proposals = 1;` |
    | `java.util.List<Response.Proposal>` | `getProposalsList()` `repeated .protocol.Proposal proposals = 1;` |
    | `Response.ProposalOrBuilder` | `getProposalsOrBuilder(int index)` `repeated .protocol.Proposal proposals = 1;` |
    | `java.util.List<? extends Response.ProposalOrBuilder>` | `getProposalsOrBuilderList()` `repeated .protocol.Proposal proposals = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.ProposalList.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.ProposalList.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.ProposalList.Builder` | `mergeFrom(Response.ProposalList other)` |
    | `Response.ProposalList.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.ProposalList.Builder` | `removeProposals(int index)` `repeated .protocol.Proposal proposals = 1;` |
    | `Response.ProposalList.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.ProposalList.Builder` | `setProposals(int index, Response.Proposal.Builder builderForValue)` `repeated .protocol.Proposal proposals = 1;` |
    | `Response.ProposalList.Builder` | `setProposals(int index, Response.Proposal value)` `repeated .protocol.Proposal proposals = 1;` |
    | `Response.ProposalList.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.ProposalList.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ProposalList.Builder>`
    - #### clear

      ```
      public Response.ProposalList.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ProposalList.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ProposalList.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.ProposalList getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.ProposalList build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.ProposalList buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.ProposalList.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ProposalList.Builder>`
    - #### setField

      ```
      public Response.ProposalList.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                    java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ProposalList.Builder>`
    - #### clearField

      ```
      public Response.ProposalList.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ProposalList.Builder>`
    - #### clearOneof

      ```
      public Response.ProposalList.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ProposalList.Builder>`
    - #### setRepeatedField

      ```
      public Response.ProposalList.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                            int index,
                                                            java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ProposalList.Builder>`
    - #### addRepeatedField

      ```
      public Response.ProposalList.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                            java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ProposalList.Builder>`
    - #### mergeFrom

      ```
      public Response.ProposalList.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.ProposalList.Builder>`
    - #### mergeFrom

      ```
      public Response.ProposalList.Builder mergeFrom(Response.ProposalList other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ProposalList.Builder>`
    - #### mergeFrom

      ```
      public Response.ProposalList.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                     com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                              throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.ProposalList.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getProposalsList

      ```
      public java.util.List<Response.Proposal> getProposalsList()
      ```

      `repeated .protocol.Proposal proposals = 1;`

      Specified by:
      :   `getProposalsList` in interface `Response.ProposalListOrBuilder`
    - #### getProposalsCount

      ```
      public int getProposalsCount()
      ```

      `repeated .protocol.Proposal proposals = 1;`

      Specified by:
      :   `getProposalsCount` in interface `Response.ProposalListOrBuilder`
    - #### getProposals

      ```
      public Response.Proposal getProposals(int index)
      ```

      `repeated .protocol.Proposal proposals = 1;`

      Specified by:
      :   `getProposals` in interface `Response.ProposalListOrBuilder`
    - #### setProposals

      ```
      public Response.ProposalList.Builder setProposals(int index,
                                                        Response.Proposal value)
      ```

      `repeated .protocol.Proposal proposals = 1;`
    - #### setProposals

      ```
      public Response.ProposalList.Builder setProposals(int index,
                                                        Response.Proposal.Builder builderForValue)
      ```

      `repeated .protocol.Proposal proposals = 1;`
    - #### addProposals

      ```
      public Response.ProposalList.Builder addProposals(Response.Proposal value)
      ```

      `repeated .protocol.Proposal proposals = 1;`
    - #### addProposals

      ```
      public Response.ProposalList.Builder addProposals(int index,
                                                        Response.Proposal value)
      ```

      `repeated .protocol.Proposal proposals = 1;`
    - #### addProposals

      ```
      public Response.ProposalList.Builder addProposals(Response.Proposal.Builder builderForValue)
      ```

      `repeated .protocol.Proposal proposals = 1;`
    - #### addProposals

      ```
      public Response.ProposalList.Builder addProposals(int index,
                                                        Response.Proposal.Builder builderForValue)
      ```

      `repeated .protocol.Proposal proposals = 1;`
    - #### addAllProposals

      ```
      public Response.ProposalList.Builder addAllProposals(java.lang.Iterable<? extends Response.Proposal> values)
      ```

      `repeated .protocol.Proposal proposals = 1;`
    - #### clearProposals

      ```
      public Response.ProposalList.Builder clearProposals()
      ```

      `repeated .protocol.Proposal proposals = 1;`
    - #### removeProposals

      ```
      public Response.ProposalList.Builder removeProposals(int index)
      ```

      `repeated .protocol.Proposal proposals = 1;`
    - #### getProposalsBuilder

      ```
      public Response.Proposal.Builder getProposalsBuilder(int index)
      ```

      `repeated .protocol.Proposal proposals = 1;`
    - #### getProposalsOrBuilder

      ```
      public Response.ProposalOrBuilder getProposalsOrBuilder(int index)
      ```

      `repeated .protocol.Proposal proposals = 1;`

      Specified by:
      :   `getProposalsOrBuilder` in interface `Response.ProposalListOrBuilder`
    - #### getProposalsOrBuilderList

      ```
      public java.util.List<? extends Response.ProposalOrBuilder> getProposalsOrBuilderList()
      ```

      `repeated .protocol.Proposal proposals = 1;`

      Specified by:
      :   `getProposalsOrBuilderList` in interface `Response.ProposalListOrBuilder`
    - #### addProposalsBuilder

      ```
      public Response.Proposal.Builder addProposalsBuilder()
      ```

      `repeated .protocol.Proposal proposals = 1;`
    - #### addProposalsBuilder

      ```
      public Response.Proposal.Builder addProposalsBuilder(int index)
      ```

      `repeated .protocol.Proposal proposals = 1;`
    - #### getProposalsBuilderList

      ```
      public java.util.List<Response.Proposal.Builder> getProposalsBuilderList()
      ```

      `repeated .protocol.Proposal proposals = 1;`
    - #### setUnknownFields

      ```
      public final Response.ProposalList.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ProposalList.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.ProposalList.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.ProposalList.Builder>`