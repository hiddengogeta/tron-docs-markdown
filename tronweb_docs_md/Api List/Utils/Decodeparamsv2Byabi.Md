

* [API List](/docu/docs/API List/)
* utils
* abi.decodeParamsV2ByABI
Version: 6.3.0

On this page

# abi.decodeParamsV2ByABI [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/utils/abi.ts#L152)

This method supports decode output data of function's abi. Unlike decodeParams, it supports tuple type which is already supported by solidity in new versions. It can be seen as the reverse of [abi.encodeParamsV2ByABI](/docu/docs/API List/utils/encodeParamsV2ByABI).

### Usage[​](#usage "Direct link to Usage")

```
tronWeb.utils.abi.decodeParamsV2ByABI(funAbi, data);
```

### Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description | Data Type |
| --- | --- | --- |
| funAbi | The abi of a function | object contains outputs array |
| data | The output data | hex string |

### Returns[​](#returns "Direct link to Returns")

Array - The decoded data array.

### Example[​](#example "Direct link to Example")

```
const functionABI = {  
  "constant": true,  
  "inputs": [],  
  "name": "test",  
  "outputs": [  
    {  
      "name": "r0",  
      "type": "string[2]"  
    },  
    {  
      "name": "r1",  
      "type": "uint128"  
    },  
    {  
      "components": [  
        {  
          "name": "a",  
          "type": "bytes"  
        },  
        {  
          "name": "b",  
          "type": "bytes"  
        },  
        {  
          "name": "c",  
          "type": "bytes"  
        }  
      ],  
      "name": "r2",  
      "type": "tuple"  
    },  
    {  
      "name": "r3",  
      "type": "bytes"  
    }  
  ],  
  "payable": false,  
  "stateMutability": "pure",  
  "type": "function"  
};  
const data = '0x000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000ca07f722e5aead62dcccf1357800000000000000000000000000000000000000000000000000000000000003c000000000000000000000000000000000000000000000000000000000000005200000000000000000000000000000000000000000000000000000000000000040000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000001914c6f72656d20697073756d20646f6c6f722073697420616d65742c20636f6e73656374657475722061646970697363696e6720656c69742c2073656420646f20656975736d6f642074656d706f7220696e6369646964756e74207574206c61626f726520657420646f6c6f7265206d61676e6120616c697175612e20557420656e696d206164206d696e696d2076656e69616d2c2071756973206e6f737472756420657865726369746174696f6e20756c6c616d636f206c61626f726973206e69736920757420616c697175697020657820656120636f6d6d6f646f20636f6e7365717561742e2044756973206175746520697275726520646f6c6f7220696e20726570726568656e646572697420696e20766f6c7570746174652076656c697420657373652063696c6c756d20646f6c6f726520657520667567696174206e756c6c612070617269617475722e204578636570746575722073696e74206f6363616563617420637570696461746174206e6f6e2070726f6964656e742c2073756e7420696e2063756c70612071756920000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010c4c6f72656d20697073756d20646f6c6f722073697420616d65742c20636f6e73656374657475722061646970697363696e6720656c69742c2073656420646f20656975736d6f642074656d706f7220696e6369646964756e74207574206c61626f726520657420646f6c6f7265206d61676e6120616c697175612e20557420656e696d206164206d696e696d2076656e69616d2c2071756973206e6f737472756420657865726369746174696f6e20756c6c616d636f206c61626f726973206e69736920757420616c697175697020657820656120636f6d6d6f646f20636f6e7365717561742e2044756973206175746520697275726520646f6c6f7220696e20726570726568656e6465720000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000000a00000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000ac66a151d9b0763859a670000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000306e1a7e1a868b83dbbb0b9761f85b991f2ab73b5fef04476333b3fadd663d54b94e42a0354d479d0e5a9b44f7cd78bbcd000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000033f99eddc0917e7c94687bf18c77656aa414cfd8e9b5d0fb34e41b83ca0e1e91eecfe0fc28fe7ccc0244ebfcfd376ff63120c3c700000000000000000000000000000000000000000000000000000000000000000000000000000000000000001447666ad90c94e7cb655d9a68acc2d45451e5b94b000000000000000000000000';  
const result = tronWeb.utils.abi.decodeParamsV2ByABI(functionABI, data);  
[  
  [  
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui ',  
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehender'  
  ],  
  BigNumber {  
    _hex: '0xca07f722e5aead62dcccf13578',  
    _isBigNumber: true  
  },  
  [  
    '0xc66a151d9b0763859a67',  
    '0x6e1a7e1a868b83dbbb0b9761f85b991f2ab73b5fef04476333b3fadd663d54b94e42a0354d479d0e5a9b44f7cd78bbcd',  
    '0xf99eddc0917e7c94687bf18c77656aa414cfd8e9b5d0fb34e41b83ca0e1e91eecfe0fc28fe7ccc0244ebfcfd376ff63120c3c7',  
    a: '0xc66a151d9b0763859a67',  
    b: '0x6e1a7e1a868b83dbbb0b9761f85b991f2ab73b5fef04476333b3fadd663d54b94e42a0354d479d0e5a9b44f7cd78bbcd',  
    c: '0xf99eddc0917e7c94687bf18c77656aa414cfd8e9b5d0fb34e41b83ca0e1e91eecfe0fc28fe7ccc0244ebfcfd376ff63120c3c7'  
  ],  
  '0x47666ad90c94e7cb655d9a68acc2d45451e5b94b',  
  r0: [  
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui ',  
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehender'  
  ],  
  r1: BigNumber {  
    _hex: '0xca07f722e5aead62dcccf13578',  
    _isBigNumber: true  
  },  
  r2: [  
    '0xc66a151d9b0763859a67',  
    '0x6e1a7e1a868b83dbbb0b9761f85b991f2ab73b5fef04476333b3fadd663d54b94e42a0354d479d0e5a9b44f7cd78bbcd',  
    '0xf99eddc0917e7c94687bf18c77656aa414cfd8e9b5d0fb34e41b83ca0e1e91eecfe0fc28fe7ccc0244ebfcfd376ff63120c3c7',  
    a: '0xc66a151d9b0763859a67',  
    b: '0x6e1a7e1a868b83dbbb0b9761f85b991f2ab73b5fef04476333b3fadd663d54b94e42a0354d479d0e5a9b44f7cd78bbcd',  
    c: '0xf99eddc0917e7c94687bf18c77656aa414cfd8e9b5d0fb34e41b83ca0e1e91eecfe0fc28fe7ccc0244ebfcfd376ff63120c3c7'  
  ],  
  r3: '0x47666ad90c94e7cb655d9a68acc2d45451e5b94b'  
]
```