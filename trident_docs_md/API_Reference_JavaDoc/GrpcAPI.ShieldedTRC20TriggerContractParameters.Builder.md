

org.tron.trident.api

## Class GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder](../../../../org/tron/trident/api/GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder](../../../../org/tron/trident/api/GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.ShieldedTRC20TriggerContractParameters](../../../../org/tron/trident/api/GrpcAPI.ShieldedTRC20TriggerContractParameters.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder>
  implements GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder
  ```

  Protobuf type `protocol.ShieldedTRC20TriggerContractParameters`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `addAllSpendAuthoritySignature(java.lang.Iterable<? extends GrpcAPI.BytesMessage> values)` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `addSpendAuthoritySignature(GrpcAPI.BytesMessage.Builder builderForValue)` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `addSpendAuthoritySignature(GrpcAPI.BytesMessage value)` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `addSpendAuthoritySignature(int index, GrpcAPI.BytesMessage.Builder builderForValue)` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `addSpendAuthoritySignature(int index, GrpcAPI.BytesMessage value)` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `GrpcAPI.BytesMessage.Builder` | `addSpendAuthoritySignatureBuilder()` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `GrpcAPI.BytesMessage.Builder` | `addSpendAuthoritySignatureBuilder(int index)` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters` | `build()` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters` | `buildPartial()` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `clear()` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `clearAmount()` `string amount = 3;` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `clearShieldedTRC20Parameters()` `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `clearSpendAuthoritySignature()` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `clearTransparentToAddress()` `bytes transparent_to_address = 4;` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `clone()` |
    | `java.lang.String` | `getAmount()` `string amount = 3;` |
    | `com.google.protobuf.ByteString` | `getAmountBytes()` `string amount = 3;` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `GrpcAPI.ShieldedTRC20Parameters` | `getShieldedTRC20Parameters()` `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;` |
    | `GrpcAPI.ShieldedTRC20Parameters.Builder` | `getShieldedTRC20ParametersBuilder()` `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;` |
    | `GrpcAPI.ShieldedTRC20ParametersOrBuilder` | `getShieldedTRC20ParametersOrBuilder()` `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;` |
    | `GrpcAPI.BytesMessage` | `getSpendAuthoritySignature(int index)` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `GrpcAPI.BytesMessage.Builder` | `getSpendAuthoritySignatureBuilder(int index)` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `java.util.List<GrpcAPI.BytesMessage.Builder>` | `getSpendAuthoritySignatureBuilderList()` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `int` | `getSpendAuthoritySignatureCount()` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `java.util.List<GrpcAPI.BytesMessage>` | `getSpendAuthoritySignatureList()` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `GrpcAPI.BytesMessageOrBuilder` | `getSpendAuthoritySignatureOrBuilder(int index)` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `java.util.List<? extends GrpcAPI.BytesMessageOrBuilder>` | `getSpendAuthoritySignatureOrBuilderList()` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `com.google.protobuf.ByteString` | `getTransparentToAddress()` `bytes transparent_to_address = 4;` |
    | `boolean` | `hasShieldedTRC20Parameters()` `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `mergeFrom(GrpcAPI.ShieldedTRC20TriggerContractParameters other)` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `mergeShieldedTRC20Parameters(GrpcAPI.ShieldedTRC20Parameters value)` `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `removeSpendAuthoritySignature(int index)` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `setAmount(java.lang.String value)` `string amount = 3;` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `setAmountBytes(com.google.protobuf.ByteString value)` `string amount = 3;` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `setShieldedTRC20Parameters(GrpcAPI.ShieldedTRC20Parameters.Builder builderForValue)` `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `setShieldedTRC20Parameters(GrpcAPI.ShieldedTRC20Parameters value)` `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `setSpendAuthoritySignature(int index, GrpcAPI.BytesMessage.Builder builderForValue)` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `setSpendAuthoritySignature(int index, GrpcAPI.BytesMessage value)` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `setTransparentToAddress(com.google.protobuf.ByteString value)` `bytes transparent_to_address = 4;` |
    | `GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder>`
    - #### clear

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder>`
    - #### setField

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                             java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder>`
    - #### clearField

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                     int index,
                                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder mergeFrom(GrpcAPI.ShieldedTRC20TriggerContractParameters other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                              com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                                       throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### hasShieldedTRC20Parameters

      ```
      public boolean hasShieldedTRC20Parameters()
      ```

      `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;`

      Specified by:
      :   `hasShieldedTRC20Parameters` in interface `GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder`

      Returns:
      :   Whether the shieldedTRC20Parameters field is set.
    - #### getShieldedTRC20Parameters

      ```
      public GrpcAPI.ShieldedTRC20Parameters getShieldedTRC20Parameters()
      ```

      `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;`

      Specified by:
      :   `getShieldedTRC20Parameters` in interface `GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder`

      Returns:
      :   The shieldedTRC20Parameters.
    - #### setShieldedTRC20Parameters

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder setShieldedTRC20Parameters(GrpcAPI.ShieldedTRC20Parameters value)
      ```

      `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;`
    - #### setShieldedTRC20Parameters

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder setShieldedTRC20Parameters(GrpcAPI.ShieldedTRC20Parameters.Builder builderForValue)
      ```

      `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;`
    - #### mergeShieldedTRC20Parameters

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder mergeShieldedTRC20Parameters(GrpcAPI.ShieldedTRC20Parameters value)
      ```

      `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;`
    - #### clearShieldedTRC20Parameters

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder clearShieldedTRC20Parameters()
      ```

      `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;`
    - #### getShieldedTRC20ParametersBuilder

      ```
      public GrpcAPI.ShieldedTRC20Parameters.Builder getShieldedTRC20ParametersBuilder()
      ```

      `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;`
    - #### getShieldedTRC20ParametersOrBuilder

      ```
      public GrpcAPI.ShieldedTRC20ParametersOrBuilder getShieldedTRC20ParametersOrBuilder()
      ```

      `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;`

      Specified by:
      :   `getShieldedTRC20ParametersOrBuilder` in interface `GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder`
    - #### getSpendAuthoritySignatureList

      ```
      public java.util.List<GrpcAPI.BytesMessage> getSpendAuthoritySignatureList()
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`

      Specified by:
      :   `getSpendAuthoritySignatureList` in interface `GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder`
    - #### getSpendAuthoritySignatureCount

      ```
      public int getSpendAuthoritySignatureCount()
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`

      Specified by:
      :   `getSpendAuthoritySignatureCount` in interface `GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder`
    - #### getSpendAuthoritySignature

      ```
      public GrpcAPI.BytesMessage getSpendAuthoritySignature(int index)
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`

      Specified by:
      :   `getSpendAuthoritySignature` in interface `GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder`
    - #### setSpendAuthoritySignature

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder setSpendAuthoritySignature(int index,
                                                                                               GrpcAPI.BytesMessage value)
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`
    - #### setSpendAuthoritySignature

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder setSpendAuthoritySignature(int index,
                                                                                               GrpcAPI.BytesMessage.Builder builderForValue)
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`
    - #### addSpendAuthoritySignature

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder addSpendAuthoritySignature(GrpcAPI.BytesMessage value)
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`
    - #### addSpendAuthoritySignature

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder addSpendAuthoritySignature(int index,
                                                                                               GrpcAPI.BytesMessage value)
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`
    - #### addSpendAuthoritySignature

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder addSpendAuthoritySignature(GrpcAPI.BytesMessage.Builder builderForValue)
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`
    - #### addSpendAuthoritySignature

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder addSpendAuthoritySignature(int index,
                                                                                               GrpcAPI.BytesMessage.Builder builderForValue)
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`
    - #### addAllSpendAuthoritySignature

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder addAllSpendAuthoritySignature(java.lang.Iterable<? extends GrpcAPI.BytesMessage> values)
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`
    - #### clearSpendAuthoritySignature

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder clearSpendAuthoritySignature()
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`
    - #### removeSpendAuthoritySignature

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder removeSpendAuthoritySignature(int index)
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`
    - #### getSpendAuthoritySignatureBuilder

      ```
      public GrpcAPI.BytesMessage.Builder getSpendAuthoritySignatureBuilder(int index)
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`
    - #### getSpendAuthoritySignatureOrBuilder

      ```
      public GrpcAPI.BytesMessageOrBuilder getSpendAuthoritySignatureOrBuilder(int index)
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`

      Specified by:
      :   `getSpendAuthoritySignatureOrBuilder` in interface `GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder`
    - #### getSpendAuthoritySignatureOrBuilderList

      ```
      public java.util.List<? extends GrpcAPI.BytesMessageOrBuilder> getSpendAuthoritySignatureOrBuilderList()
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`

      Specified by:
      :   `getSpendAuthoritySignatureOrBuilderList` in interface `GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder`
    - #### addSpendAuthoritySignatureBuilder

      ```
      public GrpcAPI.BytesMessage.Builder addSpendAuthoritySignatureBuilder()
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`
    - #### addSpendAuthoritySignatureBuilder

      ```
      public GrpcAPI.BytesMessage.Builder addSpendAuthoritySignatureBuilder(int index)
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`
    - #### getSpendAuthoritySignatureBuilderList

      ```
      public java.util.List<GrpcAPI.BytesMessage.Builder> getSpendAuthoritySignatureBuilderList()
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`
    - #### getAmount

      ```
      public java.lang.String getAmount()
      ```

      `string amount = 3;`

      Specified by:
      :   `getAmount` in interface `GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder`

      Returns:
      :   The amount.
    - #### getAmountBytes

      ```
      public com.google.protobuf.ByteString getAmountBytes()
      ```

      `string amount = 3;`

      Specified by:
      :   `getAmountBytes` in interface `GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder`

      Returns:
      :   The bytes for amount.
    - #### setAmount

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder setAmount(java.lang.String value)
      ```

      `string amount = 3;`

      Parameters:
      :   `value` - The amount to set.

      Returns:
      :   This builder for chaining.
    - #### clearAmount

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder clearAmount()
      ```

      `string amount = 3;`

      Returns:
      :   This builder for chaining.
    - #### setAmountBytes

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder setAmountBytes(com.google.protobuf.ByteString value)
      ```

      `string amount = 3;`

      Parameters:
      :   `value` - The bytes for amount to set.

      Returns:
      :   This builder for chaining.
    - #### getTransparentToAddress

      ```
      public com.google.protobuf.ByteString getTransparentToAddress()
      ```

      `bytes transparent_to_address = 4;`

      Specified by:
      :   `getTransparentToAddress` in interface `GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder`

      Returns:
      :   The transparentToAddress.
    - #### setTransparentToAddress

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder setTransparentToAddress(com.google.protobuf.ByteString value)
      ```

      `bytes transparent_to_address = 4;`

      Parameters:
      :   `value` - The transparentToAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearTransparentToAddress

      ```
      public GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder clearTransparentToAddress()
      ```

      `bytes transparent_to_address = 4;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder>`