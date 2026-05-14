

* [API List](/docu/docs/API List/)
* utils
* BigNumber
Version: 6.3.0

On this page

# BigNumber

Convert a given number or hexadecimal string to a BigNumber.

### Usage[​](#usage "Direct link to Usage")

```
new BigNumber(value);
```

### Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description | Data Type |
| --- | --- | --- |
| value | The value to be converted | Any |

### Returns[​](#returns "Direct link to Returns")

BigNumber - BigNumber instance

Example

```
import { BigNumber } from 'tronweb';  
const value = new BigNumber('200000000000000000000001');
```

**Note**:

* TronWeb v4.0.0 updated bignumber.js to v9.0.1, which is a breaking change.
* If you get a result after triggerConstantContract or call method, do not use TronWeb.BigNumber(result) which will get null. Thus：
* TronWeb v4.0.0 and later：tronWeb.toBigNumber(result) or tronWeb.BigNumber(result.\_hex)
* TronWeb version before v4.0.0：tronWeb.BigNumber(result)