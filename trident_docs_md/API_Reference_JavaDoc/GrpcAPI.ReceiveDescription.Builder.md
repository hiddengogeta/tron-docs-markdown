

org.tron.trident.api

## Class GrpcAPI.ReceiveDescription.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.ReceiveDescription.Builder](../../../../org/tron/trident/api/GrpcAPI.ReceiveDescription.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.ReceiveDescription.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.ReceiveDescriptionOrBuilder](../../../../org/tron/trident/api/GrpcAPI.ReceiveDescriptionOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.ReceiveDescription](../../../../org/tron/trident/api/GrpcAPI.ReceiveDescription.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.ReceiveDescription.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveDescription.Builder>
  implements GrpcAPI.ReceiveDescriptionOrBuilder
  ```

  Protobuf type `protocol.ReceiveDescription`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.ReceiveDescription.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.ReceiveDescription` | `build()` |
    | `GrpcAPI.ReceiveDescription` | `buildPartial()` |
    | `GrpcAPI.ReceiveDescription.Builder` | `clear()` |
    | `GrpcAPI.ReceiveDescription.Builder` | `clearCEnc()` Encryption for incoming, decrypt it with ivk |
    | `GrpcAPI.ReceiveDescription.Builder` | `clearCOut()` Encryption for audit, decrypt it with ovk |
    | `GrpcAPI.ReceiveDescription.Builder` | `clearEpk()` for Encryption |
    | `GrpcAPI.ReceiveDescription.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.ReceiveDescription.Builder` | `clearNoteCommitment()` `bytes note_commitment = 2;` |
    | `GrpcAPI.ReceiveDescription.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.ReceiveDescription.Builder` | `clearValueCommitment()` `bytes value_commitment = 1;` |
    | `GrpcAPI.ReceiveDescription.Builder` | `clearZkproof()` `bytes zkproof = 6;` |
    | `GrpcAPI.ReceiveDescription.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getCEnc()` Encryption for incoming, decrypt it with ivk |
    | `com.google.protobuf.ByteString` | `getCOut()` Encryption for audit, decrypt it with ovk |
    | `GrpcAPI.ReceiveDescription` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `com.google.protobuf.ByteString` | `getEpk()` for Encryption |
    | `com.google.protobuf.ByteString` | `getNoteCommitment()` `bytes note_commitment = 2;` |
    | `com.google.protobuf.ByteString` | `getValueCommitment()` `bytes value_commitment = 1;` |
    | `com.google.protobuf.ByteString` | `getZkproof()` `bytes zkproof = 6;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.ReceiveDescription.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.ReceiveDescription.Builder` | `mergeFrom(GrpcAPI.ReceiveDescription other)` |
    | `GrpcAPI.ReceiveDescription.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.ReceiveDescription.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.ReceiveDescription.Builder` | `setCEnc(com.google.protobuf.ByteString value)` Encryption for incoming, decrypt it with ivk |
    | `GrpcAPI.ReceiveDescription.Builder` | `setCOut(com.google.protobuf.ByteString value)` Encryption for audit, decrypt it with ovk |
    | `GrpcAPI.ReceiveDescription.Builder` | `setEpk(com.google.protobuf.ByteString value)` for Encryption |
    | `GrpcAPI.ReceiveDescription.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.ReceiveDescription.Builder` | `setNoteCommitment(com.google.protobuf.ByteString value)` `bytes note_commitment = 2;` |
    | `GrpcAPI.ReceiveDescription.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.ReceiveDescription.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.ReceiveDescription.Builder` | `setValueCommitment(com.google.protobuf.ByteString value)` `bytes value_commitment = 1;` |
    | `GrpcAPI.ReceiveDescription.Builder` | `setZkproof(com.google.protobuf.ByteString value)` `bytes zkproof = 6;` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveDescription.Builder>`
    - #### clear

      ```
      public GrpcAPI.ReceiveDescription.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveDescription.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveDescription.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.ReceiveDescription getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.ReceiveDescription build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.ReceiveDescription buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.ReceiveDescription.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveDescription.Builder>`
    - #### setField

      ```
      public GrpcAPI.ReceiveDescription.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                         java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveDescription.Builder>`
    - #### clearField

      ```
      public GrpcAPI.ReceiveDescription.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveDescription.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.ReceiveDescription.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveDescription.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.ReceiveDescription.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                 int index,
                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveDescription.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.ReceiveDescription.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                 java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveDescription.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.ReceiveDescription.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.ReceiveDescription.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.ReceiveDescription.Builder mergeFrom(GrpcAPI.ReceiveDescription other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveDescription.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.ReceiveDescription.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                   throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.ReceiveDescription.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getValueCommitment

      ```
      public com.google.protobuf.ByteString getValueCommitment()
      ```

      `bytes value_commitment = 1;`

      Specified by:
      :   `getValueCommitment` in interface `GrpcAPI.ReceiveDescriptionOrBuilder`

      Returns:
      :   The valueCommitment.
    - #### setValueCommitment

      ```
      public GrpcAPI.ReceiveDescription.Builder setValueCommitment(com.google.protobuf.ByteString value)
      ```

      `bytes value_commitment = 1;`

      Parameters:
      :   `value` - The valueCommitment to set.

      Returns:
      :   This builder for chaining.
    - #### clearValueCommitment

      ```
      public GrpcAPI.ReceiveDescription.Builder clearValueCommitment()
      ```

      `bytes value_commitment = 1;`

      Returns:
      :   This builder for chaining.
    - #### getNoteCommitment

      ```
      public com.google.protobuf.ByteString getNoteCommitment()
      ```

      `bytes note_commitment = 2;`

      Specified by:
      :   `getNoteCommitment` in interface `GrpcAPI.ReceiveDescriptionOrBuilder`

      Returns:
      :   The noteCommitment.
    - #### setNoteCommitment

      ```
      public GrpcAPI.ReceiveDescription.Builder setNoteCommitment(com.google.protobuf.ByteString value)
      ```

      `bytes note_commitment = 2;`

      Parameters:
      :   `value` - The noteCommitment to set.

      Returns:
      :   This builder for chaining.
    - #### clearNoteCommitment

      ```
      public GrpcAPI.ReceiveDescription.Builder clearNoteCommitment()
      ```

      `bytes note_commitment = 2;`

      Returns:
      :   This builder for chaining.
    - #### getEpk

      ```
      public com.google.protobuf.ByteString getEpk()
      ```

      ```
       for Encryption
      ```

      `bytes epk = 3;`

      Specified by:
      :   `getEpk` in interface `GrpcAPI.ReceiveDescriptionOrBuilder`

      Returns:
      :   The epk.
    - #### setEpk

      ```
      public GrpcAPI.ReceiveDescription.Builder setEpk(com.google.protobuf.ByteString value)
      ```

      ```
       for Encryption
      ```

      `bytes epk = 3;`

      Parameters:
      :   `value` - The epk to set.

      Returns:
      :   This builder for chaining.
    - #### clearEpk

      ```
      public GrpcAPI.ReceiveDescription.Builder clearEpk()
      ```

      ```
       for Encryption
      ```

      `bytes epk = 3;`

      Returns:
      :   This builder for chaining.
    - #### getCEnc

      ```
      public com.google.protobuf.ByteString getCEnc()
      ```

      ```
       Encryption for incoming, decrypt it with ivk
      ```

      `bytes c_enc = 4;`

      Specified by:
      :   `getCEnc` in interface `GrpcAPI.ReceiveDescriptionOrBuilder`

      Returns:
      :   The cEnc.
    - #### setCEnc

      ```
      public GrpcAPI.ReceiveDescription.Builder setCEnc(com.google.protobuf.ByteString value)
      ```

      ```
       Encryption for incoming, decrypt it with ivk
      ```

      `bytes c_enc = 4;`

      Parameters:
      :   `value` - The cEnc to set.

      Returns:
      :   This builder for chaining.
    - #### clearCEnc

      ```
      public GrpcAPI.ReceiveDescription.Builder clearCEnc()
      ```

      ```
       Encryption for incoming, decrypt it with ivk
      ```

      `bytes c_enc = 4;`

      Returns:
      :   This builder for chaining.
    - #### getCOut

      ```
      public com.google.protobuf.ByteString getCOut()
      ```

      ```
       Encryption for audit, decrypt it with ovk
      ```

      `bytes c_out = 5;`

      Specified by:
      :   `getCOut` in interface `GrpcAPI.ReceiveDescriptionOrBuilder`

      Returns:
      :   The cOut.
    - #### setCOut

      ```
      public GrpcAPI.ReceiveDescription.Builder setCOut(com.google.protobuf.ByteString value)
      ```

      ```
       Encryption for audit, decrypt it with ovk
      ```

      `bytes c_out = 5;`

      Parameters:
      :   `value` - The cOut to set.

      Returns:
      :   This builder for chaining.
    - #### clearCOut

      ```
      public GrpcAPI.ReceiveDescription.Builder clearCOut()
      ```

      ```
       Encryption for audit, decrypt it with ovk
      ```

      `bytes c_out = 5;`

      Returns:
      :   This builder for chaining.
    - #### getZkproof

      ```
      public com.google.protobuf.ByteString getZkproof()
      ```

      `bytes zkproof = 6;`

      Specified by:
      :   `getZkproof` in interface `GrpcAPI.ReceiveDescriptionOrBuilder`

      Returns:
      :   The zkproof.
    - #### setZkproof

      ```
      public GrpcAPI.ReceiveDescription.Builder setZkproof(com.google.protobuf.ByteString value)
      ```

      `bytes zkproof = 6;`

      Parameters:
      :   `value` - The zkproof to set.

      Returns:
      :   This builder for chaining.
    - #### clearZkproof

      ```
      public GrpcAPI.ReceiveDescription.Builder clearZkproof()
      ```

      `bytes zkproof = 6;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.ReceiveDescription.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveDescription.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.ReceiveDescription.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ReceiveDescription.Builder>`