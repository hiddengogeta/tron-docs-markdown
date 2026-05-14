

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getNowWitnessList
Version: 6.3.0

On this page

# getNowWitnessList [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L1526)

Query the real-time vote count of witnesses

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getNowWitnessList()
```

## Parameters[​](#parameters "Direct link to Parameters")

| Parameters | Parameter Description | Data Type |
| --- | --- | --- |
| options.offset | paginated offset, defaults to 0 | number |
| options.limit | paginated page size, defaults to 10 | number |
| options.visible | true means returning base58 address, false means returning hex address, defaults to false | boolean |
| options.confirmed | whether to query the solidity node, defaults to true | boolean |

## Return[​](#return "Direct link to Return")

Object Array - The list of the witnesses with vote count, see the example below.

## Example[​](#example "Direct link to Example")

```
//Parameter Base58  
await tronWeb.trx.getNowWitnessList();  
[  
  {  
    address: '41608e7e1c6f6dcc1679ea512503e41ca0254e0948',  
    voteCount: 5405936847,  
    url: 'http://sr-8.com',  
    totalProduced: 1802839,  
    totalMissed: 456,  
    latestBlockNum: 64608831,  
    latestSlotNum: 590095017,  
    isJobs: true  
  },  
  {  
    address: '4139e58c94e9877bbe5556ee7acc6d6d428a3929e9',  
    voteCount: 2322244615,  
    url: 'http://sr-27.com',  
    totalProduced: 1808914,  
    totalMissed: 619,  
    latestBlockNum: 64608832,  
    latestSlotNum: 590095018,  
    isJobs: true  
  },  
  {  
    address: '41a234e405a2c6fd67cdd4d0ea2f6188f65534c8b1',  
    voteCount: 2321262761,  
    url: 'http://sr-13.com',  
    totalProduced: 1810285,  
    totalMissed: 178,  
    latestBlockNum: 64608833,  
    latestSlotNum: 590095019,  
    isJobs: true  
  },  
  {  
    address: '416c28585d13602ae332c5de6f73f8e50f697a196b',  
    voteCount: 2320942993,  
    url: 'http://sr-9.com',  
    totalProduced: 1804770,  
    totalMissed: 208,  
    latestBlockNum: 64608834,  
    latestSlotNum: 590095020,  
    isJobs: true  
  },  
  {  
    address: '41010f8928947769a5cd54b1f4a5c9b7d3e497994b',  
    voteCount: 2320891065,  
    url: 'http://sr-6.com',  
    totalProduced: 1811875,  
    totalMissed: 464,  
    latestBlockNum: 64608835,  
    latestSlotNum: 590095021,  
    isJobs: true  
  },  
  {  
    address: '4196409f85790883057edf03286d08e4aa608c0d0a',  
    voteCount: 2320890203,  
    url: 'http://sr-26.com',  
    totalProduced: 1808832,  
    totalMissed: 329,  
    latestBlockNum: 64608836,  
    latestSlotNum: 590095022,  
    isJobs: true  
  },  
  {  
    address: '41e7860196ad5b5718c1d6326babab039b70b8c1cd',  
    voteCount: 2320625793,  
    url: 'http://sr-25.com',  
    totalProduced: 1808378,  
    totalMissed: 318,  
    latestBlockNum: 64608837,  
    latestSlotNum: 590095023,  
    isJobs: true  
  },  
  {  
    address: '416606973497a56dcfcedb684e60a2386f2ae39db5',  
    voteCount: 2320588143,  
    url: 'http://sr-4.com',  
    totalProduced: 1802817,  
    totalMissed: 170,  
    latestBlockNum: 64608838,  
    latestSlotNum: 590095024,  
    isJobs: true  
  },  
  {  
    address: '4150d3765e4e670727ebac9d5b598f74b75a3d54a7',  
    voteCount: 2320491649,  
    url: 'http://sr-7.com',  
    totalProduced: 1808968,  
    totalMissed: 183,  
    latestBlockNum: 64608839,  
    latestSlotNum: 590095025,  
    isJobs: true  
  },  
  {  
    address: '411d298407f3b8792ee14d91d6924185846d88dd97',  
    voteCount: 2320483065,  
    url: 'http://sr-16.com',  
    totalProduced: 1809442,  
    totalMissed: 248,  
    latestBlockNum: 64608840,  
    latestSlotNum: 590095026,  
    isJobs: true  
  }  
]
```