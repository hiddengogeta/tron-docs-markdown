

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* tradeExchangeTokens
Version: 6.3.0

On this page

# tradeExchangeTokens [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L2133)

Trade tokens on a bancor style exchange.

## Usage[​](#usage "Direct link to Usage")

```
const transaction = await tronWeb.transactionBuilder.tradeExchangeTokens(exchangeId, tokenName, tokenAmountSold, tokenAmountExpected, ownerAddress, options)
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| exchangeId | Non-negative integer exchange id | Integer |
| tokeId | tokeId | String |
| tokenAmountSold | Amount of token actually sold | Integer |
| tokenAmountExpected | Amount of token expected | Integer |
| ownerAddress | Token owner address in hex | hexString |
| options | The permissions id for multi-sign and block header for contract block header info. | `{ permissionId: number, blockHeader: ... }` |

## Returns[​](#returns "Direct link to Returns")

Unsigned transaction object.

## Example[​](#example "Direct link to Example")

```
await tronWeb.transactionBuilder.tradeExchangeTokens(1, "1000003", 1000, 1000, "410ca7c49aa44d26aabfe7f594c645cf9f17a4ff70");  
{  
    "visible": false,  
    "txId": "545ed6a5eb793fe5903ec177761b2504147e010875644fce321f0dbb28799456",  
    "raw_data": {  
        "contract": [  
            {  
                "parameter": {  
                    "value": {  
                        "exchange_id": 1,  
                        "token_id": "31303030303033",  
                        "expected": 1000,  
                        "owner_address": "410ca7c49aa44d26aabfe7f594c645cf9f17a4ff70",  
                        "quant": 1000  
                    },  
                    "type_url": "type.googleapis.com/protocol.ExchangeTransactionContract"  
                },  
                "type": "ExchangeTransactionContract"  
            }  
        ],  
        "ref_block_bytes": "c778",  
        "ref_block_hash": "db086b31f0f10f69",  
        "expiration": 1581650238000,  
        "timestamp": 1581650180365  
    },  
    "raw_data_hex": "0a02c7782208db086b31f0f10f6940b0b4cd8d842e5a68082c12640a38747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e45786368616e67655472616e73616374696f6e436f6e747261637412280a15410ca7c49aa44d26aabfe7f594c645cf9f17a4ff7010011a073130303030303320e80728e807708df2c98d842e"  
}
```