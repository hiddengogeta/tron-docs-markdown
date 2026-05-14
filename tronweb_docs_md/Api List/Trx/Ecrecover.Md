

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* ecRecover
Version: 6.3.0

On this page

# ecRecover [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L542)

Recover the address(es) of the signer(s) from a signed transaction.

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.ecRecover(signedTransaction)
```

## Parameter[​](#parameter "Direct link to Parameter")

A signed transaction

## Return[​](#return "Direct link to Return")

Base58 address or array of base58 address recovered from the signature(s) of the signed transaction.

```
const pk1 = '...';  
const pk2 = '...';  
const tx = await tronWeb.transactionBuilder.sendTrx('to', 100);  
const signedTransaction = await tronWeb.trx.sign(tx, pk1);  
  
// Recover address of a signed transaction with one signer.  
const a = await tronWeb.trx.ecRecover(signedTransaction);  
// a === tronWeb.address.fromPrivateKey(pk1);  
  
// Recover addresses of a signed transaction with more than one signer.  
const signedTx = await tronWeb.trx.sign(tx, pk2);  
const b = await tronWeb.trx.ecRecover(signedTx);  
// b is deep equal to [tronWeb.address.fromPrivateKey(pk1), tronWeb.address.fromPrivateKey(pk2)].
```