

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getBandwidth
Version: 6.3.0

On this page

# getBandwidth [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L356)

Query the Bandwidth information for the account.

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getBandwidth(address);
```

## Parameters[​](#parameters "Direct link to Parameters")

Address string(in either HexString or Base58 format)

## Return[​](#return "Direct link to Return")

Number - The account's bandwidth.

## Example[​](#example "Direct link to Example")

```
//Example 1  
await tronWeb.trx.getBandwidth('TVJ6njG5EpUwJt4N9xjTrqU5za78cgadS2');  
5000  
  
//Example 2  
await tronWeb.trx.getBandwidth('41D3FD1B6F3F3A86303E2925844456C49876C4561F');  
5000
```