

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* createProposal
Version: 6.3.0

On this page

# createProposal [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L1788)

Create an unsigned transaction that creates a proposal.

## Usage[​](#usage "Direct link to Usage")

```
const transaction = await tronWeb.transactionBuilder.createProposal(parameters, issuerAddress, options);
```

**Note**:
parameters need to be sorted according to the stringified key order. For example:

```
parameters = parameters.sort((a, b) => {  
  return a.key.toString() > b.key.toString() ? 1 : -1;  
});
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| parameters | Proposal parameters | `Array<{ key: string, value: string}>` |
| issuerAddress | Creator address(format in hexstring or base58) | string |
| options | Optional. The permission id for multi-signature and block header for contract block header info. | `{ permissionId: number, blockHeader: ... }` |

## Returns[​](#returns "Direct link to Returns")

Unsigned transaction object.

## Example[​](#example "Direct link to Example")

```
await tronWeb.transactionBuilder.createProposal([{ "key": 32, "value": 1 }, { "key": 33, "value": 11 }],"41BF97A54F4B829C4E9253B26024B1829E1A3B1120");  
{  
  visible: false,  
  txID: '771d2fe10099dd2d48e9f874bc7c17a5882c77bca2622fbb695cc59327e1bc08',  
  raw_data: {  
    contract: [ [Object] ],  
    ref_block_bytes: 'ba3b',  
    ref_block_hash: 'e09ff41b96e649f1',  
    expiration: 1581050079000,  
    timestamp: 1581050021547  
  },  
  raw_data_hex: '0a02ba3b2208e09ff41b96e649f14098ceb6ef812e5a5e0810125a0a33747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e50726f706f73616c437265617465436f6e747261637412230a1541bf97a54f4b829c4e9253b26024b1829e1a3b112012040820100112040821100b70ab8db3ef812e'  
}
```