

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getAccountResources
Version: 6.3.0

On this page

# getAccountResources [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L1078)

Get the account's bandwidth and energy resources.

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getAccountResources(address);
```

## Parameter[​](#parameter "Direct link to Parameter")

Address string(in either HexString or Base58 format)

## Return[​](#return "Direct link to Return")

Object - Account resources, see examples below.

## Example[​](#example "Direct link to Example")

```
//Parameter Base58  
await tronWeb.trx.getAccountResources('TTSFjEG3Lu9WkHdp4JrWYhbGP6K1REqnGQ');  
{  
  freeNetLimit: 5000,  
  NetLimit: 483512,  
  assetNetUsed: [ { key: '1000001', value: 0 } ],  
  assetNetLimit: [ { key: '1000001', value: 0 } ],  
  TotalNetLimit: 43200000000,  
  TotalNetWeight: 1072155,  
  EnergyLimit: 4949344,  
  TotalEnergyLimit: 971444468045,  
  TotalEnergyWeight: 2355329  
}  
  
//Parameter HexString  
await tronWeb.trx.getAccountResources('41BF97A54F4B829C4E9253B26024B1829E1A3B1120');  
{  
  freeNetLimit: 5000,  
  NetLimit: 448135,  
  assetNetUsed: [ { key: '1000001', value: 0 } ],  
  assetNetLimit: [ { key: '1000001', value: 0 } ],  
  TotalNetLimit: 43200000000,  
  TotalNetWeight: 1156792,  
  EnergyLimit: 1778164,  
  TotalEnergyLimit: 381032718821,  
  TotalEnergyWeight: 2571411  
}
```