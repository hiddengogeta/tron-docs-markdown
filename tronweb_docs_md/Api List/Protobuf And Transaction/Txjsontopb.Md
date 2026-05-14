

* [API List](/docu/docs/API List/)
* protobuf and transaction
* txJsonToPb()
Version: 6.3.0

On this page

# txJsonToPb() [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/utils/transaction.ts#L898)

Serialize a transaction, convert transaction object in json format into protobuf structure

## Usage[​](#usage "Direct link to Usage")

```
utils.transaction.txJsonToPb(transaction)
```

## Parameters[​](#parameters "Direct link to Parameters")

transaction : Object - The transaction object in json format.

## Return[​](#return "Direct link to Return")

Object - A transaction object in protobuf format.

## Example[​](#example "Direct link to Example")

```
import { TronWeb, utils } from 'tronweb';  
  
const tronWeb = new TronWeb({  
    fullHost: 'https://api.nileex.io',  
    privateKey: 'your private key',  
});  
const txJson = await tronWeb.transactionBuilder.sendTrx("TVDGpn4hCSzJ5nkHPLetk8KQBtwaTppnkr", 100, "TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL");  
const txPb = utils.transaction.txJsonToPb(txJson);
```