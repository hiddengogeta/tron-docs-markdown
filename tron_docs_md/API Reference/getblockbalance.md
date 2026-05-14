

JUMP TO

Powered by

# GetBlockBalance

post

https://api.shasta.trongrid.io/wallet/getblockbalance

Get all balance change operations in a block.(Note: At present, the interface data can only be queried through the following official nodes 13.228.119.63 & 18.139.193.235&18.141.79.38 &18.139.248.26)

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

LoadingLoading…

Body Params

hash

string

required

Block hash (ID). Example: `0000000003dba95c7f05cedf1ba32cd64b6baa082a7870f533b4451703e432ab`

number

int32

required

Block number. The block hash and block number must be consistent, referring to the same block. Example: `64727388`

visible

boolean

Set to `true` to format addresses in Base58; set to `false` for hex format. (Default: `false`)

truefalse

Responses

# 200 200

# 400 400

Updated about 1 month ago

---

Language

ShellNodeRubyPHPPython

Credentials

Header

Header

```
LoadingLoading…
```

Response

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200 - Result400 - Result

Updated about 1 month ago

---