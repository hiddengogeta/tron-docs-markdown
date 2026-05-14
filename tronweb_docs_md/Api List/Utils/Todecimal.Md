

* [API List](/docu/docs/API List/)
* utils
* toDecimal
Version: 6.3.0

On this page

# toDecimal [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/tronweb.ts#L366)

Convert a hexadecimal to a decimal number

### Usage[​](#usage "Direct link to Usage")

```
TronWeb.toDecimal(value);
```

### Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description | Data Type |
| --- | --- | --- |
| value | String-Hex string | String |

### Returns[​](#returns "Direct link to Returns")

Number - The hexadecimal value represented by the passed in string.

### Example[​](#example "Direct link to Example")

```
TronWeb.toDecimal('0x15')  
21
```