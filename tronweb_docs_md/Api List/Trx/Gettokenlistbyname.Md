

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getTokenListByName
Version: 6.3.0

On this page

# getTokenListByName [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L1369)

Query the list of TRC10 tokens by name.

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getTokenListByName(tokenName);
```

## Parameters[​](#parameters "Direct link to Parameters")

String - Token name.

## Return[​](#return "Direct link to Return")

Object array - The list of TRC10 token with same name, see the example below.

## Example[​](#example "Direct link to Example")

```
await tronWeb.trx.getTokenListByName("BTT");  
[  
  {  
    owner_address: '4113189bb13f1ec4f45c88526bd05482f482c06a11',  
    name: 'BTT',  
    abbr: 'BTT',  
    total_supply: 100000000000000,  
    frozen_supply: [ [Object] ],  
    trx_num: 1000000,  
    num: 1,  
    start_time: 1547456580180,  
    end_time: 1547715780180,  
    description: 'BitTorrent',  
    url: 'BitTorrent',  
    id: '1001927'  
  },  
  {  
    owner_address: '41f4204dec09b1899444d851dd54fbfc21397e20ab',  
    name: 'BTT',  
    abbr: 'BTT',  
    total_supply: 999000000000000000,  
    frozen_supply: [ [Object] ],  
    trx_num: 1000000,  
    precision: 6,  
    num: 1000000,  
    start_time: 1549987200000,  
    end_time: 1550073600000,  
    description: 'BTT Candy',  
    url: 'www.bittorrent.com',  
    id: '1002083'  
  },  
  {  
    owner_address: '41d2bcae5375057098726f8b8d839c8037499d38c5',  
    name: 'BTT',  
    abbr: 'BTT',  
    total_supply: 1000000000000000000,  
    frozen_supply: [ [Object] ],  
    trx_num: 1000000,  
    precision: 6,  
    num: 244000000,  
    start_time: 1555948800000,  
    end_time: 1577376000000,  
    description: 'BTT',  
    url: 'COM',  
    id: '1002334'  
  }  
]
```