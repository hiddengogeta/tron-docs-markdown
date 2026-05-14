

* Interact with the contract
Version: 6.3.0

On this page

# Interact with the contract

TronWeb provides several methods to interact with the contract. First, you need to instantiate a contract. Here we use USDT contract in nile test net and assume the address is `USDT_ADDRESS`. Now we try to interact with it.

## call[​](#call "Direct link to call")

Use call to execute a pure or view smart contract method. These methods do not modify the blockchain, do not cost anything to execute and are also not broadcasted to the network.
Assume we want to know the balance of `ACCOUNT_ADDRESS`, you can do it as follow:

```
let abi = [  
  {  
    'outputs': [{ 'type': 'uint256' }],  
    'constant': true,  
    'inputs': [{ 'name': 'who', 'type': 'address' }],  
    'name': 'balanceOf',  
    'stateMutability': 'View',  
    'type': 'Function'  
  },  
  {  
    'outputs': [{ 'type': 'bool' }],  
    'inputs': [  
      { 'name': '_to', 'type': 'address' },  
      { 'name': '_value', 'type': 'uint256' }  
    ],  
    'name': 'transfer',  
    'stateMutability': 'Nonpayable',  
    'type': 'Function'  
  }  
];  
let contract = await tronWeb.contract(abi, 'USDT_ADDRESS');  
let result = await contract.balanceOf('ACCOUNT_ADDRESS').call();  
console.log(result.toString(10));  
// result is big number, using toString method to convert it to string.
```

## send[​](#send "Direct link to send")

Use send to execute a non-pure or modify smart contract method on a given smart contract that modifies or changes values on the blockchain. These methods consume resources(bandwidth and energy) to perform as the changes need to be broadcasted out to the network.
Now we want to transfer some USDT(TRC20 token) to `ACCOUNT_ADDRESS`, we can use `transfer` method:

```
let abi = [...];  
let contract = await tronWeb.contract(abi, 'USDT_ADDRESS');  
let txID = await contract.transfer('ACCOUNT_ADDRESS', 100).send();  
// now you can visit web page https://nile.tronscan.org/#/transaction/${txID} to view the transaction detail.  
// or using code below:  
let result = await tronWeb.trx.getTransaction(txID);
```

> Not only can we use call & send, but we also can use triggerConstantContract & triggerSmartContract.

## triggerConstantContract[​](#triggerconstantcontract "Direct link to triggerConstantContract")

Trigger the read-only function of the contract ( they are the contract function which decorated by the pure and view modifiers), the query result is a non-solidified state.
Now we use another way to query the balance of `ACCOUNT_ADDRESS`:

```
const functionSelector = 'balanceOf(address)';  
const parameter = [{ type: 'address', value: 'ACCOUNT_ADDRESS' }]  
const result = await tronWeb.transactionBuilder.triggerConstantContract('USDT_ADDRESS', functionSelector, {}, parameter);  
  
// result is as below. We can see the constant_result returns the correct balance value of ACCOUNT_ADDRESS  
{  
  "result": {  
    "result": true  
  },  
  "energy_used": 935,  
  "constant_result": [  
    "0000000000000000000000000000000000000000000000000000000000000064"  
  ],  
  "transaction": {  
    "ret": [  
      {}  
    ],  
    "visible": false,  
    "txID": "a1c6d9b7d3c6cf8485fa1fff023a377123ab0d5285b4bc410ac1f017572fc5c9",  
    "raw_data": {  
      "contract": [  
        {  
          "parameter": {  
            "value": {  
              "data": "70a08231000000000000000000000000526f3626eaccc3f5fadd8f5f51fd9c49ce53b090",  
              "owner_address": "4175f09e51f8ecb695a0be1701581ec9493b164495",  
              "contract_address": "41eca9bc828a3005b9a3b909f2cc5c2a54794de05f"  
            },  
            "type_url": "type.googleapis.com/protocol.TriggerSmartContract"  
          },  
          "type": "TriggerSmartContract"  
        }  
      ],  
      "ref_block_bytes": "39c0",  
      "ref_block_hash": "20db92bea2aa0929",  
      "expiration": 1677062004000,  
      "timestamp": 1677061945989  
    },  
    "raw_data_hex": "0a0239c0220820db92bea2aa092940a0babdc5e7305a8e01081f1289010a31747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e54726967676572536d617274436f6e747261637412540a154175f09e51f8ecb695a0be1701581ec9493b164495121541eca9bc828a3005b9a3b909f2cc5c2a54794de05f222470a08231000000000000000000000000526f3626eaccc3f5fadd8f5f51fd9c49ce53b0907085f5b9c5e730"  
  }  
}
```

## triggerSmartContract[​](#triggersmartcontract "Direct link to triggerSmartContract")

It returns TransactionExtension, which contains the unsigned Transaction.
Now we use triggerSmartContract to rewrite `transfer`:

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

We now check out the balance of `ACCOUNT_ADDRESS`, it would be 200.

## abiV2[​](#abiv2 "Direct link to abiV2")

TronWeb has supported abiV2, so you can use TronWeb to interact with contract that contains tuple.
Here is the example.

