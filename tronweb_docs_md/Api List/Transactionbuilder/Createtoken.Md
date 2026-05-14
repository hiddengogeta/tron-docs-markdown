

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* createToken
Version: 6.3.0

On this page

# createToken [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L1429)

Create an unsigned transaction that issue TRC10 token.

## Usage[​](#usage "Direct link to Usage")

```
const trcOptions = {  
  name: 'test', // Token name, default string  
  abbreviation: 'tt', // Token name abbreviation, default string  
  description: 'fortest', // Token description, optional  
  url: 'tronweb.network', // Token official website url, default string  
  totalSupply: 100000, // Token total supply  
  trxRatio: 1, // Define the price by the ratio of trx_num/num  
  tokenRatio: 1, // Define the price by the ratio of trx_num/num  
  saleStart: 1581047830000, // ICO start time  
  saleEnd: 1681047110000, // ICO end time  
  freeBandwidth: 0, // The creator's "donated" bandwidth for use by token holders, optional  
  freeBandwidthLimit: 0, // Out of `totalFreeBandwidth`, the amount each token holder get, optional  
  frozenAmount: 0, // Token staked supply  
  frozenDuration: 0, // for now there is no default for the following values  
  precision: 6, // Precision of issued tokens  
  permissionId: 2, // Optional, for multi-signature use  
  blockHeader: {...} // Optional, for contract block header info.  
};  
const transaction = await tronWeb.transactionBuilder.createToken(trcOptions, issuerAddress);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| options | Options to create TRC10 token | object |
| issuerAddress | Address of issuer in hex or base58 | string |

## Returns[​](#returns "Direct link to Returns")

Unsigned transaction object.

## Example[​](#example "Direct link to Example")

```
const trcOptions = {  
  name : "test",  
  abbreviation : "tt",  
  description : "fortest",  
  url : "tronweb.network",  
  totalSupply : 100000,  
  trxRatio : 1,  
  tokenRatio : 1,  
  saleStart : 1581047830000,  
  saleEnd : 1681047110000,  
  freeBandwidth : 0,  
  freeBandwidthLimit : 0,  
  frozenAmount : 0,  
  frozenDuration : 0,  
  precision : 6  
};  
await tronWeb.transactionBuilder.createToken(trcOptions,"41BF97A54F4B829C4E9253B26024B1829E1A3B1120");  
{  
  visible: false,  
  txID: '5a2b16c0436dddd6378a29087ba1e924b9a55f6bc2978554a0830cf741b1c03e',  
  raw_data: {  
    contract: [ [Object] ],  
    ref_block_bytes: 'b756',  
    ref_block_hash: '64bdb1724356ee49',  
    expiration: 1581047856000,  
    timestamp: 1581047797358  
  },  
  raw_data_hex: '0a02b756220864bdb1724356ee494080f7aeee812e5a8b0108061286010a2f747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e41737365744973737565436f6e747261637412530a1541bf97a54f4b829c4e9253b26024b1829e1a3b11201204746573741a02747420a08d0630013806400148f0abadee812e50f082ddb1f630a20107666f7274657374aa010d7777772e62616964752e636f6d70eeacabee812e'  
}
```