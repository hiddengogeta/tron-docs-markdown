

* Core concepts
Version: 6.3.0

On this page

# Core concepts

## Account[​](#account "Direct link to Account")

In TronWeb, an account is an object including the following properties:

* `address.base58`: The address of the account, base58 format.
* `address.hex`: The address of the account, hex format.
* `privateKey`: The private key of the account. You need to keep it secret.
* `publicKey`: The public key of the account.

If an account is activated, it means that it has been recorded on the TRON network. Thus, it has many other attributes such as TRX & TRC10 token balances, Bandwidth amount, and Energy amount. You can use `tronWeb.trx.getAccount(address)` to get the account information.

For more information about TRON account model, go [here](https://developers.tron.network/docs/account).

## Contract[​](#contract "Direct link to Contract")

The Contract class is used for interacting with contracts. You can use it to deploy and trigger contracts.

It is recommended to instantiate a contract like this: `const contract = tronWeb.contract(abi, contractAddress)`.

If you want to deploy a contract, you can use `await tronWeb.contract().new(options)` where options is the same as the argument of `tronWeb.transactionBuilder.createSmartContract`.

If you want to trigger a contract, you can use `await contract.method(params).call()` or `await contract.method(params).send()`.

If you want to get the information about a deployed contract, you can use `await tronWeb.trx.getContract(contract_address)`.

Refer to the [Interact with contract](/docu/docs/Interact with contract) for a complete example.

## FullNode & SolidityNode & EventServer[​](#fullnode--soliditynode--eventserver "Direct link to FullNode & SolidityNode & EventServer")

"Node" refers to a running piece of client software. A client is an implementation of TRON protocol that verifies all transactions in each block, keeping the network secure and the data accurate. A full node is a client that synchronizes the blockchain data and maintains the full history of the blockchain. A Solidity node is a client that maintains the full history of the solidified blockchain. An event server is a client that maintains the event logs. When instantiating a TronWeb instance, you can specify the fullNode, solidityNode and eventServer address. If they have the same address, you can set `fullHost` attribute instead.

## TransactionBuilder[​](#transactionbuilder "Direct link to TransactionBuilder")

TransactionBuilder is a class that helps you build transaction object. For example, you can use `tronWeb.transactionBuilder.sendTrx(to_address, amount)` to build a transaction object to send TRX. You can also use `tronWeb.transactionBuilder.createSmartContract(options)` to build a transaction object to deploy a contract. TronWeb has supported the most commonly used transaction types. For more details, refer to the [Build transaction](/docu/docs/API List/transactionBuilder/).

## Energy & Bandwidth & feeLimit[​](#energy--bandwidth--feelimit "Direct link to Energy & Bandwidth & feeLimit")

Bandwidth, and Energy are important system resources of the TRON network. Bandwidth is the unit that measures the size of the transaction bytes stored in the blockchain database. Energy is the unit that measures the amount of computation required by the TRON Virtual Machine (TVM) to perform specific operations on the TRON network.
The execution of each instruction of a smart contract consumes a certain amount of Energy while running. But you can specify the max fee you want to consume in a contract related transaction. That attribute is feeLimit. TronWeb has set the default feeLimit to `150000000`. The unit is sun and `1 Trx = 1000000 sun`.

## Processing transactions locally[​](#processing-transactions-locally "Direct link to Processing transactions locally")

To process transactions locally, TronWeb introduces protobuf. You can get a protobuf object from a transaction object by using `tronWeb.utils.transaction.txJsonToPb(transaction)`. Due to the benefit of protobuf, you can recover the transaction detail from raw data hex by using `tronWeb.utils.transaction.DeserializeTransaction(transactionType, raw_data_hex)`.