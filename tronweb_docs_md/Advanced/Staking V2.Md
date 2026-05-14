

* [Advanced](/docu/docs/category/advanced)
* Staking V2
Version: 6.3.0

On this page

# Staking V2

# Staking V2 Guide

TRON's Stake 2.0 (V2) system replaces the legacy Stake 1.0 model, providing more flexibility for resource management and delegation. This guide covers all V2 staking operations available in TronWeb.

tip

Stake 2.0 was introduced in JAVA-TRON v4.7.0.1. All new staking operations should use V2 methods. V1 methods (`freezeBalance`/`unfreezeBalance`) are deprecated.

## Overview[​](#overview "Direct link to Overview")

| Feature | Stake 1.0 (V1) | Stake 2.0 (V2) |
| --- | --- | --- |
| Stake | `freezeBalance` | `freezeBalanceV2` |
| Unstake | `unfreezeBalance` | `unfreezeBalanceV2` + `withdrawExpireUnfreeze` |
| Cancel Stake | N/A | `cancelUnfreezeBalanceV2` |
| Resource Delegation | Built into stake | Separate `delegateResource` |
| Flexibility | All-or-nothing | Partial stake/unstake |

## Stake TRX[​](#stake-trx "Direct link to Stake TRX")

Stake TRX to obtain **BANDWIDTH** or **ENERGY** resources.

```
const tx = await tronWeb.transactionBuilder.freezeBalanceV2(  
    1000000000, // amount in SUN (1000 TRX)  
    'ENERGY',   // resource type: 'BANDWIDTH' or 'ENERGY'  
);  
const signedTx = await tronWeb.trx.sign(tx);  
const receipt = await tronWeb.trx.sendRawTransaction(signedTx);
```

**Parameters:**

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `amount` | number | 0 | Amount of TRX to stake, in SUN |
| `resource` | string | `'BANDWIDTH'` | Resource type: `'BANDWIDTH'` or `'ENERGY'` |
| `address` | string | Default address | Owner address |
| `options` | object | `{}` | Transaction options (e.g., `{ permissionId }`) |

## Unstake TRX[​](#unstake-trx "Direct link to Unstake TRX")

Unstake TRX in two steps:

### Step 1: Initiate Unstaking[​](#step-1-initiate-unstaking "Direct link to Step 1: Initiate Unstaking")

```
// Start the unstaking process (14-day waiting period)  
const tx = await tronWeb.transactionBuilder.unfreezeBalanceV2(  
    500000000,  // amount in SUN (500 TRX)  
    'ENERGY',   // resource type  
);  
const signedTx = await tronWeb.trx.sign(tx);  
const receipt = await tronWeb.trx.sendRawTransaction(signedTx);
```

### Step 2: Withdraw After Waiting Period[​](#step-2-withdraw-after-waiting-period "Direct link to Step 2: Withdraw After Waiting Period")

After the 14-day waiting period, withdraw the unfrozen TRX:

```
const tx = await tronWeb.transactionBuilder.withdrawExpireUnfreeze();  
const signedTx = await tronWeb.trx.sign(tx);  
const receipt = await tronWeb.trx.sendRawTransaction(signedTx);
```

### Cancel Unstaking[​](#cancel-unstaking "Direct link to Cancel Unstaking")

Cancel a pending unstaking operation before the waiting period expires:

```
const tx = await tronWeb.transactionBuilder.cancelUnfreezeBalanceV2();  
const signedTx = await tronWeb.trx.sign(tx);  
const receipt = await tronWeb.trx.sendRawTransaction(signedTx);
```

## Resource Delegation[​](#resource-delegation "Direct link to Resource Delegation")

Delegate your frozen resources (bandwidth or energy) to another account.

### Delegate Resources[​](#delegate-resources "Direct link to Delegate Resources")

```
const tx = await tronWeb.transactionBuilder.delegateResource(  
    1000000000,     // amount in SUN  
    'TReceiverAddr', // receiver address  
    'ENERGY',        // resource type  
    'TOwnerAddr',    // owner address (optional)  
    false,           // lock delegation (optional)  
    0,               // lock period (optional)  
);  
const signedTx = await tronWeb.trx.sign(tx);  
const receipt = await tronWeb.trx.sendRawTransaction(signedTx);
```

**Parameters:**

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `amount` | number | 0 | Amount to delegate, in SUN |
| `receiverAddress` | string | - | Receiver's address |
| `resource` | string | `'BANDWIDTH'` | Resource type |
| `address` | string | Default address | Owner address |
| `lock` | boolean | `false` | Whether to lock the delegation |
| `lockPeriod` | number | - | Lock period in blocks (optional) |
| `options` | object | `{}` | Transaction options |

caution

The receiver address must be different from the owner address.

### Undelegate Resources[​](#undelegate-resources "Direct link to Undelegate Resources")

```
const tx = await tronWeb.transactionBuilder.undelegateResource(  
    500000000,       // amount in SUN  
    'TReceiverAddr', // address to undelegate from  
    'ENERGY',        // resource type  
);  
const signedTx = await tronWeb.trx.sign(tx);  
const receipt = await tronWeb.trx.sendRawTransaction(signedTx);
```

## Query Delegation Info[​](#query-delegation-info "Direct link to Query Delegation Info")

### Get Delegated Resources[​](#get-delegated-resources "Direct link to Get Delegated Resources")

