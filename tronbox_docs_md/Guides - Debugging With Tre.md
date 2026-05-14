

# Debugging with TRE [​](#debugging-with-tre)

TronBox provides a TronBox Runtime Environment (TRE) private chain, a local TRON network designed for development. It allows you to deploy your contracts, run your tests and debug your code on your local environment. When using this network on TronBox, you need to use Docker to pull the image. For the specific usage process, please refer to the [documentation](/docs/quickstart#deploy-to-tre).

## Solidity `console.log` [​](#solidity-console-log)

TIP

*NOTE: This feature requires TronBox v3.4.0 or later.*

When running your contracts and tests on TronBox Runtime Environment (TRE), you can print logging messages and contract variables calling `console.log` from your Solidity code. To use it, you have to import `tronbox/console.sol` in your contract code.

This is what it looks like:

Solidity

solidity

```
pragma solidity ^0.8.0;

import "tronbox/console.sol"; 

contract Token {
  mapping(address => uint) balance;
  event Transfer(address _from, address _to, uint256 _value);

  constructor() {
      balance[msg.sender] = 100;
  }

  //...
}
```

Then you can just add some `console.log` calls to the `transfer()` function as if you were using it in JavaScript:

Solidity

solidity

```
function transfer(
    address _sender,
    address _recipient,
    uint256 _amount
) public {
    require(_recipient != address(0), "TRANSFER_TO_ZERO_ADDRESS");
    uint256 balanceOfSender = balance[_sender];
    require(balanceOfSender >= _amount, "NO_ENOUGH_BALANCE_TO_TRANSFER");

    console.log( 
        "Transferring from %s to %s %s tokens", 
        msg.sender, 
        _recipient, 
        _amount 
    );

    balanceOfSender -= _amount;
    balance[_sender] = balanceOfSender;
    balance[_recipient] += _amount;
    emit Transfer(_sender, _recipient, _amount);
}
```

Execute the deployment:

Terminal

shell

```
tronbox migrate
```

The log output is shown as follows:

Terminal

solidity

```
Compiling your contracts ...
============================
Compiling ./contracts/Token.sol...
Compiling tronbox/console.sol...
Writing artifacts to ./build/contracts

> Compiled successfully using:
  - solc: 0.8.6
Using network 'development'.

Running migration: 1_initial_migration.js
  Deploying Token...
  Token:
    (base58) TJWQUFE9aZzuugnYsXXKVtJQcUWQNHBY9V
    (hex) 415da779869e8eac338beaf7cbeda1cdfe412be84f
Saving artifacts...
Transferring from TJHD16Qq3aWtygQqU4R5UcAGh3hFKxnEwQ to TGjX4QszjhRbyP8k39cGert9pSvkN2sRTA 100 tokens
```