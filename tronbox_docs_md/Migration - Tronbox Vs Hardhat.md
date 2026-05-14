

# TronBox vs Hardhat [​](#tronbox-vs-hardhat)

This guide compares TronBox and Hardhat for developers familiar with Hardhat who want to understand the similarities and differences.

## Command Mapping [​](#command-mapping)

### From Hardhat to TronBox [​](#from-hardhat-to-tronbox)

Hardhat developers will need to adjust to TronBox's migration-based workflow:

| Task | Hardhat | TronBox | Notes |
| --- | --- | --- | --- |
| **Initialize** | `npx hardhat init` | `tronbox init` | Different structure |
| **Compile** | `npx hardhat compile` | `tronbox compile` | Similar |
| **Deploy** | `npx hardhat run scripts/deploy.js --network <name>` | `tronbox migrate --network <name>` | Use migrations |
| **Test** | `npx hardhat test --network <name>` | `tronbox test --network <name>` | Different assertions |

**Key adaptation:** Convert your deployment scripts to numbered migration files.

## Configuration Comparison [​](#configuration-comparison)

### From Hardhat Config to TronBox Config [​](#from-hardhat-config-to-tronbox-config)

**Hardhat Configuration (hardhat.config.js):**

JavaScript

javascript

```
require('@nomicfoundation/hardhat-toolbox');

module.exports = {
  networks: {
    localhost: {
      url: 'http://127.0.0.1:8545',
      accounts: [process.env.PRIVATE_KEY]
    },
    mainnet: {
      url: `https://mainnet.infura.io/v3/${process.env.INFURA_KEY}`,
      accounts: [process.env.PRIVATE_KEY],
      chainId: 1
    }
  },
  solidity: {
    version: '0.8.6'
  }
};
```

**TronBox Configuration (tronbox-config.js):**

JavaScript

javascript

```
module.exports = {
  networks: {
    development: {
      privateKey: process.env.PRIVATE_KEY, // ⚠️ Single key, not array
      feeLimit: 1e8, // ⚠️ Resource limit
      fullHost: 'http://127.0.0.1:9090', // ⚠️ Use `fullHost`, not `url`
      network_id: '9'
    },
    mainnet: {
      privateKey: process.env.PRIVATE_KEY,
      feeLimit: 1e8,
      fullHost: 'https://api.trongrid.io', // ⚠️ TRON mainnet
      network_id: '1'
    }
  },
  compilers: {
    solc: {
      version: '0.8.6' // ⚠️ TVM Solidity version
    }
  }
};
```

**Key differences:**

* 🔧 **Compiler:** Configure your TVM compiler under the `compilers.solc` object.
* 🔑 **Authentication:** Provide a single `privateKey` for the account.
* 🌐 **Endpoint:** Use `fullHost` to specify the network URL.
* ⚡ **Resources:** Set the `feeLimit` as the resource upper limit for a transaction.
* 🔌 **Plugins:** No external plugins needed; core features are built-in.

## Blockchain Interaction Library [​](#blockchain-interaction-library)

### From Ethers.js (Hardhat) to TronWeb [​](#from-ethers-js-hardhat-to-tronweb)

**Ethers.js pattern you know:**

JavaScript

javascript

```
const { ethers } = require('hardhat');

// Deploy contract
const MyContract = await ethers.getContractFactory('MyContract');
const contract = await MyContract.deploy({ gasLimit: 3000000 });
await contract.waitForDeployment();

// Call function
const result = await contract.getValue();

// Send transaction
await contract.setValue(42);
```

**TronWeb equivalent:**

JavaScript

javascript

```
const { TronWeb } = require('tronweb');
const tronWeb = new TronWeb({
  fullHost: 'http://127.0.0.1:9090',
  privateKey: process.env.PRIVATE_KEY
});

// Deploy contract
const contract = await tronWeb.contract().new({
  abi: abi,
  bytecode: bytecode,
  feeLimit: 1e8,
  parameters: [arg1, arg2]
});

// Call function
const result = await contract.getValue();

