

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* timeUntilNextVoteCycle
Version: 6.3.0

On this page

# timeUntilNextVoteCycle [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L497)

Query the time interval till the next vote round

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.timeUntilNextVoteCycle();
```

## Return[​](#return "Direct link to Return")

Number - The time interval till the next vote round.

## Example[​](#example "Direct link to Example")

```
await tronWeb.trx.timeUntilNextVoteCycle();  
1579068000
```