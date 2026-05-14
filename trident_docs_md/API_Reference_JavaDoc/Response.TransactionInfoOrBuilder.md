

org.tron.trident.proto

## Interface Response.TransactionInfoOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.TransactionInfo](../../../../org/tron/trident/proto/Response.TransactionInfo.html "class in org.tron.trident.proto"), [Response.TransactionInfo.Builder](../../../../org/tron/trident/proto/Response.TransactionInfo.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.TransactionInfoOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `boolean` | `containsCancelUnfreezeV2Amount(java.lang.String key)` `map<string, int64> cancel_unfreezeV2_amount = 29;` |
    | `java.lang.String` | `getAssetIssueID()` `string assetIssueID = 14;` |
    | `com.google.protobuf.ByteString` | `getAssetIssueIDBytes()` `string assetIssueID = 14;` |
    | `long` | `getBlockNumber()` `int64 blockNumber = 3;` |
    | `long` | `getBlockTimeStamp()` `int64 blockTimeStamp = 4;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getCancelUnfreezeV2Amount()` Deprecated. |
    | `int` | `getCancelUnfreezeV2AmountCount()` `map<string, int64> cancel_unfreezeV2_amount = 29;` |
    | `java.util.Map<java.lang.String,java.lang.Long>` | `getCancelUnfreezeV2AmountMap()` `map<string, int64> cancel_unfreezeV2_amount = 29;` |
    | `long` | `getCancelUnfreezeV2AmountOrDefault(java.lang.String key, long defaultValue)` `map<string, int64> cancel_unfreezeV2_amount = 29;` |
    | `long` | `getCancelUnfreezeV2AmountOrThrow(java.lang.String key)` `map<string, int64> cancel_unfreezeV2_amount = 29;` |
    | `com.google.protobuf.ByteString` | `getContractAddress()` `bytes contract_address = 6;` |
    | `com.google.protobuf.ByteString` | `getContractResult(int index)` `repeated bytes contractResult = 5;` |
    | `int` | `getContractResultCount()` `repeated bytes contractResult = 5;` |
    | `java.util.List<com.google.protobuf.ByteString>` | `getContractResultList()` `repeated bytes contractResult = 5;` |
    | `long` | `getExchangeId()` `int64 exchange_id = 21;` |
    | `long` | `getExchangeInjectAnotherAmount()` `int64 exchange_inject_another_amount = 19;` |
    | `long` | `getExchangeReceivedAmount()` `int64 exchange_received_amount = 18;` |
    | `long` | `getExchangeWithdrawAnotherAmount()` `int64 exchange_withdraw_another_amount = 20;` |
    | `long` | `getFee()` `int64 fee = 2;` |
    | `com.google.protobuf.ByteString` | `getId()` `bytes id = 1;` |
    | `Response.InternalTransaction` | `getInternalTransactions(int index)` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `int` | `getInternalTransactionsCount()` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `java.util.List<Response.InternalTransaction>` | `getInternalTransactionsList()` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `Response.InternalTransactionOrBuilder` | `getInternalTransactionsOrBuilder(int index)` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `java.util.List<? extends Response.InternalTransactionOrBuilder>` | `getInternalTransactionsOrBuilderList()` `repeated .protocol.InternalTransaction internal_transactions = 17;` |
    | `Response.TransactionInfo.Log` | `getLog(int index)` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `int` | `getLogCount()` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `java.util.List<Response.TransactionInfo.Log>` | `getLogList()` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `Response.TransactionInfo.LogOrBuilder` | `getLogOrBuilder(int index)` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `java.util.List<? extends Response.TransactionInfo.LogOrBuilder>` | `getLogOrBuilderList()` `repeated .protocol.TransactionInfo.Log log = 8;` |
    | `Common.MarketOrderDetail` | `getOrderDetails(int index)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `int` | `getOrderDetailsCount()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `java.util.List<Common.MarketOrderDetail>` | `getOrderDetailsList()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `Common.MarketOrderDetailOrBuilder` | `getOrderDetailsOrBuilder(int index)` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `java.util.List<? extends Common.MarketOrderDetailOrBuilder>` | `getOrderDetailsOrBuilderList()` `repeated .protocol.MarketOrderDetail orderDetails = 26;` |
    | `com.google.protobuf.ByteString` | `getOrderId()` `bytes orderId = 25;` |
    | `long` | `getPackingFee()` `int64 packingFee = 27;` |
    | `Response.ResourceReceipt` | `getReceipt()` `.protocol.ResourceReceipt receipt = 7;` |
    | `Response.ResourceReceiptOrBuilder` | `getReceiptOrBuilder()` `.protocol.ResourceReceipt receipt = 7;` |
    | `com.google.protobuf.ByteString` | `getResMessage()` `bytes resMessage = 10;` |
    | `Response.TransactionInfo.code` | `getResult()` `.protocol.TransactionInfo.code result = 9;` |
    | `int` | `getResultValue()` `.protocol.TransactionInfo.code result = 9;` |
    | `long` | `getShieldedTransactionFee()` `int64 shielded_transaction_fee = 22;` |
    | `long` | `getUnfreezeAmount()` `int64 unfreeze_amount = 16;` |
    | `long` | `getWithdrawAmount()` `int64 withdraw_amount = 15;` |
    | `long` | `getWithdrawExpireAmount()` `int64 withdraw_expire_amount = 28;` |
    | `boolean` | `hasReceipt()` `.protocol.ResourceReceipt receipt = 7;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getId

      ```
      com.google.protobuf.ByteString getId()
      ```

      `bytes id = 1;`

      Returns:
      :   The id.
    - #### getFee

      ```
      long getFee()
      ```

      `int64 fee = 2;`

      Returns:
      :   The fee.
    - #### getBlockNumber

      ```
      long getBlockNumber()
      ```

      `int64 blockNumber = 3;`

      Returns:
      :   The blockNumber.
    - #### getBlockTimeStamp

      ```
      long getBlockTimeStamp()
      ```

      `int64 blockTimeStamp = 4;`

      Returns:
      :   The blockTimeStamp.
    - #### getContractResultList

      ```
      java.util.List<com.google.protobuf.ByteString> getContractResultList()
      ```

      `repeated bytes contractResult = 5;`

      Returns:
      :   A list containing the contractResult.
    - #### getContractResultCount

      ```
      int getContractResultCount()
      ```

      `repeated bytes contractResult = 5;`

      Returns:
      :   The count of contractResult.
    - #### getContractResult

      ```
      com.google.protobuf.ByteString getContractResult(int index)
      ```

      `repeated bytes contractResult = 5;`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The contractResult at the given index.
    - #### getContractAddress

      ```
      com.google.protobuf.ByteString getContractAddress()
      ```

      `bytes contract_address = 6;`

      Returns:
      :   The contractAddress.
    - #### hasReceipt

      ```
      boolean hasReceipt()
      ```

      `.protocol.ResourceReceipt receipt = 7;`

      Returns:
      :   Whether the receipt field is set.
    - #### getReceipt

      ```
      Response.ResourceReceipt getReceipt()
      ```

      `.protocol.ResourceReceipt receipt = 7;`

      Returns:
      :   The receipt.
    - #### getReceiptOrBuilder

      ```
      Response.ResourceReceiptOrBuilder getReceiptOrBuilder()
      ```

      `.protocol.ResourceReceipt receipt = 7;`
    - #### getLogList

      ```
      java.util.List<Response.TransactionInfo.Log> getLogList()
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`
    - #### getLog

      ```
      Response.TransactionInfo.Log getLog(int index)
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`
    - #### getLogCount

      ```
      int getLogCount()
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`
    - #### getLogOrBuilderList

      ```
      java.util.List<? extends Response.TransactionInfo.LogOrBuilder> getLogOrBuilderList()
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`
    - #### getLogOrBuilder

      ```
      Response.TransactionInfo.LogOrBuilder getLogOrBuilder(int index)
      ```

      `repeated .protocol.TransactionInfo.Log log = 8;`
    - #### getResultValue

      ```
      int getResultValue()
      ```

      `.protocol.TransactionInfo.code result = 9;`

      Returns:
      :   The enum numeric value on the wire for result.
    - #### getResult

      ```
      Response.TransactionInfo.code getResult()
      ```

      `.protocol.TransactionInfo.code result = 9;`

      Returns:
      :   The result.
    - #### getResMessage

      ```
      com.google.protobuf.ByteString getResMessage()
      ```

      `bytes resMessage = 10;`

      Returns:
      :   The resMessage.
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
    - #### getInternalTransactionsList

      ```
      java.util.List<Response.InternalTransaction> getInternalTransactionsList()
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`
    - #### getInternalTransactions

      ```
      Response.InternalTransaction getInternalTransactions(int index)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`
    - #### getInternalTransactionsCount

      ```
      int getInternalTransactionsCount()
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`
    - #### getInternalTransactionsOrBuilderList

      ```
      java.util.List<? extends Response.InternalTransactionOrBuilder> getInternalTransactionsOrBuilderList()
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`
    - #### getInternalTransactionsOrBuilder

      ```
      Response.InternalTransactionOrBuilder getInternalTransactionsOrBuilder(int index)
      ```

      `repeated .protocol.InternalTransaction internal_transactions = 17;`
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
    - #### getPackingFee

      ```
      long getPackingFee()
      ```

      `int64 packingFee = 27;`

      Returns:
      :   The packingFee.
    - #### getWithdrawExpireAmount

      ```
      long getWithdrawExpireAmount()
      ```

      `int64 withdraw_expire_amount = 28;`

      Returns:
      :   The withdrawExpireAmount.
    - #### getCancelUnfreezeV2AmountCount

      ```
      int getCancelUnfreezeV2AmountCount()
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 29;`
    - #### containsCancelUnfreezeV2Amount

      ```
      boolean containsCancelUnfreezeV2Amount(java.lang.String key)
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 29;`
    - #### getCancelUnfreezeV2Amount

      ```
      @Deprecated
      java.util.Map<java.lang.String,java.lang.Long> getCancelUnfreezeV2Amount()
      ```

      Deprecated.

      Use [`getCancelUnfreezeV2AmountMap()`](../../../../org/tron/trident/proto/Response.TransactionInfoOrBuilder.html#getCancelUnfreezeV2AmountMap--) instead.
    - #### getCancelUnfreezeV2AmountMap

      ```
      java.util.Map<java.lang.String,java.lang.Long> getCancelUnfreezeV2AmountMap()
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 29;`
    - #### getCancelUnfreezeV2AmountOrDefault

      ```
      long getCancelUnfreezeV2AmountOrDefault(java.lang.String key,
                                              long defaultValue)
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 29;`
    - #### getCancelUnfreezeV2AmountOrThrow

      ```
      long getCancelUnfreezeV2AmountOrThrow(java.lang.String key)
      ```

      `map<string, int64> cancel_unfreezeV2_amount = 29;`