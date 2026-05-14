

* [API List](/docu/docs/API List/)
* utils
* fromMnemonic
Version: 6.3.0

On this page

# fromMnemonic [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/tronweb.ts#L421)

Obtain the address and private key according to the provided mnemonic.

### Usage[​](#usage "Direct link to Usage")

```
TronWeb.fromMnemonic(mnemonic, path, password, wordlist);
```

### Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description | Data Type |
| --- | --- | --- |
| mnemonic | mnemonic. Separate each mnemonic with a space. | String |
| path | BIP44 path, optional parameter. If you want to get an account other than index 0, you need to fill in this parameter, and the complete path is required. | String |
| password | password of the mnemonic, optional | string |
| wordlist | Language type, optional parameter. If the incoming mnemonic is not english(en), you need to fill in the corresponding language object through this parameter, see more in [WordLists](https://docs.ethers.org/v6/api/wordlists/#Wordlists) | Object |

### Returns[​](#returns "Direct link to Returns")

Object - Returns the obtained account information, including mnemonic, public key, and private key. If the entered BIP44 path does not start with m/44'/195', throw an exception - Error: Invalid tron path provided.

### Example[​](#example "Direct link to Example")

Example 1

```
TronWeb.fromMnemonic( 'patch **** **** **** **** **** **** **** **** **** **** denial');  
{  
  "mnemonic": {  
    "phrase": "patch **** **** **** **** **** **** **** **** **** **** denial",  
    "password": "",  
    "wordlist": {  
      "locale": "en"  
    },  
    "entropy": "0xa0cfe524b0ab112c772ff82f51f3581d"  
  },  
  "privateKey": "0x0f91****ffe7",  
  "publicKey": "0x0464****b8f46ce5ee0ffa832492ce1b55a6c90463b2a31a03729b212281f6531558145b634ee0",  
  "address": "TPiD26cc1vptLxwYmw4waHTPCNgqtZ5SCX"  
}
```

Example 2

```
TronWeb.fromMnemonic( 'patch **** **** **** **** **** **** **** **** **** **** denial',"m/44'/195'/0'/0/1")  
{  
  "mnemonic": {  
    "phrase": "patch **** **** **** **** **** **** **** **** **** **** denial",  
    "password": "",  
    "wordlist": {  
      "locale": "en"  
    },  
    "entropy": "0xa0cfe524b0ab112c772ff82f51f3581d"  
  },  
  "privateKey": "0x5f3e****04a0",  
  "publicKey": "0x04df****552f9de3c6a7993e3814b4022a673faa70ad137bcc65857fc40cc0d59218ce28002361",  
  "address": "TXzMaz1QU4jKLctDu2QibrWvPtogtYHdW7"  
}
```