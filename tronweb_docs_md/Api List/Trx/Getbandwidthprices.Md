

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getBandwidthPrices
Version: 6.3.0

On this page

# getBandwidthPrices [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L1487)

Query historical bandwidth unit price.

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getBandwidthPrices();
```

## Return[​](#return "Direct link to Return")

String - All historical bandwidth unit price information. Each unit price change is separated by a comma. Before the colon is the millisecond timestamp, and after the colon is the bandwidth unit price in sun. Zero timestamp means that the unit price is valid from the beginning of the chain.

## Example[​](#example "Direct link to Example")

```
//Example 1  
await tronWeb.trx.getBandwidthPrices();  
"0:10"
```