

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getUnconfirmedBalance
Version: 6.3.0

On this page

# getUnconfirmedBalance [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L351)

Query unconfirmed balance

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getUnconfirmedBalance(address);
```

## Parameters[​](#parameters "Direct link to Parameters")

Address string(in either HexString or Base58 format)

## Return[​](#return "Direct link to Return")

Number - The unconfirmed balance of the address.

## Example[​](#example "Direct link to Example")

```
//Parameter Base58  
await tronWeb.trx.getUnconfirmedBalance('TTSFjEG3Lu9WkHdp4JrWYhbGP6K1REqnGQ');  
29340074430  
           
//Parameter HexString  
await tronWeb.trx.getUnconfirmedBalance('41BF97A54F4B829C4E9253B26024B1829E1A3B1120');  
29340074430
```