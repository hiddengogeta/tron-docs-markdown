

* Learn
Version: 6.3.0

On this page

# Learn

This page will guide you through many TronWeb core concepts and help you learn TronWeb.

> You will learn
>
> * How to instantiate a TronWeb instance.
> * How to create an account.
> * How to query account information.
> * How to create, sign and send a transaction.
> * How to transfer tokens

## Instantiating a TronWeb instance[​](#instantiating-a-tronweb-instance "Direct link to Instantiating a TronWeb instance")

You need to instantiate a TronWeb instance to interact with the TRON network. The `fullNode` or `fullHost` field is required when instantiating TronWeb. So you need to choose a network that you want to interact with.

There are 3 commonly used public networks you can choose:

* Mainnet: <https://api.trongrid.io>
* Shasta Testnet: <https://api.shasta.trongrid.io>
* Nile Testnet: <https://api.nileex.io>

Mainnet is the primary public TRON production blockchain, where actual-value transactions occur on the distributed ledger. In development use cases, we recommend using the testnet.

Here we use the Nile Testnet:

```
import { TronWeb } from 'tronweb';  
const tronWeb = new TronWeb({  
  fullHost: 'https://api.nileex.io',  
});
```

We recommend using TypeScript for type inference and better code completion. If you want to run this code in NodeJS, just replace `import { TronWeb } from 'tronweb';` with `const { TronWeb } = require('tronweb');`.

## Creating an account[​](#creating-an-account "Direct link to Creating an account")

An account is the basis to interact with the TRON chain. You can create an account by following code:

```
const account = tronWeb.createAccount();
```

**Note**:
Please keep the private key secret. Don't share it with anyone else.

After creating an account, you need to activate it. On Nile Testnet, you can open [faucet website](https://nileex.io/join/getJoinPage) to get testing TRX to activate an account.

You can also send any TRX to an account to activate it. You can just send 1 TRX(= 1\_000\_000 sun):

```
const tx = await tronWeb.trx.sendTrx(account.address.base58, 1_000_000);
```

To make the above code run correctly, you need to instantiate the TronWeb instance with the private key of an account that possessed enough TRX:

```
const tronWeb = new TronWeb({  
  fullHost: 'https://api.nileex.io',  
  privateKey: '', // your private key here  
});
```

## Querying account information[​](#querying-account-information "Direct link to Querying account information")

Now you get an activated account. You can query the balance of the account:

```
console.log(await tronWeb.trx.getBalance(account.address.base58));
```

There are many other methods to query account information. You can check them in the [Trx API](/docu/docs/API List/trx/).

## Creating, signing, and sending a transaction[​](#creating-signing-and-sending-a-transaction "Direct link to Creating, signing, and sending a transaction")

In this section, you will learn how to change the chain state by sending a transaction.

### Creating a transaction[​](#creating-a-transaction "Direct link to Creating a transaction")

TronWeb has supported 36 transaction types. Here we use `sendTrx` as an example to show you how to create a transaction:

```
const tx = await tronWeb.transactionBuilder.sendTrx('toAddress', 1_000_000, 'fromAddress');
```

Replace the `toAddress` and the `fromAddress` with the actual address.

If you want to create a different transaction type, simply replace sendTrx with the desired transaction method and provide the appropriate parameters.

### Signing a transaction[​](#signing-a-transaction "Direct link to Signing a transaction")

Before a transaction to be send on the chain, you have to sign it to prove that the transaction is valid. It's a local operation, you **must** keep your private key secret. You can sign a transaction by following code:

```
const signedTx = await tronWeb.trx.sign(tx, 'privateKey');
```

Replace the `privateKey` with the actual private key.

All transactions can be signed in this way. But if you want to use multi sign, you need to use the `multiSign` method:

```
const signedTx = await tronWeb.trx.multiSign(tx, 'privateKey');
```

For more about multi sign, go [here](https://developers.tron.network/docs/multi-signature).

### Sending a transaction[​](#sending-a-transaction "Direct link to Sending a transaction")

The last step is broadcasting the signed transaction:

```
const receipt = await tronWeb.trx.sendRawTransaction(signedTx);
```

The `receipt` is the broadcasting result. You can check the transaction status by check the fields of the receipt.

If `receipt.result` is true, in most time it shows that the transaction has been broadcasted successfully. But it is not guaranteed. You can go to [nile tronscan](https://nile.tronscan.org/) and search `receipt.txid` to check if the broadcasting is successful.

If `receipt.result` is false, the receipt will contain a `messsage` field which shows the reason why the broadcasting fails. The `message` field is a hex string. You can convert it to a string by following code:

```
tronWeb.toUtf8(receipt.message);
```

Now you know how to change the chain state by sending a transaction.

## Transferring tokens[​](#transferring-tokens "Direct link to Transferring tokens")

Transferring tokens requires you to know how to create, sign and send a transaction. There are 4 types of tokens:

* TRX
* TRC10
* TRC20
* TRC721

TRX transfers and TRC10 transfers are among the mentioned transaction types. TRX transferring method is `sendTrx` while TRC10 transferring method is `sendToken`:

```
const sendTRXtx = await tronWeb.transactionBuilder.sendTrx('toAddress', 1_000_000, 'fromAddress');  
const sendTRC10tx = await tronWeb.transactionBuilder.sendToken('toAddress', 1_000_000, 'tokenId', 'fromAddress');
```

TRC20 transfers and TRC721 transfers are about [Contract](/docu/docs/Interact with contract). Before transferring, you need to select a contract address. Then, create a transaction using `triggerSmartContract` with the appropriate parameters to call the contract’s transfer-related methods:

```
const sendTRC20tx = await tronWeb.transactionBuilder.triggerSmartContract(  
  'TRC20ContractAddress',  
  'transfer(address,uint256)',  
  {  
    txLocal: true,  
  },  
  [{ type: 'address', value: 'toAddress' }, { type: 'uint256', value: 1_000_000 }],  
  'fromAddress',  
);  
const sendTRC721tx = await tronWeb.transactionBuilder.triggerSmartContract(  
  'TRC721ContractAddress',  
  'transferFrom(address,address,uint256)',  
  {  
    txLocal: true,  
  },  
  [{ type: 'address', value: 'fromAddress' }, { type: 'address', value: 'toAddress' }, { type: 'uint256', value: 100001 }],  
  'fromAddress',  
);
```

## Next Steps[​](#next-steps "Direct link to Next Steps")

Congratulations! You have completed the first and most important step toward developing on the TRON blockchain. The next steps for your learning are as follows:

1. Read the [Terminology](/docu/docs/Terminology).
2. Learn how to [Interact with contract](/docu/docs/Interact with contract).
3. Practice in the [Cookbook](/docu/docs/CookBook)