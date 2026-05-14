

* [API List](/docu/docs/API List/)
* utils
* fromDecimal
Version: 6.3.0

On this page

# fromDecimal [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/tronweb.ts#L371)

Converts a number, or a string of numbers, into a hexadecimal string.

### Usage[​](#usage "Direct link to Usage")

```
TronWeb.fromDecimal(number);
```

### Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description | Data Type |
| --- | --- | --- |
| number | String or Number | Hexadecimal string / Number |

### Returns[​](#returns "Direct link to Returns")

String - The converted hex string.

### Example[​](#example "Direct link to Example")

```
TronWeb.fromDecimal("12345678");  
'0xbc614e'
```