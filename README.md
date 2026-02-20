# 🤖 Presearch Search API - Decentralized Web Search for AI Agents

[![Presearch](https://assets.presearch.com/referral/ban-5.jpg)](https://presearch.com/signup?rid=4779685)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/downloads/)
[![Node.js](https://img.shields.io/badge/Node.js-14%2B-green)](https://nodejs.org/)
[![Presearch API](https://img.shields.io/badge/API-Presearch-orange)](https://presearch.io/searchapi)

> **🎯 Flagship Prompt:** *"Search for latest advancements in autonomous AI agents"*

**🔍 Privacy-first decentralized web search for AI agents, local LLMs, and autonomous systems.**

This production-ready skill enables real-time internet access for AI agents using Presearch's decentralized infrastructure - no tracking, no censorship, no centralized control.

## ✨ Key Features

- **🔒 Privacy-First**: Zero tracking, zero profiling, complete anonymity
- **🌐 Decentralized**: Powered by community nodes worldwide
- **⚡ Real-time**: Live web search with structured JSON responses
- **🤖 AI-Optimized**: Designed specifically for autonomous agents
- **🛡️ Uncensored**: No content filtering or search manipulation
- **🚀 Production-Ready**: Rate limiting, error handling, exponential backoff

## 🚀 Quick Start

### 1. Get Your API Key
To obtain a Search API Key, please email **`collaborate@presearch.com`**.
*Tip: You can also [Sign up at Presearch](https://presearch.com/signup?rid=4779685) to create your main account.*

### 2. Installation
```bash
git clone https://github.com/NosytLabs/presearch-search-skill.git
cd presearch-search-skill
export PRESEARCH_API_KEY="your_api_key_here"
```

### 3. Run Your First Search
**Python:**
```bash
python3 presearch_python.py "latest AI agent developments"
```

**Node.js:**
```bash
node presearch_nodejs.js "decentralized AI search"
```

## 📊 Real Results & Performance

### 🎯 Flagship Prompt Results
Our flagship prompt *"Search for latest advancements in autonomous AI agents"* returns:

```json
{
  "results": [
    {
      "title": "Helping AI agents search to get the best results out of large language models",
      "link": "https://news.mit.edu/2026/helping-ai-agents-search-to-get-best-results-from-llms-0205",
      "description": "Feb 5, 2026 · EnCompass executes AI agent programs by backtracking and making multiple attempts..."
    },
    {
      "title": "A Comprehensive Review of AI Agents: Transforming ...",
      "link": "https://arxiv.org/html/2508.11957v1",
      "description": "Aug 16, 2025 · AI agents have rapidly evolved from specialized, rule-based programs to versatile, learning-driven autonomous systems..."
    },
    {
      "title": "Advancements in AI Agents: A Review of Recent Developments in early 2025",
      "link": "https://medium.com/@tanaby.mofrad/advancements-in-ai-agents-a-review-of-recent-developments-in-early-2025-8ab0f57c5d20",
      "description": "Jul 11, 2025 · This article aims to provide a comprehensive review of significant advancements in AI agents..."
    }
  ]
}
```

### ⚡ Advanced Features Demo Results
Our comprehensive testing shows consistent performance across all search types:

| Search Type | Results Found | Top Result | Response Time |
|-------------|---------------|------------|---------------|
| **Latest Tech News** (24h) | 11 results | MIT Technology Review | < 2s |
| **Bitcoin Trends** (30d) | 7 results | YCharts Historical Data | < 2s |
| **Local Weather** (SF) | 13 results | Weather.com | < 2s |
| **Linux Kernel** (unfiltered) | 13 results | Unix StackExchange | < 2s |
| **Python Tutorials** (Page 2) | 13 results | Reddit LearnPython | < 2s |

## 💰 Search Plans & Pricing

All users can get started by signing up for the free plan. Paid plans offer higher throughput for production applications.

| Plan | Queries / Second | Queries / Month | Description |
| :--- | :--- | :--- | :--- |
| **Free** | 1 query/second | 2,500 queries/mo | Perfect for testing and development |
| **P1** | 30 queries/second | 5,000 queries/mo | For growing applications |
| **P2** | 60 queries/second | 5,000 queries/mo | High-performance needs |
| **Enterprise** | Unlimited | Unlimited | Custom solutions for large scale |

*For custom enterprise limits or higher volume needs, contact `collaborate@presearch.com`.*

## 💡 Perfect for These Use Cases

### 🤖 Autonomous AI Agents
- Real-time information gathering
- Market research and analysis
- Fact-checking and verification
- Trend identification

### 👨‍💻 Development & Coding
- Documentation discovery
- Error troubleshooting
- Library and framework research
- Stack Overflow alternatives

### 📊 Business Intelligence
- Competitor analysis
- Market trend monitoring
- News and sentiment tracking
- Investment research

### 🔬 Academic Research
- Scientific paper discovery
- Technical documentation
- Educational resource finding
- Citation research

## 🎯 Example Agent Prompts

### General Intelligence
- *"Search for breakthrough developments in quantum computing 2026"*
- *"Find the latest research on AI safety and alignment"*
- *"Search for emerging cryptocurrency trends this month"*

### Technical Research
- *"Search for official Python 3.12 documentation and new features"*
- *"Find GitHub repositories for autonomous AI agent frameworks"*
- *"Search for solutions to CUDA out of memory errors"*

### Market Analysis
- *"Search for NVIDIA stock performance and GPU releases 2026"*
- *"Find competitors to Presearch decentralized search engine"*
- *"Search for trending SaaS startup ideas and funding"*

### Real-time Information
- *"Search for current weather in San Francisco"*
- *"Find today's technology news headlines"*
- *"Search for live cryptocurrency prices and market cap"*

## 📋 API Reference

### Authentication
```http
GET https://na-us-1.presearch.com/v1/search
Authorization: Bearer YOUR_API_KEY
```

### Parameters
| Parameter | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `q` | string | ✅ | - | Search query (URL encoded) |
| `ip` | string | ✅ | 127.0.0.1 | User IP for geolocation |
| `location` | JSON | ❌ | - | GPS coordinates: `{"lat": 37.77, "long": -122.41}` |
| `lang` | string | ❌ | en-US | Language: `en-US`, `es-ES`, `de-DE`, etc. |
| `time` | enum | ❌ | any | Filter: `any`, `day`, `week`, `month`, `year` |
| `page` | integer | ❌ | 1 | Pagination (1-100) |
| `safe` | enum | ❌ | 1 | Safe search: `1` (on), `0` (off) |

### Response Format
```json
{
  "results": [
    {
      "title": "Page Title",
      "link": "https://example.com",
      "description": "Page description...",
      "favicon": "https://example.com/favicon.ico"
    }
  ],
  "pagination": {
    "current_page": 1,
    "has_next": true
  }
}
```

## ⚡ Advanced Features

### 📍 Location-Based Search
```python
# Search for local restaurants in San Francisco
response = skill.search("best restaurants", location='{"lat": 37.77, "long": -122.41}')
```

### 📅 Time-Based Filtering
```python
# Search for news from the last 24 hours
response = skill.search("technology news", time_filter="day")

# Search for developments this month
response = skill.search("AI breakthroughs", time_filter="month")
```

### 🔍 Pagination Support
```python
# Get multiple pages of results
for page in range(1, 4):
    response = skill.search("machine learning", page=page)
    process_results(response.results)
```

## 🛡️ Rate Limits & Best Practices

### Free Tier Limits
- **1 query per second** (60 queries/minute)
- **2,500 queries per month**
- Automatic exponential backoff for 429 errors

### Production Recommendations
- Implement caching for repeated queries
- Use appropriate time filters to reduce load
- Batch similar searches when possible
- Monitor your usage patterns

## 🔧 Integration Examples

### Python Integration
```python
from presearch_python import PresearchSkill
import os

# Initialize with your API key
skill = PresearchSkill(os.getenv("PRESEARCH_API_KEY"))

# Search with advanced parameters
results = skill.search(
    query="latest AI developments",
    lang="en-US",
    time_filter="week",
    page=1
)

# Process results
for result in results.results:
    print(f"Title: {result.title}")
    print(f"URL: {result.link}")
    print(f"Description: {result.description}")
```

### Node.js Integration
```javascript
import { PresearchSkill } from './presearch_nodejs.js';

const skill = new PresearchSkill(process.env.PRESEARCH_API_KEY);

// Search with options
const results = await skill.search({
  query: "decentralized search engines",
  lang: 'en-US',
  time: 'month',
  page: 1
});

// Handle results
results.results.forEach(result => {
  console.log(`Title: ${result.title}`);
  console.log(`URL: ${result.link}`);
  console.log(`Description: ${result.description}`);
});
```

## 🌍 Why Decentralized Search Matters

### 🚫 Problems with Traditional Search
- **Surveillance capitalism**: Your searches are tracked and monetized
- **Algorithmic bias**: Results manipulated for profit
- **Censorship**: Content filtered without transparency
- **Data harvesting**: Personal information collected and sold

### ✅ Presearch Advantages
- **Privacy by design**: No tracking, no profiling, no data collection
- **Community governance**: Decentralized node network
- **Transparent algorithms**: Open-source and auditable
- **Censorship resistant**: No central authority controlling results
- **Reward participation**: Earn PRE tokens for using the network

## 🤝 Compatible With

- **🏗️ Agent Frameworks**: AutoGPT, LangChain, CrewAI
- **🧠 Local LLMs**: Llama 2, GPT-4, Claude, Mistral
- **⚙️ Orchestration**: n8n, Zapier, Make.com
- **🔧 Development**: Python, Node.js, Go, Rust
- **🐳 Deployment**: Docker, Kubernetes, serverless

## 🌟 Community & Support

### 📱 Connect With Presearch
- **🌐 Website**: [presearch.com](https://presearch.com/signup?rid=4779685)
- **💬 Discord**: [discord.gg/presearch](https://discord.gg/presearch)
- **📱 Telegram**: [t.me/presearch](https://t.me/presearch)
- **🐦 Twitter**: [@presearchnews](https://twitter.com/presearchnews)
- **📺 YouTube**: [Presearch Channel](https://youtube.com/c/Presearch)
- **💼 LinkedIn**: [Presearch LinkedIn](https://linkedin.com/company/presearch)
- **📖 Medium**: [Presearch Blog](https://medium.com/@presearch)

### 🆘 Support
- **📧 Email**: collaborate@presearch.com
- **📚 Docs**: [Official Documentation](https://docs.presearch.io)
- **🐛 Issues**: [GitHub Issues](https://github.com/NosytLabs/presearch-search-skill/issues)
- **💬 Community**: [Presearch Discord](https://discord.gg/presearch)

## 📄 License

**MIT License** - See [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Presearch Team** for building decentralized search infrastructure
- **Community Nodes** for powering the decentralized network
- **Open Source Contributors** for making this skill possible

---

<div align="center">

**⭐ Star this repo if you find it useful!**

[**🚀 Get Started with Presearch**](https://presearch.com/signup?rid=4779685) | [**📖 Read the Docs**](https://docs.presearch.io) | [**💬 Join Discord**](https://discord.gg/presearch)

*Built with ❤️ for the decentralized future*

</div>