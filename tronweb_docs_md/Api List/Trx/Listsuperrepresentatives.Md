

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* listSuperRepresentatives
Version: 6.3.0

On this page

# listSuperRepresentatives [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L465)

Query the list of the witnesses.

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.listSuperRepresentatives();
```

## Return[​](#return "Direct link to Return")

Object Array - The list of the witnesses, see the example below.

## Example[​](#example "Direct link to Example")

```
await tronWeb.trx.listSuperRepresentatives();  
[  
  {  
    address: '417bdd2efb4401c50b6ad255e6428ba688e0b83f81',  
    voteCount: 280515210,  
    url: 'https://minergate.com',  
    totalProduced: 280912,  
    totalMissed: 672,  
    latestBlockNum: 16214311,  
    latestSlotNum: 526299468,  
    isJobs: true  
  },  
  {  
    address: '4138e3e3a163163db1f6cfceca1d1c64594dd1f0ca',  
    voteCount: 256034164,  
    url: 'https://twitter.com/justinsuntron',  
    totalProduced: 549168,  
    totalMissed: 1712,  
    latestBlockNum: 16214312,  
    latestSlotNum: 526299469,  
    isJobs: true  
  },  
   ... //more items
```