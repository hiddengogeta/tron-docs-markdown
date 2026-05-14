

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getUnconfirmedReward
Version: 6.3.0

On this page

# getUnconfirmedReward [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L1424)

Query unconfirmed reward

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getUnconfirmedReward(address)
```

## Parameters[​](#parameters "Direct link to Parameters")

Address string(in either HexString or Base58 format)

## Return[​](#return "Direct link to Return")

Number - The unconfirmed reward of the address.

## Example[​](#example "Direct link to Example")

```
//Parameter Base58  
await tronWeb.trx.getUnconfirmedReward("TTSFjEG3Lu9WkHdp4JrWYhbGP6K1REqnGQ");  
0  
  
//Parameter HexString  
await tronWeb.trx.getUnconfirmedReward("41BF97A54F4B829C4E9253B26024B1829E1A3B1120");  
0
```