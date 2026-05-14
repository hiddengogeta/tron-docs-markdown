

* [API List](/docu/docs/API List/)
* utils
* getCreate2Address
Version: 6.3.0

On this page

# getCreate2Address

Get the create2 address.

### Usage[​](#usage "Direct link to Usage")

```
TronWeb.utils.address.getCreate2Address(options)
```

### Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Description | Data Type |
| --- | --- | --- |
| options.from | The from address | string |
| options.salt | The salt | string | Uint8Array |
| options.initCode | The init code | string | Uint8Array |
| options.addressFormat | Optional, the address format. Default is base58. | 'hex' | 'base58' |

### Returns[​](#returns "Direct link to Returns")

string - the create2 address

Example

```
import { TronWeb } from 'tronweb';  
const create2Address = TronWeb.utils.address.getCreate2Address({  
    from: '411F4428123047f51a0e76a4B3f2DA904a7855208C',  
    salt: '0x8b0e2c2f2d68d6511892c7881e5e21ac528b18be0f55cedce98321cd4a562be5',  
    initCode: '0x6080604052348015600f57600080fd5b5060405160e338038060e38339818101604052810190602d9190604c565b80600081905550506097565b6000815190506046816083565b92915050565b600060208284031215605f57605e607e565b5b6000606b848285016039565b91505092915050565b6000819050919050565b600080fd5b608a816074565b8114609457600080fd5b50565b603f8060a46000396000f3fe6080604052600080fdfea2646970667358221220a32ca22663d59fb69eed5207435acdbbb7af0b9c8b4e7a096fddadb2ad231a5e64736f6c63430008070033537d6837290bb0b492c0f9b48db6c37c730d80ed549a3d8a34113f44009c47a2',  
});  
'TYeJXEmbomUcf9HYTe4mdedu7xgFq6Sbtn'
```