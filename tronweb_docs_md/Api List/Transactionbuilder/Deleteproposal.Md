

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* deleteProposal
Version: 6.3.0

On this page

# deleteProposal [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L1828)

Create a transaction that deletes a proposal.

## Usage[​](#usage "Direct link to Usage")

```
const transaction = await tronWeb.transactionBuilder.deleteProposal(proposalId, issuerAddress, options);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| proposalId | Integer type proposal id | Integer |
| issuerAddress | Proposal issuer address in hex string | string |
| options | The permission id, optional, for multi-signature and block header for contract block header info. | `{ permissionId: number, blockHeader: ... }` |

## Returns[​](#returns "Direct link to Returns")

Unsigned transaction object.

## Example[​](#example "Direct link to Example")

```
//example 1  
await tronWeb.transactionBuilder.deleteProposal(1, "41010D3A8E0D80F8C83148240202DD178DF495B7BD", { permissionId: 2 });  
{  
  visible: false,  
  txID: '1152c19215aaefffe166cf9fcd6a299b06f532f8ec4b62b9804338fbe533308d',  
  raw_data: {  
    contract: [ [Object] ],  
    ref_block_bytes: '03cf',  
    ref_block_hash: 'ec181002d427df4c',  
    expiration: 1581332046000,  
    timestamp: 1581331986337  
  },  
  raw_data_hex: '0a0203cf2208ec181002d427df4c40b0c1f0f5822e5a54081212500a33747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e50726f706f73616c44656c657465436f6e747261637412190a1541010d3a8e0d80f8c83148240202dd178df495b7bd100170a1efecf5822e'  
}  
  
//example 2  
await tronWeb.transactionBuilder.deleteProposal(1, "TA4mXQ6rMNSBcvd9Kn9LLFS4bbX8b27RCS");  
{  
  visible: false,  
  txID: '512a758fc5b87615b10c28f840d72f977286384e77959a421c2470bd580f2845',  
  raw_data: {  
    contract: [ [Object] ],  
    ref_block_bytes: '04bb',  
    ref_block_hash: 'ca274c26abdb1fc6',  
    expiration: 1581332754000,  
    timestamp: 1581332694494  
  },  
  raw_data_hex: '0a0204bb2208ca274c26abdb1fc640d0dc9bf6822e5a54081212500a33747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e50726f706f73616c44656c657465436f6e747261637412190a1541010d3a8e0d80f8c83148240202dd178df495b7bd100170de8b98f6822e'  
}
```