

* [Advanced](/docu/docs/category/advanced)
* Exchange Operations
Version: 6.3.0

On this page

# Exchange Operations Guide

TronWeb provides built-in support for the Bancor-based decentralized exchange (DEX) protocol on TRON. This allows creating token trading pairs and executing trades on-chain.

note

TRON's built-in DEX uses the **Bancor algorithm** for automated price discovery based on token supply and balance ratios.

## Creating an Exchange[​](#creating-an-exchange "Direct link to Creating an Exchange")

### TRX-to-Token Exchange[​](#trx-to-token-exchange "Direct link to TRX-to-Token Exchange")

Create a trading pair between TRX and a TRC-10 token:

```
const tx = await tronWeb.transactionBuilder.createTRXExchange(  
    'TokenName',   // TRC-10 token name  
    1000000000,    // token amount to deposit  
);  
const signedTx = await tronWeb.trx.sign(tx);  
const receipt = await tronWeb.trx.sendRawTransaction(signedTx);
```

### Token-to-Token Exchange[​](#token-to-token-exchange "Direct link to Token-to-Token Exchange")

Create a trading pair between two TRC-10 tokens:

```
const tx = await tronWeb.transactionBuilder.createTokenExchange(  
    'TokenA',      // first token name  
    1000000000,    // first token amount  
    'TokenB',      // second token name  
    2000000000,    // second token amount  
);  
const signedTx = await tronWeb.trx.sign(tx);  
const receipt = await tronWeb.trx.sendRawTransaction(signedTx);
```

## Managing Exchange Liquidity[​](#managing-exchange-liquidity "Direct link to Managing Exchange Liquidity")

### Inject Tokens[​](#inject-tokens "Direct link to Inject Tokens")

Add liquidity to an existing exchange:

```
const tx = await tronWeb.transactionBuilder.injectExchangeTokens(  
    exchangeId,    // exchange ID  
    'TokenName',   // token to inject  
    1000000000,    // amount to inject  
);  
const signedTx = await tronWeb.trx.sign(tx);  
const receipt = await tronWeb.trx.sendRawTransaction(signedTx);
```

### Withdraw Tokens[​](#withdraw-tokens "Direct link to Withdraw Tokens")

Remove liquidity from an exchange:

```
const tx = await tronWeb.transactionBuilder.withdrawExchangeTokens(  
    exchangeId,    // exchange ID  
    'TokenName',   // token to withdraw  
    500000000,     // amount to withdraw  
);  
const signedTx = await tronWeb.trx.sign(tx);  
const receipt = await tronWeb.trx.sendRawTransaction(signedTx);
```

## Trading[​](#trading "Direct link to Trading")

Execute a trade on an exchange:

```
const tx = await tronWeb.transactionBuilder.tradeExchangeTokens(  
    exchangeId,    // exchange ID  
    'TokenName',   // token to sell  
    1000000000,    // amount to sell  
    500000000,     // expected minimum amount to receive  
);  
const signedTx = await tronWeb.trx.sign(tx);  
const receipt = await tronWeb.trx.sendRawTransaction(signedTx);
```

**Parameters:**

| Parameter | Type | Description |
| --- | --- | --- |
| `exchangeID` | number | The exchange pair ID |
| `tokenName` | string | Token you are selling |
| `tokenAmountSold` | number | Amount of token to sell |
| `tokenAmountExpected` | number | Minimum amount expected to receive (slippage protection) |

tip

Set `tokenAmountExpected` to provide slippage protection. The trade will fail if the actual received amount is less than this value.

## Querying Exchanges[​](#querying-exchanges "Direct link to Querying Exchanges")

```
// List all exchanges  
const exchanges = await tronWeb.trx.listExchanges();  
  
// Get details of a specific exchange  
const exchange = await tronWeb.trx.getExchangeByID(exchangeId);  
console.log(exchange);  
// {  
//   exchange_id: 1,  
//   creator_address: '...',  
//   first_token_id: 'TokenA',  
//   first_token_balance: 1000000000,  
//   second_token_id: '_',  // '_' represents TRX  
//   second_token_balance: 5000000000,  
// }  
  
// List exchanges created by a specific account  
const myExchanges = await tronWeb.trx.listExchangesPaginated(limit, offset);
```

## Bancor Price Calculation[​](#bancor-price-calculation "Direct link to Bancor Price Calculation")

The Bancor algorithm ensures that:

```
first_token_balance × second_token_balance = constant
```

When you sell token A to buy token B:

```
Amount of B received = second_balance - (first_balance × second_balance) / (first_balance + amount_of_A_sold)
```

This means larger trades have higher price impact (slippage).

## Related API References[​](#related-api-references "Direct link to Related API References")

* [transactionBuilder.injectExchangeTokens](/docu/docs/API List/transactionBuilder/injectExchangeTokens)
* [transactionBuilder.withdrawExchangeTokens](/docu/docs/API List/transactionBuilder/withdrawExchangeTokens)
* [transactionBuilder.tradeExchangeTokens](/docu/docs/API List/transactionBuilder/tradeExchangeTokens)