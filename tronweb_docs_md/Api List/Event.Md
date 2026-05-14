

* [API List](/docu/docs/API List/)
* event
Version: 6.3.0

On this page

# event

[Events](https://developers.tron.network/docs/event) can be fetched with `TronWeb#event` property.

## Standard events query result[​](#standard-events-query-result "Direct link to Standard events query result")

The returned value of API for querying events has a standard format shown as following:

```
{  
    "success":true,  
    "data": [  
      {  
          "block_number": 42054864,  
          "block_timestamp": 1700704884000,  
          "caller_contract_address": "TPYwAC9Y4uUcT2QH3WPPjqxzJSJWymMoMS",  
          "contract_address": "TPYwAC9Y4uUcT2QH3WPPjqxzJSJWymMoMS","event_index": 1,  
          "event_name": "Transfer",  
          "result": {  
             "0": "0x65fa68800fff5a10346d1a3aa1fb2ce92f2e2971",  
             "1": "0xbbd6d9c36cf31f73b01ad2415b12d9d2bda7fb08",  
             "2": "27000000","from":"0x65fa68800fff5a10346d1a3aa1fb2ce92f2e2971",  
             "to": "0xbbd6d9c36cf31f73b01ad2415b12d9d2bda7fb08","value": "27000000"  
          },  
          "result_type": {  
            "from":"address",  
            "to":"address",  
            "value":"uint256"  
          },  
          "event": "Transfer(address indexed from, address indexed to, uint256 value)",  
          "transaction_id": "9c9e4776de1ee889aad48be360262e3dd6d1a1e3d4e0d7c72dc50075260846df"  
        }  
    ],  
    "meta": {  
        "at":1700720666204,  
        "page_size": 1  
    }  
}
```