

org.tron.trident.proto

## Class Chain.Transaction.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Chain.Transaction.Builder](../../../../org/tron/trident/proto/Chain.Transaction.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Chain.Transaction.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Chain.TransactionOrBuilder](../../../../org/tron/trident/proto/Chain.TransactionOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Chain.Transaction](../../../../org/tron/trident/proto/Chain.Transaction.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Chain.Transaction.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Builder>
  implements Chain.TransactionOrBuilder
  ```

  Protobuf type `protocol.Transaction`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Chain.Transaction.Builder` | `addAllRet(java.lang.Iterable<? extends Chain.Transaction.Result> values)` `repeated .protocol.Transaction.Result ret = 5;` |
    | `Chain.Transaction.Builder` | `addAllSignature(java.lang.Iterable<? extends com.google.protobuf.ByteString> values)` only support size = 1, repeated list here for muti-sig extension |
    | `Chain.Transaction.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Chain.Transaction.Builder` | `addRet(Chain.Transaction.Result.Builder builderForValue)` `repeated .protocol.Transaction.Result ret = 5;` |
    | `Chain.Transaction.Builder` | `addRet(Chain.Transaction.Result value)` `repeated .protocol.Transaction.Result ret = 5;` |
    | `Chain.Transaction.Builder` | `addRet(int index, Chain.Transaction.Result.Builder builderForValue)` `repeated .protocol.Transaction.Result ret = 5;` |
    | `Chain.Transaction.Builder` | `addRet(int index, Chain.Transaction.Result value)` `repeated .protocol.Transaction.Result ret = 5;` |
    | `Chain.Transaction.Result.Builder` | `addRetBuilder()` `repeated .protocol.Transaction.Result ret = 5;` |
    | `Chain.Transaction.Result.Builder` | `addRetBuilder(int index)` `repeated .protocol.Transaction.Result ret = 5;` |
    | `Chain.Transaction.Builder` | `addSignature(com.google.protobuf.ByteString value)` only support size = 1, repeated list here for muti-sig extension |
    | `Chain.Transaction` | `build()` |
    | `Chain.Transaction` | `buildPartial()` |
    | `Chain.Transaction.Builder` | `clear()` |
    | `Chain.Transaction.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Chain.Transaction.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Chain.Transaction.Builder` | `clearRawData()` `.protocol.Transaction.raw raw_data = 1;` |
    | `Chain.Transaction.Builder` | `clearRet()` `repeated .protocol.Transaction.Result ret = 5;` |
    | `Chain.Transaction.Builder` | `clearSignature()` only support size = 1, repeated list here for muti-sig extension |
    | `Chain.Transaction.Builder` | `clone()` |
    | `Chain.Transaction` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `Chain.Transaction.raw` | `getRawData()` `.protocol.Transaction.raw raw_data = 1;` |
    | `Chain.Transaction.raw.Builder` | `getRawDataBuilder()` `.protocol.Transaction.raw raw_data = 1;` |
    | `Chain.Transaction.rawOrBuilder` | `getRawDataOrBuilder()` `.protocol.Transaction.raw raw_data = 1;` |
    | `Chain.Transaction.Result` | `getRet(int index)` `repeated .protocol.Transaction.Result ret = 5;` |
    | `Chain.Transaction.Result.Builder` | `getRetBuilder(int index)` `repeated .protocol.Transaction.Result ret = 5;` |
    | `java.util.List<Chain.Transaction.Result.Builder>` | `getRetBuilderList()` `repeated .protocol.Transaction.Result ret = 5;` |
    | `int` | `getRetCount()` `repeated .protocol.Transaction.Result ret = 5;` |
    | `java.util.List<Chain.Transaction.Result>` | `getRetList()` `repeated .protocol.Transaction.Result ret = 5;` |
    | `Chain.Transaction.ResultOrBuilder` | `getRetOrBuilder(int index)` `repeated .protocol.Transaction.Result ret = 5;` |
    | `java.util.List<? extends Chain.Transaction.ResultOrBuilder>` | `getRetOrBuilderList()` `repeated .protocol.Transaction.Result ret = 5;` |
    | `com.google.protobuf.ByteString` | `getSignature(int index)` only support size = 1, repeated list here for muti-sig extension |
    | `int` | `getSignatureCount()` only support size = 1, repeated list here for muti-sig extension |
    | `java.util.List<com.google.protobuf.ByteString>` | `getSignatureList()` only support size = 1, repeated list here for muti-sig extension |
    | `boolean` | `hasRawData()` `.protocol.Transaction.raw raw_data = 1;` |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Chain.Transaction.Builder` | `mergeFrom(Chain.Transaction other)` |
    | `Chain.Transaction.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Chain.Transaction.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Chain.Transaction.Builder` | `mergeRawData(Chain.Transaction.raw value)` `.protocol.Transaction.raw raw_data = 1;` |
    | `Chain.Transaction.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Chain.Transaction.Builder` | `removeRet(int index)` `repeated .protocol.Transaction.Result ret = 5;` |
    | `Chain.Transaction.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Chain.Transaction.Builder` | `setRawData(Chain.Transaction.raw.Builder builderForValue)` `.protocol.Transaction.raw raw_data = 1;` |
    | `Chain.Transaction.Builder` | `setRawData(Chain.Transaction.raw value)` `.protocol.Transaction.raw raw_data = 1;` |
    | `Chain.Transaction.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Chain.Transaction.Builder` | `setRet(int index, Chain.Transaction.Result.Builder builderForValue)` `repeated .protocol.Transaction.Result ret = 5;` |
    | `Chain.Transaction.Builder` | `setRet(int index, Chain.Transaction.Result value)` `repeated .protocol.Transaction.Result ret = 5;` |
    | `Chain.Transaction.Builder` | `setSignature(int index, com.google.protobuf.ByteString value)` only support size = 1, repeated list here for muti-sig extension |
    | `Chain.Transaction.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Builder>`
    - #### clear

      ```
      public Chain.Transaction.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Chain.Transaction getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Chain.Transaction build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Chain.Transaction buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Chain.Transaction.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Builder>`
    - #### setField

      ```
      public Chain.Transaction.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Builder>`
    - #### clearField

      ```
      public Chain.Transaction.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Builder>`
    - #### clearOneof

      ```
      public Chain.Transaction.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Builder>`
    - #### setRepeatedField

      ```
      public Chain.Transaction.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                        int index,
                                                        java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Builder>`
    - #### addRepeatedField

      ```
      public Chain.Transaction.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                        java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Builder>`
    - #### mergeFrom

      ```
      public Chain.Transaction.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Chain.Transaction.Builder>`
    - #### mergeFrom

      ```
      public Chain.Transaction.Builder mergeFrom(Chain.Transaction other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Builder>`
    - #### mergeFrom

      ```
      public Chain.Transaction.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                 com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                          throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Chain.Transaction.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### hasRawData

      ```
      public boolean hasRawData()
      ```

      `.protocol.Transaction.raw raw_data = 1;`

      Specified by:
      :   `hasRawData` in interface `Chain.TransactionOrBuilder`

      Returns:
      :   Whether the rawData field is set.
    - #### getRawData

      ```
      public Chain.Transaction.raw getRawData()
      ```

      `.protocol.Transaction.raw raw_data = 1;`

      Specified by:
      :   `getRawData` in interface `Chain.TransactionOrBuilder`

      Returns:
      :   The rawData.
    - #### setRawData

      ```
      public Chain.Transaction.Builder setRawData(Chain.Transaction.raw value)
      ```

      `.protocol.Transaction.raw raw_data = 1;`
    - #### setRawData

      ```
      public Chain.Transaction.Builder setRawData(Chain.Transaction.raw.Builder builderForValue)
      ```

      `.protocol.Transaction.raw raw_data = 1;`
    - #### mergeRawData

      ```
      public Chain.Transaction.Builder mergeRawData(Chain.Transaction.raw value)
      ```

      `.protocol.Transaction.raw raw_data = 1;`
    - #### clearRawData

      ```
      public Chain.Transaction.Builder clearRawData()
      ```

      `.protocol.Transaction.raw raw_data = 1;`
    - #### getRawDataBuilder

      ```
      public Chain.Transaction.raw.Builder getRawDataBuilder()
      ```

      `.protocol.Transaction.raw raw_data = 1;`
    - #### getRawDataOrBuilder

      ```
      public Chain.Transaction.rawOrBuilder getRawDataOrBuilder()
      ```

      `.protocol.Transaction.raw raw_data = 1;`

      Specified by:
      :   `getRawDataOrBuilder` in interface `Chain.TransactionOrBuilder`
    - #### getSignatureList

      ```
      public java.util.List<com.google.protobuf.ByteString> getSignatureList()
      ```

      ```
       only support size = 1, repeated list here for muti-sig extension
      ```

      `repeated bytes signature = 2;`

      Specified by:
      :   `getSignatureList` in interface `Chain.TransactionOrBuilder`

      Returns:
      :   A list containing the signature.
    - #### getSignatureCount

      ```
      public int getSignatureCount()
      ```

      ```
       only support size = 1, repeated list here for muti-sig extension
      ```

      `repeated bytes signature = 2;`

      Specified by:
      :   `getSignatureCount` in interface `Chain.TransactionOrBuilder`

      Returns:
      :   The count of signature.
    - #### getSignature

      ```
      public com.google.protobuf.ByteString getSignature(int index)
      ```

      ```
       only support size = 1, repeated list here for muti-sig extension
      ```

      `repeated bytes signature = 2;`

      Specified by:
      :   `getSignature` in interface `Chain.TransactionOrBuilder`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The signature at the given index.
    - #### setSignature

      ```
      public Chain.Transaction.Builder setSignature(int index,
                                                    com.google.protobuf.ByteString value)
      ```

      ```
       only support size = 1, repeated list here for muti-sig extension
      ```

      `repeated bytes signature = 2;`

      Parameters:
      :   `index` - The index to set the value at.
      :   `value` - The signature to set.

      Returns:
      :   This builder for chaining.
    - #### addSignature

      ```
      public Chain.Transaction.Builder addSignature(com.google.protobuf.ByteString value)
      ```

      ```
       only support size = 1, repeated list here for muti-sig extension
      ```

      `repeated bytes signature = 2;`

      Parameters:
      :   `value` - The signature to add.

      Returns:
      :   This builder for chaining.
    - #### addAllSignature

      ```
      public Chain.Transaction.Builder addAllSignature(java.lang.Iterable<? extends com.google.protobuf.ByteString> values)
      ```

      ```
       only support size = 1, repeated list here for muti-sig extension
      ```

      `repeated bytes signature = 2;`

      Parameters:
      :   `values` - The signature to add.

      Returns:
      :   This builder for chaining.
    - #### clearSignature

      ```
      public Chain.Transaction.Builder clearSignature()
      ```

      ```
       only support size = 1, repeated list here for muti-sig extension
      ```

      `repeated bytes signature = 2;`

      Returns:
      :   This builder for chaining.
    - #### getRetList

      ```
      public java.util.List<Chain.Transaction.Result> getRetList()
      ```

      `repeated .protocol.Transaction.Result ret = 5;`

      Specified by:
      :   `getRetList` in interface `Chain.TransactionOrBuilder`
    - #### getRetCount

      ```
      public int getRetCount()
      ```

      `repeated .protocol.Transaction.Result ret = 5;`

      Specified by:
      :   `getRetCount` in interface `Chain.TransactionOrBuilder`
    - #### getRet

      ```
      public Chain.Transaction.Result getRet(int index)
      ```

      `repeated .protocol.Transaction.Result ret = 5;`

      Specified by:
      :   `getRet` in interface `Chain.TransactionOrBuilder`
    - #### setRet

      ```
      public Chain.Transaction.Builder setRet(int index,
                                              Chain.Transaction.Result value)
      ```

      `repeated .protocol.Transaction.Result ret = 5;`
    - #### setRet

      ```
      public Chain.Transaction.Builder setRet(int index,
                                              Chain.Transaction.Result.Builder builderForValue)
      ```

      `repeated .protocol.Transaction.Result ret = 5;`
    - #### addRet

      ```
      public Chain.Transaction.Builder addRet(Chain.Transaction.Result value)
      ```

      `repeated .protocol.Transaction.Result ret = 5;`
    - #### addRet

      ```
      public Chain.Transaction.Builder addRet(int index,
                                              Chain.Transaction.Result value)
      ```

      `repeated .protocol.Transaction.Result ret = 5;`
    - #### addRet

      ```
      public Chain.Transaction.Builder addRet(Chain.Transaction.Result.Builder builderForValue)
      ```

      `repeated .protocol.Transaction.Result ret = 5;`
    - #### addRet

      ```
      public Chain.Transaction.Builder addRet(int index,
                                              Chain.Transaction.Result.Builder builderForValue)
      ```

      `repeated .protocol.Transaction.Result ret = 5;`
    - #### addAllRet

      ```
      public Chain.Transaction.Builder addAllRet(java.lang.Iterable<? extends Chain.Transaction.Result> values)
      ```

      `repeated .protocol.Transaction.Result ret = 5;`
    - #### clearRet

      ```
      public Chain.Transaction.Builder clearRet()
      ```

      `repeated .protocol.Transaction.Result ret = 5;`
    - #### removeRet

      ```
      public Chain.Transaction.Builder removeRet(int index)
      ```

      `repeated .protocol.Transaction.Result ret = 5;`
    - #### getRetBuilder

      ```
      public Chain.Transaction.Result.Builder getRetBuilder(int index)
      ```

      `repeated .protocol.Transaction.Result ret = 5;`
    - #### getRetOrBuilder

      ```
      public Chain.Transaction.ResultOrBuilder getRetOrBuilder(int index)
      ```

      `repeated .protocol.Transaction.Result ret = 5;`

      Specified by:
      :   `getRetOrBuilder` in interface `Chain.TransactionOrBuilder`
    - #### getRetOrBuilderList

      ```
      public java.util.List<? extends Chain.Transaction.ResultOrBuilder> getRetOrBuilderList()
      ```

      `repeated .protocol.Transaction.Result ret = 5;`

      Specified by:
      :   `getRetOrBuilderList` in interface `Chain.TransactionOrBuilder`
    - #### addRetBuilder

      ```
      public Chain.Transaction.Result.Builder addRetBuilder()
      ```

      `repeated .protocol.Transaction.Result ret = 5;`
    - #### addRetBuilder

      ```
      public Chain.Transaction.Result.Builder addRetBuilder(int index)
      ```

      `repeated .protocol.Transaction.Result ret = 5;`
    - #### getRetBuilderList

      ```
      public java.util.List<Chain.Transaction.Result.Builder> getRetBuilderList()
      ```

      `repeated .protocol.Transaction.Result ret = 5;`
    - #### setUnknownFields

      ```
      public final Chain.Transaction.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Builder>`
    - #### mergeUnknownFields

      ```
      public final Chain.Transaction.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Chain.Transaction.Builder>`