

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* signTypedData
Version: 6.3.0

On this page

# signTypedData [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L714)

Sign the typed data value with types data structure for domain using the [TIP-712 specification](https://github.com/tronprotocol/tips/issues/443).

**Note:**
The method was previously named `trx._signTypedData`. Since it has been stable and widely used for a long time, we decided to formalize it by removing the leading underscore. The original underscored method will remain available for backward compatibility.

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.signTypedData(domain, types, value, privateKey);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameters | Parameter Description | Data Type |
| --- | --- | --- |
| domain | Domain separator. This field is to prevent collisions with other transactions on the network or messages with the same structure. | JSON |
| types | Type definition of Typed Data | JSON |
| value | The value of Typed Data | JSON |
| privateKey | Optional. The private key used for signing. If omitted, the private key passed in when constructing tronweb object will be used. | String |

## Return[​](#return "Direct link to Return")

String - Signature of the typed data

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
  
const signature = await tronWeb.trx.signTypedData(domain, types, value);  
0x72cc671f38be492773e2cd44c64535ab8825d8ab7b0e580ee45731d00fc0aa5a385bf816505e6c53864bc8539677f7c6a6ece907c94e02d473d392e364cfd5691c
```