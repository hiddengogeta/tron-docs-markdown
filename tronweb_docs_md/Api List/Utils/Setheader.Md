

* [API List](/docu/docs/API List/)
* utils
* setHeader
Version: 6.3.0

On this page

# setHeader [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/tronweb.ts#L221)

Set the API Key parameters of all TronWeb API requests

**Note**:
It needs to be set only when using the Trongrid service. For API Key parameter application and use, please refer to [document](https://developers.tron.network/reference#api-key).

### Usage[​](#usage "Direct link to Usage")

```
TronWeb.setHeader({"TRON-PRO-API-KEY": 'your api key'});
```

### Parameter[​](#parameter "Direct link to Parameter")

| Parameter | Description | Data Type |
| --- | --- | --- |
| Options | http request header | Object |

### Returns[​](#returns "Direct link to Returns")

No return value

### Example[​](#example "Direct link to Example")

```
const tronWeb = new TronWeb({fullHost: 'fullHost'});  
tronWeb.setHeader({ "TRON-PRO-API-KEY": 'xxx' });
```