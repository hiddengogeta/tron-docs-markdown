

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* purchaseToken
Version: 6.3.0

On this page

# purchaseToken [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L195)

Creates an unsigned transaction for ICO token purchase.

## Usage[​](#usage "Direct link to Usage")

```
const transaction = await tronWeb.transactionBuilder.purchaseToken(issuerAddress, tokenId, amount, buyer, options);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| issuerAddress | Address issuing the Token. | String |
| tokenId | Name of the token, matching the exact capitalization. | String |
| amount | Amount of tokens to buy. | Integer |
| buyer | Optional. Address purchasing the tokens. | String |
| options | Optional. Permission id for multi-signature and block header for contract block header info. | `{ permissionId: number, blockHeader: ... }` |

## Returns[​](#returns "Direct link to Returns")

Unsigned transaction object.

## Example[​](#example "Direct link to Example")

```
// Example 1  
await tronWeb.transactionBuilder.purchaseToken("41bf97a54f4b829c4e9253b26024b1829e1a3b1120", "1000088", 100, "41010D3A8E0D80F8C83148240202DD178DF495B7BD");  
{  
  visible: false,  
  txID: '9ffe34c87be9e803ca219c05a1e976cdbc1ee63459335a43fbdc290b616fe09f',  
  raw_data: {  
    contract: [ [Object] ],  
    ref_block_bytes: '6ce6',  
    ref_block_hash: 'e123937572ed7ab5',  
    expiration: 1581384000000,  
    timestamp: 1581383940593  
  },  
  raw_data_hex: '0a026ce62208e123937572ed7ab54080c4d38e832e5a7b080912770a3a747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e506172746963697061746541737365744973737565436f6e747261637412390a1541010d3a8e0d80f8c83148240202dd178df495b7bd121541bf97a54f4b829c4e9253b26024b1829e1a3b11201a0731303030303838206470f1f3cf8e832e'  
}  
  
// Example 2  
await tronWeb.transactionBuilder.purchaseToken("TTSFjEG3Lu9WkHdp4JrWYhbGP6K1REqnGQ", "1000088", 100,"TPnBjYQEMo4Yd4866KCzXdi4a169KGd63n");  
{  
  visible: false,  
  txID: 'b86ac32d981d56ce7aef1461a6e8455c4176d2cb5daa5860d16d3132210ac49b',  
  raw_data: {  
    contract: [ [Object] ],  
    ref_block_bytes: '6cfb',  
    ref_block_hash: '5ff675a58150b8e0',  
    expiration: 1581384063000,  
    timestamp: 1581384004388  
  },  
  raw_data_hex: '0a026cfb22085ff675a58150b8e04098b0d78e832e5a7b080912770a3a747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e506172746963697061746541737365744973737565436f6e747261637412390a1541977c20977f412c2a1aa4ef3d49fee5ec4c31cdfb121541bf97a54f4b829c4e9253b26024b1829e1a3b11201a0731303030303838206470a4e6d38e832e'  
}
```