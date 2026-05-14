

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* cancelUnfreezeBalanceV2
Version: 6.3.0

On this page

# cancelUnfreezeBalanceV2 [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L442)

Support canceling unstaking in Stake 2.0, which means that users can use this API to cancel unstaking in waiting period time, make the unstaking TRX restaked, and meanwhile help users withdraw the TRX expired waiting period to balance. (v5.3.0 new interface)

## Usage[​](#usage "Direct link to Usage")

```
const transaction = await tronWeb.transactionBuilder.cancelUnfreezeBalanceV2(address);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| address | Restack account address (base58 or hex) | String |
| options | Optional. The permission id for multi-signature and block header for contract block header info. | `{ permissionId: number, blockHeader: ... }` |

## Returns[​](#returns "Direct link to Returns")

Unsigned transaction object.

## Example[​](#example "Direct link to Example")

```
const transaction = await tronWeb.transactionBuilder.cancelUnfreezeBalanceV2('TMVQGm1qAQYVdetCeGRRkTWYYrLXuHK2HC');
```