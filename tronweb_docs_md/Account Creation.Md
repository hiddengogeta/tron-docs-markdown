

* Account creation
Version: 6.3.0

On this page

# Account creation

This is a tutorial about how to create an account using TronWeb.

## 1. Generate an account[​](#1-generate-an-account "Direct link to 1. Generate an account")

First, you need to use `tronWeb.createAccount()` to create an account.

```
const account = await tronWeb.createAccount();
```

## 2. Activate the account[​](#2-activate-the-account "Direct link to 2. Activate the account")

After creating an account, you need to activate it. First, use your already exist account to instantiate TronWeb. Then, use `tronWeb.trx.sendTrx()` to send TRX to the account.

```
const transaction = await tronWeb.trx.sendTrx(  
  account.address.base58,  
  1000000  
);
```

You can also use `tronWeb.transactionBuilder.createAccount()`, then sign the transaction and broadcast it.

```
const tx = await tronWeb.transactionBuilder.createAccount(account.address.base58);  
const signTx = await tronWeb.trx.sign(tx);  
const receipt = await tronWeb.trx.sendRawTransaction(signTx);
```

## 3. Compute address from public key[​](#3-compute-address-from-public-key "Direct link to 3. Compute address from public key")

You may need to compute the TRON address from public key. Here's the method:

```
const pubkey = tronWeb.utils.code.hexStr2byteArray(account.publicKey.replace(/^0x/, ''));  
const addressBytes = tronWeb.utils.crypto.computeAddress(pubkey);  
const addressHex = tronWeb.utils.bytes.byteArray2hexStr(addressBytes);
```

For information about account model, go [here](https://developers.tron.network/docs/account).