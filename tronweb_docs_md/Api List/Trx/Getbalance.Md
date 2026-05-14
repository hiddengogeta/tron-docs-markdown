

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getBalance
Version: 6.3.0

On this page

# getBalance [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L326)

Get the account's balance of TRX, and display the TRX balance in SUN

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getBalance(address);
```

## Parameters[​](#parameters "Direct link to Parameters")

Address string(in either HexString or Base58 format)

## Return[​](#return "Direct link to Return")

Number - The account's TRX balance in SUN.

## Example[​](#example "Direct link to Example")

```
//Parameter Base58  
await tronWeb.trx.getBalance('TTSFjEG3Lu9WkHdp4JrWYhbGP6K1REqnGQ');  
29887074430  
           
//Parameter HexString  
await tronWeb.trx.getBalance('41BF97A54F4B829C4E9253B26024B1829E1A3B1120');  
29340074430
```