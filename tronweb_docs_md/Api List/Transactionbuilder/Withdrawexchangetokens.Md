

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* withdrawExchangeTokens
Version: 6.3.0

On this page

# withdrawExchangeTokens [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L2079)

Create a transaction to withdraw tokens from an exchange pair based on Bancor protocol.

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.transactionBuilder.withdrawExchangeTokens(exchangeID, tokenID, tokenAmount, ownerAddress, options);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| exchangeID | non-negative integer exchange id. | Integer |
| tokenID | Token id of the token inject. | String |
| tokenAmount | The number of token withdraw. | Integer |
| ownerAddress | The address of the creator of the exchange pair. | String |
| options | Permission id for multi-signature and block header for contract block header info. | `{ permissionId: number, blockHeader: ... }` |

## Returns[​](#returns "Direct link to Returns")

Unsigned transaction object.

## Example[​](#example "Direct link to Example")

```
//Example 1  
const transaction = await tronWeb.transactionBuilder.withdrawExchangeTokens(1, "1000003", 100, "410ca7c49aa44d26aabfe7f594c645cf9f17a4ff70");  
console.log(transaction);  
{  
  visible: false,  
  txID: '560b803647f39b87a76623c4428102d1d96d18367b7f679412cc810029499a71',  
  raw_data: {  
    contract: [ [Object] ],  
    ref_block_bytes: '6e55',  
    ref_block_hash: '96fe9781aef670d8',  
    expiration: 1581385101000,  
    timestamp: 1581385042932  
  },  
  raw_data_hex: '0a026e55220896fe9781aef670d840c8dd968f832e5a61082b125d0a35747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e45786368616e67655769746864726177436f6e747261637412240a15410ca7c49aa44d26aabfe7f594c645cf9f17a4ff7010011a0731303030303033206470f497938f832e'  
}  
  
// Example 2  
await tronWeb.transactionBuilder.withdrawExchangeTokens(1, "1000003", 100, "TB8865sqTQ3qxWqhNQRCBov3KtPXFRPccK");  
{  
  visible: false,  
  txID: 'a776c9009655b72c4ad4858d391e25a522d753d9e40197f24703adda41dc3c77',  
  raw_data: {  
    contract: [ [Object] ],  
    ref_block_bytes: '6e7b',  
    ref_block_hash: '413bf5de7cf22452',  
    expiration: 1581385215000,  
    timestamp: 1581385155940  
  },  
  raw_data_hex: '0a026e7b2208413bf5de7cf224524098d89d8f832e5a61082b125d0a35747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e45786368616e67655769746864726177436f6e747261637412240a15410ca7c49aa44d26aabfe7f594c645cf9f17a4ff7010011a0731303030303033206470e48a9a8f832e'  
}
```