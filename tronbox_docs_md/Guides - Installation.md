

# Installation [​](#installation)

## Requirements [​](#requirements)

* Node.js >=20
* Windows, Linux or Mac OS X
* Docker Engine >=17

## Install Node.js [​](#install-node-js)

### Linux and macOS [​](#linux-and-macos)

Node Package Manager (npm) recommends installing Node.js with [Node Version Manager (nvm)](https://github.com/nvm-sh/nvm) to avoid permission errors when installing globally.

1. Use `curl` or `wget` to install `nvm`:

Terminal

shell

```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.2/install.sh | bash
```

Terminal

shell

```
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.2/install.sh | bash
```

2. Make sure nvm is properly installed. You may need to reload the terminal for the command to take effect.

Terminal

shell

```
nvm --version
```

3. Use nvm to install a compatible version of Node.js. For example, to install Node.js v20, run

Terminal

shell

```
nvm install 20
```

4. Run `node --version` to confirm that Node.js has been properly installed.

### Windows [​](#windows)

TronBox recommends using the installer from the website of Node.js.

Make sure that you agree to automatically install the necessary tools during installation so that the required Visual Studio build tools, Python, and Chocolately package manager can be installed.

![](/docs/windows-nodejs.png)

## Install TronBox [​](#install-tronbox)

You can install TronBox by executing the following command:

npmpnpmyarnbun

sh

```
npm install -g tronbox
```

sh

```
pnpm add -g tronbox
```

sh

```
yarn global add tronbox
```

sh

```
bun install -g tronbox
```

You may receive warnings during installation. Type tronbox version on the terminal to check whether TronBox has been properly installed.

Terminal

shell

```
tronbox version
```

## For Windows users [​](#for-windows-users)

If you are running TronBox on Windows, you may encounter naming conflicts that may prevent TronBox from executing properly. In this case, please see [Resolve naming conflicts on Windows](/docs/reference/configuration#resolve-naming-conflicts-on-windows) for any helpful information.