

* [API List](/docu/docs/API List/)
* [contract](/docu/docs/API List/contract/)
* tronweb.contract().new()
Version: 6.3.0

On this page

# tronweb.contract().new() [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/contract/index.ts#L109)

Deploy a smart contract.

## Usage[​](#usage "Direct link to Usage")

```
let abi = 'some abi for contract';  
let code = 'bytecode';  
async function deploy_contract(){  
  let contract_instance = await tronWeb.contract().new({  
    abi:JSON.parse(abi),  
    bytecode:code,  
    feeLimit:1000000000,  
    callValue:0,  
    userFeePercentage:1,  
    originEnergyLimit:10000000,  
    parameters:[param1, param2, param3,...]  
  });  
  console.log(contract_instance.address);  
}
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description | Data Type | Option |
| --- | --- | --- | --- |
| abi | Smart Contract's String Application Binary Interface. | Array | Required |
| bytecode | The compiled contract's identifier, used to interact with the Virtual Machine. | String | Required |
| feeLimit | The maximum SUN consumes by deploying this contract. (1TRX = 1,000,000SUN) | Integer, long | Optional |
| callValue | Amount of SUN transferred to the contract with this transaction.(1TRX = 1,000,000SUN) | Integer | Optional |
| userFeePercentage | The energy consumption percentage specified for the user calling this contract. | Integer between 0 and 100 | Optional |
| originEnergyLimit | The max energy which will be consumed by the owner in the process of execution or creation of the contract, is an integer which should be greater than 0. | Integer | Optional |
| parameters | Parameter passed to the constructor of the contract. | Array | Optional, required if constructor needs parameters |

**Important Note:** for the `userFeePercentage` parameter, it is **strongly recommended** to set the integer value between 1 and 99 (inclusive). Setting as 0 could potentially open the contract developer up to an infinite loop time-out attack.

## Returns[​](#returns "Direct link to Returns")

Object - The contract instance.

## Example[​](#example "Direct link to Example")

```
let abi = 'some abi for contract';  
let code = 'bytecode';  
async function deploy_contract(){  
  let contract_instance = await tronWeb.contract().new({  
    abi:JSON.parse(abi),  
    bytecode:code,  
    feeLimit:1_00_000_000,  
    callValue:0,  
    userFeePercentage:1,  
    originEnergyLimit:10_000_000  
  });  
  console.log(contract_instance.address);  
}  
  
deploy_contract();// Execute the function  
414d137bb7f91e8704d712d3967f6a745b9eedd839
```