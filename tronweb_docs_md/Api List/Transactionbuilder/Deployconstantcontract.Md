

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* deployConstantContract
Version: 6.3.0

On this page

# deployConstantContract [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L1020)

Estimate the energy required for the successful execution of deploying a contract.(v5.3.0 new interface)

## Usage[​](#usage "Direct link to Usage")

```
const transaction = await tronWeb.transactionBuilder.deployConstantContract(options);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| options | Options releated to contract deploying | Object |
| options.input | The bytecode of contract to be deployed. | String |
| options.ownerAddress | Owner address of the new contract. | String |
| options.tokenId | Optional. The id of token to be transfered to the new contract. | Number |
| options.tokenValue | Optional. The amount of token to be transfered to the new contract. | Number |
| options.callValue | Optional. Amount of TRX transferred with this transaction, measured in SUN (1TRX = 1,000,000 SUN). | Number |
| options.confirmed | Optional. Whether send request to solidity node. The default is `false` | Boolean |

## Returns[​](#returns "Direct link to Returns")

```
{  
    /**  
     * The energy required for deploying the contract.  
     */  
    energy_required: number;  
    result: {  
        result: boolean;  
    }  
}
```

## Example[​](#example "Direct link to Example")

```
const result = await tronWeb.transactionBuilder.deployConstantContract({  
    ownerAddress: 'TMVQGm1qAQYVdetCeGRRkTWYYrLXuHK2HC',  
    input: '0x60806040526000805534801561001457600080fd5b50d3801561002157600080fd5b50d2801561002e57600080fd5b5060e08061003d6000396000f3fe6080604052348015600f57600080fd5b50d38015601b57600080fd5b50d28015602757600080fd5b5060043610605d576000357c01000000000000000000000000000000000000000000000000000000009004806360fe47b1146062575b600080fd5b608b60048036036020811015607657600080fd5b810190808035906020019092919050505060a1565b6040518082815260200191505060405180910390f35b600081600081905550600054905091905056fea165627a7a72305820392f2cf7f1b37873349bf7ce496fb370bc80c6539de204bded6197106c530e7000',  
});
```