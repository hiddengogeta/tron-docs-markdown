

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* applyForSR
Version: 6.3.0

On this page

# applyForSR [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L648)

Create an unsigned transaction that apply to be an SR. The balance of the applied account
needs to be at least 9999 TRX, and the operation will consume 9999 TRX.

## Usage[​](#usage "Direct link to Usage")

```
// Format  
const transaction = await tronWeb.transactionBuilder.applyForSR(address, url, options);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| address | The account address applied for SR in hex format(hexstring or base58) | string |
| url | SR URL link | string |
| options | Optional. The permission id for multi-signature and block header for contract block header info. | `{ permissionId: number, blockHeader: ... }` |

## Returns[​](#returns "Direct link to Returns")

Unsigned transaction object.

## Example[​](#example "Direct link to Example")

```
const result = await tronWeb.transactionBuilder.applyForSR("41BF97A54F4B829C4E9253B26024B1829E1A3B1120", "www.fortest.com");  
console.log(result)  
{  
  visible: false,  
  txID: '388172e15216a6eb216a11ed312c3794ce50dd85873e83767b6c5bea1da78b43',  
  raw_data: {  
    contract: [ [Object] ],  
    ref_block_bytes: '499a',  
    ref_block_hash: '05853c8ec7523765',  
    expiration: 1580963556000,  
    timestamp: 1580963496941  
  },  
  raw_data_hex: '0a02499a220805853c8ec752376540a0d595c6812e5a620805125e0a32747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5769746e657373437265617465436f6e747261637412280a1541bf97a54f4b829c4e9253b26024b1829e1a3b1120120f7777772e666f72746573742e636f6d70ed8792c6812e'  
}
```