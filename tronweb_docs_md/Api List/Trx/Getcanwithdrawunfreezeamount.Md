

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getCanWithdrawUnfreezeAmount
Version: 6.3.0

On this page

# getCanWithdrawUnfreezeAmount [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L1209)

Query an account under the V2 interface, if you operate WithdrawExpireUnfreeze to withdraw the principal, the amount of withdrawal principal that can be obtained. (v5.1.0 new interface)

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getCanWithdrawUnfreezeAmount(address, timestamp, options);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameters | Parameter Description | Data Type |
| --- | --- | --- |
| address | account address (base58 or hex) | String |
| timestamp | query cutoff timestamp(millisecond), larger than 0, default is Date.now() | Integer |
| options | Optional. Default is `{ confirmed: true }`. If `options.confirmed` is `true`, the result is queried from solidity node. | `{ confirmed: boolean }` |

## Return[​](#return "Direct link to Return")

Object - An object including the amount of withdrawal principal that can be obtained.

## Example[​](#example "Direct link to Example")

```
await tronWeb.trx.getCanWithdrawUnfreezeAmount('TMVQGm1qAQYVdetCeGRRkTWYYrLXuHK2HC', Date.now());  
{  
    "amount": 9000000  
}
```