

org.tron.trident.proto

## Class Common.SmartContract.ABI.Entry.Param.Builder

* java.lang.Object
* + com.google.protobuf.AbstractMessageLite.Builder
  + - com.google.protobuf.AbstractMessage.Builder<BuilderT>
    - * com.google.protobuf.GeneratedMessageV3.Builder<[Common.SmartContract.ABI.Entry.Param.Builder](../../../../org/tron/trident/proto/Common.SmartContract.ABI.Entry.Param.Builder.html "class in org.tron.trident.proto")>
      * + org.tron.trident.proto.Common.SmartContract.ABI.Entry.Param.Builder

* All Implemented Interfaces:
  :   com.google.protobuf.Message.Builder, com.google.protobuf.MessageLite.Builder, com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder, java.lang.Cloneable, [Common.SmartContract.ABI.Entry.ParamOrBuilder](../../../../org/tron/trident/proto/Common.SmartContract.ABI.Entry.ParamOrBuilder.html "interface in org.tron.trident.proto")

  Enclosing class:
  :   [Common.SmartContract.ABI.Entry.Param](../../../../org/tron/trident/proto/Common.SmartContract.ABI.Entry.Param.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static final class Common.SmartContract.ABI.Entry.Param.Builder
  extends com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Param.Builder>
  implements Common.SmartContract.ABI.Entry.ParamOrBuilder
  ```

  Protobuf type `protocol.SmartContract.ABI.Entry.Param`

* + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Common.SmartContract.ABI.Entry.Param` | `build()` |
    | `Common.SmartContract.ABI.Entry.Param` | `buildPartial()` |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `clear()` |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `clearField(com.google.protobuf.Descriptors.FieldDescriptor field)` |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `clearIndexed()` `bool indexed = 1;` |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `clearName()` `string name = 2;` |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)` |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `clearType()` SolidityType type = 3; |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `clone()` |
    | `Common.SmartContract.ABI.Entry.Param` | `getDefaultInstanceForType()` |
    | `static com.google.protobuf.Descriptors.Descriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.Descriptor` | `getDescriptorForType()` |
    | `boolean` | `getIndexed()` `bool indexed = 1;` |
    | `java.lang.String` | `getName()` `string name = 2;` |
    | `com.google.protobuf.ByteString` | `getNameBytes()` `string name = 2;` |
    | `java.lang.String` | `getType()` SolidityType type = 3; |
    | `com.google.protobuf.ByteString` | `getTypeBytes()` SolidityType type = 3; |
    | `protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable` | `internalGetFieldAccessorTable()` |
    | `boolean` | `isInitialized()` |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `mergeFrom(com.google.protobuf.CodedInputStream input, com.google.protobuf.ExtensionRegistryLite extensionRegistry)` |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `mergeFrom(Common.SmartContract.ABI.Entry.Param other)` |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `mergeFrom(com.google.protobuf.Message other)` |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `setField(com.google.protobuf.Descriptors.FieldDescriptor field, java.lang.Object value)` |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `setIndexed(boolean value)` `bool indexed = 1;` |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `setName(java.lang.String value)` `string name = 2;` |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `setNameBytes(com.google.protobuf.ByteString value)` `string name = 2;` |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field, int index, java.lang.Object value)` |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `setType(java.lang.String value)` SolidityType type = 3; |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `setTypeBytes(com.google.protobuf.ByteString value)` SolidityType type = 3; |
    | `Common.SmartContract.ABI.Entry.Param.Builder` | `setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)` |

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
      :   `internalGetFieldAccessorTable` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Param.Builder>`
    - #### clear

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder clear()
      ```

      Specified by:
      :   `clear` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clear` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clear` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Param.Builder>`
    - #### getDescriptorForType

      ```
      public com.google.protobuf.Descriptors.Descriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.MessageOrBuilder`

      Overrides:
      :   `getDescriptorForType` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Param.Builder>`
    - #### getDefaultInstanceForType

      ```
      public Common.SmartContract.ABI.Entry.Param getDefaultInstanceForType()
      ```

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Specified by:
      :   `getDefaultInstanceForType` in interface `com.google.protobuf.MessageOrBuilder`
    - #### build

      ```
      public Common.SmartContract.ABI.Entry.Param build()
      ```

      Specified by:
      :   `build` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `build` in interface `com.google.protobuf.MessageLite.Builder`
    - #### buildPartial

      ```
      public Common.SmartContract.ABI.Entry.Param buildPartial()
      ```

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `buildPartial` in interface `com.google.protobuf.MessageLite.Builder`
    - #### clone

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder clone()
      ```

      Specified by:
      :   `clone` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `clone` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `clone` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Param.Builder>`
    - #### setField

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder setField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                   java.lang.Object value)
      ```

      Specified by:
      :   `setField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Param.Builder>`
    - #### clearField

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder clearField(com.google.protobuf.Descriptors.FieldDescriptor field)
      ```

      Specified by:
      :   `clearField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Param.Builder>`
    - #### clearOneof

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder clearOneof(com.google.protobuf.Descriptors.OneofDescriptor oneof)
      ```

      Specified by:
      :   `clearOneof` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `clearOneof` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Param.Builder>`
    - #### setRepeatedField

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder setRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                           int index,
                                                                           java.lang.Object value)
      ```

      Specified by:
      :   `setRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Param.Builder>`
    - #### addRepeatedField

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder addRepeatedField(com.google.protobuf.Descriptors.FieldDescriptor field,
                                                                           java.lang.Object value)
      ```

      Specified by:
      :   `addRepeatedField` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `addRepeatedField` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Param.Builder>`
    - #### mergeFrom

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder mergeFrom(com.google.protobuf.Message other)
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Common.SmartContract.ABI.Entry.Param.Builder>`
    - #### mergeFrom

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder mergeFrom(Common.SmartContract.ABI.Entry.Param other)
      ```
    - #### isInitialized

      ```
      public final boolean isInitialized()
      ```

      Specified by:
      :   `isInitialized` in interface `com.google.protobuf.MessageLiteOrBuilder`

      Overrides:
      :   `isInitialized` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Param.Builder>`
    - #### mergeFrom

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder mergeFrom(com.google.protobuf.CodedInputStream input,
                                                                    com.google.protobuf.ExtensionRegistryLite extensionRegistry)
                                                             throws java.io.IOException
      ```

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.Message.Builder`

      Specified by:
      :   `mergeFrom` in interface `com.google.protobuf.MessageLite.Builder`

      Overrides:
      :   `mergeFrom` in class `com.google.protobuf.AbstractMessage.Builder<Common.SmartContract.ABI.Entry.Param.Builder>`

      Throws:
      :   `java.io.IOException`
    - #### getIndexed

      ```
      public boolean getIndexed()
      ```

      `bool indexed = 1;`

      Specified by:
      :   `getIndexed` in interface `Common.SmartContract.ABI.Entry.ParamOrBuilder`

      Returns:
      :   The indexed.
    - #### setIndexed

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder setIndexed(boolean value)
      ```

      `bool indexed = 1;`

      Parameters:
      :   `value` - The indexed to set.

      Returns:
      :   This builder for chaining.
    - #### clearIndexed

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder clearIndexed()
      ```

      `bool indexed = 1;`

      Returns:
      :   This builder for chaining.
    - #### getName

      ```
      public java.lang.String getName()
      ```

      `string name = 2;`

      Specified by:
      :   `getName` in interface `Common.SmartContract.ABI.Entry.ParamOrBuilder`

      Returns:
      :   The name.
    - #### getNameBytes

      ```
      public com.google.protobuf.ByteString getNameBytes()
      ```

      `string name = 2;`

      Specified by:
      :   `getNameBytes` in interface `Common.SmartContract.ABI.Entry.ParamOrBuilder`

      Returns:
      :   The bytes for name.
    - #### setName

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder setName(java.lang.String value)
      ```

      `string name = 2;`

      Parameters:
      :   `value` - The name to set.

      Returns:
      :   This builder for chaining.
    - #### clearName

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder clearName()
      ```

      `string name = 2;`

      Returns:
      :   This builder for chaining.
    - #### setNameBytes

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder setNameBytes(com.google.protobuf.ByteString value)
      ```

      `string name = 2;`

      Parameters:
      :   `value` - The bytes for name to set.

      Returns:
      :   This builder for chaining.
    - #### getType

      ```
      public java.lang.String getType()
      ```

      ```
       SolidityType type = 3;
      ```

      `string type = 3;`

      Specified by:
      :   `getType` in interface `Common.SmartContract.ABI.Entry.ParamOrBuilder`

      Returns:
      :   The type.
    - #### getTypeBytes

      ```
      public com.google.protobuf.ByteString getTypeBytes()
      ```

      ```
       SolidityType type = 3;
      ```

      `string type = 3;`

      Specified by:
      :   `getTypeBytes` in interface `Common.SmartContract.ABI.Entry.ParamOrBuilder`

      Returns:
      :   The bytes for type.
    - #### setType

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder setType(java.lang.String value)
      ```

      ```
       SolidityType type = 3;
      ```

      `string type = 3;`

      Parameters:
      :   `value` - The type to set.

      Returns:
      :   This builder for chaining.
    - #### clearType

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder clearType()
      ```

      ```
       SolidityType type = 3;
      ```

      `string type = 3;`

      Returns:
      :   This builder for chaining.
    - #### setTypeBytes

      ```
      public Common.SmartContract.ABI.Entry.Param.Builder setTypeBytes(com.google.protobuf.ByteString value)
      ```

      ```
       SolidityType type = 3;
      ```

      `string type = 3;`

      Parameters:
      :   `value` - The bytes for type to set.

      Returns:
      :   This builder for chaining.
    - #### setUnknownFields

      ```
      public final Common.SmartContract.ABI.Entry.Param.Builder setUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `setUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `setUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Param.Builder>`
    - #### mergeUnknownFields

      ```
      public final Common.SmartContract.ABI.Entry.Param.Builder mergeUnknownFields(com.google.protobuf.UnknownFieldSet unknownFields)
      ```

      Specified by:
      :   `mergeUnknownFields` in interface `com.google.protobuf.Message.Builder`

      Overrides:
      :   `mergeUnknownFields` in class `com.google.protobuf.GeneratedMessageV3.Builder<Common.SmartContract.ABI.Entry.Param.Builder>`