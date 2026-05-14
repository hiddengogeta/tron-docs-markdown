

org.tron.trident.api

## Class GrpcAPI.SpendDescription.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.SpendDescription.Builder](../../../../org/tron/trident/api/GrpcAPI.SpendDescription.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.SpendDescription.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.SpendDescriptionOrBuilder](../../../../org/tron/trident/api/GrpcAPI.SpendDescriptionOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.SpendDescription](../../../../org/tron/trident/api/GrpcAPI.SpendDescription.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.SpendDescription.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendDescription.Builder>
  implements GrpcAPI.SpendDescriptionOrBuilder
  ```

  Protobuf type `protocol.SpendDescription`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.SpendDescription.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.SpendDescription` | `build()` |
    | `GrpcAPI.SpendDescription` | `buildPartial()` |
    | `GrpcAPI.SpendDescription.Builder` | `clear()` |
    | `GrpcAPI.SpendDescription.Builder` | `clearAnchor()` merkle root |
    | `GrpcAPI.SpendDescription.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.SpendDescription.Builder` | `clearNullifier()` used for check double spend |
    | `GrpcAPI.SpendDescription.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.SpendDescription.Builder` | `clearRk()` used for check spend authority signature |
    | `GrpcAPI.SpendDescription.Builder` | `clearSpendAuthoritySignature()` `bytes spend_authority_signature = 6;` |
    | `GrpcAPI.SpendDescription.Builder` | `clearValueCommitment()` `bytes value_commitment = 1;` |
    | `GrpcAPI.SpendDescription.Builder` | `clearZkproof()` `bytes zkproof = 5;` |
    | `GrpcAPI.SpendDescription.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getAnchor()` merkle root |
    | `GrpcAPI.SpendDescription` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getNullifier()` used for check double spend |
    | `com.google.protobuf.ByteString` | `getRk()` used for check spend authority signature |
    | `com.google.protobuf.ByteString` | `getSpendAuthoritySignature()` `bytes spend_authority_signature = 6;` |
    | `com.google.protobuf.ByteString` | `getValueCommitment()` `bytes value_commitment = 1;` |
    | `com.google.protobuf.ByteString` | `getZkproof()` `bytes zkproof = 5;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.SpendDescription.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.SpendDescription.Builder` | `mergeFrom(GrpcAPI.SpendDescription other)` |
    | `GrpcAPI.SpendDescription.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.SpendDescription.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.SpendDescription.Builder` | `setAnchor(com.google.protobuf.ByteString value)` merkle root |
    | `GrpcAPI.SpendDescription.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.SpendDescription.Builder` | `setNullifier(com.google.protobuf.ByteString value)` used for check double spend |
    | `GrpcAPI.SpendDescription.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.SpendDescription.Builder` | `setRk(com.google.protobuf.ByteString value)` used for check spend authority signature |
    | `GrpcAPI.SpendDescription.Builder` | `setSpendAuthoritySignature(com.google.protobuf.ByteString value)` `bytes spend_authority_signature = 6;` |
    | `GrpcAPI.SpendDescription.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.SpendDescription.Builder` | `setValueCommitment(com.google.protobuf.ByteString value)` `bytes value_commitment = 1;` |
    | `GrpcAPI.SpendDescription.Builder` | `setZkproof(com.google.protobuf.ByteString value)` `bytes zkproof = 5;` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendDescription.Builder>`
    - #### clear

      ```
      public GrpcAPI.SpendDescription.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendDescription.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendDescription.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.SpendDescription getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.SpendDescription build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.SpendDescription buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.SpendDescription.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendDescription.Builder>`
    - #### setField

      ```
      public GrpcAPI.SpendDescription.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                       java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendDescription.Builder>`
    - #### clearField

      ```
      public GrpcAPI.SpendDescription.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendDescription.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.SpendDescription.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendDescription.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.SpendDescription.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               int index,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendDescription.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.SpendDescription.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                               java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendDescription.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.SpendDescription.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.SpendDescription.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.SpendDescription.Builder mergeFrom(GrpcAPI.SpendDescription other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendDescription.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.SpendDescription.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                 throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.SpendDescription.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getValueCommitment

      ```
      public com.google.protobuf.ByteString getValueCommitment()
      ```

      `bytes value_commitment = 1;`

      Specified by:
      :   `getValueCommitment` in interface `GrpcAPI.SpendDescriptionOrBuilder`

      Returns:
      :   The valueCommitment.
    - #### setValueCommitment

      ```
      public GrpcAPI.SpendDescription.Builder setValueCommitment(com.google.protobuf.ByteString value)
      ```

      `bytes value_commitment = 1;`

      Parameters:
      :   `value` - The valueCommitment to set.

      Returns:
      :   This builder for chaining.
    - #### clearValueCommitment

      ```
      public GrpcAPI.SpendDescription.Builder clearValueCommitment()
      ```

      `bytes value_commitment = 1;`

      Returns:
      :   This builder for chaining.
    - #### getAnchor

      ```
      public com.google.protobuf.ByteString getAnchor()
      ```

      ```
       merkle root
      ```

      `bytes anchor = 2;`

      Specified by:
      :   `getAnchor` in interface `GrpcAPI.SpendDescriptionOrBuilder`

      Returns:
      :   The anchor.
    - #### setAnchor

      ```
      public GrpcAPI.SpendDescription.Builder setAnchor(com.google.protobuf.ByteString value)
      ```

      ```
       merkle root
      ```

      `bytes anchor = 2;`

      Parameters:
      :   `value` - The anchor to set.

      Returns:
      :   This builder for chaining.
    - #### clearAnchor

      ```
      public GrpcAPI.SpendDescription.Builder clearAnchor()
      ```

      ```
       merkle root
      ```

      `bytes anchor = 2;`

      Returns:
      :   This builder for chaining.
    - #### getNullifier

      ```
      public com.google.protobuf.ByteString getNullifier()
      ```

      ```
       used for check double spend
      ```

      `bytes nullifier = 3;`

      Specified by:
      :   `getNullifier` in interface `GrpcAPI.SpendDescriptionOrBuilder`

      Returns:
      :   The nullifier.
    - #### setNullifier

      ```
      public GrpcAPI.SpendDescription.Builder setNullifier(com.google.protobuf.ByteString value)
      ```

      ```
       used for check double spend
      ```

      `bytes nullifier = 3;`

      Parameters:
      :   `value` - The nullifier to set.

      Returns:
      :   This builder for chaining.
    - #### clearNullifier

      ```
      public GrpcAPI.SpendDescription.Builder clearNullifier()
      ```

      ```
       used for check double spend
      ```

      `bytes nullifier = 3;`

      Returns:
      :   This builder for chaining.
    - #### getRk

      ```
      public com.google.protobuf.ByteString getRk()
      ```

      ```
       used for check spend authority signature
      ```

      `bytes rk = 4;`

      Specified by:
      :   `getRk` in interface `GrpcAPI.SpendDescriptionOrBuilder`

      Returns:
      :   The rk.
    - #### setRk

      ```
      public GrpcAPI.SpendDescription.Builder setRk(com.google.protobuf.ByteString value)
      ```

      ```
       used for check spend authority signature
      ```

      `bytes rk = 4;`

      Parameters:
      :   `value` - The rk to set.

      Returns:
      :   This builder for chaining.
    - #### clearRk

      ```
      public GrpcAPI.SpendDescription.Builder clearRk()
      ```

      ```
       used for check spend authority signature
      ```

      `bytes rk = 4;`

      Returns:
      :   This builder for chaining.
    - #### getZkproof

      ```
      public com.google.protobuf.ByteString getZkproof()
      ```

      `bytes zkproof = 5;`

      Specified by:
      :   `getZkproof` in interface `GrpcAPI.SpendDescriptionOrBuilder`

      Returns:
      :   The zkproof.
    - #### setZkproof

      ```
      public GrpcAPI.SpendDescription.Builder setZkproof(com.google.protobuf.ByteString value)
      ```

      `bytes zkproof = 5;`

      Parameters:
      :   `value` - The zkproof to set.

      Returns:
      :   This builder for chaining.
    - #### clearZkproof

      ```
      public GrpcAPI.SpendDescription.Builder clearZkproof()
      ```

      `bytes zkproof = 5;`

      Returns:
      :   This builder for chaining.
    - #### getSpendAuthoritySignature

      ```
      public com.google.protobuf.ByteString getSpendAuthoritySignature()
      ```

      `bytes spend_authority_signature = 6;`

      Specified by:
      :   `getSpendAuthoritySignature` in interface `GrpcAPI.SpendDescriptionOrBuilder`

      Returns:
      :   The spendAuthoritySignature.
    - #### setSpendAuthoritySignature

      ```
      public GrpcAPI.SpendDescription.Builder setSpendAuthoritySignature(com.google.protobuf.ByteString value)
      ```

      `bytes spend_authority_signature = 6;`

      Parameters:
      :   `value` - The spendAuthoritySignature to set.

      Returns:
      :   This builder for chaining.
    - #### clearSpendAuthoritySignature

      ```
      public GrpcAPI.SpendDescription.Builder clearSpendAuthoritySignature()
      ```

      `bytes spend_authority_signature = 6;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.SpendDescription.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendDescription.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.SpendDescription.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.SpendDescription.Builder>`