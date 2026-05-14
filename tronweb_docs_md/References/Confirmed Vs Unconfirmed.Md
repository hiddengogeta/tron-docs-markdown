

* [References](/docu/docs/category/references)
* Confirmed vs Unconfirmed
Version: 6.3.0

On this page

# Confirmed vs Unconfirmed Transactions

Understanding the difference between confirmed and unconfirmed transaction states is essential for building reliable TRON applications.

## Transaction Lifecycle[​](#transaction-lifecycle "Direct link to Transaction Lifecycle")

```
Create → Sign → Broadcast → Pending → Confirmed (Solid)  
                                ↓  
                            Unconfirmed
```

| State | Description | Finality |
| --- | --- | --- |
| **Unconfirmed** | Transaction is in the pending pool or in a recent block not yet solidified | May be rolled back |
| **Confirmed (Solid)** | Transaction is in a solidified block (approved by 2/3+ of SRs) | Irreversible |

## TRON Block Confirmation[​](#tron-block-confirmation "Direct link to TRON Block Confirmation")

* **Block time**: ~3 seconds
* **Solidification**: A block is confirmed after 2/3 of the 27 Super Representatives confirm it
* **Typical confirmation time**: ~19 blocks (~57 seconds)

## Querying Confirmed vs Unconfirmed Data[​](#querying-confirmed-vs-unconfirmed-data "Direct link to Querying Confirmed vs Unconfirmed Data")

### Full Node (Unconfirmed)[​](#full-node-unconfirmed "Direct link to Full Node (Unconfirmed)")

By default, TronWeb queries the **Full Node**, which returns the latest state including unconfirmed transactions:

```
// Unconfirmed (latest) balance  
const balance = await tronWeb.trx.getBalance(address);  
  
// Unconfirmed transaction  
const tx = await tronWeb.trx.getTransaction(txId);
```

### Solidity Node (Confirmed)[​](#solidity-node-confirmed "Direct link to Solidity Node (Confirmed)")

For confirmed data, use the `confirmed: true` option or solidity-node endpoints:

```
// Confirmed balance  
const confirmedBalance = await tronWeb.trx.getBalance(address, { confirmed: true });  
  
// Confirmed transaction  
const confirmedTx = await tronWeb.trx.getConfirmedTransaction(txId);
```

### Event Queries[​](#event-queries "Direct link to Event Queries")

```
// Get confirmed events only  
const events = await tronWeb.event.getEventsByContractAddress(contractAddress, {  
    onlyConfirmed: true,  
});  
  
// Get unconfirmed events only  
const unconfirmedEvents = await tronWeb.event.getEventsByContractAddress(contractAddress, {  
    onlyUnconfirmed: true,  
});
```

## TronWeb Node Configuration[​](#tronweb-node-configuration "Direct link to TronWeb Node Configuration")

TronWeb uses separate endpoints for confirmed and unconfirmed data:

```
const tronWeb = new TronWeb({  
    fullHost: 'https://api.trongrid.io',  
    // OR specify individually:  
    fullNode: 'https://api.trongrid.io',  
    solidityNode: 'https://api.trongrid.io',  
    eventServer: 'https://api.trongrid.io',  
});
```

* **fullNode**: Returns unconfirmed (latest) data
* **solidityNode**: Returns confirmed (solid) data only
* **eventServer**: Event query endpoint supporting both modes

## When to Use Which[​](#when-to-use-which "Direct link to When to Use Which")

| Use Case | Recommended | Reason |
| --- | --- | --- |
| Display balance to user | Unconfirmed | Faster, shows pending changes |
| Process payments | **Confirmed** | Prevents double-spend attacks |
| Read contract state | Depends | Unconfirmed for UI, confirmed for critical logic |
| Event listeners | Both | Monitor unconfirmed for UX, confirmed for finality |
| Exchange deposits | **Confirmed** | Always wait for solid confirmation |

## Best Practices[​](#best-practices "Direct link to Best Practices")

1. **Always confirm payments** — Never treat unconfirmed transactions as final for financial operations.
2. **Poll for confirmation** — After broadcasting, poll for confirmed status:

   ```
   async function waitForConfirmation(txId, maxRetries = 20) {  
       for (let i = 0; i < maxRetries; i++) {  
           try {  
               const result = await tronWeb.trx.getConfirmedTransaction(txId);  
               if (result && result.txID) {  
                   return result;  
               }  
           } catch (e) {  
               // Not confirmed yet  
           }  
           await new Promise(r => setTimeout(r, 3000)); // Wait 3 seconds  
       }  
       throw new Error('Transaction not confirmed');  
   }
   ```
3. **Handle rollbacks** — Unconfirmed transactions can be dropped. Design your application to handle this case.