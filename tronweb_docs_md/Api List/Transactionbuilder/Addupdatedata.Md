

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* addUpdateData
Version: 6.3.0

On this page

# addUpdateData [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L2461)

add memo to an unsigned transaction.

## Usage[​](#usage "Direct link to Usage")

```
const transaction = await tronWeb.transactionBuilder.addUpdateData(unsignedTransaction, memo, dataFormat, options);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| unsignedTransaction | Unsigned transaction object. | JSON |
| memo | Memo info | Utf8 string or Hex string |
| dataFormat | Optional. The format of `memo` parameter. If the `memo` is hex string, this parameter should be `hex`. Default is `utf8`. | `hex` or `utf8` |
| options | Optional. Options for `addUpdateData`. If `options.txLocal` is true, it will build locally. Default is `{ txLocal: false }`. | `{ txLocal: boolean }` |

## Returns[​](#returns "Direct link to Returns")

The new transaction object. The added memo is stored in `raw_data.data` property.

**Note**:

* The Transaction hash(Transaction ID) will be changed after `addUpdateData` was executed as a new transaction object is generated.
* Please use the newly generated `transaction` for subsequent processes like `tronweb.trx.sign(transaction)` or `tronweb.trx.broadcast(transaction)`.
* From v6.0.4, `addUpdateData` will use `TronWeb.fromUtf8` to convert the provided data string-unless it starts with '0x'. If the resulting data string has an odd length, a '0' will be prepended to ensure even length.

## Example[​](#example "Direct link to Example")

```
var txn = await tronWeb.transactionBuilder.sendTrx("TUoHaVjx7n5xz8LwPRDckgFrDWhMhuSuJM", 100, "TUznHJfHe6gdYY7gvWmf6bNZHuPHDZtowf");  
var nexTxn = await tronWeb.transactionBuilder.addUpdateData(txn,"test");  
var signedtxn = await tronWeb.trx.sign(nexTxn, privateKey);  
console.log(nexTxn)  
{  
  visible: false,  
  txID: "8c3a4b4c20cfdf8df340905949a8241aee639492e0c4d73f1bf18847346444f1",  
  raw_data: {  
    contract: [ [Object] ],  
    data: "74657374", // this is the HexString of memo  
    expiration: 1628073045000,  
    ref_block_bytes: "7254",  
    ref_block_hash: "c45fff3a6a0347cc",  
    timestamp: 1628072986845  
  },  
  raw_data_hex: "0a0272542208c45fff3a6a0347cc4088d8dc85b12f5204746573745a65080112610a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412300a1541d0b69631440f0a494bb51f7eee68ff5c593c00f0121541ce8a0cf0c16d48bcf22825f6053248df653c89ca186470dd91d985b12f"  
}
```