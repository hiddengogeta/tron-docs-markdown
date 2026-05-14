

* [API List](/docu/docs/API List/)
* utils
* toBigNumber
Version: 6.3.0

On this page

# toBigNumber [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/tronweb.ts#L391)

Convert a given number or hexadecimal string to a BigNumber

### Usage[​](#usage "Direct link to Usage")

```
TronWeb.toBigNumber(value);
```

### Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description | Data Type |
| --- | --- | --- |
| value | Number or String in hexadecimal format | String or Number |

### Returns[​](#returns "Direct link to Returns")

BigNumber - BigNumber instance

### Example[​](#example "Direct link to Example")

```
const value = TronWeb.toBigNumber('200000000000000000000001');  
2.0000000000000002e+23  
console.log(value.toString(10))  
200000000000000000000001
```