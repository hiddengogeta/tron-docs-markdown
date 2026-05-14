

* [References](/docu/docs/category/references)
* Error Codes
Version: 6.3.0

On this page

# Error Codes Reference

This page lists common error codes and messages encountered when using TronWeb.

## Transaction Errors[​](#transaction-errors "Direct link to Transaction Errors")

| Error | Description | Solution |
| --- | --- | --- |
| `BANDWITH_ERROR` | Insufficient bandwidth | Freeze TRX for bandwidth or ensure account has free bandwidth |
| `CONTRACT_VALIDATE_ERROR` | Transaction validation failed | Check parameters, account balance, or permissions |
| `CONTRACT_EXE_ERROR` | Contract execution failed | Check energy/fee limit, contract state, and input parameters |
| `SIGERROR` | Signature verification failed | Verify correct private key and transaction data |
| `DUP_TRANSACTION_ERROR` | Duplicate transaction | Transaction already submitted; wait or create a new one |
| `TAPOS_ERROR` | Block reference expired | Rebuild the transaction with current block reference |
| `TOO_BIG_TRANSACTION_ERROR` | Transaction too large | Reduce transaction data or split into multiple transactions |
| `TRANSACTION_EXPIRATION_ERROR` | Transaction expired | Rebuild and sign the transaction (default expiry: 60 seconds) |
| `NOT_ENOUGH_PERMISSION` | Multi-sig threshold not met | Collect more signatures before broadcasting |

## Smart Contract Errors[​](#smart-contract-errors "Direct link to Smart Contract Errors")

| Error | Description | Solution |
| --- | --- | --- |
| `OUT_OF_ENERGY` | Energy exhausted | Increase `feeLimit`, stake more TRX for energy |
| `OUT_OF_TIME` | Execution timeout | Optimize contract code, reduce complexity |
| `REVERT` | Contract reverted | Check `require()`/`revert()` conditions in contract |
| `JVMStackOverFlow` | Stack overflow | Reduce recursion depth in contract |
| `OUT_OF_MEMORY` | Memory limit exceeded | Reduce memory usage in contract |
| `TRANSFER_FAILED` | TRX/token transfer failed | Check recipient address and balance |

## TronWeb Client Errors[​](#tronweb-client-errors "Direct link to TronWeb Client Errors")

| Error Message | Description | Solution |
| --- | --- | --- |
| `Invalid address provided` | Address format invalid | Use valid base58 or hex address |
| `Invalid issuer address provided` | Sender address invalid | Set `tronWeb.defaultAddress` or provide valid address |
| `Private key does not match address` | Key-address mismatch | Use the correct private key for the account |
| `Invalid amount provided` | Amount is not a positive integer | Provide a positive integer value (in SUN) |
| `Invalid token ID provided` | Token ID not found | Verify the token exists on the network |
| `Contract has not been deployed` | Contract address invalid | Verify contract deployment and address |
| `Calling a non-contract address` | Address is not a contract | Check the contract address |

## HTTP API Errors[​](#http-api-errors "Direct link to HTTP API Errors")

| Status Code | Description | Solution |
| --- | --- | --- |
| 400 | Bad request | Check request parameters |
| 404 | Endpoint not found | Verify Full Node URL and API path |
| 503 | Node unavailable | Node is syncing or down; try another node |
| Rate limited | Too many requests | Reduce request frequency or use API key |

## Tips for Debugging[​](#tips-for-debugging "Direct link to Tips for Debugging")

1. **Check transaction info** — After broadcasting, check the transaction result:

   ```
   const info = await tronWeb.trx.getTransactionInfo(txId);  
   console.log(info.receipt);      // resource consumption  
   console.log(info.result);       // equal to 'FAILED' if failed  
   console.log(info.contractResult); // contract return data
   ```
2. **Decode revert reason** — For contract reverts:

   ```
   const info = await tronWeb.trx.getTransactionInfo(txId);  
   if (info.result === 'FAILED') {  
       const reason = tronWeb.toUtf8(info.resMessage);  
       console.log('Revert reason:', reason);  
   }
   ```
3. **Use confirmed endpoints** — For reliable reads, use confirmed (solidity) node:

   ```
   const confirmedBalance = await tronWeb.trx.getBalance(address, { confirmed: true });
   ```