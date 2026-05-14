

* [API List](/docu/docs/API List/)
* utils
* isAddress
Version: 6.3.0

On this page

# isAddress [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/tronweb.ts#L400)

Helper function that will check if a given address is valid.

### Usage[​](#usage "Direct link to Usage")

```
TronWeb.isAddress(address)
```

### Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description | Data Type |
| --- | --- | --- |
| address | The address to be checked | Base58 and Hex format String |

### Returns[​](#returns "Direct link to Returns")

Boolean

### Example[​](#example "Direct link to Example")

```
TronWeb.isAddress("414fa1f834a47f621957ec2ae7d445da9b3be0bee4")  
true  
TronWeb.isAddress("THEGR4Aor5pCDVktbbbwgHAE6PQWRfejBf")  
true
```