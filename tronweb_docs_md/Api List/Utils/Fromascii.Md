

* [API List](/docu/docs/API List/)
* utils
* fromAscii
Version: 6.3.0

On this page

# fromAscii [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/tronweb.ts#L358)

Helper function that will convert ASCII to HEX

### Usage[​](#usage "Direct link to Usage")

```
TronWeb.fromUtf8(value);
```

### Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description | Data Type |
| --- | --- | --- |
| value | The string to be converted | string |

### Returns[​](#returns "Direct link to Returns")

String - The converted hex string.

### Example[​](#example "Direct link to Example")

```
TronWeb.fromUtf8("test");  
'0x74657374'
```