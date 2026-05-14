

* [API List](/docu/docs/API List/)
* [contract](/docu/docs/API List/contract/)
* tronWeb.contract()
Version: 6.3.0

On this page

# tronWeb.contract() [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/tronweb.ts#L266)

Creates a contract object that wraps an ABI. Allows you to easily call
functions on the contract.

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.contract(abi,contractAddress);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameters | Description | Type |
| --- | --- | --- |
| abi | Optionally provide the ABI for a contract. | Array |
| address | Optionally provide the address for a contract. Hex or Base58 format | String |

## Returns[​](#returns "Direct link to Returns")

Object - The contract instance.

## Example[​](#example "Direct link to Example")

```
//example 1:Create the contract object through contract address and ABI  
let instance = await tronWeb.contract([{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}],"contractAddress")  
  
//example 2:First create an empty contract object, and then specify the contract address by at() function. If the abi is on the chain, at() function will load ABI automatically , else you need to load it manually   
let abi = [...] as const;  
let instance = await tronWeb.contract(abi, "contractAddress");
```

If the contract ABI does not exist on the chain, Please invoke loadAbi
function to manually load the contract ABI. An example is as below:

```
//example 1  
let instance =await tronWeb.contract([{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}],"contractAddress")  
let res = await instance.name().call({_isConstant:true})  
  
//example 2  
let abi = [];  
let instance = await tronWeb.contract(abi, "contractAddress");  
instance.loadAbi([{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}]);  
let res = await instance.name().call({_isConstant:true})
```