# Decentralized Search Skill for AI Agents

[![Presearch](https://assets.presearch.com/referral/ban-5.jpg)](https://presearch.com/signup?rid=4779685)

> **Flagship Prompt:** "Search for latest advancements in autonomous AI agents"

**Enable AI agents, local LLMs, and autonomous systems to perform real-time decentralized web searches using Presearch.**

This skill provides a simple, reliable interface for retrieving live internet results, allowing agents to access current information beyond their training data.

[**View on ClawHub**](https://clawhub.ai/u/NosytLabs)

---

## ⚡ Quick Start

1.  **Get API Key**: [Sign up at Presearch](https://presearch.com/signup?rid=4779685) & email `collaborate@presearch.com` for access.
2.  **Clone**: `git clone https://github.com/NosytLabs/presearch-search-skill`
3.  **Run**:
    ```bash
    export PRESEARCH_API_KEY="your_key"
    python3 presearch_python.py "latest AI news"
    ```

---

## 📖 Overview

Most AI agents and local language models lack native access to real-time internet search. This skill solves that limitation by connecting agents directly to Presearch, enabling:

-   **Real-time web search**
-   **Autonomous research**
-   **Live data retrieval**
-   **Technical documentation discovery**
-   **Market and business intelligence**

This allows agents to operate with current, real-world knowledge while preserving privacy through decentralized infrastructure.

## ✨ Features

-   **Real-time decentralized web search**
-   **Agent-compatible structured responses**
-   **Lightweight and fast integration**
-   **No centralized search dependency**
-   **Compatible with autonomous agent frameworks**
-   **Works with local LLMs and cloud agents**

## 💡 Example Prompts

These prompts demonstrate how agents can use the skill:

### General Search
-   *"Search for latest advancements in autonomous AI agents"*
-   *"Search for official documentation for FastAPI Python framework"*

### Programming Assistance
-   *"Search for how to fix Python ModuleNotFoundError requests"*
-   *"Search for GitHub repositories for local LLM agents"*

### Autonomous Research
-   *"Search for trending SaaS startup ideas in 2026"*
-   *"Search for best open-source AI agent frameworks"*

### Crypto and Blockchain
-   *"Search for latest Solana ecosystem projects"*
-   *"Search for Pump.fun token launch tutorial"*

### Technology and Market Intelligence
-   *"Search for latest NVIDIA GPU releases"*
-   *"Search for competitors of Presearch search engine"*

## 🚀 Use Cases

This skill enables powerful agent capabilities:

1.  **Autonomous AI Research**: Agents can gather real-time information from the internet.
2.  **Coding Assistants**: Agents can find documentation, debug errors, and locate resources.
3.  **Local LLM Internet Access**: Local models gain real-time search capabilities.
4.  **Market Intelligence**: Agents can analyze trends, competitors, and opportunities.
5.  **Autonomous Decision Making**: Agents can research before executing tasks.

## 🔧 Installation & Usage

### 1. Get an API Key
Sign up at [Presearch.com](https://presearch.com/signup?rid=4779685) and request API access (`collaborate@presearch.com`).

### 2. Install the Skill
Clone the repository:
```bash
git clone https://github.com/NosytLabs/presearch-search-skill
cd presearch-search-skill
```

### 3. Configure Environment
Set your API key:
```bash
export PRESEARCH_API_KEY="your_api_key_here"
```

### 4. Run the Skill
**Python:**
```bash
python3 presearch_python.py "latest AI agents"
```

**Node.js:**
```bash
node presearch_nodejs.js "decentralized search"
```

**Advanced Demo:**
Check out `example.py` for advanced usage (filters, location, pagination).
```bash
python3 example.py
```

## 📋 API Overview

-   **Endpoint**: `https://na-us-1.presearch.com/v1/search`
-   **Method**: `GET`
-   **Auth**: Bearer Token
-   **Docs**: [Official Documentation](https://presearch.io/searchapi)

### Parameters

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `q` | string | ✅ | - | Search query (URL encoded) |
| `ip` | string | ✅ | 127.0.0.1 | User IP (required by API). Use `127.0.0.1` if unknown. |
| `location` | string | ❌ | - | JSON string: `{"lat": 37.77, "long": -122.41}` |
| `lang` | string | ❌ | en-US | Language code (e.g., `en-US`, `de-DE`) |
| `time` | enum | ❌ | any | `any`, `day`, `week`, `month`, `year` |
| `page` | integer | ❌ | 1 | Page number (1-100) |
| `safe` | enum | ❌ | 1 | `1` (strict), `0` (off) |

## 🌍 Why Decentralized Search?

Using Presearch provides:
-   **Open and decentralized infrastructure**
-   **No restrictive API barriers**
-   **Reliable and consistent search access**
-   **Agent-friendly integration**

This makes it ideal for autonomous systems that prioritize privacy and censorship resistance.

## 🤝 Compatibility

This skill works with:
-   Autonomous AI agents
-   Local LLM frameworks
-   Agent orchestration systems
-   Custom AI assistants
-   Automation workflows

## 🔮 Future Improvements

-   Structured result parsing
-   Multi-query execution
-   Result ranking optimization
-   Integration with agent memory systems

## 📄 License

MIT License

---

[**Sign up for Presearch**](https://presearch.com/signup?rid=4779685) to start searching privately.