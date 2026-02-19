# Presearch Skill.md

Production-ready decentralized search for AI agents. Privacy-first, uncensored web search via distributed node infrastructure.

## 🚀 What is This?

This is a **clean SKILL.md implementation** for the Presearch Search API. It's designed to work with AI agents, MCP servers, and any system that supports the SKILL.md standard.

- **No complex dependencies**
- **No bloated code**
- **Just the essential API documentation**
- **Ready for AI agent integration**

## 📋 API Overview

### Authentication
Get your API key from [presearch.com](https://presearch.com) dashboard.

```http
Authorization: Bearer YOUR_API_KEY_HERE
```

### Core Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `q` | string | ✅ | - | Search query |
| `lang` | string | ❌ | en-US | Language code |
| `time` | string | ❌ | any | any, day, week, month, year |
| `page` | string | ❌ | 1 | Page number |
| `safe` | string | ❌ | 1 | Safe search |

### Rate Limiting
- **100 requests per minute**
- Automatic retry with exponential backoff
- Built-in error handling for 429 responses

## 🔧 Implementation Examples

### Python (with Context Manager)
```python
import os
from presearch_python import PresearchSkill

api_key = os.getenv("PRESEARCH_API_KEY")
with PresearchSkill(api_key=api_key) as skill:
    results = skill.search("decentralized AI", lang="en-US", time_filter="week")
    for result in results.results:
        print(f"{result.title}: {result.link}")
```

### Node.js (Async/Await)
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

### For Trae / Claude / Cursor Users

This repository provides a **clean SKILL.md file** that teaches AI agents how to:

1. **Authenticate** with Bearer tokens
2. **Search** with proper parameter formatting
3. **Handle errors** gracefully (401, 402, 422, 429)
4. **Respect rate limits** (100 req/min)
5. **Parse responses** correctly

### MCP Server Integration

```python
# Example MCP tool definition
def search_tool(query: str, lang: str = "en-US", time_filter: str = "any"):
    """Search the web using Presearch API"""
    with PresearchSkill(api_key=os.getenv("PRESEARCH_API_KEY")) as skill:
        return skill.search(query, lang=lang, time_filter=time_filter)
```

## 🔒 Privacy Features

- **No tracking** - Zero user profiling or data collection
- **Decentralized** - Powered by independent nodes worldwide
- **Encrypted** - All traffic uses HTTPS encryption
- **Uncensored** - Access information without restrictions

## 🎯 Error Handling

| Status | Error | Solution |
|--------|--------|----------|
| 401 | Invalid API key | Get key from [presearch.com](https://presearch.com) |
| 402 | Payment required | Add credits to your account |
| 422 | Invalid parameters | Check parameter format |
| 429 | Rate limit exceeded | Wait and retry (100 req/min) |

## 📚 Resources

- **[Presearch Website](https://presearch.com)** - Get your API key
- **[Presearch API Docs](https://presearch-search-api.readme.io)** - Full API reference
- **[Privacy Policy](https://presearch.com/privacy)** - Learn about privacy protections
- **[Node Network](https://presearch.com/nodes)** - Join the decentralized network

## 📄 License

MIT License - Use freely in your AI agents and MCP servers.

---

**Clean. Simple. Production-ready.** This is Presearch Skill.md.