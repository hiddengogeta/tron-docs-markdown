

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* sendTrx
Version: 6.3.0

On this page

# sendTrx [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L92)

Creates an unsigned TRX transfer transaction

## Usage[​](#usage "Direct link to Usage")

```
const transaction = await tronWeb.transactionBuilder.sendTrx(to, amount, from, options);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| to | Address to send TRX to in hex or base58. | String |
| amount | Amount of TRX (units in SUN) to send. | Integer **(units in SUN)** |
| from | Optional address that is transferring the Tokens. If omitted, will use the address associated with the private key. | String |
| options | The permissions id for multi-sign and block header for contract block header info. | `{ permissionId: number, blockHeader: ... }` |

## Returns[​](#returns "Direct link to Returns")

Unsigned transaction object.

## Example[​](#example "Direct link to Example")

```
await tronWeb.transactionBuilder.sendTrx("TVDGpn4hCSzJ5nkHPLetk8KQBtwaTppnkr", 100, "TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL");  
{  
    "visible": false,  
    "txID": "9f62a65d0616c749643c4e2620b7877efd0f04dd5b2b4cd14004570d39858d7e",  
    "raw_data": {  
        "contract": [  
            {  
                "parameter": {  
                    "value": {  
                        "amount": 100,  
                        "owner_address": "418840e6c55b9ada326d211d818c34a994aeced808",  
                        "to_address": "41d3136787e667d1e055d2cd5db4b5f6c880563049"  
                    },  
                    "type_url": "type.googleapis.com/protocol.TransferContract"  
                },  
                "type": "TransferContract"  
            }  
        ],  
        "ref_block_bytes": "0add",  
        "ref_block_hash": "6c2763abadf9ed29",  
        "expiration": 1581308685000,  
        "timestamp": 1581308626092  
    },  
    "raw_data_hex": "0a020add22086c2763abadf9ed2940c8d5deea822e5a65080112610a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412300a15418840e6c55b9ada326d211d818c34a994aeced808121541d3136787e667d1e055d2cd5db4b5f6c880563049186470ac89dbea822e"  
}
```