

org.tron.trident.api

## Interface GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.ShieldedTRC20TriggerContractParameters](../../../../org/tron/trident/api/GrpcAPI.ShieldedTRC20TriggerContractParameters.html "class in org.tron.trident.api"), [GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder](../../../../org/tron/trident/api/GrpcAPI.ShieldedTRC20TriggerContractParameters.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.ShieldedTRC20TriggerContractParametersOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `java.lang.String` | `getAmount()` `string amount = 3;` |
    | `com.google.protobuf.ByteString` | `getAmountBytes()` `string amount = 3;` |
    | `GrpcAPI.ShieldedTRC20Parameters` | `getShieldedTRC20Parameters()` `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;` |
    | `GrpcAPI.ShieldedTRC20ParametersOrBuilder` | `getShieldedTRC20ParametersOrBuilder()` `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;` |
    | `GrpcAPI.BytesMessage` | `getSpendAuthoritySignature(int index)` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `int` | `getSpendAuthoritySignatureCount()` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `java.util.List<GrpcAPI.BytesMessage>` | `getSpendAuthoritySignatureList()` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `GrpcAPI.BytesMessageOrBuilder` | `getSpendAuthoritySignatureOrBuilder(int index)` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `java.util.List<? extends GrpcAPI.BytesMessageOrBuilder>` | `getSpendAuthoritySignatureOrBuilderList()` `repeated .protocol.BytesMessage spend_authority_signature = 2;` |
    | `com.google.protobuf.ByteString` | `getTransparentToAddress()` `bytes transparent_to_address = 4;` |
    | `boolean` | `hasShieldedTRC20Parameters()` `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### hasShieldedTRC20Parameters

      ```
      boolean hasShieldedTRC20Parameters()
      ```

      `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;`

      Returns:
      :   Whether the shieldedTRC20Parameters field is set.
    - #### getShieldedTRC20Parameters

      ```
      GrpcAPI.ShieldedTRC20Parameters getShieldedTRC20Parameters()
      ```

      `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;`

      Returns:
      :   The shieldedTRC20Parameters.
    - #### getShieldedTRC20ParametersOrBuilder

      ```
      GrpcAPI.ShieldedTRC20ParametersOrBuilder getShieldedTRC20ParametersOrBuilder()
      ```

      `.protocol.ShieldedTRC20Parameters shielded_TRC20_Parameters = 1;`
    - #### getSpendAuthoritySignatureList

      ```
      java.util.List<GrpcAPI.BytesMessage> getSpendAuthoritySignatureList()
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`
    - #### getSpendAuthoritySignature

      ```
      GrpcAPI.BytesMessage getSpendAuthoritySignature(int index)
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`
    - #### getSpendAuthoritySignatureCount

      ```
      int getSpendAuthoritySignatureCount()
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`
    - #### getSpendAuthoritySignatureOrBuilderList

      ```
      java.util.List<? extends GrpcAPI.BytesMessageOrBuilder> getSpendAuthoritySignatureOrBuilderList()
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`
    - #### getSpendAuthoritySignatureOrBuilder

      ```
      GrpcAPI.BytesMessageOrBuilder getSpendAuthoritySignatureOrBuilder(int index)
      ```

      `repeated .protocol.BytesMessage spend_authority_signature = 2;`
    - #### getAmount

      ```
      java.lang.String getAmount()
      ```

      `string amount = 3;`

      Returns:
      :   The amount.
    - #### getAmountBytes

      ```
      com.google.protobuf.ByteString getAmountBytes()
      ```

      `string amount = 3;`

      Returns:
      :   The bytes for amount.
    - #### getTransparentToAddress

      ```
      com.google.protobuf.ByteString getTransparentToAddress()
      ```

      `bytes transparent_to_address = 4;`

      Returns:
      :   The transparentToAddress.