

# Quickstart [​](#quickstart)

This doc will take you through the basics of creating a TronBox project and deploying a smart contract to a blockchain.

TIP

*NOTE: Before you begin, it is advised that you read the [TRON documentation](https://tronprotocol.github.io/documentation-en/getting_started/getting_started_with_javatron/).*

## Install TronBox [​](#install-tronbox)

Before using `TronBox`, please install it using `npm` command. You can install TronBox by referring to the [installation instructions](/docs/guides/installation).

## Create a project [​](#create-a-project)

Most of the TronBox commands are run under the directories of TronBox projects. So the first step is to create a TronBox project. You can create a bare project, but for those getting started, you can use TronBox Boxes, which offers example applications and project templates. We'll use the MetaCoin box, which creates a token that can be transferred between accounts.

1. Create a directory for MetaCoin:

Terminal

shell

```
mkdir MetaCoin
cd MetaCoin
```

2. Download ("unbox") the MetaCoin project:

Terminal

shell

```
tronbox unbox metacoin
```

> You can create a bare project without smart contracts using `tronbox init`.

Once this operation is completed, you will have a project structure with the following items:

* `contracts/`: Directory for [Solidity contracts](/docs/guides/interact-with-contracts)
* `migrations/`: Directory for [scriptable deployment files](/docs/guides/deploy-contracts)
* `test/`: Directory for [test contracts](/docs/guides/test-contracts)
* `tronbox.js`: TronBox [configuration file](/docs/reference/configuration)

## Explore the project [​](#explore-the-project)

TIP

*NOTE: This page is just a quickstart, and we're going to get into the details in the following sections.*

* `contracts/MetaCoin.sol`: This is a smart contract (written in Solidity) that creates a MetaCoin token. Note that this also references another Solidity file `contracts/ConvertLib.sol` in the same directory.
* `contracts/Migrations.sol`: This is a separate Solidity file used to manage and upgrade smart contracts. It is needed in every project and usually does not need to be edited.
* `migrations/1_initial_migration.js`: This is the script used to deploy the Migrations contract, and is stored within the Migrations.sol file.
* `migrations/2_deploy_contracts.js`: This is a deployment script that is used to deploy the MetaCoin contract. (Deployment scripts run in sequence. Scripts titled with 2 normally run after those titled 1.)
* `test/metacoin.js`: This is a [testing script written in JavaScript](/docs/guides/write-javascript-tests) that ensures your contract is working as expected.
* `tronbox.js`: This is the TronBox [configuration file](/docs/reference/configuration), for setting network information and other project-related settings. The file can be left blank because we can use a TronBox command that has some defaults built in.

## Compile contracts [​](#compile-contracts)

Execute the compilation:

Terminal

shell

```
tronbox compile
```

We will see the following output:

Terminal

shell

```
Compiling your contracts ...
============================
Compiling ./contracts/ConvertLib.sol...
Compiling ./contracts/MetaCoin.sol...
Compiling ./contracts/Migrations.sol...
Writing artifacts to ./build/contracts

> Compiled successfully using:
  - solc: 0.5.4
```

## Deploy to TRE [​](#deploy-to-tre)

To deploy our smart contracts, we're going to need to connect to a blockchain. TronBox provides a TronBox Runtime Environment (TRE) private chain that can be used for testing. Please note that this blockchain is local to your system and does not interact with the main TRON network. You can start this blockchain and interact with it using TRE. This step is to create a complete personal chain for development on TRON.

1. Pull images from the Docker:

Terminal

shell

```
docker pull tronbox/tre
```

> For how to install Docker, please refer to [Docker installation documentation](https://docs.docker.com/desktop/install/mac-install/)

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

This shows ten accounts (and their private keys) that can be used when interacting with the blockchain.

> This Docker image is not optimized for the Apple ARM chip (Apple silicon), so it may be unusable and the docker needs to be restarted several times.

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

This shows the network, addresses of your deployed contracts, and transaction statuses.

TIP

*NOTE: Your transaction hashes and contract addresses will be different from the above.*

## Test contracts [​](#test-contracts)

1. Open the console terminal and run the Solidity test instance

Terminal

shell

```
tronbox test ./test/metacoin.js
```

2. After hitting the return key, you will see the following output:

Terminal

shell

```
Using network 'development'.

Deploying contracts to development network...
Preparing Javascript tests (if any)...


  Contract: MetaCoin
    ✔ should verify that there are at least three available accounts
    ✔ should verify that the contract has been deployed by accounts[0]
    ✔ should put 10000 MetaCoin in the first account
Sleeping for 1 second... Slept.
    ✔ should call a function that depends on a linked library (1091ms)
Sleeping for 3 seconds... Slept.
    ✔ should send coins from account 0 to 1 (3208ms)


  5 passing (4s)
```

TIP

*NOTE: If you’re on Windows and encountering problems running this command, please see the documentation on [Solving naming conflicts on Windows](/docs/reference/configuration#resolve-naming-conflicts-on-windows).*

## Interact with the contract [​](#interact-with-the-contract)

To interact with the contract, you can use the `tronbox console`.

Terminal

shell

```
tronbox console
```

You will see the following prompt:

Terminal

shell

```
tronbox(development)>
```

TIP

*NOTE: The name in the parentheses of the prompt `tronbox(development)>` is the network that is currently connected to.*

For example:

* Check the account balance:

Terminal

shell

```
tronbox(development)> tronWeb.trx.getAccount();

// outputs:
// {
//   address: '41320c394dbec1d860fdde90d116d4be8313e4479e',
//   balance: 9890784090,
//   create_time: 1744265463000,
//   latest_opration_time: 1744266600000,
//   free_net_usage: 4746,
//   latest_consume_free_time: 1744266540000,
//   net_window_size: 28800000,
//   net_window_optimized: true,
//   account_resource: {
//     latest_consume_time_for_energy: 1744266600000,
//     energy_window_size: 28800000,
//     energy_window_optimized: true
//   },
//   owner_permission: { permission_name: 'owner', threshold: 1, keys: [ [Object] ] },
//   active_permission: [
//     {
//       type: 'Active',
//       id: 2,
//       permission_name: 'active',
//       threshold: 1,
//       operations: '7fff1fc0033ec30f000000000000000000000000000000000000000000000000',
//       keys: [Array]
//     }
//   ],
//   frozenV2: [ {}, { type: 'ENERGY' }, { type: 'TRON_POWER' } ],
//   asset_optimized: true
// }
```

* Obtain the list of accounts:

Terminal

shell

```
tronbox(development)> tronWeb._accounts;

// outputs:
// [
//   'TEXqRygDHvE7Xe5XcnBpJeJsRCu2pB3e4U',
//   'TBXGwsmz7n6QemBABmooTBvWgn86H8n7QT',
//   'THaLQRHEfmYwRbVfHkL3VrpzJzUvgStJbX',
//   'TTuWX3EiRSgSEX35z39dKnkGwux27E7tYe',
//   'TKnbNtvgW2jnkXZApWNMGVunuirts4UaL8',
//   'TSZ4ABf1nKTsTFqqBfcGDDkfcsGcdC7784',
//   'TXHDhBZ9ZYHLbH1ZEKjXBmaR3eJfdgeTWE',
//   'TJUiUEAbkQ7vfupB5GoJRVr6QwQBR97n45',
//   'TCzMS8UDrWJ9Yf5Pk49Y7cD9C2i7Ui4Ve1',
//   'TT31CTebLhcSynLxm5Ak7W9Pjnq4Mupdbb'
// ]
```

* Call the contract to check the account balance:

Terminal

shell

```
tronbox(development)> MetaCoin.deployed().then(res => res.getBalance(tronWeb._accounts[0]));

// outputs:
// 10000n
```

* Transfer some metacoin to other accounts:

Terminal

shell

```
tronbox(development)> MetaCoin.deployed().then(res => res.sendCoin(tronWeb._accounts[1], 500));

// outputs:
// 'ca1ab0f44ee878633f1e431d400a5aa60c9a38b110b6c997b4831769c8aae5ab'
```

* Check the balance of the account that received the metacoin:

Terminal

shell

```
tronbox(development)> MetaCoin.deployed().then(res => res.getBalance(tronWeb._accounts[1]));

// outputs:
// 500n
```

* Check the balance of the account that sent the metacoin:

Terminal

shell

```
tronbox(development)> MetaCoin.deployed().then(res => res.getBalance(tronWeb._accounts[0]));

// outputs:
// 9500n
```

## Continue learning [​](#continue-learning)

This quickstart showed you the basics of the TronBox project lifecycle, but there is much more to learn. Please continue with the rest of our documentation.