

* [API List](/docu/docs/API List/)
* utils
* fromSun
Version: 6.3.0

On this page

# fromSun [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/tronweb.ts#L379)

Helper function that will convert a value in SUN to TRX (1 SUN = 0.000001 TRX).
If you want to convert a value in TRX to SUN, `toSun` is available.

### Usage[​](#usage "Direct link to Usage")

```
TronWeb.fromSun(value)
```

### Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description | Data Type |
| --- | --- | --- |
| value | The value in SUN | String |

### Returns[​](#returns "Direct link to Returns")

String - The converted TRX value.

### Example[​](#example "Direct link to Example")

```
TronWeb.fromSun("1000000")  
'1'
```