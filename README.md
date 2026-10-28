# Presearch Search API client

This archived repository contains experimental Python and Node.js clients for a historical Presearch search endpoint. It is not a verified or production-ready service.

**Current status:** on 2026-10-28, an unauthenticated request to the configured endpoint returned HTTP 530. This does not establish whether an authenticated request would work. Confirm the current endpoint, terms, and availability with Presearch before configuring a real API key or relying on results. No live authenticated request was performed in this maintenance pass.

## Requirements and setup

- Node.js 18 or newer for the Node client and its tests.
- Python 3.7 or newer and `requests` for the Python client.
- A Presearch Search API key if the service and endpoint are confirmed by the provider.

```bash
python3 -m pip install -r requirements.txt
export PRESEARCH_API_KEY="your-key"
python3 presearch_python.py "example query"
node presearch_nodejs.js "example query"
```

Both clients send the query and supplied parameters to the configured remote service, with the key in an Authorization header. Do not include sensitive information in searches without reviewing the provider's current privacy terms. The default `ip` parameter is `127.0.0.1`; do not assume it represents a user's actual location.

The clients return an error on HTTP 429 instead of retrying indefinitely. Python uses connect/read timeouts and rejects redirects; Node uses a socket inactivity timeout. Callers should handle errors and choose any retries according to the provider's current limits.

## Offline checks

```bash
npm test
python3 -m unittest discover -s tests -p 'test_*.py'
```

The tests use fake HTTP responses and do not validate the live endpoint, authentication, results, provider privacy, pricing, or service availability. See [Presearch's documentation](https://docs.presearch.io/) for current information. The example response format and endpoint are historical and may have changed.

MIT licensed; see [LICENSE](LICENSE).
