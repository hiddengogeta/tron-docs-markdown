

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* delegateResource
Version: 6.3.0

On this page

# delegateResource [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L467)

After staking and obtaining resources, resources can be delegated to multiple recipients through this interface. The optional `lock` parameter can specify whether the delegation can be revoked within 3 days. (v5.1.0 new interface)

**Note:**
In versions before 6.x, most methods support variable parameter length. For example, the following codes are both valid:

```
// Normally the third parameter is 'fromAddress', and the forth is options.  
await tronWeb.transactionBuilder.delegateResource(10e6, 'toAddress', 'BANDWIDTH', 'fromAddress', false, 0, { permissionId: 2 });  
  
// If the third parameter is object, it will be treated as options and fromAddress will be tronWeb.defaultAddress.  
await tronWeb.transactionBuilder.delegateResource(10e6, 'toAddress', 'BANDWIDTH', 'fromAddress', false, { permissionId: 2 });
```

In v6.x, we do **not** support ignoring some of the arguments between required arguments and object arguments such as `options` with `permissioinId`.

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.transactionBuilder.delegateResource(amount, receiverAddress, resource, address, lock, lockPeriod, options);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| amount | The amount of assets in `sun` to be delegated, larger than 0 | Integer |
| receiverAddress | The account address of receiving delegation (base58 or hex) | String |
| resource | Asset type to be delegated. Optional, the default is `BANDWIDTH`. | `BANDWIDTH` or `ENERGY` |
| address | Owner address (base58 or hex) | String |
| lock | If the `lock` is `true`, delegation can not be revoked within 3 days. The default is `false` | Boolean |
| lockPeriod | When `lock` is `true`, this parameter will set the lock time, with the unit of blocks. And the new resource delegating to the same address of same type should have this `lockPeriod` value larger than the lockup blocks left of the address. | Integer |
| options | The permission id, optional, for multi-signature and block header for contract block header info. | `{ permissionId: number, blockHeader: ... }` |

## Returns[​](#returns "Direct link to Returns")

Unsigned transaction object.

## Example[​](#example "Direct link to Example")

```
const transaction = await tronWeb.transactionBuilder.delegateResource(10e6, 'receiverAddress', 'BANDWIDTH', 'TMVQGm1qAQYVdetCeGRRkTWYYrLXuHK2HC', true, 86400);
```