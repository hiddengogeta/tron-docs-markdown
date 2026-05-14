

org.tron.trident.proto

## Class Response.InternalTransaction.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Response.InternalTransaction.Builder](../../../../org/tron/trident/proto/Response.InternalTransaction.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Response.InternalTransaction.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Response.InternalTransactionOrBuilder](../../../../org/tron/trident/proto/Response.InternalTransactionOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Response.InternalTransaction](../../../../org/tron/trident/proto/Response.InternalTransaction.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Response.InternalTransaction.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.Builder>
  implements Response.InternalTransactionOrBuilder
  ```

  Protobuf type `protocol.InternalTransaction`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Response.InternalTransaction.Builder` | `addAllCallValueInfo(java.lang.Iterable<? extends Response.InternalTransaction.CallValueInfo> values)` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `Response.InternalTransaction.Builder` | `addCallValueInfo(int index, Response.InternalTransaction.CallValueInfo.Builder builderForValue)` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `Response.InternalTransaction.Builder` | `addCallValueInfo(int index, Response.InternalTransaction.CallValueInfo value)` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `Response.InternalTransaction.Builder` | `addCallValueInfo(Response.InternalTransaction.CallValueInfo.Builder builderForValue)` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `Response.InternalTransaction.Builder` | `addCallValueInfo(Response.InternalTransaction.CallValueInfo value)` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `Response.InternalTransaction.CallValueInfo.Builder` | `addCallValueInfoBuilder()` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `Response.InternalTransaction.CallValueInfo.Builder` | `addCallValueInfoBuilder(int index)` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `Response.InternalTransaction.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.InternalTransaction` | `build()` |
    | `Response.InternalTransaction` | `buildPartial()` |
    | `Response.InternalTransaction.Builder` | `clear()` |
    | `Response.InternalTransaction.Builder` | `clearCallerAddress()` the one send trx (TBD: or token) via function |
    | `Response.InternalTransaction.Builder` | `clearCallValueInfo()` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `Response.InternalTransaction.Builder` | `clearExtra()` `string extra = 7;` |
    | `Response.InternalTransaction.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Response.InternalTransaction.Builder` | `clearHash()` internalTransaction identity, the root InternalTransaction hash should equals to root transaction id. |
    | `Response.InternalTransaction.Builder` | `clearNote()` `bytes note = 5;` |
    | `Response.InternalTransaction.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Response.InternalTransaction.Builder` | `clearRejected()` `bool rejected = 6;` |
    | `Response.InternalTransaction.Builder` | `clearTransferToAddress()` the one recieve trx (TBD: or token) via function |
    | `Response.InternalTransaction.Builder` | `clone()` |
    | `com.google.protobuf.ByteString` | `getCallerAddress()` the one send trx (TBD: or token) via function |
    | `Response.InternalTransaction.CallValueInfo` | `getCallValueInfo(int index)` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `Response.InternalTransaction.CallValueInfo.Builder` | `getCallValueInfoBuilder(int index)` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `java.util.List<Response.InternalTransaction.CallValueInfo.Builder>` | `getCallValueInfoBuilderList()` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `int` | `getCallValueInfoCount()` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `java.util.List<Response.InternalTransaction.CallValueInfo>` | `getCallValueInfoList()` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `Response.InternalTransaction.CallValueInfoOrBuilder` | `getCallValueInfoOrBuilder(int index)` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `java.util.List<? extends Response.InternalTransaction.CallValueInfoOrBuilder>` | `getCallValueInfoOrBuilderList()` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `Response.InternalTransaction` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `java.lang.String` | `getExtra()` `string extra = 7;` |
    | `com.google.protobuf.ByteString` | `getExtraBytes()` `string extra = 7;` |
    | `com.google.protobuf.ByteString` | `getHash()` internalTransaction identity, the root InternalTransaction hash should equals to root transaction id. |
    | `com.google.protobuf.ByteString` | `getNote()` `bytes note = 5;` |
    | `boolean` | `getRejected()` `bool rejected = 6;` |
    | `com.google.protobuf.ByteString` | `getTransferToAddress()` the one recieve trx (TBD: or token) via function |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Response.InternalTransaction.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Response.InternalTransaction.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Response.InternalTransaction.Builder` | `mergeFrom(Response.InternalTransaction other)` |
    | `Response.InternalTransaction.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Response.InternalTransaction.Builder` | `removeCallValueInfo(int index)` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `Response.InternalTransaction.Builder` | `setCallerAddress(com.google.protobuf.ByteString value)` the one send trx (TBD: or token) via function |
    | `Response.InternalTransaction.Builder` | `setCallValueInfo(int index, Response.InternalTransaction.CallValueInfo.Builder builderForValue)` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `Response.InternalTransaction.Builder` | `setCallValueInfo(int index, Response.InternalTransaction.CallValueInfo value)` `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;` |
    | `Response.InternalTransaction.Builder` | `setExtra(java.lang.String value)` `string extra = 7;` |
    | `Response.InternalTransaction.Builder` | `setExtraBytes(com.google.protobuf.ByteString value)` `string extra = 7;` |
    | `Response.InternalTransaction.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Response.InternalTransaction.Builder` | `setHash(com.google.protobuf.ByteString value)` internalTransaction identity, the root InternalTransaction hash should equals to root transaction id. |
    | `Response.InternalTransaction.Builder` | `setNote(com.google.protobuf.ByteString value)` `bytes note = 5;` |
    | `Response.InternalTransaction.Builder` | `setRejected(boolean value)` `bool rejected = 6;` |
    | `Response.InternalTransaction.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Response.InternalTransaction.Builder` | `setTransferToAddress(com.google.protobuf.ByteString value)` the one recieve trx (TBD: or token) via function |
    | `Response.InternalTransaction.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.Builder>`
    - #### clear

      ```
      public Response.InternalTransaction.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Response.InternalTransaction getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Response.InternalTransaction build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Response.InternalTransaction buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Response.InternalTransaction.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.Builder>`
    - #### setField

      ```
      public Response.InternalTransaction.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                           java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.Builder>`
    - #### clearField

      ```
      public Response.InternalTransaction.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.Builder>`
    - #### clearOneof

      ```
      public Response.InternalTransaction.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.Builder>`
    - #### setRepeatedField

      ```
      public Response.InternalTransaction.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                   int index,
                                                                   java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.Builder>`
    - #### addRepeatedField

      ```
      public Response.InternalTransaction.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                   java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.Builder>`
    - #### mergeFrom

      ```
      public Response.InternalTransaction.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.InternalTransaction.Builder>`
    - #### mergeFrom

      ```
      public Response.InternalTransaction.Builder mergeFrom(Response.InternalTransaction other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.Builder>`
    - #### mergeFrom

      ```
      public Response.InternalTransaction.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                            com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                     throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Response.InternalTransaction.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getHash

      ```
      public com.google.protobuf.ByteString getHash()
      ```

      ```
       internalTransaction identity, the root InternalTransaction hash
       should equals to root transaction id.
      ```

      `bytes hash = 1;`

      Specified by:
      :   `getHash` in interface `Response.InternalTransactionOrBuilder`

      Returns:
      :   The hash.
    - #### setHash

      ```
      public Response.InternalTransaction.Builder setHash(com.google.protobuf.ByteString value)
      ```

      ```
       internalTransaction identity, the root InternalTransaction hash
       should equals to root transaction id.
      ```

      `bytes hash = 1;`

      Parameters:
      :   `value` - The hash to set.

      Returns:
      :   This builder for chaining.
    - #### clearHash

      ```
      public Response.InternalTransaction.Builder clearHash()
      ```

      ```
       internalTransaction identity, the root InternalTransaction hash
       should equals to root transaction id.
      ```

      `bytes hash = 1;`

      Returns:
      :   This builder for chaining.
    - #### getCallerAddress

      ```
      public com.google.protobuf.ByteString getCallerAddress()
      ```

      ```
       the one send trx (TBD: or token) via function
      ```

      `bytes caller_address = 2;`

      Specified by:
      :   `getCallerAddress` in interface `Response.InternalTransactionOrBuilder`

      Returns:
      :   The callerAddress.
    - #### setCallerAddress

      ```
      public Response.InternalTransaction.Builder setCallerAddress(com.google.protobuf.ByteString value)
      ```

      ```
       the one send trx (TBD: or token) via function
      ```

      `bytes caller_address = 2;`

      Parameters:
      :   `value` - The callerAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearCallerAddress

      ```
      public Response.InternalTransaction.Builder clearCallerAddress()
      ```

      ```
       the one send trx (TBD: or token) via function
      ```

      `bytes caller_address = 2;`

      Returns:
      :   This builder for chaining.
    - #### getTransferToAddress

      ```
      public com.google.protobuf.ByteString getTransferToAddress()
      ```

      ```
       the one recieve trx (TBD: or token) via function
      ```

      `bytes transferTo_address = 3;`

      Specified by:
      :   `getTransferToAddress` in interface `Response.InternalTransactionOrBuilder`

      Returns:
      :   The transferToAddress.
    - #### setTransferToAddress

      ```
      public Response.InternalTransaction.Builder setTransferToAddress(com.google.protobuf.ByteString value)
      ```

      ```
       the one recieve trx (TBD: or token) via function
      ```

      `bytes transferTo_address = 3;`

      Parameters:
      :   `value` - The transferToAddress to set.

      Returns:
      :   This builder for chaining.
    - #### clearTransferToAddress

      ```
      public Response.InternalTransaction.Builder clearTransferToAddress()
      ```

      ```
       the one recieve trx (TBD: or token) via function
      ```

      `bytes transferTo_address = 3;`

      Returns:
      :   This builder for chaining.
    - #### getCallValueInfoList

      ```
      public java.util.List<Response.InternalTransaction.CallValueInfo> getCallValueInfoList()
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`

      Specified by:
      :   `getCallValueInfoList` in interface `Response.InternalTransactionOrBuilder`
    - #### getCallValueInfoCount

      ```
      public int getCallValueInfoCount()
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`

      Specified by:
      :   `getCallValueInfoCount` in interface `Response.InternalTransactionOrBuilder`
    - #### getCallValueInfo

      ```
      public Response.InternalTransaction.CallValueInfo getCallValueInfo(int index)
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`

      Specified by:
      :   `getCallValueInfo` in interface `Response.InternalTransactionOrBuilder`
    - #### setCallValueInfo

      ```
      public Response.InternalTransaction.Builder setCallValueInfo(int index,
                                                                   Response.InternalTransaction.CallValueInfo value)
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`
    - #### setCallValueInfo

      ```
      public Response.InternalTransaction.Builder setCallValueInfo(int index,
                                                                   Response.InternalTransaction.CallValueInfo.Builder builderForValue)
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`
    - #### addCallValueInfo

      ```
      public Response.InternalTransaction.Builder addCallValueInfo(Response.InternalTransaction.CallValueInfo value)
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`
    - #### addCallValueInfo

      ```
      public Response.InternalTransaction.Builder addCallValueInfo(int index,
                                                                   Response.InternalTransaction.CallValueInfo value)
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`
    - #### addCallValueInfo

      ```
      public Response.InternalTransaction.Builder addCallValueInfo(Response.InternalTransaction.CallValueInfo.Builder builderForValue)
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`
    - #### addCallValueInfo

      ```
      public Response.InternalTransaction.Builder addCallValueInfo(int index,
                                                                   Response.InternalTransaction.CallValueInfo.Builder builderForValue)
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`
    - #### addAllCallValueInfo

      ```
      public Response.InternalTransaction.Builder addAllCallValueInfo(java.lang.Iterable<? extends Response.InternalTransaction.CallValueInfo> values)
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`
    - #### clearCallValueInfo

      ```
      public Response.InternalTransaction.Builder clearCallValueInfo()
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`
    - #### removeCallValueInfo

      ```
      public Response.InternalTransaction.Builder removeCallValueInfo(int index)
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`
    - #### getCallValueInfoBuilder

      ```
      public Response.InternalTransaction.CallValueInfo.Builder getCallValueInfoBuilder(int index)
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`
    - #### getCallValueInfoOrBuilder

      ```
      public Response.InternalTransaction.CallValueInfoOrBuilder getCallValueInfoOrBuilder(int index)
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`

      Specified by:
      :   `getCallValueInfoOrBuilder` in interface `Response.InternalTransactionOrBuilder`
    - #### getCallValueInfoOrBuilderList

      ```
      public java.util.List<? extends Response.InternalTransaction.CallValueInfoOrBuilder> getCallValueInfoOrBuilderList()
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`

      Specified by:
      :   `getCallValueInfoOrBuilderList` in interface `Response.InternalTransactionOrBuilder`
    - #### addCallValueInfoBuilder

      ```
      public Response.InternalTransaction.CallValueInfo.Builder addCallValueInfoBuilder()
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`
    - #### addCallValueInfoBuilder

      ```
      public Response.InternalTransaction.CallValueInfo.Builder addCallValueInfoBuilder(int index)
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`
    - #### getCallValueInfoBuilderList

      ```
      public java.util.List<Response.InternalTransaction.CallValueInfo.Builder> getCallValueInfoBuilderList()
      ```

      `repeated .protocol.InternalTransaction.CallValueInfo callValueInfo = 4;`
    - #### getNote

      ```
      public com.google.protobuf.ByteString getNote()
      ```

      `bytes note = 5;`

      Specified by:
      :   `getNote` in interface `Response.InternalTransactionOrBuilder`

      Returns:
      :   The note.
    - #### setNote

      ```
      public Response.InternalTransaction.Builder setNote(com.google.protobuf.ByteString value)
      ```

      `bytes note = 5;`

      Parameters:
      :   `value` - The note to set.

      Returns:
      :   This builder for chaining.
    - #### clearNote

      ```
      public Response.InternalTransaction.Builder clearNote()
      ```

      `bytes note = 5;`

      Returns:
      :   This builder for chaining.
    - #### getRejected

      ```
      public boolean getRejected()
      ```

      `bool rejected = 6;`

      Specified by:
      :   `getRejected` in interface `Response.InternalTransactionOrBuilder`

      Returns:
      :   The rejected.
    - #### setRejected

      ```
      public Response.InternalTransaction.Builder setRejected(boolean value)
      ```

      `bool rejected = 6;`

      Parameters:
      :   `value` - The rejected to set.

      Returns:
      :   This builder for chaining.
    - #### clearRejected

      ```
      public Response.InternalTransaction.Builder clearRejected()
      ```

      `bool rejected = 6;`

      Returns:
      :   This builder for chaining.
    - #### getExtra

      ```
      public java.lang.String getExtra()
      ```

      `string extra = 7;`

      Specified by:
      :   `getExtra` in interface `Response.InternalTransactionOrBuilder`

      Returns:
      :   The extra.
    - #### getExtraBytes

      ```
      public com.google.protobuf.ByteString getExtraBytes()
      ```

      `string extra = 7;`

      Specified by:
      :   `getExtraBytes` in interface `Response.InternalTransactionOrBuilder`

      Returns:
      :   The bytes for extra.
    - #### setExtra

      ```
      public Response.InternalTransaction.Builder setExtra(java.lang.String value)
      ```

      `string extra = 7;`

      Parameters:
      :   `value` - The extra to set.

      Returns:
      :   This builder for chaining.
    - #### clearExtra

      ```
      public Response.InternalTransaction.Builder clearExtra()
      ```

      `string extra = 7;`

      Returns:
      :   This builder for chaining.
    - #### setExtraBytes

      ```
      public Response.InternalTransaction.Builder setExtraBytes(com.google.protobuf.ByteString value)
      ```

      `string extra = 7;`

      Parameters:
      :   `value` - The bytes for extra to set.

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Response.InternalTransaction.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.Builder>`
    - #### mergeUnknownFields

      ```
      public final Response.InternalTransaction.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Response.InternalTransaction.Builder>`