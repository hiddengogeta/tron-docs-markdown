

* Quickstart
Version: 6.3.0

On this page

# Quickstart

## Getting Started[​](#getting-started "Direct link to Getting Started")

The TronWeb is a JavaScript library for building Web3 projects on TRON. It consists of 4 main parts:

1. TransactionBuilder for building transactions with client-side integrity check.
2. Trx for requesting data from nodes or sign transactions etc.
3. Contract for interacting with contracts.
4. Other useful Utils like web3.js or ethers.js.

### Installation[​](#installation "Direct link to Installation")

#### Node.js[​](#nodejs "Direct link to Node.js")

```
npm install tronweb
```

or

```
yarn add tronweb
```

#### Browser[​](#browser "Direct link to Browser")

The easiest way to use TronWeb in a browser is to install it as above and copy the dist file to your working folder. For example:

```
cp node_modules/tronweb/dist/TronWeb.js ./js/tronweb.js
```

so that you can call it in your HTML page as

```
<script src="./js/tronweb.js"></script>
```

### Instantiation[​](#instantiation "Direct link to Instantiation")

Then, in your JavaScript file, define TronWeb:

```
const { TronWeb } = require('tronweb');
```

or use esm-style import:

```
import { TronWeb } from 'tronweb';
```

When you instantiate TronWeb you can set

* fullHost

Supposing you are using a server that provides everything, like TronGrid, you can instantiate TronWeb as:

```
const tronWeb = new TronWeb({  
  fullHost: 'https://api.trongrid.io',  
  headers: { 'TRON-PRO-API-KEY': 'your api key' },  
  privateKey: 'your private key'  
});
```

Like infura API Key, you can sign up for [TronGrid](https://www.trongrid.io/) and create your API key on the dashboard to access TRON Network data.

Note

* **Do not expose your private key** in any web browser environment.
* You can instantiate TronWeb **without privateKey**, if you only need to use some `utils` functions such as `TronWeb.utils`
* If you only want to **query information** from the TRON Network blockchain **without signing a transaction**, you have two options:
  + Pass a **placeholder private key** (e.g. `01`) when instantiating TronWeb. This is a convenient way to avoid passing an address manually in each API call.
  + Instantiate TronWeb **without any private key**. In this case, you need to pass the required address explicitly in the corresponding method parameters when calling on-chain APIs such as `triggerConstantContract`, `getTransactionInfo`.

> *TronWeb constructor parameters*
>
> For backward compatibility, TronWeb keeps multi-type constructor parameters. But it is recommended that you use options format which supports below properties:
>
> * fullNode: where TronWeb send full node requests to. It can be a url string or an `HttpProvider` instance.
> * solidityNode: where TronWeb send solidity node requests to. It can be a url string or an `HttpProvider` instance.
> * eventServer: where TronWeb send event requests to. It can be a url string or an `HttpProvider` instance.
> * fullHost: set `fullNode`/`solidityNode`/`eventServer` to the same server.
> * headers: set http headers of axios for full node **and** solidity node.
> * eventHeaders: set http headers of axios for event server.
> * privateKey: set the private key for TronWeb to use. Once set, default address of TronWeb instance will be set to the address of the private key.
> * disablePlugins: whether to disable plugins. Default is false.

> *Note*:
> In instances where both `fullHost` and individual endpoints (`fullNode`, `solidityNode`, `eventServer`) are provided, the individual endpoint settings will take precedence.
> Additionally, `TronWeb.providers.HttpProvider` can be employed for the manual construction of customized providers, allowing for features such as retry logic or custom headers.

### Querying the TRON network[​](#querying-the-tron-network "Direct link to Querying the TRON network")

You can query data of the TRON network with `tronweb.trx` easy as follows:

```
await tronWeb.trx.getBlockByNumber(12345);  
{  
  blockID: '000000000000303987c7c8ab3f5967c107a619fa47819940597e9938811a1764',  
  block_header: {  
    raw_data: {  
      number: 12345,  
      txTrieRoot: '0000000000000000000000000000000000000000000000000000000000000000',  
      witness_address: '414b4778beebb48abe0bc1df42e92e0fe64d0c8685',  
      parentHash: '0000000000003038c0a3aa1806236bc5b281633728b5fe8a14a51062522e651d',  
      timestamp: 1529928585000  
    },  
    witness_signature: 'cb889103aa9ce691d39df8030b54b50b12b77984684281f3490e0b802cbc364c13af773ede8d9314add0fa4d247165be82fa28721f17493c88761b7039ba1c1100'  
  }  
}
```

### Creating a transaction[​](#creating-a-transaction "Direct link to Creating a transaction")

Tronweb provides well-rounded APIs to satisfy your transaction building demands. No worry about the transaction would have tampered with because client-side integrity checking is done behind. See the example:

```
const transaction = await tronWeb.transactionBuilder.sendTrx("TVDGpn4hCSzJ5nkHPLetk8KQBtwaTppnkr", 100, "TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL");  
{  
    "visible": false,  
    "txID": "9f62a65d0616c749643c4e2620b7877efd0f04dd5b2b4cd14004570d39858d7e",  
    "raw_data": {  
        "contract": [  
            {  
                "parameter": {  
                    "value": {  
                        "amount": 100,  
                        "owner_address": "418840e6c55b9ada326d211d818c34a994aeced808",  
                        "to_address": "41d3136787e667d1e055d2cd5db4b5f6c880563049"  
                    },  
                    "type_url": "type.googleapis.com/protocol.TransferContract"  
                },  
                "type": "TransferContract"  
            }  
        ],  
        "ref_block_bytes": "0add",  
        "ref_block_hash": "6c2763abadf9ed29",  
        "expiration": 1581308685000,  
        "timestamp": 1581308626092  
    },  
    "raw_data_hex": "0a020add22086c2763abadf9ed2940c8d5deea822e5a65080112610a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412300a15418840e6c55b9ada326d211d818c34a994aeced808121541d3136787e667d1e055d2cd5db4b5f6c880563049186470ac89dbea822e"  
}
```

### Signing a transaction[​](#signing-a-transaction "Direct link to Signing a transaction")

Tronweb will automatically use the privateKey you provided when you initialize tronweb. Or you can provide an optional privateKey as a second argument.

```
const signedTransaction = await tronWeb.trx.sign(transaction, privateKey);
```

### Broadcasting[​](#broadcasting "Direct link to Broadcasting")

Broadcasting is as easy as follows:

```
tronWeb.trx.sendRawTransaction(signedTransaction);
```

### Contracts[​](#contracts "Direct link to Contracts")

First, load a contract:

```
const abi = [...];         
const instance = await tronWeb.contract(abi,'contractAddress');
```

Call read-only methods:

```
const result = await contract.function_name(param1,param2,...).call();
```

Call state changing methods:

```
const result = await contract.function_name(param1,param2,...).send({  
  feeLimit:100_000_000,  
  callValue:0,  
  tokenId:1000036,  
  tokenValue:100,  
  shouldPollResponse:true  
});
```