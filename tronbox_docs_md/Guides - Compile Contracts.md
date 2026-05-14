

# Compile contracts [​](#compile-contracts)

## Location [​](#location)

All of your contracts are located in your project's `contracts/` directory. As contracts are written in [Solidity](https://docs.soliditylang.org/en/develop/), all files containing contracts will have a file extension of `.sol`. Associated Solidity [libraries](https://docs.soliditylang.org/en/develop/contracts.html#libraries) will also have a `.sol` extension.

You will generate a `Migrations.sol` contract file for deployment by creating an empty TronBox project with the `tronbox init` command. Multiple contract files will be generated if you create your project with TronBox Box.

## Command [​](#command)

To compile a TronBox project, change to the root of the directory where the project is located and then type the following into a terminal:

Terminal

shell

```
tronbox compile
```

Upon the first run, all contracts will be compiled. Upon subsequent runs, TronBox will compile only the contracts that have been changed since the last compile. If you would like to override this behavior, run the above command with the `--all` option.

## Build artifacts [​](#build-artifacts)

Artifacts of your compilation will be placed in the `build/contracts/` directory relative to your project root. (This directory will be created if it does not exist.)

These artifacts are integral to the inner workings of TronBox, and play a vital role in the successful deployment of your application. **You should not edit these files** as they will be overwritten by contract compilation and deployment.

## Dependencies [​](#dependencies)

You can declare contract dependencies using Solidity's import command. TronBox will compile contracts in the correct order and ensure all dependencies are sent to the compiler. Dependencies can be specified in two ways:

### Import dependencies via file name [​](#import-dependencies-via-file-name)

To import contracts from a separate file, add the following code to your Solidity source file:

Solidity

solidity

```
import './AnotherContract.sol';
```

This will make all contracts within `AnotherContract.sol` available. Here, `AnotherContract.sol` is relative to the path of the current contract being written.

Solidity allows other import syntaxes as well. You may see the [Solidity import documentation](https://docs.soliditylang.org/en/latest/layout-of-source-files.html#importing-other-source-files) for more information.

### Import contracts from an external package [​](#import-contracts-from-an-external-package)

TronBox supports dependencies installed via `npm`. To import contracts from a dependency, use the following syntax:

Solidity

solidity

```
import 'somepackage/SomeContract.sol';
```

Here, `somepackage` represents a package installed via `npm`, and `SomeContract.sol` represents a Solidity source file provided by that package.

For more information on how to use TronBox's package management features, please see the [Package Management via NPM](/docs/guides/work-with-npm).

### Supports TIP-467 Stake 2.0 [​](#supports-tip-467-stake-2-0)

`TRON Solidity Compiler v0.8.18` is supported in TronBox v3.1.2. This version supports the new commands and pre-compiled contracts introduced in [TIP-467](https://github.com/tronprotocol/tips/blob/master/tip-467.md).

* TVM: Introduce freezebalancev2(uint256,uint256) in Solidity.
* TVM: Introduce unfreezebalancev2(uint256,uint256) in Solidity.
* TVM: Introduce cancelallunfreezev2() in Solidity.
* TVM: Introduce withdrawexpireunfreeze() in Solidity.
* TVM: Introduce <address payable>.delegateResource(uint256,uint256) in Solidity.
* TVM: Introduce <address payable>.unDelegateResource(uint256,uint256) in Solidity.
* TVM: Introduce <address>.availableUnfreezeV2Size() in Solidity.
* TVM: Introduce <address>.unfreezableBalanceV2(uint256) in Solidity.
* TVM: Introduce <address>.expireUnfreezeBalanceV2(uint256) in Solidity.
* TVM: Introduce <address>.delegatableResource(uint256) in Solidity.
* TVM: Introduce <address>.resourceV2(address,uint256) in Solidity.
* TVM: Introduce <address>.checkUnDelegateResource(address,uint256) in Solidity.
* TVM: Introduce <address>.resourceUsage(uint256) in Solidity.
* TVM: Introduce <address>.totalResource(uint256) in Solidity.
* TVM: Introduce <address>.totalDelegatedResource(uint256) in Solidity.
* TVM: Introduce <address>.totalAcquiredResource(uint256) in Solidity.
* TVM: Introduce new magic type chain in Solidity and the parameters that can be queried include chain.totalNetLimit, chain.totalNetWeight, chain.totalEnergyCurrentLimit, chain.totalEnergyWeight and chain.unfreezeDelayDays.