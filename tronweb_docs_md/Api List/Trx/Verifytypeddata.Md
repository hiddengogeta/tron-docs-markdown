

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* verifyTypedData
Version: 6.3.0

On this page

# verifyTypedData [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L599)

Verify the signature of the typed data value with types data structure for domain using the [TIP-712 specification](https://github.com/tronprotocol/tips/issues/443).

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.verifyTypedData(domain, types, value, signature, address);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameters | Parameter Description | Data Type |
| --- | --- | --- |
| domain | Domain separator. This field is to prevent collisions with other transactions on the network or messages with the same structure. | JSON |
| types | Type definition of Typed Data | JSON |
| value | The value of Typed Data | JSON |
| signature | The signature to be verified | string |
| address | The expected address that signed the data. Default is `tronWeb.defaultAddress.base58`. | string |

## Return[​](#return "Direct link to Return")

bool - true if verify successfully, else return error Signature does not match.

## Example[​](#example "Direct link to Example")

```
// All properties on a domain are optional  
const domain = {  
  name: 'TRON Mail',  
  version: '1',  
  chainId: '0x2b6653dc',  
  verifyingContract: 'TUe6BwpA7sVTDKaJQoia7FWZpC9sK8WM2t'  
};  
  
// The named list of all type definitions  
const types = {  
  Person: [  
    { name: 'name', type: 'string' },  
    { name: 'wallet', type: 'address' }  
  ],  
  Mail: [  
    { name: 'from', type: 'Person' },  
    { name: 'to', type: 'Person' },  
    { name: 'contents', type: 'string' }  
  ]  
};  
  
// The data to sign  
const value = {  
  from: {  
    name: 'Cow',  
    wallet: 'TUg28KYvCXWW81EqMUeZvCZmZw2BChk1HQ'  
  },  
  to: {  
    name: 'Bob',  
    wallet: 'TT5rFsXYCrnzdE2q1WdR9F2SuVY59A4hoM'  
  },  
  contents: 'Hello, Bob!'  
};  
  
let signature = await tronWeb.trx._signTypedData(domain, types, value);  
  
const tail = signature.substring(128, 130);  
if (tail == '01') {  
  signature = signature.substring(0,128)+'1c';  
} else if(tail == '00') {  
  signature = signature.substring(0,128)+'1b';  
}  
  
const result = await tronWeb.trx.verifyTypedData(domain, types, value, signature);  
// verification result: true
```