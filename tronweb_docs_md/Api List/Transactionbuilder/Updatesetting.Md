

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* updateSetting
Version: 6.3.0

On this page

# updateSetting [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L2193)

Create an unsigned transaction that update the `consume_user_resource_percent` parameter of a smart contract.

## Usage[​](#usage "Direct link to Usage")

```
const transaction = await tronWeb.transactionBuilder.updateSetting(contractAddress, consumeUserResourcePercent, ownerAddress, options);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| contractAddress | Smart Contract address string(format:hexstring or base58) | String |
| consumeUserResourcePercent | The percentage of smart contract execution fee paid for by smart contract user. Also known as User Pay Ratio. | Number |
| ownerAddress | Smart contract creator's address(format: hexstring or base58) | String |
| options | Permission id for multi-signature and block header for contract block header info. | `{ permissionId: number, blockHeader: ... }` |

## Returns[​](#returns "Direct link to Returns")

Unsigned transaction object.

## Example[​](#example "Direct link to Example")

```
const transaction = await tronWeb.transactionBuilder.updateSetting("TBQ8ubHnwWAZvHVPJevnKpEfabetDdaQdQ",40,"TTSFjEG3Lu9WkHdp4JrWYhbGP6K1REqnGQ");  
{  
  visible: false,  
  txID: 'eb9ce3d85c033e16e4dd0058d2bdff06857379b534839193bf982c05adebd271',  
  raw_data: {  
    contract: [ [Object] ],  
    ref_block_bytes: '19c3',  
    ref_block_hash: '610212ce583a92aa',  
    expiration: 1581320133000,  
    timestamp: 1581320074559  
  },  
  raw_data_hex: '0a0219c32208610212ce583a92aa4088b399f0822e5a6a082112660a32747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e55706461746553657474696e67436f6e747261637412300a1541bf97a54f4b829c4e9253b26024b1829e1a3b11201215410faf1b6bce9e815555544aea9d350f9d3dc6d3ba182870bfea95f0822e'  
}
```