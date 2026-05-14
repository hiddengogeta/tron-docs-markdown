

* [API List](/docu/docs/API List/)
* contract
Version: 6.3.0

# contract

**Type Inference**

TronWeb provides type inference for smart contracts from v6.0.4, allowing you to work with contract methods and their parameters in a type-safe manner. This feature is particularly useful when using TypeScript. To use type inference, you need to add `as const` assertion to the contract ABI. For example:

```
const abi = [  
  {  
    "constant": true,  
    "inputs": [{ "name": "input_value", "type": "uint256" }],  
    "name": "getValue",  
    "outputs": [{ "name": "output_value", "type": "uint256" }],  
    "payable": false,  
    "stateMutability": "view",  
    "type": "function"  
  }  
] as const;  
const contract = tronWeb.contract(abi, 'contractAddress');  
const value = await contract.getValue(100).call();
```

In the example above, you can get the parameter type of `contract.getValue` as `Numbers` and the return value type as `[Numbers] & { output_value: Numbers }`.

**Note:**

* If you want to call a contract with overloaded functions, you must use the `contract[functionSelector](...args)` syntax to trigger the contract, even though type inference is available when using `contract[functionName](...args)`.
* If the ABI outputs include a field named `length`, the returned array will not contain this property because length is a reserved property of arrays. As a result, if `length` is the only output defined in the ABI, the returned value will be unwrapped and returned as a single value rather than an array.
* If a contract method argument is an array, you must either pass the array directly to the method or use `as const` to narrow the argument type.
* The `send()` method accepts a `SendOptions` object as its sole parameter. To ensure the correct return type is inferred, pass the object directly to the method or use `as const` to narrow the argument type.

**Smart Contract Deployment**

For deploying a smart contract, you can not only use the
[tronWeb.transactionBuilder.createSmartContract](/docu/docs/API List/transactionBuilder/createSmartContract) interface, but also the [tronWeb.contract().new()](/docu/docs/API List/contract/tronweb.contract().new) interface.

**Smart Contract Invocation**

Get smart contract instance

Before calling a smart contract, you need to obtain the smart contract instance first. You can create a contract instance in the following way:

```
//Example 1  
let abi = [...] as const;         
let instance = await tronWeb.contract(abi,'contractAddress');
```

Calling smart contract methods

Different types of contract methods need to be invoked by different
tronweb apis:

* Use `call` to execute `pure` or `view` smart contract methods, please
  refer to [method.call()](/docu/docs/API List/contract/method.call).
* Use `send` to
  execute `non-pure` or `modify` smart contract methods, please refer to
  [method.send()](/docu/docs/API List/contract/method.send) for specific usage
  instructions.