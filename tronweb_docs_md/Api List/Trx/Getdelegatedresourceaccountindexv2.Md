

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getDelegatedResourceAccountIndexV2
Version: 6.3.0

On this page

# getDelegatedResourceAccountIndexV2 [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L1130)

Query which accounts have delegated resources to other accounts under the V2 interface. (v5.1.0 new interface)

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getDelegatedResourceAccountIndexV2(address, options)
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameters | Parameter Description | Data Type |
| --- | --- | --- |
| address | account address (base58 or hex) | String |
| options | Optional. Default is `{ confirmed: true }`. If `options.confirmed` is `true`, the result is queried from solidity node. | `{ confirmed: boolean }` |

## Return[​](#return "Direct link to Return")

Object - `fromAccounts` prop shows the list of addresses that have delegated resources to the account, `toAccounts` prop shows the list of addresses that the account has delegated resources to.

## Example[​](#example "Direct link to Example")

```
await tronWeb.trx.getDelegatedResourceAccountIndexV2('TMVQGm1qAQYVdetCeGRRkTWYYrLXuHK2HC');  
{  
    "account": "TMVQGm1qAQYVdetCeGRRkTWYYrLXuHK2HC",  
    "fromAccounts": [  
        "TKTX96CBxr5kvhjsDHcqoiPWZageGxoTW3"  
    ],  
    "toAccounts": [  
        "TDvSsdrNM5eeXNL3czpa6AxLDHZA9nwe9K"  
    ]  
}
```