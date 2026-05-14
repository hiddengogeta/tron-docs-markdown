

* [API List](/docu/docs/API List/)
* utils
* address
Version: 6.3.0

On this page

# address [<src>](https://github.com/tronprotocol/tronweb/blob/v6.3.0/src/tronweb.ts#L271)

Object that allows you to convert between hex / base58 and privatekey representations of a TRON address.

**Note**:
If you wish to convert generic data to hexadecimal strings, please use the function `TronWeb.toHex`.

## 1. TronWeb.address.toHex[​](#1-tronwebaddresstohex "Direct link to 1. TronWeb.address.toHex")

Convert Base58 format address to Hex format address.

**Usage**

```
TronWeb.address.toHex('base58 format address');
```

**Parameters**

string - Base58 format address

**Returns**

string - TRON Hex format address

**Example**

```
TronWeb.address.toHex('TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL');  
'418840E6C55B9ADA326D211D818C34A994AECED808'
```

## 2. TronWeb.address.fromHex[​](#2-tronwebaddressfromhex "Direct link to 2. TronWeb.address.fromHex")

Convert Hex format address to Base58 format address.

**Usage**

```
TronWeb.address.fromHex('hex format address');
```

**Parameters**

string - Hex format address

**Returns**

string - TRON Base58 format address

**Example**

```
TronWeb.address.fromHex('418840E6C55B9ADA326D211D818C34A994AECED808');  
'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL'
```

## 3. TronWeb.address.fromPrivateKey[​](#3-tronwebaddressfromprivatekey "Direct link to 3. TronWeb.address.fromPrivateKey")

Derive its corresponding address based on the provided private key.

**Usage**

```
TronWeb.address.fromPrivateKey('private key');
```

**Parameters**

string - private key without prefix `0x`

**Returns**

string - Base58 format address

**Example**

```
TronWeb.address.fromPrivateKey('AD71****7509');  
'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL'  
// The provided private key is not allowed to start with prefix `0x`, otherwise it will return false  
TronWeb.address.fromPrivateKey('0xAD71****7509');  
false
```

## 4. TronWeb.address.toChecksumAddress[​](#4-tronwebaddresstochecksumaddress "Direct link to 4. TronWeb.address.toChecksumAddress")

Convert a unchecksumed address to checksumed address.

**Usage**

```
TronWeb.address.toChecksumAddress('417e5f4552091a69125d5dfcb7b8c2659029395bdf');  
'417E5F4552091A69125d5DfCb7b8C2659029395Bdf'
```

**Parameters**

string - the unchecksumed address

**Returns**

string - the checksumed address

## 5. TronWeb.address.isChecksumAddress[​](#5-tronwebaddressischecksumaddress "Direct link to 5. TronWeb.address.isChecksumAddress")

Check if the input hex string is a checksumed address.

**Usage**

```
TronWeb.address.isChecksumAddress('417e5f4552091a69125d5dfcb7b8c2659029395bdf');  
false  
TronWeb.address.isChecksumAddress('417E5F4552091A69125d5DfCb7b8C2659029395Bdf');  
true
```

**Parameters**

string - the hex address

**Returns**

boolean - if it's checksumed address