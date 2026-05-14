

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getTokenByID
Version: 6.3.0

On this page

# getTokenByID [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L1395)

Query TRC10 token information by the token id.

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getTokenByID(tokenID);
```

## Parameters[​](#parameters "Direct link to Parameters")

String or Number - Token ID.

## Return[​](#return "Direct link to Return")

Object - Token information, see examples below.

## Example[​](#example "Direct link to Example")

```
//example 1  
await tronWeb.trx.getTokenByID(1002000);  
{  
  owner_address: '4137fa1a56eb8c503624701d776d95f6dae1d9f0d6',  
  name: 'BitTorrent',  
  abbr: 'BTT',  
  total_supply: 990000000000000000,  
  trx_num: 1,  
  precision: 6,  
  num: 1,  
  start_time: 1548000000000,  
  end_time: 1548000001000,  
  description: 'Official Token of BitTorrent Protocol',  
  url: 'www.bittorrent.com',  
  id: '1002000'  
}  
  
//example 2  
tronWeb.trx.getTokenByID('1002000').then(result => {console.log(result)});  
{  
  owner_address: '4137fa1a56eb8c503624701d776d95f6dae1d9f0d6',  
  name: 'BitTorrent',  
  abbr: 'BTT',  
  total_supply: 990000000000000000,  
  trx_num: 1,  
  precision: 6,  
  num: 1,  
  start_time: 1548000000000,  
  end_time: 1548000001000,  
  description: 'Official Token of BitTorrent Protocol',  
  url: 'www.bittorrent.com',  
  id: '1002000'  
}
```