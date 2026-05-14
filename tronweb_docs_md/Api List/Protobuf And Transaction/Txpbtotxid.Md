

* [API List](/docu/docs/API List/)
* protobuf and transaction
* txPbToTxID()
Version: 6.3.0

On this page

# txPbToTxID() [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/utils/transaction.ts#L986)

Calculate the transaction ID from the transaction protobuf format

## Usage[​](#usage "Direct link to Usage")

```
utils.transaction.txPbToTxID(transaction)
```

## Parameters[​](#parameters "Direct link to Parameters")

transaction : Object - The transaction object in protobuf format.

## Return[​](#return "Direct link to Return")

String - Transaction ID

## Example[​](#example "Direct link to Example")

```
import { TronWeb, utils } from 'tronweb';  
  
const tronWeb = new TronWeb({  
    fullHost: 'https://api.nileex.io',  
    privateKey: 'your private key',  
});  
const txJson = await tronWeb.transactionBuilder.sendTrx("TVDGpn4hCSzJ5nkHPLetk8KQBtwaTppnkr", 100, "TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL");  
// Convert the transaction object in json format to protobuf format  
const txPb = utils.transaction.txJsonToPb(txJson);  
// Calculate the transaction ID from the transaction protobuf format  
const txID = utils.transaction.txPbToTxID(txPb);
```