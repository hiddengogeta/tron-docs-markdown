

* [API List](/docu/docs/API List/)
* utils
* toHex
Version: 6.3.0

On this page

# toHex [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/tronweb.ts#L297)

Convert any value to HEX.

**Note**:
This function does not convert TRON address to Hex. If you wish to specifically convert TRX addresses to HEX, please use TronWeb.address.toHex instead.

### Usage[​](#usage "Direct link to Usage")

```
TronWeb.toHex(value);
```

### Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description | Data Type |
| --- | --- | --- |
| value | The value to be converted to HEX. | String, Number, Object, Array or BigNumber |

### Returns[​](#returns "Direct link to Returns")

String - The hexadecimal value of the passed in value.

### Example[​](#example "Direct link to Example")

```
TronWeb.toHex("abcABC")  
"0x616263414243"  
// If it is an object or array type, it will first be converted to a string using JSON.stringify.  
TronWeb.toHex({ abc: "ABC" })  
"0x7b22616263223a22414243227d"
```