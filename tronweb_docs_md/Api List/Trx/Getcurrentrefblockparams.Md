

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getCurrentRefBlockParams
Version: 6.3.0

On this page

# getCurrentRefBlockParams [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L1507)

Retrieve the parameters required for transaction building

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getCurrentRefBlockParams()
```

## Return[​](#return "Direct link to Return")

Object - with 4 properties that can be passed to transactionBuilder methods:

* ref\_block\_bytes
* ref\_block\_hash
* expiration
* timestamp

## Example[​](#example "Direct link to Example")

```
await tronWeb.trx.getCurrentRefBlockParams();  
{  
  ref_block_bytes: '0015',  
  ref_block_hash: 'a7e9b8b30827c333',  
  expiration: 1760932113000,  
  timestamp: 1760932053000  
}
```