

* Sign and Verify Message
Version: 6.3.0

On this page

# Sign and Verify Message

## signMessageV2[​](#signmessagev2 "Direct link to signMessageV2")

This returns a Promise which resolves to the Raw Signature of message.

A signed message is prefixed with "\x19TRON Signed Message:\n" and the length of the message, using the [hashMessage](https://docs.ethers.org/v5/api/utils/hashing/#utils-hashMessage) method in ethers.js, so that it is [TIP-191](https://github.com/tronprotocol/tips/blob/master/tip-191.md) compliant.

**Note**:
`tronWeb.trx.signMessage` has been deprecated, as it is prefixed with "\x19TRON Signed Message:\n32" which customizes the message length and only accepts hex string. Consequently, we add signMessageV2 function to support plaintext string signature. It is always highly recommended that you use tronWeb.trx.signMessageV2 above the TronWeb version v4.4.0.

In signMessageV2 function, we should note that:

* If message is a string (string), it will be converted to a Uint8Array (byte array).
* If message is a regular array of numbers, it will be converted to a Uint8Array.
* If message is already a Uint8Array, no conversion is needed and it will be used directly.

  For example, signMessageV2 will take the string "0x1234" as a 6 characters string not the hex string.
* If you only want to sign a hash, you should convert your hash string to an Bytes Array first using `TronWeb.utils.ethersUtils.arrayify` utility function.

### Usage[​](#usage "Direct link to Usage")

If you keep the private key, you can use as follows:

```
const { TronWeb, Trx } = require('tronweb');  
// way1: initiate a tronWeb instance and pass the private key  
const tronWeb = new TronWeb({fullHost: 'xxx', privateKey: 'privateKey'});  
const signature = await tronWeb.trx.signMessageV2('message')  
// way2: just call by Trx Class without initiating tronWeb  
const signature = await Trx.signMessageV2('message', 'privateKey');
```

If the private key is in wallets such as TronLink extension, TronLink wallet APP, you can use the exported tronWeb instance by wallets.

```
const signature = await tronWeb.trx.signMessageV2('message');
```

This will popup a signature confirmation dialog to request the confirmation of users.

## verifyMessageV2[​](#verifymessagev2 "Direct link to verifyMessageV2")

`verifyMessageV2` function is corresponding to `signMessageV2`. It will return the recovering address in Base58 format. Users should check if the recovering address is the signed account.

*Note*\*:
`tronWeb.trx.verifyMessage` will be deprecated soon, is corresponding to `tronWeb.trx.signMessage`. And if you get a signature with v2, you can not use `tronWeb.trx.verifyMessage` to verify it as they are not incompatible. It is always highly recommended that you use tronWeb.trx.signMessageV2 to sign and tronWeb.trx.verifyMessageV2 to verify the signature.

### Usage[​](#usage-1 "Direct link to Usage")

This is only a utility function, you can use like this:

```
const base58Address = await tronWeb.trx.verifyMessageV2(message, signature);
```

or

```
const base58Address = await tronWeb.trx.verifyMessageV2(message, signature);
```