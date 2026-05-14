

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* voteProposal
Version: 6.3.0

On this page

# voteProposal [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L1866)

Create an unsigned transaction that to approve a proposal.

## Usage[​](#usage "Direct link to Usage")

```
const transaction = await tronWeb.transactionBuilder.voteProposal(proposalId, hasApproval, voterAddress, options);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| proposalId | Integer type proposal id | Integer |
| hasApproval | Approving the proposal or not. | Boolean |
| issuerAddress | The address that makes the approve action ,format:hexstring or base58 | String |
| options | Permission id for multi-signature and block header for contract block header info. | `{ permissionId: number, blockHeader: ... }` |

## Returns[​](#returns "Direct link to Returns")

Unsigned transaction object.

## Example[​](#example "Direct link to Example")

```
await tronWeb.transactionBuilder.voteProposal(32,true,"TNDFkUNA2TukukC1Moeqj61pAS53NFchGF");  
{  
  visible: false,  
  txID: 'e214267985087a1820a8533586f5c7db010084f8caa109f967a57e8fbc035a1b',  
  raw_data: {  
    contract: [ [Object] ],  
    ref_block_bytes: '1dca',  
    ref_block_hash: 'cb1fd6e2719cef8c',  
    expiration: 1581399042000,  
    timestamp: 1581398984483  
  },  
  raw_data_hex: '0a021dca2208cb1fd6e2719cef8c40d0cfe995832e5a860108041281010a30747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e566f74655769746e657373436f6e7472616374124d0a1541bf97a54f4b829c4e9253b26024b1829e1a3b112012190a15414a193c92cd631c1911b99ca964da8fd342f4cddd100112190a154178c842ee63b253f8f0d2955bbc582c661a078c9d100170a38ee695832e'  
}
```