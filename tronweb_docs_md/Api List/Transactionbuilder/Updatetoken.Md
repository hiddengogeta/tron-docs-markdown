

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* updateToken
Version: 6.3.0

On this page

# updateToken [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L1694)

Create an unsigned transaction that update TRC10 token information.

## Usage[​](#usage "Direct link to Usage")

```
const options = {  
  description: "justfortest", // The description of token, optional  
  url: "www.my-token.com", // The token's website url, default String  
  freeBandwidth: 1000000, // Each token holder's free bandwidth, optional  
  freeBandwidthLimit: 100, // The total free bandwidth of the token, optional  
  permissionId: 2 // Optional, for multi-signature use  
}  
const transaction = await tronWeb.transactionBuilder.updateToken(options, issuerAddress);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| options | Options for updating token information. | `UpdateTokenOptions` |
| issuerAddress | Address of the token issuer,format:hexstring or base58 | String |

```
interface UpdateTokenOptions {  
    /**  
     * The description of token.  
     * Optional.  
     */  
    description?: string;  
    /**  
     * The token's website url.  
     */  
    url: string;  
    /**  
     * Each token holder's free bandwidth.  
     * Optional.  
     */  
    freeBandwidth?: number;  
    /**  
     * The total free bandwidth of the token.  
     * Optional. Default is 0.  
     */  
    freeBandwidthLimit?: number;  
    /**  
     * Permission id for multi-sign.  
     */  
    permissionId?: number;  
    blockHeader?: {  
      ref_block_bytes: string;  
      ref_block_hash: string;  
      expiration: number;  
      timestamp: number;  
    };  
}
```

## Returns[​](#returns "Direct link to Returns")

Unsigned transaction object.

## Example[​](#example "Direct link to Example")

```
const createasset = {  
  description: "justfortest",  
  url: "www.my-token.com",  
  freeBandwidth: 1000000,  
  freeBandwidthLimit: 100,  
  permissionId: 2  
}  
const transaction = await tronWeb.transactionBuilder.updateToken(createasset, "TTSFjEG3Lu9WkHdp4JrWYhbGP6K1REqnGQ");  
console.log(transaction);  
{  
  visible: false,  
  txID: '009e8b45c34fbccf86d3f8d1f5e52d694c40b14550289a49048e9ba64799520f',  
  raw_data: {  
    contract: [ [Object] ],  
    ref_block_bytes: '21ca',  
    ref_block_hash: '65b258d979c2d3f8',  
    expiration: 1581326298000,  
    timestamp: 1581326241240  
  },  
  raw_data_hex: '0a0221ca220865b258d979c2d3f84090d791f3822e5a72080f126c0a30747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5570646174654173736574436f6e747261637412380a1541bf97a54f4b829c4e9253b26024b1829e1a3b1120120b6a757374666f72746573741a0c7777772e636374762e636f6d20c0843d2864280170d89b8ef3822e'  
}
```