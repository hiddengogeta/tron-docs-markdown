

* [API List](/docu/docs/API List/)
* [event](/docu/docs/API List/event/)
* getEventsByContractAddress()
Version: 6.3.0

On this page

# getEventsByContractAddress() [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/event.ts#L30)

Query events by contract address.

## Usage[​](#usage "Direct link to Usage")

```
const events = await tronWeb.event.getEventsByContractAddress(  
    contractAddress,  
    options  
  );
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameters | Parameter Description | Type |
| --- | --- | --- |
| contractAddress | contract address (base58 or hex) | String |
| options | Optional. | See the following. |

The type of `options`:

```
interface GetEventResultOptions {  
    /**  
     * Name of the event to filter by.  
     */  
    eventName?: string;  
    /**  
     * Specific block number to query.  
     */  
    blockNumber?: number;  
    /**  
     * Maximum number returned.  
     */  
    limit?: number;  
    /**  
     * When the data volume of the query result is large, the returned result of one query will not contain all the data, and it takes multiple queries to obtain the complete data. Therefore, the fingerprint field will appear in the last piece of data in the returned result. After specifying this field as the content of the fingerprint in the result of the previous query in the next query, the query will return subsequent data. If there is no such field in the last data of the query result, it means that there is no more data.  
     */  
    fingerprint?: string;  
    /**  
     * If set to true, only returns confirmed transactions.  
     */  
    onlyConfirmed?: boolean;  
    /**  
     * If set to true, only returns unconfirmed transactions.  
     */  
    onlyUnconfirmed?: boolean;  
    /**  
     * Specify the query order, whether to query forward or backward from the sinceTimestamp.  
     * The value can be 'block_timestamp,desc' for time sequence or 'block_timestamp,asc' for the reverse.  
     * Default is 'block_timestamp,desc'.  
     */  
    orderBy?: 'block_timestamp,desc' | 'block_timestamp,asc';  
    /**  
     * Specifies the starting timestamp of the query, in milliseconds, default value is the current time.  
     */  
    minBlockTimestamp?: number;  
    /**  
     * Specifies the ending timestamp of the query, in milliseconds.  
     */  
    maxBlockTimestamp?: number;  
}
```

## Return[​](#return "Direct link to Return")

[Standard events query result](/docu/docs/API List/event/#standard-events-query-result)

## Example[​](#example "Direct link to Example")

```
const events = await tronWeb.event.getEventsByContractAddress(  
  'TPYwAC9Y4uUcT2QH3WPPjqxzJSJWymMoMS',  
  {  
    eventName: 'Transfer'  
  }  
);  
console.log(events);  
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