

# Advanced Security Settings

A guide on configuring advanced security settings for your TRONSCAN API Key.

## When are these settings needed?

Advanced security settings are generally implemented to protect API services from malicious attacks or misuse. They may be required in the following cases:

### 1. Request Method Whitelist

This feature is recommended when you would like to allow only requests through trusted methods to use your API Key. API whitelisting can help prevent unauthorized access and malicious attacks.

### 2. User Agent Whitelist

This feature is recommended when you would like to restrict your API Key access to only a specific set of trusted User Agents. User Agent whitelisting can help safeguard your API Key against unauthorized access and malicious attacks.

### 3. Origin Header Whitelist

This feature is recommended when you would like to grant your API Key access to requests with particular Origin headers. Origin header whitelisting can effectively prevent cross-site request forgery (CSRF).

### 4. JWT

This mechanism helps authenticate users and allows only authenticated users to use your API Key.

Configuring advanced security settings is essential to protect your API Key from malicious attacks or misuse. However, advanced settings may increase the complexity of the API service, making it harder to manage. Evaluate different situations carefully and proceed with caution.

---

## Request Method Whitelist

When this feature is configured, only API requests using whitelisted methods will be accepted.

This feature helps secure the system against malicious attacks and unauthorized access by rejecting requests that use non-whitelisted HTTP methods.

---

## Origin Header Whitelist

The `Origin` header is an HTTP request header that specifies the origin of a request.

In cross-origin resource sharing (CORS), the `Origin` header is used to determine whether a request is allowed.

When the `Origin` header is used for CORS, it is recommended to also implement other security mechanisms — such as **CSRF tokens** and **CORS preflight requests** — to prevent malicious attacks and enhance overall system security.

---

## User Agent Whitelist

A request will be accepted if the `User-Agent` string it sends matches any entry on the whitelist.

Use this setting to restrict API Key usage to specific clients, browsers, or server environments you control.

---

## JWT

JSON Web Tokens (JWT) are used for authentication and authorization. JWT authentication enhances the security and scalability of the system by preventing specific attacks.

To use this feature, you must correctly configure the JWT options — including the **private key**, **algorithm**, and **expiration time**. Incorrect configurations may introduce security vulnerabilities.

### JWT Configuration Requirements

| Field | Location | Required Value |
| --- | --- | --- |
| `alg` | JWT Header | `RS256` |
| `typ` | JWT Header | `JWT` |
| `aud` | JWT Payload | `tronscan.org` |
| `kid` | JWT Header | The `kid` generated from your JWT public key |

The `kid` (Key ID) field in the JWT header must match the `kid` derived from the public key you registered. This links the token to the correct public key used for signature verification.