The smart contract is:

```
pragma experimental ABIEncoderV2;  
  
  
contract Test {  
  struct Struct47985BF5FB {  
    address a;  
    trcToken b;  
    address c;  
  }  
  mapping (uint256 => Struct47985BF5FB) public s;  
  
  function setStruct(Struct47985BF5FB calldata _s)  public {  
    s[0] = Struct47985BF5FB(_s.a,_s.b,_s.c);  
  }  
  
  function get() public view returns(Struct47985BF5FB memory s2){  
      s2 = s[0];  
  }  
  
}
```

### Live code editor[​](#live-code-editor "Direct link to Live code editor")

**Note**:

* Do not expose your real private key here, use private key for testing instead.
* To run this code, you need to provide a private key that have TRX in Nile test network.
* To get TRX from nile faucet, use this [link](https://nileex.io/join/getJoinPage)

index.ts

```
import { TronWeb } from 'tronweb';
const tronWeb = new TronWeb({
  fullHost: 'https://api.nileex.io',
  // You need to set test private key here.
  // Don't use your real private key in test!
  privateKey: '',
});

// First, deploy it and wait for broadcasting:
const funcABIV2_4 = {
  abi: [
    {
      'inputs': [],
      'name': 'get',
      'outputs': [
        {
          'components': [
            {
              'internalType': 'address',
              'name': 'a',
              'type': 'address'
            },
            {
              'internalType': 'trcToken',
              'name': 'b',
              'type': 'trcToken'
            },
            {
              'internalType': 'address',
              'name': 'c',
              'type': 'address'
            }
          ],
          'internalType': 'struct Test.Struct47985BF5FB',
          'name': 's2',
          'type': 'tuple'
        }
      ],
      'stateMutability': 'view',
      'type': 'function'
    },
    {
      'inputs': [
        {
          'internalType': 'uint256',
          'name': '',
          'type': 'uint256'
        }
      ],
      'name': 's',
      'outputs': [
        {
          'internalType': 'address',
          'name': 'a',
          'type': 'address'
        },
        {
          'internalType': 'trcToken',
          'name': 'b',
          'type': 'trcToken'
        },
        {
          'internalType': 'address',
          'name': 'c',
          'type': 'address'
        }
      ],
      'stateMutability': 'view',
      'type': 'function'
    },
    {
      'inputs': [
        {
          'components': [
            {
              'internalType': 'address',
              'name': 'a',
              'type': 'address'
            },
            {
              'internalType': 'trcToken',
              'name': 'b',
              'type': 'trcToken'
            },
            {
              'internalType': 'address',
              'name': 'c',
              'type': 'address'
            }
          ],
          'internalType': 'struct Test.Struct47985BF5FB',
          'name': '_s',
          'type': 'tuple'
        }
      ],
      'name': 'setStruct',
      'outputs': [],
      'stateMutability': 'nonpayable',
      'type': 'function'
    }
  ],
  bytecode:
    '0x608060405234801561001057600080fd5b50d3801561001d57600080fd5b50d2801561002a57600080fd5b506106028061003a6000396000f3fe608060405234801561001057600080fd5b50d3801561001d57600080fd5b50d2801561002a57600080fd5b506004361061005b5760003560e01c806352efd685146100605780635aeccbe6146100925780636d4ce63c146100ae575b600080fd5b61007a60048036038101906100759190610430565b6100cc565b604051610089939291906104db565b60405180910390f35b6100ac60048036038101906100a79190610403565b610136565b005b6100b6610255565b6040516100c39190610512565b60405180910390f35b60006020528060005260406000206000915090508060000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16908060010154908060020160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905083565b604051806060016040528082600001602081019061015491906103d6565b73ffffffffffffffffffffffffffffffffffffffff1681526020018260200135815260200182604001602081019061018c91906103d6565b73ffffffffffffffffffffffffffffffffffffffff1681525060008080815260200190815260200160002060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506020820151816001015560408201518160020160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555090505050565b61025d610335565b6000808081526020019081526020016000206040518060600160405290816000820160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001600182015481526020016002820160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681525050905090565b6040518060600160405280600073ffffffffffffffffffffffffffffffffffffffff16815260200160008152602001600073ffffffffffffffffffffffffffffffffffffffff1681525090565b6000813590506103918161059e565b61039a8161052d565b905092915050565b6000606082840312156103b8576103b7610594565b5b81905092915050565b6000813590506103d0816105b5565b92915050565b6000602082840312156103ec576103eb610599565b5b60006103fa84828501610382565b91505092915050565b60006060828403121561041957610418610599565b5b6000610427848285016103a2565b91505092915050565b60006020828403121561044657610445610599565b5b6000610454848285016103c1565b91505092915050565b6104668161052d565b82525050565b6104758161052d565b82525050565b606082016000820151610491600085018261045d565b5060208201516104a460208501826104bd565b5060408201516104b7604085018261045d565b50505050565b6104c68161053f565b82525050565b6104d58161053f565b82525050565b60006060820190506104f0600083018661046c565b6104fd60208301856104cc565b61050a604083018461046c565b949350505050565b6000606082019050610527600083018461047b565b92915050565b600061053882610549565b9050919050565b6000819050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b600074ffffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b600080fd5b600080fd5b6105a781610569565b81146105b257600080fd5b50565b6105be8161058a565b81146105c957600080fd5b5056fea26474726f6e5822122003e6f6fe8adb4a16e48e773436d2d36d3bcf3d16227953199ec68896e85b82b264736f6c63430008060033'
};
(async () => {
  const transaction = await tronWeb.transactionBuilder.createSmartContract({
    abi: funcABIV2_4.abi,
    bytecode: funcABIV2_4.bytecode
  });
  await tronWeb.trx.sendRawTransaction(await tronWeb.trx.sign(transaction));
  while (true) {
    const tx = await tronWeb.trx.getTransaction(transaction.txID);
    if (Object.keys(tx).length === 0) {
      await new Promise(r => setTimeout(r, 3000));
      continue;
    } else {
      break;
    }
  }
  const deployed = await tronWeb.contract(funcABIV2_4.abi, transaction.contract_address);

  // Then, set tuple data. Note here we describe tuple as array. You have to set values from top to bottom of the structure of Struct47985BF5FB. Because this method change data on chain, we also have to wait for broadcasting.

  let txID = await deployed
    .setStruct(['TPL66VK2gCXNCD7EJg9pgJRfqcRazjhUZY', 1000100, 'TPL66VK2gCXNCD7EJg9pgJRfqcRazjhUZY'])
    .send();
  while (true) {
    const tx = await tronWeb.trx.getTransaction(txID);
    if (Object.keys(tx).length === 0) {
      await new Promise(r => setTimeout(r, 3000));
      continue;
    } else {
      console.log(tx);
      break;
    }
  }

  // Finally, checkout the 0 item of the map:
  let result = await deployed.s(0).call();
  console.log(result);
  // The output addresses are the hex format of the addresses provided.
})();
```

Output:

Clean

## estimateEnergy[​](#estimateenergy "Direct link to estimateEnergy")

If you want to know the cost to trigger a smart contract, you can use this method. It takes the same arguments as `triggerSmartContract` except the feeLimit parameter, but the result could not be the same as the real cost. See the example below:

```
const functionSelector = 'transfer(address,uint256)';  
const parameter = [{type:'address',value:'ACCOUNT_ADDRESS'},{type:'uint256',value:100}]  
const result = await tronWeb.transactionBuilder.estimateEnergy('USDT_ADDRESS', functionSelector, {}, parameter);  
// the result looks like below:  
{  
  "result": {  
    "result": true  
  },  
  "energy_required": 16482  
}
```

## TriggerSmartContractOptions[​](#triggersmartcontractoptions "Direct link to TriggerSmartContractOptions")

The options for trigger contract is defined as `TriggerSmartContractOptions`:

```
interface TriggerSmartContractOptions {  
  /**  
   * The maximum TRX burns for resource consumption in SUN（1TRX = 1,000,000SUN）.  
   */  
  feeLimit?: number;  
  /**  
   * The TRX transfer to the contract for each call in SUN（1TRX = 1,000,000SUN）  
   */  
  callValue?: number;  
  /**  
   * The id of trc10 token transfer to the contract (Optional)  
   */  
  tokenId?: string;  
  /**  
   * The amount of trc10 token transfer to the contract for each call (Optional)  
   */  
  tokenValue?: number;  
  /**  
   * JSON format for contract function.  
   * For example: `{ "type":"function", "inputs": [{"name":"a","type":"uint256"}], "name":"foo", "outputs": [] }`.  
   * If exists, the `parameters` will be ignored.  
   * Optional.  
   */  
  funcABIV2?: AbiFragment;  
  /**  
   * The parameters of the function specified by `funcABIV2`.  
   * Required if `funcABIV2` exists.  
   */  
  parametersV2?: unknown[];  
  /**  
   * Raw parameters encoded according to [ABI Specification](https://docs.soliditylang.org/en/latest/abi-spec.html).  
   * If exists, the `parametersV2` and `parameters` will be ignored.  
   * For example: 0x0000000000000000000000000000000000000000000000000000000000000001.  
   * Optional.  
   */  
  shieldedParameter?: string;  
  /**  
   * Alias of `shieldedParameter`. If exists, the `shieldedParameter`, `parametersV2` and `parameters` will be ignored.  
   */  
  rawParameter?: string;  
  /**  
   * If `functionSelector` is not specified, this parameter will be used as data.  
   */  
  input?: string;  
  /**  
   * Create transaction locally.  
   */  
  txLocal?: boolean;  
  /**  
   * For multi-signature use.  
   * Optional.  
   */  
  permissionId?: number;  
  blockHeader?: {  
    ref_block_bytes: string;  
    ref_block_hash: string;  
    expiration: number;  
    timestamp: number;  
  };  
  _isConstant?: boolean;  
  /**  
   * If use solidity node to trigger smart contract.  
   */  
  confirmed?: boolean;  
}
```