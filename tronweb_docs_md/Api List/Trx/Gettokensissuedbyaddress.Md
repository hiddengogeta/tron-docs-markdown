

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getTokensIssuedByAddress
Version: 6.3.0

On this page

# getTokensIssuedByAddress [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L376)

Query the TRC10 token issue information of an account.

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getTokensIssuedByAddress(address);
```

## Parameters[​](#parameters "Direct link to Parameters")

Address string(in either HexString or Base58 format)

## Return[​](#return "Direct link to Return")

Object - The TRC10 token issue information of the account, see examples below.

## Example[​](#example "Direct link to Example")

```
//example 1  
await tronWeb.trx.getTokensIssuedByAddress("TF5Bn4cJCT6GVeUgyCN4rBhDg42KBrpAjg");  
{  
  BitTorrent: {  
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
}  
  
//example 2  
await tronWeb.trx.getTokensIssuedByAddress("4137fa1a56eb8c503624701d776d95f6dae1d9f0d6");  
{  
  BitTorrent: {  
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
}
```