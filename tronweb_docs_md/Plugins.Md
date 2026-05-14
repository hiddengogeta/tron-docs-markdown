

* Plugins
Version: 6.3.0

On this page

# Plugins

TronWeb provides a unique way to customize its behavior through the tronWeb.plugin method. With this method, you can modify how TronWeb works without changing its core code. In this section, we’ll introduce several ways to use it.

## 1. Create a plugin[​](#1-create-a-plugin "Direct link to 1. Create a plugin")

A plugin is a class whose constructor accepts a TronWeb instance as a parameter. It must also implement a pluginInterface method. The return value of this method must conform to the following interface:

```
interface PluginInterfaceReturn {  
    requires: string;  
    components?: Record<string | number | symbol, any>;  
    fullClass?: boolean;  
}
```

`requires` field specifies the version requirement of TronWeb according to the semver standard. If you set `fullClass` to `true`, it means the plugin should be mounted on the TronWeb **class** and the plugin instance should be mounted on the TronWeb **instance**. If you set `fullClass` to `false`, it means the methods that the `components` field specified should be mounted on each module of the TronWeb **instance**. Read the example below for more details.

1. `fullClass` is true

```
import { TronWeb } from 'tronweb';  
class MyPlugin1 {  
    tronWeb: TronWeb;  
    constructor(tronWeb: TronWeb) {  
        this.tronWeb = tronWeb;  
    }  
    pluginInterface() {  
        return {  
            requires: '>=6.0.0',  
            fullClass: true,  
        };  
    }  
    myPlugin1Method() {  
        console.log('MyPlugin1 method');  
    }  
}
```

2. `fullClass` is false

```
import { TronWeb } from 'tronweb';  
class MyPlugin2 {  
    tronWeb: TronWeb;  
    constructor(tronWeb: TronWeb) {  
        this.tronWeb = tronWeb;  
    }  
    pluginInterface() {  
        return {  
            requires: '>=6.0.0',  
            fullClass: false,  
            components: {  
                trx: {  
                    myPlugin2Method: this.myPlugin2Method,  
                },  
            },  
        };  
    }  
    myPlugin2Method() {  
        console.log('MyPlugin2 method');  
    }  
}
```

## 2. Register a plugin[​](#2-register-a-plugin "Direct link to 2. Register a plugin")

```
const tronWeb = new TronWeb({  
    fullHost: 'http://127.0.0.1:9090',  
});  
tronWeb.plugin.register(MyPlugin1);  
tronWeb.plugin.register(MyPlugin2);
```

## 3. Use a plugin[​](#3-use-a-plugin "Direct link to 3. Use a plugin")

```
tronWeb.myPlugin1.myPlugin1Method();  
tronWeb.trx.myPlugin2Method();
```

## Put it all together[​](#put-it-all-together "Direct link to Put it all together")

index.ts

```
import { TronWeb } from 'tronweb';
class MyPlugin1 {
    tronWeb: TronWeb;
    constructor(tronWeb: TronWeb) {
        this.tronWeb = tronWeb;
    }
    pluginInterface() {
        return {
            requires: '>=6.0.0',
            fullClass: true,
        };
    }
    myPlugin1Method() {
        console.log('MyPlugin1 method');
    }
}
class MyPlugin2 {
    tronWeb: TronWeb;
    constructor(tronWeb: TronWeb) {
        this.tronWeb = tronWeb;
    }
    pluginInterface() {
        return {
            requires: '>=6.0.0',
            fullClass: false,
            components: {
                trx: {
                    myPlugin2Method: this.myPlugin2Method,
                },
            },
        };
    }
    myPlugin2Method() {
        console.log('MyPlugin2 method');
    }
}
const tronWeb = new TronWeb({
    fullHost: 'http://127.0.0.1:9090',
});
tronWeb.plugin.register(MyPlugin1);
tronWeb.plugin.register(MyPlugin2);
tronWeb.myPlugin1.myPlugin1Method();
tronWeb.trx.myPlugin2Method();
```

Output:

Clean