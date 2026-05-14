

* [API List](/docu/docs/API List/)
* utils
* getEventResult
Version: 6.3.0

On this page

# getEventResult [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/tronweb.ts#L256)

Returns all events matching the filters.

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.getEventResult(contractAddress, options)
```

## Parameter[​](#parameter "Direct link to Parameter")

contractAddress - String : Contract address.

options - Object : (optional) The filter conditions, including the following fields:

| Parameter | Description | Data Type |
| --- | --- | --- |
| eventName | Name of the event to filter by. | String |
| blockNumber | Specific block number to query. | Number |
| limit | Maximum number returned. | Number |
| fingerprint | When the data volume of the query result is large, the returned result of one query will not contain all the data, and it takes multiple queries to obtain the complete data. Therefore, the fingerprint field will appear in the last piece of data in the returned result. After specifying this field as the content of the fingerprint in the result of the previous query in the next query, the query will return subsequent data. If there is no such field in the last data of the query result, it means that there is no more data. | String |
| onlyConfirmed | If set to true, only returns confirmed transactions. | Boolean |
| onlyUnconfirmed | If set to true, only returns unconfirmed transactions. | Boolean |
| orderBy | 'block\_timestamp,desc' or 'block\_timestamp,asc' | string |
| minBlockTimestamp | Specifies the starting timestamp of the query, in milliseconds, default value is the current time. | number |
| maxBlockTimestamp | Specifies the ending timestamp of the query, in milliseconds. | number |

## Return[​](#return "Direct link to Return")

Object Array - The event list.

## Example[​](#example "Direct link to Example")

```
tronWeb.getEventResult("TUPz3wD356e3iV337s4cnjQS2weUdhX5ci",{eventName:"RNGIterated",limit:2}).then(result => {console.log(result)})  
[  
  {  
    block: 615212,  
    timestamp: 1577440164000,  
    contract: 'TUPz3wD356e3iV337s4cnjQS2weUdhX5ci',  
    name: 'RNGIterated',  
    transaction: 'a8929bcfb8a7337d6c8c5850b5ed63cdd09ff17bbde46dad07b2c1f20c427e89',  
    result: {  
      index: '41796',  
      rng: '3f7bf1c50a01cbcb980360effa904e0e11880af8daeeb2f8da686b7b3e5d9a50',  
      timestamp: '1577440164'  
    },  
    resourceNode: 'solidityNode'  
  },  
  {  
    block: 615205,  
    timestamp: 1577440143000,  
    contract: 'TUPz3wD356e3iV337s4cnjQS2weUdhX5ci',  
    name: 'RNGIterated',  
    transaction: 'fa9e91282de9eb462efabea838c2d0465602312a87ded06524c87d8afafd743d',  
    result: {  
      index: '41795',  
      rng: 'bf190910aa5293ab12f644eb723b5460340e3ec11ac073124147e5fc92ca44d2',  
      timestamp: '1577440143'  
    },  
    resourceNode: 'solidityNode',  
    fingerprint: '2TBTeOqO3x2kJDyxT'  
  }  
]
```