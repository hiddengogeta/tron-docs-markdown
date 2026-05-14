

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* injectExchangeTokens
Version: 6.3.0

On this page

# injectExchangeTokens [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L2025)

Create a transaction to inject tokens into an exchange pair based on
Bancor protocol.

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.transactionBuilder.injectExchangeTokens(exchangeId, tokenId, tokenAmount, ownerAddress, options)
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| exchangeId | Non-negative integer exchange id. | Integer |
| tokenId | Token id of the token inject. | String |
| tokenAmount | The number of token inject. | Integer |
| ownerAddress | The address of the creator of the exchange pair. | String |
| options | Optional. Permission id for multi-signature and block header for contract block header info. | `{ permissionId: number, blockHeader: ... }` |

## Returns[​](#returns "Direct link to Returns")

Unsigned transaction object.

## Example[​](#example "Direct link to Example")

```
// Example 1  
await tronWeb.transactionBuilder.injectExchangeTokens(1, "1000003", 10000, "410ca7c49aa44d26aabfe7f594c645cf9f17a4ff70");  
{  
  visible: false,  
  txID: 'cdac0a375d5042042aef204301d67181bb83390ba060b11033a7913221af0ebb',  
  raw_data: {  
    contract: [ [Object] ],  
    ref_block_bytes: 'ce03',  
    ref_block_hash: '620c5f8f84ac6944',  
    expiration: 1581261939000,  
    timestamp: 1581261879534  
  },  
  raw_data_hex: '0a02ce032208620c5f8f84ac694440b8c2b9d4822e5a60082a125c0a33747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e45786368616e6765496e6a656374436f6e747261637412250a15410ca7c49aa44d26aabfe7f594c645cf9f17a4ff7010011a073130303030303320904e70eef1b5d4822e'  
}  
  
//Example 2  
await tronWeb.transactionBuilder.injectExchangeTokens(1, "1000003",10000,"TB8865sqTQ3qxWqhNQRCBov3KtPXFRPccK");  
{  
  visible: false,  
  txID: 'a05cace199e2a1d39410adfac5f17a18e63f43bdc78b5840f63a083cbcfa6cb9',  
  raw_data: {  
    contract: [ [Object] ],  
    ref_block_bytes: '72a2',  
    ref_block_hash: 'd85b910374acd2ed',  
    expiration: 1581388404000,  
    timestamp: 1581388345878  
  },  
  raw_data_hex: '0a0272a22208d85b910374acd2ed40a0aae090832e5a60082a125c0a33747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e45786368616e6765496e6a656374436f6e747261637412250a15410ca7c49aa44d26aabfe7f594c645cf9f17a4ff7010011a073130303030303320904e7096e4dc90832e'  
}
```