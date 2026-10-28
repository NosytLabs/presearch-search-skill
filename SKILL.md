---
name: presearch-search
description: Experimental archived clients for a historical Presearch search endpoint; live availability is unverified.
version: "1.0.0"
env:
  - PRESEARCH_API_KEY
primary_env: PRESEARCH_API_KEY
---

# Presearch Search API Skill

This repository is archived. An unauthenticated request to the configured endpoint returned HTTP 530 on 2026-10-28; authenticated access has not been verified. Confirm the current endpoint and provider terms before using a real key. Do not present this client as production-ready or claim that its results are live without a successful verified request.

The Python and Node clients send search queries and parameters to a remote service. Review the provider's current privacy terms before sending sensitive information.

```bash
python3 presearch_python.py "example query"
node presearch_nodejs.js "example query"
```

See [README.md](README.md) for requirements, offline checks, timeout behavior, and limitations.
