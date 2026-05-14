

* [API List](/docu/docs/API List/)
* utils
* toUtf8
Version: 6.3.0

On this page

# toUtf8 [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/tronweb.ts#L321)

Helper function that will convert HEX to UTF8.

### Usage[​](#usage "Direct link to Usage")

```
TronWeb.toUtf8(value);
```

### Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description | Data Type |
| --- | --- | --- |
| value | A hex string | String |

### Return[​](#return "Direct link to Return")

String - The UTF8 value of the passed in hex string.

### Example[​](#example "Direct link to Example")

```
TronWeb.toUtf8("0x74657374");  
'test'
```