

* CookBook
Version: 6.3.0

On this page

# CookBook

The TronWeb Cookbook is a collection of practical, example‑driven guides and code snippets that show how to use TronWeb. With it, you can quickly:

* Find a working snippet for a task you’re trying to implement.
* Copy, adapt, and run code immediately.
* Learn best practices.

## For developing and testing[​](#for-developing-and-testing "Direct link to For developing and testing")

1. Choose an http api network from [here](https://developers.tron.network/docs/networks). For example, if you want to use Nile Testnet, you can use `https://api.nileex.io`. But you can also use a local network, see [here](/docu/docs/Build local node).
2. Connect to the network you chose.
3. Write your code. You may need to use TRX in your code. For testnet, go to faucet respectively to get the TRX for testing. For local network, you can use `tre_setAccountBalance` to activate the account and get TRX.
4. Live code editor:

Using Nile Testnet.

> Show Code Editor

Using local network, this code might not work in browser because local network uses http protocol while the site is hosted on https.

> Show Code Editor

## Contracts manipulation[​](#contracts-manipulation "Direct link to Contracts manipulation")

Supposing you have the below contract and you want to deploy it and trigger it, you can do like follow.

```
pragma solidity ^0.4.18;  
contract funcABIV2 {  
    uint256 public check;  
  
    constructor(uint256 _check) public {  
        check = _check;  
    }  
  
    function setCheck(uint256 _check) public {  
        check = _check;  
    }  
}
```

You can get its abi and bytecode by compiling it using [TronIDE](https://www.tronide.io/).

Deploy the contract and trigger it:

> Show Code Editor

## Build/sign/broadcast transactions[​](#buildsignbroadcast-transactions "Direct link to Build/sign/broadcast transactions")

TronWeb has supported 36 transaction types. You can go [here](/docu/docs/API List/transactionBuilder/) to see all transaction types. Here we use `sendTrx` transaction as an example to see how to build/sign/broadcast a transaction:

> Show Code Editor

## Events subscribing[​](#events-subscribing "Direct link to Events subscribing")

You may need to subscribe events to get the real-time status of a transaction. Here is an example to do it:

> Show Code Editor