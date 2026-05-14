

org.tron.trident.api

## Interface GrpcAPI.ShieldedTRC20ParametersOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.ShieldedTRC20Parameters](../../../../org/tron/trident/api/GrpcAPI.ShieldedTRC20Parameters.html "class in org.tron.trident.api"), [GrpcAPI.ShieldedTRC20Parameters.Builder](../../../../org/tron/trident/api/GrpcAPI.ShieldedTRC20Parameters.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.ShieldedTRC20ParametersOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getBindingSignature()` `bytes binding_signature = 3;` |
    | `com.google.protobuf.ByteString` | `getMessageHash()` `bytes message_hash = 4;` |
    | `java.lang.String` | `getParameterType()` `string parameter_type = 6;` |
    | `com.google.protobuf.ByteString` | `getParameterTypeBytes()` `string parameter_type = 6;` |
    | `GrpcAPI.ReceiveDescription` | `getReceiveDescription(int index)` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `int` | `getReceiveDescriptionCount()` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `java.util.List<GrpcAPI.ReceiveDescription>` | `getReceiveDescriptionList()` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `GrpcAPI.ReceiveDescriptionOrBuilder` | `getReceiveDescriptionOrBuilder(int index)` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `java.util.List<? extends GrpcAPI.ReceiveDescriptionOrBuilder>` | `getReceiveDescriptionOrBuilderList()` `repeated .protocol.ReceiveDescription receive_description = 2;` |
    | `GrpcAPI.SpendDescription` | `getSpendDescription(int index)` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `int` | `getSpendDescriptionCount()` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `java.util.List<GrpcAPI.SpendDescription>` | `getSpendDescriptionList()` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `GrpcAPI.SpendDescriptionOrBuilder` | `getSpendDescriptionOrBuilder(int index)` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `java.util.List<? extends GrpcAPI.SpendDescriptionOrBuilder>` | `getSpendDescriptionOrBuilderList()` `repeated .protocol.SpendDescription spend_description = 1;` |
    | `java.lang.String` | `getTriggerContractInput()` `string trigger_contract_input = 5;` |
    | `com.google.protobuf.ByteString` | `getTriggerContractInputBytes()` `string trigger_contract_input = 5;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getSpendDescriptionList

      ```
      java.util.List<GrpcAPI.SpendDescription> getSpendDescriptionList()
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`
    - #### getSpendDescription

      ```
      GrpcAPI.SpendDescription getSpendDescription(int index)
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`
    - #### getSpendDescriptionCount

      ```
      int getSpendDescriptionCount()
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`
    - #### getSpendDescriptionOrBuilderList

      ```
      java.util.List<? extends GrpcAPI.SpendDescriptionOrBuilder> getSpendDescriptionOrBuilderList()
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`
    - #### getSpendDescriptionOrBuilder

      ```
      GrpcAPI.SpendDescriptionOrBuilder getSpendDescriptionOrBuilder(int index)
      ```

      `repeated .protocol.SpendDescription spend_description = 1;`
    - #### getReceiveDescriptionList

      ```
      java.util.List<GrpcAPI.ReceiveDescription> getReceiveDescriptionList()
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`
    - #### getReceiveDescription

      ```
      GrpcAPI.ReceiveDescription getReceiveDescription(int index)
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`
    - #### getReceiveDescriptionCount

      ```
      int getReceiveDescriptionCount()
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`
    - #### getReceiveDescriptionOrBuilderList

      ```
      java.util.List<? extends GrpcAPI.ReceiveDescriptionOrBuilder> getReceiveDescriptionOrBuilderList()
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`
    - #### getReceiveDescriptionOrBuilder

      ```
      GrpcAPI.ReceiveDescriptionOrBuilder getReceiveDescriptionOrBuilder(int index)
      ```

      `repeated .protocol.ReceiveDescription receive_description = 2;`
    - #### getBindingSignature

      ```
      com.google.protobuf.ByteString getBindingSignature()
      ```

      `bytes binding_signature = 3;`

      Returns:
      :   The bindingSignature.
    - #### getMessageHash

      ```
      com.google.protobuf.ByteString getMessageHash()
      ```

      `bytes message_hash = 4;`

      Returns:
      :   The messageHash.
    - #### getTriggerContractInput

      ```
      java.lang.String getTriggerContractInput()
      ```

      `string trigger_contract_input = 5;`

      Returns:
      :   The triggerContractInput.
    - #### getTriggerContractInputBytes

      ```
      com.google.protobuf.ByteString getTriggerContractInputBytes()
      ```

      `string trigger_contract_input = 5;`

      Returns:
      :   The bytes for triggerContractInput.
    - #### getParameterType

      ```
      java.lang.String getParameterType()
      ```

      `string parameter_type = 6;`

      Returns:
      :   The parameterType.
    - #### getParameterTypeBytes

      ```
      com.google.protobuf.ByteString getParameterTypeBytes()
      ```

      `string parameter_type = 6;`

      Returns:
      :   The bytes for parameterType.