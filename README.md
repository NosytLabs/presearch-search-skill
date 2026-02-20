# Presearch Skill.md

[![Presearch](https://assets.presearch.com/referral/ban-5.jpg)](https://presearch.com/signup?rid=4779685)

**Production-ready decentralized search for AI agents.** Privacy-first, uncensored web search via a distributed node infrastructure.

## 🚀 Why Presearch?

Presearch is a decentralized search engine that respects your privacy. Unlike traditional search engines, Presearch:

-   **🚫 No Tracking**: Does not store your search history or IP address.
-   **🔓 Uncensored**: Results are not filtered or biased by corporate agendas.
-   **🌍 Decentralized**: Powered by a community of thousands of nodes running on independent hardware.
-   **🛡️ Encrypted**: All search traffic is end-to-end encrypted.

## 📋 API Overview

-   **Endpoint**: `https://na-us-1.presearch.com/v1/search`
-   **Method**: `GET`
-   **Auth**: Bearer Token
-   **Docs**: [Official Documentation](https://presearch.io/searchapi)

## 🔑 How to Get an API Key

1.  **Sign Up**: Create a free account using this [Referral Link](https://presearch.com/signup?rid=4779685).
2.  **Request Access**: Send an email to `collaborate@presearch.com` requesting API access for your account.
3.  **Generate Key**: Once approved, navigate to your dashboard to generate your API key.

## 💰 Pricing & Rate Limits

| Plan | Queries / Second | Queries / Month | Cost |
| :--- | :--- | :--- | :--- |
| **Free** | 1 QPS | 2,500 | $0 |
| **P1** | 30 QPS | 5,000 | Paid |
| **P2** | 60 QPS | 5,000 | Paid |
| **Enterprise** | Unlimited | Unlimited | Custom |

> **Note**: This skill implementation includes built-in rate limiting and exponential backoff to handle the Free tier's 1 QPS limit gracefully.

## 🔧 Implementation Examples

### Python
```python
import os
from presearch_python import PresearchSkill

api_key = os.getenv("PRESEARCH_API_KEY")
with PresearchSkill(api_key=api_key) as skill:
    results = skill.search("decentralized AI", lang="en-US", time_filter="week")
    for result in results.results:
        print(f"{result.title}: {result.link}")
```

### Node.js
```javascript
import { PresearchSkill } from './presearch_nodejs.js';

const skill = new PresearchSkill(process.env.PRESEARCH_API_KEY);
const results = await skill.search({ 
  query: 'decentralized AI',
  lang: 'en-US',
  time: 'week'
});
console.log(results.results);
```

## 🤖 AI Agent Integration

This repository adheres to the **SKILL.md** standard, making it instantly usable by AI agents like Trae, Claude, and Cursor.

1.  **Context**: The agent reads `SKILL.md` to understand the API contract.
2.  **Auth**: It knows to use the `Authorization: Bearer <key>` header.
3.  **Constraints**: It respects the `100 requests/minute` (approx 1.6 QPS) guideline, with fallback logic for strict 1 QPS limits.
4.  **Error Handling**: It knows how to interpret `401`, `402`, and `429` errors.

## 📄 License

MIT License - Use freely in your AI agents and MCP servers.

---

[**Sign up for Presearch**](https://presearch.com/signup?rid=4779685) to start searching privately.