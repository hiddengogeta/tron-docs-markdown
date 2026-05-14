

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* createAccount
Version: 6.3.0

On this page

# createAccount [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L1582)

Create a unsigned transaction to active an account.

## Usage[​](#usage "Direct link to Usage")

```
const transaction = await tronWeb.transactionBuilder.createAccount(address, options);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| address | Account address to be activated in hex format(hexstring or base58) | string |
| options | Optional. The permission id for multi-signature and block header for contract block header info. | `{ permissionId: number, blockHeader: ... }` |

## Returns[​](#returns "Direct link to Returns")

Object - Transaction created to activate an account.

## Example[​](#example "Direct link to Example")

```
const transaction = await tronWeb.transactionBuilder.createAccount('TZ4UXDV5ZhNW7fb2AMSbgfAEZ7hWsnYS2g');  
  
const signedTransaction = await tronWeb.trx.sign(transaction);  
  
const result = await tronWeb.trx.sendRawTransaction(signedTransaction);
```