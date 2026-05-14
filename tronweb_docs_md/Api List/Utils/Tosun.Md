

* [API List](/docu/docs/API List/)
* utils
* toSun
Version: 6.3.0

On this page

# toSun [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/tronweb.ts#L385)

Helper function that will convert a value in TRX to SUN. (1 SUN = 0.000001 TRX).

### Usage[​](#usage "Direct link to Usage")

```
TronWeb.toSun(value);
```

### Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description | Data Type |
| --- | --- | --- |
| value | A number value | Number |

### Return[​](#return "Direct link to Return")

String - The value in SUN.

### Example[​](#example "Direct link to Example")

```
TronWeb.toSun(10)  
"10000000"
```