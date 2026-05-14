

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getEnergyPrices
Version: 6.3.0

On this page

# getEnergyPrices [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L1497)

Query historical energy unit price.

## Usage[​](#usage "Direct link to Usage")

```
await tronWeb.trx.getEnergyPrices();
```

## Return[​](#return "Direct link to Return")

string - All historical energy unit price information. Each unit price change is separated by a comma. Before the colon is the millisecond timestamp, and after the colon is the energy unit price in sun.

## Example[​](#example "Direct link to Example")

```
//Example 1  
await tronWeb.trx.getEnergyPrices();  
"0:100"
```