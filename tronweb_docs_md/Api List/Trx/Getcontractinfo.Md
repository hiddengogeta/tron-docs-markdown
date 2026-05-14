

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getContractInfo
Version: 6.3.0

On this page

# getContractInfo [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L526)

Queries a contract's information from the blockchain. The difference from the `trx.getContract` interface is that this interface returns not only the `bytecode` but also the `runtime bytecode` of the contract. Compared with `bytecode`, `runtime bytecode` does not contain constructor and constructor parameter information.

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getContractInfo(address);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameters | Parameter Description | Data Type |
| --- | --- | --- |
| address | Smart Contract Address | String |

## Return[​](#return "Direct link to Return")

Object - Contract info.

## Example[​](#example "Direct link to Example")

```
await tronWeb.trx.getContractInfo("TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t");  
{  
  "runtimecode": "6080604052600436106101a1576000357c01...45553445400000000000000000000000000000000000000000000000000000000",  
  "smart_contract": {  
    "bytecode": "60806040526000600260146101000a81548160ff0219169...45553445400000000000000000000000000000000000000000000000000000000",  
    "consume_user_resource_percent": 30,  
    "name": "TetherToken",  
    "origin_address": "41517591d35d313bf6a5e33098284502b045e2bc08",  
    "abi": {  
      "entrys": [  
        {  
          "outputs": [  
            {  
              "type": "string"  
            }  
          ],  
          "constant": true,  
          "name": "name",  
          "stateMutability": "View",  
          "type": "Function"  
        },  
        ...  
        {  
          "inputs": [  
            {  
              "name": "_blackListedUser",  
              "type": "address"  
            }  
          ],  
          "name": "destroyBlackFunds",  
          "stateMutability": "Nonpayable",  
          "type": "Function"  
        }  
      ]  
    },  
    "origin_energy_limit": 10000000,  
    "contract_address": "41a614f803b6fd780986a42c78ec9c7f77e6ded13c",  
    "code_hash": "99bb60e56b4cd2642c6847e372b18b6e0f9514229e3086d3a042d60a4c7b78a9"  
  },  
  "contract_state": {  
    "update_cycle": 9460,  
    "energy_usage": 11743864698,  
    "energy_factor": 34000  
  }  
}
```