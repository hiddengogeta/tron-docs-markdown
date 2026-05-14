

# Test contracts [​](#test-contracts)

## Framework [​](#framework)

TronBox comes standard with an automated testing framework to make testing your contracts a breeze. This framework lets you write simple and manageable tests in [JavaScript](/docs/guides/write-javascript-tests), for exercising your contracts from the outside world, just like your application.

## Location [​](#location)

All test files should be located in the `./test` directory. TronBox will only run test files with the `.js` file extensions. All other files are ignored.

## Command [​](#command)

To run all tests, simply run:

Terminal

shell

```
tronbox test
```

Alternatively, you can specify a path to a specific file you want to run, e.g.,

Terminal

shell

```
tronbox test ./path/to/test/file.js
```

## Using TRE [​](#using-tre)

To test our contracts more easily, we need to connect to a blockchain network. After v3.0.0 came out, TronBox provides a TronBox Runtime Environment (TRE) private chain that can be used for testing. Please note that this blockchain is in our local system and does not connect to the TRON main network.

You can start and interact with the blockchain by using the TronBox Runtime Environment (TRE), which is designed to build a complete private chain for development on TRON.

Steps are as follows:

1. Pull images from the Docker:

Terminal

shell

```
docker pull tronbox/tre
```

2. Start the TronBox Runtime Environment (TRE) and run the following commands:

Terminal

shell

```
docker run -it -p 9090:9090 --rm --name tron tronbox/tre
```

We will see the following information:

Terminal

shell

```
----------------------------------

TronBox Runtime Environment v1.0.5

----------------------------------

Start the http proxy for dApps...
[HPM] Proxy created: /  ->  http://127.0.0.1:18190
[HPM] Proxy created: /  ->  http://127.0.0.1:18191
[HPM] Proxy created: /  ->  http://127.0.0.1:8545
[HPM] Proxy created: /  ->  http://127.0.0.1:8545
[HPM] Proxy created: /  ->  http://127.0.0.1:8060

 TRE now listening on http://127.0.0.1:9090


ADMIN /admin/accounts-generation
(1) FullNode is not already.
Sleeping for 3 seconds... Slept.
(2) FullNode is not already.
Sleeping for 3 seconds... Slept.

FullNode is already.

...
Loading the accounts and waiting for the node to mine the transactions...
(1) Waiting for receipts...
Sending 10000 TRX to TEXqRygDHvE7Xe5XcnBpJeJsRCu2pB3e4U
Sending 10000 TRX to TBXGwsmz7n6QemBABmooTBvWgn86H8n7QT
Sending 10000 TRX to THaLQRHEfmYwRbVfHkL3VrpzJzUvgStJbX
Sending 10000 TRX to TTuWX3EiRSgSEX35z39dKnkGwux27E7tYe
Sending 10000 TRX to TKnbNtvgW2jnkXZApWNMGVunuirts4UaL8
Sending 10000 TRX to TSZ4ABf1nKTsTFqqBfcGDDkfcsGcdC7784
Sending 10000 TRX to TXHDhBZ9ZYHLbH1ZEKjXBmaR3eJfdgeTWE
Sending 10000 TRX to TJUiUEAbkQ7vfupB5GoJRVr6QwQBR97n45
Sending 10000 TRX to TCzMS8UDrWJ9Yf5Pk49Y7cD9C2i7Ui4Ve1
Sending 10000 TRX to TT31CTebLhcSynLxm5Ak7W9Pjnq4Mupdbb
Sleeping for 3 seconds... Slept.
(2) Waiting for receipts...
Sleeping for 3 seconds... Slept.
(3) Waiting for receipts...
Done.

Available Accounts
==================

(0) TEXqRygDHvE7Xe5XcnBpJeJsRCu2pB3e4U (10000 TRX)
(1) TBXGwsmz7n6QemBABmooTBvWgn86H8n7QT (10000 TRX)
(2) THaLQRHEfmYwRbVfHkL3VrpzJzUvgStJbX (10000 TRX)
(3) TTuWX3EiRSgSEX35z39dKnkGwux27E7tYe (10000 TRX)
(4) TKnbNtvgW2jnkXZApWNMGVunuirts4UaL8 (10000 TRX)
(5) TSZ4ABf1nKTsTFqqBfcGDDkfcsGcdC7784 (10000 TRX)
(6) TXHDhBZ9ZYHLbH1ZEKjXBmaR3eJfdgeTWE (10000 TRX)
(7) TJUiUEAbkQ7vfupB5GoJRVr6QwQBR97n45 (10000 TRX)
(8) TCzMS8UDrWJ9Yf5Pk49Y7cD9C2i7Ui4Ve1 (10000 TRX)
(9) TT31CTebLhcSynLxm5Ak7W9Pjnq4Mupdbb (10000 TRX)

Private Keys
==================

(0) ...PRIVATE_KEY_HERE...
(1) ...PRIVATE_KEY_HERE...
(2) ...PRIVATE_KEY_HERE...
(3) ...PRIVATE_KEY_HERE...
(4) ...PRIVATE_KEY_HERE...
(5) ...PRIVATE_KEY_HERE...
(6) ...PRIVATE_KEY_HERE...
(7) ...PRIVATE_KEY_HERE...
(8) ...PRIVATE_KEY_HERE...
(9) ...PRIVATE_KEY_HERE...

HD Wallet
==================
Mnemonic:      ... MNEMONIC_HERE ...
Base HD Path:  m/44'/195'/0'/0/{account_index}

GET 200  - 10752.337 ms
```

