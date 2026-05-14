

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getBrokerage
Version: 6.3.0

On this page

# getBrokerage [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L1429)

Get SR brokerage ratio

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getBrokerage(address);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameters | Parameter Description | Data Type |
| --- | --- | --- |
| address | account address | string |

## Return[​](#return "Direct link to Return")

Number - SR brokerage ratio.

## Example[​](#example "Direct link to Example")

```
await tronWeb.trx.getBrokerage("TBtrUZ2DXdsBGhpquSPkoEcD2KbWx2rZvE");  
20
```