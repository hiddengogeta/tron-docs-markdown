

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getAvailableUnfreezeCount
Version: 6.3.0

On this page

# getAvailableUnfreezeCount [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L1187)

Query the number of times an account can operate UnFreezeBalanceV2 to unfreeze under the V2 interface. (v5.1.0 new interface)

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getAvailableUnfreezeCount(address, options);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parametersf | Parameter Description | Type |
| --- | --- | --- |
| address | account address (base58 or hex) | String |
| options | Optional. Default is `{ confirmed: true }`. If `options.confirmed` is `true`, the result is queried from solidity node. | `{ confirmed: boolean }` |

## Return[​](#return "Direct link to Return")

Object - An object including the number of times an account can operate UnFreezeBalanceV2 to unfreeze, see the example below.

## Example[​](#example "Direct link to Example")

```
await tronWeb.trx.getAvailableUnfreezeCount('TMVQGm1qAQYVdetCeGRRkTWYYrLXuHK2HC');  
{  
    "count": 32  
}
```