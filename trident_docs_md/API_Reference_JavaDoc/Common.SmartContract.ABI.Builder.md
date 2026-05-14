

org.tron.trident.proto

## Class Common.SmartContract.ABI.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Common.SmartContract.ABI.Builder](../../../../org/tron/trident/proto/Common.SmartContract.ABI.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Common.SmartContract.ABI.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Common.SmartContract.ABIOrBuilder](../../../../org/tron/trident/proto/Common.SmartContract.ABIOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Common.SmartContract.ABI](../../../../org/tron/trident/proto/Common.SmartContract.ABI.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Common.SmartContract.ABI.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Builder>
  implements Common.SmartContract.ABIOrBuilder
  ```

  Protobuf type `protocol.SmartContract.ABI`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Common.SmartContract.ABI.Builder` | `addAllEntrys(java.lang.Iterable<? extends Common.SmartContract.ABI.Entry> values)` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `Common.SmartContract.ABI.Builder` | `addEntrys(Common.SmartContract.ABI.Entry.Builder builderForValue)` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `Common.SmartContract.ABI.Builder` | `addEntrys(Common.SmartContract.ABI.Entry value)` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `Common.SmartContract.ABI.Builder` | `addEntrys(int index, Common.SmartContract.ABI.Entry.Builder builderForValue)` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `Common.SmartContract.ABI.Builder` | `addEntrys(int index, Common.SmartContract.ABI.Entry value)` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `addEntrysBuilder()` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `addEntrysBuilder(int index)` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `Common.SmartContract.ABI.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Common.SmartContract.ABI` | `build()` |
    | `Common.SmartContract.ABI` | `buildPartial()` |
    | `Common.SmartContract.ABI.Builder` | `clear()` |
    | `Common.SmartContract.ABI.Builder` | `clearEntrys()` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `Common.SmartContract.ABI.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Common.SmartContract.ABI.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Common.SmartContract.ABI.Builder` | `clone()` |
    | `Common.SmartContract.ABI` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Common.SmartContract.ABI.Entry` | `getEntrys(int index)` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `Common.SmartContract.ABI.Entry.Builder` | `getEntrysBuilder(int index)` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `java.util.List<Common.SmartContract.ABI.Entry.Builder>` | `getEntrysBuilderList()` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `int` | `getEntrysCount()` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `java.util.List<Common.SmartContract.ABI.Entry>` | `getEntrysList()` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `Common.SmartContract.ABI.EntryOrBuilder` | `getEntrysOrBuilder(int index)` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `java.util.List<? extends Common.SmartContract.ABI.EntryOrBuilder>` | `getEntrysOrBuilderList()` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Common.SmartContract.ABI.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Common.SmartContract.ABI.Builder` | `mergeFrom(Common.SmartContract.ABI other)` |
    | `Common.SmartContract.ABI.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Common.SmartContract.ABI.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Common.SmartContract.ABI.Builder` | `removeEntrys(int index)` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `Common.SmartContract.ABI.Builder` | `setEntrys(int index, Common.SmartContract.ABI.Entry.Builder builderForValue)` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `Common.SmartContract.ABI.Builder` | `setEntrys(int index, Common.SmartContract.ABI.Entry value)` `repeated .protocol.SmartContract.ABI.Entry entrys = 1;` |
    | `Common.SmartContract.ABI.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Common.SmartContract.ABI.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Common.SmartContract.ABI.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Builder>`
    - #### clear

      ```
      public Common.SmartContract.ABI.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Common.SmartContract.ABI getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Common.SmartContract.ABI build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Common.SmartContract.ABI buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Common.SmartContract.ABI.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Builder>`
    - #### setField

      ```
      public Common.SmartContract.ABI.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Builder>`
    - #### clearField

      ```
      public Common.SmartContract.ABI.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Builder>`
    - #### clearOneof

      ```
      public Common.SmartContract.ABI.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Builder>`
    - #### setRepeatedField

      ```
      public Common.SmartContract.ABI.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               int index,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Builder>`
    - #### addRepeatedField

      ```
      public Common.SmartContract.ABI.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Builder>`
    - #### mergeFrom

      ```
      public Common.SmartContract.ABI.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Common.SmartContract.ABI.Builder>`
    - #### mergeFrom

      ```
      public Common.SmartContract.ABI.Builder mergeFrom(Common.SmartContract.ABI other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Builder>`
    - #### mergeFrom

      ```
      public Common.SmartContract.ABI.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                 throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Common.SmartContract.ABI.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getEntrysList

      ```
      public java.util.List<Common.SmartContract.ABI.Entry> getEntrysList()
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`

      Specified by:
      :   `getEntrysList` in interface `Common.SmartContract.ABIOrBuilder`
    - #### getEntrysCount

      ```
      public int getEntrysCount()
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`

      Specified by:
      :   `getEntrysCount` in interface `Common.SmartContract.ABIOrBuilder`
    - #### getEntrys

      ```
      public Common.SmartContract.ABI.Entry getEntrys(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`

      Specified by:
      :   `getEntrys` in interface `Common.SmartContract.ABIOrBuilder`
    - #### setEntrys

      ```
      public Common.SmartContract.ABI.Builder setEntrys(int index,
                                                        Common.SmartContract.ABI.Entry value)
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`
    - #### setEntrys

      ```
      public Common.SmartContract.ABI.Builder setEntrys(int index,
                                                        Common.SmartContract.ABI.Entry.Builder builderForValue)
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`
    - #### addEntrys

      ```
      public Common.SmartContract.ABI.Builder addEntrys(Common.SmartContract.ABI.Entry value)
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`
    - #### addEntrys

      ```
      public Common.SmartContract.ABI.Builder addEntrys(int index,
                                                        Common.SmartContract.ABI.Entry value)
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`
    - #### addEntrys

      ```
      public Common.SmartContract.ABI.Builder addEntrys(Common.SmartContract.ABI.Entry.Builder builderForValue)
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`
    - #### addEntrys

      ```
      public Common.SmartContract.ABI.Builder addEntrys(int index,
                                                        Common.SmartContract.ABI.Entry.Builder builderForValue)
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`
    - #### addAllEntrys

      ```
      public Common.SmartContract.ABI.Builder addAllEntrys(java.lang.Iterable<? extends Common.SmartContract.ABI.Entry> values)
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`
    - #### clearEntrys

      ```
      public Common.SmartContract.ABI.Builder clearEntrys()
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`
    - #### removeEntrys

      ```
      public Common.SmartContract.ABI.Builder removeEntrys(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`
    - #### getEntrysBuilder

      ```
      public Common.SmartContract.ABI.Entry.Builder getEntrysBuilder(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`
    - #### getEntrysOrBuilder

      ```
      public Common.SmartContract.ABI.EntryOrBuilder getEntrysOrBuilder(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`

      Specified by:
      :   `getEntrysOrBuilder` in interface `Common.SmartContract.ABIOrBuilder`
    - #### getEntrysOrBuilderList

      ```
      public java.util.List<? extends Common.SmartContract.ABI.EntryOrBuilder> getEntrysOrBuilderList()
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`

      Specified by:
      :   `getEntrysOrBuilderList` in interface `Common.SmartContract.ABIOrBuilder`
    - #### addEntrysBuilder

      ```
      public Common.SmartContract.ABI.Entry.Builder addEntrysBuilder()
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`
    - #### addEntrysBuilder

      ```
      public Common.SmartContract.ABI.Entry.Builder addEntrysBuilder(int index)
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`
    - #### getEntrysBuilderList

      ```
      public java.util.List<Common.SmartContract.ABI.Entry.Builder> getEntrysBuilderList()
      ```

      `repeated .protocol.SmartContract.ABI.Entry entrys = 1;`
    - #### setUnknownFields

      ```
      public final Common.SmartContract.ABI.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Builder>`
    - #### mergeUnknownFields

      ```
      public final Common.SmartContract.ABI.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Builder>`