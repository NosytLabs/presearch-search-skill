---
name: "presearch-search"
description: "Production-ready decentralized search for AI agents. Privacy-first, uncensored web search via distributed node infrastructure. No tracking, no profiling."
---

# Presearch Search API

**Endpoint:** `https://na-us-1.presearch.com/v1/search`  
**Method:** GET  
**Auth:** Bearer Token  
**Docs:** [https://presearch.io/searchapi](https://presearch.io/searchapi)

## 🚀 Getting Started
To get an API key:
1.  **Sign Up**: Create an account via [Referral Link](https://presearch.com/signup?rid=4779685)
2.  **Request Access**: Email `collaborate@presearch.com` to enable API access.
3.  **Dashboard**: Generate your key in the user dashboard.

## ⚡ Rate Limits & Plans

| Plan | Queries / Second | Queries / Month | Cost |
| :--- | :--- | :--- | :--- |
| **Free** | 1 QPS | 2,500 | $0 |
| **P1** | 30 QPS | 5,000 | Paid |
| **P2** | 60 QPS | 5,000 | Paid |
| **Enterprise** | Unlimited | Unlimited | Custom |

> **Note for Agents:** By default, assume the **Free Plan** (1 request/second) unless configured otherwise. Implement exponential backoff for `429 Too Many Requests`.

## Authentication
```http
Authorization: Bearer YOUR_API_KEY_HERE
```

## Parameters

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `q` | string | ✅ | - | Search query (URL encoded) |
| `lang` | string | ❌ | en-US | Language code (e.g., `en-US`, `de-DE`) |
| `time` | string | ❌ | any | `any`, `day`, `week`, `month`, `year` |
| `page` | string | ❌ | 1 | Page number for pagination |
| `safe` | string | ❌ | 1 | `1` (strict), `0` (off) |

## Response Schema
```json
{
  "data": {
    "standardResults": [
      {
        "title": "Page Title",
        "link": "https://example.com/page",
        "description": "A brief summary of the page content...",
        "favicon": "https://example.com/favicon.ico"
      }
    ],
    "pagination": {
      "current_page": 1,
      "has_next": true
    }
  }
}
```

## Error Codes
- **401 Unauthorized**: Invalid API key. Check your Bearer token.
- **402 Payment Required**: Plan limit reached or credits exhausted.
- **422 Unprocessable Entity**: Invalid parameters (e.g., missing `q`).
- **429 Too Many Requests**: Rate limit exceeded ( > 1 req/sec for Free tier).
- **5xx Server Error**: Presearch node network issue. Retry with backoff.

## Usage Examples

### Python
```python
import requests
import time

def search_presearch(query, api_key):
    url = "https://na-us-1.presearch.com/v1/search"
    headers = {"Authorization": f"Bearer {api_key}"}
    params = {"q": query}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 429:
            time.sleep(1) # Backoff for rate limit
            return search_presearch(query, api_key)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}
```

### Node.js
```javascript
async function searchPresearch(query, apiKey) {
  const url = `https://na-us-1.presearch.com/v1/search?q=${encodeURIComponent(query)}`;
  const response = await fetch(url, {
    headers: { 'Authorization': `Bearer ${apiKey}` }
  });
  
  if (response.status === 429) {
    await new Promise(r => setTimeout(r, 1000));
    return searchPresearch(query, apiKey);
  }
  
  return await response.json();
}
```

## 🔒 Privacy & Decentralization
- **No Tracking**: Your IP address is removed; no search history is stored.
- **Uncensored**: Results are aggregated from a decentralized network of independent nodes.
- **Encrypted**: All traffic is SSL encrypted to protect against eavesdropping.
- **No Profiling**: Presearch does not build user profiles or retarget ads.