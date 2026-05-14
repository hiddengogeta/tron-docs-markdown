

* [References](/docu/docs/category/references)
* Provider Configuration
Version: 6.3.0

On this page

# Provider Configuration

TronWeb supports flexible node provider configuration for connecting to different TRON networks and custom nodes.

## Basic Configuration[​](#basic-configuration "Direct link to Basic Configuration")

### Using fullHost (Recommended)[​](#using-fullhost-recommended "Direct link to Using fullHost (Recommended)")

The simplest configuration — uses the same URL for all services:

```
import TronWeb from 'tronweb';  
  
const tronWeb = new TronWeb({  
    fullHost: 'https://api.trongrid.io',  
    headers: { 'TRON-PRO-API-KEY': 'your-api-key' },  
    privateKey: 'your-private-key',  
});
```

### Individual Node Configuration[​](#individual-node-configuration "Direct link to Individual Node Configuration")

Specify separate endpoints for each service:

```
const tronWeb = new TronWeb({  
    fullNode: 'https://api.trongrid.io',  
    solidityNode: 'https://api.trongrid.io',  
    eventServer: 'https://api.trongrid.io',  
    headers: { 'TRON-PRO-API-KEY': 'your-api-key' },  
    privateKey: 'your-private-key',  
});
```

## Network Endpoints[​](#network-endpoints "Direct link to Network Endpoints")

### Mainnet[​](#mainnet "Direct link to Mainnet")

| Provider | URL |
| --- | --- |
| TronGrid | `https://api.trongrid.io` |
| Custom node | Your self-hosted Full Node URL |

### Nile Testnet[​](#nile-testnet "Direct link to Nile Testnet")

| Provider | URL |
| --- | --- |
| TronGrid Nile | `https://nile.trongrid.io` |

### Shasta Testnet[​](#shasta-testnet "Direct link to Shasta Testnet")

| Provider | URL |
| --- | --- |
| TronGrid Shasta | `https://api.shasta.trongrid.io` |

## Node Types[​](#node-types "Direct link to Node Types")

| Node Type | Property | Purpose |
| --- | --- | --- |
| **Full Node** | `fullNode` | Latest (unconfirmed) blockchain state, broadcasting transactions |
| **Solidity Node** | `solidityNode` | Confirmed (solidified) blockchain state only |
| **Event Server** | `eventServer` | Smart contract event queries |

## Changing Providers at Runtime[​](#changing-providers-at-runtime "Direct link to Changing Providers at Runtime")

```
// Change full node  
tronWeb.setFullNode('https://new-fullnode.example.com');  
  
// Change solidity node  
tronWeb.setSolidityNode('https://new-soliditynode.example.com');  
  
// Change event server  
tronWeb.setEventServer('https://new-eventserver.example.com');  
  
// Change custom headers  
tronWeb.setHeader({ 'TRON-PRO-API-KEY': 'new-api-key' });
```

## Custom Headers[​](#custom-headers "Direct link to Custom Headers")

Headers are attached to every HTTP request. Use them for API keys and custom metadata:

```
const tronWeb = new TronWeb({  
    fullHost: 'https://api.trongrid.io',  
    headers: {  
        'TRON-PRO-API-KEY': 'your-api-key',  
        'Custom-Header': 'value',  
    },  
});
```

## Using with TronLink[​](#using-with-tronlink "Direct link to Using with TronLink")

You can retrieve the connected wallet address and TronWeb instance via the TIP-6963 protocol:

```
window.addEventListener("TIP6963:announceProvider", async (e) => {  
    // Check if the announced provider is TronLink  
    if (e.detail.info && e.detail.info.name === "TronLink") {  
        console.log("You have TronLink installed!");  
        const tron = e.detail.provider;  
        const addresses = await tron.request({  
            method: 'eth_requestAccounts',  
        });  
        console.log("Your address: ", addresses[0]);  
        const tronWeb = tron.tronWeb;  
    }  
});  
  
// Request all TIP-6963 wallets to announce themselves  
window.dispatchEvent(new Event("TIP6963:requestProvider"));
```

## Multiple TronWeb Instances[​](#multiple-tronweb-instances "Direct link to Multiple TronWeb Instances")

You can create multiple instances for different networks:

```
// Mainnet instance  
const mainnet = new TronWeb({ fullHost: 'https://api.trongrid.io' });  
  
// Testnet instance  
const testnet = new TronWeb({ fullHost: 'https://nile.trongrid.io' });  
  
// Use both  
const mainBalance = await mainnet.trx.getBalance(address);  
const testBalance = await testnet.trx.getBalance(address);
```

## TronGrid API Keys[​](#trongrid-api-keys "Direct link to TronGrid API Keys")

[TronGrid](https://www.trongrid.io/) provides free API access with rate limits. For production use, register for an API key:

1. Visit [trongrid.io](https://www.trongrid.io/) and create an account
2. Create an API key in the dashboard
3. Add the key to your TronWeb configuration:

```
const tronWeb = new TronWeb({  
    fullHost: 'https://api.trongrid.io',  
    headers: { 'TRON-PRO-API-KEY': 'your-api-key' },  
});
```

| Plan | Rate Limit | Notes |
| --- | --- | --- |
| Free | Limited QPS | Sufficient for development |
| Pro | Higher QPS | For production applications |