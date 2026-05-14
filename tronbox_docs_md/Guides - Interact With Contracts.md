

# Interact with contracts [​](#interact-with-contracts)

## Introduction [​](#introduction)

If you were writing raw requests to the TRON network yourself in order to interact with your contracts or conduct tests, you'd soon realize that writing these requests is clunky and cumbersome. As well, you might find that managing the state for each request you've made is *complicated*. Fortunately, TronBox takes care of this complexity for you to make interacting with your contracts a breeze.

## Read and write data [​](#read-and-write-data)

The TRON network distinguishes between writing data to the network and reading data from it, which plays a significant part in how you write your application. In general, writing data is called a **transaction** whereas reading data is called a **call**. Transactions and calls are treated very differently and have the following characteristics.

## Transaction [​](#transaction)

Transactions fundamentally change the state of the network. A transaction can be as simple as sending TRX to another account, or as complicated as executing a contract function or adding a new contract to the network. The defining characteristic of a transaction is that it writes (or changes) data. Transactions cost `Energy` and `Bandwidth` to run and take time to process. When you execute a contract's function via a transaction, you cannot receive that function's return value because the transaction isn't processed immediately. In general, functions meant to be executed via a transaction will not return a value, but a transaction id instead. So in summary, transactions:

* Cost `Energy` and `Bandwidth`, which can be obtained by freezing TRX
* Change the state of the network
* Aren't processed immediately (need to wait for confirmations by Super Representatives)
* Won't expose a return value (only a transaction id)

## Call [​](#call)

Calls, on the other hand, are very different. Calls can be used to execute code on the network, though no data will be permanently changed. Calls are free to run, and their defining characteristic is that they read data. When you execute a contract function via a call you will receive the return value immediately. In summary, calls:

* Are free (does not cost `Energy` or `Bandwidth`)
* Do not change the state of the network
* Are executed immediately
* Will expose a return value

Choosing between a `transaction` and a `call` is as simple as deciding whether you want to read data or write it.

## Introducing abstractions [​](#introducing-abstractions)

Contract abstractions are the bread and butter of interacting with TRON contracts from JavaScript. In short, contract abstractions are wrapper code that makes interaction with your contracts easy, in a way that lets you forget about the many engines and gears executing under the hood. TronBox uses its own contract abstraction via the tronbox-contract module, which is described below.

In order to appreciate the usefulness of a contract abstraction, however, we first need a contract to talk about. We'll use the `MetaCoin` contract available to you through TronBox Boxes via `tronbox unbox metacoin`.

Solidity

solidity

```
pragma solidity ^0.5.4;

import "./ConvertLib.sol";

// This is just a simple example of a coin-like contract.
// It is not standards compatible and cannot be expected to talk to other
// coin/token contracts.

contract MetaCoin {
  mapping(address => uint) balances;

  event Transfer(address _from, address _to, uint256 _value);

  address owner;

  constructor(uint initialBalance) public {
    owner = msg.sender;
    balances[msg.sender] = initialBalance;
  }

  function sendCoin(address receiver, uint amount) public returns (bool sufficient) {
    if (balances[msg.sender] < amount) return false;
    balances[msg.sender] -= amount;
    balances[receiver] += amount;
    emit Transfer(msg.sender, receiver, amount);
    return true;
  }

  function getConvertedBalance(address addr) public view returns (uint){
    return ConvertLib.convert(getBalance(addr), 2);
  }

  function getBalance(address addr) public view returns (uint) {
    return balances[addr];
  }

  function getOwner() public view returns (address) {
    return owner;
  }
}
```

This contract has three methods aside from the constructor (`sendCoin`, `getBalanceInEth`, and `getBalance`). All three methods can be executed as either a `transaction` or a `call`.

First execute the deployment:

Terminal

shell

```
tronbox migrate
```

After the deployment is successful, let's look at the JavaScript object called MetaCoin provided for us by TronBox, as made available in the TronBox console:

Terminal

shell

```
tronbox(development)> MetaCoin.deployed().then(instance => console.log(instance));

// outputs:
// ...
// - address: { get: [Function: get], set: [Function: set] }
// - getOwner: <ref *1> [Function: f] { call: [Circular *1] },
// - sendCoin: <ref *2> [Function: f] { call: [Circular *2] },
// - getConvertedBalance: <ref *3> [Function: f] { call: [Circular *3] },
// - getBalance: <ref *4> [Function: f] { call: [Circular *4] },
// ...
```

Note that the abstraction contains the exact same functions that exist within our contract. It also contains an address that points to the deployed version of the MetaCoin contract.

## Execute contract functions [​](#execute-contract-functions)

With the abstraction, you can easily execute contract functions on the TRON network.

### Make a transaction [​](#make-a-transaction)

There are three functions on the MetaCoin contract that we can execute. If you analyze each of them, you'll see that `sendCoin` is the only function that aims to make changes to the network. The goal of `sendCoin` is to "send" some Meta coins from one account to another, and these changes should persist.

When calling `sendCoin`, we'll execute it as a `transaction`. In the following example, we'll send 10 Meta coins from one account to another in a way that is making a `transaction`:

Terminal

shell

