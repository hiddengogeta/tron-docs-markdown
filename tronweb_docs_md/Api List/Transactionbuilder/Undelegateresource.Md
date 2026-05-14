

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* undelegateResource
Version: 6.3.0

On this page

# undelegateResource [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L541)

The interface used to revoke delegated resource, which can specify the number of revoked resources. (v5.1.0 new interface)

## Usage[​](#usage "Direct link to Usage")

```
const transaction = await tronWeb.transactionBuilder.undelegateResource(amount, receiverAddress, resource, address, options);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| amount | The amount of assets to be revoked (sun), larger than 0 | String |
| receiverAddress | The account address to receive revoked delegation (base58 or hex) | String |
| resource | Optional. Asset type of revoked delegation. Default is `BANDWIDTH`. | `BANDWIDTH` or `ENERGY` |
| address | The account address of the revoked delegation asset (base58 or hex) | Number |
| options | Permission id for multi-sign and block header for contract block header info. | `{ permissionId: number, blockHeader: ... }` |

## Returns[​](#returns "Direct link to Returns")

Unsigned transaction object.

## Example[​](#example "Direct link to Example")

```
const transaction = await tronWeb.transactionBuilder.undelegateResource(10e6, 'receiverAddress', 'BANDWIDTH', 'TMVQGm1qAQYVdetCeGRRkTWYYrLXuHK2HC');
```