

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* withdrawExpireUnfreeze
Version: 6.3.0

On this page

# withdrawExpireUnfreeze [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L596)

After performing the operation of canceling the stake, the user need to call this interface to retrieve resources after waiting for `N` days. `N` is a TRON network parameter. (v5.1.0 new interface)

## Usage[​](#usage "Direct link to Usage")

```
const transaction = await tronWeb.transactionBuilder.withdrawExpireUnfreeze(address);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameters | Description | Type |
| --- | --- | --- |
| address | refund account address (base58 or hex) | String |
| options | Permission id for multi-signature and block header for contract block header info. | `{ permissionId: number, blockHeader: ... }` |

## Returns[​](#returns "Direct link to Returns")

Unsigned transaction object.

## Example[​](#example "Direct link to Example")

```
const transaction = await tronWeb.transactionBuilder.withdrawExpireUnfreeze('TMVQGm1qAQYVdetCeGRRkTWYYrLXuHK2HC');
```