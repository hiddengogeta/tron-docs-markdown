

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* unfreezeBalanceV2
Version: 6.3.0

On this page

# unfreezeBalanceV2 [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L399)

The interface used to cancel the staked resources. It can specify the number of canceled stakes, but the number cannot exceed the number that can be canceled. The delegated resources cannot be canceled. (v5.1.0 new interface)

## Usage[​](#usage "Direct link to Usage")

```
const transaction = await tronWeb.transactionBuilder.unfreezeBalanceV2(amount, resource, address, options);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| amount | the amount of assets to be frozen (sun), larger than 0 | Integer |
| resource | Optional. The frozen asset type. Default is `BANDWIDTH`. | `BANDWIDTH` or `ENERGY` |
| address | the account address of the frozen asset (base58 or hex) | String |
| options | Permission id for multi-signature and block header for contract block header info. | `{ permissionId: number, blockHeader: ... }` |

## Returns[​](#returns "Direct link to Returns")

Unsigned transaction object.

## Example[​](#example "Direct link to Example")

```
const transaction = await tronWeb.transactionBuilder.unfreezeBalanceV2(10e6, 'BANDWIDTH', 'TMVQGm1qAQYVdetCeGRRkTWYYrLXuHK2HC')
```