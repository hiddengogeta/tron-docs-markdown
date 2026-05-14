

# FAQ

## Exit codes

| Code | Meaning | Suggested handling |
| --- | --- | --- |
| 0 | Success | Continue. |
| 1 | Unknown command or runtime error (including non-JSON API bodies) | Stop and show the error. |
| 2 | Invalid argument or missing API Key | Fix command arguments or run `ts setup`. |
| 3 | Network request failed | Check network connectivity and retry later. |
| 4 | HTTP/API request failed | Check API Key, endpoint, parameters, or rate limits. |

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `未找到 API Key` | Run `ts setup YOUR_API_KEY` or set `TRONSCAN_API_KEY` in the environment. |
| HTTP 401/403 | Check whether the API Key is valid. |
| HTTP 429 | Reduce request rate and retry later. |
| HTTP 404 | Check the command arguments or API path. |
| Network request failed | Check local network connectivity. |