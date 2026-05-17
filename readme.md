# 🌍 OmniSEO-Agent: Cross-border E-commerce SEO Content Workflow

基于大语言模型（LLM）与多智能体（Multi-Agent）协同架构的跨境电商多语言 SEO 内容自动生成引擎。

## 📖 项目简介
本项目专为跨境电商场景设计。它能够自动抓取竞品网页提取核心卖点，结合预设的品牌语调（Tone of Voice）和特定 SEO 关键词，自动化批量生成高质量的多语言商品详情页（Listing / Blog）。

系统内置了 **Actor-Critic（生成-评估）双模型架构**，生成的内容必须经过 Critic 模型的严苛打分验证（涵盖查重、SEO 密度、品牌一致性），不达标则自动触发重写闭环，确保最终产出的内容质量。现已成功接管十余个独立站的内容引擎。

## ✨ 核心特性
- **🕸️ 智能竞品分析 (Scraper Agent)**: 自动绕过基础反爬，提取竞品网页中的参数与用户痛点。
- **✍️ 品牌定制化生成 (Generator Agent)**: 深度融合品牌语调与指定 SEO 关键词，支持长文本流式生成。
- **⚖️ 质量评审闭环 (Critic Agent)**: 内置打分机制，对流畅度、SEO 合规性进行自检与自动重写。
- **🌐 多语言矩阵**: 一键生成 EN/ES/FR/DE/JA 等多国本地化语言文案。

## 🚀 快速开始
1. 克隆本仓库
2. 安装依赖: `pip install -r requirements.txt`
3. 复制 `.env.example` 为 `.env` 并填入您的 API Key
4. 配置 `config.yaml` 中的业务参数
5. 运行主程序: `python main.py`
