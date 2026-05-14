

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* unfreezeBalance
Version: 6.3.0

On this page

# unfreezeBalance [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L310)

Creates an unsigned unfreeze TRX transaction. This unfreezes TRX for the
specified resource. If you unfreeze for BANDWIDTH, it removes TRON
POWER, which also removes VOTES. If the bandwidth is already spent, the
account will be negative for bandwidth.

## Usage[​](#usage "Direct link to Usage")

```
const transaction = await tronWeb.transactionBuilder.unfreezeBalance(resource, ownerAddress, receiverAddress, options);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| resource | Optional. Specifying the resource type. Default is `BANDWIDTH`. | `BANDWIDTH` or `ENERGY` |
| address (optional) | Address of the owner of the TRX to be unstaked (defaults to caller's default address).(format:hexstring or base58) | String |
| receiver address | Address of user in which the resource is being removed from, due to unstake.(hexstring or base58) | String |
| options | Permission id for multi-signature and block header for contract block header info. | `{ permissionId: number, blockHeader: ... }` |

## Returns[​](#returns "Direct link to Returns")

Unsigned transaction object.

## Example[​](#example "Direct link to Example")

```
await tronWeb.transactionBuilder.unfreezeBalance("BANDWIDTH", "41BF97A54F4B829C4E9253B26024B1829E1A3B1120", "41BF97A54F4B829C4E9253B26024B1829E1A3B1120");  
{  
  visible: false,  
  txID: '2ba070338263eecbec034aac62a0a9b906a033ac34eb3e183cc7ccc2c4d1fb20',  
  raw_data: {  
    contract: [ [Object] ],  
    ref_block_bytes: 'afa9',  
    ref_block_hash: 'd25a977d06b9fb63',  
    expiration: 1581312834000,  
    timestamp: 1581312774685  
  },  
  raw_data_hex: '0a02afa92208d25a977d06b9fb6340d0f3dbec822e5a53080c124f0a34747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e556e667265657a6542616c616e6365436f6e747261637412170a1541bf97a54f4b829c4e9253b26024b1829e1a3b1120709da4d8ec822e'  
}
```