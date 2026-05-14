

* [API List](/docu/docs/API List/)
* protobuf and transaction
* deserializeTransaction()
Version: 6.3.0

On this page

# deserializeTransaction() [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/utils/deserializeTx.ts#L626)

Deserialize a transaction, convert raw data hex into an object.

## Usage[​](#usage "Direct link to Usage")

```
utils.deserializeTx.deserializeTransaction(type, rawDataHex)
```

## Parameters[​](#parameters "Direct link to Parameters")

| Argument | Description | Type |
| --- | --- | --- |
| type | The transaction type. | string |
| type | The raw data hex of a transaction. | string |

**Note**:

1. In TronWeb v6.0.2, we used to deserialize a triggerSmartContract type transaction by `DTriggerSmartContract`. But we give a unified API to deserialize transactions with any type in this version. And `DTriggerSmartContract` no longer exists.
2. In TronWeb v6.1.0, we refactored the related code into a new file. As a result, the utils module has been updated to `deserializeTx`. And `DeserializeTransaction` has been renamed to `deserializeTransaction`, with the initial "D" now lowercase.

## Supported type[​](#supported-type "Direct link to Supported type")

* TriggerSmartContract
* FreezeBalanceV2Contract
* UnfreezeBalanceV2Contract
* CancelAllUnfreezeV2Contract
* DelegateResourceContract
* UnDelegateResourceContract
* WithdrawExpireUnfreezeContract
* TransferContract
* WithdrawBalanceContract
* WitnessCreateContract
* TransferAssetContract
* ParticipateAssetIssueContract
* AssetIssueContract
* UpdateAssetContract

## Return[​](#return "Direct link to Return")

Object - An object with the transaction data.

## Example[​](#example "Direct link to Example")

```
import { TronWeb, utils } from 'tronweb';  
  
const tronWeb = new TronWeb({  
    fullHost: 'https://api.nileex.io',  
    privateKey: 'your private key',  
});  
const contractAddress = 'TXYZopYRdj2D9XRtbG411XZZ3kM5VkAeBf'; // nile usdt address  
const account = await tronWeb.createAccount();  
const account2 = await tronWeb.createAccount();  
const tx = (await tronWeb.transactionBuilder.triggerSmartContract(  
    contractAddress,  
    'transfer(address,uint256)',  
    {  
        txLocal: true,  
        tokenId: '1000008',  
        tokenValue: 100,  
        feeLimit: 100 * (10 ** 6),  
    },  
    [  
        { type: "address", value: account2.address.base58 },  
        { type: "uint256", value: 100000000 }  
    ],  
    account.address.base58,  
)).transaction;  
const dResult = utils.deserializeTx.deserializeTransaction('TriggerSmartContract', tx.raw_data_hex);
```