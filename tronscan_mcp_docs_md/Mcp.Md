

# User Guide

TronScan MCP Server is a TRON blockchain data query service based on the Model Context Protocol (MCP), providing **119 tool interfaces** covering blocks, accounts, contracts, transactions, tokens, SR, wallets, deep analysis, and other comprehensive on-chain data query capabilities.

## Quick Start

### MCP Service URL

| Environment | URL |
| --- | --- |
| Production | `https://mcp.tronscan.org/mcp` |

### Protocol

* **MCP Protocol Version**: 2025-06-18
* **Transport Protocol**: Streamable HTTP

---

## Client Configuration

### Claude Desktop

Edit the configuration file:

* **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
* **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```
{
  "mcpServers": {
    "tronscan": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://mcp.tronscan.org/mcp",
        "--transport",
        "http-only",
        "--header",
        "Content-Type: application/json",
        "--header",
        "Accept:application/json, text/event-stream"
      ]
    }
  }
}
```

To pass an API Key:

```
{
  "mcpServers": {
    "tronscan": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://mcp.tronscan.org/mcp",
        "--transport",
        "http-only",
        "--header",
        "TRON-PRO-API-KEY:<your-api-key>",
        "--header",
        "Content-Type: application/json",
        "--header",
        "Accept:application/json, text/event-stream"
      ]
    }
  }
}
```

### Claude Code

**Option 1: CLI Command**

```
claude mcp add --transport http tronscan https://mcp.tronscan.org/mcp
```

**Option 2: Project Configuration File**

Create `.mcp.json` in the project root directory:

```
{
  "mcpServers": {
    "tronscan": {
      "type": "http",
      "url": "https://mcp.tronscan.org/mcp"
    }
  }
}
```

### Generic HTTP Call

```
# 1. Initialize connection
curl -X POST https://mcp.tronscan.org/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "method": "initialize",
    "params": {
      "protocolVersion": "2025-06-18",
      "capabilities": {},
      "clientInfo": {"name": "my-client", "version": "1.0"}
    },
    "id": 1
  }'
 
# 2. Call a tool (include the returned mcp-session-id)
curl -X POST https://mcp.tronscan.org/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "mcp-session-id: <session-id>" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "getBlocks",
      "arguments": {"limit": 1, "sort": "-number"}
    },
    "id": 2
  }'
```

---

## API Key

* Pass via HTTP request header `TRON-PRO-API-KEY`
* Get an API Key: Register at <https://tronscan.org> and apply

---