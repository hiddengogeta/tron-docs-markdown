

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getUnconfirmedTransactionInfo
Version: 6.3.0

On this page

# getUnconfirmedTransactionInfo [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L194)

Gets the details for an unconfirmed transaction by txid, including the fees and virtual machine events for an unconfirmed transaction.

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getUnconfirmedTransactionInfo(txID);
```

## Parameters[​](#parameters "Direct link to Parameters")

String - The transaction ID.

## Return[​](#return "Direct link to Return")

Object - The unconfirmed transaction info, see the example below.

## Example[​](#example "Direct link to Example")

```
await tronWeb.trx.getUnconfirmedTransactionInfo("f6b72dda65682b858c1c1980710aad7955fbf6db91c66840da0f852fc3cc694b");  
{  
  id: 'f6b72dda65682b858c1c1980710aad7955fbf6db91c66840da0f852fc3cc694b',  
  fee: 47350,  
  blockNumber: 16239601,  
  blockTimeStamp: 1578974295000,  
  contractResult: [  
    '0000000000000000000000000000000000000000000000000000000000000000'  
  ],  
  contract_address: '41a614f803b6fd780986a42c78ec9c7f77e6ded13c',  
  receipt: {  
    energy_fee: 43900,  
    origin_energy_usage: 10241,  
    energy_usage_total: 14631,  
    net_fee: 3450,  
    result: 'SUCCESS'  
  },  
  log: [  
    {  
      address: 'a614f803b6fd780986a42c78ec9c7f77e6ded13c',  
      topics: [Array],  
      data: '0000000000000000000000000000000000000000000000000000000b734e2770'  
    }  
  ]  
}
```