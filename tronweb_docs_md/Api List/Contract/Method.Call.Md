

* [API List](/docu/docs/API List/)
* [contract](/docu/docs/API List/contract/)
* call()
Version: 6.3.0

On this page

# call() [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/contract/method.ts#L169)

Use `call` to execute a `pure` or `view` smart contract method. These
methods do not modify the blockchain, do not cost anything to execute
and are also not broadcasted to the network.

## Usage[​](#usage "Direct link to Usage")

```
//Example 1  
let abi = [...] as const;  
let contract = await tronWeb.contract(abi, 'contractAddress');  
let result = await contract.function_name(param1,param2,...).call();  
  
//Example 2  
let abi = [...] as const;  
let contract = await tronWeb.contract(abi, 'contractAddress');  
let result = await contract["function_selector"](param1,param2,...).call();
```

## Returns[​](#returns "Direct link to Returns")

Object - Method calling result.

## Example[​](#example "Direct link to Example")

```
//example 1  
async function triggercontract(){  
   let abi = [...];  
   let instance = await tronWeb.contract(abi, 'contractAddress');  
   let res = await instance.totalSupply().call();  
   console.log(res);  
}  
triggercontract();  
  
//example 2  
async function triggercontract(){  
   let abi = [...];  
   let instance = await tronWeb.contract(abi, 'contractAddress');  
   let res = await instance["totalSupply"]().call();  
   console.log(res);  
}  
triggercontract();  
  
//example 3：the ABI of the smart contract is not on-chain  
async function triggercontract(){  
   let abi = [];  
   let instance = await tronWeb.contract(abi, 'contractAddress');  
   instance.loadAbi([{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}]);  
   let res = await instance.name().call({_isConstant:true})  
   console.log(res);  
}  
triggercontract();
```