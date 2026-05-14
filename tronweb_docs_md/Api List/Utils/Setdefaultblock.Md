

* [API List](/docu/docs/API List/)
* utils
* setDefaultBlock
Version: 6.3.0

On this page

# setDefaultBlock [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/tronweb.ts#L153)

Sets the default block used as a reference for tronWeb.trx.getBlock, tronWeb.trx.getBlockTransactionCount, tronWeb.trx.getTransactionFromBlock

## Usage[​](#usage "Direct link to Usage")

```
TronWeb.setDefaultBlock(blockID);
```

## Parameter[​](#parameter "Direct link to Parameter")

| Parameter | Description | Data Type |
| --- | --- | --- |
| blockID | Possible input values can be `latest`, `earliest`, left blank or block number.   `latest`: The reference block is the latest block   `earliest`: The reference block is the genesis block   left blank: No reference block   block number: The reference block is the corresponding block | Number / String |

## Returns[​](#returns "Direct link to Returns")

String or false or Number - The same as the input parameter.

## Example[​](#example "Direct link to Example")

```
tronWeb.setDefaultBlock('latest');  
'latest'  
  
tronWeb.setDefaultBlock();  
false  
  
tronWeb.setDefaultBlock('earliest');  
'earliest'  
  
tronWeb.setDefaultBlock(585367);  
585367
```