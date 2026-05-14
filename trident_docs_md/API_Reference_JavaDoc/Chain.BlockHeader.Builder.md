

org.tron.trident.proto

## Class Chain.BlockHeader.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Chain.BlockHeader.Builder](../../../../org/tron/trident/proto/Chain.BlockHeader.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Chain.BlockHeader.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Chain.BlockHeaderOrBuilder](../../../../org/tron/trident/proto/Chain.BlockHeaderOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Chain.BlockHeader](../../../../org/tron/trident/proto/Chain.BlockHeader.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Chain.BlockHeader.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.Builder>
  implements Chain.BlockHeaderOrBuilder
  ```

  Protobuf type `protocol.BlockHeader`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Chain.BlockHeader.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Chain.BlockHeader` | `build()` |
    | `Chain.BlockHeader` | `buildPartial()` |
    | `Chain.BlockHeader.Builder` | `clear()` |
    | `Chain.BlockHeader.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Chain.BlockHeader.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Chain.BlockHeader.Builder` | `clearRawData()` `.protocol.BlockHeader.raw raw_data = 1;` |
    | `Chain.BlockHeader.Builder` | `clearWitnessSignature()` `bytes witness_signature = 2;` |
    | `Chain.BlockHeader.Builder` | `clone()` |
    | `Chain.BlockHeader` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Chain.BlockHeader.raw` | `getRawData()` `.protocol.BlockHeader.raw raw_data = 1;` |
    | `Chain.BlockHeader.raw.Builder` | `getRawDataBuilder()` `.protocol.BlockHeader.raw raw_data = 1;` |
    | `Chain.BlockHeader.rawOrBuilder` | `getRawDataOrBuilder()` `.protocol.BlockHeader.raw raw_data = 1;` |
    | `com.google.protobuf.ByteString` | `getWitnessSignature()` `bytes witness_signature = 2;` |
    | `boolean` | `hasRawData()` `.protocol.BlockHeader.raw raw_data = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Chain.BlockHeader.Builder` | `mergeFrom(Chain.BlockHeader other)` |
    | `Chain.BlockHeader.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Chain.BlockHeader.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Chain.BlockHeader.Builder` | `mergeRawData(Chain.BlockHeader.raw value)` `.protocol.BlockHeader.raw raw_data = 1;` |
    | `Chain.BlockHeader.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Chain.BlockHeader.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Chain.BlockHeader.Builder` | `setRawData(Chain.BlockHeader.raw.Builder builderForValue)` `.protocol.BlockHeader.raw raw_data = 1;` |
    | `Chain.BlockHeader.Builder` | `setRawData(Chain.BlockHeader.raw value)` `.protocol.BlockHeader.raw raw_data = 1;` |
    | `Chain.BlockHeader.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Chain.BlockHeader.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Chain.BlockHeader.Builder` | `setWitnessSignature(com.google.protobuf.ByteString value)` `bytes witness_signature = 2;` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.Builder>`
    - #### clear

      ```
      public Chain.BlockHeader.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Chain.BlockHeader getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Chain.BlockHeader build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Chain.BlockHeader buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Chain.BlockHeader.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.Builder>`
    - #### setField

      ```
      public Chain.BlockHeader.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.Builder>`
    - #### clearField

      ```
      public Chain.BlockHeader.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.Builder>`
    - #### clearOneof

      ```
      public Chain.BlockHeader.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.Builder>`
    - #### setRepeatedField

      ```
      public Chain.BlockHeader.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                        int index,
                                                        java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.Builder>`
    - #### addRepeatedField

      ```
      public Chain.BlockHeader.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                        java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.Builder>`
    - #### mergeFrom

      ```
      public Chain.BlockHeader.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Chain.BlockHeader.Builder>`
    - #### mergeFrom

      ```
      public Chain.BlockHeader.Builder mergeFrom(Chain.BlockHeader other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.Builder>`
    - #### mergeFrom

      ```
      public Chain.BlockHeader.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                 com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                          throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Chain.BlockHeader.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### hasRawData

      ```
      public boolean hasRawData()
      ```

      `.protocol.BlockHeader.raw raw_data = 1;`

      Specified by:
      :   `hasRawData` in interface `Chain.BlockHeaderOrBuilder`

      Returns:
      :   Whether the rawData field is set.
    - #### getRawData

      ```
      public Chain.BlockHeader.raw getRawData()
      ```

      `.protocol.BlockHeader.raw raw_data = 1;`

      Specified by:
      :   `getRawData` in interface `Chain.BlockHeaderOrBuilder`

      Returns:
      :   The rawData.
    - #### setRawData

      ```
      public Chain.BlockHeader.Builder setRawData(Chain.BlockHeader.raw value)
      ```

      `.protocol.BlockHeader.raw raw_data = 1;`
    - #### setRawData

      ```
      public Chain.BlockHeader.Builder setRawData(Chain.BlockHeader.raw.Builder builderForValue)
      ```

      `.protocol.BlockHeader.raw raw_data = 1;`
    - #### mergeRawData

      ```
      public Chain.BlockHeader.Builder mergeRawData(Chain.BlockHeader.raw value)
      ```

      `.protocol.BlockHeader.raw raw_data = 1;`
    - #### clearRawData

      ```
      public Chain.BlockHeader.Builder clearRawData()
      ```

      `.protocol.BlockHeader.raw raw_data = 1;`
    - #### getRawDataBuilder

      ```
      public Chain.BlockHeader.raw.Builder getRawDataBuilder()
      ```

      `.protocol.BlockHeader.raw raw_data = 1;`
    - #### getRawDataOrBuilder

      ```
      public Chain.BlockHeader.rawOrBuilder getRawDataOrBuilder()
      ```

      `.protocol.BlockHeader.raw raw_data = 1;`

      Specified by:
      :   `getRawDataOrBuilder` in interface `Chain.BlockHeaderOrBuilder`
    - #### getWitnessSignature

      ```
      public com.google.protobuf.ByteString getWitnessSignature()
      ```

      `bytes witness_signature = 2;`

      Specified by:
      :   `getWitnessSignature` in interface `Chain.BlockHeaderOrBuilder`

      Returns:
      :   The witnessSignature.
    - #### setWitnessSignature

      ```
      public Chain.BlockHeader.Builder setWitnessSignature(com.google.protobuf.ByteString value)
      ```

      `bytes witness_signature = 2;`

      Parameters:
      :   `value` - The witnessSignature to set.

      Returns:
      :   This builder for chaining.
    - #### clearWitnessSignature

      ```
      public Chain.BlockHeader.Builder clearWitnessSignature()
      ```

      `bytes witness_signature = 2;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Chain.BlockHeader.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.Builder>`
    - #### mergeUnknownFields

      ```
      public final Chain.BlockHeader.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.BlockHeader.Builder>`