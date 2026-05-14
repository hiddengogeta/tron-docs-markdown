

* [API List](/docu/docs/API List/)
* [trx](/docu/docs/API List/trx/)
* getChainParameters
Version: 6.3.0

On this page

# getChainParameters [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/lib/trx.ts#L1066)

Query the parameters of the blockchain used for witnessses to create a proposal

## Usage[​](#usage "Direct link to Usage")

```
tronWeb.trx.getChainParameters();
```

## Return[​](#return "Direct link to Return")

Arrays - An array of objects containing the parameters of the blockchain.

## Example[​](#example "Direct link to Example")

```
await tronWeb.trx.getChainParameters();  
[ { key: 'getMaintenanceTimeInterval', value: 21600000 },  
  { key: 'getAccountUpgradeCost', value: 9999000000 },  
  { key: 'getCreateAccountFee', value: 100000 },  
  { key: 'getTransactionFee', value: 10 },  
  { key: 'getAssetIssueFee', value: 1024000000 },  
  { key: 'getWitnessPayPerBlock', value: 32000000 },  
  { key: 'getWitnessStandbyAllowance', value: 115200000000 },  
  { key: 'getCreateNewAccountFeeInSystemContract' },  
  { key: 'getCreateNewAccountBandwidthRate', value: 1 },  
  { key: 'getAllowCreationOfContracts', value: 1 },  
  { key: 'getRemoveThePowerOfTheGr', value: -1 },  
  { key: 'getEnergyFee', value: 10 },  
  { key: 'getExchangeCreateFee', value: 1024000000 },  
  { key: 'getMaxCpuTimeOfOneTx', value: 50 },  
  { key: 'getAllowUpdateAccountName' },  
  { key: 'getAllowSameTokenName', value: 1 },  
  { key: 'getAllowDelegateResource', value: 1 },  
  { key: 'getTotalEnergyLimit', value: 100000000000 },  
  { key: 'getAllowTvmTransferTrc10', value: 1 },  
  { key: 'getTotalEnergyCurrentLimit', value: 100000000000 },  
  { key: 'getAllowMultiSign' },  
  { key: 'getAllowAdaptiveEnergy' },  
  { key: 'getTotalEnergyTargetLimit', value: 6944444 },  
  { key: 'getTotalEnergyAverageUsage' },  
  { key: 'getUpdateAccountPermissionFee', value: 100000000 },  
  { key: 'getMultiSignFee', value: 1000000 } ]
```