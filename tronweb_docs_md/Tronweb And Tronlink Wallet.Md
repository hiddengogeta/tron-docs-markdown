

* TronWeb and TronLink wallet
Version: 6.3.0

Here we will introduce the relationship between TronWeb and TronLink wallet including chrome and firefox extensions, Android and iOS Applications.

We do not limit TronLink-related wallets. Any wallet that implements the [TIP-1193](https://github.com/tronprotocol/tips/blob/master/tip-1193.md) protocol can follow the rules described below.

TronLink wallets import the TronWeb lib and initiate a TronWeb instance and export it to the website. Of course, the user's agreement is required.

Website developers can use the exposed tronWeb to sign transactions. Usually, a web3 DApp needs the authorized transaction signature of the wallet users. For wallet users, their assets are safely stored in the wallet, and no website can get the wallet users' private key. Website developers only initiate signature requests for transactions, and the authorization awaits the wallet users' acceptance.

If you want to know how to use the TronLink wallet, please refer to the [help center](https://tronlinkorg.zendesk.com/hc/en-us).

If you are interested in DApp development and want your website to connect to the TronLink wallets, the following code may be very helpful.

# Obtain the `tron` provider from TronLink wallet

Generally, we need to first obtain the tron object that the TronLink wallet injects into the page, which contains the methods and properties that we interact with the TronLink wallet.

We can obtain the `tron` object like this:

```
const tron = window.tron;  
const tronWeb = tron.tronWeb;
```

The tron object need some time to initiate, so you may need to access it in setTimeout function.

# sign transaction with TronLink wallet

When the website gets the injected tronWeb instance by TronLink wallet, you can create a transaction with tronWeb and sign the transaction with `tronWeb.trx.sign` function. When you call `tronWeb.trx.sign` function, TronLink will pop up a confirmation dialog that needs users to confirm.

```
const signedTx = await tronWeb.trx.sign(tx);
```

# Broadcast the transaction

```
await tronWeb.trx.sendRawTransaction(signedTx);
```

# Try tronwallet-adapter

Tronwallet‑adapter is a lightweight library designed to make it easier for DApps to connect with multiple wallets that support TRON network. For detailed usage and API documentation, please visit [here](https://walletadapter.org/).