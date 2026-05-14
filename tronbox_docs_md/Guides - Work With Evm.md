

# Work with EVM-compatible chains [​](#work-with-evm-compatible-chains)

Tronbox supports deploying contracts to EVM-compatible blockchains.

TIP

*NOTE: This feature requires TronBox v4.0.0 or later.*

## Configuration file [​](#configuration-file)

The configuration file for EVM related configurations is named `tronbox-evm-config.js` and is located in the root directory of the project directory. The file content is as follows:

JavaScript

javascript

```
module.exports = {
  networks: {
    bttc: {
      privateKey: process.env.PRIVATE_KEY_BTTC,
      fullHost: 'https://rpc.bt.io',
      gas: 8500000, // Gas sent with each transaction
      gasPrice: '500000000000000', // 500,000 gwei (in wei)
      network_id: '1'
    },
    development: {
      privateKey: process.env.PRIVATE_KEY_DEV,
      fullHost: 'http://127.0.0.1:8545',
      network_id: '*'
    }
  },
  compilers: {
    solc: {
      version: '0.8.7',
      // An object with the same schema as the settings entry in the Input JSON.
      // See https://docs.soliditylang.org/en/latest/using-the-compiler.html#input-description
      settings: {
        // optimizer: {
        //   enabled: true,
        //   runs: 200
        // },
        // evmVersion: 'istanbul',
        // viaIR: true,
      }
    }
  }
};
```

## Compile contracts [​](#compile-contracts)

To deploy to an EVM-compatible blockchain, you must compile your contracts using an EVM solidity compiler. Run the following command:

Terminal

shell

```
tronbox compile --evm
```

When you add the `--evm` flag to the compile command, the `solc` version configured in the `tronbox-evm-config.js` file will be used for compilation.

## Deploy contracts [​](#deploy-contracts)

To deploy to an EVM-compatible blockchain such as the BTTC network, configure your network settings in `tronbox-evm-config.js` and run the following command:

Terminal

shell

```
tronbox migrate --network bttc --evm
```

When you add the `--evm` flag to the migrate command, the `network` settings configured in the `tronbox-evm-config.js` file will be used for deployment.

For details on the deployment script, pleaase see [Deploy contracts](/docs/guides/deploy-contracts) .

## Test contracts [​](#test-contracts)

To run tests on an EVM-compatible blockchain, use the following command:

Terminal

shell

```
tronbox test --evm
```

When you add the `--evm` flag to the test command, the `network` settings configured in the `tronbox-evm-config.js` file will be used for testing.

For more information about the test script, please see [Testing contracts](/docs/guides/test-contracts) .