

* Terminology
Version: 6.3.0

On this page

# Terminology

## Address(public key) & private key[​](#addresspublic-key--private-key "Direct link to Address(public key) & private key")

The public key and the private key are a key pair obtained via a hash algorithm.
The public key is the public part while the private key is the non-public part. And the public key can be calculated from the private key using a specific algorithm.
An address is derived from a public key. It has two formats: hex and Base58. Hex format consists of 42 hex characters and always starts with '41'. Base58 format consists of 34 Base58 characters and always starts with 'T'.
The private key consists of 64 hex characters. **You should always keep the private key secret**.

## Mnemonic[​](#mnemonic "Direct link to Mnemonic")

A mnemonic (or mnemonic phrase) is a set of human-readable words used to back up and restore a crypto wallet. It’s based on the BIP-39 standard. This phrase represents a private key in a secure and memorable way. Anyone with access to the mnemonic can control the derived private keys, so **it must be kept secret and safe**.

## Transactions[​](#transactions "Direct link to Transactions")

Transactions are cryptographically signed instructions from accounts. An account will initiate a transaction to update the state of the TRON network. A common transaction format is as below:

```
{  
    "raw_data":   
    {  
        "contract": [{<-->}],  
        "ref_block_bytes": "c145",  
        "ref_block_hash": "c56bd8a3b3341d9d",  
        "expiration": 1646796363000,  
        "data": "74657374",  
        "timestamp": 1646796304152,  
        "fee_limit":10000000000  
    },  
    "signature":["47b1f77b3e30cfbbfa41d795dd34475865240617dd1c5a7bad526f5fd89e52cd057c80b665cc2431efab53520e2b1b92a0425033baee915df858ca1c588b0a1800" ]   
}
```

TronWeb has supported 36 transaction types so far. You can go [here](/docu/docs/API List/transactionBuilder/) for more details.

If you want to know more about what transactions are, you can go [here](https://developers.tron.network/docs/tron-protocol-transaction).

## Contract[​](#contract "Direct link to Contract")

Contracts are a set of code (its function) and data (its state) that reside at a specific address on the TRON network. Contracts can be created and deployed by an account. Once deployed, a contract is immutable and can only be destroyed by its owner. To know more details, go [here](https://developers.tron.network/docs/smart-contracts-introduction).

## Event[​](#event "Direct link to Event")

Event is used to output specific binary data and record it in TransactionInfo while TRON virtual machine is running a contract. The Event Log can help developers confirm, check, and quickly retrieve specific states of a smart contract. TronWeb mainly provides 3 APIs to retrieve events: `getEventsByContractAddress`, `getEventsByTransactionID` and `getEventsByBlockNumber`. To know the detail of event, please visit [event docs](https://developers.tron.network/docs/event).

## Multi sign[​](#multi-sign "Direct link to Multi sign")

Multi sign is a transaction type that allows multiple accounts to sign a transaction. Before you use multi sign, you need to update account permission config. Each permission can correspond to multiple private keys. This makes it possible to achieve multi-person joint control of accounts, and different permissions are managed by different people. With account permission set, you can use `tronWeb.trx.multiSign` to sign a transaction. For more about multi sign, go [here](https://developers.tron.network/docs/multi-signature).

## Block header[​](#block-header "Direct link to Block header")

A block is used to store transaction information and includes a block header. The block header is used to verify the integrity of the block. It contains key metadata that uniquely identifies the block and links it to previous blocks—forming the blockchain. In TronWeb, a block header includes the following four fields:

* ref\_block\_bytes: The last 4 bytes of the reference block height, in hex format.
* ref\_block\_hash: The 8th to 16th(exclusive) bytes of the reference block hash(ID), in hex format.
* expiration: The expiration time of the transaction which should be no more than 1 day. The unit is milliseconds.
* timestamp: The timestamp of the transaction. The unit is milliseconds.

## Super representatives[​](#super-representatives "Direct link to Super representatives")

Block producers of the TRON network, also called super representatives (SRs), are elected through voting. Any account can apply to become an SR candidate by paying 9,999 TRX and then participate in the SR election. Any account can vote for SR candidates, and the top 27 candidates with the most votes become SRs, who need to run a TRON node to participate in block production and will receive block production rewards and voting rewards. Voters who vote for SRs will also receive voting rewards. To know more about super representative, go [here](https://developers.tron.network/docs/super-representatives).

## Staking V2[​](#staking-v2 "Direct link to Staking V2")

TRON allocates resources through the staking mechanism. In addition to obtaining Bandwidth or Energy resources, staking TRX can also bring you voting rights (which is TRON Power, TP for short), equal to the amount of TRX staked. The Energy or Bandwidth resources obtained by staking are used to pay transaction fees, and the obtained voting rights are used to vote for Super Representatives (SRs) to obtain voting rewards. To know more about staking, go [here](https://developers.tron.network/docs/staking-on-tron-network).