

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* listExchangesPaginated
Version: 6.3.0

On this page

# listExchangesPaginated [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L1263)

Query the list of the exchange pairs by pagination.

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.listExchangesPaginated(Limit, Offset);
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameters | Parameter Description | Data Type |
| --- | --- | --- |
| Limit | The amount of exchanges returned. | Number |
| Offset | The index of the start exchange. | Number |

## Return[​](#return "Direct link to Return")

Array - The list of the exchange pairs.

## Example[​](#example "Direct link to Example")

```
await tronWeb.trx.listExchangesPaginated(2, 0);  
[  
  {  
    exchange_id: 1,  
    creator_address: '41f596e85bfd042744f76880979a133da0728679d9',  
    create_time: 1539673398000,  
    first_token_id: '31303030353634',  
    first_token_balance: 174,  
    second_token_id: '5f',  
    second_token_balance: 85199  
  },  
  {  
    exchange_id: 2,  
    creator_address: '41cd3444bd2d493628b14d6dcec93181e15f94d169',  
    create_time: 1541678472000,  
    first_token_id: '31303031333035',  
    first_token_balance: 128,  
    second_token_id: '5f',  
    second_token_balance: 15102  
  }  
]
```