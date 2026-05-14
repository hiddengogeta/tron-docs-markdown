

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* estimateEnergy
Version: 6.3.0

On this page

# estimateEnergy [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L1008)

Estimate the energy required to trigger the contract. This interface requires the fullnode node to enable the service. If the call is not enabled, an error will be reported. You can continue to use the triggerconstantcontract interface to estimate the energy. (v5.1.0 new interface)

## Usage[​](#usage "Direct link to Usage")

```
const result = await tronWeb.transactionBuilder.estimateEnergy(contractAddress, functionSelector, options, parameter, issuerAddress);
```

## Parameters[​](#parameters "Direct link to Parameters")

The parameters of `estimateEnergy()` is same as [triggerSmartContract()](/docu/docs/API List/transactionBuilder/triggerSmartContract).

## Returns[​](#returns "Direct link to Returns")

```
{  
    /**  
     * The energy required for trigger the contract.  
     */  
    energy_required: number;  
    result: {  
        result: boolean;  
    }  
}
```

## Example[​](#example "Direct link to Example")

```
const result = await tronWeb.transactionBuilder.estimateEnergy(  
    'TPYwAC9Y4uUcT2QH3WPPjqxzJSJWymMoMS',  
    'balanceOf(address)', {},   
    [{ type:'address',value: 'THvMiWQeVPGEMuBtAnuKn2QpuSjqjrGQGu' }]  
)  
{  
  "result": {  
    "result": true,  
  },  
  "energy_required": 900000  
}
```