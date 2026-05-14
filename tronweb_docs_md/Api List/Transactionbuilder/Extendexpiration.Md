

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* extendExpiration
Version: 6.3.0

On this page

# extendExpiration [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L2457)

Extend unsigned transaction expiration time in seconds.

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.transactionBuilder.extendExpiration(transaction, extension, options);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| transaction | The transaction object | Object |
| extension | Extension of the expiration time in seconds | Integer |
| options | Optional. Options for extendExpiration | object |
| options.txLocal | Optional. Default is `false`. If is `true`, transaction will be build locally | boolean |

## Returns[​](#returns "Direct link to Returns")

Unsigned transaction object.

**Note**:
The Transaction hash(Transaction ID) will be changed after
"extendExpiration" was executed as a new transaction object is
generated. Please use the newly generated Transactions for subsequent
processes like `sign` or `broadcast`.

## Example[​](#example "Direct link to Example")

```
const transaction = await tronWeb.transactionBuilder.sendTrx("TNo9e8MWQpGVqdyySxLSTw3gjgFQWE3vfg", 100, "TM2TmqauSEiRf16CyFgzHV2BVxBejY9iyR");    
const extendExpirationObj =  await tronWeb.transactionBuilder.extendExpiration(transaction, 500);  
const signedtxn = await tronWeb.trx.sign(extendExpirationObj, privateKey);  
console.log(extendExpirationObj);  
{txID: "a33e940480202c8d38c65a571a699be4e082e40776bab0000103c8cca63f6cb4", raw_data: {}, raw_data_hex: "0a02c9bc2208a506a5de6e7a02c040d0c48fd3822e5a650801…d4fa7b33c9645a2276dc9b192902e2d186470e7b1edd2822e", visible: false}
```