---
name: "presearch-search"
description: "Production-ready decentralized search for AI agents. Privacy-first, uncensored web search via distributed node infrastructure. No tracking, no profiling."
env:
  - PRESEARCH_API_KEY
primary_env: PRESEARCH_API_KEY
---

# Presearch Search API Skill

Enable AI agents to perform real-time decentralized web searches using Presearch. This skill provides a simple, reliable interface for retrieving live internet results, allowing agents to access current information beyond their training data.

## 🚀 Features
- **Real-time**: Access current world information.
- **Privacy-first**: No tracking, no logging, no profiling.
- **Decentralized**: Powered by community nodes.
- **Agent-optimized**: Clean JSON responses.

## 🛠️ Usage

### Python
```bash
python3 presearch_python.py "latest AI news"
```

### Node.js
```bash
node presearch_nodejs.js "decentralized search"
```

## ⚙️ Configuration

| Variable | Description | Required |
| :--- | :--- | :--- |
| `PRESEARCH_API_KEY` | Your API Key from [presearch.com](https://presearch.com/signup?rid=4779685) | ✅ |

## 📡 API Specification

**Endpoint:** `https://na-us-1.presearch.com/v1/search`  
**Method:** `GET`  
**Auth:** Bearer Token via `PRESEARCH_API_KEY`

### Parameters

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `q` | string | ✅ | - | Search query (URL encoded) |
| `ip` | string | ✅ | 127.0.0.1 | User IP (required by API, safe to mock) |
| `lang` | string | ❌ | en-US | Language code (e.g., `en-US`, `de-DE`) |
| `time` | string | ❌ | any | `any`, `day`, `week`, `month`, `year` |
| `page` | string | ❌ | 1 | Page number (1-100) |
| `safe` | string | ❌ | 1 | `1` (strict), `0` (off) |

### Response Format
```json
{
  "data": {
    "standardResults": [
      {
        "title": "Example Page",
        "link": "https://example.com",
        "description": "Description of the result..."
      }
    ],
    "pagination": {
      "current_page": 1,
      "has_next": true
    }
  }
}
```

## ⚡ Rate Limits
- **Free Tier**: 1 query/second (60/min).
- **Paid Tiers**: Up to 60+ queries/second.
- **Note**: This skill implements exponential backoff for `429` errors.

## 🧪 Example Prompts
- "Search for latest advancements in autonomous AI agents"
- "Search for official documentation for FastAPI"
- "Search for solutions to Python ModuleNotFoundError"
- "Search for trending SaaS startup ideas in 2026"
- "Search for latest Solana ecosystem projects"

## 📜 License
MIT License
