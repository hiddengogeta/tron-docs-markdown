

* [API List](/docu/docs/API List/)
* [TransactionBuilder](/docu/docs/API List/transactionBuilder/)
* freezeBalance
Version: 6.3.0

On this page

# freezeBalance [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L248)

Creates a transaction that stakes TRX.

## Usage[​](#usage "Direct link to Usage")

```
const transaction = await tronWeb.transactionBuilder.freezeBalance(amount, duration, resource, ownerAddress, receiverAddress, options);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| amount | Amount of TRX (in SUN) to stake. | Integer |
| duration | Length in Days to stake TRX for. Minimum of 3 days. | Integer |
| resource | Resource that you're staking TRX in order to obtain. | `BANDWIDTH` or `ENERGY` |
| ownerAddress | Optional. Address of the owner of the TRX to be staked (defaults to caller's default address). | String |
| receiverAddress | Optional. Address of other user receiving the resource. | String |
| options | Optional. Permission id for multi-signature and block header for contract block header info. | `{ permissionId: number, blockHeader: ... }` |

## Returns[​](#returns "Direct link to Returns")

Unsigned transaction object.

## Example[​](#example "Direct link to Example")

```
//example 1  
await tronWeb.transactionBuilder.freezeBalance(tronWeb.toSun(100), 3, "ENERGY", "4115B95D2D2CBCE1B815BA4D2711A3BEA02CBB37F3", "4115B95D2D2CBCE1B815BA4D2711A3BEA02CBB37F3");  
{  
  visible: false,  
  txID: '98c21fe22afd4e0badb68f118b1598bbbdf7b7b66028146e48a351e87e3c606a',  
  raw_data: {  
    contract: [ [Object] ],  
    ref_block_bytes: 'cce3',  
    ref_block_hash: 'b356b0ba8cf551ad',  
    expiration: 1581261075000,  
    timestamp: 1581261017724  
  },  
  raw_data_hex: '0a02cce32208b356b0ba8cf551ad40b8e484d4822e5a5a080b12560a32747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e467265657a6542616c616e6365436f6e747261637412200a154115b95d2d2cbce1b815ba4d2711a3bea02cbb37f31080c2d72f1803500170fca481d4822e'  
}  
  
//example 2  
await tronWeb.transactionBuilder.freezeBalance(tronWeb.toSun(100), 3, "ENERGY", "TBx5FQGFeLUHPFMkn3BaFxxfVwLy7ffE5k", "TBx5FQGFeLUHPFMkn3BaFxxfVwLy7ffE5k");  
{  
  visible: false,  
  txID: 'acd5988278e27fd5e818eab0d197e8f622c8fd9428457ec7233837a5ba40aacf',  
  raw_data: {  
    contract: [ [Object] ],  
    ref_block_bytes: 'ccfc',  
    ref_block_hash: 'e7ce28d6d85e7e0c',  
    expiration: 1581261150000,  
    timestamp: 1581261090636  
  },  
  raw_data_hex: '0a02ccfc2208e7ce28d6d85e7e0c40b0ae89d4822e5a5a080b12560a32747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e467265657a6542616c616e6365436f6e747261637412200a154115b95d2d2cbce1b815ba4d2711a3bea02cbb37f31080c2d72f1803500170ccde85d4822e'  
}
```