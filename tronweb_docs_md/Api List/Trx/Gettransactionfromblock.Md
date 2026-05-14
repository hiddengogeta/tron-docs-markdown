

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getTransactionFromBlock
Version: 6.3.0

On this page

# getTransactionFromBlock [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L144)

Returns a transaction based on a block hash or number and the transactions index position.

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getTransactionFromBlock(blockNumberOrBlockHash, index)
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameters | Parameter Description | Data Type |
| --- | --- | --- |
| Block height | A block number or hash. | Integer / String |
| Number | The transactions index position | Integer |

## Return[​](#return "Direct link to Return")

Object - The transaction information, see examples below.

## Example[​](#example "Direct link to Example")

```
//示例1  
await tronWeb.trx.getTransactionFromBlock(55636269, 0);  
{  
  ret: [ { contractRet: 'SUCCESS' } ],  
  signature: [  
    '9ee35a0e3dc506bca75da2558a3dae1b8b9c9a9841cc4478ad32ff2f8f2bcea93ede5cd8007858459a85fb420f4ad2e31ad0674d02a8f231f0fcb4105490421101'  
  ],  
  txID: 'e092065f8cd1a2ef8cd6612201a3ad8c537811683fc981efdc205f040eddad25',  
  raw_data: {  
    contract: [ [Object] ],  
    ref_block_bytes: 'f11a',  
    ref_block_hash: 'ab04b2f2b405e321',  
    expiration: 1743156774000,  
    timestamp: 1743156715258  
  },  
  raw_data_hex: '0a02f11a2208ab04b2f2b405e32140f088f6e1dd325a67080112630a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412320a15417b423f463091952d203ca5f917fd5e035a17f8ff12154120d6861364c8341fe02336036d500d09a67fae2d18cdb10570fabdf2e1dd32'  
}  
  
//示例2  
await tronWeb.trx.getTransactionFromBlock("000000000350f12d2af360c5d2ab81752fb914fc77620cd2ca1a2bf8fc674452", 0);  
{  
  ret: [ { contractRet: 'SUCCESS' } ],  
  signature: [  
    '9ee35a0e3dc506bca75da2558a3dae1b8b9c9a9841cc4478ad32ff2f8f2bcea93ede5cd8007858459a85fb420f4ad2e31ad0674d02a8f231f0fcb4105490421101'  
  ],  
  txID: 'e092065f8cd1a2ef8cd6612201a3ad8c537811683fc981efdc205f040eddad25',  
  raw_data: {  
    contract: [ [Object] ],  
    ref_block_bytes: 'f11a',  
    ref_block_hash: 'ab04b2f2b405e321',  
    expiration: 1743156774000,  
    timestamp: 1743156715258  
  },  
  raw_data_hex: '0a02f11a2208ab04b2f2b405e32140f088f6e1dd325a67080112630a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412320a15417b423f463091952d203ca5f917fd5e035a17f8ff12154120d6861364c8341fe02336036d500d09a67fae2d18cdb10570fabdf2e1dd32'  
}
```