

org.tron.trident.api

## Class GrpcAPI.PrivateShieldedTRC20Parameters.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[GrpcAPI.PrivateShieldedTRC20Parameters.Builder](../../../../org/tron/trident/api/GrpcAPI.PrivateShieldedTRC20Parameters.Builder.html "class in org.tron.trident.api")>
      * + org.tron.trident.api.GrpcAPI.PrivateShieldedTRC20Parameters.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder](../../../../org/tron/trident/api/GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder.html "interface in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI.PrivateShieldedTRC20Parameters](../../../../org/tron/trident/api/GrpcAPI.PrivateShieldedTRC20Parameters.html "class in org.tron.trident.api")

  ---

    

  ```
  public static final class GrpcAPI.PrivateShieldedTRC20Parameters.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PrivateShieldedTRC20Parameters.Builder>
  implements GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder
  ```

  Protobuf type `protocol.PrivateShieldedTRC20Parameters`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `addAllShieldedReceives(java.lang.Iterable<? extends GrpcAPI.ReceiveNote> values)` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `addAllShieldedSpends(java.lang.Iterable<? extends GrpcAPI.SpendNoteTRC20> values)` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `addShieldedReceives(GrpcAPI.ReceiveNote.Builder builderForValue)` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `addShieldedReceives(GrpcAPI.ReceiveNote value)` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `addShieldedReceives(int index, GrpcAPI.ReceiveNote.Builder builderForValue)` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `addShieldedReceives(int index, GrpcAPI.ReceiveNote value)` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `GrpcAPI.ReceiveNote.Builder` | `addShieldedReceivesBuilder()` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `GrpcAPI.ReceiveNote.Builder` | `addShieldedReceivesBuilder(int index)` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `addShieldedSpends(GrpcAPI.SpendNoteTRC20.Builder builderForValue)` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `addShieldedSpends(GrpcAPI.SpendNoteTRC20 value)` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `addShieldedSpends(int index, GrpcAPI.SpendNoteTRC20.Builder builderForValue)` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `addShieldedSpends(int index, GrpcAPI.SpendNoteTRC20 value)` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `addShieldedSpendsBuilder()` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `addShieldedSpendsBuilder(int index)` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters` | `build()` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters` | `buildPartial()` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `clear()` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `clearAsk()` `bytes ask = 1;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `clearFromAmount()` `string from_amount = 4;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `clearNsk()` `bytes nsk = 2;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `clearOvk()` `bytes ovk = 3;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `clearShieldedReceives()` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `clearShieldedSpends()` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `clearShieldedTRC20ContractAddress()` `bytes shielded_TRC20_contract_address = 9;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `clearToAmount()` `string to_amount = 8;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `clearTransparentToAddress()` `bytes transparent_to_address = 7;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getAsk()` `bytes ask = 1;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `java.lang.String` | `getFromAmount()` `string from_amount = 4;` |
    | `com.google.protobuf.ByteString` | `getFromAmountBytes()` `string from_amount = 4;` |
    | `com.google.protobuf.ByteString` | `getNsk()` `bytes nsk = 2;` |
    | `com.google.protobuf.ByteString` | `getOvk()` `bytes ovk = 3;` |
    | `GrpcAPI.ReceiveNote` | `getShieldedReceives(int index)` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `GrpcAPI.ReceiveNote.Builder` | `getShieldedReceivesBuilder(int index)` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `java.util.List<GrpcAPI.ReceiveNote.Builder>` | `getShieldedReceivesBuilderList()` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `int` | `getShieldedReceivesCount()` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `java.util.List<GrpcAPI.ReceiveNote>` | `getShieldedReceivesList()` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `GrpcAPI.ReceiveNoteOrBuilder` | `getShieldedReceivesOrBuilder(int index)` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `java.util.List<? extends GrpcAPI.ReceiveNoteOrBuilder>` | `getShieldedReceivesOrBuilderList()` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `GrpcAPI.SpendNoteTRC20` | `getShieldedSpends(int index)` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `GrpcAPI.SpendNoteTRC20.Builder` | `getShieldedSpendsBuilder(int index)` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `java.util.List<GrpcAPI.SpendNoteTRC20.Builder>` | `getShieldedSpendsBuilderList()` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `int` | `getShieldedSpendsCount()` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `java.util.List<GrpcAPI.SpendNoteTRC20>` | `getShieldedSpendsList()` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `GrpcAPI.SpendNoteTRC20OrBuilder` | `getShieldedSpendsOrBuilder(int index)` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `java.util.List<? extends GrpcAPI.SpendNoteTRC20OrBuilder>` | `getShieldedSpendsOrBuilderList()` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `com.google.protobuf.ByteString` | `getShieldedTRC20ContractAddress()` `bytes shielded_TRC20_contract_address = 9;` |
    | `java.lang.String` | `getToAmount()` `string to_amount = 8;` |
    | `com.google.protobuf.ByteString` | `getToAmountBytes()` `string to_amount = 8;` |
    | `com.google.protobuf.ByteString` | `getTransparentToAddress()` `bytes transparent_to_address = 7;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `mergeFrom(GrpcAPI.PrivateShieldedTRC20Parameters other)` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `removeShieldedReceives(int index)` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `removeShieldedSpends(int index)` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `setAsk(com.google.protobuf.ByteString value)` `bytes ask = 1;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `setFromAmount(java.lang.String value)` `string from_amount = 4;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `setFromAmountBytes(com.google.protobuf.ByteString value)` `string from_amount = 4;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `setNsk(com.google.protobuf.ByteString value)` `bytes nsk = 2;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `setOvk(com.google.protobuf.ByteString value)` `bytes ovk = 3;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `setShieldedReceives(int index, GrpcAPI.ReceiveNote.Builder builderForValue)` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `setShieldedReceives(int index, GrpcAPI.ReceiveNote value)` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `setShieldedSpends(int index, GrpcAPI.SpendNoteTRC20.Builder builderForValue)` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `setShieldedSpends(int index, GrpcAPI.SpendNoteTRC20 value)` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `setShieldedTRC20ContractAddress(com.google.protobuf.ByteString value)` `bytes shielded_TRC20_contract_address = 9;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `setToAmount(java.lang.String value)` `string to_amount = 8;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `setToAmountBytes(com.google.protobuf.ByteString value)` `string to_amount = 8;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `setTransparentToAddress(com.google.protobuf.ByteString value)` `bytes transparent_to_address = 7;` |
    | `GrpcAPI.PrivateShieldedTRC20Parameters.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PrivateShieldedTRC20Parameters.Builder>`
    - #### clear

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PrivateShieldedTRC20Parameters.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PrivateShieldedTRC20Parameters.Builder>`
    - #### getDefaultInstanceForType

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PrivateShieldedTRC20Parameters.Builder>`
    - #### setField

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                     java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PrivateShieldedTRC20Parameters.Builder>`
    - #### clearField

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PrivateShieldedTRC20Parameters.Builder>`
    - #### clearOneof

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PrivateShieldedTRC20Parameters.Builder>`
    - #### setRepeatedField

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                             int index,
                                                                             java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PrivateShieldedTRC20Parameters.Builder>`
    - #### addRepeatedField

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                             java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PrivateShieldedTRC20Parameters.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.PrivateShieldedTRC20Parameters.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder mergeFrom(GrpcAPI.PrivateShieldedTRC20Parameters other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PrivateShieldedTRC20Parameters.Builder>`
    - #### mergeFrom

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                               throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<GrpcAPI.PrivateShieldedTRC20Parameters.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getAsk

      ```
      public com.google.protobuf.ByteString getAsk()
      ```

      `bytes ask = 1;`

      Specified by:
      :   `getAsk` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The ask.
    - #### setAsk

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder setAsk(com.google.protobuf.ByteString value)
      ```

      `bytes ask = 1;`

      Parameters:
      :   `value` - The ask to set.

      Returns:
      :   This builder for chaining.
    - #### clearAsk

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder clearAsk()
      ```

      `bytes ask = 1;`

      Returns:
      :   This builder for chaining.
    - #### getNsk

      ```
      public com.google.protobuf.ByteString getNsk()
      ```

      `bytes nsk = 2;`

      Specified by:
      :   `getNsk` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The nsk.
    - #### setNsk

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder setNsk(com.google.protobuf.ByteString value)
      ```

      `bytes nsk = 2;`

      Parameters:
      :   `value` - The nsk to set.

      Returns:
      :   This builder for chaining.
    - #### clearNsk

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder clearNsk()
      ```

      `bytes nsk = 2;`

      Returns:
      :   This builder for chaining.
    - #### getOvk

      ```
      public com.google.protobuf.ByteString getOvk()
      ```

      `bytes ovk = 3;`

      Specified by:
      :   `getOvk` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The ovk.
    - #### setOvk

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder setOvk(com.google.protobuf.ByteString value)
      ```

      `bytes ovk = 3;`

      Parameters:
      :   `value` - The ovk to set.

      Returns:
      :   This builder for chaining.
    - #### clearOvk

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder clearOvk()
      ```

      `bytes ovk = 3;`

      Returns:
      :   This builder for chaining.
    - #### getFromAmount

      ```
      public java.lang.String getFromAmount()
      ```

      `string from_amount = 4;`

      Specified by:
      :   `getFromAmount` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The fromAmount.
    - #### getFromAmountBytes

      ```
      public com.google.protobuf.ByteString getFromAmountBytes()
      ```

      `string from_amount = 4;`

      Specified by:
      :   `getFromAmountBytes` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The bytes for fromAmount.
    - #### setFromAmount

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder setFromAmount(java.lang.String value)
      ```

      `string from_amount = 4;`

      Parameters:
      :   `value` - The fromAmount to set.

      Returns:
      :   This builder for chaining.
    - #### clearFromAmount

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder clearFromAmount()
      ```

      `string from_amount = 4;`

      Returns:
      :   This builder for chaining.
    - #### setFromAmountBytes

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder setFromAmountBytes(com.google.protobuf.ByteString value)
      ```

      `string from_amount = 4;`

      Parameters:
      :   `value` - The bytes for fromAmount to set.

      Returns:
      :   This builder for chaining.
    - #### getShieldedSpendsList

      ```
      public java.util.List<GrpcAPI.SpendNoteTRC20> getShieldedSpendsList()
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`

      Specified by:
      :   `getShieldedSpendsList` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`
    - #### getShieldedSpendsCount

      ```
      public int getShieldedSpendsCount()
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`

      Specified by:
      :   `getShieldedSpendsCount` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`
    - #### getShieldedSpends

      ```
      public GrpcAPI.SpendNoteTRC20 getShieldedSpends(int index)
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`

      Specified by:
      :   `getShieldedSpends` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`
    - #### setShieldedSpends

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder setShieldedSpends(int index,
                                                                              GrpcAPI.SpendNoteTRC20 value)
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`
    - #### setShieldedSpends

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder setShieldedSpends(int index,
                                                                              GrpcAPI.SpendNoteTRC20.Builder builderForValue)
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`
    - #### addShieldedSpends

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder addShieldedSpends(GrpcAPI.SpendNoteTRC20 value)
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`
    - #### addShieldedSpends

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder addShieldedSpends(int index,
                                                                              GrpcAPI.SpendNoteTRC20 value)
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`
    - #### addShieldedSpends

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder addShieldedSpends(GrpcAPI.SpendNoteTRC20.Builder builderForValue)
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`
    - #### addShieldedSpends

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder addShieldedSpends(int index,
                                                                              GrpcAPI.SpendNoteTRC20.Builder builderForValue)
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`
    - #### addAllShieldedSpends

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder addAllShieldedSpends(java.lang.Iterable<? extends GrpcAPI.SpendNoteTRC20> values)
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`
    - #### clearShieldedSpends

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder clearShieldedSpends()
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`
    - #### removeShieldedSpends

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder removeShieldedSpends(int index)
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`
    - #### getShieldedSpendsBuilder

      ```
      public GrpcAPI.SpendNoteTRC20.Builder getShieldedSpendsBuilder(int index)
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`
    - #### getShieldedSpendsOrBuilder

      ```
      public GrpcAPI.SpendNoteTRC20OrBuilder getShieldedSpendsOrBuilder(int index)
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`

      Specified by:
      :   `getShieldedSpendsOrBuilder` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`
    - #### getShieldedSpendsOrBuilderList

      ```
      public java.util.List<? extends GrpcAPI.SpendNoteTRC20OrBuilder> getShieldedSpendsOrBuilderList()
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`

      Specified by:
      :   `getShieldedSpendsOrBuilderList` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`
    - #### addShieldedSpendsBuilder

      ```
      public GrpcAPI.SpendNoteTRC20.Builder addShieldedSpendsBuilder()
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`
    - #### addShieldedSpendsBuilder

      ```
      public GrpcAPI.SpendNoteTRC20.Builder addShieldedSpendsBuilder(int index)
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`
    - #### getShieldedSpendsBuilderList

      ```
      public java.util.List<GrpcAPI.SpendNoteTRC20.Builder> getShieldedSpendsBuilderList()
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`
    - #### getShieldedReceivesList

      ```
      public java.util.List<GrpcAPI.ReceiveNote> getShieldedReceivesList()
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`

      Specified by:
      :   `getShieldedReceivesList` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`
    - #### getShieldedReceivesCount

      ```
      public int getShieldedReceivesCount()
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`

      Specified by:
      :   `getShieldedReceivesCount` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`
    - #### getShieldedReceives

      ```
      public GrpcAPI.ReceiveNote getShieldedReceives(int index)
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`

      Specified by:
      :   `getShieldedReceives` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`
    - #### setShieldedReceives

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder setShieldedReceives(int index,
                                                                                GrpcAPI.ReceiveNote value)
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`
    - #### setShieldedReceives

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder setShieldedReceives(int index,
                                                                                GrpcAPI.ReceiveNote.Builder builderForValue)
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`
    - #### addShieldedReceives

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder addShieldedReceives(GrpcAPI.ReceiveNote value)
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`
    - #### addShieldedReceives

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder addShieldedReceives(int index,
                                                                                GrpcAPI.ReceiveNote value)
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`
    - #### addShieldedReceives

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder addShieldedReceives(GrpcAPI.ReceiveNote.Builder builderForValue)
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`
    - #### addShieldedReceives

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder addShieldedReceives(int index,
                                                                                GrpcAPI.ReceiveNote.Builder builderForValue)
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`
    - #### addAllShieldedReceives

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder addAllShieldedReceives(java.lang.Iterable<? extends GrpcAPI.ReceiveNote> values)
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`
    - #### clearShieldedReceives

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder clearShieldedReceives()
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`
    - #### removeShieldedReceives

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder removeShieldedReceives(int index)
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`
    - #### getShieldedReceivesBuilder

      ```
      public GrpcAPI.ReceiveNote.Builder getShieldedReceivesBuilder(int index)
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`
    - #### getShieldedReceivesOrBuilder

      ```
      public GrpcAPI.ReceiveNoteOrBuilder getShieldedReceivesOrBuilder(int index)
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`

      Specified by:
      :   `getShieldedReceivesOrBuilder` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`
    - #### getShieldedReceivesOrBuilderList

      ```
      public java.util.List<? extends GrpcAPI.ReceiveNoteOrBuilder> getShieldedReceivesOrBuilderList()
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`

      Specified by:
      :   `getShieldedReceivesOrBuilderList` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`
    - #### addShieldedReceivesBuilder

      ```
      public GrpcAPI.ReceiveNote.Builder addShieldedReceivesBuilder()
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`
    - #### addShieldedReceivesBuilder

      ```
      public GrpcAPI.ReceiveNote.Builder addShieldedReceivesBuilder(int index)
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`
    - #### getShieldedReceivesBuilderList

      ```
      public java.util.List<GrpcAPI.ReceiveNote.Builder> getShieldedReceivesBuilderList()
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`
    - #### getTransparentToAddress

      ```
      public com.google.protobuf.ByteString getTransparentToAddress()
      ```

      `bytes transparent_to_address = 7;`

      Specified by:
      :   `getTransparentToAddress` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The transparentToAddress.
    - #### setTransparentToAddress

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder setTransparentToAddress(com.google.protobuf.ByteString value)
      ```

      `bytes transparent_to_address = 7;`

      Parameters:
      :   `value` - The transparentToAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearTransparentToAddress

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder clearTransparentToAddress()
      ```

      `bytes transparent_to_address = 7;`

      Returns:
      :   This builder for chaining.
    - #### getToAmount

      ```
      public java.lang.String getToAmount()
      ```

      `string to_amount = 8;`

      Specified by:
      :   `getToAmount` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The toAmount.
    - #### getToAmountBytes

      ```
      public com.google.protobuf.ByteString getToAmountBytes()
      ```

      `string to_amount = 8;`

      Specified by:
      :   `getToAmountBytes` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The bytes for toAmount.
    - #### setToAmount

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder setToAmount(java.lang.String value)
      ```

      `string to_amount = 8;`

      Parameters:
      :   `value` - The toAmount to set.

      Returns:
      :   This builder for chaining.
    - #### clearToAmount

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder clearToAmount()
      ```

      `string to_amount = 8;`

      Returns:
      :   This builder for chaining.
    - #### setToAmountBytes

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder setToAmountBytes(com.google.protobuf.ByteString value)
      ```

      `string to_amount = 8;`

      Parameters:
      :   `value` - The bytes for toAmount to set.

      Returns:
      :   This builder for chaining.
    - #### getShieldedTRC20ContractAddress

      ```
      public com.google.protobuf.ByteString getShieldedTRC20ContractAddress()
      ```

      `bytes shielded_TRC20_contract_address = 9;`

      Specified by:
      :   `getShieldedTRC20ContractAddress` in interface `GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder`

      Returns:
      :   The shieldedTRC20ContractAddress.
    - #### setShieldedTRC20ContractAddress

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder setShieldedTRC20ContractAddress(com.google.protobuf.ByteString value)
      ```

      `bytes shielded_TRC20_contract_address = 9;`

      Parameters:
      :   `value` - The shieldedTRC20ContractAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearShieldedTRC20ContractAddress

      ```
      public GrpcAPI.PrivateShieldedTRC20Parameters.Builder clearShieldedTRC20ContractAddress()
      ```

      `bytes shielded_TRC20_contract_address = 9;`

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final GrpcAPI.PrivateShieldedTRC20Parameters.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PrivateShieldedTRC20Parameters.Builder>`
    - #### mergeUnknownFields

      ```
      public final GrpcAPI.PrivateShieldedTRC20Parameters.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<GrpcAPI.PrivateShieldedTRC20Parameters.Builder>`