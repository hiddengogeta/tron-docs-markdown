

org.tron.trident.api

## Interface GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [GrpcAPI.PrivateShieldedTRC20Parameters](../../../../org/tron/trident/api/GrpcAPI.PrivateShieldedTRC20Parameters.html "class in org.tron.trident.api"), [GrpcAPI.PrivateShieldedTRC20Parameters.Builder](../../../../org/tron/trident/api/GrpcAPI.PrivateShieldedTRC20Parameters.Builder.html "class in org.tron.trident.api")

  Enclosing class:
  :   [GrpcAPI](../../../../org/tron/trident/api/GrpcAPI.html "class in org.tron.trident.api")

  ---

    

  ```
  public static interface GrpcAPI.PrivateShieldedTRC20ParametersOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getAsk()` `bytes ask = 1;` |
    | `java.lang.String` | `getFromAmount()` `string from_amount = 4;` |
    | `com.google.protobuf.ByteString` | `getFromAmountBytes()` `string from_amount = 4;` |
    | `com.google.protobuf.ByteString` | `getNsk()` `bytes nsk = 2;` |
    | `com.google.protobuf.ByteString` | `getOvk()` `bytes ovk = 3;` |
    | `GrpcAPI.ReceiveNote` | `getShieldedReceives(int index)` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `int` | `getShieldedReceivesCount()` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `java.util.List<GrpcAPI.ReceiveNote>` | `getShieldedReceivesList()` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `GrpcAPI.ReceiveNoteOrBuilder` | `getShieldedReceivesOrBuilder(int index)` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `java.util.List<? extends GrpcAPI.ReceiveNoteOrBuilder>` | `getShieldedReceivesOrBuilderList()` `repeated .protocol.ReceiveNote shielded_receives = 6;` |
    | `GrpcAPI.SpendNoteTRC20` | `getShieldedSpends(int index)` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `int` | `getShieldedSpendsCount()` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `java.util.List<GrpcAPI.SpendNoteTRC20>` | `getShieldedSpendsList()` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `GrpcAPI.SpendNoteTRC20OrBuilder` | `getShieldedSpendsOrBuilder(int index)` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `java.util.List<? extends GrpcAPI.SpendNoteTRC20OrBuilder>` | `getShieldedSpendsOrBuilderList()` `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;` |
    | `com.google.protobuf.ByteString` | `getShieldedTRC20ContractAddress()` `bytes shielded_TRC20_contract_address = 9;` |
    | `java.lang.String` | `getToAmount()` `string to_amount = 8;` |
    | `com.google.protobuf.ByteString` | `getToAmountBytes()` `string to_amount = 8;` |
    | `com.google.protobuf.ByteString` | `getTransparentToAddress()` `bytes transparent_to_address = 7;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getAsk

      ```
      com.google.protobuf.ByteString getAsk()
      ```

      `bytes ask = 1;`

      Returns:
      :   The ask.
    - #### getNsk

      ```
      com.google.protobuf.ByteString getNsk()
      ```

      `bytes nsk = 2;`

      Returns:
      :   The nsk.
    - #### getOvk

      ```
      com.google.protobuf.ByteString getOvk()
      ```

      `bytes ovk = 3;`

      Returns:
      :   The ovk.
    - #### getFromAmount

      ```
      java.lang.String getFromAmount()
      ```

      `string from_amount = 4;`

      Returns:
      :   The fromAmount.
    - #### getFromAmountBytes

      ```
      com.google.protobuf.ByteString getFromAmountBytes()
      ```

      `string from_amount = 4;`

      Returns:
      :   The bytes for fromAmount.
    - #### getShieldedSpendsList

      ```
      java.util.List<GrpcAPI.SpendNoteTRC20> getShieldedSpendsList()
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`
    - #### getShieldedSpends

      ```
      GrpcAPI.SpendNoteTRC20 getShieldedSpends(int index)
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`
    - #### getShieldedSpendsCount

      ```
      int getShieldedSpendsCount()
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`
    - #### getShieldedSpendsOrBuilderList

      ```
      java.util.List<? extends GrpcAPI.SpendNoteTRC20OrBuilder> getShieldedSpendsOrBuilderList()
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`
    - #### getShieldedSpendsOrBuilder

      ```
      GrpcAPI.SpendNoteTRC20OrBuilder getShieldedSpendsOrBuilder(int index)
      ```

      `repeated .protocol.SpendNoteTRC20 shielded_spends = 5;`
    - #### getShieldedReceivesList

      ```
      java.util.List<GrpcAPI.ReceiveNote> getShieldedReceivesList()
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`
    - #### getShieldedReceives

      ```
      GrpcAPI.ReceiveNote getShieldedReceives(int index)
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`
    - #### getShieldedReceivesCount

      ```
      int getShieldedReceivesCount()
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`
    - #### getShieldedReceivesOrBuilderList

      ```
      java.util.List<? extends GrpcAPI.ReceiveNoteOrBuilder> getShieldedReceivesOrBuilderList()
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`
    - #### getShieldedReceivesOrBuilder

      ```
      GrpcAPI.ReceiveNoteOrBuilder getShieldedReceivesOrBuilder(int index)
      ```

      `repeated .protocol.ReceiveNote shielded_receives = 6;`
    - #### getTransparentToAddress

      ```
      com.google.protobuf.ByteString getTransparentToAddress()
      ```

      `bytes transparent_to_address = 7;`

      Returns:
      :   The transparentToAddress.
    - #### getToAmount

      ```
      java.lang.String getToAmount()
      ```

      `string to_amount = 8;`

      Returns:
      :   The toAmount.
    - #### getToAmountBytes

      ```
      com.google.protobuf.ByteString getToAmountBytes()
      ```

      `string to_amount = 8;`

      Returns:
      :   The bytes for toAmount.
    - #### getShieldedTRC20ContractAddress

      ```
      com.google.protobuf.ByteString getShieldedTRC20ContractAddress()
      ```

      `bytes shielded_TRC20_contract_address = 9;`

      Returns:
      :   The shieldedTRC20ContractAddress.