```
// Get delegation details between two addresses  
const result = await tronWeb.trx.getDelegatedResourceV2(fromAddress, toAddress);  
console.log(result.delegatedResource);  
// [{  
//   from: 'address',  
//   to: 'address',  
//   frozen_balance_for_bandwidth: 0,  
//   frozen_balance_for_energy: 1000000000,  
//   ...  
// }]
```

### Get Delegation Index[​](#get-delegation-index "Direct link to Get Delegation Index")

```
// Get all accounts involved in delegations  
const result = await tronWeb.trx.getDelegatedResourceAccountIndexV2(address);  
console.log(result.fromAccounts); // Accounts that delegated to this address  
console.log(result.toAccounts);   // Accounts this address delegated to
```

### Get Maximum Delegatable Amount[​](#get-maximum-delegatable-amount "Direct link to Get Maximum Delegatable Amount")

```
const result = await tronWeb.trx.getCanDelegatedMaxSize(address, 'ENERGY');  
console.log(result.max_size); // Maximum amount that can be delegated
```

### Get Withdrawable Amount[​](#get-withdrawable-amount "Direct link to Get Withdrawable Amount")

```
// Check how much TRX can be withdrawn after unstaking  
const result = await tronWeb.trx.getCanWithdrawUnfreezeAmount(address);  
console.log(result.amount); // Amount available for withdrawal
```

### Get Available Unfreeze Count[​](#get-available-unfreeze-count "Direct link to Get Available Unfreeze Count")

```
// Check remaining unstaking slots  
const result = await tronWeb.trx.getAvailableUnfreezeCount(address);  
console.log(result.count); // Remaining unstaking times
```

## Complete Staking Workflow Example[​](#complete-staking-workflow-example "Direct link to Complete Staking Workflow Example")

```
import TronWeb from 'tronweb';  
  
const tronWeb = new TronWeb({  
    fullHost: 'https://api.trongrid.io',  
    privateKey: 'your-private-key',  
});  
  
// 1. Stake 1000 TRX for ENERGY  
const stakedTx = await tronWeb.transactionBuilder.freezeBalanceV2(  
    1000_000_000, 'ENERGY'  
);  
const signedStaked = await tronWeb.trx.sign(stakedTx);  
await tronWeb.trx.sendRawTransaction(signedStaked);  
  
// 2. Delegate 500 TRX of ENERGY to another account  
const delegateTx = await tronWeb.transactionBuilder.delegateResource(  
    500_000_000, 'TReceiverAddress', 'ENERGY'  
);  
const signedDelegate = await tronWeb.trx.sign(delegateTx);  
await tronWeb.trx.sendRawTransaction(signedDelegate);  
  
// 3. Check delegation details  
const delegation = await tronWeb.trx.getDelegatedResourceV2(  
    tronWeb.defaultAddress.base58, 'TReceiverAddress'  
);  
console.log('Delegated:', delegation);  
  
// 4. Undelegate resources  
const undelegateTx = await tronWeb.transactionBuilder.undelegateResource(  
    500_000_000, 'TReceiverAddress', 'ENERGY'  
);  
const signedUndelegate = await tronWeb.trx.sign(undelegateTx);  
await tronWeb.trx.sendRawTransaction(signedUndelegate);  
  
// 5. Start unstaking (14-day waiting period begins)  
const unstakedTx = await tronWeb.transactionBuilder.unfreezeBalanceV2(  
    1000_000_000, 'ENERGY'  
);  
const signedUnstaked = await tronWeb.trx.sign(unstakedTx);  
await tronWeb.trx.sendRawTransaction(signedUnstaked);  
  
// 6. After 14 days, withdraw unfrozen TRX  
const withdrawTx = await tronWeb.transactionBuilder.withdrawExpireUnfreeze();  
const signedWithdraw = await tronWeb.trx.sign(withdrawTx);  
await tronWeb.trx.sendRawTransaction(signedWithdraw);
```

## Related API References[​](#related-api-references "Direct link to Related API References")

* [transactionBuilder.freezeBalanceV2](/docu/docs/API List/transactionBuilder/freezeBalanceV2)
* [transactionBuilder.unfreezeBalanceV2](/docu/docs/API List/transactionBuilder/unfreezeBalanceV2)
* [transactionBuilder.cancelUnfreezeBalanceV2](/docu/docs/API List/transactionBuilder/cancelUnfreezeBalanceV2)
* [transactionBuilder.delegateResource](/docu/docs/API List/transactionBuilder/delegateResource)
* [transactionBuilder.undelegateResource](/docu/docs/API List/transactionBuilder/undelegateResource)
* [transactionBuilder.withdrawExpireUnfreeze](/docu/docs/API List/transactionBuilder/withdrawExpireUnfreeze)
* [trx.getDelegatedResourceV2](/docu/docs/API List/trx/getDelegatedResourceV2)
* [trx.getDelegatedResourceAccountIndexV2](/docu/docs/API List/trx/getDelegatedResourceAccountIndexV2)
* [trx.getCanDelegatedMaxSize](/docu/docs/API List/trx/getCanDelegatedMaxSize)
* [trx.getCanWithdrawUnfreezeAmount](/docu/docs/API List/trx/getCanWithdrawUnfreezeAmount)
* [trx.getAvailableUnfreezeCount](/docu/docs/API List/trx/getAvailableUnfreezeCount)