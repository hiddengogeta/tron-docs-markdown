

* [Advanced](/docu/docs/category/advanced)
* Multi-Signature
Version: 6.3.0

On this page

# Multi-Signature Guide

Multi-signature (multi-sig) enables multiple parties to collectively authorize transactions on TRON. This is essential for organizational accounts, DAOs, and shared treasury management.

## How Multi-Signature Works[​](#how-multi-signature-works "Direct link to How Multi-Signature Works")

TRON accounts support three permission types:

| Permission | Description | Use Case |
| --- | --- | --- |
| **Owner** | Highest-level permission, can modify all permissions | Account recovery, permission changes |
| **Active** | Customizable operation permissions | Daily operations, contract calls |
| **Witness** | Super Representative operations | Block production |

Each permission defines:

* **threshold**: Minimum total weight required to approve
* **keys**: List of addresses with assigned weights

## Setting Up Multi-Sig Permissions[​](#setting-up-multi-sig-permissions "Direct link to Setting Up Multi-Sig Permissions")

Use `updateAccountPermissions` to configure multi-sig on an account:

```
const ownerPermission = {  
    type: 0,  
    permission_name: 'owner',  
    threshold: 2,  
    keys: [  
        { address: 'TAddress1', weight: 1 },  
        { address: 'TAddress2', weight: 1 },  
        { address: 'TAddress3', weight: 1 },  
    ],  
};  
  
const activePermission = {  
    type: 2,  
    permission_name: 'active0',  
    threshold: 2,  
    operations: '7fff1fc0033e0300000000000000000000000000000000000000000000000000',  
    keys: [  
        { address: 'TAddress1', weight: 1 },  
        { address: 'TAddress2', weight: 1 },  
    ],  
};  
  
const tx = await tronWeb.transactionBuilder.updateAccountPermissions(  
    ownerAddress,       // account to update  
    ownerPermission,    // owner permission config  
    null,               // witness permission (null for non-SR accounts)  
    [activePermission], // active permissions array  
);  
const signedTx = await tronWeb.trx.sign(tx);  
const receipt = await tronWeb.trx.sendRawTransaction(signedTx);
```

caution

Changing owner permission is irreversible without the required signers. Ensure you have access to enough keys to meet the new threshold.

## Signing Multi-Sig Transactions[​](#signing-multi-sig-transactions "Direct link to Signing Multi-Sig Transactions")

### Step 1: Create the Transaction[​](#step-1-create-the-transaction "Direct link to Step 1: Create the Transaction")

```
// Create a transaction as usual  
const tx = await tronWeb.transactionBuilder.sendTrx(  
    'TReceiverAddr', 1000000, 'TMultiSigAddr'  
);
```

### Step 2: Collect Signatures[​](#step-2-collect-signatures "Direct link to Step 2: Collect Signatures")

Each signer signs the transaction independently using `multiSign`:

```
// Signer 1 signs with their private key  
const signedTx1 = await tronWeb.trx.multiSign(tx, privateKey1, 2);  
// permissionId: 0 = owner, 2 = active (default)  
  
// Signer 2 signs the already-signed transaction  
const signedTx2 = await tronWeb.trx.multiSign(signedTx1, privateKey2, 2);
```

**Parameters:**

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `transaction` | object | - | The transaction to sign |
| `privateKey` | string | - | Private key of the signer |
| `permissionId` | number | `0` | Permission ID (0=owner, 2+=active) |

### Step 3: Verify and Broadcast[​](#step-3-verify-and-broadcast "Direct link to Step 3: Verify and Broadcast")

```
// Check if enough signatures are collected  
const signWeight = await tronWeb.trx.getSignWeight(signedTx2, 2);  
console.log(signWeight.current_weight);  // Current total weight  
console.log(signWeight.result?.code);    // 'ENOUGH_PERMISSION' when ready  
  
// Get the list of approved addresses  
const approvedList = await tronWeb.trx.getApprovedList(signedTx2);  
console.log(approvedList.approved_list); // ['TAddress1', 'TAddress2']  
  
// Broadcast when threshold is met  
if (signWeight.current_weight >= signWeight.permission.threshold) {  
    const receipt = await tronWeb.trx.sendRawTransaction(signedTx2);  
    console.log('Transaction sent:', receipt.txid);  
}
```

## Complete Multi-Sig Workflow[​](#complete-multi-sig-workflow "Direct link to Complete Multi-Sig Workflow")

```
import TronWeb from 'tronweb';  
  
// Setup - each signer has their own TronWeb instance  
const tronWeb = new TronWeb({  
    fullHost: 'https://api.trongrid.io',  
    privateKey: 'owner-private-key',  
});  
  
// 1. Configure 2-of-3 multi-sig  
const ownerPermission = {  
    type: 0,  
    permission_name: 'owner',  
    threshold: 2,  
    keys: [  
        { address: tronWeb.address.fromPrivateKey(pk1), weight: 1 },  
        { address: tronWeb.address.fromPrivateKey(pk2), weight: 1 },  
        { address: tronWeb.address.fromPrivateKey(pk3), weight: 1 },  
    ],  
};  
  
const activePermission = {  
    type: 2,  
    permission_name: 'active0',  
    threshold: 2,  
    operations: '7fff1fc0033e0300000000000000000000000000000000000000000000000000',  
    keys: [  
        { address: tronWeb.address.fromPrivateKey(pk1), weight: 1 },  
        { address: tronWeb.address.fromPrivateKey(pk2), weight: 1 },  
        { address: tronWeb.address.fromPrivateKey(pk3), weight: 1 },  
    ],  
};  
  
const updateTx = await tronWeb.transactionBuilder.updateAccountPermissions(  
    tronWeb.defaultAddress.base58,  
    ownerPermission,  
    null,  
    [activePermission],  
);  
const signedUpdate = await tronWeb.trx.sign(updateTx);  
await tronWeb.trx.sendRawTransaction(signedUpdate);  
  
// 2. Create a transfer from the multi-sig account  
const transferTx = await tronWeb.transactionBuilder.sendTrx(  
    'TReceiverAddr', 10_000_000, tronWeb.defaultAddress.base58  
);  
  
// 3. Collect 2 signatures (active permission, id=2)  
let signedTx = await tronWeb.trx.multiSign(transferTx, pk1, 2);  
signedTx = await tronWeb.trx.multiSign(signedTx, pk2, 2);  
  
// 4. Verify and broadcast  
const weight = await tronWeb.trx.getSignWeight(signedTx, 2);  
if (weight.current_weight >= 2) {  
    const result = await tronWeb.trx.sendRawTransaction(signedTx);  
    console.log('Success:', result.txid);  
}
```

## Active Permission Operations[​](#active-permission-operations "Direct link to Active Permission Operations")

The `operations` field in active permissions is a hex bitmask that controls which contract types the permission can execute. Common values:

| Value | Description |
| --- | --- |
| `7fff1fc0033e0300...` | All standard operations |
| Custom hex | Specific operation subset |

Each bit position corresponds to a TRON contract type (TransferContract, TriggerSmartContract, etc.).

## Related API References[​](#related-api-references "Direct link to Related API References")

* [trx.multiSign](/docu/docs/API List/trx/multiSign)
* [trx.getApprovedList](/docu/docs/API List/trx/getApprovedList)
* [trx.getSignWeight](/docu/docs/API List/trx/getSignWeight)
* [transactionBuilder.updateAccountPermissions](/docu/docs/API List/transactionBuilder/updateAccountPermissions)