

# Write JavaScript tests [​](#write-javascript-tests)

TronBox uses the [Mocha](https://mochajs.org/) testing framework and [Chai](http://chaijs.com/) for assertions to provide you with a solid framework from which to write your JavaScript tests. Let's dive in and see how TronBox builds on top of Mocha to make testing your contracts a breeze.

TIP

*NOTE: If you're unfamiliar with writing unit tests in Mocha, please see [Mocha's documentation](https://mochajs.org/#getting-started) before continuing.*

## Use contract() instead of describe() [​](#use-contract-instead-of-describe)

Structurally, your tests should remain largely unchanged from those of Mocha: Your tests should exist in the `./test` directory, they should end with a `.js` extension, and they should contain code that Mocha will recognize as an automated test. What makes TronBox tests different from those of Mocha is the `contract()` function.

* Before each `contract()` function is run, your contracts are redeployed to the running TRON network so the tests within it run with a clean contract state.
* The `contract()` function provides a list of accounts made available by the current TRON network, which you can use to write tests.

## Use contract abstractions within your tests [​](#use-contract-abstractions-within-your-tests)

Contract abstractions are the basis for making TRON contract interaction possible from JavaScript. Because TronBox has no way of detecting which contracts you'll need to interact with, you'll need to ask for those contracts explicitly. You do this by using the `artifacts.require()` method, a method provided by TronBox that allows you to request a usable contract abstraction for a specific Solidity contract. As you'll see in the example below, you can then use this abstraction to make sure your contracts are working properly. For more information on using contract abstractions see the [Interact with contracts](/docs/guides/interact-with-contracts) section.

## Using artifacts.require() [​](#using-artifacts-require)

Using `artifacts.require()` within your tests works the same way as using it within your migrations; you just need to pass the name of the contract. See the [artifacts.require()](/docs/guides/deploy-contracts#artifacts-require) documentation in the Migrations section for detailed usage.

## Using tronWrap [​](#using-tronwrap)

A `tronWrap` instance is available in each test file, which can be referenced directly. So calling `tronWrap.trx.getBalance(account)` just works!

## Examples [​](#examples)

Here's an example test provided in the [MetaCoin TronBox](https://github.com/tronsuper/metacoin-box) Box using [async/await](https://javascript.info/async-await) notation. Note the use of the `contract()` function, the `accounts` array for specifying available TRON accounts, and our use of `artifacts.require()` for interacting directly with our contracts.

Filename: `./test/metacoin.js`

JavaScript

javascript

```
const MetaCoin = artifacts.require('MetaCoin');

contract('2nd MetaCoin test', async accounts => {
  it('should put 10000 MetaCoin in the first account', async () => {
    let instance = await MetaCoin.deployed();
    let balance = await instance.getBalance.call(accounts[0]);
    assert.equal(balance.valueOf(), 10000);
  });

  it('should call a function that depends on a linked library', async () => {
    let meta = await MetaCoin.deployed();
    let outCoinBalance = await meta.getBalance.call(accounts[0]);
    let metaCoinBalance = Number(outCoinBalance);
    let outCoinConvertedBalance = await meta.getConvertedBalance.call(accounts[0]);
    let metaCoinConvertedBalance = Number(outCoinConvertedBalance);
    assert.equal(metaCoinConvertedBalance, 2 * metaCoinBalance);
  });

  it('should send coin correctly', async () => {
    // Get initial balances of first and second account.
    let account_one = accounts[0];
    let account_two = accounts[1];

    let amount = 10;

    let instance = await MetaCoin.deployed();
    let meta = instance;

    let balance = await meta.getBalance.call(account_one);
    let account_one_starting_balance = Number(balance);

    balance = await meta.getBalance.call(account_two);
    let account_two_starting_balance = Number(balance);
    await meta.sendCoin(account_two, amount, { from: account_one });

    balance = await meta.getBalance.call(account_one);
    let account_one_ending_balance = Number(balance);

    balance = await meta.getBalance.call(account_two);
    let account_two_ending_balance = Number(balance);

    assert.equal(
      account_one_ending_balance,
      account_one_starting_balance - amount,
      "Amount wasn't correctly taken from the sender"
    );
    assert.equal(
      account_two_ending_balance,
      account_two_starting_balance + amount,
      "Amount wasn't correctly sent to the receiver"
    );
  });
});
```

Execute the tests:

Terminal

shell

```
tronbox test
```

This test will produce the following output:

Terminal

shell

```
Using network 'development'.

Deploying contracts to development network...
Preparing Javascript tests (if any)...


  Contract: MetaCoin
    ✔ should put 10000 MetaCoin in the first account
    ✔ should call a function that depends on a linked library (68ms)
    ✔ should send coin correctly (137ms)


  3 passing (240ms)
```

## Specifying tests [​](#specifying-tests)

You can limit the tests to a specific file in the test directory as shown below:

Terminal

shell

```
tronbox test ./test/metacoin.js
```

For more information, please see the [Command line options](/docs/reference/command-line-options).