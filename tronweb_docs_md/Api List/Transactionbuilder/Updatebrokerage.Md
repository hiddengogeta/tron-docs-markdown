

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* updateBrokerage
Version: 6.3.0

On this page

# updateBrokerage [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L1402)

Create an unsigned transaction that updates the Super representative brokerage.

## Usage[​](#usage "Direct link to Usage")

```
const transaction = await tronWeb.transactionBuilder.updateBrokerage(brokerage,ownerAddress);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| brokerage | An integer which defines percentage of the brokerage | Number |
| ownerAddress | Account address | String |
| options | Permission id for multi-signature and block header for contract block header info. | `{ permissionId: number, blockHeader: ... }` |

## Returns[​](#returns "Direct link to Returns")

Unsigned transaction object.

## Example[​](#example "Direct link to Example")

```
await tronWeb.transactionBuilder.updateBrokerage(100, "414A193C92CD631C1911B99CA964DA8FD342F4CDDD");  
{  
  visible: false,  
  txID: '754bfc80cf42aa3154fda717262b0ade47ff64b108ad0fdc5f9236d5d4b0ae8a',  
  raw_data: {  
    contract: [ [Object] ],  
    ref_block_bytes: 'c466',  
    ref_block_hash: '150f95204fc606c0',  
    expiration: 1581328767000,  
    timestamp: 1581328708518  
  },  
  raw_data_hex: '0a02c4662208150f95204fc606c04098b0a8f4822e5a55083112510a34747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e55706461746542726f6b6572616765436f6e747261637412190a15414a193c92cd631c1911b99ca964da8fd342f4cddd106470a6e7a4f4822e'  
}
```