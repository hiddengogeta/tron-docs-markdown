

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* updateEnergyLimit
Version: 6.3.0

On this page

# updateEnergyLimit [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L2238)

## Usage[​](#usage "Direct link to Usage")

```
const transaction = await tronWeb.transactionBuilder.updateEnergyLimit(contractAddress, originEnergyLimit, ownerAddress, options);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| contractAddress | Smart Contract address,format:hestring or base58 | String |
| originEnergyLimit | The maximum resource consumption of the creator in one execution or creation | Number |
| ownerAddress | Smart contract creator's address,format:hestring or base58 | String |
| options | Permission id for multi-signature and block header for contract block header info. | `{ permissionId: number, blockHeader: ... }` |

## Returns[​](#returns "Direct link to Returns")

Unsigned transaction object.

## Example[​](#example "Direct link to Example")

```
const transaction = await tronWeb.transactionBuilder.updateEnergyLimit("TBQ8ubHnwWAZvHVPJevnKpEfabetDdaQdQ",30,"TTSFjEG3Lu9WkHdp4JrWYhbGP6K1REqnGQ");  
console.log(transaction)  
{  
  visible: false,  
  txID: 'b17022e101f964e0f1b413e0862ca8a3ca6c7e48f39b1765103ca59bd3a84f0a',  
  raw_data: {  
    contract: [ [Object] ],  
    ref_block_bytes: '2782',  
    ref_block_hash: '6309a83565218acf',  
    expiration: 1581330690000,  
    timestamp: 1581330630613  
  },  
  raw_data_hex: '0a02278222086309a83565218acf40d0df9df5822e5a6e082d126a0a36747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e557064617465456e657267794c696d6974436f6e747261637412300a1541bf97a54f4b829c4e9253b26024b1829e1a3b11201215410faf1b6bce9e815555544aea9d350f9d3dc6d3ba181e70d58f9af5822e'  
}
```