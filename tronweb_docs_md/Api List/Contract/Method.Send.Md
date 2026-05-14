

* [API List](/docu/docs/API List/)
* [contract](/docu/docs/API List/contract/)
* send()
Version: 6.3.0

On this page

# send() [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/contract/method.ts#L242)

Use `send` to execute a `non-pure` or `modify` smart contract method on
a given smart contract that modifies or changes values on the blockchain.
These methods consume resources(bandwidth and energy) to perform as the
changes need to be broadcasted out to the network.

## Usage[​](#usage "Direct link to Usage")

```
let abi = [...] as const;  
let contract = await tronWeb.contract(abi, 'contractAddress');   
let result = await contract.function_name(param1,param2,...).send({  
  feeLimit:100_000_000,  
  callValue:0,  
  tokenId:'1000036',  
  tokenValue:100,  
  shouldPollResponse:true  
});
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description | Data Type |
| --- | --- | --- |
| feeLimit | Optional. The maximum SUN consumes by calling this contract method. Hard capped at 15000 TRX. (1TRX = 1,000,000SUN) | Integer |
| callValue | Optional. Amount of TRX transferred with this transaction, measured in SUN (1 TRX = 1,000,000 SUN). | Integer |
| shouldPollResponse | Optional. If set to TRUE, this will wait until the transaction is confirmed on the solidity node before returning the result. | Boolean |
| keepTxID | Optional. If both shouldPollResponse and keepTxID set to TRUE, the method will return txID and poll result. | Boolean |
| rawResponse | Optional. If set to TRUE, this will return the raw response. | Boolean |
| pollTimes | Optional. If shouldPollResponse is set to TRUE, this will wait until the transaction is confirmed on the solidity node or the result has been polled the times specified by this parameter. | Integer |
| tokenId | Optional. If the function accepts a trc 10 token ,then the id of the same | String |
| tokenValue | Optional. Amount of token sent with the call. | Integer |

## Returns[​](#returns "Direct link to Returns")

Object - Method calling result.
or
String - Transaction ID.

## Example[​](#example "Direct link to Example")

```
async function triggercontract(){  
    try {  
        let abi = [...] as const;  
        let instance = await tronWeb.contract(abi, 'TQQg4EL8o1BSeKJY4MJ8TB8XK7xufxFBvK');  
        let res = await instance.transfer('TWbcHNCYzqAGbrQteKnseKJdxfzBHyTfuh',500).send({  
            feeLimit:100_000_000,  
            callValue:0,  
            shouldPollResponse:true  
        });  
  
        console.log(res);  
  
    } catch (error) {  
        console.log(error);  
    }  
}  
  
triggercontract();
```