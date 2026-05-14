

org.tron.trident.proto

## Interface Chain.Transaction.ResultOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Chain.Transaction.Result](../../../../org/tron/trident/proto/Chain.Transaction.Result.html "class in org.tron.trident.proto"), [Chain.Transaction.Result.Builder](../../../../org/tron/trident/proto/Chain.Transaction.Result.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Chain.Transaction](../../../../org/tron/trident/proto/Chain.Transaction.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Chain.Transaction.ResultOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `boolean` | `containsCancelUnfreezeV2Amount(java.lang.String key)` `map<string, int64> cancel_unfreezeV2_amount = 28;` |
    | `java.lang.String` | `getAssetIssueID()` `string assetIssueID = 14;` |
    | `com.google.protobuf.ByteString` | `getAssetIssueIDBytes()` `string assetIssueID = 14;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getCancelUnfreezeV2Amount()` Deprecated. |
    | `int` | `getCancelUnfreezeV2AmountCount()` `map<string, int64> cancel_unfreezeV2_amount = 28;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getCancelUnfreezeV2AmountMap()` `map<string, int64> cancel_unfreezeV2_amount = 28;` |
    | `long` | `getCancelUnfreezeV2AmountOrDefault(java.lang.String key, long defaultValue)` `map<string, int64> cancel_unfreezeV2_amount = 28;` |
    | `long` | `getCancelUnfreezeV2AmountOrThrow(java.lang.String key)` `map<string, int64> cancel_unfreezeV2_amount = 28;` |
    | `Chain.Transaction.Result.contractResult` | `getContractRet()` `.protocol.Transaction.Result.contractResult contractRet = 3;` |
    | `int` | `getContractRetValue()` `.protocol.Transaction.Result.contractResult contractRet = 3;` |
    | `long` | `getExchangeId()` `int64 exchange_id = 21;` |
    | `long` | `getExchangeInjectAnotherAmount()` `int64 exchange_inject_another_amount = 19;` |
    | `long` | `getExchangeReceivedAmount()` `int64 exchange_received_amount = 18;` |
    | `long` | `getExchangeWithdrawAnotherAmount()` `int64 exchange_withdraw_another_amount = 20;` |
    | `long` | `getFee()` `int64 fee = 1;` |
    | `Common.MarketOrderDetail` | `getOrderDetails(int index)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `int` | `getOrderDetailsCount()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `java.util.List<Common.MarketOrderDetail>` | `getOrderDetailsList()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Common.MarketOrderDetailOrBuilder` | `getOrderDetailsOrBuilder(int index)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `java.util.List<? extends Common.MarketOrderDetailOrBuilder>` | `getOrderDetailsOrBuilderList()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `com.google.protobuf.ByteString` | `getOrderId()` `bytes orderId = 25;` |
    | `Chain.Transaction.Result.code` | `getRet()` `.protocol.Transaction.Result.code ret = 2;` |
    | `int` | `getRetValue()` `.protocol.Transaction.Result.code ret = 2;` |
    | `long` | `getShieldedTransactionFee()` `int64 shielded_transaction_fee = 22;` |
    | `long` | `getUnfreezeAmount()` `int64 unfreeze_amount = 16;` |
    | `long` | `getWithdrawAmount()` `int64 withdraw_amount = 15;` |
    | `long` | `getWithdrawExpireAmount()` `int64 withdraw_expire_amount = 27;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getFee

      ```
      long getFee()
      ```

      `int64 fee = 1;`

      Returns:
      :   The fee.
    - #### getRetValue

      ```
      int getRetValue()
      ```

      `.protocol.Transaction.Result.code ret = 2;`

      Returns:
      :   The enum numeric value on the wire for ret.
    - #### getRet

      ```
      Chain.Transaction.Result.code getRet()
      ```

      `.protocol.Transaction.Result.code ret = 2;`

      Returns:
      :   The ret.
    - #### getContractRetValue

      ```
      int getContractRetValue()
      ```

      `.protocol.Transaction.Result.contractResult contractRet = 3;`

      Returns:
      :   The enum numeric value on the wire for contractRet.
    - #### getContractRet

      ```
      Chain.Transaction.Result.contractResult getContractRet()
      ```

      `.protocol.Transaction.Result.contractResult contractRet = 3;`

      Returns:
      :   The contractRet.
    - #### getAssetIssueID

      ```
      java.lang.String getAssetIssueID()
      ```

      `string assetIssueID = 14;`

      Returns:
      :   The assetIssueID.
    - #### getAssetIssueIDBytes

      ```
      com.google.protobuf.ByteString getAssetIssueIDBytes()
      ```

      `string assetIssueID = 14;`

      Returns:
      :   The bytes for assetIssueID.
    - #### getWithdrawAmount

      ```
      long getWithdrawAmount()
      ```

      `int64 withdraw_amount = 15;`

      Returns:
      :   The withdrawAmount.
    - #### getUnfreezeAmount

      ```
      long getUnfreezeAmount()
      ```

      `int64 unfreeze_amount = 16;`

      Returns:
      :   The unfreezeAmount.
    - #### getExchangeReceivedAmount

      ```
      long getExchangeReceivedAmount()
      ```

      `int64 exchange_received_amount = 18;`

      Returns:
      :   The exchangeReceivedAmount.
    - #### getExchangeInjectAnotherAmount

      ```
      long getExchangeInjectAnotherAmount()
      ```

      `int64 exchange_inject_another_amount = 19;`

      Returns:
      :   The exchangeInjectAnotherAmount.
    - #### getExchangeWithdrawAnotherAmount

      ```
      long getExchangeWithdrawAnotherAmount()
      ```

      `int64 exchange_withdraw_another_amount = 20;`

      Returns:
      :   The exchangeWithdrawAnotherAmount.
    - #### getExchangeId

      ```
      long getExchangeId()
      ```

      `int64 exchange_id = 21;`

      Returns:
      :   The exchangeId.
    - #### getShieldedTransactionFee

      ```
      long getShieldedTransactionFee()
      ```

      `int64 shielded_transaction_fee = 22;`

      Returns:
      :   The shieldedTransactionFee.
    - #### getOrderId

      ```
      com.google.protobuf.ByteString getOrderId()
      ```

      `bytes orderId = 25;`

      Returns:
      :   The orderId.
    - #### getOrderDetailsList

      ```
      java.util.List<Common.MarketOrderDetail> getOrderDetailsList()
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### getOrderDetails

      ```
      Common.MarketOrderDetail getOrderDetails(int index)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### getOrderDetailsCount

      ```
      int getOrderDetailsCount()
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### getOrderDetailsOrBuilderList

      ```
      java.util.List<? extends Common.MarketOrderDetailOrBuilder> getOrderDetailsOrBuilderList()
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### getOrderDetailsOrBuilder

      ```
      Common.MarketOrderDetailOrBuilder getOrderDetailsOrBuilder(int index)
      ```

      `repeated .protocol.MarketOrderDetail orderDetails = 26;`
    - #### getWithdrawExpireAmount

      ```
      long getWithdrawExpireAmount()
      ```

      `int64 withdraw_expire_amount = 27;`

      Returns:
      :   The withdrawExpireAmount.
    - #### getCancelUnfreezeV2AmountCount

      ```
      int getCancelUnfreezeV2AmountCount()
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 28;`
    - #### containsCancelUnfreezeV2Amount

      ```
      boolean containsCancelUnfreezeV2Amount(java.lang.String key)
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 28;`
    - #### getCancelUnfreezeV2Amount

      ```
      @Deprecated
      java.util.Map<java.lang.String,java.lang.Long> getCancelUnfreezeV2Amount()
      ```

      Deprecated.

      Use [`getCancelUnfreezeV2AmountMap()`](../../../../org/tron/trident/proto/Chain.Transaction.ResultOrBuilder.html#getCancelUnfreezeV2AmountMap--) instead.
    - #### getCancelUnfreezeV2AmountMap

      ```
      java.util.Map<java.lang.String,java.lang.Long> getCancelUnfreezeV2AmountMap()
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 28;`
    - #### getCancelUnfreezeV2AmountOrDefault

      ```
      long getCancelUnfreezeV2AmountOrDefault(java.lang.String key,
                                              long defaultValue)
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 28;`
    - #### getCancelUnfreezeV2AmountOrThrow

      ```
      long getCancelUnfreezeV2AmountOrThrow(java.lang.String key)
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 28;`