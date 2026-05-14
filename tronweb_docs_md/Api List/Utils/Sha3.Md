

* [API List](/docu/docs/API List/)
* utils
* sha3
Version: 6.3.0

On this page

# sha3 [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/tronweb.ts#L292)

Helper function that will sha3 any value using keccak256.
Internally it will use `Buffer.from(input, 'utf8')` to process the input first. If you want to hash a hexString or ByteArray, use `TronWeb.utils.ethersUtils.keccak256(input)`.

### Usage[​](#usage "Direct link to Usage")

```
TronWeb.sha3(value);
```

### Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description | Data Type |
| --- | --- | --- |
| string | The string that needs to be hashed using Keccak-256 SHA3 algorithm. | String |
| prefix | the result includes `0x` prefix if set as true | Boolean |

### Returns[​](#returns "Direct link to Returns")

String - The result hashed using the Keccak-256 SHA3 algorithm.

### Example[​](#example "Direct link to Example")

```
var hash = TronWeb.sha3("some string to be hashed");  
console.log(hash)  
'0xc4b9bbe7eb8797cf2818085dbcd6ea6662b3261c28810c318e079c8d0c691da6'  
var hashOfHash = TronWeb.sha3(hash, false)  
'c4b9bbe7eb8797cf2818085dbcd6ea6662b3261c28810c318e079c8d0c691da6'
```