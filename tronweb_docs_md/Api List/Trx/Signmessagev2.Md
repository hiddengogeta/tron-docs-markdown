

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* signMessageV2
Version: 6.3.0

On this page

# signMessageV2 [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L688)

Sign a plaintext string

*The sign interface is to sign the Hex format string, and the signature verification uses verifyMessage interface. But signMessageV2 can sign a plaintext string. Please use the verifyMessageV2 interface for signature verification.*

**Note**:

* If message is a string, it is treated as a string and converted to its representation in UTF8 bytes.
* If and only if a message is a Bytes Array will it be treated as binary data.
* For example, signMessageV2 will take the string "0x1234" as a 6 characters string not the hex string.
* If you only want to sign a hash, you should convert your hash string to an Bytes Array first using `TronWeb.utils.ethersUtils.arrayify` utility function.

## Usage[​](#usage "Direct link to Usage")

```
// Call directly，privatekey is needed in this way  
tronWeb.trx.signMessageV2(message, privateKey);  
  
// Called via the instantiated tronWeb object  
tronWeb.trx.signMessageV2(message, privateKey);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameters | Parameter Description | Data Type |
| --- | --- | --- |
| message | Message to be signed | ByteArray / String |
| privateKey | The private key used for signing. Optional. The default value is the private key passed in when constructing tronweb object. | String |

## Return[​](#return "Direct link to Return")

String - the signature.

## Example[​](#example "Direct link to Example")

```
var message = 'hello world';  
var signature = tronWeb.trx.signMessageV2(message);  
console.log(signature);  
0x1d1b0779da653630d29fc4f1ea1e5a109a30d52e21e7657fa896d2fccc3b430b14089377e13b6ed35ef371a1c91873773d568219d1100fa8595e5f2eec39e3e41c
```