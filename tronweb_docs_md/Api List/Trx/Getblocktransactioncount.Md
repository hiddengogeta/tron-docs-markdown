

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getBlockTransactionCount
Version: 6.3.0

On this page

# getBlockTransactionCount [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L137)

Retrieves the count of transactions within a block.

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getBlockTransactionCount(blockHeightOrBlockHash)
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameters | Parameter Description | Data Type |
| --- | --- | --- |
| Block Height or Block Hash | The height of the block or the block hash you wish to obtain transaction count data for. | Integer/string |

## Return[​](#return "Direct link to Return")

Number - The number of transactions in the block.

## Example[​](#example "Direct link to Example")

```
await tronWeb.trx.getBlockTransactionCount(16012520);  
35  
await tronWeb.trx.getBlockTransactionCount("0000000000f454e84edbee2365fbf1bf34bc98283ded06e68311bb6e5bea3cf6");  
35
```