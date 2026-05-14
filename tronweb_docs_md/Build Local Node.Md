

* Build a local node
Version: 6.3.0

On this page

# Build a local node

This guide will help you set up a local node. By using a local node, you don’t need to connect to any testnet, which provides a faster development and testing experience.

## Build[​](#build "Direct link to Build")

### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Docker

> Please go to [Docker official site](https://docs.docker.com/get-started/get-docker/) to download and install it.

### Run tronbox/tre[​](#run-tronboxtre "Direct link to Run tronbox/tre")

1. Run docker.
2. Run `docker pull tronbox/tre` in command line tools.
3. Run `docker run -it -p 9090:9090 --rm --name tron tronbox/tre` in command line tools.

> For more information about tronbox/tre, please go to <https://hub.docker.com/r/tronbox/tre>.

## Test[​](#test "Direct link to Test")

### Steps[​](#steps "Direct link to Steps")

1. Open your editor, then run `npm install tronweb` to install TronWeb.
2. Edit your js file, then add the following code:

```
import { TronWeb } from 'tronweb';  
const tronWeb = new TronWeb({  
  fullHost: 'http://127.0.0.1:9090',  
  privateKey: 'your private key',  
});
```

3. Add any code about TronWeb.
4. Run `node yourFile.js` to test it.

## Test TronWeb Source Code[​](#test-tronweb-source-code "Direct link to Test TronWeb Source Code")

If you want to test TronWeb source code, you can run TronWeb unit test cases in the following way:

1. Git pull TronWeb source code.
2. Run `npm install` to install dependencies.
3. Run `PRIVATE_KEY=your_private_key npm run test` to run unit test cases.

**Note:**
Please replace `your_private_key` with your private key which is valid in the docker. You can set it as one of the Private Key that is printed in the start of docker's log panel.