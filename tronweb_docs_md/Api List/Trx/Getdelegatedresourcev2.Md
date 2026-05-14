

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getDelegatedResourceV2
Version: 6.3.0

On this page

# getDelegatedResourceV2 [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L1095)

Query the resources that an account delegates to another account under the V2 interface. (v5.1.0 new interface)

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getDelegatedResourceV2(fromAddress, toAddress, options)
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameters | Parameter Description | Data Type |
| --- | --- | --- |
| fromAddress | resource from account address (base58 or hex) | String |
| toAddress | resource to account address (base58 or hex) | String |
| options | Optional. Default is `{ confirmed: true }`. If `options.confirmed` is `true`, the result is queried from solidity node. | `{ confirmed: boolean }` |

## Return[​](#return "Direct link to Return")

Object - Delegated resource information, see the example below.

## Example[​](#example "Direct link to Example")

```
await tronWeb.trx.getDelegatedResourceV2('TMVQGm1qAQYVdetCeGRRkTWYYrLXuHK2HC', 'TDvSsdrNM5eeXNL3czpa6AxLDHZA9nwe9K');  
{  
    "delegatedResource": [  
        {  
            "from": "TMVQGm1qAQYVdetCeGRRkTWYYrLXuHK2HC",  
            "to": "TDvSsdrNM5eeXNL3czpa6AxLDHZA9nwe9K",  
            "frozen_balance_for_bandwidth": 10000000  
        }  
    ]  
}
```