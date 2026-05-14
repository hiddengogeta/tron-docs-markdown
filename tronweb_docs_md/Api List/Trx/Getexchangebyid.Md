

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getExchangeByID
Version: 6.3.0

On this page

# getExchangeByID [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L1237)

Query Exchange by id

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getExchangeByID(exchange_id);
```

## Parameters[​](#parameters "Direct link to Parameters")

Number - Exchange ID.

## Return[​](#return "Direct link to Return")

Object - Exchange information, see the example below.

## Example[​](#example "Direct link to Example")

```
await tronWeb.trx.getExchangeByID(1);  
{  
  exchange_id: 1,  
  creator_address: '410ca7c49aa44d26aabfe7f594c645cf9f17a4ff70',  
  create_time: 1575754887000,  
  first_token_id: '31303030303033',  
  first_token_balance: 999902,  
  second_token_id: '5f',  
  second_token_balance: 200020000000  
}
```