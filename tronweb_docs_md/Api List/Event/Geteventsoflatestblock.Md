

* [API List](/docu/docs/API List/)
* [event](/docu/docs/API List/event/)
* getEventsOfLatestBlock()
Version: 6.3.0

On this page

# getEventsOfLatestBlock() [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/event.ts#L162)

Query events for current block.

## Usage[​](#usage "Direct link to Usage")

```
const events = await tronWeb.event.getEventsOfLatestBlock( options );
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameters | Parameter Description | Type |
| --- | --- | --- |
| options | Optional. | See the following. |

The type of `options`:

```
interface GetEventResultOptions {  
    /**  
     * Only query confirmed transaction events.  
     * Default is false.  
     */  
    only_confirmed?: boolean;  
}
```

## Return[​](#return "Direct link to Return")

[Standard events query result](/docu/docs/API List/event/#standard-events-query-result)

## Example[​](#example "Direct link to Example")

```
const events = await tronWeb.event.getEventsOfLatestBlock();  
console.log(events);  
{  
    "data": [  
        {  
            "block_number": 42062172,  
            "block_timestamp": 1691146032000,  
            "caller_contract_address": "TRz7J6dD2QWxBoumfYt4b3FaiRG23pXfop",  
            "contract_address": "TRz7J6dD2QWxBoumfYt4b3FaiRG23pXfop",  
            "event_index": 0,  
            "event_name": "Transfer",  
            "result": {  
                "0": "0x573708726db88a32c1b9c828fef508577cfb8483",  
                "1": "0x7b550beadccf4c92b8b4772a993e34f5afaa6eb6",  
                "2": "5000000000000000000",  
                "from": "0x573708726db88a32c1b9c828fef508577cfb8483",  
                "to": "0x7b550beadccf4c92b8b4772a993e34f5afaa6eb6",  
                "value": "5000000000000000000"  
            },  
            "result_type": {  
                "from": "address",  
                "to": "address",  
                "value": "uint256"  
            },  
            "event": "Transfer(address indexed from, address indexed to, uint256 value)",  
            "transaction_id": "028f0565c1fefc6790da474c32fcfe42769d4317e20fdfad521fd3007684d6d3"  
        }  
    ],  
    "success": true,  
    "meta": {  
        "at": 1700727510461,  
        "page_size": 1  
    }  
}
```