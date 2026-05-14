

JUMP TO

Powered by

# GetPaginatedNowWitnessList

get

https://api.shasta.trongrid.io/walletsolidity/getpaginatednowwitnesslist

This API retrieves the real-time vote counts of all Super Representatives (SRs) in the current epoch, sorted in descending order, and returns a paginated list within the specified range.

Recent Requests

Log in to see full request history

| Time | Status | User Agent |  |
| --- | --- | --- | --- |
| Retrieving recent requests… | | | |

LoadingLoading…

Query Params

offset

int64

required

The starting position of the returned results, which must be greater than or equal to 0. For example, when offset is set to `5` and limit is set to `10`, the API returns 10 Super Representatives (SRs) starting from the 6th position in the list sorted by vote count in descending order.

limit

int64

required

The number of results to return, which must be greater than 0 and cannot exceed 1000. For example: `10`

visible

boolean

Set to `true` to format addresses in Base58; set to `false` for hex format. (Default: false)

truefalse

Response

200

Updated 2 months ago

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

Click `Try It!` to start a request and see the response here!

Updated 2 months ago

---