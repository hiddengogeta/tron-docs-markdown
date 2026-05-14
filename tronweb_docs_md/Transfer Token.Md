

* Transfer Token
Version: 6.3.0

On this page

# Transfer Token

We mainly describe how to transfer 4 token types: TRX, TRC10, TRC20, TRC721

## Transfer TRX[​](#transfer-trx "Direct link to Transfer TRX")

Tron supports transferring TRX by sending a `TransferContract`-type transaction. You can do it as follows:

```
const receiverAddress = '';  
const amount = 1e6; // unit in sun.  
const tx = await tronWeb.transactionBuilder.sendTrx(receiverAddress, amount);  
const signedTx = await tronWeb.trx.sign(tx);  
const result = await tronWeb.trx.sendRawTransaction(signedTx);
```

To transfer TRX easily, TronWeb offers the `tronWeb.trx.sendTrx` method, which handles the transaction creation and broadcasting for you.

## Transfer TRC10 token[​](#transfer-trc10-token "Direct link to Transfer TRC10 token")

Tron supports transferring TRC10 token by sending a `TransferAssetContract`-type transaction. You can do it as follows:

```
const receiverAddress = '';  
const amount = 100;  
const tokenId = '1000086';  
const tx = await tronWeb.transactionBuilder.sendToken(receiverAddress, amount, tokenId);  
const signedTx = await tronWeb.trx.sign(tx);  
const result = await tronWeb.trx.sendRawTransaction(signedTx);
```

To transfer TRC10 token easily, TronWeb offers the `tronWeb.trx.sendToken` method, which handles the transaction creation and broadcasting for you.

## transfer TRC20 token[​](#transfer-trc20-token "Direct link to transfer TRC20 token")

Transfer TRC20 token is as using `triggerSmartContract` method, see the example:

```
const functionSelector = 'transfer(address,uint256)';  
const parameter = [{type:'address',value:'ACCOUNT_ADDRESS'},{type:'uint256',value:100}]  
const tx = await tronWeb.transactionBuilder.triggerSmartContract('USDT_ADDRESS', functionSelector, {}, parameter);  
const signedTx = await tronWeb.trx.sign(tx.transaction);  
const result = await tronWeb.trx.sendRawTransaction(signedTx);  
// the result looks like below:  
{  
  "result": true,  
  "txid": "bea6cff8d62d62209f87810396a9a26802b93f566cb08f925ec91a071002060f",  
  "transaction": {  
    "visible": false,  
    "txID": "bea6cff8d62d62209f87810396a9a26802b93f566cb08f925ec91a071002060f",  
    "raw_data": {  
      "contract": [  
        {  
          "parameter": {  
            "value": {  
              "data": "a9059cbb000000000000000000000000526f3626eaccc3f5fadd8f5f51fd9c49ce53b0900000000000000000000000000000000000000000000000000000000000000064",  
              "owner_address": "4175f09e51f8ecb695a0be1701581ec9493b164495",  
              "contract_address": "41eca9bc828a3005b9a3b909f2cc5c2a54794de05f"  
            },  
            "type_url": "type.googleapis.com/protocol.TriggerSmartContract"  
          },  
          "type": "TriggerSmartContract"  
        }  
      ],  
      "ref_block_bytes": "3bc7",  
      "ref_block_hash": "a5b57140c2f487fa",  
      "expiration": 1677063573000,  
      "fee_limit": 150000000,  
      "timestamp": 1677063515485  
    },  
    "raw_data_hex": "0a023bc72208a5b57140c2f487fa40889c9dc6e7305aae01081f12a9010a31747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e54726967676572536d617274436f6e747261637412740a154175f09e51f8ecb695a0be1701581ec9493b164495121541eca9bc828a3005b9a3b909f2cc5c2a54794de05f2244a9059cbb000000000000000000000000526f3626eaccc3f5fadd8f5f51fd9c49ce53b090000000000000000000000000000000000000000000000000000000000000006470ddda99c6e730900180a3c347",  
    "signature": [  
      "c1dddbc3812ad0b93d245b304506f6df54c0ff8e56167a52211e560ca1bb8aea45329c9ed2f3a0e959412cf1099f3042f5f716677bb196df1d02e0bf27d5dec800"  
    ]  
  }  
}
```

## transfer TRC721 token(nft)[​](#transfer-trc721-tokennft "Direct link to transfer TRC721 token(nft)")

Call the transferFrom() function of the TRC721 contract for NFT transfers, see the example:

```
const { TronWeb, providers } = require('tronweb')  
  
const HttpProvider = providers.HttpProvider;  
const fullNode = new HttpProvider("https://nile.trongrid.io");  
const solidityNode = new HttpProvider("https://nile.trongrid.io");  
const eventServer = new HttpProvider("https://nile.trongrid.io");  
const privateKey = "your private key";  
const tronWeb = new TronWeb(fullNode,solidityNode,eventServer,privateKey);  
  
async function trc721_transferFrom() {  
    const trc721ContractAddress = "TRio4FwnDvtYN2ogss6Qm7Hn2EaTLwWMNs";//contract address  
  
    try {  
        let abi = [...];  
        let contract = await tronWeb.contract(abi, trc721ContractAddress);  
        //Use send to execute a non-pure or modify smart contract method on a given smart contract that modifies or changes values on the blockchain.  
        // These methods consume resources(bandwidth and energy) to perform as the changes need to be broadcasted out to the network.  
        await contract.transferFrom(  
            "TA1g2WQiXbU5GnYBTJ5Cp22dvSjT3ug9uK", //address _from  
            "TM8vRhebJD7zeoBLWAnr9SrYrhWNrHjBgC", //address _to  
            666 //uint256 tokenId  
        ).send({  
            feeLimit: 100000000  
        }).then(output => {console.log('- transferFrom hash:', output, '\n');});  
    } catch(error) {  
        console.error("trigger smart contract error",error)  
    }  
}  
trc721_transferFrom()
```