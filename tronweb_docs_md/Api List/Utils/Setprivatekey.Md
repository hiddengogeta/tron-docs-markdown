

* [API List](/docu/docs/API List/)
* utils
* setPrivateKey
Version: 6.3.0

On this page

# setPrivateKey [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/tronweb.ts#L163)

Set a private key used with the TronWeb instance, used for obtaining the address, signing transactions, and getting balances.

> ❗️WARNING :
>
> Do not use this with any web/user facing TronWeb instances. This will leak the private key.

## Usage[​](#usage "Direct link to Usage")

```
TronWeb.setPrivateKey(private key);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description | Data Type |
| --- | --- | --- |
| private key | The private key to be set | String |

## Returns[​](#returns "Direct link to Returns")

No return value

## Example[​](#example "Direct link to Example")

```
tronWeb.setPrivateKey('AD71****7509');  
tronWeb.defaultPrivateKey  
'AD71****7509'
```