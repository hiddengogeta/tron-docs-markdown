

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getUnconfirmedBrokerage
Version: 6.3.0

On this page

# getUnconfirmedBrokerage [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L1434)

Query unconfirmed brokerage.

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getUnconfirmedBrokerage(address)
```

## Parameters[​](#parameters "Direct link to Parameters")

Address string(in either HexString or Base58 format)

## Return[​](#return "Direct link to Return")

Number - The unconfirmed brokerage of the address.

## Example[​](#example "Direct link to Example")

```
//Parameter Base58  
await tronWeb.trx.getUnconfirmedBrokerage("TLyqzVGLV1srkB7dToTAEqgDSfPtXRJZYH");  
20  
  
//Parameter HexString  
await tronWeb.trx.getUnconfirmedBrokerage("4178C842EE63B253F8F0D2955BBC582C661A078C9D");  
20
```