

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* triggerConfirmedConstantContract
Version: 6.3.0

On this page

# triggerConfirmedConstantContract [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L996)

Trigger the read-only function of the contract ( they are the contract function which decorated by the pure and view modifiers), the query result is a solidified state.

## Usage[​](#usage "Direct link to Usage")

```
const transactionWrapper = await tronWeb.transactionBuilder.triggerConfirmedConstantContract(contractAddress, functionSelector, options, parameters, ownerAddress);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| contractAddress | The smart contract address. | String |
| functionSelector | Function call, must not leave a blank space | String |
| options | Options when call contract function | [`TriggerSmartContractOptions`](/docu/docs/Interact with contract#triggersmartcontractoptions) |
| parameters | The parameter passed to `functionSelector` | `Array<{ type: string, value: unknown }>` |
| ownerAddress | Address in hex which calls the `function` | String |

## Returns[​](#returns "Direct link to Returns")

A wrapper which contains unsigned transaction object.

```
interface TransactionWrapper {  
    result: {  
        result: boolean;  
    };  
    /**  
     * The transaction object created by calling contract function.  
     */  
    transaction: Transaction;  
    /**  
     * Energy used by triggering contract.  
     */  
    energy_used?: number;  
    /**  
     * The total penalty energy in the transaction  
     */  
    energy_penalty?: number;  
    /**  
     * Result of calling contract function which is decorated by `view` or `pure`.  
     */  
    constant_result?: string[];  
}
```

## Example[​](#example "Direct link to Example")

```
const parameter = [{ type: 'address', value: tronWeb.defaultAddress.base58 }];  
const options = {  
  feeLimit: 100000000,  
  callValue: 0  
}  
const transactionWrapper = await tronWeb.transactionBuilder.triggerConfirmedConstantContract("TGjgvdTWWrybVLaVeFqSyVqJQWjxqRYbaK", "balanceOf(address)", options, parameter, tronWeb.defaultAddress.base58);  
console.log(transactionWrapper);  
{  
    "result": {  
        "result": true  
    },  
    "energy_used": 473,  
    "constant_result": [  
        "00000000000000000000000000000000000000000000000b84ddc1db6e378334"  
    ],  
    "transaction": {  
        "ret": [  
            {}  
        ],  
        "visible": false,  
        "txID": "f166ca1f58e62dc70c8837b684f2ef3132cc2bf73d59f43091bb281e620055c7",  
        "raw_data": {  
            "contract": [  
                {  
                    "parameter": {  
                        "value": {  
                            "data": "70a08231000000000000000000000000573708726db88a32c1b9c828fef508577cfb8483",  
                            "owner_address": "41573708726db88a32c1b9c828fef508577cfb8483",  
                            "contract_address": "414a3a5dd265bd974b4de0bbe33faa7efb8b7b87e8"  
                        },  
                        "type_url": "type.googleapis.com/protocol.TriggerSmartContract"  
                    },  
                    "type": "TriggerSmartContract"  
                }  
            ],  
            "ref_block_bytes": "7177",  
            "ref_block_hash": "3bfbca3567020777",  
            "expiration": 1694658258000,  
            "timestamp": 1694658255514  
        },  
        "raw_data_hex": "0a02717722083bfbca356702077740d0c8838ca9315a8e01081f1289010a31747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e54726967676572536d617274436f6e747261637412540a1541573708726db88a32c1b9c828fef508577cfb84831215414a3a5dd265bd974b4de0bbe33faa7efb8b7b87e8222470a08231000000000000000000000000573708726db88a32c1b9c828fef508577cfb8483709ab5838ca931"  
    }  
}
```