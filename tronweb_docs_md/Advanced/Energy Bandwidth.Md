

* [Advanced](/docu/docs/category/advanced)
* Energy & Bandwidth
Version: 6.3.0

On this page

# Energy & Bandwidth Guide

Every transaction on TRON consumes resources — **Bandwidth** for data transmission and **Energy** for smart contract execution. Understanding these resources is critical for cost optimization.

## Resource Types[​](#resource-types "Direct link to Resource Types")

| Resource | Purpose | How to Obtain | Consumed By |
| --- | --- | --- | --- |
| **Bandwidth** | Transaction data size | Freeze TRX / Daily free allowance | All transactions |
| **Energy** | Smart contract execution | Freeze TRX only | Contract calls only |

### Free Bandwidth[​](#free-bandwidth "Direct link to Free Bandwidth")

TRON provides free bandwidth (resets every 24 hours) for every account. For details, see [here](https://developers.tron.network/docs/resource-model#bandwidth).

### Bandwidth Cost[​](#bandwidth-cost "Direct link to Bandwidth Cost")

Each transaction consumes bandwidth based on its raw data byte size. If bandwidth is insufficient, TRX is burned for the transaction fee.

### Energy Cost[​](#energy-cost "Direct link to Energy Cost")

Energy is required only for smart contract operations (deploy, trigger). The energy cost depends on the contract's computational complexity.

## Estimating Energy[​](#estimating-energy "Direct link to Estimating Energy")

Before calling a smart contract, estimate the energy required:

```
const result = await tronWeb.transactionBuilder.estimateEnergy(  
    'TContractAddr',               // contract address  
    'transfer(address,uint256)',   // function selector  
    {},                             // options  
    [  
        { type: 'address', value: 'TReceiverAddr' },  
        { type: 'uint256', value: 1000000 },  
    ],  
    'TCallerAddr',                 // issuer address  
);  
console.log('Estimated energy:', result.energy_required);
```

**Parameters:**

| Parameter | Type | Description |
| --- | --- | --- |
| `contractAddress` | string | Smart contract address |
| `functionSelector` | string | Function signature (e.g., `'transfer(address,uint256)'`) |
| `options` | object | Options like `{ callValue, tokenId, tokenValue, feeLimit }` |
| `parameters` | array | Function parameters: `[{ type, value }]` |
| `issuerAddress` | string | Caller address |

### Constant Contract Deployment[​](#constant-contract-deployment "Direct link to Constant Contract Deployment")

For estimating deployment costs:

```
const result = await tronWeb.transactionBuilder.deployConstantContract({  
    input: contractBytecode,  
    ownerAddress: 'TDeployerAddr',  
    // ABI, feeLimit, etc.  
});  
console.log('Deploy energy estimate:', result.energy_used);
```

## Querying Account Resources[​](#querying-account-resources "Direct link to Querying Account Resources")

```
const resources = await tronWeb.trx.getAccountResources(address);  
console.log(resources);  
// {  
//   freeNetUsed: 100,        // Free bandwidth used  
//   freeNetLimit: 1500,      // Free bandwidth limit  
//   NetUsed: 200,            // Staked bandwidth used  
//   NetLimit: 5000,          // Staked bandwidth limit  
//   EnergyUsed: 10000,       // Energy used  
//   EnergyLimit: 50000,      // Energy limit from staking  
//   TotalNetLimit: ...,      // Network total bandwidth  
//   TotalNetWeight: ...,     // Network total bandwidth weight  
//   TotalEnergyLimit: ...,   // Network total energy  
//   TotalEnergyWeight: ...,  // Network total energy weight  
// }
```

## Resource Calculation[​](#resource-calculation "Direct link to Resource Calculation")

### How Much Energy Do I Get From Staking?[​](#how-much-energy-do-i-get-from-staking "Direct link to How Much Energy Do I Get From Staking?")

```
Your Energy = (Your Frozen TRX / Total Network Frozen TRX) × Total Energy Limit
```

```
const resources = await tronWeb.trx.getAccountResources(address);  
const myFrozen = 10000_000_000; // 10,000 TRX in SUN  
const estimatedEnergy = Math.floor(  
    (myFrozen / resources.TotalEnergyWeight) * resources.TotalEnergyLimit  
);  
console.log('Estimated energy from staking:', estimatedEnergy);
```

### Bandwidth Calculation[​](#bandwidth-calculation "Direct link to Bandwidth Calculation")

```
Your Bandwidth = (Your Frozen TRX / Total Network Frozen TRX) × Total Bandwidth Limit
```

## Cost Optimization Tips[​](#cost-optimization-tips "Direct link to Cost Optimization Tips")

1. **Stake for Energy** — Contract-heavy dApps should stake TRX for energy rather than paying per-transaction TRX fees.
2. **Estimate before execution** — Always use `estimateEnergy` before calling contracts to set appropriate `feeLimit`.
3. **Use free bandwidth** — Simple TRX transfers and TRC-10 operations can use the daily free bandwidth allowance.
4. **Batch operations** — Combine multiple operations when possible to reduce overhead.
5. **Set appropriate feeLimit** — Setting `feeLimit` too high doesn't cost more, but setting it too low causes transaction failure with fees still consumed.

```
// Good practice: estimate + buffer  
const estimate = await tronWeb.transactionBuilder.estimateEnergy(...);  
const safeLimit = Math.ceil(estimate.energy_required * 1.2); // 20% buffer  
const chainParameters = await tronWeb.trx.getChainParameters();  
// current energy price in SUN  
const energyPrice = chainParameters.find((item) => item.key === 'getEnergyFee').value;  
  
const tx = await tronWeb.transactionBuilder.triggerSmartContract(  
    contractAddress,  
    'transfer(address,uint256)',  
    { feeLimit: safeLimit * energyPrice },  
    [{ type: 'address', value: to }, { type: 'uint256', value: amount }],  
);
```

## Related API References[​](#related-api-references "Direct link to Related API References")

* [transactionBuilder.estimateEnergy](/docu/docs/API List/transactionBuilder/estimateEnergy)
* [trx.getAccountResources](/docu/docs/API List/trx/getAccountResources)
* [transactionBuilder.freezeBalanceV2](/docu/docs/API List/transactionBuilder/freezeBalanceV2)