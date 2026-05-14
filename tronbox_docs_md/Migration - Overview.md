

# Migrating to TronBox [​](#migrating-to-tronbox)

This guide helps Truffle and Hardhat developers migrate their projects to TronBox, focusing on migration workflows, command mappings, and practical tips to accelerate the process.

## Quick Overview [​](#quick-overview)

**TronBox** is a development framework specifically designed for the TRON network, inspired by Truffle's workflow and conventions. If you're familiar with Truffle or Hardhat, you'll find TronBox's workflow intuitive, with some TRON-specific adaptations.

| Aspect | TronBox | Developer Notes |
| --- | --- | --- |
| **Project Structure** | Same as Truffle | ✅ Truffle devs: Instantly familiar ⚠️ Hardhat devs: Uses migrations, not scripts |
| **Primary Library** | TronWeb | ⚠️ Similar to Web3.js/Ethers.js but TRON-specific |
| **Solidity Version** | TVM Solidity versions | ⚠️ Truffle/Hardhat use EVM Solidity versions |
| **Address Format** | Base58 (T...) | ⚠️ Different from Ethereum's 0x... format |
| **Resource Model** | Energy + Bandwidth + feeLimit | ⚠️ Different from Ethereum's gas model |
| **Unit System** | sun / TRX (1 TRX = 1,000,000 sun) | ⚠️ Different from wei / ether |

## Installation & Setup [​](#installation-setup)

### For Truffle Developers [​](#for-truffle-developers)

If you're coming from Truffle, TronBox will feel like home:

Terminal

shell

```
# Install TronBox (similar to Truffle)
npm install -g tronbox

# Initialize a project
tronbox init
```

**What's the same:**

* ✅ Global installation
* ✅ Same project structure (`contracts/`, `migrations/`, `test/`)
* ✅ Same command patterns

**What's different:**

* ⚠️ Configuration file is `tronbox-config.js` (not `truffle-config.js`)
* ⚠️ Network configuration uses TRON-specific parameters

### For Hardhat Developers [​](#for-hardhat-developers)

If you're coming from Hardhat, note these key differences:

Terminal

shell

```
# Install TronBox globally (unlike Hardhat's local installation)
npm install -g tronbox

# Initialize a project
tronbox init
```

**Key differences from Hardhat:**

* ⚠️ Uses `migrations/` directory instead of `scripts/`
* ⚠️ Migration-based deployment (numbered files like `2_deploy_contracts.js`)
* ⚠️ Built-in migration state tracking (no manual logic needed)
* ⚠️ Different test assertion style (closer to Truffle)

## TRON-Specific Concepts [​](#tron-specific-concepts)

### Address Format & Validation [​](#address-format-validation)

TRON addresses use Base58 and typically start with 'T' (for example, `TRX9aKv8GQ9KvWxJ...`).

**Address Validation:**

JavaScript

javascript

```
// Validate an address format
const isValid = tronWeb.isAddress('TRX9aKv8GQ9KvWxJ...');
```

**Common pitfall for Ethereum devs:**

* ❌ Don't use `0x` prefix for TRON addresses
* ✅ Use Base58 format (addresses usually start with 'T')

### Unit Conversion [​](#unit-conversion)

**Ethereum units you know:**

* 1 ether = 10^18 wei
* `web3.utils.toWei('1', 'ether')` → wei
* `web3.utils.fromWei('1000000000000000000', 'ether')` → ether

**TRON units:**

* 1 TRX = 1,000,000 sun (10^6, not 10^18!)
* `tronWeb.toSun(1)` → 1,000,000 sun
* `tronWeb.fromSun(1000000)` → 1 TRX

**Example:**

JavaScript

javascript

```
// Convert TRX to sun
const amountInSun = tronWeb.toSun(10); // 10 TRX = 10,000,000 sun

// Convert sun to TRX
const amountInTrx = tronWeb.fromSun(1000000); // 1,000,000 sun = 1 TRX
```

### Resource Model: Energy & Bandwidth [​](#resource-model-energy-bandwidth)

**Ethereum gas model you know:**

* Pay gas for every operation
* `gasLimit × gasPrice = max cost`

**TRON resource model:**

* **Bandwidth:** Free daily allowance for transactions
* **Energy:** Consumed by smart contract execution
* **feeLimit:** Maximum TRX willing to burn if resources insufficient

**Key parameters:**

JavaScript

javascript

```
{
  feeLimit: 1e8,              // Max 100 TRX (in sun)
  callValue: 0                // TRX sent with transaction
}
```

**Best practices:**

* 🔋 Set `feeLimit` generously (won't charge extra if not used)
* 💡 Start with `1e8` (100 TRX) for complex contracts
* 📊 Monitor energy consumption in TronScan
* ⚡ Consider staking TRX for energy if deploying frequently

## Network Configuration Examples [​](#network-configuration-examples)

### TRON Networks [​](#tron-networks)

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

    // Shasta Testnet (alternative testnet)
    shasta: {
      privateKey: process.env.PRIVATE_KEY,
      feeLimit: 1e8,
      fullHost: 'https://api.shasta.trongrid.io',
      network_id: '2'
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

## Learning Resources [​](#learning-resources)

### Official Documentation [​](#official-documentation)

* **TronBox Docs:** <https://tronbox.io/docs/quickstart>
* **TronWeb Docs:** <https://tronweb.network/docu/docs/intro/>
* **TRON Network:** <https://developers.tron.network>
* **TVM Solidity:** <https://github.com/tronprotocol/solidity/releases>

### Tools [​](#tools)

* **TronBox TRE Docker (local runtime):** <https://hub.docker.com/r/tronbox/tre>
* **TronGrid (API):** <https://www.trongrid.io>
* **Mainnet Explorer:** <https://tronscan.org>
* **Nile Testnet Explorer:** <https://nile.tronscan.org>
* **Shasta Testnet Explorer:** <https://shasta.tronscan.org>
* **Nile Faucet (get test TRX):** <https://nileex.io/join/getJoinPage>
* **Shasta Faucet (get test TRX):** <https://shasta.tronex.io/join/getJoinPage>

### Getting Help [​](#getting-help)

* **GitHub Issues:** <https://github.com/tronprotocol/tronbox>