```
tronbox(development)> MetaCoin.deployed().then(res => res.sendCoin(tronWeb._accounts[1], 500, { from: tronWeb._accounts[0] }));

// outputs:
// 'dc445da425b1e9f00c8bc36241486644c71319a3445e62d98e6a68598c5a7488'
```

A few things are interesting about the above code:

* We called the abstraction's `sendCoin` function directly. This will result in a `transaction` by default (i.e, writing data) instead of `call`.
* We passed an object as the third parameter to `sendCoin`. Note that the `sendCoin` function in our Solidity contract doesn't have a third parameter. What you see above is a special object that can always be passed as the last parameter to a function that lets you edit specific details about the transaction. Here, we set the `from` address ensuring this transaction came from `accounts[0]`. The transaction params that you can set:
  + `from`: from refers to the sending party of the transaction.
  + `callValue`: callValue refers to the value of TRX sent to the contract address when deploying a contract. Default value is `0`.
  + `tokenId`: tokenId refers to the ID of the TRC10 token sent to a contract address for contract deployment. Default value is `0`.
  + `tokenValue`: tokenValue refers to the amount of the TRC10 token sent to a contract address for contract deployment. Default value is `0`.
  + `feeLimit`: feeLimit refers to the upper limit of the Energy cost for deploying or calling a smart contract. Default value is `1000000000` (1,000 TRX).

### Make a call [​](#make-a-call)

Continuing with MetaCoin, notice the `getBalance` function is a great candidate for reading data from the network. It doesn't need to make any changes, as it just returns the MetaCoin balance of the address passed to it. Let's give it a shot:

Terminal

shell

```
tronbox(development)> MetaCoin.deployed().then(res => res.getBalance(tronWeb._accounts[0]));

// outputs:
// 9500n
```

### Process transaction results [​](#process-transaction-results)

When you make a `transaction`, you're given a `result` object that gives you a wealth of information about the `transaction`.

Specifically, you get the following via the transaction id:

Terminal

shell

```
tronbox(development)> tronWeb.trx.getTransactionInfo('dc445da425b1e9f00c8bc36241486644c71319a3445e62d98e6a68598c5a7488');

// outputs:
// {
//   id: 'dc445da425b1e9f00c8bc36241486644c71319a3445e62d98e6a68598c5a7488',
//   fee: 2755760,
//   blockNumber: 176,
//   blockTimeStamp: 1744630854000,
//   contractResult: [
//     '0000000000000000000000000000000000000000000000000000000000000001'
//   ],
//   contract_address: '411990a6d220f598da4e969dfee8622da86a1c4876',
//   receipt: {
//     energy_fee: 2752300,
//     energy_usage_total: 27523,
//     net_fee: 3460,
//     result: 'SUCCESS'
//   },
//   log: [
//     {
//       address: '1990a6d220f598da4e969dfee8622da86a1c4876',
//       topics: [
//         'ddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
//       ],
//       data: '000000000000000000000000c32e5231366762b190a46e98b9f775e432812ead000000000000000000000000cdb6f650ae118778af202d4c28b001b406ca91f100000000000000000000000000000000000000000000000000000000000001f4'
//     }
//   ]
// }
```

### Catch events [​](#catch-events)

Your contracts can fire events that you can catch to gain more insight into what your contracts are doing. Below, we will illustrate the structure of events by retrieving a TransactionInfo using `tronWeb.trx.getTransactionInfo`.

The event is triggered by the `sendCoin` function, which emits the `Transfer(address,address,uint256)` event.

Terminal

shell

```
tronbox(development)> tronWeb.trx.getTransactionInfo('dc445da425b1e9f00c8bc36241486644c71319a3445e62d98e6a68598c5a7488').then(res => console.log(res.log))

// outputs:
// [
//   {
//     address: '1990a6d220f598da4e969dfee8622da86a1c4876',
//     topics: [
//       'ddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
//     ],
//     data: '000000000000000000000000c32e5231366762b190a46e98b9f775e432812ead000000000000000000000000cdb6f650ae118778af202d4c28b001b406ca91f100000000000000000000000000000000000000000000000000000000000001f4'
//   }
// ]
```

### Add a new contract to the network [​](#add-a-new-contract-to-the-network)

We can deploy our own version to the network using the `.new()` function:

Terminal

shell

```
tronbox(development)> MetaCoin.new(50).then(res => console.log(res.address))

// outputs:
// 418912f128b414779e0a21251883b026671706ea6d
```

### Use a contract at a specific address [​](#use-a-contract-at-a-specific-address)

If you already have an address for a contract, you can create a new abstraction to represent the contract at that address.

Terminal

shell

```
tronbox(development)> MetaCoin.at('418912f128b414779e0a21251883b026671706ea6d')

// outputs:
// ...
// - address: { get: [Function: get], set: [Function: set] }
// - getOwner: <ref *1> [Function: f] { call: [Circular *1] },
// - sendCoin: <ref *2> [Function: f] { call: [Circular *2] },
// - getConvertedBalance: <ref *3> [Function: f] { call: [Circular *3] },
// - getBalance: <ref *4> [Function: f] { call: [Circular *4] },
// ...
```