

# Migrating from Hardhat to TronBox [​](#migrating-from-hardhat-to-tronbox)

This guide walks you through the process of migrating an existing Hardhat project to TronBox.

## Migration Workflow [​](#migration-workflow)

**Step 1: Initialize TronBox project**

Start by creating a fresh TronBox workspace. This scaffolds the standard folders (`contracts`, `migrations`, `test`) and a baseline project structure.

Terminal

shell

```
mkdir my-tron-project
cd my-tron-project
tronbox init
```

**Step 2: Copy your contract files**

You can reuse your Solidity contracts from your Hardhat project. Most contracts can be migrated without changes.

Terminal

shell

```
# Copy contracts (no changes needed for most Solidity code)
cp -r ../my-hardhat-project/contracts/* ./contracts/
```

**Step 3: Configure TronBox**

Create `tronbox-config.js` based on your `hardhat.config.js`, then set networks and compiler as follows:

JavaScript

javascript

```
// tronbox-config.js
module.exports = {
  networks: {
    // Local development (TronBox TRE / local node)
    development: {
      privateKey: 'your-dev-private-key',
      feeLimit: 1e8,
      fullHost: 'http://127.0.0.1:9090',
      network_id: '9'
    },

    // Nile Testnet (recommended for testing)
    nile: {
      privateKey: process.env.PRIVATE_KEY,
      feeLimit: 1e8,
      fullHost: 'https://nile.trongrid.io',
      network_id: '3'
    },

    // Mainnet (production)
    mainnet: {
      privateKey: process.env.PRIVATE_KEY,
      feeLimit: 1e8,
      fullHost: 'https://api.trongrid.io',
      network_id: '1'
    }
  },
  compilers: {
    // TVM Solidity versions
    solc: {
      version: '0.8.6',
      settings: {
        optimizer: {
          enabled: true,
          runs: 200
        }
      }
    }
  }
};
```

Changes from Hardhat:

* Endpoint: use one `fullHost` URL (replaces `url` in Hardhat's network config).
* Accounts: set `privateKey` or `mnemonic` per network (replaces `accounts`).
* Fees: set the `feeLimit` as the resource upper limit for a transaction.
* Compiler: pick a TVM Solidity version.

**Step 4: Convert deployment scripts to migrations**

Hardhat uses custom scripts in a `scripts` folder, while TronBox uses numbered migration files in a `migrations` folder.

JavaScript

javascript

```
// scripts/deploy.js (Hardhat)
async function main() {
  const MyContract = await ethers.getContractFactory('MyContract');
  const contract = await MyContract.deploy(/* constructor arguments */);
  await contract.waitForDeployment();
  console.log('Contract deployed to:', await contract.getAddress());
}

main();
```

JavaScript

javascript

```
// migrations/2_deploy_contracts.js (TronBox)
const MyContract = artifacts.require('MyContract');

module.exports = function (deployer) {
  deployer.deploy(MyContract /* constructor arguments */);
};
```

**Step 5: Convert tests**

Test scripts must be converted from Hardhat's testing patterns, which use `ethers.js` and `chai`. In TronBox, you will use the globally available `tronWeb` object for chain interactions, the `artifacts` object to load contracts, and standard `assert` statements for assertions.

JavaScript

javascript

```
// test/my_contract.test.js (Hardhat)
const { expect } = require('chai');

describe('MyContract', function () {
  it('should store value', async () => {
    const MyContract = await ethers.getContractFactory('MyContract');
    const contract = await MyContract.deploy();

    // Log account balance (wei)
    const [owner] = await ethers.getSigners();
    const balance = await ethers.provider.getBalance(owner.address);
    console.log('ETH balance (wei):', balance);

    // Set value via transaction
    await contract.setValue(42);

    // Verify state via call
    const value = await contract.getValue();
    expect(value).to.equal(42, 'getValue should return 42 after setValue');
  });
});
```

JavaScript

javascript

```
// test/my_contract.test.js (TronBox)
const MyContract = artifacts.require('MyContract');

contract('MyContract', accounts => {
  it('should work', async () => {
    const instance = await MyContract.deployed();

    // Log account balance (sun)
    const balance = await tronWeb.trx.getBalance(accounts[0]);
    console.log('TRX balance (sun):', balance);

    // Set value via transaction
    await instance.setValue(42);

    // Verify state via call
    const value = await instance.getValue();
    assert.equal(value.toString(), '42', 'getValue should return 42 after setValue');
  });
});
```

**Step 6: Compile contracts**

Compile to generate TVM bytecode and ABI artifacts. Outputs are written to `./build/contracts` for use in migrations and tests.

Terminal

shell

```
tronbox compile
```

**Expected output:**

Terminal

shell

```
➜  my-tron-project tronbox compile
Compiling your contracts...
===========================
Compiling ./contracts/MyContract.sol...
Compiling ./contracts/Migrations.sol...
Writing artifacts to ./build/contracts

> Compiled successfully using:
  - solc: 0.8.6
```

**Step 7: Deploy contracts**

Deploy your contracts to the desired network. For local testing, you can use the TronBox development environment (TRE).

First, start the local development node:

Terminal

shell

```
docker run -it -p 9090:9090 --rm --name tron tronbox/tre
```

Then, run the `migrate` command to deploy the contracts to the `development` network:

Terminal

shell

```
tronbox migrate
```

**Expected output:**

Terminal

shell

```
➜  my-tron-project tronbox migrate
Using network 'development'.

Compiling your contracts...
===========================
> Everything is up to date, there is nothing to compile.

Running migration: 1_initial_migration.js
  Deploying Migrations...
  Migrations:
    (base58) TJh3ZF79JTbvDn6KZuCpZSAy1MAfvxPGK4
    (hex) 415faa97a14951ab963c9b21398396344c899a84d4
Saving successful migration to network...
Saving artifacts...
Running migration: 2_deploy_contracts.js
  Deploying MyContract...
  MyContract:
    (base58) TQTKy6ri3if3QJJ6EYpBqW5rokaj1RWgcg
    (hex) 419ee3391925a4d5b9c7299faf509478ad30e0ddd9
Saving successful migration to network...
Saving artifacts...
```

To deploy to a different network like Nile, use the `--network` flag:

Terminal

shell

```
tronbox migrate --network nile
```

**Step 8: Test contracts**

Run your tests against the desired network. By default, tests run against the `development` network.

Terminal

shell

```
tronbox test
```

**Expected output:**

Terminal

shell

```
➜  my-tron-project tronbox test
Using network 'development'.

Compiling your contracts...
===========================
> Everything is up to date, there is nothing to compile.

Deploying contracts to development network...
Preparing JavaScript tests (if any)...


  Contract: MyContract
TRX balance (sun): 8062066112
    ✔ should work


  1 passing (35ms)
```

To run tests against a different network like Nile, use the `--network` flag:

Terminal

shell

```
tronbox test --network nile
```

## Conclusion [​](#conclusion)

Congratulations! You have successfully migrated your project from Hardhat to TronBox.

The key takeaways from this guide are:

* **Project Structure**: While the `contracts` folder is similar, you must adapt Hardhat's deployment scripts into TronBox's `migrations` format.
* **Configuration**: The main changes are in `tronbox-config.js`, where you need to adapt network endpoints, account keys, and compiler settings for the TRON network.
* **API Differences**: Script conversion requires replacing `ethers` with `tronWeb` for deployment and test interactions, and replacing `chai` with `assert` for test assertions.

Your project is now ready to leverage the full power of the TRON ecosystem. Happy coding!