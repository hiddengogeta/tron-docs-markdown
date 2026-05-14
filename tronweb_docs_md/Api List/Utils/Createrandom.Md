

* [API List](/docu/docs/API List/)
* utils
* createRandom
Version: 6.3.0

On this page

# createRandom [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/tronweb.ts#L412)

Generate a random mnemonic (total number 12) and using TRON path "m/44'/195'" by default, return the 0th account address and private key.

### Usage[​](#usage "Direct link to Usage")

```
TronWeb.createRandom();
```

### Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description | Data Type |
| --- | --- | --- |
| password | password of the mnemonic, optional | string |
| path | BIP44 path, optional parameter. If you want to get an account other than index 0, you need to fill in this parameter, and the complete path is required. | string |
| wordlist | wordlist of the mnemonic, optional | Object |

### Returns[​](#returns "Direct link to Returns")

Object - Returns randomly created account information, including mnemonic, public key, and private key. If the entered BIP44 path does not start with m/44'/195', throw an exception - Error: Invalid tron path provided.

### Example[​](#example "Direct link to Example")

Get a mnemonic and the 0th account:

```
TronWeb.createRandom();  
{  
    "mnemonic": {  
      "phrase": "draw **** **** **** **** **** **** **** **** **** **** usage",  
      "password": "",  
      "wordlist": {  
        "locale": "en"  
      },  
      "entropy": "0x4277becab26f842c773b40601f9c7af7"  
    },  
    "privateKey": "0x9537****f523",  
    "publicKey": "0x0457****8d30f8aaf4c017649ead9df6c6a71961ce7168f19ca7c1f81d2a42a027d892dae82620",  
    "address": "TEzJCRgq8nGzDtYm2b4QZDfxx5ReeUktrA",  
    "path": "m/44'/195'/0'/0/0"  
  }
```

If you want to get an account with the custom path index, you can provide the path.

```
TronWeb.createRandom('', "m/44'/195'/1'/0/0");  
{  
  "mnemonic": {  
    "phrase": "gain **** **** **** **** **** **** **** **** **** **** chimney",  
    "password": "",  
    "wordlist": {  
      "locale": "en"  
    },  
    "entropy": "0x5ec8cde1156c60b5b384aaa1ccfe8294"  
  },  
  "privateKey": "0x6414****a234",  
  "publicKey": "0x04d7****b1677646d9a805586f440a8c984d6641cb24e97c1e9aed56547f04d62b85859d29cd79",  
  "address": "TYP9p8b3yK4P4i3YjPBVDuwYjLsSUEyuS5",  
  "path": "m/44'/195'/1'/0/0"  
}
```