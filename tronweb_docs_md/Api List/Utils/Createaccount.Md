

* [API List](/docu/docs/API List/)
* utils
* createAccount
Version: 6.3.0

On this page

# createAccount [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/TransactionBuilder/TransactionBuilder.ts#L1582)

Generate a new privatekey + address combination. This account is not activated on the network.

> ### ❗️WARNING[​](#️warning "Direct link to ❗️WARNING")
>
> **This API exposes the private key for the new address. Do not use this in any unsafe environments**.

**Usage**

```
TronWeb.createAccount();
```

**returns**
Object - includes privateKey, publicKey and address in Base58 format and Hex format

**Example**

```
await TronWeb.createAccount();  
{  
    "privateKey": "D9AA****1A7E",  
    "publicKey": "04FFFA899E5EAEB8DB1AA583A96D598DDBAB6DDC0D24B4FD8948E740D7D8E828AC8F177D3937960DE6E2567CECD7E899130DA921EA3B90F0A8FEF24E9D1670A0C1",  
    "address": {  
        "base58": "TXeSp72o5r185cmeGxFDkdCZFdJS1TAyHw",  
        "hex": "41EDC66496A39744FEA631A598CBAE4B7D6A728AA7"  
    }  
}
```