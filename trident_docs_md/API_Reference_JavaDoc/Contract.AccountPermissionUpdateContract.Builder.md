

org.tron.trident.proto

## Class Contract.AccountPermissionUpdateContract.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Contract.AccountPermissionUpdateContract.Builder](../../../../org/tron/trident/proto/Contract.AccountPermissionUpdateContract.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Contract.AccountPermissionUpdateContract.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Contract.AccountPermissionUpdateContractOrBuilder](../../../../org/tron/trident/proto/Contract.AccountPermissionUpdateContractOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Contract.AccountPermissionUpdateContract](../../../../org/tron/trident/proto/Contract.AccountPermissionUpdateContract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Contract.AccountPermissionUpdateContract.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountPermissionUpdateContract.Builder>
  implements Contract.AccountPermissionUpdateContractOrBuilder
  ```

  Protobuf type `protocol.AccountPermissionUpdateContract`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Contract.AccountPermissionUpdateContract.Builder` | `addActives(Common.Permission.Builder builderForValue)` Empty is invalidate |
    | `Contract.AccountPermissionUpdateContract.Builder` | `addActives(Common.Permission value)` Empty is invalidate |
    | `Contract.AccountPermissionUpdateContract.Builder` | `addActives(int index, Common.Permission.Builder builderForValue)` Empty is invalidate |
    | `Contract.AccountPermissionUpdateContract.Builder` | `addActives(int index, Common.Permission value)` Empty is invalidate |
    | `Common.Permission.Builder` | `addActivesBuilder()` Empty is invalidate |
    | `Common.Permission.Builder` | `addActivesBuilder(int index)` Empty is invalidate |
    | `Contract.AccountPermissionUpdateContract.Builder` | `addAllActives(java.lang.Iterable<? extends Common.Permission> values)` Empty is invalidate |
    | `Contract.AccountPermissionUpdateContract.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.AccountPermissionUpdateContract` | `build()` |
    | `Contract.AccountPermissionUpdateContract` | `buildPartial()` |
    | `Contract.AccountPermissionUpdateContract.Builder` | `clear()` |
    | `Contract.AccountPermissionUpdateContract.Builder` | `clearActives()` Empty is invalidate |
    | `Contract.AccountPermissionUpdateContract.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Contract.AccountPermissionUpdateContract.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Contract.AccountPermissionUpdateContract.Builder` | `clearOwner()` Empty is invalidate |
    | `Contract.AccountPermissionUpdateContract.Builder` | `clearOwnerAddress()` `bytes owner_address = 1;` |
    | `Contract.AccountPermissionUpdateContract.Builder` | `clearWitness()` Can be empty |
    | `Contract.AccountPermissionUpdateContract.Builder` | `clone()` |
    | `Common.Permission` | `getActives(int index)` Empty is invalidate |
    | `Common.Permission.Builder` | `getActivesBuilder(int index)` Empty is invalidate |
    | `java.util.List<Common.Permission.Builder>` | `getActivesBuilderList()` Empty is invalidate |
    | `int` | `getActivesCount()` Empty is invalidate |
    | `java.util.List<Common.Permission>` | `getActivesList()` Empty is invalidate |
    | `Common.PermissionOrBuilder` | `getActivesOrBuilder(int index)` Empty is invalidate |
    | `java.util.List<? extends Common.PermissionOrBuilder>` | `getActivesOrBuilderList()` Empty is invalidate |
    | `Contract.AccountPermissionUpdateContract` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Common.Permission` | `getOwner()` Empty is invalidate |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `Common.Permission.Builder` | `getOwnerBuilder()` Empty is invalidate |
    | `Common.PermissionOrBuilder` | `getOwnerOrBuilder()` Empty is invalidate |
    | `Common.Permission` | `getWitness()` Can be empty |
    | `Common.Permission.Builder` | `getWitnessBuilder()` Can be empty |
    | `Common.PermissionOrBuilder` | `getWitnessOrBuilder()` Can be empty |
    | `boolean` | `hasOwner()` Empty is invalidate |
    | `boolean` | `hasWitness()` Can be empty |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Contract.AccountPermissionUpdateContract.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Contract.AccountPermissionUpdateContract.Builder` | `mergeFrom(Contract.AccountPermissionUpdateContract other)` |
    | `Contract.AccountPermissionUpdateContract.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Contract.AccountPermissionUpdateContract.Builder` | `mergeOwner(Common.Permission value)` Empty is invalidate |
    | `Contract.AccountPermissionUpdateContract.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.AccountPermissionUpdateContract.Builder` | `mergeWitness(Common.Permission value)` Can be empty |
    | `Contract.AccountPermissionUpdateContract.Builder` | `removeActives(int index)` Empty is invalidate |
    | `Contract.AccountPermissionUpdateContract.Builder` | `setActives(int index, Common.Permission.Builder builderForValue)` Empty is invalidate |
    | `Contract.AccountPermissionUpdateContract.Builder` | `setActives(int index, Common.Permission value)` Empty is invalidate |
    | `Contract.AccountPermissionUpdateContract.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Contract.AccountPermissionUpdateContract.Builder` | `setOwner(Common.Permission.Builder builderForValue)` Empty is invalidate |
    | `Contract.AccountPermissionUpdateContract.Builder` | `setOwner(Common.Permission value)` Empty is invalidate |
    | `Contract.AccountPermissionUpdateContract.Builder` | `setOwnerAddress(com.google.protobuf.ByteString value)` `bytes owner_address = 1;` |
    | `Contract.AccountPermissionUpdateContract.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Contract.AccountPermissionUpdateContract.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Contract.AccountPermissionUpdateContract.Builder` | `setWitness(Common.Permission.Builder builderForValue)` Can be empty |
    | `Contract.AccountPermissionUpdateContract.Builder` | `setWitness(Common.Permission value)` Can be empty |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountPermissionUpdateContract.Builder>`
    - #### clear

      ```
      public Contract.AccountPermissionUpdateContract.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountPermissionUpdateContract.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountPermissionUpdateContract.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Contract.AccountPermissionUpdateContract getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Contract.AccountPermissionUpdateContract build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Contract.AccountPermissionUpdateContract buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Contract.AccountPermissionUpdateContract.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountPermissionUpdateContract.Builder>`
    - #### setField

      ```
      public Contract.AccountPermissionUpdateContract.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountPermissionUpdateContract.Builder>`
    - #### clearField

      ```
      public Contract.AccountPermissionUpdateContract.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountPermissionUpdateContract.Builder>`
    - #### clearOneof

      ```
      public Contract.AccountPermissionUpdateContract.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountPermissionUpdateContract.Builder>`
    - #### setRepeatedField

      ```
      public Contract.AccountPermissionUpdateContract.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                               int index,
                                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountPermissionUpdateContract.Builder>`
    - #### addRepeatedField

      ```
      public Contract.AccountPermissionUpdateContract.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                               java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountPermissionUpdateContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.AccountPermissionUpdateContract.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.AccountPermissionUpdateContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.AccountPermissionUpdateContract.Builder mergeFrom(Contract.AccountPermissionUpdateContract other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountPermissionUpdateContract.Builder>`
    - #### mergeFrom

      ```
      public Contract.AccountPermissionUpdateContract.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                 throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Contract.AccountPermissionUpdateContract.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getOwnerAddress

      ```
      public com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Specified by:
      :   `getOwnerAddress` in interface `Contract.AccountPermissionUpdateContractOrBuilder`

      Returns:
      :   The ownerAddress.
    - #### setOwnerAddress

      ```
      public Contract.AccountPermissionUpdateContract.Builder setOwnerAddress(com.google.protobuf.ByteString value)
      ```

      `bytes owner_address = 1;`

      Parameters:
      :   `value` - The ownerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearOwnerAddress

      ```
      public Contract.AccountPermissionUpdateContract.Builder clearOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   This builder for chaining.
    - #### hasOwner

      ```
      public boolean hasOwner()
      ```

      ```
       Empty is invalidate
      ```

      `.protocol.Permission owner = 2;`

      Specified by:
      :   `hasOwner` in interface `Contract.AccountPermissionUpdateContractOrBuilder`

      Returns:
      :   Whether the owner field is set.
    - #### getOwner

      ```
      public Common.Permission getOwner()
      ```

      ```
       Empty is invalidate
      ```

      `.protocol.Permission owner = 2;`

      Specified by:
      :   `getOwner` in interface `Contract.AccountPermissionUpdateContractOrBuilder`

      Returns:
      :   The owner.
    - #### setOwner

      ```
      public Contract.AccountPermissionUpdateContract.Builder setOwner(Common.Permission value)
      ```

      ```
       Empty is invalidate
      ```

      `.protocol.Permission owner = 2;`
    - #### setOwner

      ```
      public Contract.AccountPermissionUpdateContract.Builder setOwner(Common.Permission.Builder builderForValue)
      ```

      ```
       Empty is invalidate
      ```

      `.protocol.Permission owner = 2;`
    - #### mergeOwner

      ```
      public Contract.AccountPermissionUpdateContract.Builder mergeOwner(Common.Permission value)
      ```

      ```
       Empty is invalidate
      ```

      `.protocol.Permission owner = 2;`
    - #### clearOwner

      ```
      public Contract.AccountPermissionUpdateContract.Builder clearOwner()
      ```

      ```
       Empty is invalidate
      ```

      `.protocol.Permission owner = 2;`
    - #### getOwnerBuilder

      ```
      public Common.Permission.Builder getOwnerBuilder()
      ```

      ```
       Empty is invalidate
      ```

      `.protocol.Permission owner = 2;`
    - #### getOwnerOrBuilder

      ```
      public Common.PermissionOrBuilder getOwnerOrBuilder()
      ```

      ```
       Empty is invalidate
      ```

      `.protocol.Permission owner = 2;`

      Specified by:
      :   `getOwnerOrBuilder` in interface `Contract.AccountPermissionUpdateContractOrBuilder`
    - #### hasWitness

      ```
      public boolean hasWitness()
      ```

      ```
       Can be empty
      ```

      `.protocol.Permission witness = 3;`

      Specified by:
      :   `hasWitness` in interface `Contract.AccountPermissionUpdateContractOrBuilder`

      Returns:
      :   Whether the witness field is set.
    - #### getWitness

      ```
      public Common.Permission getWitness()
      ```

      ```
       Can be empty
      ```

      `.protocol.Permission witness = 3;`

      Specified by:
      :   `getWitness` in interface `Contract.AccountPermissionUpdateContractOrBuilder`

      Returns:
      :   The witness.
    - #### setWitness

      ```
      public Contract.AccountPermissionUpdateContract.Builder setWitness(Common.Permission value)
      ```

      ```
       Can be empty
      ```

      `.protocol.Permission witness = 3;`
    - #### setWitness

      ```
      public Contract.AccountPermissionUpdateContract.Builder setWitness(Common.Permission.Builder builderForValue)
      ```

      ```
       Can be empty
      ```

      `.protocol.Permission witness = 3;`
    - #### mergeWitness

      ```
      public Contract.AccountPermissionUpdateContract.Builder mergeWitness(Common.Permission value)
      ```

      ```
       Can be empty
      ```

      `.protocol.Permission witness = 3;`
    - #### clearWitness

      ```
      public Contract.AccountPermissionUpdateContract.Builder clearWitness()
      ```

      ```
       Can be empty
      ```

      `.protocol.Permission witness = 3;`
    - #### getWitnessBuilder

      ```
      public Common.Permission.Builder getWitnessBuilder()
      ```

      ```
       Can be empty
      ```

      `.protocol.Permission witness = 3;`
    - #### getWitnessOrBuilder

      ```
      public Common.PermissionOrBuilder getWitnessOrBuilder()
      ```

      ```
       Can be empty
      ```

      `.protocol.Permission witness = 3;`

      Specified by:
      :   `getWitnessOrBuilder` in interface `Contract.AccountPermissionUpdateContractOrBuilder`
    - #### getActivesList

      ```
      public java.util.List<Common.Permission> getActivesList()
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`

      Specified by:
      :   `getActivesList` in interface `Contract.AccountPermissionUpdateContractOrBuilder`
    - #### getActivesCount

      ```
      public int getActivesCount()
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`

      Specified by:
      :   `getActivesCount` in interface `Contract.AccountPermissionUpdateContractOrBuilder`
    - #### getActives

      ```
      public Common.Permission getActives(int index)
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`

      Specified by:
      :   `getActives` in interface `Contract.AccountPermissionUpdateContractOrBuilder`
    - #### setActives

      ```
      public Contract.AccountPermissionUpdateContract.Builder setActives(int index,
                                                                         Common.Permission value)
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`
    - #### setActives

      ```
      public Contract.AccountPermissionUpdateContract.Builder setActives(int index,
                                                                         Common.Permission.Builder builderForValue)
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`
    - #### addActives

      ```
      public Contract.AccountPermissionUpdateContract.Builder addActives(Common.Permission value)
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`
    - #### addActives

      ```
      public Contract.AccountPermissionUpdateContract.Builder addActives(int index,
                                                                         Common.Permission value)
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`
    - #### addActives

      ```
      public Contract.AccountPermissionUpdateContract.Builder addActives(Common.Permission.Builder builderForValue)
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`
    - #### addActives

      ```
      public Contract.AccountPermissionUpdateContract.Builder addActives(int index,
                                                                         Common.Permission.Builder builderForValue)
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`
    - #### addAllActives

      ```
      public Contract.AccountPermissionUpdateContract.Builder addAllActives(java.lang.Iterable<? extends Common.Permission> values)
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`
    - #### clearActives

      ```
      public Contract.AccountPermissionUpdateContract.Builder clearActives()
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`
    - #### removeActives

      ```
      public Contract.AccountPermissionUpdateContract.Builder removeActives(int index)
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`
    - #### getActivesBuilder

      ```
      public Common.Permission.Builder getActivesBuilder(int index)
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`
    - #### getActivesOrBuilder

      ```
      public Common.PermissionOrBuilder getActivesOrBuilder(int index)
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`

      Specified by:
      :   `getActivesOrBuilder` in interface `Contract.AccountPermissionUpdateContractOrBuilder`
    - #### getActivesOrBuilderList

      ```
      public java.util.List<? extends Common.PermissionOrBuilder> getActivesOrBuilderList()
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`

      Specified by:
      :   `getActivesOrBuilderList` in interface `Contract.AccountPermissionUpdateContractOrBuilder`
    - #### addActivesBuilder

      ```
      public Common.Permission.Builder addActivesBuilder()
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`
    - #### addActivesBuilder

      ```
      public Common.Permission.Builder addActivesBuilder(int index)
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`
    - #### getActivesBuilderList

      ```
      public java.util.List<Common.Permission.Builder> getActivesBuilderList()
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`
    - #### setUnknownFields

      ```
      public final Contract.AccountPermissionUpdateContract.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountPermissionUpdateContract.Builder>`
    - #### mergeUnknownFields

      ```
      public final Contract.AccountPermissionUpdateContract.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Contract.AccountPermissionUpdateContract.Builder>`