Here we see ten accounts (and their private keys) that can be used to interact with the blockchain.

TIP

*NOTE: This Docker image is not optimized for the Apple ARM chip (Apple silicon), so it may be unusable and the Docker needs to be restarted several times.*

3. Open the console and execute the deployment:

Terminal

shell

```
tronbox migrate
```

We will see the following output:

Terminal

shell

```
Using network 'development'.

Running migration: 1_initial_migration.js
  Deploying Migrations...
  Migrations:
    (base58) TVbadXqMTap8D2rNjyf353Rc2jD82kWKac
    (hex) 41d74b6b5c04a4a8ec9dd60127d354540d40270889
Saving successful migration to network...
Saving artifacts...
Running migration: 2_deploy_contracts.js
  Deploying ConvertLib...
  ConvertLib:
    (base58) TGcA7gVte4sw45FVXg7tkA7Y4MVYKWvgT5
    (hex) 4148cdbc805388241d397bc9e3da63cc1371e21b30
  Linking ConvertLib to MetaCoin
  Deploying MetaCoin...
  MetaCoin:
    (base58) TLQnf4xrHjn2t983AutNZKzJwisJEyM18k
    (hex) 417287c03e5db15b58b8d3c111302815b6d10c0235
Saving successful migration to network...
Saving artifacts...
```

Here shows the network, addresses of your deployed contracts, and transactions statuses.

After starting TronBox Runtime Environment (TRE), you can use the following advanced features in unit testing.

TIP

*NOTE: You can use tronWrap in unit testing.*

* `tre_setAccountBalance`: To set account balance.

JavaScript

javascript

```
const address = 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL';
const balance = '0x3e8';
const result = await tronWrap.send('tre_setAccountBalance', [address, balance]);
console.log(result);
```

* `tre_setAccountCode`: To set account code (It's recommended to set it as runtime bytecode, because setting it to the creation code of the contract will cause an exception in executing the contract).

JavaScript

javascript

```
const address = 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL';
const data = '0xbaddad42';
const result = await tronWrap.send('tre_setAccountCode', [address, data]);
console.log(result);
```

* `tre_setAccountStorageAt`: To set account storage.

JavaScript

javascript

```
const address = 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL';
const slot = '0x0000000000000000000000000000000000000000000000000000000000000005';
const data = '0xbaddad42';
const result = await tronWrap.send('tre_setAccountStorageAt', [address, slot, data]);
console.log(result);
```

* `tre_mine`: Immediately mine the specified number of blocks, and the blocks parameter specifies the additionally mined blocks. The parameter range is (0, 100] (if the parameter is not given, the default is 1).

JavaScript

javascript

```
const result = await tronWrap.send('tre_mine', [{ blocks: 5 }]);
console.log(result);
```

* `tre_unlockedAccounts`: Unlock accounts. Transactions sent from unlocked accounts do not require private key signatures.

JavaScript

javascript

```
const result = await tronWrap.send('tre_unlockedAccounts', [['TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL']]);
console.log(result);
```

* `tre_blockTime`: To set the auto-mining time. If the parameter is 0, auto-mining is stoped, and a block will mine after receiving a transaction.

JavaScript

javascript

```
const result = await tronWrap.send('tre_blockTime', [3]);
console.log(result);
```

* `debug_traceTransaction`: Returns all traces of a given transaction.

JavaScript

javascript

```
const txid = 'f6b72dda65682b858c1c1980710aad7955fbf6db91c66840da0f852fc3cc694b';
const result = await tronWrap.send('debug_traceTransaction', [txid]);
console.log(result);
```

* `debug_storageRangeAt`: Returns the contract storage for the specified range.

JavaScript

javascript

```
const result = await tronWrap.send('debug_storageRangeAt', [0, 0, contractAddress, '0x01', 1]);
console.log(result);
```