// Send transaction
await contract.setValue(42);
```

**Key differences:**

* 🔑 Private key: set on the `TronWeb` instance.
* 🧭 Sender: Signer is configured in TronWeb instance.
* ⚡ Fees: use `feeLimit` (replaces `gasLimit` + `gasPrice`).
* 📮 Addresses: Base58 (`T...`) instead of `0x...`.

## Testing Comparison [​](#testing-comparison)

### Hardhat to TronBox Testing [​](#hardhat-to-tronbox-testing)

**Main changes:**

| Aspect | Hardhat | TronBox |
| --- | --- | --- |
| **Structure** | `describe()` + `it()` | `contract()` + `it()` |
| **Assertions** | `expect(x).to.equal(y)` | `assert.equal(x, y)` |
| **Deployment** | `await Contract.deploy()` | `await Contract.new()` |
| **Accounts** | `await ethers.getSigners()` | `accounts` parameter |

**Example conversion:**

JavaScript

javascript

```
// Hardhat
const { expect } = require('chai');

describe('MyContract', function () {
  let contract;
  let owner;

  beforeEach(async function () {
    [owner] = await ethers.getSigners();
    const MyContract = await ethers.getContractFactory('MyContract');
    contract = await MyContract.deploy();
  });

  it('should work', async function () {
    expect(await contract.getValue()).to.equal(0);
  });
});
```

JavaScript

javascript

```
// TronBox
const MyContract = artifacts.require('MyContract');

contract('MyContract', accounts => {
  let instance;

  beforeEach(async () => {
    instance = await MyContract.new();
  });

  it('should pass test', async () => {
    // Test code here
    const result = await instance.getValue();
    assert.equal(result, expectedValue);
  });
});
```

## Common Pitfalls & Solutions [​](#common-pitfalls-solutions)

### For Hardhat Developers [​](#for-hardhat-developers)

| Issue | Cause | Solution |
| --- | --- | --- |
| **"Invalid address"** | Using 0x... format | Use TRON Base58 addresses (T...) |
| **"Out of energy"** | Insufficient feeLimit | Increase feeLimit to 1e8 or higher |
| **"expect is not defined"** | Using Hardhat assertions | Use `assert` instead of `expect` |
| **Tests fail with ethers** | `ethers` not compatible | Replace with `tronWeb` |
| **Migration fails** | Wrong network config | Check fullHost |

## Quick Reference: Code Snippets [​](#quick-reference-code-snippets)

### Contract Deployment [​](#contract-deployment)

JavaScript

javascript

```
// Hardhat
const MyContract = await ethers.getContractFactory('MyContract');
const contract = await MyContract.deploy(arg1, arg2);

// TronBox
const MyContract = artifacts.require('MyContract');
const instance = await MyContract.new(arg1, arg2);
```

### Reading Contract State [​](#reading-contract-state)

JavaScript

javascript

```
// Hardhat
const value = await contract.getValue();

// TronBox
const value = await instance.getValue(); // ✅ Same!
```

### Sending Transactions [​](#sending-transactions)

JavaScript

javascript

```
// Hardhat
await contract.setValue(42);

// TronBox
await instance.setValue(42); // ✅ Same!
```

## Summary [​](#summary)

### For Hardhat Developers [​](#for-hardhat-developers-1)

**What's different:**

* ⚠️ `ether` → `tronWeb`
* ⚠️ Address format (0x... → T...)
* ⚠️ Units (wei/ether → sun/TRX)
* ⚠️ Migration-based deployment (not custom scripts)
* ⚠️ Different test assertions (assert, not expect)
* ⚠️ Config file name and network params
* ⚠️ Global installation (not per-project)

**What you'll appreciate:**

* ✅ Built-in migration state tracking
* ✅ Simpler transaction sending (no gas estimation)
* ✅ Familiar Solidity compilation

**Your advantage:** More structured deployment process!

### Next Steps [​](#next-steps)

1. **Install TronBox:** `npm install -g tronbox`
2. **Try a quick start:** `tronbox init`
3. **Get testnet TRX:** [Visit Nile faucet](https://nileex.io/join/getJoinPage)
4. **Deploy your first contract:** `tronbox migrate --network nile`
5. **Explore TronWeb:** Practice unit conversion and basic API usage
6. **Migrate a real project:** Follow the migration workflows in the next guide

Welcome to TRON development! 🚀