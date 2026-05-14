

org.tron.trident.proto

## Interface Chain.Transaction.ContractOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Chain.Transaction.Contract](../../../../org/tron/trident/proto/Chain.Transaction.Contract.html "class in org.tron.trident.proto"), [Chain.Transaction.Contract.Builder](../../../../org/tron/trident/proto/Chain.Transaction.Contract.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Chain.Transaction](../../../../org/tron/trident/proto/Chain.Transaction.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Chain.Transaction.ContractOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getContractName()` `bytes ContractName = 4;` |
    | `com.google.protobuf.Any` | `getParameter()` `.google.protobuf.Any parameter = 2;` |
    | `com.google.protobuf.AnyOrBuilder` | `getParameterOrBuilder()` `.google.protobuf.Any parameter = 2;` |
    | `int` | `getPermissionId()` `int32 Permission_id = 5;` |
    | `com.google.protobuf.ByteString` | `getProvider()` `bytes provider = 3;` |
    | `Chain.Transaction.Contract.ContractType` | `getType()` `.protocol.Transaction.Contract.ContractType type = 1;` |
    | `int` | `getTypeValue()` `.protocol.Transaction.Contract.ContractType type = 1;` |
    | `boolean` | `hasParameter()` `.google.protobuf.Any parameter = 2;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getTypeValue

      ```
      int getTypeValue()
      ```

      `.protocol.Transaction.Contract.ContractType type = 1;`

      Returns:
      :   The enum numeric value on the wire for type.
    - #### getType

      ```
      Chain.Transaction.Contract.ContractType getType()
      ```

      `.protocol.Transaction.Contract.ContractType type = 1;`

      Returns:
      :   The type.
    - #### hasParameter

      ```
      boolean hasParameter()
      ```

      `.google.protobuf.Any parameter = 2;`

      Returns:
      :   Whether the parameter field is set.
    - #### getParameter

      ```
      com.google.protobuf.Any getParameter()
      ```

      `.google.protobuf.Any parameter = 2;`

      Returns:
      :   The parameter.
    - #### getParameterOrBuilder

      ```
      com.google.protobuf.AnyOrBuilder getParameterOrBuilder()
      ```

      `.google.protobuf.Any parameter = 2;`
    - #### getProvider

      ```
      com.google.protobuf.ByteString getProvider()
      ```

      `bytes provider = 3;`

      Returns:
      :   The provider.
    - #### getContractName

      ```
      com.google.protobuf.ByteString getContractName()
      ```

      `bytes ContractName = 4;`

      Returns:
      :   The contractName.
    - #### getPermissionId

      ```
      int getPermissionId()
      ```

      `int32 Permission_id = 5;`

      Returns:
      :   The permissionId.