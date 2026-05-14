

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* verifyMessageV2
Version: 6.3.0

On this page

# verifyMessageV2 [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L591)

Verify the signature on a plaintext string

*The plaintext string can be signed through the signMessageV2 interface, and then the signature can be verified through this interface.*

## Usage[​](#usage "Direct link to Usage")

```
// Call directly  
tronWeb.trx.verifyMessageV2(message, signature)  
  
// Called via the instantiated tronWeb object  
tronWeb.trx.verifyMessageV2(message, signature)
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameters | Parameter Description | Data Type |
| --- | --- | --- |
| message | the signed string | String |
| signature | Signature to be verified | String |

## Return[​](#return "Direct link to Return")

String - the signed address in base58 format

## Example[​](#example "Direct link to Example")

```
var str = "helloworld";   
var signature = tronWeb.trx.signMessageV2(str);  
var base58Address = await tronWeb.trx.verifyMessageV2(str, signature);
```