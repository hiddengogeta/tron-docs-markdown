

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getCanDelegatedMaxSize
Version: 6.3.0

On this page

# getCanDelegatedMaxSize [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L1154)

Query the maximum value of an account's delegated resources (BANDWIDTH, ENERGY) that can be operated on DelegateResource under the V2 interface. (v5.1.0 new interface)

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getCanDelegatedMaxSize(address, resource，options);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameters | Parameter Description | Data Type |
| --- | --- | --- |
| address | account address (base58 or hex) | String |
| resource | resource type, optional `BANDWIDTH` or `ENERGY` | String |
| options | Optional. Default is `{ confirmed: true }`. If `options.confirmed` is `true`, the result is queried from solidity node. | `{ confirmed: boolean }` |

## Return[​](#return "Direct link to Return")

Object - An object including the maximum value of an account's delegated resources (BANDWIDTH, ENERGY) that can be operated on DelegateResource under the V2 interface.

## Example[​](#example "Direct link to Example")

```
await tronWeb.trx.getCanDelegatedMaxSize('TMVQGm1qAQYVdetCeGRRkTWYYrLXuHK2HC'，'BANDWIDTH');  
{  
    "max_size": 100000000  
}
```