

* [API List](/docu/docs/API List/)
* utils
* setAddress
Version: 6.3.0

On this page

# setAddress [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/tronweb.ts#L173)

Sets the address used with all TronWeb API's. Will not sign any transactions.

## Usage[​](#usage "Direct link to Usage")

```
TronWeb.setAddress(address);
```

## Parameter[​](#parameter "Direct link to Parameter")

| Parameter | Description | Data Type |
| --- | --- | --- |
| address | The address to be set | HexString / Base58 String |

## Returns[​](#returns "Direct link to Returns")

No return value

## Example[​](#example "Direct link to Example")

```
//Example 1  
tronWeb.setAddress('TVJ6njG5EpUwJt4N9xjTrqU5za78cgadS2');  
tronWeb.defaultAddress  
{  
  hex: '41d3fd1b6f3f3a86303e2925844456c49876c4561f',  
  base58: 'TVJ6njG5EpUwJt4N9xjTrqU5za78cgadS2'  
}  
  
//Example 2  
tronWeb.setAddress('41d3fd1b6f3f3a86303e2925844456c49876c4561f');  
tronWeb.defaultAddress  
{  
  hex: '41d3fd1b6f3f3a86303e2925844456c49876c4561f',  
  base58: 'TVJ6njG5EpUwJt4N9xjTrqU5za78cgadS2'  
}
```