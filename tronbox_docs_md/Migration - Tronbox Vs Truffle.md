

# TronBox vs Truffle [​](#tronbox-vs-truffle)

This guide compares TronBox and Truffle for developers familiar with Truffle who want to understand the similarities and differences.

## Command Mapping [​](#command-mapping)

### From Truffle to TronBox [​](#from-truffle-to-tronbox)

Great news for Truffle developers: commands are nearly identical!

| Task | Truffle | TronBox | Notes |
| --- | --- | --- | --- |
| **Initialize** | `truffle init` | `tronbox init` | ✅ Same |
| **Compile** | `truffle compile` | `tronbox compile` | ✅ Same |
| **Deploy** | `truffle migrate --network <name>` | `tronbox migrate --network <name>` | ✅ Same |
| **Test** | `truffle test --network <name>` | `tronbox test --network <name>` | ✅ Same |
| **Unbox** | `truffle unbox <box-name>` | `tronbox unbox <box-name>` | ✅ Same |

**The main difference:** Replace `web3` with `tronWeb` in your scripts and tests.

## Configuration Comparison [​](#configuration-comparison)

### From Truffle Config to TronBox Config [​](#from-truffle-config-to-tronbox-config)

**Truffle Configuration (truffle-config.js):**

JavaScript

javascript

```
module.exports = {
  networks: {
    development: {
      host: '127.0.0.1',
      port: 8545,
      network_id: '*',
      gas: 6721975,
      gasPrice: 20000000000
    },
    mainnet: {
      provider: () =>
        new HDWalletProvider(process.env.MNEMONIC, `https://mainnet.infura.io/v3/${process.env.INFURA_KEY}`),
      network_id: 1,
      gas: 5500000,
      gasPrice: 20000000000
    }
  },
  compilers: {
    solc: {
      version: '0.8.6'
    }
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
      // Supports both privateKey and mnemonic
      privateKey: process.env.PRIVATE_KEY,
      // Or use mnemonic:
      // mnemonic: process.env.MNEMONIC,
      feeLimit: 1e8, // ⚠️ Replaces gas + gasPrice
      fullHost: 'http://127.0.0.1:9090', // ⚠️ Single endpoint, not host + port
      network_id: '9'
    },
    mainnet: {
      privateKey: process.env.PRIVATE_KEY,
      feeLimit: 1e8,
      fullHost: 'https://api.trongrid.io', // ⚠️ TRON mainnet endpoint
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

* 🔑 **Authentication:** Supports `privateKey` or `mnemonic`.
* 🌐 **Endpoint:** Uses `fullHost` (single URL) instead of separate host + port.
* ⚡ **Resources:** Uses `feeLimit` (replaces `gas` + `gasPrice`).
* 💱 **Units:** TRON uses `sun` for amounts (1 TRX = 1,000,000 sun).

## Blockchain Interaction Library [​](#blockchain-interaction-library)

### From Web3.js to TronWeb [​](#from-web3-js-to-tronweb)

**Web3.js pattern you know:**

JavaScript

javascript

```
const { Web3 } = require('web3');
const web3 = new Web3('http://localhost:8545');

// Add account
const account = web3.eth.accounts.privateKeyToAccount(process.env.PRIVATE_KEY);
web3.eth.accounts.wallet.add(account);
web3.defaultAccount = account.address;

// Deploy contract
const contract = new web3.eth.Contract(abi);
const instance = await contract
  .deploy({
    data: bytecode,
    arguments: [arg1, arg2]
  })
  .send({ gas: 1500000 });

// Call function
const result = await instance.methods.getValue().call();

// Send transaction
await instance.methods.setValue(42).send({ gas: 1500000 });
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
const result = await contract.getValue().call();

// Send transaction
await contract.setValue(42).send({
  feeLimit: 1e8
});
```

**Key differences:**

* 🔑 Private key: set on the `TronWeb` instance.
* 🧭 Sender: no need to set `defaultAccount`.
* ⚡ Fees: use `feeLimit` (replaces `gas` + `gasPrice`).
* 📮 Addresses: Base58 (`T...`) instead of `0x...`.

## Testing Comparison [​](#testing-comparison)

### Truffle to TronBox Testing [​](#truffle-to-tronbox-testing)

**Great news:** Your test structure remains the same!

JavaScript

javascript

```
// Both Truffle and TronBox use this pattern
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

**Only change needed:** Replace `web3` calls with `tronWeb`:

JavaScript

javascript

```
// Truffle
const balance = await web3.eth.getBalance(accounts[0]);
const block = await web3.eth.getBlock('latest');

// TronBox
const balance = await tronWeb.trx.getBalance(accounts[0]);
const block = await tronWeb.trx.getCurrentBlock();
```

## Common Pitfalls & Solutions [​](#common-pitfalls-solutions)

### For Truffle Developers [​](#for-truffle-developers)

| Issue | Cause | Solution |
| --- | --- | --- |
| **"Invalid address"** | Using 0x... format | Use TRON Base58 addresses (T...) |
| **"Out of energy"** | Insufficient feeLimit | Increase feeLimit to 1e8 or higher |
| **Tests fail with web3** | `web3` not compatible | Replace with `tronWeb` |
| **Migration fails** | Wrong network config | Check fullHost |

## Quick Reference: Code Snippets [​](#quick-reference-code-snippets)

### Contract Deployment [​](#contract-deployment)

JavaScript

javascript

```
// Truffle
const instance = await MyContract.new(arg1, arg2);

// TronBox
const instance = await MyContract.new(arg1, arg2); // ✅ Same!
```

### Reading Contract State [​](#reading-contract-state)

JavaScript

javascript

```
// Truffle
const value = await instance.getValue();

// TronBox
const value = await instance.getValue(); // ✅ Same!
```

### Sending Transactions [​](#sending-transactions)

JavaScript

javascript

```
// Truffle
await instance.setValue(42);

// TronBox
await instance.setValue(42); // ✅ Same!
```

## Summary [​](#summary)

### For Truffle Developers [​](#for-truffle-developers-1)

**What stays the same:**

* ✅ Project structure
* ✅ Command patterns
* ✅ Migration workflow
* ✅ Test structure

**What changes:**

* ⚠️ `web3` → `tronWeb`
* ⚠️ Config file name and network params
* ⚠️ Address format (0x... → T...)
* ⚠️ Units (wei/ether → sun/TRX)

**Your advantage:** Minimal learning curve, almost identical workflow!

### Next Steps [​](#next-steps)

1. **Install TronBox:** `npm install -g tronbox`
2. **Try a quick start:** `tronbox init`
3. **Get testnet TRX:** [Visit Nile faucet](https://nileex.io/join/getJoinPage)
4. **Deploy your first contract:** `tronbox migrate --network nile`
5. **Explore TronWeb:** Practice unit conversion and basic API usage
6. **Migrate a real project:** Follow the migration workflows in the next guide

Welcome to TRON development! 🚀