

* [API List](/docu/docs/API List/)
* utils
* toAscii
Version: 6.3.0

On this page

# toAscii [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/tronweb.ts#L339)

Convert HEX string to ASCII string.

### Usage[​](#usage "Direct link to Usage")

```
TronWeb.toAscii(value);
```

### Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description | Data Type |
| --- | --- | --- |
| value | A hexadecimal string | String |

### Returns[​](#returns "Direct link to Returns")

String - The ASCII value corresponding to the given hexadecimal string.

### Example[​](#example "Direct link to Example")

```
const str = tronWeb.toAscii("0x74726f6e")  
'tron'
```