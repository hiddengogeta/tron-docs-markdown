

# Deploy contracts [​](#deploy-contracts)

## Run Migrations [​](#run-migrations)

Migrations are JavaScript files that help you deploy contracts to the TRON network. These files are responsible for staging your deployment tasks, and they are written under the assumption that your deployment needs will change over time. As your project evolves, you will create new migration scripts to further this evolution on the blockchain. A history of previously run migrations is recorded on-chain through a special `Migrations` contract. The details are as follows.

## Command [​](#command)

To run your migrations, run the following:

Terminal

shell

```
tronbox migrate
```

This will run all migrations located in the `migrations` directory of your project. At their simplest, migrations are a set of managed deployment scripts. If your migrations were previously run successfully, `tronbox migrate` will start execution from the last migration that was run, running only newly created migrations. If no new migration exists, `tronbox migrate` will not perform any action at all. You can use the `--reset` option to run all your migrations from the beginning. For local testing, make sure to install Docker and have [TronBox Runtime Environment (TRE)](https://hub.docker.com/r/tronbox/tre) running before executing migrate.

## Migration file [​](#migration-file)

A simple migration file looks like this:

Filename: `./migrations/4_example_migration.js`

JavaScript

javascript

```
const MyContract = artifacts.require('MyContract');

module.exports = function (deployer) {
  deployer.deploy(MyContract);
};
```

Note that the filename is prefixed with a number and is suffixed by a description. The numbered prefix is required in order to record whether the migration ran successfully. The suffix is purely for readability and comprehension. **The numbered prefix also serves the purpose of running the migration files in order.**

### artifacts.require() [​](#artifacts-require)

Before the migration, we tell TronBox which contracts we would like to interact with via the `artifacts.require()` method. This method is similar to Node's `require`, but in our case, it specifically returns a contract abstraction that we can use within the rest of our deployment script. The name specified should match **the name of the contract definition** within that source file. Do not pass the name of the source file, as files can contain more than one contract.

Consider this example where two contracts are specified within the same source file:

Filename: `./contracts/Contracts.sol`

Solidity

solidity

```
contract ContractOne {
  // ...
}

contract ContractTwo {
  // ...
}
```

To use only ContractTwo, your artifacts.require() statement would look like this:

JavaScript

javascript

```
const ContractTwo = artifacts.require('ContractTwo');
```

To use both contracts, you will need two `artifacts.require()` statements:

JavaScript

javascript

```
const ContractOne = artifacts.require('ContractOne');
const ContractTwo = artifacts.require('ContractTwo');
```

### module.exports [​](#module-exports)

All migrations must export a function via the `module.exports` syntax. The function exported by each migration should accept a `deployer` object as its first parameter. This object aids in deployment by providing a clear syntax for deploying smart contracts and performing some of the deployment's more mundane duties, such as saving deployed artifacts for later use. The `deployer` object is your main interface for staging deployment tasks, and its API is described at the bottom of this page.

Your migration function can accept other parameters as well. See the examples below.

### Initialize migration function [​](#initialize-migration-function)

TronBox requires that you have a Migration contract to use the migration function. This contract must contain specific interfaces, but you may edit this contract at will. For most projects, this contract will initially be deployed as the first migration file and will not be updated again. We will also receive this contract by default when creating a new project using `tronbox init`.

Filename: `./contracts/Migrations.sol`

Solidity

solidity

```
// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract Migrations {
  address public owner = msg.sender;
  uint public last_completed_migration;

  modifier restricted() {
    require(msg.sender == owner, "This function is restricted to the contract's owner");
    _;
  }

  function setCompleted(uint completed) public restricted {
    last_completed_migration = completed;
  }
}
```

You have to deploy this contract in the first migration to use the migration function. To do this, the following migration file needs to be created:

Filename: `./migrations/1_initial_migration.js`

JavaScript

javascript

```
const Migrations = artifacts.require('Migrations');

module.exports = function (deployer) {
  deployer.deploy(Migrations);
};
```

From here, you can create new migrations with increasing numbered prefixes to deploy other contracts and perform further deployment steps.

## Deployer [​](#deployer)

Your migration files will use the deployer to stage deployment tasks. As such, you can write deployment tasks synchronously and they will be executed in the correct order:

JavaScript

javascript

```
// Stage deploying A before B
deployer.deploy(A);
deployer.deploy(B);
```

Alternatively, each function on the deployer can be used as a Promise to queue up deployment tasks that depend on the execution of the previous task:

JavaScript

javascript

```
// Deploy A, then deploy B, passing in A's newly deployed address
deployer.deploy(A).then(function () {
  return deployer.deploy(B, A.address);
});
```

It is possible to write your deployment as a single promise chain if you find that syntax to be more clear. The deployer API is discussed at the bottom of this page.

## Network considerations [​](#network-considerations)

It is possible to run deployment steps conditionally based on the network being deployed to.

To conditionally stage deployment steps, write your migrations so that they accept a second parameter, called `network`. Example:

JavaScript

javascript

```
module.exports = function (deployer, network) {
  if (network == 'nile') {
    // Do something specific to the network named "nile".
  } else {
    // Perform a different step otherwise.
  }
};
```

## From address [​](#from-address)

Migrations are also passed the deployer account address (from) for the network you're deploying to, for you to use during your deployments.

JavaScript

javascript

```
module.exports = function (deployer, network, from) {
  // Use the from address within your migrations.
};
```

## Deployer API [​](#deployer-api)

The deployer contains many functions available to simplify your migrations.

### deployer.deploy(contract, ...args, options) [​](#deployer-deploy-contract-args-options)

You can deploy a specific contract specified by the `contract object` with `optional constructor arguments`. This is useful for singleton contracts, such that only one instance of this contract exists for your DApp. This will set the address of the contract after deployment (i.e., `Contract.address` will equal the newly deployed address), and it will override any previous address stored.

You may also pass an array of contracts, or an array of arrays, to speed up the deployment of multiple contracts. Additionally, the last argument is an optional object that can include the key named `overwrite` as well as other transaction parameters such as `feeLimit` and `from`. If `overwrite` is set to `false`, the deployer will not deploy this contract if it has already been deployed. This is useful for certain circumstances where a contract address is provided by an external dependency.

Note that you will need to deploy and link any libraries your contracts depend on first before calling `deploy`. See the `link` function below for more details.

Examples:

JavaScript

javascript

```
// Deploy a single contract without constructor arguments
deployer.deploy(A);

// Deploy a single contract with constructor arguments
deployer.deploy(A, arg1, arg2, ...);

// Don't deploy this contract if it has already been deployed
deployer.deploy(A, { overwrite: false });

// Set a maximum amount of fee_limit and `userFeePercentage`  for the deployment
deployer.deploy(A, { fee_limit: 1.1e8, userFeePercentage: 30 });

// Deploying multiple contracts as an array is now deprecated.
// This used to be quicker than writing three `deployer.deploy()` statements as the deployer
// can perform the deployment as a single batched request.
// deployer.deploy([
//   [A, arg1, arg2, ...],
//   B,
//   [C, arg1]
// ]);

// External dependency example:
//
// For this example, our dependency provides an address when we're deploying to the
// live network, but not for any other networks like testing and development.
// When we're deploying to the live network we want it to use that address, but in
// testing and development we need to deploy a version of our own. Instead of writing
// a bunch of conditionals, we can simply use the `overwrite` key.
deployer.deploy(SomeDependency, { overwrite: false });
```

### deployer.link(library, destinations) [​](#deployer-link-library-destinations)

Link an already-deployed library to a contract or multiple contracts. The `destinations` argument can be a single contract or an array of multiple contracts. If any contract within the destination doesn't rely on the library being linked, the contract will be ignored.

Example:

JavaScript

javascript

```
// Deploy library LibA, then link LibA to contract B, then deploy B.
deployer.deploy(LibA);
deployer.link(LibA, B);
deployer.deploy(B);

// Link LibA to many contracts
deployer.link(LibA, [B, C, D]);
```

### deployer.then(function() {}) [​](#deployer-then-function)

Just like a promise, run an arbitrary deployment step. Use this to call specific contract functions during your migration to add, edit, and reorganize contract data.

Example:

JavaScript

javascript

```
const A = artifacts.require('A');
const B = artifacts.require('B');

module.exports = async function (deployer) {
  let a, b;
  deployer
    .then(function () {
      // Create a new version of A
      return A.new();
    })
    .then(function (instance) {
      a = instance;
      // Get the deployed instance of B
      return B.deployed();
    })
    .then(function (instance) {
      b = instance;
      // Set the new instance of A's address on B via B's setA() function.
      return b.setA(a.address);
    });
};
```

### Migrations with async/await [​](#migrations-with-async-await)

You can also migrate your contracts using async/await:

Example:

JavaScript

javascript

```
const MyContract = artifacts.require('MyContract');

module.exports = async function (deployer) {
  // deploy a contract
  await deployer.deploy(MyContract);
  //access information about your deployed contract instance
  const instance = await MyContract.deployed();
};
```