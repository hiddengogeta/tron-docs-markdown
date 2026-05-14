

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* freezeBalanceV2
Version: 6.3.0

On this page

# freezeBalanceV2 [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L356)

The interface used to stake and obtain resources. The resource type can be specified as `BANDWIDTH` or `ENERGY`. (v5.1.0 new interface)

## Usage[​](#usage "Direct link to Usage")

```
const transaction = await tronWeb.transactionBuilder.freezeBalanceV2(amount, resource, address, options);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameters | Description | Type |
| --- | --- | --- |
| amount | The amount of assets to be frozen (sun), larger than 0 | Integer |
| resource | The frozen asset type, optional `BANDWIDTH` or `ENERGY` | String |
| address | The account address of the frozen asset (base58 or hex) | String |
| options | optional. Permission id for multi-sign and block header for contract block header info. | `{ permissionId: number, blockHeader: ... }` |

## Returns[​](#returns "Direct link to Returns")

Unsigned transaction object.

## Example[​](#example "Direct link to Example")

```
const transaction = await tronWeb.transactionBuilder.freezeBalanceV2(10e6, 'BANDWIDTH', 'TMVQGm1qAQYVdetCeGRRkTWYYrLXuHK2HC');
```