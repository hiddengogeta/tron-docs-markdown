

* [API List](/docu/docs/API List/)
* utils
* fromUtf8
Version: 6.3.0

On this page

# fromUtf8 [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/tronweb.ts#L331)

Helper function that will convert UTF8 to HEX.
And `toUtf8` function is also available.

### Usage[​](#usage "Direct link to Usage")

```
TronWeb.fromUtf8(value)
```

### Parameter[​](#parameter "Direct link to Parameter")

| Parameter | Description | Data Type |
| --- | --- | --- |
| value | The value to be converted | String |

### Returns[​](#returns "Direct link to Returns")

String - The converted HEX value.

### Example[​](#example "Direct link to Example")

```
TronWeb.fromUtf8("test")  
"0x74657374"
```