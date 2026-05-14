

org.tron.trident.proto

## Interface Common.SmartContract.ABI.Entry.ParamOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Common.SmartContract.ABI.Entry.Param](../../../../org/tron/trident/proto/Common.SmartContract.ABI.Entry.Param.html "class in org.tron.trident.proto"), [Common.SmartContract.ABI.Entry.Param.Builder](../../../../org/tron/trident/proto/Common.SmartContract.ABI.Entry.Param.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Common.SmartContract.ABI.Entry](../../../../org/tron/trident/proto/Common.SmartContract.ABI.Entry.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Common.SmartContract.ABI.Entry.ParamOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `boolean` | `getIndexed()` `bool indexed = 1;` |
    | `java.lang.String` | `getName()` `string name = 2;` |
    | `com.google.protobuf.ByteString` | `getNameBytes()` `string name = 2;` |
    | `java.lang.String` | `getType()` SolidityType type = 3; |
    | `com.google.protobuf.ByteString` | `getTypeBytes()` SolidityType type = 3; |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getIndexed

      ```
      boolean getIndexed()
      ```

      `bool indexed = 1;`

      Returns:
      :   The indexed.
    - #### getName

      ```
      java.lang.String getName()
      ```

      `string name = 2;`

      Returns:
      :   The name.
    - #### getNameBytes

      ```
      com.google.protobuf.ByteString getNameBytes()
      ```

      `string name = 2;`

      Returns:
      :   The bytes for name.
    - #### getType

      ```
      java.lang.String getType()
      ```

      ```
       SolidityType type = 3;
      ```

      `string type = 3;`

      Returns:
      :   The type.
    - #### getTypeBytes

      ```
      com.google.protobuf.ByteString getTypeBytes()
      ```

      ```
       SolidityType type = 3;
      ```

      `string type = 3;`

      Returns:
      :   The bytes for type.