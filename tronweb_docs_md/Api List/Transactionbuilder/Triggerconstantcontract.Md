

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* triggerConstantContract
Version: 6.3.0

On this page

# triggerConstantContract [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L985)

Trigger the read-only function of the contract ( they are the contract function which decorated by the `pure` and `view` modifiers), the query
result is a non-solidified state.

## Usage[​](#usage "Direct link to Usage")

```
const transactionWrapper = tronWeb.transactionBuilder.triggerConstantContract(contractAddress, functionSelector, options, parameter, ownerAddress);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| contractAddress | The smart contract address. | String |
| functionSelector | Function to call, must not leave a blank space | String |
| options | Options for trigger smart contract | [`TriggerSmartContractOptions`](/docu/docs/Interact with contract#triggersmartcontractoptions) |
| parameter | The parameter passed to `function` | `Array<{ type: string; value: unknown }>` |
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
const parameter = [{ type: 'address', value: 'TV3nb5HYFe2xBEmyb3ETe93UGkjAhWyzrs' }, { type: 'uint256', value: 100 }];  
const transactionWrapper = await tronWeb.transactionBuilder.triggerConstantContract("419e62be7f4f103c36507cb2a753418791b1cdc182", "transfer(address,uint256)", {}, parameter, "417946F66D0FC67924DA0AC9936183AB3B07C81126");  
console.log(transactionWrapper);  
{  
    "result": {  
        "result": true  
    },  
    "energy_used": 29631,  
    "constant_result": [  
        "0000000000000000000000000000000000000000000000000000000000000000"  
    ],  
    "logs": [  
        {  
            "address": "9e62be7f4f103c36507cb2a753418791b1cdc182",  
            "data": "0000000000000000000000000000000000000000000000000000000000000064",  
            "topics": [  
                "ddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",  
                "0000000000000000000000007946f66d0fc67924da0ac9936183ab3b07c81126",  
                "000000000000000000000000d148171f1ceeeb40d668c47d70e7e94e67977559"  
            ]  
        }  
    ],  
    "transaction": {  
        "ret": [  
            {}  
        ],  
        "visible": false,  
        "txID": "5c280444c82f3050e4b0c672ab98bae264830d80b09db6c861b31699f6bcaaa8",  
        "raw_data": {  
            "contract": [  
                {  
                    "parameter": {  
                        "value": {  
                            "data": "a9059cbb000000000000000000000000d148171f1ceeeb40d668c47d70e7e94e679775590000000000000000000000000000000000000000000000000000000000000064",  
                            "owner_address": "417946f66d0fc67924da0ac9936183ab3b07c81126",  
                            "contract_address": "419e62be7f4f103c36507cb2a753418791b1cdc182"  
                        },  
                        "type_url": "type.googleapis.com/protocol.TriggerSmartContract"  
                    },  
                    "type": "TriggerSmartContract"  
                }  
            ],  
            "ref_block_bytes": "3d8f",  
            "ref_block_hash": "316b196f79afe0dc",  
            "expiration": 1649655780000,  
            "timestamp": 1649655730243  
        },  
        "raw_data_hex": "0a023d8f2208316b196f79afe0dc40a0a596b981305aae01081f12a9010a31747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e54726967676572536d617274436f6e747261637412740a15417946f66d0fc67924da0ac9936183ab3b07c811261215419e62be7f4f103c36507cb2a753418791b1cdc1822244a9059cbb000000000000000000000000d148171f1ceeeb40d668c47d70e7e94e67977559000000000000000000000000000000000000000000000000000000000000006470c3a093b98130"  
    }  
}
```

**Note**:
After GreatVoyage-v4.3.0(Bacon), user can invoke the read-only method as well as the non-read-only method of a contract via wallet/triggerconstantcontract API, and there is a new field energy\_limit in the return value, it means the actual energy consumption of this contract invoking. This API can be used to forecast energy usage.