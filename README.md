# 🔴 TRON Ecosystem Docs (Markdown Archive)

![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)
![TRON](https://img.shields.io/badge/Network-TRON-red.svg)
![Docs](https://img.shields.io/badge/Docs-Markdown-success.svg)

Welcome! This repository contains the complete TRON Network developer documentation, API references, and DeFi ecosystem guides, scraped and converted entirely into clean **Markdown (.md)** format. With over 2,500 files, this is the ultimate offline knowledge base for the TRON blockchain.

## 🎯 Why does this exist?
The official TRON documentation is scattered across multiple platforms (ReadMe, Docusaurus, VuePress, MkDocs, JavaDoc). Feeding raw HTML or PDFs into Large Language Models (LLMs) or AI contexts (like Google AI Studio or ChatGPT) is noisy, expensive, and inefficient. 

This repo provides pure, structured, text-only Markdown files. It is highly optimized for:
* Feeding context to AI agents, coding assistants, and RAG pipelines.
* Developers building Web3 applications, smart contracts, and dApps.
* Reading offline in your favorite terminal editor.

## 🏗️ Ecosystems Included
This archive aggregates and standardizes documentation from the core pillars of the TRON network:

* **`tron_docs_md/` (Core Protocol):** TVM rules, opcodes, energy/bandwidth mechanisms, and protocol-level transaction anatomy.
* **`sun_docs_md/` (SUN.io):** Smart contracts, liquidity pool mechanics, V4 routing, and swap logic.
* **`justlend_docs_md/` (JustLend DAO):** Interest rate models, liquidation mechanisms, and lending architecture.
* **`winklink_docs_md/` (WINkLink):** Price feed integration and Oracle mechanics.
* **`tronweb_docs_md/` (TronWeb):** Complete JavaScript/TypeScript SDK API reference for signing and broadcasting transactions.
* **`tronbox_docs_md/` (TronBox):** TRON's framework for compiling, testing, and deploying smart contracts.
* **`trident_docs_md/` (Trident Java SDK):** Complete JavaDoc and guides for the Trident SDK.
* **`tronscan_mcp_docs_md/` (TronScan MCP):** Model Context Protocol (MCP) skills allowing AI agents to query on-chain data natively.

## ⚙️ Methodology & How to Update
Originally started as a manual scraping project using browser extensions, this repository is now fully automated. The data is extracted using custom Python scrapers designed to bypass dynamic rendering and convert HTML directly into semantic Markdown using `markdownify`.

If you need to update the documentation to the latest versions, you can re-run the crawlers locally:

1. Install dependencies:
```bash
pip install requests beautifulsoup4 markdownify

```

2. Execute the desired crawler:

```bash
python tronweb_crawler.py

```

*(Crawlers are available in the root directory for all included ecosystems).*

## 🤝 Contributing

This project is open-source, and community help is highly appreciated! If you are a developer and want to improve this repository, you are more than welcome to contribute.

How to help:

1. Fix broken tables or poorly formatted markdown from the raw scraping.
2. Add crawlers for missing TRON ecosystem projects.
3. Keep the documentation up to date with new official releases.

**Feel free to open a Pull Request (PR) with your improvements!**

---

*Maintained by hiddengogeta.*
